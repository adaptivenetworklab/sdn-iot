from flask import Flask, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime # Ditambahkan untuk parsing timestamp

app = Flask(__name__)

# --- Konfigurasi InfluxDB ---
client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)
INFLUX_BUCKET = "max" # Definisikan bucket di satu tempat
INFLUX_CAM= "camera"
# --- Endpoint 1: Sensor Detak Jantung (dari script Asli) ---
@app.route('/sensor-max', methods=['POST'])
def receive_heart_rate_sensor():
    data = request.json
    
    try:
        point = Point("iotHeartRate_data") \
            .field("heart_rate", data["heart_rate"]) \
            .field("spo2", data["spo2"])
        
        write_api.write(bucket=INFLUX_BUCKET, org="sdn", record=point)
        
        return "OK (Heart Rate)"
    except KeyError as e:
        return f"Missing key in JSON: {e}", 400
    except Exception as e:
        return f"Internal server error: {e}", 500

# --- Endpoint 2: Data Kamera (BARU) ---
@app.route('/camera-data', methods=['POST'])
def receive_camera_data():
    data = request.json
    
    try:
        # 1. Ambil data metrik (jumlah orang)
        if "person" not in data:
            return "Missing key in JSON: 'person'", 400
            
        person_count = int(data["person"])
        
        # 2. Ambil timestamp dari data
        if "timestamp" not in data:
             return "Missing key in JSON: 'timestamp'", 400

        timestamp_str = data["timestamp"]
        # Konversi string timestamp ke datetime object agar presisi
        timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")

        # 3. Buat Point untuk InfluxDB
        # PENTING: Kita HANYA menyimpan metrik (person_count).
        # Field "image" (base64) sengaja DIABAIKAN.
        # Menyimpan image di InfluxDB akan merusak performa database.
        point = Point("iotCamera_data") \
            .field("person_count", person_count) \
            .time(timestamp_dt) # Menggunakan timestamp presisi dari kamera

        # 4. Tulis ke bucket
        write_api.write(bucket=INFLUX_CAM, org="sdn", record=point)
        
        # Beri tahu jika image diterima tapi diabaikan
        if "image" in data:
            return "OK (Camera Data: Metric Saved, Image Ignored)"
        else:
            return "OK (Camera Data: Metric Saved)"
    
    except KeyError as e:
        return f"Missing key in JSON: {e}", 400
    except ValueError as e:
        # Error jika format 'person' atau 'timestamp' salah
        return f"Invalid data format (e.g., timestamp): {e}", 400
    except Exception as e:
        return f"Internal server error: {e}", 500

# --- Menjalankan Server ---
if __name__ == '__main__':
    # Port 5001 sama seperti script asli Anda
    # debug=True akan auto-restart server jika Anda mengubah script ini
    app.run(host="0.0.0.0", port=5001, debug=True)
