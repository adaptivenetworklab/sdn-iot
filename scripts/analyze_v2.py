"""Analysis of the final V2 sweep. FROZEN with protocol-v2-final; run it unmodified.

    python scripts/analyze_v2.py                                   # results/final-v2, test
    python scripts/analyze_v2.py --dir <layout> --expect-eval-phase val --out <dir>

Implements protocol v2 section 8 exactly:
  primary   families (a) (b) (c) (e); Wilcoxon signed-rank on seed-paired differences,
            two-sided, zero_method='wilcox'; Holm within each family; paired t as
            companion; matched-pairs rank-biserial; 95% percentile bootstrap CI of the
            mean paired difference (10,000 resamples of seeds). A non-significant result
            is written as "selisih dalam [a, b]", never "tidak ada efek" (K3).
  IQM       per cell with stratified-bootstrap 95% CI, and probability of improvement
            for every primary pair (rliable). Reported beside Holm, not instead of it.
  explore   (d) sdhppo vs no_dueling at both safety levels, (c) at the non-primary
            safety level, non-stationary scenarios, SLA-threshold sensitivity
            (0.5x, 0.75x, 1.5x, 2x and real_train_median). No tests, no Holm.
  secondary per-slice violation, mean delay per slice, drop, reward: mean and CI.
  curves    val probe curves per learner cell: mean, bootstrap band, every seed.

Unit of analysis: the seed. One number per run = mean over its 20 evaluation episodes.
Lower violation is better throughout; d = X - Y < 0 means X is better.

Reads only the CSV/JSON a run wrote; writes only under --out.
"""

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from make_tables import boot_ci, holm  # noqa: E402  (shared with V1, unchanged)

REPO_ROOT = Path(__file__).resolve().parents[1]
PORTS = ("p1", "p2", "p4")
LEARNERS = ("ppo", "sdhppo", "dqn", "ddqn")
HEURISTICS = ("demand_prop", "no_control", "equal_split", "threshold")
ARMS = ("full", "real_only", "aug_subsample", "no_dueling")
CELL = re.compile(rf"^(?P<method>.+?)_(?P<arm>{'|'.join(ARMS)})_safety(?P<safety>on|off)$")
LABEL = {"ppo": "PPO", "sdhppo": "SDH-PPO", "dqn": "DQN", "ddqn": "DDQN",
         "ressdhppo": "SDH-PPO residual", "bcsdhppo": "SDH-PPO + BC init",
         "demand_prop": "demand_prop", "no_control": "no_control",
         "equal_split": "equal_split", "threshold": "threshold"}
# Protocol 8.2: multipliers of each port's SLA, plus the named point added at approval.
SENS_MULT = (0.5, 0.75, 1.5, 2.0)
REAL_TRAIN_MEDIAN = {"p1": 6.50, "p2": 8.23, "p4": 6.52}
# Protocol 8, family (c): which safety level carries the primary test.
C_SAFETY = "off"
ALPHA, N_BOOT = 0.05, 10_000


# ------------------------------------------------------------------ loading
def run_metrics(ev, sla):
    rec = {"reward": ev["reward"].mean(),
           "drop_total": sum(ev[f"drop_{p}"].mean() for p in PORTS)}
    for p in PORTS:
        rec[f"viol_{p}"] = ev[f"viol_{p}"].mean() * 100
        rec[f"delay_{p}"] = ev[f"delay_{p}"].mean()
    rec["viol_total"] = np.mean([rec[f"viol_{p}"] for p in PORTS])
    # Re-thresholding check: at 1x the stored delays must reproduce the stored flags.
    again = np.mean([(ev[f"delay_{p}"] > sla[p]).mean() * 100 for p in PORTS])
    assert abs(again - rec["viol_total"]) < 1e-9, "delay columns do not reproduce viol flags"
    for k in SENS_MULT:
        rec[f"sens_{k:g}x"] = np.mean([(ev[f"delay_{p}"] > k * sla[p]).mean() * 100
                                       for p in PORTS])
    rec["sens_real_train_median"] = np.mean(
        [(ev[f"delay_{p}"] > REAL_TRAIN_MEDIAN[p]).mean() * 100 for p in PORTS])
    return rec


def load(root, expect_phase):
    rows, curves = [], []
    for d in sorted(p for p in Path(root).iterdir() if p.is_dir()):
        m = CELL.match(d.name)
        if not m:
            continue
        for js in sorted(d.glob("*.json")):
            meta = json.loads(js.read_text(encoding="utf-8"))
            if meta.get("eval_phase") != expect_phase:
                raise SystemExit(f"{js}: eval_phase {meta.get('eval_phase')!r}, "
                                 f"expected {expect_phase!r}")
            stem = js.with_suffix("")
            ev = pd.read_csv(f"{stem}_eval.csv")
            sla = meta.get("sla_ms") or {"p1": 6.0, "p2": 70.0, "p4": 7.0}
            rec = {"cell": d.name, **m.groupdict(), "seed": meta["seed"],
                   "best_val_step": meta.get("best_val_step"), **run_metrics(ev, sla)}
            for sc in ("diurnal", "flash"):
                f = Path(f"{stem}_eval_{sc}.csv")
                if f.exists():
                    rec[f"scen_{sc}"] = pd.read_csv(f)[[f"viol_{p}" for p in PORTS]].values.mean() * 100
            tr = Path(f"{stem}_train.csv")
            if tr.exists():
                t = pd.read_csv(tr)
                if "val_viol" in t:
                    v = t.dropna(subset=["val_viol"]).reset_index(drop=True)
                    for i, r in v.iterrows():
                        curves.append({"cell": d.name, "seed": meta["seed"], "probe": i + 1,
                                       "step": r["step"], "val_viol": r["val_viol"]})
                if "res_mean_abs" in t:
                    rec["res_mean_abs"] = t["res_mean_abs"].mean()
            rows.append(rec)
    if not rows:
        raise SystemExit(f"no runs under {root}")
    df = pd.DataFrame(rows)
    dup = df.duplicated(["cell", "seed"])
    assert not dup.any(), f"duplicate runs: {df[dup][['cell', 'seed']].values.tolist()}"
    return df, pd.DataFrame(curves)


# ------------------------------------------------------------------ statistics
def rb_paired(d):
    """Matched-pairs rank-biserial: (W+ - W-) / (W+ + W-), zeros dropped."""
    d = d[d != 0]
    if len(d) == 0:
        return 0.0
    r = stats.rankdata(np.abs(d))
    wp, wm = r[d > 0].sum(), r[d < 0].sum()
    return (wp - wm) / (wp + wm)


def paired(df, x, y, metric="viol_total"):
    """x, y = (method, arm, safety). Pairs by seed; returns one result row."""
    def sel(c):
        m, a, s = c
        return df[(df.method == m) & (df.arm == a) & (df.safety == s)].set_index("seed")[metric]
    X, Y = sel(x), sel(y)
    seeds = X.index.intersection(Y.index)
    out = {"X": "{} [{}] safety {}".format(LABEL.get(x[0], x[0]), x[1], x[2]),
           "Y": "{} [{}] safety {}".format(LABEL.get(y[0], y[0]), y[1], y[2]), "n": len(seeds)}
    if len(seeds) < 2:
        return {**out, "mean_X": np.nan, "mean_Y": np.nan, "mean_d": np.nan, "ci_lo": np.nan,
                "ci_hi": np.nan, "p_wilcoxon": np.nan, "p_ttest": np.nan, "rank_biserial": np.nan}
    d = (X[seeds] - Y[seeds]).to_numpy()
    lo, hi = boot_ci(d, n=N_BOOT)
    if np.all(d == 0):
        pw, pt = 1.0, 1.0
    else:
        pw = stats.wilcoxon(d, zero_method="wilcox", alternative="two-sided").pvalue
        pt = stats.ttest_rel(X[seeds], Y[seeds]).pvalue
    return {**out, "mean_X": X[seeds].mean(), "mean_Y": Y[seeds].mean(), "mean_d": d.mean(),
            "ci_lo": lo, "ci_hi": hi, "p_wilcoxon": pw, "p_ttest": pt,
            "rank_biserial": rb_paired(d)}


def families():
    fam = {"a": [((m, "full", "on"), (m, "full", "off")) for m in LEARNERS + HEURISTICS],
           "b": [(("sdhppo", "full", "on"), ("demand_prop", "full", "on"))],
           "c": [((m, a, C_SAFETY), (m, b, C_SAFETY)) for m in LEARNERS
                 for a, b in (("full", "real_only"), ("full", "aug_subsample"),
                              ("real_only", "aug_subsample"))],
           "e": [((r, "full", "on"), ("demand_prop", "full", "on"))
                 for r in ("ressdhppo", "bcsdhppo")]}
    other = "on" if C_SAFETY == "off" else "off"
    explore = {"d": [(("sdhppo", "full", s), ("sdhppo", "no_dueling", s)) for s in ("on", "off")],
               f"c_safety{other}": [((m, a, other), (m, b, other)) for m in LEARNERS
                                    for a, b in (("full", "real_only"), ("full", "aug_subsample"),
                                                 ("real_only", "aug_subsample"))]}
    return fam, explore


def verdict(r, tested=True):
    if np.isnan(r["mean_d"]):
        return "data tidak tersedia"
    span = f"selisih dalam [{r['ci_lo']:.2f}, {r['ci_hi']:.2f}]"
    if not tested or np.isnan(r.get("p_holm", np.nan)) or r["p_holm"] >= ALPHA:
        return ("tidak signifikan; " if tested else "") + span
    return ("X lebih baik; " if r["mean_d"] < 0 else "X lebih buruk; ") + span


def run_families(df, fam, tested):
    rows = []
    for name, pairs in fam.items():
        res = [paired(df, x, y) for x, y in pairs]
        p = np.array([r["p_wilcoxon"] for r in res], dtype=float)
        ok = ~np.isnan(p)
        adj = np.full(len(p), np.nan)
        if tested and ok.any():
            # A missing comparison still counts toward m (as p = 1), so a lost cell can
            # never make the correction for the remaining ones less strict.
            adj[ok] = holm(np.where(ok, p, 1.0))[ok]
        for r, pa in zip(res, adj):
            r.update(family=name, m=len(pairs), p_holm=pa)
            if not tested:
                r.update(p_wilcoxon=np.nan, p_ttest=np.nan, p_holm=np.nan)
            r["verdict"] = verdict(r, tested)
            rows.append(r)
    return pd.DataFrame(rows)


def rliable_block(df, fam):
    """IQM per cell and probability of improvement per primary pair (rliable)."""
    from rliable import library as rly
    from rliable import metrics
    cells = {c: -g.sort_values("seed").viol_total.to_numpy()[:, None]
             for c, g in df.groupby("cell") if len(g) >= 2}
    iqm_pt, iqm_ci = rly.get_interval_estimates(
        cells, lambda s: np.array([metrics.aggregate_iqm(s)]), reps=N_BOOT)
    iqm = pd.DataFrame([{"cell": c, "n": len(cells[c]), "iqm_viol": -iqm_pt[c][0],
                         "ci_lo": -iqm_ci[c][1][0], "ci_hi": -iqm_ci[c][0][0]}
                        for c in sorted(cells)])
    pairs = {}
    for name, ps in fam.items():
        for x, y in ps:
            cx, cy = (f"{x[0]}_{x[1]}_safety{x[2]}", f"{y[0]}_{y[1]}_safety{y[2]}")
            if cx in cells and cy in cells:
                pairs[f"{name}: {cx} vs {cy}"] = (cells[cx], cells[cy])
    poi = pd.DataFrame()
    if pairs:
        pt, ci = rly.get_interval_estimates(
            pairs, lambda x, y: np.array([metrics.probability_of_improvement(x, y)]), reps=N_BOOT)
        poi = pd.DataFrame([{"pair": k, "p_X_better": pt[k][0], "ci_lo": ci[k][0][0],
                             "ci_hi": ci[k][1][0]} for k in pairs])
    return iqm, poi


def describe(df, cols):
    out = []
    for c, g in df.groupby("cell"):
        rec = {"cell": c, "n": len(g)}
        for col in cols:
            if col in g and g[col].notna().any():
                x = g[col].dropna().to_numpy()
                lo, hi = boot_ci(x, n=N_BOOT)
                rec[col] = x.mean()
                rec[f"{col}_lo"], rec[f"{col}_hi"] = lo, hi
        out.append(rec)
    return pd.DataFrame(out)


def plot_curves(curves, df, out):
    out.mkdir(parents=True, exist_ok=True)
    for cell, g in curves.groupby("cell"):
        piv = g.pivot_table(index="probe", columns="seed", values="val_viol")
        steps = g.groupby("probe").step.median()
        fig, ax = plt.subplots(figsize=(6, 3.5))
        for s in piv.columns:
            ax.plot(steps[piv.index], piv[s], color="0.75", lw=0.7)
        mean = piv.mean(axis=1)
        band = np.array([boot_ci(piv.loc[i].dropna(), n=2000) for i in piv.index])
        ax.fill_between(steps[piv.index], band[:, 0], band[:, 1], alpha=0.3)
        ax.plot(steps[piv.index], mean, lw=2, label=f"mean, n={piv.shape[1]}")
        best = df[df.cell == cell].best_val_step.dropna()
        for b in best:
            ax.axvline(b, color="tab:red", lw=0.4, alpha=0.4)
        ax.set(title=cell, xlabel="training step", ylabel="val probe violation %")
        ax.legend(fontsize=8)
        fig.text(0.99, 0.01, "probe set = selection set; minimum is optimistic",
                 ha="right", fontsize=6)
        fig.tight_layout()
        fig.savefig(out / f"{cell}.png", dpi=120)
        plt.close(fig)


def latex_primary(prim):
    lines = [r"\begin{table*}[t]", r"\centering", r"\footnotesize",
             r"\caption{Primary comparisons (protocol v2 \S8): total violation rate, seed-paired "
             r"(n per row), Wilcoxon signed-rank, Holm within family. "
             r"$\Delta = X - Y$, lower is better.}",
             r"\label{tab:primary_v2}", r"\begin{tabular}{llllrrrl}", r"\toprule",
             r"Fam. & X & Y & n & $\Delta$ [95\% CI] & $p_{\mathrm{Holm}}$ & $r_{rb}$ & Verdict \\",
             r"\midrule"]
    for _, r in prim.iterrows():
        ci = "n/a" if np.isnan(r.mean_d) else f"{r.mean_d:.2f} [{r.ci_lo:.2f}, {r.ci_hi:.2f}]"
        ph = "n/a" if np.isnan(r.p_holm) else f"{r.p_holm:.3g}"
        rb = "n/a" if np.isnan(r.rank_biserial) else f"{r.rank_biserial:.2f}"
        row = f"({r.family}) & {r.X} & {r.Y} & {r.n} & {ci} & {ph} & {rb} & {r.verdict}"
        lines.append(row.replace("_", r"\_") + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    return "\n".join(lines)


def latex_cells(sec):
    lines = [r"\begin{table*}[t]", r"\centering", r"\footnotesize",
             r"\caption{Violation rate per cell, mean [95\% bootstrap CI] over seeds.}",
             r"\label{tab:cells_v2}", r"\begin{tabular}{lrllll}", r"\toprule",
             r"Cell & n & Total & P1 & P2 & P4 \\", r"\midrule"]
    for _, r in sec.sort_values("cell").iterrows():
        cols = [f"{r[c]:.2f} [{r[c + '_lo']:.2f}, {r[c + '_hi']:.2f}]"
                for c in ("viol_total", "viol_p1", "viol_p2", "viol_p4")]
        lines.append((f"{r.cell} & {r.n} & " + " & ".join(cols)).replace("_", r"\_") + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    return "\n".join(lines)


def md(df_, cols, fmt="{:.2f}"):
    head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n"
    body = ""
    for _, r in df_.iterrows():
        vals = []
        for c in cols:
            v = r[c] if c in r else np.nan
            if isinstance(v, (float, np.floating)):
                vals.append("n/a" if np.isnan(v) else fmt.format(v))
            else:
                vals.append(str(v))
        body += "| " + " | ".join(vals) + " |\n"
    return head + body


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dir", type=Path, default=REPO_ROOT / "results" / "final-v2")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "analysis-v2")
    p.add_argument("--expect-eval-phase", default="test", choices=["val", "test"])
    a = p.parse_args()

    df, curves = load(a.dir, a.expect_eval_phase)
    a.out.mkdir(parents=True, exist_ok=True)
    df.to_csv(a.out / "per_run.csv", index=False)

    fam, explore = families()
    prim = run_families(df, fam, tested=True)
    expl = run_families(df, explore, tested=False)
    iqm, poi = rliable_block(df, fam)
    sec_cols = ["viol_total"] + [f"{k}_{p}" for k in ("viol", "delay") for p in PORTS] + \
        ["drop_total", "reward", "res_mean_abs"]
    sec = describe(df, sec_cols)
    scen = describe(df, ["viol_total", "scen_diurnal", "scen_flash"])
    sens_cols = ["viol_total"] + [f"sens_{k:g}x" for k in SENS_MULT] + ["sens_real_train_median"]
    sens = df.groupby("cell")[sens_cols].mean().reset_index()

    for name, t in (("primary", prim), ("exploratory", expl), ("iqm", iqm), ("poi", poi),
                    ("secondary", sec), ("scenarios", scen), ("sensitivity", sens)):
        t.to_csv(a.out / f"{name}.csv", index=False)
    if not curves.empty:
        curves.to_csv(a.out / "curves.csv", index=False)
        plot_curves(curves, df, a.out / "curves")
    (a.out / "table_primary_v2.tex").write_text(latex_primary(prim), encoding="utf-8")
    (a.out / "table_cells_v2.tex").write_text(latex_cells(sec), encoding="utf-8")

    pc = ["family", "X", "Y", "n", "mean_X", "mean_Y", "mean_d", "ci_lo", "ci_hi",
          "p_wilcoxon", "p_ttest", "p_holm", "rank_biserial", "verdict"]
    size = df.groupby("cell").size()
    report = [f"# Analisis V2 ({a.expect_eval_phase})", "",
              f"Dibangkitkan oleh `scripts/analyze_v2.py` dari `{a.dir.name}`. "
              f"{len(df)} run, {df.cell.nunique()} cell, seed per cell {size.min()}-{size.max()}.",
              "", "## Primer (Holm di dalam keluarga)", "", md(prim, pc, "{:.4g}"),
              "## Eksploratif (tanpa uji)", "",
              md(expl, ["family", "X", "Y", "n", "mean_d", "ci_lo", "ci_hi", "verdict"]),
              "## IQM total violation (rliable, stratified bootstrap)", "",
              md(iqm, ["cell", "n", "iqm_viol", "ci_lo", "ci_hi"]),
              "## Probability of improvement P(X lebih baik dari Y)", "",
              md(poi, ["pair", "p_X_better", "ci_lo", "ci_hi"]) if not poi.empty else "n/a\n",
              "## Sekunder", "", md(sec, ["cell", "n"] + [c for c in sec_cols if c in sec]),
              "## Skenario non-stasioner (eksploratif)", "",
              md(scen, ["cell", "n"] + [c for c in ("viol_total", "scen_diurnal", "scen_flash")
                                       if c in scen]),
              "## Sensitivitas ambang SLA (eksploratif; kebijakan dilatih pada 6/70/7)", "",
              md(sens, ["cell"] + sens_cols)]
    (a.out / "report.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report[:3]))
    print(f"-> {a.out}")


if __name__ == "__main__":
    main()
