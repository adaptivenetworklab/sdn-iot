#!/usr/bin/env python3
import socket
import json
import time
import csv
import os
from datetime import datetime, timezone

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9999

# ✅ BASE DIR sekarang udah pindah ke sdn-iot/pengujian
BASE_DIR = "/home/ovs/sdn-iot/pengujian"
OUT_CSV = os.path.join(BASE_DIR, "delay_log.csv")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print(f"[INFO] UDP delay listener running on {LISTEN_IP}:{LISTEN_PORT}")
print(f"[INFO] Output -> {OUT_CSV}")

# ✅ pastiin folder ada
os.makedirs(BASE_DIR, exist_ok=True)

# ✅ buat file + header kalau belum ada
if not os.path.exists(OUT_CSV):
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "device_id", "src_ip", "delay_ms"])

while True:
    data, addr = sock.recvfrom(65535)
    recv_ts = time.time()

    try:
        payload = json.loads(data.decode(errors="ignore"))
    except:
        continue

    device_id = payload.get("device_id", "unknown")
    send_ts = payload.get("send_ts", None)

    if send_ts is None:
        continue

    try:
        send_ts = float(send_ts)
    except:
        continue

    delay_ms = (recv_ts - send_ts) * 1000.0

    # ✅ filter delay ngawur
    if delay_ms < 0 or delay_ms > 60000:
        continue

    ts_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    src_ip = addr[0]

    with open(OUT_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts_iso, device_id, src_ip, f"{delay_ms:.3f}"])

    print(f"[OK] {ts_iso} dev={device_id} src={src_ip} delay={delay_ms:.3f}ms")
