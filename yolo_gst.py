import cv2
import time
from ultralytics import YOLO

# Load Model
print("⏳ Meload model YOLOv11n...")
model = YOLO("yolo11n.pt")

# --- SETTING KHUSUS RASPBERRY PI 5 ---
# Kita tidak pakai index (0/1), tapi pakai GStreamer Pipeline.
# Ini memaksa OpenCV mengambil data langsung dari libcamera.
gst_pipeline = (
    "libcamerasrc ! "
    "video/x-raw, width=640, height=480, framerate=30/1 ! "
    "videoconvert ! "
    "appsink"
)

print(f"📷 Membuka kamera via GStreamer...")
# Perhatikan cv2.CAP_GSTREAMER di parameter kedua
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("❌ Gagal membuka kamera via GStreamer.")
    print("Pastikan Anda sudah install: sudo apt install gstreamer1.0-libcamera")
    exit()

print("✅ Kamera Terbuka! Tekan 'q' untuk keluar.")

# Inisialisasi waktu untuk FPS
prev_time = 0

while True:
    success, frame = cap.read()
    if not success:
        print("⚠️ Frame drop / gagal baca.")
        break

    # 1. Inference YOLO
    # stream=True agar lebih hemat memori
    results = model(frame, stream=True, conf=0.5, verbose=False)

    # 2. Gambar kotak deteksi
    for r in results:
        annotated_frame = r.plot()

    # 3. Hitung FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Tampilkan FPS
    cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 4. Tampilkan Gambar
    cv2.imshow("YOLOv11 - Pi 5 GStreamer", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
