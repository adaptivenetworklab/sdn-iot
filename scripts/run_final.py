"""Driver for the final V2 sweep (protocol v2 section 7.2). Frozen with the protocol.

    python scripts/run_final.py                 # the real sweep: test split, 20 seeds
    python scripts/run_final.py --dry           # print the queue, run nothing
    python scripts/run_final.py --eval-phase val --steps 4096 --seeds 3 \
        --out results/smoke/final-dryrun        # end-to-end rehearsal, never touches test

Cells: 4 learners x {full, real_only, aug_subsample} x safety {on, off}; 4 heuristics
x safety on/off (arm full); sdhppo no_dueling x on/off; residual and BC-init sdhppo
x on/off. Each learner runs the configuration selected on val in results/tuning-v2
(selection.csv, argmin of mean val violation); no_dueling and the augmentation arms
reuse their learner's configuration.

Every run gets the same seeds 0..N-1, so seed i is the same environment realisation
for every method (K2, scripts/check_crn.py).

Resume: a run is skipped when its eval CSV already exists. A failed run is retried
once with the identical command and both attempts are logged in failures.log.
Before starting, the driver refuses to run on uncommitted changes under scripts/ or
in the protocol, so the git hash that train_online.py stores in every run's JSON
is the code that actually ran.
"""

import argparse
import ctypes
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
SELECTION = REPO_ROOT / "results" / "tuning-v2" / "selection.csv"
PROTOCOL = "docs/experiments/07-protocol-v2.md"
LEARNERS = ("ppo", "sdhppo", "dqn", "ddqn")
HEURISTICS = ("demand_prop", "no_control", "equal_split", "threshold")
RESIDUAL_ARMS = {"ressdhppo": ["--residual", "on"], "bcsdhppo": ["--actor-init", "bc"]}


def config_args(cfg):
    """Selected tuning directory name -> train_online.py flags."""
    m = re.fullmatch(r"lr([\de.-]+)_ent([\d.]+)_(clip|tanh)_rs([\d.]+)", cfg)
    if m:
        return ["--lr", m[1], "--ent-coef", m[2], "--action-param", m[3], "--reward-scale", m[4]]
    m = re.fullmatch(r"lr([\de.-]+)_ts(\d+)_b(\d+)_ed(\d+)", cfg)
    if m:
        return ["--lr", m[1], "--target-sync", m[2], "--bins", m[3], "--eps-decay", m[4],
                "--reward-scale", "19.0106"]
    raise SystemExit(f"cannot parse configuration {cfg!r}")


def selected():
    sel = pd.read_csv(SELECTION)
    return {arm: g.loc[g.viol_mean.idxmin(), "config"] for arm, g in sel.groupby("arm")}


def cells():
    """(cell_dir, algo, extra flags) for every cell of the design."""
    cfg = selected()
    out = []
    for s in ("on", "off"):
        for algo in LEARNERS:
            for arm in ("full", "real_only", "aug_subsample"):
                out.append((f"{algo}_{arm}_safety{s}", algo,
                            ["--arm", arm, "--safety", s] + config_args(cfg[algo])))
        out.append((f"sdhppo_no_dueling_safety{s}", "sdhppo",
                    ["--arm", "no_dueling", "--safety", s] + config_args(cfg["sdhppo"])))
        for name, flags in RESIDUAL_ARMS.items():
            out.append((f"{name}_full_safety{s}", "sdhppo",
                        ["--arm", "full", "--safety", s] + config_args(cfg[name]) + flags))
        for algo in HEURISTICS:
            out.append((f"{algo}_full_safety{s}", algo,
                        ["--arm", "full", "--safety", s, "--reward-scale", "19.0106"]))
    return out


def git(*a):
    return subprocess.check_output(["git", *a], cwd=REPO_ROOT, text=True).strip()


def keep_awake(on):
    """Stop Windows from sleeping mid-sweep; a power loss already cost one batch."""
    if sys.platform == "win32":
        ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if on else 0))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "final-v2")
    p.add_argument("--seeds", type=int, default=20)
    p.add_argument("--steps", type=int, default=300_000)
    p.add_argument("--parallel", type=int, default=12)
    p.add_argument("--eval-phase", default="test", choices=["val", "test"])
    p.add_argument("--dry", action="store_true")
    a = p.parse_args()

    common = ["--phase", "train", "--eval-phase", a.eval_phase, "--device", "cpu",
              "--steps", str(a.steps), "--episode-len", "50", "--eval-every", "25000",
              "--probe-episodes", "20", "--eval-episodes", "20", "--random-init-alloc",
              "--capacity", "12.0", "--eval-scenario", "diurnal", "--eval-scenario", "flash"]
    if a.steps < 25_000:                     # rehearsal: still probe twice
        common[common.index("--eval-every") + 1] = str(max(a.steps // 2, 1))
    if a.eval_phase == "test":
        common.append("--allow-test")

    jobs = []
    for cell, algo, extra in cells():
        d = a.out / cell
        for s in range(a.seeds):
            if list(d.glob(f"*_seed{s}_eval.csv")) or list(d.glob(f"*_seed{s}_*_eval.csv")):
                continue
            jobs.append([sys.executable, "scripts/train_online.py", "--algo", algo,
                         "--seed", str(s), "--out", str(d)] + common + extra)
    print(f"{len(cells())} cells x {a.seeds} seeds; {len(jobs)} runs queued -> {a.out}")
    if a.dry:
        for j in jobs:
            print(" ".join(j[1:]))
        return
    if not jobs:
        return

    dirty = git("status", "--porcelain", "--", "scripts", PROTOCOL)
    if dirty and a.eval_phase == "test":
        raise SystemExit(f"uncommitted changes, refusing to run the final sweep:\n{dirty}")

    a.out.mkdir(parents=True, exist_ok=True)
    manifest = {"started_utc": datetime.now(timezone.utc).isoformat(),
                "git_commit": git("rev-parse", "HEAD"),
                "git_describe": git("describe", "--tags", "--always"), "seeds": a.seeds,
                "steps": a.steps, "eval_phase": a.eval_phase, "parallel": a.parallel,
                "n_cells": len(cells()), "queued": len(jobs), "selected": selected()}
    (a.out / f"manifest_{int(time.time())}.json").write_text(json.dumps(manifest, indent=2))

    log = (a.out / "run.log").open("a", encoding="utf-8")
    fails = a.out / "failures.log"

    def run(cmd):
        for attempt in (1, 2):
            r = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
            if r.returncode == 0:
                lines = r.stdout.strip().splitlines()
                return cmd, attempt, lines[-1] if lines else ""
            with fails.open("a", encoding="utf-8") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} attempt {attempt} rc "
                        f"{r.returncode}: {' '.join(cmd[1:])}\n{r.stderr[-2000:]}\n")
        return cmd, None, "FAILED twice: " + " ".join(cmd[1:])

    keep_awake(True)
    done = 0
    try:
        with ThreadPoolExecutor(max_workers=a.parallel) as ex:
            for fut in as_completed([ex.submit(run, j) for j in jobs]):
                cmd, attempt, last = fut.result()
                done += 1
                tag = "" if attempt == 1 else (" (RETRIED)" if attempt else " (FAILED)")
                log.write(f"[{done}/{len(jobs)}] {last}{tag}\n")
                log.flush()
    finally:
        keep_awake(False)
    log.write(f"SWEEP DONE {datetime.now(timezone.utc).isoformat()}\n")
    log.close()
    print(f"done; log at {a.out / 'run.log'}")


if __name__ == "__main__":
    main()
