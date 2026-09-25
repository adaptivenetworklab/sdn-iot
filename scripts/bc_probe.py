"""Behaviour-cloning probe: can the PPO actor express demand_prop at all?

DIAGNOSTIC -- not for the paper.

The pilot showed PPO and SDH-PPO stuck around 44% violation while the one-line
demand_prop heuristic reached 32%. Two explanations are possible: the policy
class cannot represent the heuristic, or it can but the RL optimisation never
finds it. This separates them.

Trains the same Actor used by run_ppo, supervised, to match demand_prop's action
on the train split, then evaluates the cloned policy on val.

Reading the result (fixed before running):
  * BC lands near demand_prop  -> representation is fine; PPO's failure is
    optimisation and exploration, which is where the tuning grid should aim.
  * BC lands far above         -> a representation or observability limit we
    have not yet identified, and the tuning grid would be wasted.

    python scripts/bc_probe.py
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_env import SliceEnv, load_arrival_trace  # noqa: E402
from train_online import Actor, Normalizer, heuristic_action  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
BANNER = "DIAGNOSTIC - not for paper"


def make_env(arrivals, args, seed):
    return SliceEnv(arrivals, link_capacity_mbps=args.capacity, episode_len=args.episode_len,
                    seed=seed, random_init_alloc=True, reward_scale=args.reward_scale)


def collect(env, norm, mean_demand, n_steps):
    """States visited under demand_prop, paired with the action it chose.

    Cloning on demand_prop's own state distribution is the right target: the
    question is whether the network can express the mapping, not whether it is
    robust off-distribution.
    """
    S, A = [], []
    s = norm(env.reset())
    for _ in range(n_steps):
        a = heuristic_action("demand_prop", env, mean_demand)
        S.append(s)
        A.append(a)
        ns, _, done, _ = env.step(a)
        s = norm(env.reset() if done else ns)
    return np.array(S, dtype=np.float32), np.array(A, dtype=np.float32)


def evaluate(policy, env, norm, episodes, ep_len):
    viol = []
    for _ in range(episodes):
        s = norm(env.reset())
        for _ in range(ep_len):
            ns, _, _, info = env.step(policy(env, s))
            viol.append(info["violation"])
            s = norm(ns)
    return float(np.mean(viol) * 100)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--seeds", type=int, default=2)
    p.add_argument("--bc-steps", type=int, default=20000, help="transitions collected")
    p.add_argument("--epochs", type=int, default=200)
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--capacity", type=float, default=12.0)
    p.add_argument("--episode-len", type=int, default=50)
    p.add_argument("--eval-episodes", type=int, default=20)
    p.add_argument("--reward-scale", type=float, default=19.0106)
    p.add_argument("--split", default="0.6,0.2,0.2")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "diag2")
    args = p.parse_args()

    trace = load_arrival_trace()
    f_tr, f_va, _ = (float(x) for x in args.split.split(","))
    n = len(trace)
    a, b = int(n * f_tr), int(n * (f_tr + f_va))
    train, val = trace[:a], trace[a:b]
    mean_demand = train.mean(axis=0)          # train only, as the protocol requires

    rows = []
    for seed in range(args.seeds):
        torch.manual_seed(seed)
        np.random.seed(seed)

        tr_env = make_env(train, args, seed)
        norm = Normalizer(tr_env)
        S, A = collect(tr_env, norm, mean_demand, args.bc_steps)

        actor = Actor(tr_env.state_dim, tr_env.action_dim)
        opt = torch.optim.Adam(actor.parameters(), lr=args.lr)
        St, At = torch.as_tensor(S), torch.as_tensor(A)

        idx = np.arange(len(St))
        loss_val = float("nan")
        for _ in range(args.epochs):
            np.random.shuffle(idx)
            for k in range(0, len(idx), args.batch_size):
                bidx = idx[k:k + args.batch_size]
                mu, _ = actor(St[bidx])
                loss = nn.MSELoss()(mu, At[bidx])
                opt.zero_grad()
                loss.backward()
                opt.step()
            loss_val = loss.item()

        def cloned(e, st):
            with torch.no_grad():
                mu, _ = actor(torch.as_tensor(st, dtype=torch.float32).unsqueeze(0))
            return mu.squeeze(0).numpy()

        v_bc = evaluate(cloned, make_env(val, args, seed + 10_000), norm,
                        args.eval_episodes, args.episode_len)
        v_dp = evaluate(lambda e, st: heuristic_action("demand_prop", e, mean_demand),
                        make_env(val, args, seed + 10_000), norm,
                        args.eval_episodes, args.episode_len)

        rows.append({"seed": seed, "bc_mse_final": loss_val,
                     "viol_bc": v_bc, "viol_demand_prop": v_dp, "delta": v_bc - v_dp})
        print(f"seed {seed}: BC mse={loss_val:.5f} | val viol BC={v_bc:.2f} "
              f"demand_prop={v_dp:.2f} delta={v_bc - v_dp:+.2f}")

    df = pd.DataFrame(rows)
    df.insert(0, "note", BANNER)
    args.out.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out / "bc_probe.csv", index=False)

    print()
    print(BANNER)
    print(f"mean val violation  BC={df.viol_bc.mean():.2f}  "
          f"demand_prop={df.viol_demand_prop.mean():.2f}  delta={df.delta.mean():+.2f}")
    print(f"-> {args.out / 'bc_probe.csv'}")


if __name__ == "__main__":
    main()
