from flask import Flask, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Kamu harus menjalankan skrip yang ada logika ini
@app.route('/sensor', methods=['POST'])
def receive_sensor():
    data = request.json
    
    try:
        # --- Logika Pemilah ---
        # Cek apakah ini data DHT11?
        if "temperature" in data and "humidity" in data:
            # INI KODE YANG BENAR (TIDAK PAKAI '...')
            point = Point("iotDHT11_data") \
                .field("temperature", data["temperature"]) \
                .field("humidity", data["humidity"])
            
            # Tulis ke bucket dht11
            write_api.write(bucket="dht11", org="sdn", record=point)
            
            return "OK (DHT)"

        # Cek apakah ini data Heart Rate (MAX)?
        elif "heart_rate" in data and "spo2" in data:
            # INI KODE YANG BENAR (TIDAK PAKAI '...')
            point = Point("iotHeartRate_data") \
                .field("heart_rate", data["heart_rate"]) \
                .field("spo2", data["spo2"])
            
            # Tulis ke bucket max
            write_api.write(bucket="max", org="sdn", record=point)
            
            return "OK (HeartRate)"
        
        # Jika data tidak dikenali
        else:
            # Tambahkan logging agar tahu datanya apa
            print(f"Warning: Unrecognized data format received: {data}")
            return "Error: Unrecognized data format", 400
            
    except KeyError as e:
        print(f"Error: Missing key {e} in data: {data}")
        return f"Missing key in JSON: {e}", 400
    except Exception as e:
        print(f"Error: Internal server error: {e}")
        return f"Internal server error: {e}", 500

app.run(host="0.0.0.0", port=5000)
