"""Driver for the V3 sweep (docs/experiments/09-protocol-v3.md, sections 3, 4, 10, 11).

Operational tooling only: it runs exactly the cells and seeds the protocol fixes
and adds no cell, seed, arm, scenario or hyperparameter. Helpers are reused from
the frozen V2 driver (scripts/run_final.py: config_args, selected, git,
keep_awake) without modifying it.

Cells (seeds 20-39, test split, 300k steps, diurnal and flash evaluated):
  block A  dqn, ddqn x {aug_subsample, full, real_only} safety off;
           dqn, ddqn aug_subsample safety on; demand_prop (full) safety off and on
  block B  dqn, ddqn x {var_matched, moment_matched} safety off
240 learning runs and 40 heuristic runs, each through scripts_v3/run_v3.py.

Safeguards:
- refuses to start on uncommitted changes under scripts/ or scripts_v3/ or in the
  protocol, or when HEAD does not contain the tag protocol-v3-final;
- every finished run's arguments are compared with the V2 run of the same cell
  (seed 0; new arms against real_only): any difference other than seed, out
  and arm stops new launches and is logged as ARGS MISMATCH;
- resume: a run whose eval CSV exists is skipped; a crashed run is retried once
  with the identical command (protocol section 10, item 2), both attempts logged;
- each worker is opted out of Windows power throttling (speed only, no effect on
  results); the opt-out ends with the process.

    python scripts_v3/run_sweep_v3.py            # the sweep
    python scripts_v3/run_sweep_v3.py --dry      # print the queue only
"""
import argparse
import ctypes
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from run_final import config_args, git, keep_awake, selected  # noqa: E402

PROTOCOL = "docs/experiments/09-protocol-v3.md"
TAG = "protocol-v3-final"
SEEDS = range(20, 40)
OUT = ROOT / "results" / "v3"
V2 = ROOT / "results" / "final-v2"
COMMON = ["--phase", "train", "--eval-phase", "test", "--allow-test", "--device", "cpu",
          "--steps", "300000", "--episode-len", "50", "--eval-every", "25000",
          "--probe-episodes", "20", "--eval-episodes", "20", "--random-init-alloc",
          "--capacity", "12.0", "--eval-scenario", "diurnal", "--eval-scenario", "flash"]


def cells():
    """(cell_dir, algo, arm, safety) of every V3 cell, protocol section 4."""
    out = [("demand_prop_full_safety" + s, "demand_prop", "full", s) for s in ("off", "on")]
    for algo in ("ddqn", "dqn"):
        out += [(f"{algo}_{arm}_safetyoff", algo, arm, "off")
                for arm in ("aug_subsample", "full", "real_only", "var_matched", "moment_matched")]
        out.append((f"{algo}_aug_subsample_safetyon", algo, "aug_subsample", "on"))
    return out


def job(cfg, cell, algo, arm, safety, seed):
    extra = (["--reward-scale", "19.0106"] if algo == "demand_prop" else config_args(cfg[algo]))
    return [sys.executable, str(ROOT / "scripts_v3" / "run_v3.py"), "--algo", algo,
            "--arm", arm, "--safety", safety, "--seed", str(seed), "--out", str(OUT / cell),
            *COMMON, *extra]


def v2_reference(cell, algo, arm, safety):
    ref_arm = "real_only" if arm in ("var_matched", "moment_matched") else arm
    f = V2 / f"{algo}_{ref_arm}_safety{safety}" / f"{algo}_{ref_arm}_train_safety{safety}_seed0.json"
    return json.loads(f.read_text(encoding="utf-8"))["args"]


def args_mismatch(cell, algo, arm, safety, seed):
    stem = f"{algo}_{arm}_train_safety{safety}_seed{seed}"
    new = json.loads((OUT / cell / f"{stem}.json").read_text(encoding="utf-8"))["args"]
    ref = v2_reference(cell, algo, arm, safety)
    return sorted(k for k in set(ref) | set(new)
                  if k not in ("seed", "out", "arm") and ref.get(k) != new.get(k))


def opt_out_throttling(pid):
    if sys.platform != "win32":
        return
    class PPT(ctypes.Structure):
        _fields_ = [("Version", ctypes.c_ulong), ("ControlMask", ctypes.c_ulong),
                    ("StateMask", ctypes.c_ulong)]
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.OpenProcess.restype = ctypes.c_void_p
    h = k32.OpenProcess(0x0200, False, pid)            # PROCESS_SET_INFORMATION
    if h:
        s = PPT(1, 0x1 | 0x4, 0)                         # EXECUTION_SPEED | IGNORE_TIMER, state 0
        k32.SetProcessInformation(ctypes.c_void_p(h), 4, ctypes.byref(s), ctypes.sizeof(s))
        k32.CloseHandle(ctypes.c_void_p(h))


def oplog(msg):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "operations.log").open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')}  {msg}\n")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--parallel", type=int, default=14)
    p.add_argument("--dry", action="store_true")
    a = p.parse_args()

    cfg = selected()
    queue = []
    for cell, algo, arm, safety in cells():
        for seed in SEEDS:
            if (OUT / cell / f"{algo}_{arm}_train_safety{safety}_seed{seed}_eval.csv").exists():
                continue
            queue.append(((cell, algo, arm, safety, seed), job(cfg, cell, algo, arm, safety, seed)))
    print(f"{len(cells())} cells x {len(SEEDS)} seeds; {len(queue)} runs queued -> {OUT}")
    if a.dry:
        for _, cmd in queue:
            print(" ".join(cmd[2:]))
        return
    if not queue:
        return

    dirty = git("status", "--porcelain", "--", "scripts", "scripts_v3", PROTOCOL)
    if dirty:
        raise SystemExit(f"uncommitted changes, refusing to run the V3 sweep:\n{dirty}")
    if subprocess.run(["git", "merge-base", "--is-ancestor", TAG, "HEAD"], cwd=ROOT).returncode:
        raise SystemExit(f"HEAD does not contain tag {TAG}; refusing to run")

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"started_utc": datetime.now(timezone.utc).isoformat(),
                "git_commit": git("rev-parse", "HEAD"),
                "git_describe": git("describe", "--tags", "--always"),
                "seeds": [SEEDS.start, SEEDS.stop - 1], "parallel": a.parallel,
                "n_cells": len(cells()), "queued": len(queue), "selected": cfg}
    (OUT / f"manifest_{int(time.time())}.json").write_text(json.dumps(manifest, indent=2))
    oplog(f"Sweep started: run_sweep_v3.py --parallel {a.parallel}, {len(queue)} runs queued, "
          f"commit {manifest['git_commit'][:7]} ({manifest['git_describe']}); "
          f"power-throttling opt-out per worker.")

    stop = threading.Event()
    log = (OUT / "run.log").open("a", encoding="utf-8")
    fails = OUT / "failures.log"

    def run(key, cmd):
        if stop.is_set():
            return key, None, "SKIPPED (sweep stopped)"
        for attempt in (1, 2):
            proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)
            opt_out_throttling(proc.pid)
            out, err = proc.communicate()
            if proc.returncode == 0:
                bad = args_mismatch(*key)
                if bad:
                    stop.set()
                    return key, attempt, f"ARGS MISMATCH {bad}"
                lines = out.strip().splitlines()
                return key, attempt, lines[-2] if len(lines) > 1 else (lines[-1] if lines else "")
            with fails.open("a", encoding="utf-8") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} attempt {attempt} rc "
                        f"{proc.returncode}: {' '.join(cmd[2:])}\n{err[-2000:]}\n")
        return key, None, "FAILED twice: " + " ".join(cmd[2:])

    keep_awake(True)
    done = 0
    try:
        with ThreadPoolExecutor(max_workers=a.parallel) as ex:
            for fut in as_completed([ex.submit(run, k, c) for k, c in queue]):
                key, attempt, last = fut.result()
                done += 1
                tag = "" if attempt == 1 else (" (RETRIED)" if attempt else " (FAILED)")
                log.write(f"[{done}/{len(queue)}] {datetime.now(timezone.utc).strftime('%H:%MZ')} "
                          f"{last}{tag}\n")
                log.flush()
    finally:
        keep_awake(False)
    end = "SWEEP STOPPED (ARGS MISMATCH)" if stop.is_set() else "SWEEP DONE"
    log.write(f"{end} {datetime.now(timezone.utc).isoformat()}\n")
    log.close()
    oplog(f"{end}: {done} runs reported.")
    print(f"{end}; log at {OUT / 'run.log'}")


if __name__ == "__main__":
    main()
