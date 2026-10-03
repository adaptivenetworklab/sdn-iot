"""Planning numbers for the final V2 sweep, from CSVs and logs, never by hand.

DIAGNOSTIC, bukan untuk paper. Feeds protocol v2 sections 2.3, 7.2, 8.1 and 8.2.

1. heur  - heuristic val violation over 20 seeds (results/diagnostic/heur_val20/).
2. mde   - minimum detectable effect (MDE) at N = 20 for every primary comparison.
           Reported to show what N = 20 can and cannot resolve; it does NOT choose N
           (K1 fixed N = 20 before this was computed).
3. sweep - run count and wall-time estimate for the final sweep at N = 20.
4. sla   - medians behind the SLA thresholds (protocol 8.2, question A2).

MDE method. Paired t, n = 20, df = 19, power 0.8, two-sided, solved exactly
with the noncentral t; then inflated by sqrt(1/0.955), the Pitman efficiency of
the Wilcoxon signed-rank test relative to t under normality. Holm runs inside
each family (protocol section 8), so the first Holm step tests at alpha/m and
the last at alpha: both are reported, as the worst and best case. A Bonferroni
column over all primary tests shows the cost of correcting across families.

SD sources and how far to trust them. Learners: tuning-v2, safety off, 2 seeds
per configuration. 'pooled' pools the within-configuration variance over the 8
configurations of a method (df = 8, assumes equal variance across configs);
'selected' is the chosen configuration alone (df = 1). Heuristics: 20 seeds on
val (df = 19). For a learner-vs-learner or learner-vs-heuristic difference no
paired data exists at N > 2, so sigma_d is bounded by rho = 0,
sqrt(s1^2 + s2^2). Shared episode sets make rho positive in practice, so this
bound is conservative; the n = 2 paired estimate is printed beside it and is not
reliable (df = 1). The 95% CI of each MDE carries the chi-square CI of sigma.

    python scripts/final_plan_stats.py [--fill-protocol]
"""

import argparse
import io
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

from slice_env import DEFAULT_SLA_MS, DEFAULT_TRACE
from summarize_tuning import ARM_LABEL, read_run

REPO_ROOT = Path(__file__).resolve().parents[1]
TUNING = REPO_ROOT / "results" / "tuning-v2"
HEUR = REPO_ROOT / "results" / "diagnostic" / "heur_val20"
OUT = REPO_ROOT / "results" / "diagnostic" / "final_plan_stats.md"
PROTOCOL = REPO_ROOT / "docs" / "experiments" / "07-protocol-v2.md"
PORTS = ("p1", "p2", "p4")
HEURISTICS = ("demand_prop", "no_control", "equal_split", "threshold")
LEARNERS = ("ppo", "sdhppo", "dqn", "ddqn")
N, POWER, ALPHA, ARE = 20, 0.8, 0.05, 0.955
M = {"a": 8, "b": 1, "c": 12, "e": 2}          # family sizes, protocol section 8
M_ALL = sum(M.values())


def mde(sigma_d, alpha, n=N):
    """Smallest true mean difference a two-sided paired test detects with POWER."""
    df = n - 1
    tc = stats.t.ppf(1 - alpha / 2, df)

    def power(d):
        nc = d * np.sqrt(n) / sigma_d
        # scipy returns NaN for the lower tail once nc is large; it is ~0 there.
        lower = np.nan_to_num(stats.nct.cdf(-tc, df, nc))
        return stats.nct.sf(tc, df, nc) + lower - POWER

    if sigma_d == 0:
        return 0.0
    return optimize.brentq(power, 1e-9 * sigma_d, 5 * sigma_d) / np.sqrt(ARE)


def sigma_ci(s, df):
    return (s * np.sqrt(df / stats.chi2.ppf(0.975, df)),
            s * np.sqrt(df / stats.chi2.ppf(0.025, df)))


def fmt(x):
    return f"{x:.2f}".replace(".", ",")


def tuning_sds():
    rows = []
    for d in sorted(p for p in TUNING.iterdir() if p.is_dir()):
        m = re.match(r"([a-z]+)_", d.name)
        if not m or m.group(1) not in ARM_LABEL:
            continue
        for ev in d.glob("*_eval.csv"):
            r = read_run(ev)
            rows.append({"arm": m.group(1), "config": d.name, "seed": r["seed"],
                         "viol": r["viol"]})
    df = pd.DataFrame(rows)
    out = {}
    for arm, g in df.groupby("arm"):
        per_cfg = g.groupby("config").viol
        best = per_cfg.mean().idxmin()
        dof = int((per_cfg.size() - 1).sum())
        pooled = float(np.sqrt((per_cfg.var(ddof=1) * (per_cfg.size() - 1)).sum() / dof))
        sel = g[g.config == best].set_index("seed").viol.sort_index()
        out[arm] = {"pooled": pooled, "pooled_df": dof,
                    "selected": float(sel.std(ddof=1)), "selected_df": len(sel) - 1,
                    "per_seed": sel}
    return out


def heuristic_table():
    rows = []
    for js in HEUR.glob("*.json"):
        meta = json.loads(js.read_text(encoding="utf-8"))
        ev = pd.read_csv(str(js).replace(".json", "_eval.csv"))
        assert meta["eval_phase"] == "val", js
        rows.append({"algo": meta["algo"], "safety": "on" if meta["safety_applied"] else "off",
                     "seed": meta["seed"],
                     "viol": float(ev[[f"viol_{p}" for p in PORTS]].values.mean() * 100)})
    if not rows:
        raise SystemExit(f"no runs under {HEUR}; run the heuristic val sweep first")
    return pd.DataFrame(rows).pivot_table(index="seed", columns=["algo", "safety"], values="viol")


def heur_block(H):
    b = [f"Heuristik di val, {H.shape[0]} seed (violation %):", "",
         "| Kebijakan | Safety | mean | sd | min | max | seed 0 |", "|---|---|---|---|---|---|---|"]
    for algo in HEURISTICS:
        for s in ("off", "on"):
            v = H[(algo, s)]
            b.append(f"| `{algo}` | {s} | {fmt(v.mean())} | {fmt(v.std(ddof=1))} | "
                     f"{fmt(v.min())} | {fmt(v.max())} | {fmt(v.loc[0])} |")
    return b


def mde_block(H, T):
    n_seeds = H.shape[0]
    b = ["SD learner dari tuning-v2 (val, safety off):", "",
         "| Arm | SD pooled (df) | SD config terpilih (df) |", "|---|---|---|"]
    for arm, t in T.items():
        b.append(f"| {ARM_LABEL[arm]} | {fmt(t['pooled'])} ({t['pooled_df']}) | "
                 f"{fmt(t['selected'])} ({t['selected_df']}) |")

    def lsd(arm):
        return (T[arm]["pooled"], T[arm]["pooled_df"])

    def hsd(algo, s):
        v = H[(algo, s)]
        return (float(v.std(ddof=1)), len(v) - 1)

    def pair2(arm, algo, s):
        d = T[arm]["per_seed"] - H[(algo, s)].loc[T[arm]["per_seed"].index]
        return float(d.std(ddof=1))

    # (label, family, sigma components [(sd, df)], basis, paired n=2 estimate)
    comps = []
    for algo in HEURISTICS:
        on, off = H[(algo, "on")], H[(algo, "off")]
        comps.append((f"(a) `{algo}` on vs off", "a",
                      [(float((on - off).std(ddof=1)), n_seeds - 1)], "paired", None))
    for arm in LEARNERS:
        comps.append((f"(a) {ARM_LABEL[arm]} on vs off", "a", [lsd(arm), lsd(arm)], "rho0", None))
    comps.append(("(b) SDH-PPO+safety vs `demand_prop`+safety", "b",
                  [lsd("sdhppo"), hsd("demand_prop", "on")], "rho0",
                  pair2("sdhppo", "demand_prop", "off")))
    for arm in LEARNERS:
        comps.append((f"(c) {ARM_LABEL[arm]}, tiap pasangan arm (3x)", "c", [lsd(arm), lsd(arm)],
                      "rho0", None))
    for arm in ("ressdhppo", "bcsdhppo"):
        comps.append((f"(e) {ARM_LABEL[arm]}+safety vs `demand_prop`+safety", "e",
                      [lsd(arm), hsd("demand_prop", "on")], "rho0",
                      pair2(arm, "demand_prop", "off")))
    comps.append(("(d) SDH-PPO vs no_dueling [EKSPLORATIF]", "d", [lsd("sdhppo"), lsd("sdhppo")],
                  "rho0", None))

    b += ["", f"MDE pada N = {N}, power {POWER}, dua sisi, dalam poin persentase violation. "
          f"CI 95% dari CI chi-square SD. Kolom alpha/{M_ALL}: Bonferroni lintas seluruh tes "
          f"primer.", "",
          "| Perbandingan | sigma_d | dasar | MDE @ alpha/m | CI 95% | MDE @ alpha | "
          f"MDE @ alpha/{M_ALL} | sigma_d berpasangan n=2 |",
          "|---|---|---|---|---|---|---|---|"]
    for label, fam, parts, basis, p2 in comps:
        sd = float(np.sqrt(sum(x ** 2 for x, _ in parts)))
        lo = float(np.sqrt(sum(sigma_ci(x, d)[0] ** 2 for x, d in parts)))
        hi = float(np.sqrt(sum(sigma_ci(x, d)[1] ** 2 for x, d in parts)))
        a_m = ALPHA / M.get(fam, 1)
        dfs = "/".join(str(d) for _, d in parts)
        basis_txt = f"berpasangan, df {dfs}" if basis == "paired" else f"rho = 0, df {dfs}"
        col_m = fmt(mde(sd, a_m)) if fam != "d" else f"{fmt(mde(sd, ALPHA))} (tanpa koreksi)"
        all_col = fmt(mde(sd, ALPHA / M_ALL)) if fam != "d" else "-"
        b.append(f"| {label} | {fmt(sd)} | {basis_txt} | {col_m} | "
                 f"[{fmt(mde(lo, a_m))}; {fmt(mde(hi, a_m))}] | {fmt(mde(sd, ALPHA))} | "
                 f"{all_col} | {fmt(p2) if p2 is not None else '-'} |")
    return b


def sweep_block():
    """Wall time per method, measured under 12-way parallel load (tuning-v2/run.log)."""
    secs = {}
    for ln in (TUNING / "run.log").read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\w+?)_full_train_safetyoff_seed\d+(_init-bc|_res[\d.]+)?: "
                     r"train (\d+)s eval ([\d.]+)s", ln)
        if m:
            key = m.group(1) + {"_init-bc": "+bc", None: ""}.get(m.group(2), "+res")
            secs.setdefault(key, []).append(int(m.group(3)) + float(m.group(4)))
    mean = {k: float(np.mean(v)) for k, v in secs.items()}
    s2 = 2                                      # safety on / off
    plan = [
        ("arm `full`, 4 learner", {k: s2 * N for k in LEARNERS}),
        ("arm `full`, 4 heuristik", {"heur": len(HEURISTICS) * s2 * N}),
        ("`real_only` + `aug_subsample`, 4 learner", {k: 2 * s2 * N for k in LEARNERS}),
        ("`no_dueling` (SDH-PPO)", {"sdhppo": s2 * N}),
        ("residual + BC init", {"sdhppo+res": s2 * N, "sdhppo+bc": s2 * N}),
    ]
    b = ["| Blok | Run | CPU-jam (serial) |", "|---|---|---|"]
    tot_runs = tot_s = 0
    for name, cnt in plan:
        runs = sum(cnt.values())
        sec = sum(c * mean.get(k, 0.0) for k, c in cnt.items())
        tot_runs += runs
        tot_s += sec
        b.append(f"| {name} | {runs} | {fmt(sec / 3600)} |")
    b += [f"| **Total** | **{tot_runs}** | **{fmt(tot_s / 3600)}** |", "",
          f"Wall clock ideal pada 12 proses: **{fmt(tot_s / 3600 / 12)} jam** (total / 12, tanpa "
          f"ekor antrean). Heuristik dihitung 0 s. Rata-rata detik per run (train + eval): "
          + ", ".join(f"{k} {mean[k]:.0f}" for k in sorted(mean)) + "."]
    return b


def sla_block():
    """Medians behind the SLA thresholds: real trace vs the V1 synthetic sets."""
    raw = DEFAULT_TRACE.read_text(encoding="utf-8", errors="ignore").splitlines()
    real = pd.read_csv(io.StringIO("\n".join(ln.strip().replace('"', "") for ln in raw)),
                       sep=";", decimal=",")
    rl = REPO_ROOT / "Reinforcement Learning"
    sources = [
        ("trace riil `dataset_dqn_rich.csv`", real, "delay_ms_{}"),
        ("sintetis V1 `final/synthetic_15k_complete_final.csv`",
         pd.read_csv(rl / "final" / "synthetic_15k_complete_final.csv"), "delay_ms_{}"),
        ("sintetis V1 `revision/drl_preprocessed_final.csv`",
         pd.read_csv(rl / "revision" / "drl_preprocessed_final.csv"), "raw_delay_{}"),
    ]
    b = ["| Sumber | baris | median P1 (ms) | median P2 (ms) | median P4 (ms) |",
         "|---|---|---|---|---|",
         "| **Ambang di `slice_env.py`** | - | "
         + " | ".join(fmt(DEFAULT_SLA_MS[p]) for p in PORTS) + " |"]
    for name, df, col in sources:
        b.append(f"| {name} | {len(df)} | "
                 + " | ".join(fmt(df[col.format(p)].median()) for p in PORTS) + " |")
    return b


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fill-protocol", action="store_true",
                    help="also replace the GENERATED blocks in docs/experiments/07-protocol-v2.md")
    cli = ap.parse_args()

    H = heuristic_table()
    blocks = {"heur": heur_block(H), "mde": mde_block(H, tuning_sds()),
              "sweep": sweep_block(), "sla": sla_block()}

    md = ["# Final-sweep planning numbers", "",
          "DIAGNOSTIC, bukan untuk paper. Generated by `scripts/final_plan_stats.py`.", ""]
    for name, b in blocks.items():
        md += [f"## {name}", ""] + b + [""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))
    print(f"-> {OUT}")

    if cli.fill_protocol:
        text = PROTOCOL.read_text(encoding="utf-8")
        for name, b in blocks.items():
            pat = re.compile(rf"(<!-- BEGIN GENERATED {name} -->\n).*?(<!-- END GENERATED {name} -->)",
                             re.S)
            assert pat.search(text), f"marker for {name} missing in {PROTOCOL.name}"
            text = pat.sub(lambda m: m.group(1) + "\n".join(b) + "\n" + m.group(2), text)
        PROTOCOL.write_text(text, encoding="utf-8")
        print(f"-> {PROTOCOL} (GENERATED blocks filled)")


if __name__ == "__main__":
    main()
