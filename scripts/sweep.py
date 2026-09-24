"""CLI wrapper around the training/eval logic of Reinforcement Learning/revision/allModel4.ipynb.

Faithful port: the training loop, losses, optimizers, schedulers and evaluation
formula are transcribed unchanged. The only structural changes are (a) argparse
plumbing, (b) raw per-epoch / per-sample output instead of aggregated tables,
and (c) constants that were hardcoded in the notebook are exposed as flags whose
DEFAULTS REPRODUCE THE NOTEBOOK EXACTLY.

Known defects are preserved on purpose so the sweep measures the real baseline.
They are documented in docs/experiments/00-contamination-audit.md and listed by
--audit. Do not "fix" them here without recording the decision in
docs/experiments/protocol.md first.
"""

import argparse
import ast
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.optim.lr_scheduler import LinearLR

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = REPO_ROOT / "Reinforcement Learning" / "revision" / "drl_preprocessed_final.csv"

ALGOS = ["dqn", "ddqn", "ppo", "sdhppo", "static"]
ARMS = ["full", "no_mask", "no_dueling", "no_aug"]

ALGO_LABEL = {
    "dqn": "DQN",
    "ddqn": "DDQN",
    "ppo": "PPO Standard",
    "sdhppo": "Proposed (SDH-PPO)",
    "static": "Static",
}

AUDIT_NOTES = """Preserved defects (see docs/experiments/00-contamination-audit.md):
  1. Evaluation delay is a closed-form surrogate d = raw * (1 - k*a), monotone in
     the action and free of cost. Optimal policy is trivially a = +1.
  2. k differs by algorithm NAME: 0.15 for SDH-PPO on P4 vs 0.10 for every
     baseline. Exposed here as --k-p4-proposed / --k-p4-other. Pass --fair-eval
     to equalise them.
  3. DQN/DDQN act through 3 bins {0.0, +0.1, -0.1}; the continuous arms emit
     tanh in [-1, 1]. A 10x action-authority gap. See --dqn-bins.
  4. The safety mask compares a z-scored state feature against a millisecond
     threshold, so it fires on ~0.11% of rows. Preserved as-is.
  5. The PPO ratio uses old_log_probs = current.detach(), so ratio == 1 and the
     clip never activates; this is vanilla policy gradient, not PPO.
  6. Reward is a function of the logged next row only and does not contain the
     action, so the advantage carries no action information.
  7. Logged 'reward' per epoch is the dataset batch mean, identical in
     expectation across algorithms and independent of the policy.
"""


# --------------------------------------------------------------------------
# Networks - transcribed verbatim from allModel4.ipynb cell 2
# --------------------------------------------------------------------------
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_size, 64), nn.ReLU(),
            nn.Linear(64, 64), nn.ReLU(),
            nn.Linear(64, action_size),
        )

    def forward(self, x):
        return self.fc(x)


class DuelingDQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.feature_layer = nn.Sequential(nn.Linear(state_dim, 128), nn.ReLU())
        self.value_stream = nn.Sequential(nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, 1))
        self.advantage_stream = nn.Sequential(nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, action_dim))

    def forward(self, state):
        features = self.feature_layer(state)
        value = self.value_stream(features)
        advantage = self.advantage_stream(features)
        return value + (advantage - advantage.mean(dim=1, keepdim=True))


class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.actor = nn.Sequential(nn.Linear(state_dim, 64), nn.Tanh(), nn.Linear(64, action_dim))
        self.sigma = nn.Parameter(torch.ones(1) * 0.5)
        self.critic = nn.Sequential(nn.Linear(state_dim, 64), nn.Tanh(), nn.Linear(64, 1))

    def forward(self, state):
        mu = torch.tanh(self.actor(state))
        sigma = torch.exp(self.sigma)
        value = self.critic(state)
        return mu, sigma, value


class PPOActor(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
        )
        self.mu = nn.Linear(128, 1)
        self.sigma = nn.Parameter(torch.ones(1) * 0.5)

    def forward(self, x):
        x = self.fc(x)
        return torch.tanh(self.mu(x)), torch.exp(self.sigma)


class DuelingCritic(nn.Module):
    """Notebook's 'dueling' critic. With action_dim == 1 the decomposition is
    vacuous and a.mean() lacks dim=, so it reduces to a two-head MLP. Preserved
    verbatim; the no_dueling arm swaps in PlainCritic below."""

    def __init__(self, input_dim):
        super().__init__()
        self.base = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.value_head = nn.Linear(256, 1)
        self.adv_head = nn.Linear(256, 1)

    def forward(self, x):
        x = self.base(x)
        v = self.value_head(x)
        a = self.adv_head(x)
        return v + (a - a.mean())


class PlainCritic(nn.Module):
    """Ablation counterpart: same width and depth, single value head."""

    def __init__(self, input_dim):
        super().__init__()
        self.base = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.value_head = nn.Linear(256, 1)

    def forward(self, x):
        return self.value_head(self.base(x))


def compute_ppo_loss(old_probs, current_probs, advantages, epsilon=0.2):
    ratio = torch.exp(current_probs - old_probs)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    return -torch.min(surr1, surr2).mean()


def get_action_with_mask(state, raw_action, thresholds, safety_margin=0.5, gain=2.0):
    """Verbatim from allModel4.ipynb cell 3, including the z-score vs millisecond
    unit mismatch that makes it a no-op on ~99.89% of rows."""
    delay_p4 = state[10]
    limit_p4 = thresholds["P4"]

    if delay_p4 > (limit_p4 * safety_margin):
        error = (delay_p4 - (limit_p4 * safety_margin)) / limit_p4
        return float(np.clip(raw_action + (gain * error), -1.0, 1.0))

    if delay_p4 < (limit_p4 * 0.5):
        if state[2] > thresholds["P1"] or state[6] > thresholds["P2"]:
            return float(np.clip(raw_action + 0.2, -1.0, 1.0))

    return raw_action


# --------------------------------------------------------------------------
def load_dataset(path):
    df = pd.read_csv(path)
    df["state"] = df["state"].apply(lambda x: np.array(ast.literal_eval(x)))
    df["next_state"] = df["next_state"].apply(lambda x: np.array(ast.literal_eval(x)))
    for col in ("raw_delay_p1", "raw_delay_p2", "raw_delay_p4"):
        if col not in df.columns:
            raise SystemExit(
                f"{path} lacks column '{col}'. The 'final/' copy uses the older schema; "
                "use the revision/ dataset."
            )
    return df


def build_models(state_dim, arm, device):
    """Construct every network in the notebook's original order so the torch RNG
    stream matches a joint run, then return them all. Training only steps the
    requested algorithm."""
    dqn_model = DQN(state_dim, 3).to(device)
    dqn_target = DQN(state_dim, 3).to(device)
    dqn_target.load_state_dict(dqn_model.state_dict())

    ddqn_model = DuelingDQN(state_dim, 3).to(device)
    ddqn_target = DuelingDQN(state_dim, 3).to(device)
    ddqn_target.load_state_dict(ddqn_model.state_dict())

    ppo_model = ActorCritic(state_dim, 1).to(device)

    sdh_actor = PPOActor(state_dim).to(device)
    critic_cls = PlainCritic if arm == "no_dueling" else DuelingCritic
    sdh_critic = critic_cls(state_dim).to(device)

    return dqn_model, dqn_target, ddqn_model, ddqn_target, ppo_model, sdh_actor, sdh_critic


def train(args, train_df, state_dim, device):
    nets = build_models(state_dim, args.arm, device)
    dqn_model, dqn_target, ddqn_model, ddqn_target, ppo_model, sdh_actor, sdh_critic = nets

    end_factor = args.lr_end / args.lr
    opts, scheds = {}, []

    if args.algo == "dqn":
        opts["dqn"] = optim.Adam(dqn_model.parameters(), lr=args.lr)
    elif args.algo == "ddqn":
        opts["ddqn"] = optim.Adam(ddqn_model.parameters(), lr=args.lr)
    elif args.algo == "ppo":
        opts["ppo"] = optim.Adam(ppo_model.parameters(), lr=args.lr)
    elif args.algo == "sdhppo":
        opts["sdh_actor"] = optim.Adam(sdh_actor.parameters(), lr=args.lr)
        opts["sdh_critic"] = optim.Adam(sdh_critic.parameters(), lr=args.lr)

    for o in opts.values():
        scheds.append(LinearLR(o, start_factor=1.0, end_factor=end_factor, total_iters=args.steps))

    rows = []
    for epoch in range(args.steps):
        batch = train_df.sample(args.batch_size)
        states = torch.tensor(np.stack(batch["state"].values), dtype=torch.float32).to(device)
        next_states = torch.tensor(np.stack(batch["next_state"].values), dtype=torch.float32).to(device)
        rewards = torch.tensor(batch["reward"].values, dtype=torch.float32).unsqueeze(1).to(device)
        actions_discrete = torch.tensor(batch["action_discrete"].values, dtype=torch.long).unsqueeze(1).to(device)
        actions_continuous = torch.tensor(batch["action_continuous"].values, dtype=torch.float32).unsqueeze(1).to(device)
        dones = torch.zeros((args.batch_size, 1), dtype=torch.float32).to(device)

        rec = {"epoch": epoch + 1, "batch_reward_mean": rewards.mean().item()}

        if args.algo == "dqn":
            q_values = dqn_model(states).gather(1, actions_discrete)
            next_q = dqn_target(next_states).max(1)[0].unsqueeze(1).detach()
            target_q = rewards + args.gamma * next_q * (1 - dones)
            loss = nn.MSELoss()(q_values, target_q)
            opts["dqn"].zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(dqn_model.parameters(), max_norm=args.grad_clip)
            opts["dqn"].step()
            if epoch % args.target_sync == 0:
                dqn_target.load_state_dict(dqn_model.state_dict())
            rec["loss"] = loss.item()
            rec["q_mean"] = q_values.mean().item()

        elif args.algo == "ddqn":
            q_values = ddqn_model(states).gather(1, actions_discrete)
            next_actions = ddqn_model(next_states).max(1)[1].unsqueeze(1)
            next_q = ddqn_target(next_states).gather(1, next_actions).detach()
            target_q = rewards + args.gamma * next_q * (1 - dones)
            loss = nn.MSELoss()(q_values, target_q)
            opts["ddqn"].zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(ddqn_model.parameters(), max_norm=args.grad_clip)
            opts["ddqn"].step()
            if epoch % args.target_sync == 0:
                ddqn_target.load_state_dict(ddqn_model.state_dict())
            rec["loss"] = loss.item()
            rec["q_mean"] = q_values.mean().item()

        elif args.algo == "ppo":
            mu, sigma, values = ppo_model(states)
            _, _, next_values = ppo_model(next_states)
            target_values = rewards + args.gamma * next_values.detach() * (1 - dones)
            advantages = target_values - values.detach()
            advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
            loss_critic = nn.MSELoss()(values, target_values)
            dist = torch.distributions.Normal(mu, sigma)
            current_lp = dist.log_prob(actions_continuous)
            old_lp = current_lp.detach()
            actor_loss = compute_ppo_loss(old_lp, current_lp, advantages, epsilon=args.clip_eps)
            entropy = dist.entropy().mean()
            loss_actor = actor_loss - args.ent_coef * entropy
            loss = loss_critic + loss_actor
            opts["ppo"].zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(ppo_model.parameters(), max_norm=args.grad_clip)
            opts["ppo"].step()
            rec.update(loss=loss.item(), loss_critic=loss_critic.item(),
                       loss_actor=loss_actor.item(), entropy=entropy.item(),
                       mu_mean=mu.mean().item(), sigma=sigma.item())

        elif args.algo == "sdhppo":
            values = sdh_critic(states)
            next_values = sdh_critic(next_states).detach()
            target_values = rewards + args.gamma * next_values * (1 - dones)
            advantages = target_values - values.detach()
            advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
            loss_critic = nn.MSELoss()(values, target_values)

            mu, sigma = sdh_actor(states)
            dist = torch.distributions.Normal(mu, sigma)
            current_lp = dist.log_prob(actions_continuous)
            old_lp = current_lp.detach()
            actor_loss = compute_ppo_loss(old_lp, current_lp, advantages, epsilon=args.clip_eps)
            entropy = dist.entropy().mean()
            loss_actor = actor_loss - args.ent_coef * entropy

            opts["sdh_critic"].zero_grad()
            loss_critic.backward()
            torch.nn.utils.clip_grad_norm_(sdh_critic.parameters(), max_norm=args.grad_clip)
            opts["sdh_critic"].step()

            opts["sdh_actor"].zero_grad()
            loss_actor.backward()
            torch.nn.utils.clip_grad_norm_(sdh_actor.parameters(), max_norm=args.grad_clip)
            opts["sdh_actor"].step()

            rec.update(loss=(loss_critic + loss_actor).item(), loss_critic=loss_critic.item(),
                       loss_actor=loss_actor.item(), entropy=entropy.item(),
                       mu_mean=mu.mean().item(), sigma=sigma.item())

        for s in scheds:
            s.step()
        rows.append(rec)

    return nets, pd.DataFrame(rows)


def evaluate(args, nets, test_df, sla, device):
    dqn_model, _, ddqn_model, _, ppo_model, sdh_actor, sdh_critic = nets
    for m in (dqn_model, ddqn_model, ppo_model, sdh_actor, sdh_critic):
        m.eval()

    bins = [float(x) for x in args.dqn_bins.split(",")]
    k_p4 = args.k_p4_proposed if args.algo == "sdhppo" else args.k_p4_other
    if args.fair_eval:
        k_p4 = args.k_p4_other
    use_mask = args.algo == "sdhppo" and args.arm != "no_mask"

    rows = []
    for idx, row in test_df.iterrows():
        st = row["state"]
        action_raw = None

        if args.algo == "static":
            action = float(row["action_continuous"])
        else:
            with torch.no_grad():
                st_t = torch.tensor(st, dtype=torch.float32).unsqueeze(0).to(device)
                if args.algo == "sdhppo":
                    action_raw = sdh_actor(st_t)[0].item()
                    action = get_action_with_mask(st, action_raw, sla,
                                                  args.safety_margin, args.mask_gain) if use_mask else action_raw
                elif args.algo == "ppo":
                    action = ppo_model(st_t)[0].item()
                else:
                    model = dqn_model if args.algo == "dqn" else ddqn_model
                    action_idx = model(st_t).argmax().item()
                    action = bins[action_idx] if action_idx < len(bins) else 0.0

        raw_p1, raw_p2, raw_p4 = row["raw_delay_p1"], row["raw_delay_p2"], row["raw_delay_p4"]
        rows.append({
            "sample_idx": idx,
            "action": action,
            "action_raw": action_raw if action_raw is not None else action,
            "raw_p1": raw_p1, "raw_p2": raw_p2, "raw_p4": raw_p4,
            "d1": raw_p1 * (1 - args.k_p1 * action),
            "d2": raw_p2 * (1 - args.k_p2 * action),
            "d4": raw_p4 * (1 - k_p4 * action),
        })

    return pd.DataFrame(rows), k_p4


def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                                       stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--algo", required=True, choices=ALGOS)
    p.add_argument("--arm", default="full", choices=ARMS)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--steps", type=int, default=2000, help="gradient updates (notebook: 2000 epochs)")
    p.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "raw")
    p.add_argument("--data", type=Path, default=DEFAULT_DATA)
    p.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"])

    g = p.add_argument_group("hyperparameters (notebook defaults)")
    g.add_argument("--lr", type=float, default=3e-4)
    g.add_argument("--lr-end", type=float, default=1e-5)
    g.add_argument("--batch-size", type=int, default=64)
    g.add_argument("--gamma", type=float, default=0.99)
    g.add_argument("--clip-eps", type=float, default=0.2)
    g.add_argument("--ent-coef", type=float, default=0.05)
    g.add_argument("--grad-clip", type=float, default=0.5)
    g.add_argument("--target-sync", type=int, default=10)
    g.add_argument("--test-size", type=float, default=0.2)

    e = p.add_argument_group("evaluation surrogate (see --audit)")
    e.add_argument("--k-p1", type=float, default=0.1)
    e.add_argument("--k-p2", type=float, default=0.1)
    e.add_argument("--k-p4-proposed", type=float, default=0.15)
    e.add_argument("--k-p4-other", type=float, default=0.10)
    e.add_argument("--fair-eval", action="store_true",
                   help="force k_p4_proposed = k_p4_other, removing the name-keyed bias")
    e.add_argument("--dqn-bins", default="0.0,0.1,-0.1")
    e.add_argument("--sla-p1", type=float, default=6.0)
    e.add_argument("--sla-p2", type=float, default=70.0)
    e.add_argument("--sla-p4", type=float, default=7.0)
    e.add_argument("--safety-margin", type=float, default=0.5)
    e.add_argument("--mask-gain", type=float, default=2.0)

    p.add_argument("--audit", action="store_true", help="print preserved-defect list and exit")
    args = p.parse_args()

    if args.audit:
        print(AUDIT_NOTES)
        return

    if args.arm == "no_aug":
        raise SystemExit(
            "arm 'no_aug' needs a real-data-only preprocessed dataset, which does not exist yet.\n"
            "drl_preprocessed_final.csv is built from the WGAN-GP-augmented 15k set. Producing a\n"
            "real-only counterpart requires rerunning Preprocessing on dataset_dqn_rich.csv\n"
            "(1022 measured rows, semicolon-delimited). See docs/experiments/01-training-loop.md."
        )

    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("--device cuda requested but torch.cuda.is_available() is False")

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if device.type == "cuda":
        torch.cuda.manual_seed_all(args.seed)

    df = load_dataset(args.data)
    state_dim = len(df["state"].iloc[0])
    train_df, test_df = train_test_split(df, test_size=args.test_size, random_state=args.seed)
    sla = {"P1": args.sla_p1, "P2": args.sla_p2, "P4": args.sla_p4}

    started = datetime.now(timezone.utc)
    t0 = time.perf_counter()

    if args.algo == "static":
        nets = build_models(state_dim, args.arm, device)
        train_log = pd.DataFrame()
    else:
        nets, train_log = train(args, train_df, state_dim, device)
    train_secs = time.perf_counter() - t0

    t1 = time.perf_counter()
    eval_df, k_p4_used = evaluate(args, nets, test_df, sla, device)
    eval_secs = time.perf_counter() - t1
    finished = datetime.now(timezone.utc)

    args.out.mkdir(parents=True, exist_ok=True)
    stem = f"{args.algo}_{args.arm}_seed{args.seed}"
    eval_path = args.out / f"{stem}_eval.csv"
    eval_df.to_csv(eval_path, index=False)
    train_path = None
    if not train_log.empty:
        train_path = args.out / f"{stem}_train.csv"
        train_log.to_csv(train_path, index=False)

    meta = {
        "algo": args.algo,
        "algo_label": ALGO_LABEL[args.algo],
        "arm": args.arm,
        "seed": args.seed,
        "args": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
        "k_p4_used": k_p4_used,
        "state_dim": state_dim,
        "n_train": len(train_df),
        "n_test": len(test_df),
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "train_seconds": round(train_secs, 3),
        "eval_seconds": round(eval_secs, 3),
        "git_commit": git_commit(),
        "outputs": {
            "eval_csv": eval_path.name,
            "train_csv": train_path.name if train_path else None,
        },
        "env": {
            "python": sys.version.split()[0],
            "torch": torch.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "device": str(device),
            "cuda_available": torch.cuda.is_available(),
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
            "platform": platform.platform(),
            "processor": platform.processor(),
        },
        "preserved_defects": AUDIT_NOTES.strip().splitlines(),
    }
    (args.out / f"{stem}.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"{stem}: train {train_secs:.1f}s, eval {eval_secs:.1f}s, device={device}, "
          f"k_p4={k_p4_used}, mean|action|={eval_df['action'].abs().mean():.4f} -> {args.out}")


if __name__ == "__main__":
    main()
