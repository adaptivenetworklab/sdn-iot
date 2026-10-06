"""Input statistics of the var_matched arm. No method is trained or evaluated.

Per port: mean, std (ddof 0, as used by run_v3.var_matched) and lag-1
autocorrelation for the real train rows, the synthetic trace (attempt 1) and
the var_matched rows, plus the number of clipped values and rows. Only the
train split and the synthetic trace are read.

    python scripts_v3/var_matched_stats.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts_v3"))
import run_v3  # noqa: E402
from slice_env import PORTS, load_arrival_trace  # noqa: E402

OUT = ROOT / "results" / "v3" / "var_matched_stats.csv"


def acf1(x):
    return float(np.corrcoef(x[:-1], x[1:])[0, 1])


def main():
    trace = load_arrival_trace()
    n_train = int(len(trace) * 0.6)                 # split "0.6,0.2,0.2", train_online.py:557-560
    train = trace[:n_train]
    synth = run_v3.load_synth()
    vm, info = run_v3.var_matched(train, synth)
    rows = []
    for name, arr in (("real_train", train), ("synthetic", synth), ("var_matched", vm)):
        for i, p in enumerate(PORTS):
            rows.append({"data": name, "port": p, "rows": len(arr), "mean": arr[:, i].mean(),
                         "std": arr[:, i].std(), "acf1": acf1(arr[:, i])})
    df = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(df.to_string(index=False, float_format=lambda v: f"{v:.4f}"))
    print(f"scale per port: {[round(s, 4) for s in info['scale']]}")
    print(f"clipped values per port: {info['clipped_values_per_port']}, "
          f"clipped rows: {info['clipped_rows']} of {info['rows']}")
    print(f"written {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
