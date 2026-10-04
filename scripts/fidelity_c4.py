"""Generator fidelity, protocol v2 section 6.2 (C4). Reporting only; train and val, never test.

    python scripts/fidelity_c4.py

Specified before the final sweep (section 6.2), implemented after it as a recorded
deviation (08-results-v2.md section 5.3). Two comparisons, same metrics:

  bound   real train vs real val: how far two pieces of the real trace differ
  synth   synthetic trace vs real train: the training data of aug_subsample vs real_only

The data are taken through train_online.split_arrivals(), so each series is exactly
what the arms trained or probed on. Metrics per slice: two-sample KS statistic D and
Wasserstein-1 (Mbps) on the marginal; |ACF difference| at lags 1-10 (mean and max over
lags). Discriminator AUC on sliding 50 x 3 windows: standardised logistic regression,
5-fold stratified CV without shuffling, so each fold is a contiguous block of each
series (overlapping windows only leak at fold borders); 0.5 = indistinguishable.
Plus descriptive statistics of each series. Writes results/analysis-v2/fidelity_c4*.
"""

import hashlib
import sys
from argparse import Namespace
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import ks_2samp, wasserstein_distance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_synth_trace import WINDOW, windows  # noqa: E402
from slice_env import PORTS, load_arrival_trace  # noqa: E402
from train_online import REPO_ROOT, split_arrivals  # noqa: E402

OUT = REPO_ROOT / "results" / "analysis-v2"
SYNTH = REPO_ROOT / "data" / "synth" / "train_synth_trace.csv"
SYNTH_MD5 = "7687de3b3b66977cf49c813d22939bf1"     # attempt 1, protocol section 6 (K6)
LAGS = range(1, 11)


def acf(x, k):
    x = x - x.mean()
    return float((x[:-k] * x[k:]).sum() / (x * x).sum())


def auc(a, b):
    wa, wb = windows(a, WINDOW), windows(b, WINDOW)
    X, y = np.vstack([wa, wb]), np.r_[np.zeros(len(wa)), np.ones(len(wb))]
    clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
    folds = []
    for tr, te in StratifiedKFold(5, shuffle=False).split(X, y):
        clf.fit(X[tr], y[tr])
        folds.append(roc_auc_score(y[te], clf.predict_proba(X[te])[:, 1]))
    return float(np.mean(folds)), float(np.std(folds)), len(X)


def data():
    assert hashlib.md5(SYNTH.read_bytes()).hexdigest() == SYNTH_MD5, "synthetic trace is not attempt 1"
    trace = load_arrival_trace()
    base = dict(phase="train", eval_phase="val", allow_test=False, split="0.6,0.2,0.2")
    real_train, _, real_val, _ = split_arrivals(trace, Namespace(**base, arm="real_only"))
    synth, *_ = split_arrivals(trace, Namespace(**base, arm="aug_subsample"))
    # test never enters: val ends where test starts
    assert len(real_train) + len(real_val) == int(len(trace) * 0.8)
    assert np.array_equal(real_val, trace[len(real_train):len(real_train) + len(real_val)])
    return {"riil-train (real_only)": real_train, "sintetis (aug_subsample)": synth,
            "riil-val": real_val}


def main():
    s = data()
    pairs = {"batas: riil-train vs riil-val": (s["riil-train (real_only)"], s["riil-val"]),
             "sintetis vs riil-train": (s["sintetis (aug_subsample)"], s["riil-train (real_only)"])}
    rows, acf_rows = [], []
    for name, (a, b) in pairs.items():
        for i, port in enumerate(PORTS):
            d = [abs(acf(a[:, i], k) - acf(b[:, i], k)) for k in LAGS]
            acf_rows += [{"perbandingan": name, "slice": port, "lag": k, "acf_a": acf(a[:, i], k),
                          "acf_b": acf(b[:, i], k), "abs_diff": dk} for k, dk in zip(LAGS, d)]
            rows.append({"perbandingan": name, "slice": port,
                         "KS D": ks_2samp(a[:, i], b[:, i]).statistic,
                         "W1 (Mbps)": wasserstein_distance(a[:, i], b[:, i]),
                         "|dACF| rata2 lag 1-10": np.mean(d), "|dACF| maks lag 1-10": np.max(d)})
        m, sd, n = auc(a, b)
        rows.append({"perbandingan": name, "slice": "semua (jendela 50x3)",
                     "AUC discriminator (5-fold)": m, "AUC sd antar fold": sd, "jumlah jendela": n})
    met = pd.DataFrame(rows)
    desc = pd.DataFrame([{"data": k, "slice": port, "baris": len(v), "mean": v[:, i].mean(),
                          "sd": v[:, i].std(ddof=1), "min": v[:, i].min(),
                          "p5": np.percentile(v[:, i], 5), "p50": np.median(v[:, i]),
                          "p95": np.percentile(v[:, i], 95), "max": v[:, i].max()}
                         for k, v in s.items() for i, port in enumerate(PORTS)])

    OUT.mkdir(parents=True, exist_ok=True)
    met.to_csv(OUT / "fidelity_c4.csv", index=False)
    pd.DataFrame(acf_rows).to_csv(OUT / "fidelity_c4_acf.csv", index=False)
    desc.to_csv(OUT / "fidelity_c4_desc.csv", index=False)
    marg = met[met["slice"].isin(PORTS)].dropna(axis=1, how="all")
    disc = met[~met["slice"].isin(PORTS)].dropna(axis=1, how="all")
    md = ("# Fidelitas generator (C4)\n\n## Marginal dan ACF\n\n"
          + marg.to_markdown(index=False, floatfmt=".3f")
          + "\n\n## Discriminator\n\n" + disc.to_markdown(index=False, floatfmt=".3f")
          + "\n\n## Deskriptif\n\n" + desc.to_markdown(index=False, floatfmt=".3f") + "\n")
    (OUT / "fidelity_c4.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
