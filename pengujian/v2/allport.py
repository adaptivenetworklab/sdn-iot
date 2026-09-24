#!/usr/bin/python3
import socket
import time
import random
import json
import hashlib
import os
from datetime import datetime, timezone
import threading

# Global event to signal threads to stop
stop_event = threading.Event()

# --- Shared Helper Functions ---
def get_image_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return "nofile"

def make_random_string(n):
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(n))

def readFirstLine(filename):
    try:
        with open(filename, "rt") as f:
            value = int(f.readline())
            return True, value
    except (ValueError, OSError):
        return False, 0

def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

# --- Thread Functions ---

def run_camera():
    DEST_IP = "192.168.15.239"   # IP OVS listener
    DEST_PORT = 9999
    DEVICE_ID = "camera"         # port 2
    DEVICE_TYPE = "camera"
    IMAGE_PATH = "/home/sdn/Gambar/test.png"
    MIN_PAYLOAD_BYTES = 500
    MAX_PAYLOAD_BYTES = 1500

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    seq = 0

    print("[INFO] Camera sender thread started")

    while not stop_event.is_set():
        seq += 1
        send_ts = time.time()
        dummy_size = random.randint(MIN_PAYLOAD_BYTES, MAX_PAYLOAD_BYTES)

        payload = {
            "device_id": DEVICE_ID,
            "type": DEVICE_TYPE,
            "seq": seq,
            "send_ts": send_ts,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "person_count": random.randint(1, 10),
            "image_name": os.path.basename(IMAGE_PATH),
            "image_hash": get_image_hash(IMAGE_PATH),
            "dummy_size": dummy_size,
            "dummy_payload": make_random_string(dummy_size)
        }

        # Encode twice to include payload_bytes in the message
        try:
            raw = json.dumps(payload).encode()
            payload["payload_bytes"] = len(raw)
            raw = json.dumps(payload).encode()
        except Exception as e:
            print(f"[CAMERA] [ERROR] JSON encode failed: {e}")
            time.sleep(1)
            continue

        t0 = time.time()
        try:
            sock.sendto(raw, (DEST_IP, DEST_PORT))
            print(f"[CAMERA] [SENT] seq={seq} bytes={len(raw)}")
        except Exception as e:
            print(f"[CAMERA] [ERROR] UDP send failed: {e}")
            time.sleep(1)
            continue

        try:
            ack_data, _ = sock.recvfrom(4096)
            t1 = time.time()
            ack = json.loads(ack_data.decode(errors="ignore"))
            if ack.get("type") == "ack" and ack.get("seq") == seq:
                rtt_ms = (t1 - t0) * 1000
                print(f"   [CAMERA] [ACK] seq={seq} RTT={rtt_ms:.3f} ms")
            else:
                print("   [CAMERA] [WARN] ACK mismatch")
        except socket.timeout:
            print("   [CAMERA] [WARN] ACK timeout")
        except Exception as e:
            print(f"   [CAMERA] [WARN] ACK error: {e}")

        time.sleep(1)
    
    sock.close()
    print("[INFO] Camera thread stopped")

def run_dht():
    OVS_IP = "192.168.15.238"
    OVS_PORT = 9999
    DEVICE_ID = "dht11"
    DEVICE_TYPE = "sensor"
    device0 = "/sys/bus/iio/devices/iio:device0"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    seq = 0
    current_send_delay = 1

    print(f"[INFO] DHT11 thread started -> {OVS_IP}:{OVS_PORT}")

    while not stop_event.is_set():
        FlagT, RawTemp = readFirstLine(device0 + "/in_temp_input")
        temp_val = (RawTemp // 1000) if FlagT else 0
        FlagH, RawHum = readFirstLine(device0 + "/in_humidityrelative_input")
        hum_val = (RawHum // 1000) if FlagH else 0

        seq += 1
        payload = {
            "device_id": DEVICE_ID,
            "type": DEVICE_TYPE,
            "seq": seq,
            "send_ts": time.time(),
            "Temperature": int(temp_val),
            "Humidity": int(hum_val),
        }

        try:
            message_bytes = json.dumps(payload).encode()
            payload["payload_bytes"] = len(message_bytes)
            message_bytes = json.dumps(payload).encode()
        except Exception as e:
            print(f"[DHT] [ERROR] JSON encode failed: {e}")
            time.sleep(current_send_delay)
            continue

        t0 = time.time()
        try:
            sock.sendto(message_bytes, (OVS_IP, OVS_PORT))
            print(f"[{time.strftime('%H:%M:%S')}] [DHT] SENT seq={seq}")
        except Exception as e:
            print(f"[DHT] [ERROR] UDP send failed: {e}")
            time.sleep(current_send_delay)
            continue

        try:
            ack_data, _ = sock.recvfrom(4096)
            t1 = time.time()
            ack = json.loads(ack_data.decode(errors="ignore"))
            if ack.get("type") == "ack" and ack.get("seq") == seq:
                rtt_ms = (t1 - t0) * 1000
                print(f"   [DHT] [ACK] seq={seq} RTT={rtt_ms:.3f} ms")
            else:
                print("   [DHT] [WARN] ACK mismatch")
        except socket.timeout:
            print("   [DHT] [WARN] ACK timeout")
        except Exception as e:
            print(f"   [DHT] [WARN] ACK error: {e}")

        time.sleep(current_send_delay)
    
    sock.close()
    print("[INFO] DHT thread stopped")

def run_max():
    OVS_IP = "192.168.15.240"
    OVS_PORT = 9999
    DEVICE_ID = "max"
    DEVICE_TYPE = "sensor"
    BPM_MIN, BPM_MAX = 67, 75
    SPO2_MIN, SPO2_MAX = 95, 100
    STATE_UPDATE_INTERVAL = 5
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    
    current_bpm = random.randint(BPM_MIN, BPM_MAX)
    current_spo2 = random.randint(SPO2_MIN, SPO2_MAX)
    current_send_delay = 1
    last_state_update = time.time()
    seq = 0

    print(f"[INFO] MAX simulator thread started -> {OVS_IP}:{OVS_PORT}")

    while not stop_event.is_set():
        now = time.time()
        if now - last_state_update >= STATE_UPDATE_INTERVAL:
            bpm_change = random.randint(-2, 2)
            spo2_change = random.randint(-1, 1)
            current_bpm = clamp(current_bpm + bpm_change, BPM_MIN, BPM_MAX)
            current_spo2 = clamp(current_spo2 + spo2_change, SPO2_MIN, SPO2_MAX)
            last_state_update = now
            print(f"[MAX] [SENSOR UPDATE] BPM={current_bpm} | SpO2={current_spo2}%")

        seq += 1
        payload = {
            "device_id": DEVICE_ID,
            "type": DEVICE_TYPE,
            "seq": seq,
            "send_ts": time.time(),
            "HeartRate": int(current_bpm),
            "SpO2": float(current_spo2),
        }

        try:
            msg_bytes = json.dumps(payload).encode()
            payload["payload_bytes"] = len(msg_bytes)
            msg_bytes = json.dumps(payload).encode()
        except Exception as e:
            print(f"[MAX] [ERROR] JSON encode failed: {e}")
            time.sleep(current_send_delay)
            continue

        t0 = time.time()
        try:
            sock.sendto(msg_bytes, (OVS_IP, OVS_PORT))
            print(f"[{time.strftime('%H:%M:%S')}] [MAX] SENT seq={seq}")
        except Exception as e:
            print(f"[MAX] [ERROR] UDP send failed: {e}")
            time.sleep(current_send_delay)
            continue

        try:
            ack_data, _ = sock.recvfrom(4096)
            t1 = time.time()
            ack = json.loads(ack_data.decode(errors="ignore"))
            if ack.get("type") == "ack" and ack.get("seq") == seq:
                rtt_ms = (t1 - t0) * 1000
                print(f"   [MAX] [ACK] seq={seq} RTT={rtt_ms:.3f} ms")
            else:
                print("   [MAX] [WARN] ACK mismatch")
        except socket.timeout:
            print("   [MAX] [WARN] ACK timeout")
        except Exception as e:
            print(f"   [MAX] [WARN] ACK error: {e}")

        time.sleep(current_send_delay)
    
    sock.close()
    print("[INFO] MAX thread stopped")

# --- Main Execution ---
if __name__ == "__main__":
    t1 = threading.Thread(target=run_camera, daemon=True)
    t2 = threading.Thread(target=run_dht, daemon=True)
    t3 = threading.Thread(target=run_max, daemon=True)

    t1.start()
    t2.start()
    t3.start()

    print("[INFO] All threads started. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping all threads...")
        stop_event.set()
        t1.join()
        t2.join()
        t3.join()
        print("[INFO] All done.")
