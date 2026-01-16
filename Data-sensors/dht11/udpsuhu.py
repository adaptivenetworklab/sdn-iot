#!/bin/python3
import time
import socket
import json  # Import wajib untuk JSON

device0 = "/sys/bus/iio/devices/iio:device0"

# konfigurasi UDP
OVS_IP = "192.168.15.238"
OVS_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# function to read first line and return integer
def readFirstLine(filename):
    try:
        with open(filename, "rt") as f:
            value = int(f.readline())
            return True, value
    except ValueError:
        return False, -1
    except OSError:
        return False, 0

print(f"[INFO] Sensor DHT11 (JSON Mode) dimulai. Target: {OVS_IP}:{OVS_PORT}")

try:
    while True:
        # 1. Baca Data Suhu
        FlagT, RawTemp = readFirstLine(device0 + "/in_temp_input")
        # Jika berhasil baca, bagi 1000. Jika gagal, kirim 0.
        temp_val = (RawTemp // 1000) if FlagT else 0

        # 2. Baca Data Kelembaban
        FlagH, RawHum = readFirstLine(device0 + "/in_humidityrelative_input")
        # Jika berhasil baca, bagi 1000. Jika gagal, kirim 0.
        hum_val = (RawHum // 1000) if FlagH else 0

        # 3. Format JSON Payload
        # Kita kirim raw number (integer), bukan string dengan "C" atau "%"
        payload = {
            "Temperature": temp_val,
            "Humidity": hum_val
        }

        # Konversi ke JSON String
        message = json.dumps(payload)
        
        try:
            sock.sendto(message.encode(), (OVS_IP, OVS_PORT))
            print(f"[SENT] {message} --> {OVS_IP}:{OVS_PORT}")
        except Exception as e:
            print(f"[ERROR] Gagal mengirim data: {e}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n[INFO] Dihentikan oleh pengguna.")
finally:
    sock.close()
    print("[INFO] Socket ditutup.")
