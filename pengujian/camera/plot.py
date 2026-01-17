import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_file = sys.argv[1]
interval = float(sys.argv[2])
out_png = sys.argv[3]

# setting smoothing
WINDOW_SECONDS = 10  # rata-rata per 10 detik
CLIP_MAX_MBPS = 20   # batas maksimum biar spike tidak ngerusak skala

df = pd.read_csv(csv_file)
df["timestamp"] = pd.to_datetime(df["timestamp"])

df["rx_bytes_diff"] = df["rx_bytes"].diff()
df["tx_bytes_diff"] = df["tx_bytes"].diff()

df["rx_mbps"] = (df["rx_bytes_diff"] * 8) / (interval * 1_000_000)
df["tx_mbps"] = (df["tx_bytes_diff"] * 8) / (interval * 1_000_000)

df = df.dropna()

# --- Downsample (average tiap WINDOW_SECONDS) ---
df = df.set_index("timestamp")
df_agg = df[["rx_mbps", "tx_mbps"]].resample(f"{WINDOW_SECONDS}S").mean()

# --- Clip spike biar grafik kebaca ---
df_agg["rx_mbps_clip"] = df_agg["rx_mbps"].clip(upper=CLIP_MAX_MBPS)
df_agg["tx_mbps_clip"] = df_agg["tx_mbps"].clip(upper=CLIP_MAX_MBPS)

print("=== SUMMARY ===")
print("Samples original:", len(df))
print("Samples agg     :", len(df_agg))
print("RX avg Mbps:", df["rx_mbps"].mean())
print("TX avg Mbps:", df["tx_mbps"].mean())
print("RX peak Mbps:", df["rx_mbps"].max())
print("TX peak Mbps:", df["tx_mbps"].max())

# ===== Plot =====
plt.figure()
plt.plot(df_agg.index, df_agg["rx_mbps_clip"], label=f"RX Mbps (avg {WINDOW_SECONDS}s)")
plt.plot(df_agg.index, df_agg["tx_mbps_clip"], label=f"TX Mbps (avg {WINDOW_SECONDS}s)")
plt.xlabel("Time")
plt.ylabel("Throughput (Mbps)")
plt.title(f"OVS Port Throughput (clipped max {CLIP_MAX_MBPS} Mbps)")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig(out_png, dpi=200)
plt.show()
