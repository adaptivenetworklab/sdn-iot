"""WGAN-GP generator for synthetic arrival traces.

Feeds the real_only / aug_subsample arms of protocol v2. Trained on sliding
windows of rx_mbps from the TRAIN split only, so nothing from val or test can
reach the generator.

Difference from the V1 augmentation this replaces: that one generated rows of a
(state, action, reward, next_state) dataset and then overwrote the policing-rate
column with np.random.uniform after the generator had run, which is where the
fake action variance came from. Here the generator produces an arrival time
series only. Policing rate is the agent's action, not a data column, so there is
nothing to overwrite.

Architecture and hyperparameters follow DataAugmentation.ipynb: latent 100,
GP lambda 10, lr 1e-4, betas (0.5, 0.9), batch 64, 301 epochs, generator updated
every 5 epochs.

    python scripts/make_synth_trace.py
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from scipy.stats import ks_2samp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_env import PORTS, load_arrival_trace  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
LATENT = 100
WINDOW = 50          # matches episode_len, so one sample is one episode of arrivals

# Pass thresholds for the single mode-collapse repair attempt. FIXED BEFORE
# the attempt was run and not revised afterwards. All three must hold for all
# three slices, computed on the TRAIN split only. The first attempt failed the
# std criterion outright: ratios 0.336 / 0.348 / 0.341.
PASS_STD_RATIO = (0.80, 1.25)     # synthetic std / real std, per slice
PASS_KS_D = 0.15                  # two-sample KS statistic on the marginal
PASS_ACF1_DIFF = 0.15             # |lag-1 autocorrelation difference|


class Generator(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.main = nn.Sequential(
            nn.Linear(in_dim, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, out_dim),
        )

    def forward(self, z):
        return self.main(z)


class Critic(nn.Module):
    """WGAN-GP critic with a minibatch-standard-deviation feature.

    Repair attempt for the mode collapse of the first generator (synthetic std
    collapsed to a third of the real std). The extra input is the mean
    per-feature std across the batch, so a batch of near-identical samples is
    directly distinguishable from a real batch and the generator is pushed to
    keep spread. Standard anti-collapse device; it costs one scalar.
    """

    def __init__(self, in_dim, minibatch_std=True):
        super().__init__()
        self.minibatch_std = minibatch_std
        self.main = nn.Sequential(
            nn.Linear(in_dim + int(minibatch_std), 512), nn.LeakyReLU(0.2),
            nn.Linear(512, 256), nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
        )

    def forward(self, x):
        if self.minibatch_std:
            sd = x.std(dim=0, unbiased=False).mean().expand(x.size(0), 1)
            x = torch.cat([x, sd], dim=1)
        return self.main(x)


def gradient_penalty(critic, real, fake):
    alpha = torch.rand(real.size(0), 1)
    mid = (alpha * real + (1 - alpha) * fake).requires_grad_(True)
    d = critic(mid)
    g = torch.autograd.grad(outputs=d, inputs=mid, grad_outputs=torch.ones_like(d),
                            create_graph=True, retain_graph=True)[0]
    return ((g.norm(2, dim=1) - 1) ** 2).mean()


def windows(trace, w):
    """Sliding windows, flattened to (n, w * n_slices)."""
    n = len(trace) - w + 1
    return np.stack([trace[i:i + w].reshape(-1) for i in range(n)])


def quality(real, synth):
    """Distribution metrics against the thresholds fixed at the top of the file."""
    out, ok = {}, True
    for i, port in enumerate(PORTS):
        r, g = real[:, i], synth[:, i]
        ratio = float(g.std() / r.std())
        d = float(ks_2samp(r, g).statistic)
        acf_r = float(np.corrcoef(r[:-1], r[1:])[0, 1])
        acf_g = float(np.corrcoef(g[:-1], g[1:])[0, 1])
        dacf = abs(acf_g - acf_r)
        passed = (PASS_STD_RATIO[0] <= ratio <= PASS_STD_RATIO[1]
                  and d <= PASS_KS_D and dacf <= PASS_ACF1_DIFF)
        ok &= passed
        out[port] = {"std_ratio": ratio, "ks_d": d, "acf1_real": acf_r,
                     "acf1_synth": acf_g, "acf1_diff": dacf, "pass": bool(passed)}
    return ok, out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--split", default="0.6,0.2,0.2")
    p.add_argument("--epochs", type=int, default=301)
    p.add_argument("--batch-size", type=int, default=64)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--gp-lambda", type=float, default=10.0)
    p.add_argument("--n-critic", type=int, default=5,
                   help="critic updates per generator update, counted in BATCHES. The "
                        "first attempt gated on epoch %% 5, so the generator trained "
                        "during one epoch in five instead of at a 5:1 batch ratio. "
                        "Deliberate deviation from DataAugmentation.ipynb.")
    p.add_argument("--window", type=int, default=WINDOW)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", type=Path, default=REPO_ROOT / "data" / "synth")
    args = p.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    trace = load_arrival_trace()
    f_tr = float(args.split.split(",")[0])
    train = trace[:int(len(trace) * f_tr)]
    n_slices = train.shape[1]

    X = windows(train, args.window)
    mu, sd = X.mean(axis=0), X.std(axis=0) + 1e-8      # fitted on train windows only
    Xs = (X - mu) / sd
    dim = Xs.shape[1]

    gen = Generator(LATENT, dim)
    critic = Critic(dim)
    og = torch.optim.Adam(gen.parameters(), lr=args.lr, betas=(0.5, 0.9))
    oc = torch.optim.Adam(critic.parameters(), lr=args.lr, betas=(0.5, 0.9))
    loader = torch.utils.data.DataLoader(torch.FloatTensor(Xs), batch_size=args.batch_size,
                                         shuffle=True, drop_last=True)

    loss_g = torch.tensor(float("nan"))
    batches = 0
    for epoch in range(args.epochs):
        for real in loader:
            z = torch.randn(real.size(0), LATENT)
            fake = gen(z)
            loss_c = (critic(fake.detach()).mean() - critic(real).mean()
                      + args.gp_lambda * gradient_penalty(critic, real, fake.detach()))
            oc.zero_grad(); loss_c.backward(); oc.step()
            batches += 1
            if batches % args.n_critic == 0:
                loss_g = -critic(gen(z)).mean()
                og.zero_grad(); loss_g.backward(); og.step()
        if epoch % 100 == 0:
            print(f"epoch {epoch:4d} | critic {loss_c.item():+.4f} | gen {loss_g.item():+.4f}")

    n_windows = int(np.ceil(len(train) / args.window))
    with torch.no_grad():
        z = torch.randn(n_windows, LATENT)
        synth = gen(z).numpy() * sd + mu
    synth = synth.reshape(-1, n_slices)[:len(train)]
    synth = np.clip(synth, 0.0, None)          # arrivals cannot be negative

    args.out.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(synth, columns=[f"rx_mbps_{p_}" for p_ in PORTS])
    csv = args.out / "train_synth_trace.csv"
    df.to_csv(csv, index=False)

    ok, qual = quality(train, synth)
    meta = {
        "source": "train split only", "rows": int(len(df)), "window": args.window,
        "epochs": args.epochs, "latent": LATENT, "gp_lambda": args.gp_lambda,
        "seed": args.seed, "n_critic": args.n_critic, "minibatch_std": True,
        "thresholds": {"std_ratio": list(PASS_STD_RATIO), "ks_d": PASS_KS_D,
                       "acf1_diff": PASS_ACF1_DIFF},
        "quality": qual, "passed": bool(ok),
        "real_mean_mbps": train.mean(axis=0).tolist(),
        "synth_mean_mbps": synth.mean(axis=0).tolist(),
        "real_std_mbps": train.std(axis=0).tolist(),
        "synth_std_mbps": synth.std(axis=0).tolist(),
    }
    (args.out / "train_synth_trace.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"\nreal  mean {np.round(train.mean(axis=0), 3)} std {np.round(train.std(axis=0), 3)}")
    print(f"synth mean {np.round(synth.mean(axis=0), 3)} std {np.round(synth.std(axis=0), 3)}")
    (args.out / "train_synth_trace_quality.json").write_text(
        json.dumps({"thresholds": meta["thresholds"], "quality": qual, "passed": bool(ok)},
                   indent=2), encoding="utf-8")
    for port, m in qual.items():
        print(f"{port}: std_ratio {m['std_ratio']:.3f} | ks_d {m['ks_d']:.3f} | "
              f"acf1_diff {m['acf1_diff']:.3f} | {'PASS' if m['pass'] else 'FAIL'}")
    print(f"VERDICT: {'PASS' if ok else 'FAIL'}")
    print(f"-> {csv} ({len(df)} rows)")


if __name__ == "__main__":
    main()
