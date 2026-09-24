"""Online RL training and evaluation in the queueing simulator (slice_env).

This is the replacement experiment, NOT a port. scripts/sweep.py is kept
unchanged so check_fidelity.py can still prove the old notebook was reproduced
faithfully; this file is the honest re-run.

Differences from the old pipeline, each fixing a defect recorded in
docs/experiments/00-contamination-audit.md:

  old                                        new
  ---------------------------------------    ----------------------------------
  delay = raw * (1 - k*a), k keyed by name    finite-buffer queue, one model for
                                              every method
  next_state read from the log                next_state produced by the env, so
                                              the action actually matters
  reward independent of the action            reward computed from the state the
                                              action produced
  1-D action, DQN capped at +-0.1             3-D action, identical [-1,1] range
                                              for every method
  old_log_probs = current.detach()            log-probs stored at rollout time,
                                              so the PPO ratio is real
  mask compared z-scores against ms           state carries delay in ms, so the
                                              safety layer compares like with
                                              like
  dueling head with action_dim=1 (vacuous)    branching Q with 21 bins per
                                              slice, so the decomposition means
                                              something
"""

import argparse
import json
import platform
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_env import PORTS, SliceEnv, load_arrival_trace  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
LEARNERS = ["ppo", "sdhppo", "dqn", "ddqn"]
HEURISTICS = ["no_control", "const_max", "threshold", "demand_prop", "equal_split"]
ALGOS = LEARNERS + HEURISTICS
# no_mask is V1-only; V2 expresses the safety layer as the orthogonal --safety
# factor so every method can be run with and without it.
ARMS = ["full", "no_mask", "no_dueling", "real_only", "aug_subsample"]
PHASES = ["train", "val", "test"]

LABEL = {
    "sdhppo": "Proposed (SDH-PPO)", "ppo": "PPO Standard", "dqn": "DQN", "ddqn": "DDQN",
    "no_control": "No Control", "const_max": "Const Max", "threshold": "Threshold",
    "equal_split": "Equal Split",
    "demand_prop": "Demand Proportional",
}


# ---------------------------------------------------------------- utilities
class Normalizer:
    """Fixed, method-independent state scaling. Fixed rather than running so
    every algorithm sees identical inputs and no method gains from a better
    adapted normaliser."""

    def __init__(self, env):
        n = env.n
        self.scale = np.concatenate([
            np.full(n, 10.0),                                    # arrival Mbps
            np.full(n, 2.0),                                     # utilisation
            np.array([env.sla[p] for p in PORTS], dtype=float),  # delay, in SLA units
            np.full(n, env.C),                                   # rate Mbps
        ])

    def __call__(self, s):
        return np.asarray(s, dtype=np.float32) / self.scale


def mlp(inp, out, hidden=(256, 128), act=nn.ReLU):
    layers, prev = [], inp
    for h in hidden:
        layers += [nn.Linear(prev, h), act()]
        prev = h
    layers.append(nn.Linear(prev, out))
    return nn.Sequential(*layers)


class Actor(nn.Module):
    def __init__(self, state_dim, action_dim, hidden=(256, 128)):
        super().__init__()
        self.body = mlp(state_dim, action_dim, hidden)
        self.log_std = nn.Parameter(torch.zeros(action_dim) - 0.5)

    def forward(self, x):
        return torch.tanh(self.body(x)), self.log_std.exp()


class Critic(nn.Module):
    """dueling=True keeps the paper's value/advantage split. With a state-value
    critic the decomposition is still only cosmetic, so the no_dueling arm
    measures exactly that."""

    def __init__(self, state_dim, hidden=(256, 128), dueling=True):
        super().__init__()
        self.dueling = dueling
        self.base = mlp(state_dim, hidden[-1], hidden[:-1])
        self.v = nn.Linear(hidden[-1], 1)
        if dueling:
            self.a = nn.Linear(hidden[-1], 1)

    def forward(self, x):
        h = torch.relu(self.base(x))
        v = self.v(h)
        if self.dueling:
            a = self.a(h)
            return v + (a - a.mean(dim=0, keepdim=True))
        return v


class BranchingQ(nn.Module):
    """One Q head per slice (branching DQN). Sidesteps the bins**3 blow-up of a
    joint discrete action and gives each branch a genuine dueling split."""

    def __init__(self, state_dim, n_branch, n_bins, hidden=(256, 128), dueling=False):
        super().__init__()
        self.n_branch, self.n_bins, self.dueling = n_branch, n_bins, dueling
        self.base = mlp(state_dim, hidden[-1], hidden[:-1])
        self.adv = nn.Linear(hidden[-1], n_branch * n_bins)
        if dueling:
            self.val = nn.Linear(hidden[-1], n_branch)

    def forward(self, x):
        h = torch.relu(self.base(x))
        a = self.adv(h).view(-1, self.n_branch, self.n_bins)
        if self.dueling:
            v = self.val(h).view(-1, self.n_branch, 1)
            return v + (a - a.mean(dim=2, keepdim=True))
        return a


# ---------------------------------------------------------------- heuristics
def _toward(env, target):
    """Action that moves the current rates toward `target` in one step."""
    return np.clip((target - env.rates) / (env.action_gain * np.maximum(env.rates, 1e-9)), -1, 1)


def heuristic_action(algo, env, mean_demand):
    n = env.n
    if algo == "no_control":
        return np.zeros(n)
    if algo == "equal_split":
        return _toward(env, np.full(n, env.C / n))
    if algo == "const_max":
        # Retained only to reproduce V1. Under a relative action projected onto
        # the capacity simplex a uniform action is a no-op, so this is
        # identical to no_control; excluded from the V2 design.
        return np.ones(n)
    if algo == "demand_prop":
        return _toward(env, mean_demand / mean_demand.sum() * env.C)
    if algo == "threshold":
        # Act in proportion to how far each slice is past its own SLA.
        ratio = np.array([env.delay_ms[i] / env.sla[p] for i, p in enumerate(PORTS)])
        return np.clip(ratio - 1.0, -1.0, 1.0)
    raise ValueError(algo)


def safety_mask(action, env, margin=0.8, gain=2.0):
    """Nudge a slice's rate up once its delay passes `margin` of its SLA.

    The old version compared a z-scored feature against a millisecond threshold
    and therefore fired on 0.11% of rows. Here both sides are in SLA-relative
    units, so the comparison is meaningful.
    """
    a = np.array(action, dtype=float)
    ratio = np.array([env.delay_ms[i] / env.sla[p] for i, p in enumerate(PORTS)])
    hot = ratio > margin
    a[hot] = np.clip(a[hot] + gain * (ratio[hot] - margin), -1.0, 1.0)
    return np.clip(a, -1.0, 1.0)


# ---------------------------------------------------------------- PPO family
def probe(policy, env, norm, episodes, ep_len):
    """Short evaluation used to trace a validation curve during training."""
    tot, viol = [], []
    for _ in range(episodes):
        s = norm(env.reset())
        for _ in range(ep_len):
            ns, r, _, info = env.step(policy(env, s))
            tot.append(r)
            viol.append(info["violation"].mean())
            s = norm(ns)
    return float(np.mean(tot)), float(np.mean(viol) * 100)


def run_ppo(args, env, norm, device, dueling, use_mask, val_probe=None):
    sd, ad = env.state_dim, env.action_dim
    actor = Actor(sd, ad).to(device)
    critic = Critic(sd, dueling=dueling).to(device)
    opt_a = optim.Adam(actor.parameters(), lr=args.lr)
    opt_c = optim.Adam(critic.parameters(), lr=args.lr)

    log, steps_done = [], 0
    s = norm(env.reset())
    while steps_done < args.steps:
        S, A, LP, R, D, V = [], [], [], [], [], []
        for _ in range(args.rollout):
            st = torch.as_tensor(s, dtype=torch.float32, device=device).unsqueeze(0)
            with torch.no_grad():
                mu, std = actor(st)
                val = critic(st)
                dist = torch.distributions.Normal(mu, std)
                raw = dist.sample()
                lp = dist.log_prob(raw).sum(-1)
            act = raw.squeeze(0).cpu().numpy().clip(-1, 1)
            if use_mask:
                act = safety_mask(act, env)
            ns, r, done, _ = env.step(act)
            S.append(s); A.append(raw.squeeze(0).cpu().numpy()); LP.append(lp.item())
            R.append(r); D.append(float(done)); V.append(val.item())
            s = norm(env.reset() if done else ns)
            steps_done += 1

        with torch.no_grad():
            last_v = critic(torch.as_tensor(s, dtype=torch.float32, device=device).unsqueeze(0)).item()

        adv, gae = np.zeros(len(R)), 0.0
        for t in reversed(range(len(R))):
            nv = last_v if t == len(R) - 1 else V[t + 1]
            delta = R[t] + args.gamma * nv * (1 - D[t]) - V[t]
            gae = delta + args.gamma * args.lam * (1 - D[t]) * gae
            adv[t] = gae
        ret = adv + np.array(V)
        adv = (adv - adv.mean()) / (adv.std() + 1e-8)

        St = torch.as_tensor(np.array(S), dtype=torch.float32, device=device)
        At = torch.as_tensor(np.array(A), dtype=torch.float32, device=device)
        LPt = torch.as_tensor(np.array(LP), dtype=torch.float32, device=device)
        Advt = torch.as_tensor(adv, dtype=torch.float32, device=device)
        Rett = torch.as_tensor(ret, dtype=torch.float32, device=device).unsqueeze(1)

        idx = np.arange(len(R))
        for _ in range(args.ppo_epochs):
            np.random.shuffle(idx)
            for k in range(0, len(idx), args.batch_size):
                b = idx[k:k + args.batch_size]
                mu, std = actor(St[b])
                dist = torch.distributions.Normal(mu, std)
                lp = dist.log_prob(At[b]).sum(-1)
                # Real ratio: LPt was recorded at rollout time, not this update.
                ratio = torch.exp(lp - LPt[b])
                s1 = ratio * Advt[b]
                s2 = torch.clamp(ratio, 1 - args.clip_eps, 1 + args.clip_eps) * Advt[b]
                ent = dist.entropy().sum(-1).mean()
                loss_a = -torch.min(s1, s2).mean() - args.ent_coef * ent
                loss_c = nn.MSELoss()(critic(St[b]), Rett[b])

                opt_a.zero_grad(); loss_a.backward()
                nn.utils.clip_grad_norm_(actor.parameters(), args.grad_clip); opt_a.step()
                opt_c.zero_grad(); loss_c.backward()
                nn.utils.clip_grad_norm_(critic.parameters(), args.grad_clip); opt_c.step()

        with torch.no_grad():
            clipped = ((ratio - 1).abs() > args.clip_eps).float().mean().item()
        rec = {"step": steps_done, "loss_actor": loss_a.item(), "loss_critic": loss_c.item(),
               "entropy": ent.item(), "mean_reward": float(np.mean(R)),
               "clip_fraction": clipped}
        if val_probe is not None:
            def _pol(e, st):
                with torch.no_grad():
                    mu, _ = actor(torch.as_tensor(st, dtype=torch.float32, device=device).unsqueeze(0))
                a = mu.squeeze(0).cpu().numpy()
                return safety_mask(a, e) if use_mask else a
            rec["val_reward"], rec["val_viol"] = val_probe(_pol)
        log.append(rec)

    def policy(e, st):
        with torch.no_grad():
            mu, _ = actor(torch.as_tensor(st, dtype=torch.float32, device=device).unsqueeze(0))
        a = mu.squeeze(0).cpu().numpy()
        return safety_mask(a, e) if use_mask else a

    return policy, pd.DataFrame(log)


# ---------------------------------------------------------------- DQN family
def run_dqn(args, env, norm, device, double, dueling, use_mask=False, val_probe=None):
    sd, nb = env.state_dim, env.action_dim
    bins = np.linspace(-1.0, 1.0, args.bins)
    q = BranchingQ(sd, nb, args.bins, dueling=dueling).to(device)
    tgt = BranchingQ(sd, nb, args.bins, dueling=dueling).to(device)
    tgt.load_state_dict(q.state_dict())
    opt = optim.Adam(q.parameters(), lr=args.lr)
    buf = deque(maxlen=args.buffer)

    log = []
    s = norm(env.reset())
    for step in range(args.steps):
        eps = max(args.eps_end, args.eps_start - step / max(args.eps_decay, 1))
        if np.random.rand() < eps:
            ai = np.random.randint(0, args.bins, nb)
        else:
            with torch.no_grad():
                ai = q(torch.as_tensor(s, dtype=torch.float32, device=device).unsqueeze(0)
                       ).squeeze(0).argmax(dim=-1).cpu().numpy()
        # The discrete choice is decoded to a continuous vector first, so the
        # identical safety_mask used by the PPO arms applies unchanged.
        act = bins[ai]
        if use_mask:
            act = safety_mask(act, env)
        ns, r, done, _ = env.step(act)
        ns_n = norm(ns)
        buf.append((s, ai, r, ns_n, float(done)))
        s = norm(env.reset()) if done else ns_n

        if len(buf) >= args.batch_size and step % args.train_every == 0:
            batch = [buf[i] for i in np.random.randint(0, len(buf), args.batch_size)]
            bs = torch.as_tensor(np.array([b[0] for b in batch]), dtype=torch.float32, device=device)
            ba = torch.as_tensor(np.array([b[1] for b in batch]), dtype=torch.int64, device=device)
            br = torch.as_tensor(np.array([b[2] for b in batch]), dtype=torch.float32, device=device)
            bn = torch.as_tensor(np.array([b[3] for b in batch]), dtype=torch.float32, device=device)
            bd = torch.as_tensor(np.array([b[4] for b in batch]), dtype=torch.float32, device=device)

            qv = q(bs).gather(2, ba.unsqueeze(2)).squeeze(2)          # (B, branches)
            with torch.no_grad():
                if double:
                    na = q(bn).argmax(dim=2, keepdim=True)
                    nq = tgt(bn).gather(2, na).squeeze(2)
                else:
                    nq = tgt(bn).max(dim=2)[0]
                # Reward is shared across branches, so every branch bootstraps
                # toward the same return.
                target = br.unsqueeze(1) + args.gamma * nq * (1 - bd).unsqueeze(1)
            loss = nn.MSELoss()(qv, target)
            opt.zero_grad(); loss.backward()
            nn.utils.clip_grad_norm_(q.parameters(), args.grad_clip); opt.step()
            if step % args.target_sync == 0:
                tgt.load_state_dict(q.state_dict())
            if step % (args.train_every * 50) == 0:
                rec = {"step": step, "loss": loss.item(), "epsilon": eps,
                       "q_mean": qv.mean().item()}
                if val_probe is not None and step % args.eval_every == 0:
                    def _pol(e, st):
                        with torch.no_grad():
                            ai = q(torch.as_tensor(st, dtype=torch.float32, device=device
                                                   ).unsqueeze(0)).squeeze(0).argmax(-1).cpu().numpy()
                        a = bins[ai]
                        return safety_mask(a, e) if use_mask else a
                    rec["val_reward"], rec["val_viol"] = val_probe(_pol)
                log.append(rec)

    def policy(e, st):
        with torch.no_grad():
            ai = q(torch.as_tensor(st, dtype=torch.float32, device=device).unsqueeze(0)
                   ).squeeze(0).argmax(dim=-1).cpu().numpy()
        a = bins[ai]
        return safety_mask(a, e) if use_mask else a

    return policy, pd.DataFrame(log)


# ---------------------------------------------------------------- evaluation
def evaluate(policy, env, norm, episodes, ep_len, seed):
    env.rng = np.random.default_rng(seed + 10_000)   # eval starts differ from training
    rows = []
    for ep in range(episodes):
        s = norm(env.reset())
        for t in range(ep_len):
            a = policy(env, s)
            ns, r, _, info = env.step(a)
            rows.append({
                "episode": ep, "step": t, "reward": r,
                **{f"delay_{p}": info["delay_ms"][i] for i, p in enumerate(PORTS)},
                **{f"rate_{p}": info["rates_mbps"][i] for i, p in enumerate(PORTS)},
                **{f"drop_{p}": info["drop_mb"][i] for i, p in enumerate(PORTS)},
                **{f"viol_{p}": int(info["violation"][i]) for i, p in enumerate(PORTS)},
                **{f"action_{p}": float(np.asarray(a).reshape(-1)[i]) for i, p in enumerate(PORTS)},
            })
            s = norm(ns)
    return pd.DataFrame(rows)


def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                                       stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--algo", required=True, choices=ALGOS)
    p.add_argument("--arm", default="full", choices=ARMS)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--steps", type=int, default=60_000)
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "online")
    p.add_argument("--device", default="cpu", choices=["cpu", "cuda"])

    e = p.add_argument_group("environment")
    e.add_argument("--capacity", type=float, default=12.0,
                   help="link capacity Mbps; default ~= measured aggregate demand (12.28)")
    e.add_argument("--buffer-ms", type=float, default=200.0)
    e.add_argument("--action-gain", type=float, default=0.20)
    e.add_argument("--episode-len", type=int, default=200)
    e.add_argument("--eval-episodes", type=int, default=20)
    e.add_argument("--phase", default=None, choices=PHASES,
                   help="V2: which split to train and evaluate on. Omit for V1 behaviour "
                        "(whole trace, no split).")
    e.add_argument("--split", default="0.6,0.2,0.2", help="train,val,test fractions")
    e.add_argument("--eval-phase", default=None, choices=PHASES,
                   help="split to evaluate on; defaults to --phase. The pilot trains on train "
                        "and evaluates on val.")
    e.add_argument("--allow-test", action="store_true",
                   help="required guard for --phase test; the test split is touched once, "
                        "in the final V2 run only")
    e.add_argument("--safety", default=None, choices=["on", "off"],
                   help="V2: safety layer as an orthogonal factor, applied to every method "
                        "including discrete and heuristic ones. Omit for V1 behaviour "
                        "(layer only on sdhppo).")
    e.add_argument("--eval-every", type=int, default=0,
                   help="probe the eval split every N steps to trace a validation curve; "
                        "0 disables. Used by the pilot to pick the step budget.")
    e.add_argument("--probe-episodes", type=int, default=5)
    e.add_argument("--reward-scale", type=float, default=1.0,
                   help="divides the raw reward; one shared constant, see protocol v2")
    e.add_argument("--random-init-alloc", action="store_true",
                   help="V2: randomise the initial allocation so no_control, equal_split and "
                        "const_max stop collapsing onto the same policy")
    e.add_argument("--demand-source", default="full", choices=["full", "train"],
                   help="which slice of the trace demand_prop averages over. 'full' is what "
                        "the frozen sweep used and includes the evaluated rows; 'train' uses "
                        "only the first --train-frac of the trace.")
    e.add_argument("--train-frac", type=float, default=0.8)

    h = p.add_argument_group("hyperparameters (identical across methods)")
    h.add_argument("--lr", type=float, default=3e-4)
    h.add_argument("--gamma", type=float, default=0.99)
    h.add_argument("--lam", type=float, default=0.95)
    h.add_argument("--clip-eps", type=float, default=0.2)
    h.add_argument("--ent-coef", type=float, default=0.01)
    h.add_argument("--grad-clip", type=float, default=0.5)
    h.add_argument("--batch-size", type=int, default=64)
    h.add_argument("--rollout", type=int, default=2048)
    h.add_argument("--ppo-epochs", type=int, default=10)
    h.add_argument("--bins", type=int, default=21)
    h.add_argument("--buffer", type=int, default=50_000)
    h.add_argument("--train-every", type=int, default=1)
    h.add_argument("--target-sync", type=int, default=500)
    h.add_argument("--eps-start", type=float, default=1.0)
    h.add_argument("--eps-end", type=float, default=0.05)
    h.add_argument("--eps-decay", type=int, default=30_000)
    args = p.parse_args()

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    device = torch.device(args.device)

    full_trace = load_arrival_trace()

    eval_phase = args.eval_phase or args.phase
    if args.phase is None:                       # V1 behaviour: no split at all
        arrivals = eval_arrivals = full_trace
        train_slice = full_trace
    else:
        if "test" in (args.phase, eval_phase) and not args.allow_test:
            raise SystemExit("touching the test split requires --allow-test. It is reserved "
                             "for the single final V2 run.")
        f_tr, f_va, _ = (float(x) for x in args.split.split(","))
        n = len(full_trace)
        a, b = int(n * f_tr), int(n * (f_tr + f_va))
        cuts = {"train": (0, a), "val": (a, b), "test": (b, n)}
        lo, hi = cuts[args.phase]
        arrivals = full_trace[lo:hi]
        lo, hi = cuts[eval_phase]
        eval_arrivals = full_trace[lo:hi]
        train_slice = full_trace[:a]             # statistics always come from train

    # demand_prop's mean and every normalisation constant are estimated on train
    # only, never on the split being evaluated.
    if args.phase is not None or args.demand_source == "train":
        mean_demand = train_slice.mean(axis=0)
    else:
        mean_demand = full_trace.mean(axis=0)
    env = SliceEnv(arrivals, link_capacity_mbps=args.capacity, buffer_ms=args.buffer_ms,
                   action_gain=args.action_gain, episode_len=args.episode_len, seed=args.seed,
                   random_init_alloc=args.random_init_alloc, reward_scale=args.reward_scale)
    norm = Normalizer(env)

    # V1: only sdhppo carried the safety layer, which the diagnostics showed was
    # the single largest contributor. V2 makes it an explicit factor applied to
    # every method, so the comparison is like for like.
    if args.safety is None:
        want_mask = args.algo == "sdhppo" and args.arm != "no_mask"
    else:
        want_mask = args.safety == "on"

    eval_env = SliceEnv(eval_arrivals, link_capacity_mbps=args.capacity,
                        buffer_ms=args.buffer_ms, action_gain=args.action_gain,
                        episode_len=args.episode_len, seed=args.seed,
                        random_init_alloc=args.random_init_alloc,
                        reward_scale=args.reward_scale)
    val_probe = None
    if args.eval_every > 0:
        def val_probe(pol):
            return probe(pol, eval_env, norm, args.probe_episodes, args.episode_len)

    started = datetime.now(timezone.utc)
    t0 = time.perf_counter()

    if args.algo in HEURISTICS:
        train_log = pd.DataFrame()

        def policy(e, st):
            a = heuristic_action(args.algo, e, mean_demand)
            return safety_mask(a, e) if want_mask else a
    elif args.algo in ("ppo", "sdhppo"):
        dueling = args.algo == "sdhppo" and args.arm != "no_dueling"
        policy, train_log = run_ppo(args, env, norm, device, dueling, want_mask, val_probe)
    else:
        policy, train_log = run_dqn(args, env, norm, device,
                                    double=args.algo == "ddqn",
                                    dueling=args.algo == "ddqn" and args.arm != "no_dueling",
                                    use_mask=want_mask, val_probe=val_probe)
    train_secs = time.perf_counter() - t0

    t1 = time.perf_counter()
    ev = evaluate(policy, eval_env, norm, args.eval_episodes, args.episode_len, args.seed)
    eval_secs = time.perf_counter() - t1

    args.out.mkdir(parents=True, exist_ok=True)
    if args.phase is None and args.safety is None:
        stem = f"{args.algo}_{args.arm}_seed{args.seed}"          # V1 naming, unchanged
    else:
        stem = (f"{args.algo}_{args.arm}_{args.phase or 'nosplit'}"
                f"_safety{'on' if want_mask else 'off'}_seed{args.seed}")
    ev.to_csv(args.out / f"{stem}_eval.csv", index=False)
    if not train_log.empty:
        train_log.to_csv(args.out / f"{stem}_train.csv", index=False)

    meta = {
        "algo": args.algo, "algo_label": LABEL[args.algo], "arm": args.arm, "seed": args.seed,
        "args": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
        "environment": "slice_env.SliceEnv (queueing simulation)",
        "grounding": "arrival process replayed from measured rx_mbps (OVS byte counters); "
                     "action->delay relationship is queueing theory, NOT measured",
        "mean_demand_mbps": mean_demand.tolist(),
        "phase": args.phase, "safety_applied": bool(want_mask),
        "reward_scale": args.reward_scale,
        "trace_rows_used": int(len(arrivals)),
        "stats_estimated_on": "train" if args.phase is not None else args.demand_source,
        "started_utc": started.isoformat(),
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "train_seconds": round(train_secs, 2), "eval_seconds": round(eval_secs, 2),
        "git_commit": git_commit(),
        "env_versions": {"python": sys.version.split()[0], "torch": torch.__version__,
                         "numpy": np.__version__, "platform": platform.platform()},
    }
    (args.out / f"{stem}.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    viol = ev[[f"viol_{p}" for p in PORTS]].mean() * 100
    print(f"{stem}: train {train_secs:.0f}s eval {eval_secs:.1f}s | reward {ev['reward'].mean():.3f} | "
          f"viol% " + " ".join(f"{p}={viol[f'viol_{p}']:.1f}" for p in PORTS))


if __name__ == "__main__":
    main()
