# OPEN CONNECTION TO INFLUXDB AND UPLOAD IMAGES
# this script sets up a Flask server that receives JSON data containing person detection results and image data, saves the images, and writes the data to an InfluxDB instance.
from flask import Flask, request, jsonify
import base64, os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

UPLOAD_FOLDER = "/home/database/images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# InfluxDB Client Setup
client = InfluxDBClient(
    url="http://192.168.111.129:8086/",
    token="aSdE_g3CN73iUMcvQ4m70FDy3PKnehtyMrYtd14nhAQ6FUprgurglvRi7faXCKvpHVMM8QFd18Uze-rJRkkF1g==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Flask Setup
app = Flask(__name__)

@app.route("/upload-json", methods=["POST"])
def upload_json():
    data = request.get_json()
    try:
        # Extract data from JSON
        image_name = data["timestamp"] + ".jpg"  # Save image with timestamp name
        image_data = base64.b64decode(data["image_base64"])  # Decode base64 image data
        image_path = os.path.join(UPLOAD_FOLDER, image_name)

        # Save the image to the server
        with open(image_path, "wb") as f:
            f.write(image_data)

        # Create a point to be written to InfluxDB
        point = Point("person_detection") \
            .field("person_count", int(data["person_count"])) \
            .tag("camera_id", data["camera_id"]) \
            .time(data["timestamp"])

        # Write data to InfluxDB
        write_api.write(bucket="camera", org="sdn", record=point)

        # Return success response
        return jsonify({"status": "ok", "image_saved": image_name})

    except Exception as e:
        # Handle any error that occurs
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
