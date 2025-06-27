# OPEN CONNECTION TO INFLUXDB AND UPLOAD IMAGES
# this script sets up a Flask server that receives JSON data containing person detection results and image data, saves the images, and writes the data to an InfluxDB instance.
from flask import Flask, request, jsonify
import base64, os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

UPLOAD_FOLDER = "/home/influxserver/images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

client = InfluxDBClient(
    url="http://10.0.1.148:8086/",
    token="tTTKg3UPewreNn6peUFnRXbMiQ4DgQAcTHF-XRnqIOQfaVsr5oRMkUSiSPqdtWO0bWIEwjBt846zFuLhErDQnw==",
    org="test1"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

app = Flask(__name__)

@app.route("/upload-json", methods=["POST"])
def upload_json():
    data = request.get_json()
    try:
        image_name = data["image_name"]
        image_data = base64.b64decode(data["image_base64"])
        image_path = os.path.join(UPLOAD_FOLDER, image_name)

        with open(image_path, "wb") as f:
            f.write(image_data)

        point = Point("person_detection") \
            .field("person_count", int(data["person_count"])) \
            .tag("camera_id", data["camera_id"]) \
            .tag("image", image_name) \
            .time(data["timestamp"])

        write_api.write(bucket="KAMERA", org="test1", record=point)
        return jsonify({"status": "ok", "image_saved": image_name})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
