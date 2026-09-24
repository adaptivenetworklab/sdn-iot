import cv2
from ultralytics import YOLO

# Tambahkan task='detect' untuk menghilangkan warning
# Gunakan model NCNN untuk performa maksimal di RPi 5
try:
    model = YOLO("yolo11n_ncnn_model", task='detect') 
except:
    print("Model NCNN tidak ditemukan, mendownload model standar...")
    model = YOLO("yolo11n.pt", task='detect')

# Inisialisasi Kamera
cap = cv2.VideoCapture(0)

# Cek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("? Error: Kamera tidak terdeteksi!")
    exit()

print("? Memulai deteksi YOLO11... Tekan 'q' untuk berhenti.")

while True:
    success, frame = cap.read()
    if not success:
        print("Gagal mengambil gambar dari kamera.")
        break
    
    # Jalankan Inference
    # verbose=False akan membersihkan log terminal dari teks deteksi berulang
    results = model.predict(frame, conf=0.4, imgsz=640, stream=True, verbose=False)
    
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("RPi 5 - YOLO11", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
