from flask import Flask, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

client = InfluxDBClient(
    url="http://10.0.1.148:8086/",
    token="Sesuaikan dengan token kalian",
    org="Sesuaikan juga"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/sensor', methods=['POST'])
def receive_sensor():
    data = request.json
    point = Point("iotDHT11_data").field("temperature", data["temperature"]).field("humidity", data["humidity"])
    write_api.write(bucket="DHT11", org="test1", record=point)
    return "ok"

app.run(host="0.0.0.0", port=5000)
