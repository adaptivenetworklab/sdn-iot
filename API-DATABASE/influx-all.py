from flask import Flask, request, jsonify
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

app = Flask(__name__)

# --- KONFIGURASI INFLUXDB ---
# Pastikan URL, Token, dan Org sesuai dengan InfluxDB Anda
client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/sensor', methods=['POST'])
@app.route('/sensor-max', methods=['POST']) # Handle kedua endpoint url
def receive_data():
    data = request.json
    msg_type = data.get('type', 'unknown')
    
    # Uncomment untuk debug incoming data
    # print(f"DEBUG: {data}")

    try:
        # ======================================================
        # 1. TRAFFIC STATS (RX/TX Monitoring)
        # ======================================================
        # Kriteria: Tipe 'traffic_stats' ATAU ada key rx_bytes/tx_bytes
        if msg_type == 'traffic_stats' or ('rx_bytes' in data and 'tx_bytes' in data):
            point = Point("network_traffic") \
                .tag("dpid", str(data.get("dpid", "unknown"))) \
                .tag("port", str(data.get("port", "unknown"))) \
                .field("rx_bytes", int(data.get("rx_bytes", 0))) \
                .field("tx_bytes", int(data.get("tx_bytes", 0)))
            
            # Masuk ke bucket 'monitoring' (Pastikan bucket ini ADA)
            write_api.write(bucket="monitoring", org="sdn", record=point)
            return jsonify({"status": "OK (Traffic)"}), 200

        # ======================================================
        # 2. SENSOR DHT11 (Suhu & Kelembaban)
        # ======================================================
        # Logic: Case Insensitive & Zero Value Safe
        elif ("Temperature" in data or "temperature" in data):
            # Prioritas key huruf Besar, fallback ke huruf kecil
            temp = data.get("Temperature") 
            if temp is None: temp = data.get("temperature")

            hum = data.get("Humidity") 
            if hum is None: hum = data.get("humidity")
            
            # Pastikan data tidak None (Angka 0 tetap diterima)
            if temp is not None and hum is not None:
                point = Point("iotDHT11_data") \
                    .tag("device", "dht11") \
                    .field("temperature", float(temp)) \
                    .field("humidity", float(hum))
                
                write_api.write(bucket="dht11", org="sdn", record=point)
                return jsonify({"status": "OK (DHT)"}), 200
            else:
                return jsonify({"error": "DHT values are None"}), 400

        # ======================================================
        # 3. SENSOR MAX30102 (Jantung & SpO2)
        # ======================================================
        # Logic: Case Insensitive & Zero Value Safe
        elif ("HeartRate" in data or "heart_rate" in data):
            hr = data.get("HeartRate")
            if hr is None: hr = data.get("heart_rate")

            spo2 = data.get("SpO2")
            if spo2 is None: spo2 = data.get("spo2")

            if hr is not None and spo2 is not None:
                point = Point("iotHeartRate_data") \
                    .tag("device", "max30102") \
                    .field("heart_rate", float(hr)) \
                    .field("spo2", float(spo2))
                
                write_api.write(bucket="max", org="sdn", record=point)
                return jsonify({"status": "OK (HeartRate)"}), 200
            else:
                return jsonify({"error": "HeartRate values are None"}), 400

        # ======================================================
        # 4. ERROR HANDLER (Data Sampah)
        # ======================================================
        else:
            print(f"⚠️ Warning: Unrecognized data format: {data}")
            return jsonify({"error": "Unrecognized data keys"}), 400
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # GANTI PORT DISINI SESUAI KEBUTUHAN (5000 atau 5001)
    # 5000: Standar untuk DHT
    # 5001: Standar untuk MAX (sesuai config Ryu Anda)
    PORT = 5000
    print(f"⇨ SDN-IoT API Running on Port {PORT}...")
    app.run(host="0.0.0.0", port=PORT, debug=False)
