"""Delay medians behind the SLA thresholds, for the note under Table II of the paper.

    python scripts/sla_medians.py

Reads the real trace exactly as scripts/final_plan_stats.py:sla_block does (semicolon
separator, decimal comma, quotes stripped) and applies no filter: negative one-way delays, which
come from clock offset, are kept, as in every other median reported for this trace. Prints:

  thresholds         slice_env.DEFAULT_SLA_MS
  full trace         all 1022 rows; these are the values of the sensitivity point that
                     analyze_v2.py calls real_train_median (a misnomer, see protocol 8.2)
  train split        rows 0..612, the first 60 percent, as split_arrivals() cuts it
  V1 synthetic       Reinforcement Learning/final/synthetic_15k_complete_final.csv
and, for the full trace and the train split, the count and percentage of negative one-way
delays per port; the maximum of the trace's drop columns and its policing rates; then the same per port and per log format for the raw listener log
pengujian/delay_log.csv, with the time span of each, next to the time span of the trace.
"""

import io
from pathlib import Path

import pandas as pd

from slice_env import DEFAULT_SLA_MS, DEFAULT_TRACE, PORTS

REPO_ROOT = Path(__file__).resolve().parents[1]
V1_SYNTH = REPO_ROOT / "Reinforcement Learning" / "final" / "synthetic_15k_complete_final.csv"
TRAIN_FRAC = 0.6                     # protocol section 1; train_online.py --split default


def real_trace():
    raw = DEFAULT_TRACE.read_text(encoding="utf-8", errors="ignore").splitlines()
    return pd.read_csv(io.StringIO("\n".join(ln.strip().replace('"', "") for ln in raw)),
                       sep=";", decimal=",")


def medians(df):
    return [round(float(df[f"delay_ms_{p}"].median()), 2) for p in PORTS]


def negatives(df):
    """Count and percentage of negative one-way delays per port: physically impossible, they
    show that the measured delay is dominated by clock offset between sender and collector."""
    return [(int((df[f"delay_ms_{p}"] < 0).sum()), round(float((df[f"delay_ms_{p}"] < 0).mean() * 100), 2))
            for p in PORTS]


DELAY_LOG = REPO_ROOT / "pengujian" / "delay_log.csv"
DEVICE_PORT = {"dht11": "p1", "camera": "p2", "max": "p4"}     # protocol A1


def delay_log_negatives():
    """Raw per-packet one-way delays from the listener log, three stacked formats:
    4 fields (timestamp, device, ip, delay) and 6 or 7 fields (delay in the 6th).
    Returns {(fields, port): [first ts, last ts, n, n negative]}."""
    out = {}
    for ln in DELAY_LOG.read_text(encoding="utf-8", errors="ignore").splitlines():
        f = ln.strip().split(",")
        if f[0] == "timestamp" or len(f) not in (4, 6, 7):
            continue
        delay = float(f[3] if len(f) == 4 else f[5])
        rec = out.setdefault((len(f), DEVICE_PORT[f[1]]), [f[0], f[0], 0, 0])
        rec[0], rec[1] = min(rec[0], f[0]), max(rec[1], f[0])
        rec[2] += 1
        rec[3] += delay < 0
    return out


def main():
    real = real_trace()
    n_train = int(len(real) * TRAIN_FRAC)
    train = real.iloc[:n_train]
    print("median one-way delay (ms), ports", PORTS)
    print(f"{'thresholds (slice_env)':28s} {'-':>6s}", [DEFAULT_SLA_MS[p] for p in PORTS])
    for name, df in [("full real trace", real),
                     (f"real train split, rows 0-{n_train - 1}", train),
                     ("V1 synthetic dataset", pd.read_csv(V1_SYNTH))]:
        print(f"{name:28s} {len(df):6d}", medians(df))
    print("negative one-way delays (count, percent), ports", PORTS)
    for name, df in [("full real trace", real), (f"real train split, rows 0-{n_train - 1}", train)]:
        print(f"{name:28s} {len(df):6d}", negatives(df))
    print(f"trace collected {real['timestamp'].iloc[0]} .. {real['timestamp'].iloc[-1]}")
    print("trace drop column max and policing rates (kbps), ports", PORTS,
          [float(real[f"drop_{p}"].max()) for p in PORTS],
          [sorted(real[f"policing_rate_kbps_{p}"].unique().tolist()) for p in PORTS])
    log = delay_log_negatives()
    print(f"raw listener log {DELAY_LOG.name}: fields, port, first, last, n, negative, percent")
    for (fields, port), (t0, t1, n, neg) in sorted(log.items()):
        print(f"  {fields} {port} {t0} {t1} {n:6d} {neg:6d} {neg / n * 100:6.2f}")
    n_all, neg_all = sum(v[2] for v in log.values()), sum(v[3] for v in log.values())
    print(f"  all {n_all} rows, {neg_all} negative, {neg_all / n_all * 100:.2f} percent")


if __name__ == "__main__":
    main()
