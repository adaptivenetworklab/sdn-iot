import time
import random
import json
import base64
import os
import requests
from datetime import datetime

# --- Konfigurasi ---
# Alamat IP Database/Server Flask (Sesuaikan dengan IP Server kamu)
DEST_IP = "100.89.115.120" 
DEST_PORT = "5003"
URL = f"http://{DEST_IP}:{DEST_PORT}/upload-json"

CAMERA_ID = "cam-01-lobby"
IMAGE_SOURCE = "/home/sdn/Gambar/test.png" # Path gambar dummy
SEND_INTERVAL = 5    # Kirim tiap 5 detik
RANDOM_INTERVAL = 60 # Update jumlah orang tiap 60 detik

def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Gagal membaca gambar: {e}")
        return None

# Inisialisasi variabel untuk randomizing
last_random_time = 0
current_person_count = random.randint(1, 10)

try:
    print(f"[INFO] Mengirim data ke {URL}...")
    while True:
        current_time = time.time()

        # Update jumlah orang setiap 1 menit
        if current_time - last_random_time >= RANDOM_INTERVAL:
            current_person_count = random.randint(1, 10)
            last_random_time = current_time
            print(f"[UPDATE] Jumlah orang baru: {current_person_count}")

        # Siapkan data
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        img_data = get_image_base64(IMAGE_SOURCE)

        if img_data:
            # Buat pesan JSON (Struktur sesuai yang diminta API Database)
            payload = {
                "timestamp": timestamp,
                "person_count": current_person_count,
                "image_base64": img_data,
                "camera_id": CAMERA_ID
            }

            try:
                # Mengirim data menggunakan HTTP POST (mirip konsep sock.sendto tapi versi HTTP)
                response = requests.post(URL, json=payload, timeout=10)
                print(f"[SENT] {timestamp} | Count: {current_person_count} | Status: {response.status_code}")
            except Exception as e:
                print(f"[ERROR] Gagal mengirim: {e}")

        time.sleep(SEND_INTERVAL)

except KeyboardInterrupt:
    print("\n[INFO] Pengirim berhenti.")
