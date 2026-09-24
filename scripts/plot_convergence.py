"""Convergence curves for the frozen sweep. DIAGNOSTIC -- not for the paper.

Reads results/online/*_train.csv, which the sweep already produced, so nothing
is retrained and the frozen primary results are never touched. Plots mean and
bootstrap 95% CI across seeds, and prints a flatness test on the last quarter of
training so "has it converged" is answered with a number rather than by eye.

    python scripts/plot_convergence.py
"""

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
STEM = re.compile(r"^(?P<algo>.+?)_(?P<arm>full|no_mask|no_dueling)_seed(?P<seed>\d+)_train\.csv$")
BANNER = "DIAGNOSTIC - not for paper"


def load(raw_dir, algo, arm="full"):
    curves = {}
    for f in sorted(Path(raw_dir).glob(f"{algo}_{arm}_seed*_train.csv")):
        m = STEM.match(f.name)
        if m:
            curves[int(m["seed"])] = pd.read_csv(f)
    return curves


def band(curves, col, n_grid=100):
    """Mean and bootstrap 95% CI over seeds, on a shared step grid."""
    usable = {s: d for s, d in curves.items() if col in d.columns and len(d) > 1}
    if not usable:
        return None
    lo = max(d["step"].min() for d in usable.values())
    hi = min(d["step"].max() for d in usable.values())
    if not np.isfinite([lo, hi]).all() or hi <= lo:
        return None
    grid = np.linspace(lo, hi, n_grid)
    stack = np.vstack([np.interp(grid, d["step"], d[col]) for d in usable.values()])

    rng = np.random.default_rng(0)
    idx = rng.integers(0, stack.shape[0], size=(2000, stack.shape[0]))
    boots = stack[idx].mean(axis=1)
    return grid, stack.mean(axis=0), np.percentile(boots, 2.5, axis=0), \
        np.percentile(boots, 97.5, axis=0), stack.shape[0]


def flatness(curves, col):
    """Change from the first quarter to the last, as a fraction of each curve's
    range, so magnitudes across very different metrics stay comparable."""
    deltas = []
    for d in curves.values():
        if col not in d.columns or len(d) < 4:
            continue
        q = max(1, len(d) // 4)
        first, last = d[col].iloc[:q].mean(), d[col].iloc[-q:].mean()
        span = d[col].max() - d[col].min()
        deltas.append((last - first) / span if span > 0 else 0.0)
    return np.array(deltas)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", type=Path, default=REPO_ROOT / "results" / "online")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "diagnostic")
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    panels = [("ppo", "mean_reward"), ("sdhppo", "mean_reward"),
              ("ppo", "loss_critic"), ("sdhppo", "loss_critic"),
              ("dqn", "loss"), ("ddqn", "loss")]

    fig, axes = plt.subplots(3, 2, figsize=(12, 12))
    rows = []
    for ax, (algo, col) in zip(axes.ravel(), panels):
        curves = load(args.raw, algo)
        b = band(curves, col)
        if b is None:
            ax.set_title(f"{algo} / {col}: no data")
            continue
        grid, mean, lo, hi, n = b
        ax.plot(grid, mean, color="tab:blue")
        ax.fill_between(grid, lo, hi, alpha=0.25, color="tab:blue")
        ax.set_title(f"{algo} - {col} (n={n} seeds)")
        ax.set_xlabel("environment step")
        ax.set_ylabel(col)
        ax.grid(alpha=0.3)
        if "loss" in col and mean.min() > 0:
            ax.set_yscale("log")

        d = flatness(curves, col)
        rows.append({"algo": algo, "metric": col, "seeds": n,
                     "delta_frac_of_range_mean": d.mean() if len(d) else np.nan,
                     "delta_frac_of_range_std": d.std() if len(d) else np.nan,
                     "converged": bool(len(d) and abs(d.mean()) < 0.10)})

    fig.suptitle(f"Training convergence - {BANNER}", fontsize=13)
    fig.tight_layout()
    out_png = args.out / "convergence_all.png"
    fig.savefig(out_png, dpi=200)
    plt.close(fig)

    summary = pd.DataFrame(rows)
    summary.insert(0, "note", BANNER)
    summary.to_csv(args.out / "convergence_flatness.csv", index=False)

    print(BANNER)
    print("\nChange from first quarter to last, as a fraction of each curve's range.")
    print("|delta| < 0.10 is treated as converged.\n")
    print(summary.drop(columns=["note"]).round(4).to_string(index=False))
    print(f"\nplot -> {out_png}")


if __name__ == "__main__":
    main()
