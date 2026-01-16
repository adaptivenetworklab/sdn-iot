import cv2
import time
from ultralytics import YOLO

# --- CONFIG ---
# Coba index 2 dulu (Paling umum di Raspi 5), kalau gagal dia akan cari sendiri
TARGET_INDEX = 2 
MODEL_PATH = "yolo11n.pt"
# --------------

print(f"Meload model {MODEL_PATH}...")
model = YOLO(MODEL_PATH)

def find_working_camera():
    # Cek index 0 sampai 5
    for i in range(6):
        print(f"Checking camera index {i}...", end=" ")
        cap = cv2.VideoCapture(i, cv2.CAP_V4L2)
        if cap.isOpened():
            # Coba baca 1 frame
            ret, _ = cap.read()
            if ret:
                print("SUCCESS! (Gambar ditemukan)")
                cap.release()
                return i
            else:
                print("Gagal baca frame (Mungkin Metadata/Unicam).")
        else:
            print("Tidak ada device.")
        cap.release()
    return -1

# 1. Coba buka index target
print(f"\nMencoba membuka kamera index {TARGET_INDEX} dengan V4L2...")
cap = cv2.VideoCapture(TARGET_INDEX, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 2. Validasi
ret, frame = cap.read()
if not ret:
    print(f"\n⚠️ Index {TARGET_INDEX} gagal/kosong. Mencari index yang benar secara otomatis...")
    cap.release()
    
    valid_index = find_working_camera()
    if valid_index == -1:
        print("❌ Error Fatal: Tidak ada kamera yang bisa menghasilkan gambar.")
        print("Solusi: Cek kabel, atau pastikan 'rpicam-hello' masih jalan.")
        exit()
    
    print(f"✅ Kamera ditemukan di Index {valid_index}! Menggunakan index ini.")
    cap = cv2.VideoCapture(valid_index, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("\n🚀 Mulai Deteksi YOLOv11 (Tekan 'q' untuk stop)...")

while True:
    success, frame = cap.read()
    if not success:
        print("Frame drop / Camera disconnect.")
        break

    # Inference
    results = model(frame, conf=0.5, verbose=False)
    annotated_frame = results[0].plot()

    # Hitung FPS sederhana
    cv2.imshow("YOLOv11 - Pi 5 Fix", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
