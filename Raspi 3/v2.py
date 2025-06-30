# SEND TO INFLUX VIA REST API
# This script captures video from a Raspberry Pi camera, detects persons using YOLOv8,
import subprocess, numpy as np, cv2, time, base64, requests
from ultralytics import YOLO
from datetime import datetime

WIDTH, HEIGHT, FPS = 640, 480, 15
MODEL_PATH = "yolo11n.pt"
SEND_INTERVAL = 5  # seconds
DESTINATION_URL = "http://10.0.1.148:5002/upload-json"

cmd = [
    "libcamera-vid", "-t", "0",
    "--width", str(WIDTH), "--height", str(HEIGHT),
    "--framerate", str(FPS), "--codec", "yuv420",
    "--vflip", "--nopreview", "-o", "-"
]

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=10**8)
model = YOLO(MODEL_PATH)
frame_size = int(WIDTH * HEIGHT * 1.5)
last_sent = time.time() - SEND_INTERVAL

while True:
    raw_data = process.stdout.read(frame_size)
    if len(raw_data) != frame_size:
        continue

    yuv = np.frombuffer(raw_data, dtype=np.uint8).reshape((int(HEIGHT * 1.5), WIDTH))
    bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

    results = model.predict(source=bgr, imgsz=WIDTH, conf=0.4, verbose=False)
    result = results[0]

    person_count = 0
    for box in result.boxes:
        cls_id = int(box.cls[0])
        if model.names[cls_id] == "person":
            person_count += 1

    if time.time() - last_sent >= SEND_INTERVAL:
        _, jpeg = cv2.imencode(".jpg", bgr)
        img_b64 = base64.b64encode(jpeg.tobytes()).decode()
        ts = datetime.utcnow().isoformat()
        payload = {
            "timestamp": ts,
            "person_count": person_count,
            "camera_id": "raspi3-a",
            "image_name": f"frame_{ts.replace(':', '-')}.jpg",
            "image_base64": img_b64
        }
        try:
            res = requests.post(DESTINATION_URL, json=payload)
            print(f"Sent data: {person_count} person(s) at {ts}")
        except Exception as e:
            print("Error sending data:", e)
        last_sent = time.time()