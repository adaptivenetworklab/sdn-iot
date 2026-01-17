import pandas as pd
import matplotlib.pyplot as plt

CSV = "dataset_dqn.csv"

df = pd.read_csv(CSV)

# ✅ parse timestamp aman
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)

# ✅ buang baris yang timestamp-nya rusak
df = df.dropna(subset=["timestamp"])

# ✅ convert numeric (kalau ada kosong jadi NaN)
cols = [
    "rx_mbps_p1","tx_mbps_p1","drop_p1","delay_ms_p1",
    "rx_mbps_p2","tx_mbps_p2","drop_p2","delay_ms_p2",
    "rx_mbps_p4","tx_mbps_p4","drop_p4","delay_ms_p4",
]
for c in cols:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

# =======================
# PLOT RX Throughput
# =======================
plt.figure()
plt.plot(df["timestamp"], df["rx_mbps_p1"], label="RX Port 1 (dht11)")
plt.plot(df["timestamp"], df["rx_mbps_p2"], label="RX Port 2 (camera)")
plt.plot(df["timestamp"], df["rx_mbps_p4"], label="RX Port 4 (max)")
plt.xlabel("Time")
plt.ylabel("Mbps")
plt.title("RX Throughput 3 Ports")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("rx_mbps_3ports.png", dpi=200)
plt.show()

# =======================
# PLOT Delay
# =======================
plt.figure()
plt.plot(df["timestamp"], df["delay_ms_p1"], label="Delay Port 1 (dht11)")
plt.plot(df["timestamp"], df["delay_ms_p2"], label="Delay Port 2 (camera)")
plt.plot(df["timestamp"], df["delay_ms_p4"], label="Delay Port 4 (max)")
plt.xlabel("Time")
plt.ylabel("Delay (ms)")
plt.title("Delay (Device → OVS)")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("delay_ms_3ports.png", dpi=200)
plt.show()

print("[DONE] Saved: rx_mbps_3ports.png & delay_ms_3ports.png")
