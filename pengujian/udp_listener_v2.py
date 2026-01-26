#!/usr/bin/env python3
import socket, json, time, csv, os
from datetime import datetime, timezone

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9999

BASE_DIR = "/home/ovs/sdn-iot/pengujian"
OUT_CSV = os.path.join(BASE_DIR, "delay_log.csv")

os.makedirs(BASE_DIR, exist_ok=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

# header kalau belum ada
if not os.path.exists(OUT_CSV):
    with open(OUT_CSV, "w", newline="") as f:
        csv.writer(f).writerow([
            "timestamp", "device_id", "src_ip", "seq",
            "payload_bytes", "oneway_delay_ms"
        ])

print(f"[INFO] UDP listener running on {LISTEN_IP}:{LISTEN_PORT}")
print(f"[INFO] Output -> {OUT_CSV}")

while True:
    data, addr = sock.recvfrom(65535)
    recv_ts = time.time()
    src_ip, src_port = addr[0], addr[1]
    payload_bytes = len(data)

    try:
        payload = json.loads(data.decode(errors="ignore"))
    except:
        continue

    device_id = payload.get("device_id", "unknown")
    seq = payload.get("seq", -1)

    send_ts = payload.get("send_ts", None)
    if send_ts is None:
        continue

    try:
        send_ts = float(send_ts)
    except:
        continue

    oneway_delay_ms = (recv_ts - send_ts) * 1000.0

    # filter outlier ekstrim
    if oneway_delay_ms < -100 or oneway_delay_ms > 60000:
        continue

    # ✅ Kirim ACK balik (untuk RTT)
    ack = {
        "device_id": device_id,
        "seq": seq,
        "ack_ts": recv_ts
    }
    sock.sendto(json.dumps(ack).encode(), (src_ip, src_port))

    ts_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    with open(OUT_CSV, "a", newline="") as f:
        csv.writer(f).writerow([
            ts_iso, device_id, src_ip, seq,
            payload_bytes, f"{oneway_delay_ms:.3f}"
        ])

    print(f"[OK] {ts_iso} dev={device_id} seq={seq} bytes={payload_bytes} delay={oneway_delay_ms:.3f}ms")
