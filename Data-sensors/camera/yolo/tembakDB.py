import cv2
import numpy as np
import time
import json
import base64
import requests
from datetime import datetime
from ultralytics import YOLO
from picamera2 import Picamera2

# --- KONFIGURASI API ---
DEST_IP = "100.89.115.120" 
DEST_PORT = "5003"
URL = f"http://{DEST_IP}:{DEST_PORT}/upload-json"
CAMERA_ID = "cam-01-lobby"

# --- INISIALISASI MODEL & KAMERA ---
# Menggunakan YOLO11n (pastikan file .pt atau folder .ncnn ada di direktori ini)
model = YOLO("yolo11n.pt", task='detect') 

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

def encode_image_to_base64(frame):
    """Mengubah array frame OpenCV menjadi string base64"""
    try:
        # Encode ke format JPG
        _, buffer = cv2.imencode('.jpg', frame)
        # Ubah ke base64 string
        return base64.b64encode(buffer).decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Gagal encode gambar: {e}")
        return None

print(f"✅ Kamera Aktif. Mengirim data real-time ke {URL}...")

try:
    while True:
        # 1. Ambil frame dari kamera
        frame_rgb = picam2.capture_array()
        
        # Konversi RGB (Picamera2) ke BGR (OpenCV & YOLO)
        frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        # 2. Deteksi YOLO11
        # verbose=False agar terminal tidak penuh dengan log deteksi
        results = model.predict(frame_bgr, conf=0.4, imgsz=640, stream=True, verbose=False)
        
        person_count = 0
        for r in results:
            # Hitung jumlah orang (Class ID 0 dalam dataset COCO adalah 'person')
            person_count = int((r.boxes.cls == 0).sum().item())
            
            # (Opsional) Dapatkan frame yang sudah ada kotak deteksinya
            annotated_frame = r.plot()

        # 3. Siapkan Payload
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        img_base64 = encode_image_to_base64(frame_bgr) # Kirim frame asli atau annotated_frame

        if img_base64:
            payload = {
                "timestamp": timestamp,
                "person_count": person_count,
                "image_base64": img_base64,
                "camera_id": CAMERA_ID
            }

            # 4. Kirim ke Server
            try:
                # Menggunakan timeout agar program tidak hang jika jaringan lambat
                response = requests.post(URL, json=payload, timeout=5)
                print(f"[{timestamp}] SENT | Real Count: {person_count} | Status: {response.status_code}")
            except Exception as e:
                print(f"[{timestamp}] Error Pengiriman: {e}")

        # 5. Tampilkan Preview Lokal (Bisa dimatikan jika running headless)
        cv2.imshow("YOLO11 Real-time Sender", annotated_frame)
        
        # Tekan 'q' untuk berhenti
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Berikan sedikit jeda agar CPU tidak 100% (Opsional)
        # time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[INFO] Menghentikan program...")
finally:
    picam2.stop()
    cv2.destroyAllWindows()
