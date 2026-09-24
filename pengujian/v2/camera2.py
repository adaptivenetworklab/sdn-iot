#!/usr/bin/python3
import socket
import time
import random
import json
import hashlib
import os
from datetime import datetime, timezone

DEST_IP = "192.168.15.239"   # IP OVS listener
DEST_PORT = 9999

DEVICE_ID = "camera"         # port 2
DEVICE_TYPE = "camera"

IMAGE_PATH = "/home/sdn/Gambar/test.png"

# ✅ random payload tapi aman (anti-fragment)
MIN_PAYLOAD_BYTES = 500
MAX_PAYLOAD_BYTES = 1500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)  # timeout ACK biar ga nge-freeze

seq = 0

def get_image_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return "nofile"

def make_random_string(n):
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(n))

print("[INFO] Camera sender started (RTT + random payload)")

while True:
    seq += 1
    send_ts = time.time()

    dummy_size = random.randint(MIN_PAYLOAD_BYTES, MAX_PAYLOAD_BYTES)

    payload = {
        "device_id": DEVICE_ID,
        "type": DEVICE_TYPE,

        "seq": seq,
        "send_ts": send_ts,

        "timestamp": datetime.now(timezone.utc).isoformat(),

        "person_count": random.randint(1, 10),
        "image_name": os.path.basename(IMAGE_PATH),
        "image_hash": get_image_hash(IMAGE_PATH),

        "dummy_size": dummy_size,
        "dummy_payload": make_random_string(dummy_size)
    }

    # encode dulu untuk hitung payload_bytes
    raw = json.dumps(payload).encode()
    payload["payload_bytes"] = len(raw)

    # encode ulang supaya payload_bytes ikut terkirim
    raw = json.dumps(payload).encode()

    # kirim packet
    t0 = time.time()
    try:
        sock.sendto(raw, (DEST_IP, DEST_PORT))
        print(f"[SENT] seq={seq} bytes={len(raw)} dummy={dummy_size}B")
    except Exception as e:
        print(f"[ERROR] UDP send failed: {e}")
        time.sleep(1)
        continue

    # tunggu ACK buat RTT
    try:
        ack_data, _ = sock.recvfrom(4096)
        t1 = time.time()

        ack = json.loads(ack_data.decode(errors="ignore"))

        if ack.get("type") == "ack" and ack.get("seq") == seq:
            rtt_ms = (t1 - t0) * 1000
            print(f"   [ACK] seq={seq} RTT={rtt_ms:.3f} ms")
        else:
            print("   [WARN] ACK mismatch / unknown ACK format")

    except socket.timeout:
        print("   [WARN] ACK timeout (listener down / packet loss / OVS overload)")

    except Exception as e:
        print(f"   [WARN] ACK error: {e}")

    time.sleep(1)
