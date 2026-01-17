import socket
import json
import time
from datetime import datetime
import csv
import os

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9999

OUT_CSV = "delay_log.csv"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print(f"[INFO] UDP delay listener running on {LISTEN_IP}:{LISTEN_PORT}")
print(f"[INFO] Output -> {OUT_CSV}")

# init csv
is_new = not os.path.exists(OUT_CSV)
with open(OUT_CSV, "a", newline="") as f:
    writer = csv.writer(f)
    if is_new:
        writer.writerow(["timestamp", "device_id", "src_ip", "delay_ms"])

while True:
    data, addr = sock.recvfrom(65535)
    recv_ts = time.time()
    src_ip = addr[0]

    try:
        payload = json.loads(data.decode(errors="ignore"))
        device_id = payload.get("device_id", "unknown")
        send_ts = float(payload.get("send_ts", 0))

        if send_ts <= 0:
            continue

        delay_ms = (recv_ts - send_ts) * 1000.0
        ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        with open(OUT_CSV, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([ts, device_id, src_ip, f"{delay_ms:.3f}"])

    except Exception:
        pass
