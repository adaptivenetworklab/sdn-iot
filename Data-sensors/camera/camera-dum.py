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

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_image_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

last_random_time = 0
current_person_count = random.randint(1, 10)
current_send_delay = random.randint(1, 5)

print("[INFO] Camera UDP sender started")

while True:
    now = time.time()

    if now - last_random_time >= RANDOM_INTERVAL:
        current_person_count = random.randint(1, 10)
        current_send_delay = random.randint(1, 5)
        last_random_time = now

    payload = {
        "type": "camera",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "camera_id": CAMERA_ID,
        "person_count": current_person_count,
        "image_name": os.path.basename(IMAGE_PATH),
        "image_hash": get_image_hash(IMAGE_PATH)
    }

    sock.sendto(json.dumps(payload).encode(), (DEST_IP, DEST_PORT))
    print("[SENT]", payload)

    time.sleep(current_send_delay)
