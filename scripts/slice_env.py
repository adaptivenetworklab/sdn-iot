"""Queueing simulator for multi-slice policing-rate control.

Replaces the closed-form evaluator `d = raw * (1 - k*a)` used by
allModel4.ipynb, which was monotone in the action, free of cost, and carried a
name-keyed coefficient. See docs/experiments/00-contamination-audit.md.

WHAT IS GROUNDED IN MEASUREMENT AND WHAT IS NOT
-----------------------------------------------
Grounded: the arrival process. Per-slice offered load is replayed from
`rx_mbps_p{1,2,4}` in the measured trace, which comes from OVS byte counters
(`ovs-ofctl dump-ports`) and therefore does not depend on clock synchronisation.

NOT grounded: the effect of the policing rate on delay. The testbed never varied
the policing rate (it sat at 1000000 kbps for the entire campaign) and the
hardware no longer exists, so this relationship cannot be measured -- by anyone,
ever. Here it is derived from queueing theory. Any paper using this simulator
must describe the control results as simulation, not as testbed measurement.

Measured delay is deliberately NOT used as ground truth: 13.19% of the raw
one-way delay samples are negative, i.e. dominated by clock offset between the
sender and the collector rather than by queueing.

MODEL
-----
Per slice p, a finite-buffer fluid queue stepped at dt (default 1 s, matching
the collector interval):

    served_p    = min(backlog_p + arrival_p, mu_p * dt)
    backlog_p'  = backlog_p + arrival_p - served_p
    drop_p      = max(0, backlog_p' - buffer_p)
    backlog_p' := min(backlog_p', buffer_p)
    delay_p     = backlog_p' / mu_p          (Little's law, seconds -> ms)

mu_p is the policing rate, i.e. the action. Because the agent's action changes
backlog_p', which is part of the next state, this is a genuine MDP -- unlike the
logged-transition dataset, where next_state was read from the trace and did not
depend on the action.

SHARED CAPACITY IS WHAT MAKES THE PROBLEM NON-TRIVIAL
-----------------------------------------------------
The requested rates are projected onto sum(mu_p) <= link_capacity. Raising one
slice's rate therefore takes capacity from the others. Without this coupling the
optimal policy is the trivial "maximise every rate", which is exactly the
degenerate behaviour the old evaluator produced.
"""

import io
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRACE = REPO_ROOT / "Reinforcement Learning" / "revision" / "dataset_dqn_rich.csv"

PORTS = ("p1", "p2", "p4")
# Delay SLA per slice, milliseconds. Kept as the paper's evaluation thresholds
# so results stay comparable; override via the constructor.
DEFAULT_SLA_MS = {"p1": 6.0, "p2": 70.0, "p4": 7.0}


def load_arrival_trace(path=DEFAULT_TRACE):
    """Offered load per slice, in Mbps, from the measured campaign.

    collect_policy.sh writes ';'-delimited with ',' decimals and may wrap the
    header in a single pair of double quotes.
    """
    raw = Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
    cleaned = [ln.strip().replace('"', "") for ln in raw]
    df = pd.read_csv(io.StringIO("\n".join(cleaned)), sep=";", decimal=",")
    cols = [f"rx_mbps_{p}" for p in PORTS]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise SystemExit(f"{path} lacks {missing}")
    arr = df[cols].to_numpy(dtype=float)
    return np.clip(arr, 0.0, None)


class SliceEnv:
    """Multi-slice policing-rate control.

    state  (12,) : per slice -> [arrival Mbps, utilisation, delay ms, rate Mbps]
    action  (3,) : per slice in [-1, 1], relative change of the policing rate
    """

    def __init__(
        self,
        arrivals,
        link_capacity_mbps=15.0,
        rate_min_mbps=0.5,
        buffer_ms=200.0,
        dt=1.0,
        action_gain=0.20,
        sla_ms=None,
        episode_len=200,
        seed=0,
        random_init_alloc=False,
        reward_scale=1.0,
    ):
        self.arrivals = np.asarray(arrivals, dtype=float)
        if self.arrivals.ndim != 2 or self.arrivals.shape[1] != len(PORTS):
            raise ValueError(f"arrivals must be (T, {len(PORTS)})")
        self.C = float(link_capacity_mbps)
        self.rate_min = float(rate_min_mbps)
        self.buffer_ms = float(buffer_ms)
        self.dt = float(dt)
        self.action_gain = float(action_gain)
        self.sla = dict(DEFAULT_SLA_MS if sla_ms is None else sla_ms)
        self.episode_len = int(episode_len)
        self.random_init_alloc = bool(random_init_alloc)
        # Divides the raw reward. One fixed scalar, estimated once on the train
        # split under a reference policy and shared by every method, so no
        # algorithm gets a better-conditioned objective than another.
        self.reward_scale = float(reward_scale)
        self.rng = np.random.default_rng(seed)

        self.n = len(PORTS)
        self.state_dim = 4 * self.n
        self.action_dim = self.n
        self.reset()

    # -- capacity projection ------------------------------------------------
    def _project(self, rates):
        """Clip to [rate_min, C] then scale down so sum(rates) <= C.

        Scaling is applied to the headroom above rate_min so no slice can be
        starved below its floor by another slice's demand.
        """
        r = np.clip(rates, self.rate_min, self.C)
        total = r.sum()
        if total <= self.C:
            return r
        floor = self.rate_min * self.n
        headroom = self.C - floor
        if headroom <= 0:
            return np.full(self.n, self.C / self.n)
        excess = r - self.rate_min
        return self.rate_min + excess * (headroom / excess.sum())

    # -- core ---------------------------------------------------------------
    def reset(self, start=None):
        self.t = 0
        self.start = int(self.rng.integers(0, max(1, len(self.arrivals) - self.episode_len))) \
            if start is None else int(start)
        self.backlog = np.zeros(self.n)           # Mb
        if self.random_init_alloc:
            # A uniform start makes no_control, const_max and equal_split
            # produce identical allocations, because the action is a relative
            # change projected back onto the capacity simplex -- so a uniform
            # action is a no-op. Randomising the start separates them.
            w = self.rng.dirichlet(np.ones(self.n))
            self.rates = self._project(w * self.C)
        else:
            self.rates = self._project(np.full(self.n, self.C / self.n))
        self.delay_ms = np.zeros(self.n)
        self.drop = np.zeros(self.n)
        return self._obs()

    def _arrival(self):
        idx = (self.start + self.t) % len(self.arrivals)
        return self.arrivals[idx] * self.dt      # Mbps * s = Mb

    def _obs(self):
        idx = (self.start + self.t) % len(self.arrivals)
        lam = self.arrivals[idx]
        util = np.divide(lam, self.rates, out=np.zeros(self.n), where=self.rates > 0)
        return np.concatenate([lam, util, self.delay_ms, self.rates]).astype(np.float64)

    def step(self, action):
        a = np.clip(np.asarray(action, dtype=float).reshape(self.n), -1.0, 1.0)
        self.rates = self._project(self.rates * (1.0 + self.action_gain * a))

        arrival = self._arrival()
        capacity = self.rates * self.dt                       # Mb servable this step
        offered = self.backlog + arrival
        served = np.minimum(offered, capacity)
        backlog = offered - served

        buf = self.rates * (self.buffer_ms / 1000.0)          # Mb of buffer
        self.drop = np.maximum(0.0, backlog - buf)
        self.backlog = np.minimum(backlog, buf)

        # Little's law: W = L / mu. Guard mu > 0 via rate_min > 0.
        self.delay_ms = (self.backlog / self.rates) * 1000.0

        self.t += 1
        reward = self.reward()
        done = self.t >= self.episode_len
        info = {
            "delay_ms": self.delay_ms.copy(),
            "drop_mb": self.drop.copy(),
            "rates_mbps": self.rates.copy(),
            "served_mb": served.copy(),
            "arrival_mb": arrival.copy(),
            "violation": np.array([self.delay_ms[i] > self.sla[p] for i, p in enumerate(PORTS)]),
        }
        return self._obs(), reward, done, info

    def reward(self):
        """Covers every slice, unlike the paper's reward which penalised only P4
        latency (Eq. 10) and rewarded only P2 throughput (Eq. 8).

        Delay is scored relative to each slice's own SLA so the three ports are
        commensurate despite very different absolute thresholds.
        """
        ratio = np.array([self.delay_ms[i] / self.sla[p] for i, p in enumerate(PORTS)])
        delay_pen = np.sum(np.maximum(0.0, ratio - 1.0))
        drop_pen = float(self.drop.sum())
        return -(delay_pen + drop_pen) / self.reward_scale


# --------------------------------------------------------------------------
def _self_check():
    """Properties the old evaluator failed. Each assert encodes one of them."""
    rng = np.random.default_rng(0)
    arrivals = rng.uniform(3.0, 5.0, size=(500, 3))

    # 1. Shared capacity binds: rates never exceed the link.
    env = SliceEnv(arrivals, link_capacity_mbps=12.0, episode_len=50, seed=1)
    env.reset(start=0)
    for _ in range(50):
        env.step(np.ones(3))                      # everyone demands maximum
    assert env.rates.sum() <= 12.0 + 1e-9, env.rates
    assert np.all(env.rates >= env.rate_min - 1e-9)

    # 2. "Maximise everything" is NOT optimal -- the degenerate policy the old
    #    evaluator rewarded must now be beatable.
    #
    #    This needs ASYMMETRIC demand. Under symmetric arrivals the capacity
    #    projection turns "everyone asks for max" into an equal split, which is
    #    already optimal, and the test would prove nothing.
    skewed = np.column_stack([
        rng.uniform(7.0, 9.0, 500),    # p1 heavy
        rng.uniform(2.5, 3.5, 500),    # p2 moderate
        rng.uniform(0.5, 1.5, 500),    # p4 light
    ])

    def run(policy, seed=2):
        e = SliceEnv(skewed, link_capacity_mbps=12.0, episode_len=200, seed=seed)
        e.reset(start=0)
        total = 0.0
        for _ in range(200):
            _, r, _, _ = e.step(policy(e))
            total += r
        return total

    all_max = run(lambda e: np.ones(3))

    def demand_aware(e):
        """Allocate in proportion to each slice's mean demand."""
        target = skewed.mean(axis=0) / skewed.mean(axis=0).sum() * e.C
        return np.clip((target - e.rates) / (e.action_gain * np.maximum(e.rates, 1e-9)), -1, 1)

    fair = run(demand_aware)
    assert fair > all_max, f"const-max {all_max:.4f} should be beatable, fair={fair:.4f}"

    # 3. Action at t changes the state at t+1 -- a real MDP, not a bandit.
    e1 = SliceEnv(arrivals, episode_len=50, seed=3); e1.reset(start=0)
    e2 = SliceEnv(arrivals, episode_len=50, seed=3); e2.reset(start=0)
    e1.step(np.array([1.0, -1.0, 0.0]))
    e2.step(np.array([-1.0, 1.0, 0.0]))
    assert not np.allclose(e1._obs(), e2._obs()), "next state must depend on the action"

    # 4. Starving a slice raises its delay -- the relationship the old formula
    #    inverted for free.
    starve = SliceEnv(arrivals, link_capacity_mbps=12.0, episode_len=60, seed=4)
    starve.reset(start=0)
    for _ in range(60):
        starve.step(np.array([-1.0, 0.0, 0.0]))
    assert starve.delay_ms[0] > 0.0, "a starved slice must accumulate queueing delay"

    # 5. Overload produces drops.
    hot = SliceEnv(np.full((100, 3), 20.0), link_capacity_mbps=6.0, episode_len=60, seed=5)
    hot.reset(start=0)
    drops = 0.0
    for _ in range(60):
        _, _, _, info = hot.step(np.zeros(3))
        drops += info["drop_mb"].sum()
    assert drops > 0, "sustained overload must drop traffic"

    # 6. Real trace loads and has the grounded arrival columns.
    if DEFAULT_TRACE.exists():
        tr = load_arrival_trace()
        assert tr.shape[1] == 3 and len(tr) > 100, tr.shape
        assert np.isfinite(tr).all()

    print("slice_env self-check: all 6 properties hold")


if __name__ == "__main__":
    _self_check()
