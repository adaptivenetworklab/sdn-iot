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
            
    print(f"\n--- ⏱️ DEBUG LATENCY (DHT) ---")
    print(f"Arrival: {datetime.datetime.fromtimestamp(arrival_time)}")
    if sensor_ts: print(f">> E2E    : {lat_e2e:.2f} ms")
    if ryu_ts:    print(f">> Server : {lat_server:.2f} ms")
    print(f"------------------------------\n")
    
    return lat_e2e, lat_server

@app.route('/sensor', methods=['POST'])
def receive_data():
    data = request.json
    msg_type = data.get('type', 'unknown')
    
    latency_e2e, latency_server = calculate_dual_latency(data)

    try:
        # 1. TRAFFIC STATS (Tetap diterima untuk monitoring)
        if msg_type == 'traffic_stats' or ('rx_bytes' in data and 'tx_bytes' in data):
            point = Point("network_traffic") \
                .tag("dpid", str(data.get("dpid", "unknown"))) \
                .tag("port", str(data.get("port", "unknown"))) \
                .field("rx_bytes", int(data.get("rx_bytes", 0))) \
                .field("tx_bytes", int(data.get("tx_bytes", 0)))
            write_api.write(bucket="monitoring", org="sdn", record=point)
            return jsonify({"status": "OK"}), 200

        # 2. SENSOR DHT11 (Target Utama)
        elif ("Temperature" in data or "temperature" in data):
            temp = data.get("Temperature") 
            if temp is None: temp = data.get("temperature")

            hum = data.get("Humidity") 
            if hum is None: hum = data.get("humidity")
            
            if temp is not None and hum is not None:
                point = Point("iotDHT11_data") \
                    .tag("device", "dht11") \
                    .field("temperature", float(temp)) \
                    .field("humidity", float(hum)) \
                    .field("latency_e2e_ms", float(latency_e2e)) \
                    .field("latency_server_ms", float(latency_server))
                
                write_api.write(bucket="dht11", org="sdn", record=point)
                return jsonify({"status": "OK"}), 200
            else:
                return jsonify({"error": "DHT values are None"}), 400

        # 3. REJECT MAX DATA (Salah Kamar)
        elif ("HeartRate" in data or "heart_rate" in data):
            print("⚠️ WARNING: Data Max masuk ke Port 5000! Ditolak.")
            return jsonify({"error": "Wrong Port. Use 5001 for HeartRate"}), 400

        else:
            return jsonify({"error": "Unrecognized data keys"}), 400
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    PORT = 5000
    print(f"⇨ DHT11 API Running on Port {PORT}...")
    app.run(host="0.0.0.0", port=PORT, debug=False)
