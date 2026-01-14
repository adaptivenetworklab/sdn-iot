import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from datetime import datetime
import base64
import requests
import time
import json

# --- Konfigurasi Pengirim ---
CAMERA_ID = "cam-01-lobby"  # ID unik untuk kamera ini
FLASK_SERVER_URL = "http://10.0.1.16:5003/upload-json"  # Sesuaikan URL endpoint server Flask
SEND_INTERVAL = 3  # Detik

# --- Inisialisasi ---
model = YOLO("yolov8n.pt")
picam2 = Picamera2()
picam2.start()
print(f"[INFO] Kamera '{CAMERA_ID}' siap. Tekan Ctrl+C untuk berhenti.")

last_send_time = 0

try:
    while True:
        # Proses deteksi (tetap sama)
        frame = picam2.capture_array()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

        # Flip gambar secara vertikal
        flipped_frame = cv2.flip(frame_rgb, 0)  # 0 untuk flip vertikal

        # Deteksi objek menggunakan model YOLO
        results = model(flipped_frame, verbose=False)
        annotated_frame = results[0].plot()

        names = results[0].names
        classes = results[0].boxes.cls.cpu().numpy().astype(int)
        person_count = sum(1 for cls in classes if names[cls] == "person")

        now = datetime.now()
        timestamp_str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

        current_time = time.time()
        if current_time - last_send_time >= SEND_INTERVAL:
            _, buffer = cv2.imencode('.jpg', annotated_frame)
            img_base64 = base64.b64encode(buffer).decode('utf-8')

            # Payload JSON untuk dikirim ke server Flask
            payload = {
                "timestamp": timestamp_str,
                "person_count": person_count,
                "image_base64": img_base64,  # Sesuaikan key 'image_base64' dengan server Flask
                "camera_id": CAMERA_ID  # ID kamera
            }

            try:
                response = requests.post(FLASK_SERVER_URL, json=payload)
                print(f"[{timestamp_str}] Data terkirim: count={person_count}, status={response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"[{timestamp_str}] Gagal mengirim data: {e}")

            last_send_time = current_time

except KeyboardInterrupt:
    print("\n[INFO] Program dihentikan.")
finally:
    print("[INFO] Menutup kamera.")
