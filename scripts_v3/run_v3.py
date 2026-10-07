"""V3 wrapper around the frozen V2 trainer (scripts/train_online.py).

Every argument is passed to train_online.main() unchanged. The wrapper adds two
things without editing any V2 file:

1. Checkpoint persistence. V2 keeps the best-on-val weights only in memory
   (train_online.py:400, 406-407, 495-498). After main() returns, the network the
   final policy closes over (`actor` for the PPO family, `q` for the DQN family)
   holds exactly those weights; it is saved with torch.save to
   results/v3/checkpoints/<run_id>.pt, next to <run_id>.json with the full run
   metadata. run_id = <output dir name>__<V2 file stem>.

2. Data arms `var_matched` and `moment_matched` (protocol v3, section 4). Only
   these arms go through the override of split_arrivals; every other arm calls
   the V2 function untouched. Both use the 613 real train rows and rescale each
   port's deviation from its train mean by sigma_s / sigma_r, the std ratio of
   the synthetic trace data/synth/train_synth_trace.csv (attempt 1) to the real
   train rows:
       var_matched:    x' = mu_r + (x - mu_r) * sigma_s / sigma_r
       moment_matched: x' = mu_s + (x - mu_r) * sigma_s / sigma_r
   Values below 0 are clipped to 0 and counted. Statistics come from the real
   train rows and the synthetic trace only, never from val or test.

    python scripts_v3/run_v3.py <train_online.py arguments...>
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import train_online as T  # noqa: E402

VAR_ARM = "var_matched"
# arm -> whose per-port mean the rescaled rows keep
MATCHED_ARMS = {VAR_ARM: "real", "moment_matched": "synth"}
SYNTH = ROOT / "data" / "synth" / "train_synth_trace.csv"
SYNTH_ATTEMPT1 = ROOT / "data" / "synth" / "train_synth_trace_attempt1.csv"
CKPT_DIR = ROOT / "results" / "v3" / "checkpoints"

CAPTURED = {}       # network behind the returned policy, filled by the run_* wrappers
VAR_INFO = {}       # matched-arm statistics of the current run


def load_synth():
    """Synthetic train trace; refuses anything but generator attempt 1 (07:545-546)."""
    if SYNTH.read_bytes() != SYNTH_ATTEMPT1.read_bytes():
        raise SystemExit(f"{SYNTH} is not generator attempt 1")
    return pd.read_csv(SYNTH).to_numpy(dtype=float)


def matched(train_real, synth, mean_from):
    """Real train rows with per-port deviations rescaled to the synthetic std.

    mean_from = "real" keeps the real train mean (var_matched), "synth" moves it
    to the synthetic mean (moment_matched). Both arrays have 613 rows, so the
    std ratio is the same for ddof 0 and 1; numpy's default (ddof 0) is used.
    """
    mean = train_real.mean(axis=0)
    target = mean if mean_from == "real" else synth.mean(axis=0)
    scale = synth.std(axis=0) / train_real.std(axis=0)
    out = target + (train_real - mean) * scale
    neg = out < 0.0
    info = {"mean_from": mean_from, "rows": int(len(out)), "train_mean": mean.tolist(),
            "synth_mean": synth.mean(axis=0).tolist(), "target_mean": target.tolist(),
            "train_std": train_real.std(axis=0).tolist(), "synth_std": synth.std(axis=0).tolist(),
            "scale": scale.tolist(), "clipped_values_per_port": neg.sum(axis=0).tolist(),
            "clipped_rows": int(neg.any(axis=1).sum())}
    return np.clip(out, 0.0, None), info


_v2_split_arrivals = T.split_arrivals


def var_matched(train_real, synth):
    return matched(train_real, synth, "real")


def split_arrivals(full_trace, args):
    if args.arm not in MATCHED_ARMS:
        return _v2_split_arrivals(full_trace, args)
    # Same split and guards as the V2 real_only arm; only the training rows change.
    base = argparse.Namespace(**{**vars(args), "arm": "real_only"})
    arrivals, eval_arrivals, probe_arrivals, train_slice = _v2_split_arrivals(full_trace, base)
    if args.phase == "train":
        arrivals, info = matched(train_slice, load_synth(), MATCHED_ARMS[args.arm])
        VAR_INFO.clear()
        VAR_INFO.update(info)
    return arrivals, eval_arrivals, probe_arrivals, train_slice


def _capture(run_fn, attr):
    def wrapped(*a, **k):
        policy, log = run_fn(*a, **k)
        cells = dict(zip(policy.__code__.co_freevars, (c.cell_contents for c in policy.__closure__)))
        CAPTURED.clear()
        CAPTURED.update(net=cells[attr], attr=attr, best_step=log.attrs.get("best_step"))
        return policy, log
    return wrapped


def install():
    """Patch the V2 module in memory. Idempotent; V2 files are never written."""
    for arm in MATCHED_ARMS:
        if arm not in T.ARMS:
            T.ARMS.append(arm)                   # argparse choices read this list in main()
    T.split_arrivals = split_arrivals
    if not getattr(T.run_ppo, "_v3", False):
        T.run_ppo = _capture(T.run_ppo, "actor")
        T.run_dqn = _capture(T.run_dqn, "q")
        T.run_ppo._v3 = T.run_dqn._v3 = True


def output_dir(argv):
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("--out", type=Path, default=ROOT / "results" / "online")
    return p.parse_known_args(argv)[0].out


def main(argv):
    install()
    out = output_dir(argv)
    before = {f: f.stat().st_mtime for f in out.glob("*.json")} if out.exists() else {}
    sys.argv = ["train_online.py", *argv]
    T.main()
    written = [f for f in out.glob("*.json") if before.get(f) != f.stat().st_mtime]
    if len(written) != 1:
        raise SystemExit(f"expected one new run JSON in {out}, found {written}")
    meta = json.loads(written[0].read_text(encoding="utf-8"))
    run_id = f"{out.name}__{written[0].stem}"
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    record = {"run_id": run_id, "v2_run_json": str(written[0]), "argv": argv, "meta": meta,
              "matched_arm": dict(VAR_INFO) if meta["arm"] in MATCHED_ARMS else None,
              "weights": None}
    if CAPTURED:
        net = CAPTURED["net"]
        torch.save({"state_dict": net.state_dict(), "module": type(net).__name__,
                    "attr": CAPTURED["attr"], "best_val_step": CAPTURED["best_step"],
                    "config": record}, CKPT_DIR / f"{run_id}.pt")
        record["weights"] = {"file": f"{run_id}.pt", "module": type(net).__name__,
                             "best_val_step": CAPTURED["best_step"]}
    (CKPT_DIR / f"{run_id}.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"[v3] {run_id}: checkpoint "
          + (record["weights"]["file"] if record["weights"] else "none (heuristic)"))


if __name__ == "__main__":
    main(sys.argv[1:])
