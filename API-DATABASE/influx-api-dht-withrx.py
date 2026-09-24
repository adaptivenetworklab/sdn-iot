from flask import Flask, request, jsonify
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime

app = Flask(__name__)

# --- KONFIGURASI INFLUXDB ---
# Pastikan URL, Token, dan Org sesuai
client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/sensor', methods=['POST'])
def receive_sensor():
    data = request.json
    
    # Ambil tipe pesan kalau ada (dikirim oleh Ryu yang baru)
    msg_type = data.get('type', 'unknown')
    
    try:
        # ======================================================
        # 1. CEK DATA TRAFFIC / THROUGHPUT (DARI RYU) - [BARU]
        # ======================================================
        if msg_type == 'traffic_stats' or ('rx_bytes' in data and 'tx_bytes' in data):
            print(f"📥 Menerima Data Traffic: {data}")
            
            point = Point("network_traffic") \
                .tag("dpid", str(data.get("dpid", "unknown"))) \
                .tag("port", str(data.get("port", "unknown"))) \
                .field("rx_bytes", int(data["rx_bytes"])) \
                .field("tx_bytes", int(data["tx_bytes"]))
            
            # PENTING: Pastikan kamu punya bucket bernama "monitoring" di InfluxDB
            # Atau ganti jadi "dht11" kalau mau digabung
            write_api.write(bucket="monitoring", org="sdn", record=point)
            
            return jsonify({"status": "OK (Traffic)"}), 200

        # ======================================================
        # 2. CEK DATA SENSOR DHT11
        # ======================================================
        elif "temperature" in data and "humidity" in data:
            print(f"📥 Menerima Data DHT11: {data}")
            
            point = Point("iotDHT11_data") \
                .tag("device", "dht11") \
                .field("temperature", int(data["temperature"])) \
                .field("humidity", int(data["humidity"]))
            
            write_api.write(bucket="dht11", org="sdn", record=point)
            return jsonify({"status": "OK (DHT)"}), 200

        # ======================================================
        # 3. CEK DATA HEART RATE (MAX30102)
        # ======================================================
        elif "heart_rate" in data and "spo2" in data:
            print(f"📥 Menerima Data Jantung: {data}")
            
            point = Point("iotHeartRate_data") \
                .tag("device", "max30102") \
                .field("heart_rate", float(data["heart_rate"])) \
                .field("spo2", float(data["spo2"]))
            
            write_api.write(bucket="max", org="sdn", record=point)
            return jsonify({"status": "OK (HeartRate)"}), 200
        
        # ======================================================
        # 4. DATA TIDAK DIKENALI
        # ======================================================
        else:
            print(f"⚠️ Warning: Unrecognized data format: {data}")
            return jsonify({"error": "Unrecognized data format"}), 400
            
    except KeyError as e:
        print(f"❌ Error: Missing key {e} in data: {data}")
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        print(f"❌ Error: Internal server error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Host 0.0.0.0 Wajib biar bisa ditembak dari luar (Ryu Container)
    app.run(host="0.0.0.0", port=5000)
