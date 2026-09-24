from flask import Flask, request, jsonify
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import datetime

app = Flask(__name__)

# --- KONFIGURASI INFLUXDB ---
client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

def calculate_dual_latency(data):
    """Hitung Latency E2E dan Server"""
    if data.get('type') != 'sensor_data': return 0.0, 0.0

    arrival_time = time.time()
    sensor_ts = data.get("timestamp")      
    ryu_ts = data.get("ryu_timestamp")     
    
    lat_e2e = 0.0
    lat_server = 0.0
    
    if sensor_ts is not None:
        try:
            lat_e2e = (arrival_time - float(sensor_ts)) * 1000
        except ValueError: pass

    if ryu_ts is not None:
        try:
            lat_server = (arrival_time - float(ryu_ts)) * 1000
        except ValueError: pass
            
    print(f"\n--- ⏱️ DEBUG LATENCY (MAX) ---")
    print(f"Arrival: {datetime.datetime.fromtimestamp(arrival_time)}")
    if sensor_ts: print(f"E2E    : {lat_e2e:.2f} ms")
    if ryu_ts:    print(f"Server : {lat_server:.2f} ms")
    print(f"------------------------------\n")
    
    return lat_e2e, lat_server

@app.route('/sensor-max', methods=['POST'])
def receive_data():
    data = request.json
    msg_type = data.get('type', 'unknown')
    
    latency_e2e, latency_server = calculate_dual_latency(data)

    try:
        # 1. TRAFFIC STATS
        if msg_type == 'traffic_stats' or ('rx_bytes' in data and 'tx_bytes' in data):
            point = Point("network_traffic") \
                .tag("dpid", str(data.get("dpid", "unknown"))) \
                .tag("port", str(data.get("port", "unknown"))) \
                .field("rx_bytes", int(data.get("rx_bytes", 0))) \
                .field("tx_bytes", int(data.get("tx_bytes", 0)))
            write_api.write(bucket="monitoring", org="sdn", record=point)
            return jsonify({"status": "OK"}), 200

        # 2. SENSOR MAX30102 (Target Utama)
        elif ("HeartRate" in data or "heart_rate" in data):
            hr = data.get("HeartRate") 
            if hr is None: hr = data.get("heart_rate")

            spo2 = data.get("SpO2") 
            if spo2 is None: spo2 = data.get("spo2")

            if hr is not None and spo2 is not None:
                point = Point("iotHeartRate_data") \
                    .tag("device", "max30102") \
                    .field("heart_rate", float(hr)) \
                    .field("spo2", float(spo2)) \
                    .field("latency_e2e_ms", float(latency_e2e)) \
                    .field("latency_server_ms", float(latency_server))
                
                write_api.write(bucket="max", org="sdn", record=point)
                return jsonify({"status": "OK"}), 200
            else:
                return jsonify({"error": "HeartRate values are None"}), 400

        # 3. REJECT DHT DATA (Salah Kamar)
        elif ("Temperature" in data or "temperature" in data):
            print("⚠️ WARNING: Data DHT masuk ke Port 5001! Ditolak.")
            return jsonify({"error": "Wrong Port. Use 5000 for Temperature"}), 400

        else:
            return jsonify({"error": "Unrecognized data keys"}), 400
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    PORT = 5001 
    print(f"⇨ MAX30102 API Running on Port {PORT}...")
    app.run(host="0.0.0.0", port=PORT, debug=False)
