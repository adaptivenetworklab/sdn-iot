import cv2
import numpy as np
from ultralytics import YOLO
from picamera2 import Picamera2

# 1. Inisialisasi YOLO11 (Gunakan NCNN jika sudah di-export agar cepat)
model = YOLO("yolo11n.pt", task='detect') 

# 2. Inisialisasi Picamera2 (Native RPi 5)
picam2 = Picamera2()
# Konfigurasi resolusi rendah (640x480) agar FPS tetap tinggi untuk AI
config = picam2.create_video_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

print("? Kamera ov5647 Aktif. Memulai Deteksi YOLO11...")

try:
    while True:
        # 3. Ambil frame langsung sebagai array numpy
        frame = picam2.capture_array()
        
        # Picamera2 menghasilkan RGB, OpenCV butuh BGR untuk imshow
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 4. Jalankan Deteksi YOLO11
        results = model.predict(frame_bgr, conf=0.4, imgsz=640, stream=True, verbose=False)
        
        for r in results:
            annotated_frame = r.plot()
            
            # 5. Tampilkan Hasil
            cv2.imshow("RPi 5 - YOLO11 + Picamera2", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("\nMenghentikan program...")
finally:
    picam2.stop()
    cv2.destroyAllWindows()
