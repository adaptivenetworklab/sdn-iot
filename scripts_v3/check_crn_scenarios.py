"""Common-random-numbers check for the V3 design, extended to the scenarios.

Same pattern as scripts/check_crn.py (RecEnv logging every reset, lines 30-35;
env_for, lines 55-57; shared evaluation episodes, lines 83-92), which is
imported, not modified. For every seed in 20-39 and each matched arm
(var_matched, moment_matched):

- training: dqn and ddqn see the same sequence of episode resets;
- evaluation: dqn, ddqn and demand_prop see the same resets on the plain val
  trace and on its diurnal and flash transforms (slice_env.SCENARIOS), and each
  scenario uses the same resets as the plain evaluation.

Only val is read. Training uses the short check budget of check_crn.STEPS.

    python scripts_v3/check_crn_scenarios.py
"""
import sys
from argparse import Namespace
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts_v3"))
import run_v3  # noqa: E402
from check_crn import STEPS, RecEnv, args_for  # noqa: E402
from slice_env import SCENARIOS, load_arrival_trace  # noqa: E402
from train_online import Normalizer, evaluate, heuristic_action, run_dqn  # noqa: E402

SEEDS = range(20, 40)
EVAL_EPISODES, EPISODE_LEN = 20, 50


def main():
    trace = load_arrival_trace()
    for arm in run_v3.MATCHED_ARMS:
        check_arm(trace, arm)


def check_arm(trace, arm):
    split = Namespace(phase="train", eval_phase="val", allow_test=False, split="0.6,0.2,0.2",
                      arm=arm)
    train, val_arr, _, train_slice = run_v3.split_arrivals(trace, split)
    assert len(train) == len(train_slice) and not np.array_equal(train, train_slice), \
        f"{arm} did not replace the training rows"
    mean_demand = train_slice.mean(axis=0)
    n_train = n_eval = 0
    for seed in SEEDS:
        def env_for(arr):
            return RecEnv(arr, link_capacity_mbps=12.0, episode_len=EPISODE_LEN, seed=seed,
                          random_init_alloc=True, reward_scale=19.0106)

        runs = {
            "dqn": lambda e, n: run_dqn(args_for(), e, n, "cpu", double=False, dueling=False),
            "ddqn": lambda e, n: run_dqn(args_for(), e, n, "cpu", double=True, dueling=True),
        }
        train_logs, policies = {}, {}
        for name, fn in runs.items():
            np.random.seed(seed)
            torch.manual_seed(seed)
            env = env_for(train)
            policies[name], _ = fn(env, Normalizer(env))
            train_logs[name] = env.log
        assert train_logs["dqn"] == train_logs["ddqn"], f"seed {seed}: training resets differ"
        assert len(train_logs["dqn"]) >= STEPS // EPISODE_LEN
        n_train += len(train_logs["dqn"])

        policies["demand_prop"] = lambda e, s: heuristic_action("demand_prop", e, mean_demand)
        plain = None
        for scen in ("plain", *SCENARIOS):
            arr = val_arr if scen == "plain" else SCENARIOS[scen](val_arr)
            logs = {}
            for name, pol in policies.items():
                e = env_for(arr)
                e.log = []
                evaluate(pol, e, Normalizer(e), EVAL_EPISODES, EPISODE_LEN, seed)
                logs[name] = e.log
            first = logs["dqn"]
            assert all(v == first for v in logs.values()), f"seed {seed}: {scen} resets differ"
            assert len(first) == EVAL_EPISODES
            if plain is None:
                plain = first
            else:
                assert first == plain, f"seed {seed}: {scen} resets differ from plain evaluation"
            n_eval += len(first) * len(logs)
        print(f"{arm} seed {seed}: ok", flush=True)

    print(f"check_crn_scenarios: K2 holds for seeds {SEEDS.start}-{SEEDS.stop - 1}, arm "
          f"{arm}; training resets identical for dqn/ddqn ({n_train} resets); "
          f"evaluation resets identical for dqn/ddqn/demand_prop on plain, "
          f"{', '.join(SCENARIOS)} and equal across scenarios ({n_eval} episode resets)")


if __name__ == "__main__":
    main()
