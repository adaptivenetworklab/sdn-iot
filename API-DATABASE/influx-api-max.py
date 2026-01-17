from flask import Flask, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

# Pastikan URL InfluxDB benar (localhost atau IP container jika di docker)
client = InfluxDBClient(
    url="http://192.168.10.58:8086/",
    token="FCYeKuOB9_KN4QAjinRl9YJuJhkmqrs-Aav3ImscqAjLOyVKYTi2nj_HhHkiUFfRUMzvGecWwA_1eMNoVmH1RQ==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/sensor-max', methods=['POST'])
def receive_heart_rate_sensor():
    data = request.json
    
    # DEBUG: Print data yang masuk ke terminal server untuk verifikasi
    print(f"DEBUG RECEIVED DATA: {data}") 

    try:
        # PERBAIKAN DI SINI: Sesuaikan key dengan JSON Client ('HeartRate' & 'SpO2')
        hr_val = data.get("HeartRate") 
        spo2_val = data.get("SpO2")

        # Validasi sederhana: Jika data kosong/None
        if hr_val is None or spo2_val is None:
             return "Missing 'HeartRate' or 'SpO2' keys", 400

        point = Point("iotHeartRate_data") \
            .field("heart_rate", float(hr_val)) \
            .field("spo2", float(spo2_val))
        
        write_api.write(bucket="max", org="sdn", record=point)
        
        return "OK (Heart Rate)"

    except Exception as e:
        print(f"ERROR: {e}") # Print error ke terminal server
        return f"Internal server error: {e}", 500

if __name__ == '__main__':
    # Debug=True agar kalau error kelihatan detailnya, tapi matikan saat production
    app.run(host="0.0.0.0", port=5001, debug=True)
