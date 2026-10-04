"""Figures for the paper from the V2 results. Plotting only, nothing is recomputed beyond what is drawn.

    python scripts/paper_figures_v2.py

Fig. 3  fig3_fidelity_v2.png         marginal ECDF and ACF (lags 1-10) per slice for real train,
                                     synthetic (aug_subsample training data) and real val; data
                                     through fidelity_c4.data(), so train and val only, never test
Fig. 4  fig4_seed_distribution_v2.png per-seed total violation on the test split, training data
                                     real + synthetic, safety on and off, from per_run.csv
Both at 300 dpi, written to revisi/hasil-revisian/figures/.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fidelity_c4 import LAGS, acf, data  # noqa: E402
from paper_tables_v2 import METHOD, ORDER  # noqa: E402
from slice_env import PORTS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "revisi" / "hasil-revisian" / "figures"
DPI = 300
LABEL = {"riil-train (real_only)": "real train", "sintetis (aug_subsample)": "synthetic",
         "riil-val": "real validation"}


def fig_fidelity():
    s = data()
    fig, ax = plt.subplots(2, 3, figsize=(7.16, 4.2), constrained_layout=True)
    for i, port in enumerate(PORTS):
        for k, v in s.items():
            x = np.sort(v[:, i])
            ax[0, i].step(x, np.arange(1, len(x) + 1) / len(x), where="post", label=LABEL[k])
            ax[1, i].plot(list(LAGS), [acf(v[:, i], lag) for lag in LAGS], marker="o", ms=3,
                          label=LABEL[k])
        ax[0, i].set(title=port.upper(), xlabel="arrival (Mbps)", ylabel="ECDF" if i == 0 else None)
        ax[1, i].set(xlabel="lag (steps)", ylabel="autocorrelation" if i == 0 else None)
        ax[1, i].set_xticks(list(LAGS))
    ax[0, 0].legend(fontsize=7)
    for a in ax.flat:
        a.tick_params(labelsize=7)
        a.grid(alpha=0.3)
    path = OUT / "fig3_fidelity_v2.png"
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    return path


def fig_seeds():
    r = pd.read_csv(ROOT / "results" / "analysis-v2" / "per_run.csv")
    r = r[r.arm == "full"]
    methods = [m for m in ORDER if m in set(r.method)]
    fig, ax = plt.subplots(figsize=(7.16, 2.9), constrained_layout=True)
    rng = np.random.default_rng(0)                       # jitter only, for legibility
    for j, (safety, off) in enumerate((("off", -0.2), ("on", 0.2))):
        vals = [r[(r.method == m) & (r.safety == safety)].viol_total.to_numpy() for m in methods]
        pos = np.arange(len(methods)) + off
        b = ax.boxplot(vals, positions=pos, widths=0.34, patch_artist=True, showfliers=False,
                       medianprops={"color": "black"})
        for patch in b["boxes"]:
            patch.set(facecolor=f"C{j}", alpha=0.35)
        for p, v in zip(pos, vals):
            ax.scatter(p + rng.uniform(-0.07, 0.07, len(v)), v, s=5, color=f"C{j}", zorder=3)
        ax.plot([], [], "s", color=f"C{j}", alpha=0.6, label=f"safety {safety}")
    ax.set_xticks(np.arange(len(methods)), [METHOD[m] for m in methods], rotation=25, ha="right",
                  fontsize=7)
    ax.set_ylabel("total SLA violation (%)", fontsize=8)
    ax.tick_params(axis="y", labelsize=7)
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=7)
    path = OUT / "fig4_seed_distribution_v2.png"
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    return path


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in (fig_fidelity(), fig_seeds()):
        print("->", p)


if __name__ == "__main__":
    main()
