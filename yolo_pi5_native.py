import time
import cv2
import numpy as np
from ultralytics import YOLO

# Import Library Native Raspberry Pi 5
try:
    from picamera2 import Picamera2
except ImportError:
    print("FATAL ERROR: Library 'picamera2' tidak terdeteksi!")
    print("Pastikan Anda membuat venv dengan: python3 -m venv --system-site-packages yolo_env")
    exit()

# 1. Setup Model
print("⏳ Meload Model YOLOv11n...")
model = YOLO("yolo11n.pt")

# 2. Setup Kamera Native (Picamera2)
# Ini langsung mengakses hardware ISP Pi 5, jauh lebih cepat dari OpenCV standard
print("📷 Menyalakan Hardware Kamera Pi 5...")
picam2 = Picamera2()

# Konfigurasi agar outputnya format BGR (format yang disukai OpenCV)
config = picam2.create_preview_configuration(main={"size": (640, 480), "format": "BGR888"})
picam2.configure(config)
picam2.start()

print("✅ Sistem Siap! Tekan 'q' pada jendela untuk stop.")

# Variabel FPS
prev_time = 0

# 3. Loop Utama
try:
    while True:
        # Ambil frame langsung dari memori kamera (Zero-copy jika memungkinkan)
        # capture_array() menghasilkan numpy array yang siap untuk OpenCV
        frame = picam2.capture_array()

        # Inference YOLO
        # stream=True untuk performa, verbose=False agar terminal bersih
        results = model(frame, stream=True, conf=0.5, verbose=False)

        # Visualisasi
        for r in results:
            annotated_frame = r.plot()

        # Hitung FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        # Tampilkan FPS
        cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Tampilkan di Layar
        cv2.imshow("YOLOv11 - Native Pi 5", annotated_frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Force Stop...")

# Cleanup
picam2.stop()
cv2.destroyAllWindows()
print("Program selesai.")
