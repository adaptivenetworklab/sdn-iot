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
    
    # DEBUG: Print data mentah biar kelihatan apa yang masuk
    print(f"DEBUG PAYLOAD: {data}")

    try:
        # --- PERBAIKAN LOGIKA DI SINI ---
        
        # 1. Cek DHT11 (Handle Huruf Besar 'Temperature' DAN Kecil 'temperature')
        if ("Temperature" in data or "temperature" in data) and \
           ("Humidity" in data or "humidity" in data):
            
            # Ambil nilainya (Prioritas Huruf Besar, Fallback ke Huruf Kecil)
            temp_val = data.get("Temperature") or data.get("temperature")
            hum_val = data.get("Humidity") or data.get("humidity")

            # Pastikan format angka (Float)
            point = Point("iotDHT11_data") \
                .field("temperature", float(temp_val)) \
                .field("humidity", float(hum_val))
            
            write_api.write(bucket="dht11", org="sdn", record=point)
            print("SUCCESS: Data DHT11 Written to DB")
            return "OK (DHT)"

        # 2. Cek Heart Rate (Handle Huruf Besar DAN Kecil)
        elif ("HeartRate" in data or "heart_rate" in data) and \
             ("SpO2" in data or "spo2" in data):
            
            hr_val = data.get("HeartRate") or data.get("heart_rate")
            spo2_val = data.get("SpO2") or data.get("spo2")

            # Pastikan HeartRate adalah Integer/Float agar Influx senang
            point = Point("iotHeartRate_data") \
                .field("heart_rate", float(hr_val)) \
                .field("spo2", float(spo2_val))
            
            write_api.write(bucket="max", org="sdn", record=point)
            print("SUCCESS: Data MAX Written to DB")
            return "OK (HeartRate)"
        
        # 3. Handle Traffic Stats (Biar log ngga kotor)
        elif data.get("type") == "traffic_stats":
            return "Ignored (Traffic Stats)"

        else:
            print(f"WARNING: Unrecognized Keys in: {data.keys()}")
            return "Error: Unrecognized data keys", 400
            
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return f"Internal server error: {e}", 500

app.run(host="0.0.0.0", port=5000)
