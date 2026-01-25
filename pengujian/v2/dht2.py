#!/usr/bin/python3
import time
import socket
import json
import random

# --- KONFIGURASI SENSOR FISIK ---
device0 = "/sys/bus/iio/devices/iio:device0"

# --- KONFIGURASI JARINGAN ---
OVS_IP = "192.168.15.238"   # IP listener di OVS
OVS_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)  # timeout nunggu ACK (biar ga nge-freeze)

# --- ID DEVICE (buat mapping delay per port/device) ---
DEVICE_ID = "dht11"         # port 1
DEVICE_TYPE = "sensor"

# --- KONFIGURASI INTERVAL ---
CONFIG_UPDATE_INTERVAL = 600  # random delay tiap 10 menit

# --- INISIALISASI ---
seq = 0
current_send_delay = 1
last_config_update = time.time()

def readFirstLine(filename):
    try:
        with open(filename, "rt") as f:
            value = int(f.readline())
            return True, value
    except (ValueError, OSError):
        return False, 0

print(f"[INFO] DHT11 started -> {OVS_IP}:{OVS_PORT}")
print(f"[INFO] Current send delay: {current_send_delay}s")
print("[INFO] RTT mode: waiting ACK from OVS listener...\n")

try:
    while True:
        now = time.time()



        # baca sensor fisik
        FlagT, RawTemp = readFirstLine(device0 + "/in_temp_input")
        temp_val = (RawTemp // 1000) if FlagT else 0

        FlagH, RawHum = readFirstLine(device0 + "/in_humidityrelative_input")
        hum_val = (RawHum // 1000) if FlagH else 0

        seq += 1

        # payload utama
        payload = {
            "device_id": DEVICE_ID,
            "type": DEVICE_TYPE,

            "seq": seq,
            "send_ts": time.time(),  # waktu kirim dari raspi (epoch)
            "Temperature": int(temp_val),
            "Humidity": int(hum_val),
        }

        # encode dulu untuk tau ukuran bytes
        message_bytes = json.dumps(payload).encode()
        payload["payload_bytes"] = len(message_bytes)

        # encode ulang supaya payload_bytes ikut terkirim
        message_bytes = json.dumps(payload).encode()

        # kirim packet
        t0 = time.time()
        try:
            sock.sendto(message_bytes, (OVS_IP, OVS_PORT))
            print(f"[{time.strftime('%H:%M:%S')}] SENT seq={seq} delay={current_send_delay}s payload={len(message_bytes)}B temp={temp_val} hum={hum_val}")
        except Exception as e:
            print(f"[ERROR] UDP send failed: {e}")
            time.sleep(current_send_delay)
            continue

        # tunggu ACK dari OVS untuk hitung RTT
        try:
            ack_data, _ = sock.recvfrom(4096)
            t1 = time.time()

            ack = json.loads(ack_data.decode(errors="ignore"))
            if ack.get("type") == "ack" and ack.get("seq") == seq:
                rtt_ms = (t1 - t0) * 1000
                print(f"   [ACK] seq={seq} RTT={rtt_ms:.3f} ms")
            else:
                print("   [WARN] ACK mismatch / unknown format")

        except socket.timeout:
            print("   [WARN] ACK timeout (packet received by OVS maybe lost / overload)")

        except Exception as e:
            print(f"   [WARN] ACK error: {e}")

        time.sleep(current_send_delay)

except KeyboardInterrupt:
    print("\n[INFO] DHT11 stopped.")
finally:
    sock.close()
