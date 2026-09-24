from flask import Flask, request, jsonify
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# =========================
# InfluxDB Client Setup
# =========================
client = InfluxDBClient(
    url="http://192.168.111.129:8086/",
    token="aSdE_g3CN73iUMcvQ4m70FDy3PKnehtyMrYtd14nhAQ6FUprgurglvRi7faXCKvpHVMM8QFd18Uze-rJRkkF1g==",
    org="sdn"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

# =========================
# Flask Setup
# =========================
app = Flask(__name__)

@app.route("/camera", methods=["POST"])
def camera_metadata():
    data = request.get_json()

    try:
        # validasi minimal field
        required = ["timestamp", "camera_id", "person_count", "image_name", "image_hash"]
        for k in required:
            if k not in data:
                return jsonify({"status": "error", "message": f"Missing field: {k}"}), 400

        # Create Influx point
        point = (
            Point("camera_detection")
            .tag("camera_id", data["camera_id"])
            .field("person_count", int(data["person_count"]))
            .field("image_name", str(data["image_name"]))
            .field("image_hash", str(data["image_hash"]))
            .time(data["timestamp"])
        )

        write_api.write(bucket="camera", org="sdn", record=point)

        return jsonify({"status": "ok", "saved": True})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
