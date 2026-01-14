import time
import random
import json
import base64
import os
import requests
from datetime import datetime

# --- Konfigurasi ---
DEST_IP = "100.89.115.120" 
DEST_PORT = "5003"
URL = f"http://{DEST_IP}:{DEST_PORT}/upload-json"

CAMERA_ID = "cam-01-lobby"
IMAGE_SOURCE = "/home/sdn/Gambar/test.png" 
RANDOM_INTERVAL = 60 # Update parameter setiap 1 menit

def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Gagal membaca gambar: {e}")
        return None

# --- Inisialisasi Parameter Awal ---
last_random_time = 0
current_person_count = random.randint(1, 10)
current_send_delay = random.randint(1, 5) # Jeda pengiriman (1-5 detik)

try:
    print(f"[INFO] Mengirim data ke {URL}...")
    print(f"[START] Delay awal: {current_send_delay} detik")
    
    while True:
        current_time = time.time()

        # Update parameter (Orang & Delay) setiap 1 menit
        if current_time - last_random_time >= RANDOM_INTERVAL:
            current_person_count = random.randint(1, 10)
            current_send_delay = random.randint(1, 5) # Merandom jeda baru
            last_random_time = current_time
            print(f"\n[UPDATE] Konfigurasi Baru:")
            print(f" > Jumlah orang: {current_person_count}")
            print(f" > Jeda antar paket: {current_send_delay} detik\n")

        # Siapkan dan Kirim Data
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        img_data = get_image_base64(IMAGE_SOURCE)

        if img_data:
            payload = {
                "timestamp": timestamp,
                "person_count": current_person_count,
                "image_base64": img_data,
                "camera_id": CAMERA_ID
            }

            try:
                response = requests.post(URL, json=payload, timeout=10)
                print(f"[{timestamp}] SENT | Count: {current_person_count} | Delay: {current_send_delay}s | Status: {response.status_code}")
            except Exception as e:
                print(f"[{timestamp}] ERROR: {e}")

        # Gunakan jeda yang sudah dirandom
        time.sleep(current_send_delay)

except KeyboardInterrupt:
    print("\n[INFO] Pengirim berhenti.")
