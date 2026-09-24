"""Aggregate the online sweep into statistics and LaTeX tables.

Reads every results/online/*_eval.csv, aggregates across seeds, and emits
results/tables/*.tex for \\input{} into the paper. No result number is ever
typed by hand: if a number appears in the paper it was produced here from raw
per-step records.

Reporting rules (from the campaign work order):
  * mean +- 95% CI, never a bare point estimate
  * seed count stated in every caption
  * Mann-Whitney U (does not assume normality, n=10 seeds) plus Welch's t
  * Holm-Bonferroni correction across the comparisons against Proposed
  * rank-biserial correlation as effect size
  * non-significant differences reported as such, not rounded into a win
"""

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

REPO_ROOT = Path(__file__).resolve().parents[1]
PORTS = ("p1", "p2", "p4")
PROPOSED = ("sdhppo", "full")

LABEL = {
    ("sdhppo", "full"): "Proposed (SDH-PPO)",
    ("ppo", "full"): "PPO Standard",
    ("ddqn", "full"): "DDQN",
    ("dqn", "full"): "DQN",
    ("demand_prop", "full"): "Demand Proportional",
    ("threshold", "full"): "Threshold",
    ("const_max", "full"): "Const Max",
    ("no_control", "full"): "No Control",
    ("sdhppo", "no_mask"): "Proposed w/o safety layer",
    ("sdhppo", "no_dueling"): "Proposed w/o dueling critic",
}
MAIN_ORDER = [("sdhppo", "full"), ("ppo", "full"), ("ddqn", "full"), ("dqn", "full"),
              ("demand_prop", "full"), ("threshold", "full"),
              ("const_max", "full"), ("no_control", "full")]
ABLATION_ORDER = [("sdhppo", "full"), ("sdhppo", "no_mask"), ("sdhppo", "no_dueling")]

STEM = re.compile(r"^(?P<algo>.+?)_(?P<arm>full|no_mask|no_dueling)_seed(?P<seed>\d+)_eval\.csv$")


def collect(raw_dir):
    """One row per (algo, arm, seed): the per-seed summary the stats operate on."""
    rows = []
    for f in sorted(Path(raw_dir).glob("*_eval.csv")):
        m = STEM.match(f.name)
        if not m:
            continue
        d = pd.read_csv(f)
        rec = {"algo": m["algo"], "arm": m["arm"], "seed": int(m["seed"]),
               "reward": d["reward"].mean()}
        for p in PORTS:
            rec[f"viol_{p}"] = d[f"viol_{p}"].mean() * 100.0
            rec[f"delay_{p}"] = d[f"delay_{p}"].mean()
            rec[f"drop_{p}"] = d[f"drop_{p}"].mean()
        rec["viol_total"] = np.mean([rec[f"viol_{p}"] for p in PORTS])
        rows.append(rec)
    if not rows:
        raise SystemExit(f"no *_eval.csv found in {raw_dir}")
    return pd.DataFrame(rows)


def boot_ci(x, n=10_000, seed=0):
    x = np.asarray(x, dtype=float)
    if len(x) < 2:
        return (np.nan, np.nan)
    rng = np.random.default_rng(seed)
    means = rng.choice(x, size=(n, len(x)), replace=True).mean(axis=1)
    return tuple(np.percentile(means, [2.5, 97.5]))


def fmt(x, lo, hi, nd=2):
    if np.isnan(lo):
        return f"{x:.{nd}f}"
    return f"{x:.{nd}f} [{lo:.{nd}f}, {hi:.{nd}f}]"


def rank_biserial(a, b):
    """Effect size matching Mann-Whitney: P(a>b) - P(a<b)."""
    a, b = np.asarray(a), np.asarray(b)
    gt = sum((x > y) for x in a for y in b)
    lt = sum((x < y) for x in a for y in b)
    return (gt - lt) / (len(a) * len(b))


def holm(pvals):
    """Holm-Bonferroni adjusted p-values, order preserved."""
    idx = np.argsort(pvals)
    out, running = np.empty(len(pvals)), 0.0
    for rank, i in enumerate(idx):
        adj = (len(pvals) - rank) * pvals[i]
        running = max(running, adj)
        out[i] = min(running, 1.0)
    return out


def compare(df, metric, groups, lower_is_better=True):
    """Proposed vs every other group on `metric`, with Holm correction."""
    ref = df[(df.algo == PROPOSED[0]) & (df.arm == PROPOSED[1])][metric].to_numpy()
    others = [g for g in groups if g != PROPOSED]
    raw = []
    for algo, arm in others:
        x = df[(df.algo == algo) & (df.arm == arm)][metric].to_numpy()
        if len(x) < 2 or len(ref) < 2:
            raw.append((algo, arm, np.nan, np.nan, np.nan))
            continue
        u = stats.mannwhitneyu(ref, x, alternative="two-sided").pvalue
        t = stats.ttest_ind(ref, x, equal_var=False).pvalue
        raw.append((algo, arm, u, t, rank_biserial(ref, x)))
    valid = [r[2] for r in raw if not np.isnan(r[2])]
    adj = dict(zip([i for i, r in enumerate(raw) if not np.isnan(r[2])],
                   holm(np.array(valid)))) if valid else {}
    out = []
    for i, (algo, arm, u, t, eff) in enumerate(raw):
        pa = adj.get(i, np.nan)
        if np.isnan(pa):
            verdict = "n/a"
        elif pa >= 0.05:
            verdict = "no significant difference"
        else:
            ref_m = ref.mean()
            x_m = df[(df.algo == algo) & (df.arm == arm)][metric].mean()
            better = ref_m < x_m if lower_is_better else ref_m > x_m
            verdict = "Proposed better" if better else "Proposed WORSE"
        out.append({"algo": algo, "arm": arm, "label": LABEL.get((algo, arm), f"{algo}/{arm}"),
                    "p_mannwhitney": u, "p_welch": t, "p_holm": pa,
                    "effect_rank_biserial": eff, "verdict": verdict})
    return pd.DataFrame(out)


def latex_main(df, groups, n_seeds):
    lines = [
        r"\begin{table*}[t]", r"\centering",
        rf"\caption{{Performance comparison in the queueing simulation. "
        rf"Mean over {n_seeds} seeds with bootstrap 95\% CI. Lower is better. "
        rf"Delay and violation are per slice; total violation is the mean across slices.}}",
        r"\label{tab:3}", r"\begin{tabular}{lccccccc}", r"\toprule",
        r"Algorithm & P1 Delay (ms) & P1 Viol (\%) & P2 Delay (ms) & P2 Viol (\%) "
        r"& P4 Delay (ms) & P4 Viol (\%) & Total Viol (\%) \\", r"\midrule",
    ]
    for g in groups:
        sub = df[(df.algo == g[0]) & (df.arm == g[1])]
        if sub.empty:
            continue
        cells = []
        for p in PORTS:
            for key in (f"delay_{p}", f"viol_{p}"):
                v = sub[key].to_numpy()
                lo, hi = boot_ci(v)
                cells.append(fmt(v.mean(), lo, hi))
        v = sub["viol_total"].to_numpy()
        lo, hi = boot_ci(v)
        cells.append(fmt(v.mean(), lo, hi))
        lines.append(LABEL.get(g, f"{g[0]}/{g[1]}") + " & " + " & ".join(cells) + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table*}"]
    return "\n".join(lines)


def latex_stats(cmp_df, n_seeds, label, caption):
    lines = [
        r"\begin{table}[t]", r"\centering", rf"\caption{{{caption} (n={n_seeds} seeds each).}}",
        rf"\label{{{label}}}", r"\begin{tabular}{lcccl}", r"\toprule",
        r"Comparison & $p$ (MWU) & $p$ (Holm) & Effect & Verdict \\", r"\midrule",
    ]
    for _, r in cmp_df.iterrows():
        pm = "--" if np.isnan(r.p_mannwhitney) else f"{r.p_mannwhitney:.4f}"
        ph = "--" if np.isnan(r.p_holm) else f"{r.p_holm:.4f}"
        ef = "--" if np.isnan(r.effect_rank_biserial) else f"{r.effect_rank_biserial:+.2f}"
        lines.append(f"Proposed vs {r.label} & {pm} & {ph} & {ef} & {r.verdict} " + r"\\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", type=Path, default=REPO_ROOT / "results" / "online")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "tables")
    args = p.parse_args()

    df = collect(args.raw)
    args.out.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out / "per_seed_summary.csv", index=False)

    n_seeds = int(df.groupby(["algo", "arm"]).size().min())
    present = [g for g in MAIN_ORDER if not df[(df.algo == g[0]) & (df.arm == g[1])].empty]
    abl = [g for g in ABLATION_ORDER if not df[(df.algo == g[0]) & (df.arm == g[1])].empty]

    (args.out / "table_main.tex").write_text(latex_main(df, present, n_seeds), encoding="utf-8")
    if len(abl) > 1:
        (args.out / "table_ablation.tex").write_text(latex_main(df, abl, n_seeds), encoding="utf-8")

    cmp_main = compare(df, "viol_total", present)
    cmp_main.to_csv(args.out / "stats_main.csv", index=False)
    (args.out / "table_stats.tex").write_text(
        latex_stats(cmp_main, n_seeds, "tab:stats",
                    "Significance of total violation rate, Proposed vs each baseline, "
                    "Holm-corrected"), encoding="utf-8")

    cmp_abl = None
    if len(abl) > 1:
        cmp_abl = compare(df, "viol_total", abl)
        cmp_abl.to_csv(args.out / "stats_ablation.csv", index=False)
        (args.out / "table_stats_ablation.tex").write_text(
            latex_stats(cmp_abl, n_seeds, "tab:stats_abl",
                        "Ablation: significance of total violation rate, Holm-corrected"),
            encoding="utf-8")

    print(f"seeds per configuration: {n_seeds}\n")
    agg = df.groupby(["algo", "arm"]).agg(
        viol_total=("viol_total", "mean"), reward=("reward", "mean"),
        **{f"viol_{p}": (f"viol_{p}", "mean") for p in PORTS}).round(2)
    print(agg.sort_values("viol_total").to_string())
    print("\nProposed vs baselines on total violation (Holm-corrected):")
    print(cmp_main[["label", "p_mannwhitney", "p_holm", "effect_rank_biserial",
                    "verdict"]].to_string(index=False))
    if cmp_abl is not None:
        print("\nAblation:")
        print(cmp_abl[["label", "p_holm", "effect_rank_biserial", "verdict"]].to_string(index=False))
    print(f"\ntables -> {args.out}")


if __name__ == "__main__":
    main()
