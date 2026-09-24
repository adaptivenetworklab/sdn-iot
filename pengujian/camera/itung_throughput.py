import sys
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = sys.argv[1]
INTERVAL = float(sys.argv[2])
OUT_PNG = sys.argv[3]

SMOOTH_SECONDS = 10     # rata-rata per 10 detik
YMAX = 10               # batas sumbu Y biar kebaca

df = pd.read_csv(CSV_FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

df["rx_bytes_diff"] = df["rx_bytes"].diff()
df["tx_bytes_diff"] = df["tx_bytes"].diff()

df["rx_mbps"] = (df["rx_bytes_diff"] * 8) / (INTERVAL * 1_000_000)
df["tx_mbps"] = (df["tx_bytes_diff"] * 8) / (INTERVAL * 1_000_000)

df = df.dropna()

# smoothing 10 detik
df = df.set_index("timestamp")
df_s = df[["rx_mbps", "tx_mbps"]].resample(f"{SMOOTH_SECONDS}S").mean()

print("=== SUMMARY ===")
print("RX avg Mbps:", df["rx_mbps"].mean())
print("TX avg Mbps:", df["tx_mbps"].mean())
print("RX peak Mbps:", df["rx_mbps"].max())
print("TX peak Mbps:", df["tx_mbps"].max())

plt.figure()
plt.plot(df_s.index, df_s["rx_mbps"], label=f"RX Mbps (avg {SMOOTH_SECONDS}s)")
plt.plot(df_s.index, df_s["tx_mbps"], label=f"TX Mbps (avg {SMOOTH_SECONDS}s)")
plt.xlabel("Time")
plt.ylabel("Throughput (Mbps)")
plt.title("OVS Port Throughput (Smoothed)")
plt.ylim(0, YMAX)  # ini bikin grafik kebaca
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=200)
plt.show()

print(f"[DONE] Saved -> {OUT_PNG}")
