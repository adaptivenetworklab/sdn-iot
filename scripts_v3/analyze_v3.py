"""Analysis for protocol v3 (docs/experiments/09-protocol-v3.md, sections 5-6).

Frozen with the protocol (tag protocol-v3-final). Reuses scripts/analyze_v2.py
unchanged: load (run JSON + evaluation CSVs -> one row per run), paired
(Wilcoxon signed-rank two-sided, paired t, bootstrap CI of the mean paired
difference with 10,000 resamples, matched-pairs rank-biserial), holm, describe
and md. Only the cell-name pattern is extended in memory so the new arms load.

Families, Holm within each family, alpha 0.05:
  H1 (m=4)  scen_diurnal, safety off: {dqn, ddqn} x {aug_subsample, full} vs demand_prop
  H2 (m=6)  scen_diurnal and scen_flash: safety on vs off for dqn aug_subsample,
            ddqn aug_subsample, demand_prop
  H3 (m=8)  viol_total (test, no scenario), safety off, per method: aug_subsample vs
            real_only; var_matched vs real_only; moment_matched vs var_matched;
            aug_subsample vs moment_matched
Descriptive, outside the families (CI, no test): real_only vs demand_prop on
diurnal; the H1 pairs and real_only on flash; the H3 steps on diurnal (block B);
per-cell means with CI.

    python scripts_v3/analyze_v3.py                      # results/v3 -> results/analysis-v3
    python scripts_v3/analyze_v3.py --dir D --out O
"""
import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analyze_v2 as A  # noqa: E402

ALPHA = A.ALPHA
SEEDS = range(20, 40)                                    # protocol v3 section 3
NEW_ARMS = ("var_matched", "moment_matched")
A.CELL = re.compile(rf"^(?P<method>.+?)_(?P<arm>{'|'.join(A.ARMS + NEW_ARMS)})"
                    r"_safety(?P<safety>on|off)$")
LEARNERS = ("dqn", "ddqn")
DP = ("demand_prop", "full")
H3_STEPS = (("1 replikasi", "aug_subsample", "real_only"),
            ("2 variansi", "var_matched", "real_only"),
            ("3 mean", "moment_matched", "var_matched"),
            ("4 residual", "aug_subsample", "moment_matched"))
RESIDUAL_LABEL = ("perbedaan lain antara trace sintetis dan data riil yang tidak didekomposisi")


def families():
    """{family: [(label, X, Y, metric)]}; X, Y = (method, arm, safety); d = X - Y."""
    h1 = [(f"{m} {a}", (m, a, "off"), (*DP, "off"), "scen_diurnal")
          for m in LEARNERS for a in ("aug_subsample", "full")]
    h2 = [(f"{m} {a} {metric}", (m, a, "on"), (m, a, "off"), metric)
          for metric in ("scen_diurnal", "scen_flash")
          for m, a in (("dqn", "aug_subsample"), ("ddqn", "aug_subsample"), DP)]
    h3 = [(f"{m} langkah {step}", (m, x, "off"), (m, y, "off"), "viol_total")
          for m in LEARNERS for step, x, y in H3_STEPS]
    return {"H1": h1, "H2": h2, "H3": h3}


def descriptive_pairs():
    """Pairs reported with mean difference and CI only."""
    pairs = [("H1 real_only (diurnal)", (m, "real_only", "off"), (*DP, "off"), "scen_diurnal")
             for m in LEARNERS]
    pairs += [(f"H1 flash {m} {a}", (m, a, "off"), (*DP, "off"), "scen_flash")
              for m in LEARNERS for a in ("aug_subsample", "full", "real_only")]
    pairs += [(f"blok B diurnal {m} langkah {step}", (m, x, "off"), (m, y, "off"), "scen_diurnal")
              for m in LEARNERS for step, x, y in H3_STEPS]
    return pairs


def ci_has_zero(r):
    return r["ci_lo"] <= 0 <= r["ci_hi"]


def status(fam, label, r, replicated):
    """Verdict wording fixed by protocol v3 section 6."""
    if np.isnan(r["mean_d"]):
        return "data tidak tersedia"
    sig = r["p_holm"] < ALPHA
    ci = f"selisih dalam [{r['ci_lo']:.2f}, {r['ci_hi']:.2f}]"
    if fam == "H1":
        return ("bereplikasi; " if sig and r["mean_d"] < 0 else
                "signifikan, berlawanan prediksi; " if sig else "tidak bereplikasi; ") + ci
    if fam == "H2":
        return ("sesuai prediksi (safety menaikkan violation); " if sig and r["mean_d"] > 0 else
                "signifikan, berlawanan prediksi; " if sig else "tidak signifikan; ") + ci
    method, step = label.split(" langkah ")
    if step.startswith("1"):
        return ("bereplikasi; " if sig and r["mean_d"] < 0 else "tidak bereplikasi; ") + ci
    if not replicated[method]:
        return "deskriptif (langkah 1 tidak bereplikasi, tanpa klaim mekanisme); " + ci
    if ci_has_zero(r):
        return "tidak terdeteksi; " + ci
    if sig and r["mean_d"] < 0:
        what = RESIDUAL_LABEL if step.startswith("4") else "faktor berkontribusi"
        return f"{what} (menurunkan violation); " + ci
    return ("signifikan, menaikkan violation; " if sig else "tidak signifikan setelah Holm; ") + ci


def run_families(df):
    rows = []
    for fam, pairs in families().items():
        res = [{**A.paired(df, x, y, metric), "family": fam, "label": label, "metric": metric}
               for label, x, y, metric in pairs]
        p = np.array([r["p_wilcoxon"] for r in res], dtype=float)
        ok = ~np.isnan(p)
        adj = np.full(len(p), np.nan)
        if ok.any():
            # As in V2: a missing comparison still counts toward m (p = 1).
            adj[ok] = A.holm(np.where(ok, p, 1.0))[ok]
        for r, pa in zip(res, adj):
            r.update(m=len(pairs), p_holm=pa)
        replicated = {}
        if fam == "H3":
            for r in res:
                method, step = r["label"].split(" langkah ")
                if step.startswith("1"):
                    replicated[method] = (not np.isnan(r["p_holm"]) and r["p_holm"] < ALPHA
                                          and r["mean_d"] < 0)
        for r in res:
            r["status"] = status(fam, r["label"], r, replicated)
            rows.append(r)
    return pd.DataFrame(rows)


def run_descriptive(df):
    rows = []
    for label, x, y, metric in descriptive_pairs():
        r = {**A.paired(df, x, y, metric), "label": label, "metric": metric}
        r.update(p_wilcoxon=np.nan, p_ttest=np.nan, status=f"deskriptif; selisih dalam "
                 f"[{r['ci_lo']:.2f}, {r['ci_hi']:.2f}]" if not np.isnan(r["mean_d"])
                 else "data tidak tersedia")
        rows.append(r)
    return pd.DataFrame(rows)


def check_seeds(df, seeds):
    """Cells with a seed set other than the protocol's; reported, never silently used."""
    want = set(seeds)
    bad = {c: sorted(set(g.seed) ^ want) for c, g in df.groupby("cell") if set(g.seed) != want}
    return bad


def analyse(df, out, seeds=SEEDS):
    out.mkdir(parents=True, exist_ok=True)
    prim = run_families(df)
    desc = run_descriptive(df)
    cells = A.describe(df, ["viol_total", "scen_diurnal", "scen_flash"])
    bad = check_seeds(df, seeds)
    cols = ["family", "label", "metric", "X", "Y", "n", "m", "mean_X", "mean_Y", "mean_d",
            "ci_lo", "ci_hi", "p_wilcoxon", "p_ttest", "p_holm", "rank_biserial", "status"]
    prim[cols].to_csv(out / "primary_v3.csv", index=False)
    desc[[c for c in cols if c not in ("family", "m", "p_holm")]].to_csv(
        out / "descriptive_v3.csv", index=False)
    cells.to_csv(out / "cells_v3.csv", index=False)
    fmt = "{:.4g}"
    report = ["# Hasil V3 (keluaran analyze_v3.py)", "",
              f"Seed yang diharapkan: {seeds.start}-{seeds.stop - 1}. "
              + (f"Sel dengan himpunan seed lain: {bad}" if bad else "Semua sel lengkap."), "",
              "## Keluarga H1-H3 (Holm di dalam keluarga, alpha 0,05)", "",
              A.md(prim, cols, fmt), "## Deskriptif, di luar keluarga (tanpa uji)", "",
              A.md(desc, [c for c in cols if c not in ("family", "m", "p_wilcoxon", "p_ttest",
                                                       "p_holm")], fmt),
              "## Rata-rata per sel (CI 95% bootstrap)", "",
              A.md(cells, list(cells.columns), fmt)]
    (out / "report_v3.md").write_text("\n".join(report), encoding="utf-8")
    return prim, desc, cells, bad


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dir", type=Path, default=ROOT / "results" / "v3")
    p.add_argument("--out", type=Path, default=ROOT / "results" / "analysis-v3")
    a = p.parse_args()
    df, _ = A.load(a.dir, "test")
    prim, _, _, bad = analyse(df, a.out)
    print(f"{len(prim)} primary comparisons -> {a.out}" + (f"; seed sets off: {bad}" if bad else ""))


if __name__ == "__main__":
    main()
