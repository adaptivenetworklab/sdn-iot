# FILE: server_influx.py
from flask import Flask, request, jsonify
import base64
import os
import logging
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# --- KONFIGURASI ---
UPLOAD_FOLDER = "/home/database/images"
INFLUX_URL = "http://192.168.111.129:8086/"
INFLUX_TOKEN = "aSdE_g3CN73iUMcvQ4m70FDy3PKnehtyMrYtd14nhAQ6FUprgurglvRi7faXCKvpHVMM8QFd18Uze-rJRkkF1g=="
INFLUX_ORG = "sdn"
INFLUX_BUCKET = "camera"

# Pastikan folder ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Setup Logging agar terlihat di terminal
logging.basicConfig(level=logging.INFO)

# InfluxDB Client Setup
client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

app = Flask(__name__)

@app.route("/upload-json", methods=["POST"])
def upload_json():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400

        timestamp = data.get("timestamp")
        camera_id = data.get("camera_id")
        person_count = data.get("person_count")
        image_b64 = data.get("image_base64") # Bisa jadi None jika Raspi tidak mengirim gambar

        if timestamp is None or person_count is None:
            return jsonify({"status": "error", "message": "Missing timestamp or person_count"}), 400

        saved_filename = None

        # 1. PROSES GAMBAR (Hanya jika ada data gambar)
        if image_b64:
            try:
                # Ganti karakter timestamp agar valid jadi nama file
                safe_time = timestamp.replace(":", "-").replace(".", "-")
                image_name = f"{safe_time}_{camera_id}.jpg"
                image_path = os.path.join(UPLOAD_FOLDER, image_name)

                # Decode dan simpan
                image_data = base64.b64decode(image_b64)
                with open(image_path, "wb") as f:
                    f.write(image_data)
                
                saved_filename = image_name
                logging.info(f"Gambar disimpan: {image_name}")
            except Exception as img_err:
                logging.error(f"Gagal menyimpan gambar: {img_err}")

        # 2. PROSES INFLUXDB (Selalu dijalankan)
        point = Point("person_detection") \
            .tag("camera_id", camera_id) \
            .field("person_count", int(person_count)) \
            .time(timestamp) # Pastikan format waktu sesuai (ISO 8601 disarankan)

        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        logging.info(f"Data InfluxDB masuk: Cam={camera_id}, Count={person_count}")

        return jsonify({
            "status": "ok", 
            "image_saved": saved_filename if saved_filename else "skipped"
        }), 200

    except Exception as e:
        logging.error(f"Error Processing Request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Host 0.0.0.0 agar bisa diakses dari luar (dari Raspi)
    app.run(host="0.0.0.0", port=5003, debug=False)
