"""Minimum detectable effect per V3 family (protocol v3 section 7, gate G5).

Same method as V2 (07-protocol-v2.md section 8.1): two-sided paired t, n = 20,
solved exactly with the noncentral t and inflated by sqrt(1/0.955) for the
Wilcoxon test, via scripts/final_plan_stats.mde (unchanged). Power 0.8; alpha is
the worst Holm step in the family, 0.05 / m. Units: percentage points of
viol_total on the metric of the comparison.

sigma_d per comparison:
- both cells exist in V2 (seed 0-19, test): SD (ddof 1) of the paired
  differences by seed, from results/analysis-v2/per_run.csv;
- a new arm is involved (var_matched, moment_matched): rho = 0, so
  sigma_d = sqrt(sigma_X^2 + sigma_Y^2). A new arm's sigma is the largest V2 SD
  of that method over aug_subsample, full and real_only at safety off on the
  same metric (supervisor decision 2026-10-06, the most conservative choice).

    python scripts_v3/mde_v3.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts_v3"))
import analyze_v3 as V  # noqa: E402
from final_plan_stats import ALPHA, N, POWER, mde  # noqa: E402

PER_RUN = ROOT / "results" / "analysis-v2" / "per_run.csv"
OUT = ROOT / "results" / "v3" / "mde_v3.csv"
PROXY_ARMS = ("aug_subsample", "full", "real_only")


def column(df, cell, metric):
    m, a, s = cell
    sel = df[(df.method == m) & (df.arm == a) & (df.safety == s)].set_index("seed")[metric]
    assert sorted(sel.index) == list(range(20)), f"{cell}: V2 seeds incomplete"
    return sel


def sigma(df, cell, metric):
    """(sd, basis) of one cell; new arms take the conservative V2 proxy."""
    m, a, s = cell
    if a not in V.NEW_ARMS:
        return column(df, cell, metric).std(ddof=1), f"{m} {a} V2"
    sds = {arm: column(df, (m, arm, s), metric).std(ddof=1) for arm in PROXY_ARMS}
    arm = max(sds, key=sds.get)
    return sds[arm], f"{m} {a} = SD terbesar V2 ({arm})"


def main():
    df = pd.read_csv(PER_RUN)
    rows = []
    for fam, pairs in V.families().items():
        alpha = ALPHA / len(pairs)
        for label, x, y, metric in pairs:
            if x[1] in V.NEW_ARMS or y[1] in V.NEW_ARMS:
                (sx, bx), (sy, by) = sigma(df, x, metric), sigma(df, y, metric)
                sd, basis = float(np.hypot(sx, sy)), f"rho = 0: {bx}; {by}"
            else:
                d = column(df, x, metric) - column(df, y, metric)
                sd, basis = float(d.std(ddof=1)), "berpasangan V2 seed 0-19, df 19"
            rows.append({"family": fam, "label": label, "metric": metric, "m": len(pairs),
                         "alpha": alpha, "sigma_d": sd, "mde": mde(sd, alpha), "basis": basis})
    res = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    res.to_csv(OUT, index=False)
    print(f"N = {N}, power {POWER}, alpha Holm terburuk = 0.05/m; satuan poin violation\n")
    print(res.to_string(index=False, float_format=lambda v: f"{v:.3f}"))
    print()
    for fam, g in res.groupby("family"):
        print(f"{fam}: m = {g.m.iloc[0]}, alpha = {g.alpha.iloc[0]:.5f}, "
              f"MDE {g.mde.min():.2f} sampai {g.mde.max():.2f}")
    print(f"written {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
