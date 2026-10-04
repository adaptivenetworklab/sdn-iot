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


def main():
    real = real_trace()
    n_train = int(len(real) * TRAIN_FRAC)
    print(f"{'thresholds (slice_env)':28s} {'-':>6s}", [DEFAULT_SLA_MS[p] for p in PORTS])
    for name, df in [("full real trace", real),
                     (f"real train split, rows 0-{n_train - 1}", real.iloc[:n_train]),
                     ("V1 synthetic dataset", pd.read_csv(V1_SYNTH))]:
        print(f"{name:28s} {len(df):6d}", medians(df))


if __name__ == "__main__":
    main()
