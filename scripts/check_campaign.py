"""Validity gate for a policing-rate sweep campaign.

Runs the six checks in docs/experiments/03-measurement-campaign.md section 6
against a freshly collected dataset_dqn_rich.csv. Exits non-zero if any
BLOCKING check fails, so the data cannot silently be used to calibrate a
simulator.

The old campaign fails checks 1 and 4 by construction -- that is the point.
Run it against the old file to see what the gate is guarding against:

    python scripts/check_campaign.py "Reinforcement Learning/revision/dataset_dqn_rich.csv"
"""

import argparse
import io
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PORTS = ["p1", "p2", "p4"]


def load_collector_csv(path):
    """collect_policy.sh writes ';'-delimited with ',' decimals, and the header
    can arrive wrapped in a single pair of double quotes."""
    raw = Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
    cleaned = [ln.strip().replace('"', "") for ln in raw]
    return pd.read_csv(io.StringIO("\n".join(cleaned)), sep=";", decimal=",")


class Report:
    def __init__(self):
        self.rows = []

    def add(self, n, name, ok, blocking, detail):
        self.rows.append((n, name, ok, blocking, detail))

    def render(self):
        worst = 0
        for n, name, ok, blocking, detail in self.rows:
            if ok:
                tag = "PASS"
            elif blocking:
                tag = "FAIL"
                worst = max(worst, 2)
            else:
                tag = "WARN"
                worst = max(worst, 1)
            print(f"[{tag}] {n}. {name}")
            for line in detail:
                print(f"       {line}")
        return worst


def check_action_variance(df, rep):
    detail, ok = [], True
    for p in PORTS:
        col = f"policing_rate_kbps_{p}"
        if col not in df:
            detail.append(f"{col}: MISSING")
            ok = False
            continue
        n = df[col].nunique()
        detail.append(f"{col}: nunique={n}, min={df[col].min():.0f}, max={df[col].max():.0f}")
        if n < 10:
            ok = False
    if not ok:
        detail.append("-> control variable was not swept; data carries no action information")
    rep.add(1, "Action variance present (nunique >= 10 per port)", ok, True, detail)


def check_negative_delay(df, rep):
    detail, ok = [], True
    for p in PORTS:
        col = f"delay_ms_{p}"
        if col not in df:
            detail.append(f"{col}: MISSING")
            ok = False
            continue
        neg = int((df[col] < 0).sum())
        pct = 100.0 * neg / max(len(df), 1)
        detail.append(f"{col}: {neg} negative ({pct:.2f}%), min={df[col].min():.3f} ms")
        if neg:
            ok = False
    if not ok:
        detail.append("-> one-way delay cannot be negative; clocks are not synchronised")
    rep.add(2, "Zero negative delays (clock sync)", ok, True, detail)


def check_monotonicity(df, rep):
    """Delay p50 should rise as the rate falls, at least below the traffic demand."""
    detail, ok = [], True
    for p in PORTS:
        rate_col, delay_col = f"policing_rate_kbps_{p}", f"delay_ms_{p}"
        if rate_col not in df or delay_col not in df:
            detail.append(f"{p}: MISSING columns")
            ok = False
            continue
        g = df.groupby(rate_col)[delay_col].median().sort_index()
        if len(g) < 3:
            detail.append(f"{p}: only {len(g)} distinct rate(s) -- cannot assess")
            ok = False
            continue
        rho = np.corrcoef(pd.Series(g.index).rank(), pd.Series(g.values).rank())[0, 1]
        lo, hi = g.iloc[0], g.iloc[-1]
        detail.append(
            f"{p}: spearman(rate, median delay) = {rho:+.3f} | "
            f"delay at lowest rate {lo:.3f} ms vs highest rate {hi:.3f} ms"
        )
        if not (rho < -0.3 and lo > hi):
            ok = False
    if not ok:
        detail.append("-> policing rate does not move delay; the control premise fails")
    rep.add(3, "Delay responds monotonically to rate", ok, True, detail)


def check_drops(df, rep):
    detail, ok = [], True
    for p in PORTS:
        drop_col, rate_col = f"drop_{p}", f"policing_rate_kbps_{p}"
        if drop_col not in df:
            detail.append(f"{drop_col}: MISSING")
            ok = False
            continue
        total = float(df[drop_col].sum())
        detail.append(f"{drop_col}: total={total:.0f}, nonzero rows={int((df[drop_col] > 0).sum())}")
        if rate_col in df:
            low = df[df[rate_col] <= 2000]
            if len(low):
                d = float(low[drop_col].sum())
                detail.append(f"  at rate <= 2000 kbps: {len(low)} rows, drops={d:.0f}")
                if d <= 0:
                    ok = False
            else:
                detail.append("  no rows at rate <= 2000 kbps to test")
                ok = False
        if total <= 0:
            ok = False
    if not ok:
        detail.append("-> no drops even when starved; policing may not be active")
    rep.add(4, "Drops appear at low rate (policing actually active)", ok, True, detail)


def check_repeatability(df, rep):
    detail, ok = [], True
    for p in PORTS:
        rate_col, delay_col = f"policing_rate_kbps_{p}", f"delay_ms_{p}"
        if rate_col not in df or delay_col not in df:
            continue
        g = df.groupby(rate_col)[delay_col].agg(["median", "std", "count"])
        g = g[g["count"] >= 5]
        if g.empty:
            detail.append(f"{p}: not enough samples per rate")
            ok = False
            continue
        rel = (g["std"] / g["median"].abs().replace(0, np.nan)).median()
        detail.append(f"{p}: median relative spread within a rate = {rel:.3f}")
        if not (rel < 0.5):
            ok = False
    rep.add(5, "Repeatable within a rate setting (rel. spread < 0.5)", ok, False, detail)


def check_coupling(df, rep):
    """Does constraining one port move another port's delay?"""
    detail, ok = [], True
    for target in PORTS:
        rate_col = f"policing_rate_kbps_{target}"
        if rate_col not in df:
            continue
        constrained = df[df[rate_col] <= 2000]
        free = df[df[rate_col] >= 100000]
        if not len(constrained) or not len(free):
            detail.append(f"{target}: no constrained/free contrast available")
            ok = False
            continue
        for o in [q for q in PORTS if q != target]:
            dcol = f"delay_ms_{o}"
            if dcol not in df:
                continue
            a, b = constrained[dcol].median(), free[dcol].median()
            detail.append(
                f"{target} constrained -> {o} median delay {a:.3f} ms "
                f"vs {b:.3f} ms when {target} free (delta {a - b:+.3f})"
            )
    detail.append("(informational: zero coupling is a valid finding, report it honestly)")
    rep.add(6, "Cross-port coupling measured", ok, False, detail)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dataset", help="dataset_dqn_rich.csv produced by collect_policy.sh")
    args = p.parse_args()

    df = load_collector_csv(args.dataset)
    print(f"{args.dataset}: {len(df)} rows, {len(df.columns)} columns\n")

    rep = Report()
    check_action_variance(df, rep)
    check_negative_delay(df, rep)
    check_monotonicity(df, rep)
    check_drops(df, rep)
    check_repeatability(df, rep)
    check_coupling(df, rep)

    worst = rep.render()
    print()
    if worst >= 2:
        print("VERDICT: BLOCKING failures. Do not calibrate anything on this data.")
        return 1
    if worst == 1:
        print("VERDICT: passes blocking checks, with warnings. Review before proceeding.")
        return 0
    print("VERDICT: all checks pass. Data is usable for calibration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
