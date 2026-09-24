"""Verify that scripts/sweep.py reproduces allModel4.ipynb.

Recomputes the notebook's Table IV metrics from results/raw/*_eval.csv and diffs
them against the notebook's own saved sla_violation_report.csv. Any row that
disagrees beyond --tol means the port is not faithful and the sweep must not be
trusted. Exits non-zero on mismatch.

    python scripts/check_fidelity.py
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_REPORT = REPO_ROOT / "Reinforcement Learning" / "revision" / "sla_violation_report.csv"

# sweep.py --algo  ->  label used in the notebook's report
ALGO_TO_LABEL = {
    "sdhppo": "Proposed (SDH-PPO)",
    "ppo": "PPO Standard",
    "dqn": "DQN",
    "ddqn": "DDQN",
    "static": "Static",
}


def metrics(eval_csv, sla):
    df = pd.read_csv(eval_csv)
    out = {}
    for port, col in (("P1", "d1"), ("P2", "d2"), ("P4", "d4")):
        out[f"{port} Avg (ms)"] = df[col].mean()
        out[f"{port} Viol (%)"] = (df[col] > sla[port]).mean() * 100
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", type=Path, default=REPO_ROOT / "results" / "raw")
    p.add_argument("--arm", default="full")
    p.add_argument("--seed", type=int, default=42)
    # The notebook's report is rounded: percentages to 1 dp, averages to 2 dp.
    # 0.05 is that rounding granularity, not a loosened threshold.
    p.add_argument("--tol", type=float, default=0.05, help="max abs diff to accept")
    p.add_argument("--sla-p1", type=float, default=6.0)
    p.add_argument("--sla-p2", type=float, default=70.0)
    p.add_argument("--sla-p4", type=float, default=7.0)
    args = p.parse_args()

    sla = {"P1": args.sla_p1, "P2": args.sla_p2, "P4": args.sla_p4}

    ref = pd.read_csv(NOTEBOOK_REPORT)
    # the notebook writes percentages as strings with a trailing '%'
    for c in ref.columns:
        if c != "Algorithm":
            ref[c] = pd.to_numeric(ref[c].astype(str).str.rstrip("%"))
    ref = ref.set_index("Algorithm")

    rows, worst, missing = [], 0.0, []
    for algo, label in ALGO_TO_LABEL.items():
        f = args.raw / f"{algo}_{args.arm}_seed{args.seed}_eval.csv"
        if not f.exists():
            missing.append(f.name)
            continue
        if label not in ref.index:
            missing.append(f"{label} (absent from notebook report)")
            continue
        got = metrics(f, sla)
        for metric, value in got.items():
            expected = float(ref.loc[label, metric])
            diff = abs(value - expected)
            worst = max(worst, diff)
            rows.append({
                "algo": label, "metric": metric,
                "notebook": round(expected, 4), "port": round(value, 4),
                "abs_diff": round(diff, 4), "ok": diff <= args.tol,
            })

    if missing:
        print("missing inputs:", ", ".join(missing), file=sys.stderr)
    if not rows:
        print("nothing to compare", file=sys.stderr)
        return 2

    out = pd.DataFrame(rows)
    pd.set_option("display.width", 120)
    print(out.to_string(index=False))
    n_bad = int((~out["ok"]).sum())
    print(f"\nworst abs diff {worst:.4f} (tol {args.tol}); {n_bad}/{len(out)} metrics outside tolerance")
    return 1 if n_bad else 0


if __name__ == "__main__":
    sys.exit(main())
