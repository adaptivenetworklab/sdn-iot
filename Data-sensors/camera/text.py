import cv2
from ultralytics import YOLO
import time

print("Meload model YOLOv11n...")
model = YOLO("yolo11n.pt")

# COBA GANTI INDEX INI JIKA MASIH GAGAL: 0, 1, atau 2
CAMERA_INDEX = 0

print(f"Mencoba membuka kamera index {CAMERA_INDEX} dengan V4L2...")
cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

# Setup Resolusi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("FATAL ERROR: Kamera tidak terdeteksi sama sekali!")
    exit()

print("Kamera 'open', mencoba membaca frame pertama...")

# Cek bacaan frame pertama
ret, frame = cap.read()
if not ret:
    print("ERROR: Gagal membaca frame dari kamera (Frame kosong).")
    print("Tips: Coba ganti CAMERA_INDEX ke 1 atau cek kabel.")
    cap.release()
    exit()
else:
    print("Frame pertama berhasil dibaca! Memulai loop...")

while True:
    success, frame = cap.read()
    if not success:
        print("Stream terputus.")
        break

    # Inference
    results = model(frame, conf=0.5, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv11 Raspi 5", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
