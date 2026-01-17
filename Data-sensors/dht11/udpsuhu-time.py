#!/bin/python3
import time
import socket
import json

device0 = "/sys/bus/iio/devices/iio:device0"

# KONFIGURASI UDP
# Pastikan IP ini mengarah ke OVS Interface yang benar
OVS_IP = "192.168.15.238" 
OVS_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def readFirstLine(filename):
    try:
        with open(filename, "rt") as f:
            value = int(f.readline())
            return True, value
    except ValueError:
        return False, -1
    except OSError:
        return False, 0

print(f"[INFO] Sensor DHT11 (QoS Mode) dimulai. Target: {OVS_IP}:{OVS_PORT}")

try:
    while True:
        # 1. Baca Data Fisik
        FlagT, RawTemp = readFirstLine(device0 + "/in_temp_input")
        temp_val = (RawTemp // 1000) if FlagT else 0

        FlagH, RawHum = readFirstLine(device0 + "/in_humidityrelative_input")
        hum_val = (RawHum // 1000) if FlagH else 0

        # 2. Buat Payload JSON dengan TIMESTAMP
        payload = {
            "Temperature": temp_val,
            "Humidity": hum_val,
            "timestamp": time.time() # <--- INI KUNCI QoS
        }

        # 3. Kirim via UDP
        message = json.dumps(payload)
        
        try:
            sock.sendto(message.encode(), (OVS_IP, OVS_PORT))
            print(f"[SENT] {message} --> {OVS_IP}:{OVS_PORT}")
        except Exception as e:
            print(f"[ERROR] Gagal kirim: {e}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n[INFO] Stop.")
finally:
    sock.close()
