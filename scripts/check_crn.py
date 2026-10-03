"""Self-check for protocol v2 K2 (common random numbers) and A7 (selection on val).

K2: for seed i, every method must train on the same episode sequence and be
probed and evaluated on the same episode set, so the analysis can be paired.
The env RNG is only consumed in reset(), so recording (start, initial rates) at
each reset is a complete record of the environment realisation.

A7: the checkpoint-selection probe must read val whatever split the final
evaluation reads. Checked through split_arrivals() with eval_phase=train, so
the property is shown without slicing, let alone evaluating, the test split.

    python scripts/check_crn.py
"""

import sys
from argparse import Namespace
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slice_env import SliceEnv, load_arrival_trace  # noqa: E402
from train_online import (Normalizer, evaluate, heuristic_action, probe,  # noqa: E402
                          run_dqn, run_ppo, split_arrivals)

STEPS = 600          # 12 episodes of 50; enough resets to see any drift


class RecEnv(SliceEnv):
    def reset(self, start=None):
        obs = super().reset(start)
        self.log = getattr(self, "log", []) + [(self.start, *np.round(self.rates, 9))]
        return obs


def args_for(**kw):
    base = dict(steps=STEPS, rollout=100, batch_size=32, ppo_epochs=1, lr=3e-4, gamma=0.99,
                lam=0.95, clip_eps=0.2, ent_coef=0.01, action_param="clip", grad_clip=0.5,
                eval_every=0, residual="off", residual_bound=0.25, actor_init="random",
                bc_steps=500, bc_epochs=1, bc_lr=1e-3, bins=11, buffer=1000, train_every=1,
                target_sync=500, eps_start=1.0, eps_end=0.05, eps_decay=300)
    base.update(kw)
    return Namespace(**base)


def main():
    trace = load_arrival_trace()
    split = Namespace(phase="train", eval_phase="val", allow_test=False, split="0.6,0.2,0.2",
                      arm="real_only")
    train, val_arr, _, train_slice = split_arrivals(trace, split)
    mean_demand = train_slice.mean(axis=0)
    seed = 3

    def env_for(arr):
        return RecEnv(arr, link_capacity_mbps=12.0, episode_len=50, seed=seed,
                      random_init_alloc=True, reward_scale=19.0106)

    runs = {
        "ppo": lambda e, n: run_ppo(args_for(), e, n, "cpu", False, False, mean_demand=mean_demand),
        "sdhppo": lambda e, n: run_ppo(args_for(), e, n, "cpu", True, False, mean_demand=mean_demand),
        "res": lambda e, n: run_ppo(args_for(residual="on"), e, n, "cpu", True, False,
                                    mean_demand=mean_demand),
        "bc": lambda e, n: run_ppo(args_for(actor_init="bc"), e, n, "cpu", True, False,
                                   mean_demand=mean_demand),
        "dqn": lambda e, n: run_dqn(args_for(), e, n, "cpu", double=False, dueling=False),
        "ddqn": lambda e, n: run_dqn(args_for(), e, n, "cpu", double=True, dueling=True),
    }
    train_logs, policies = {}, {}
    for name, fn in runs.items():
        np.random.seed(seed); torch.manual_seed(seed)
        env = env_for(train)
        policies[name], _ = fn(env, Normalizer(env))
        train_logs[name] = env.log

    ref = train_logs["ppo"]
    assert len(ref) >= STEPS // 50, len(ref)
    for name, log in train_logs.items():
        assert log == ref, f"K2: {name} trained on a different episode sequence than ppo"

    # Probe and eval: same episode set for every policy, including a heuristic.
    policies["demand_prop"] = lambda e, s: heuristic_action("demand_prop", e, mean_demand)
    for fn_name, fn in (("evaluate", evaluate), ("probe", probe)):
        logs = {}
        for name, pol in policies.items():
            e = env_for(val_arr)
            e.log = []
            fn(pol, e, Normalizer(e), 5, 50, seed)
            logs[name] = e.log
        first = next(iter(logs.values()))
        assert all(v == first for v in logs.values()), f"K2: {fn_name} episodes differ"

    # A7: probe reads val whatever the evaluation split is.
    for ev_phase in ("val", "train"):
        _, ev_arr, pr_arr, _ = split_arrivals(trace, Namespace(**{**vars(split),
                                                                   "eval_phase": ev_phase}))
        assert np.array_equal(pr_arr, val_arr), f"A7: probe left val with eval_phase={ev_phase}"
    assert not np.array_equal(ev_arr, val_arr)
    try:
        split_arrivals(trace, Namespace(**{**vars(split), "eval_phase": "test"}))
        raise AssertionError("test guard did not fire")
    except SystemExit:
        pass

    # full now carries the synthetic trace; real_only does not.
    full, *_ = split_arrivals(trace, Namespace(**{**vars(split), "arm": "full"}))
    assert len(full) == 2 * len(train) and np.array_equal(full[:len(train)], train)

    print(f"check_crn: K2 holds for {', '.join(runs)} ({len(ref)} resets), "
          f"probe/eval sets shared incl. demand_prop; A7 probe reads val; "
          f"full = {len(full)} rows vs real_only {len(train)}")


if __name__ == "__main__":
    main()
