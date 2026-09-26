"""Select the tuning configuration per method, from the CSVs, never by hand.

Reads every run under a tuning tree and reports, per configuration, the mean and
sd of the evaluation violation rate across seeds. The winner per method is the
argmin of that mean on the VALIDATION split.

It also reports the gap between the probe value that selected a checkpoint and
the full evaluation of those same weights. That gap is the quantity that exposed
the two selection defects: 11.37 points on the first tuning round, where the
probe was 5 drifting episodes. It stays in the output as a standing check, and is
reported whatever it says.

    python scripts/summarize_tuning.py [--dir results/tuning-v2]
"""

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
PORTS = ("p1", "p2", "p4")

# Directory prefix -> reported method label. bcsdhppo/ressdhppo are the family (e)
# arms; they run the sdhppo algo, so the directory prefix is what distinguishes
# them, not the file stem.
ARM_LABEL = {
    "ppo": "PPO",
    "sdhppo": "SDH-PPO",
    "dqn": "DQN",
    "ddqn": "DDQN",
    "bcsdhppo": "SDH-PPO + BC init",
    "ressdhppo": "SDH-PPO residual",
}


def read_run(eval_csv):
    """One run: its violation rate, and how its checkpoint was chosen."""
    ev = pd.read_csv(eval_csv)
    viol = float(ev[[f"viol_{p}" for p in PORTS]].values.mean() * 100)

    meta_path = Path(str(eval_csv).replace("_eval.csv", ".json"))
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}

    n_probes, probe_best = meta.get("n_val_probes"), meta.get("best_val_viol")
    train_path = Path(str(eval_csv).replace("_eval.csv", "_train.csv"))
    if (n_probes is None or probe_best is None) and train_path.exists():
        tr = pd.read_csv(train_path)
        if "val_viol" in tr:
            v = tr["val_viol"].dropna()
            n_probes, probe_best = len(v), (float(v.min()) if len(v) else None)

    return {
        "viol": viol,
        "n_probes": n_probes,
        "probe_best": probe_best,
        "best_step": meta.get("best_val_step"),
        "seed": meta.get("seed"),
        "eval_phase": meta.get("eval_phase"),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dir", type=Path, default=REPO_ROOT / "results" / "tuning-v2")
    p.add_argument("--out", type=Path, default=None, help="default: <dir>/selection.csv")
    args = p.parse_args()

    rows = []
    for cfg_dir in sorted(d for d in args.dir.iterdir() if d.is_dir()):
        m = re.match(r"([a-z]+)_", cfg_dir.name)
        if not m or m.group(1) not in ARM_LABEL:
            continue
        for ev in sorted(cfg_dir.glob("*_eval.csv")):
            if re.search(r"_eval_[a-z]+\.csv$", ev.name):      # scenario re-evaluations
                continue
            r = read_run(ev)
            r["arm"] = m.group(1)
            r["config"] = cfg_dir.name[len(m.group(1)) + 1:]
            rows.append(r)

    if not rows:
        raise SystemExit(f"no runs found under {args.dir}")

    df = pd.DataFrame(rows)
    bad = df[df.eval_phase.notna() & (df.eval_phase != "val")]
    if len(bad):
        raise SystemExit(f"{len(bad)} run(s) were not evaluated on val; refusing to select")

    df["gap"] = df["viol"] - df["probe_best"]
    agg = (df.groupby(["arm", "config"])
             .agg(seeds=("viol", "size"), viol_mean=("viol", "mean"),
                  viol_sd=("viol", "std"), probe_best_mean=("probe_best", "mean"),
                  gap_mean=("gap", "mean"), n_probes_min=("n_probes", "min"),
                  n_probes_max=("n_probes", "max"))
             .reset_index())

    out = args.out or args.dir / "selection.csv"
    agg.sort_values(["arm", "viol_mean"]).to_csv(out, index=False)

    print(f"{len(df)} runs, {len(agg)} configurations, evaluated on val\n")

    # Probe parity is the gate that fails if the unequal-probe defect returns.
    lo, hi = int(df.n_probes.min()), int(df.n_probes.max())
    print(f"probe parity: {lo}-{hi} probes per run across all methods "
          f"-> {'OK' if lo == hi else 'UNEQUAL, investigate'}")
    print(f"probe-to-eval gap: mean {df.gap.mean():+.2f} pts, "
          f"range {df.gap.min():+.2f} to {df.gap.max():+.2f} "
          f"(first round measured +11.37 on the selected SDH-PPO run)\n")

    print("| Metode | Konfigurasi terbaik | Val viol % (sd) | gap probe->eval |")
    print("|---|---|---|---|")
    for arm in [a for a in ARM_LABEL if (agg.arm == a).any()]:
        sub = agg[agg.arm == arm]
        w = sub.loc[sub.viol_mean.idxmin()]
        sd = "n/a" if np.isnan(w.viol_sd) else f"{w.viol_sd:.2f}"
        print(f"| {ARM_LABEL[arm]} | `{w.config}` | **{w.viol_mean:.2f}** ({sd}) "
              f"| {w.gap_mean:+.2f} |")

    print("\nAll configurations, best to worst within each method:")
    for arm in [a for a in ARM_LABEL if (agg.arm == a).any()]:
        print(f"\n{ARM_LABEL[arm]}:")
        for _, r in agg[agg.arm == arm].sort_values("viol_mean").iterrows():
            sd = "n/a" if np.isnan(r.viol_sd) else f"{r.viol_sd:.2f}"
            print(f"  {r.viol_mean:6.2f} ({sd:>5}) n={int(r.seeds)}  {r.config}")

    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
