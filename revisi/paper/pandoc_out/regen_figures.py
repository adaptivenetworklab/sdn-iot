import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = r"D:\Kuliah\Semester 6\Riset\sdn-iot\Reinforcement Learning\revision"
OUT = r"D:\Kuliah\Semester 6\Riset\sdn-iot\revisi\paper\figures"

# --- Fig 5-8: Loss-only convergence plots (Reward panel dropped, not per-model meaningful) ---
models = [
    ("DQN", "fig5_dqn_convergence.png", "red"),
    ("DDQN", "fig6_ddqn_convergence.png", "orange"),
    ("PPO_Standard", "fig7_ppo_convergence.png", "blue"),
    ("Proposed_(SDH-PPO)", "fig8_sdh_ppo_convergence.png", "green"),
]

for name, outfile, color in models:
    df = pd.read_csv(f"{BASE}/training_convergence_{name}.csv")
    plt.figure(figsize=(6, 4))
    plt.plot(df["Epoch"], df["Loss"], color=color, alpha=0.8, linewidth=1.2)
    plt.title(f"{name.replace('_', ' ')} Training Loss (Offline)")
    plt.xlabel("Training Iteration")
    plt.ylabel("Loss Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{OUT}/{outfile}", dpi=300)
    plt.close()
    print("saved", outfile)

# --- Fig 4: Port delay tracking, 3-subplot, from real viz_detail CSVs ---
SLA = {"P1": 6.0, "P2": 70.0, "P4": 7.0}
port_labels = [
    ("P1", "DHT11 (Port 1, Smart Building)"),
    ("P2", "Camera (Port 2, Smart City)"),
    ("P4", "Heart Rate (Port 4, Healthcare - Critical)"),
]
model_colors = {
    "Proposed_(SDH-PPO)": "green",
    "PPO_Standard": "blue",
    "DDQN": "orange",
    "DQN": "red",
    "Static": "gray",
}
model_display = {
    "Proposed_(SDH-PPO)": "Proposed (SDH-PPO)",
    "PPO_Standard": "PPO Standard",
    "DDQN": "DDQN",
    "DQN": "DQN",
    "Static": "Static",
}

fig, axes = plt.subplots(3, 1, figsize=(7, 11))
for ax, (col, label) in zip(axes, port_labels):
    for mkey, color in model_colors.items():
        try:
            df = pd.read_csv(f"{BASE}/viz_detail_{mkey}.csv")
        except FileNotFoundError:
            continue
        data = df[col].tail(100).values
        is_proposed = "Proposed" in mkey
        ax.plot(
            data,
            label=model_display[mkey],
            color=color,
            linewidth=2.2 if is_proposed else 1.0,
            marker="o" if is_proposed else None,
            markersize=3 if is_proposed else 0,
            alpha=0.85,
        )
    ax.axhline(y=SLA[col], color="red", linestyle="--", linewidth=1.8, label=f"SLA Threshold ({SLA[col]}ms)")
    ax.set_title(f"Delay Tracking: {label}", fontsize=11, fontweight="bold")
    ax.set_ylabel("Delay (ms)")
    ax.set_xlabel("Test Samples (held-out split, last 100)")
    ax.legend(loc="upper right", ncol=2, fontsize=7)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f"{OUT}/fig4_port_delay_track.png", dpi=300)
plt.close()
print("saved fig4_port_delay_track.png")
