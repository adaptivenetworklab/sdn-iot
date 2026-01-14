import cv2
from ultralytics import YOLO
import time

# 1. Load Model YOLOv11 Nano (paling ringan)
# Saat pertama kali dijalankan, ini akan otomatis mendownload 'yolo11n.pt'
print("Meload model YOLOv11n...")
model = YOLO("yolo11n.pt")

# 2. Inisialisasi Kamera
# Pada Raspi 5 (Bookworm), biasanya index 0 bekerja dengan libcamera
# Coba paksa gunakan backend V4L2
# Kadang kamera ada di index 0, kadang di index 1 atau lebih tergantung device
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Opsional: Jika masih gelap/gagal, coba ganti format video ke MJPG
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

# Atur resolusi kamera (rendahkan sedikit agar FPS naik)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Tidak dapat membuka kamera.")
    exit()

print("Kamera terbuka. Tekan 'q' untuk keluar.")

# Hitung FPS
prev_frame_time = 0
new_frame_time = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # 3. Lakukan Inference (Deteksi)
    # conf=0.5 berarti hanya tampilkan deteksi dengan keyakinan > 50%
    results = model(frame, conf=0.5, verbose=False)

    # 4. Visualisasi Hasil
    # Plot hasil deteksi ke dalam frame gambar
    annotated_frame = results[0].plot()

    # Hitung FPS manual
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    
    # Tampilkan FPS di pojok kiri atas
    cv2.putText(annotated_frame, f'FPS: {int(fps)}', (10, 30), 
                cv2.putText(cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)[0], 
                1, (0, 255, 0), 2)

    # Tampilkan window
    cv2.imshow("YOLOv11 Raspi 5", annotated_frame)

    # Tekan 'q' untuk stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
