import socket
import time
import random
import json
import hashlib
import os
from datetime import datetime, timezone

DEST_IP = "192.168.15.239"   # IP OVS
DEST_PORT = 9999

CAMERA_ID = "cam-01-lobby"
IMAGE_PATH = "/home/sdn/Gambar/test.png"
RANDOM_INTERVAL = 60

# ukuran payload random (byte) -> bikin grafik throughput naik turun
MIN_PAYLOAD_BYTES = 100
MAX_PAYLOAD_BYTES = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_image_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def make_random_string(n):
    # n karakter ascii
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(n))

last_random_time = 0
current_person_count = random.randint(1, 10)
current_send_delay = random.randint(1, 5)

print("[INFO] Camera UDP sender started (RANDOM PAYLOAD MODE)")

while True:
    now = time.time()

    # update parameter tiap 60 detik
    if now - last_random_time >= RANDOM_INTERVAL:
        current_person_count = random.randint(1, 10)
        current_send_delay = random.randint(1, 5)
        last_random_time = now

        print("\n[UPDATE]")
        print(" People:", current_person_count)
        print(" Delay :", current_send_delay, "s\n")

    # payload random size
    dummy_size = random.randint(MIN_PAYLOAD_BYTES, MAX_PAYLOAD_BYTES)
    dummy_data = make_random_string(dummy_size)

    payload = {
        "type": "camera",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "camera_id": CAMERA_ID,
        "person_count": current_person_count,
        "image_name": os.path.basename(IMAGE_PATH),
        "image_hash": get_image_hash(IMAGE_PATH),

        # ✅ ini yang bikin ukuran paket berubah-ubah
        "dummy_payload": dummy_data,
        "dummy_size": dummy_size
    }

    sock.sendto(json.dumps(payload).encode(), (DEST_IP, DEST_PORT))

    print(f"[SENT] count={current_person_count} delay={current_send_delay}s dummy_size={dummy_size}B")

    time.sleep(current_send_delay)
