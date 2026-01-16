import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_file = sys.argv[1]
interval = float(sys.argv[2])
out_png = sys.argv[3]

df = pd.read_csv(csv_file)
df["timestamp"] = pd.to_datetime(df["timestamp"])

df["rx_bytes_diff"] = df["rx_bytes"].diff()
df["tx_bytes_diff"] = df["tx_bytes"].diff()

df["rx_mbps"] = (df["rx_bytes_diff"] * 8) / (interval * 1_000_000)
df["tx_mbps"] = (df["tx_bytes_diff"] * 8) / (interval * 1_000_000)

df = df.dropna()

print("=== SUMMARY ===")
print("RX avg Mbps:", df["rx_mbps"].mean())
print("TX avg Mbps:", df["tx_mbps"].mean())
print("RX peak Mbps:", df["rx_mbps"].max())
print("TX peak Mbps:", df["tx_mbps"].max())

plt.figure()
plt.plot(df["timestamp"], df["rx_mbps"], label="RX Mbps")
plt.plot(df["timestamp"], df["tx_mbps"], label="TX Mbps")
plt.xlabel("Time")
plt.ylabel("Throughput (Mbps)")
plt.title("OVS Port Throughput")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig(out_png, dpi=200)
plt.show()
