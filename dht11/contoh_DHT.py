#!/bin/python3
import time
import socket
import json

device0 = "/sys/bus/iio/devices/iio:device0"

# konfigurasi UDP
OVS_IP = "10.0.0.210"
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

try:
    while True:
        Flag, Temperature = readFirstLine(device0 + "/in_temp_input")
        temperature_val = Temperature // 1000 if Flag else None

        Flag, Humidity = readFirstLine(device0 + "/in_humidityrelative_input")
        humidity_val = Humidity // 1000 if Flag else None

        # Buat pesan JSON
        message = json.dumps({
            "temperature": temperature_val,
            "humidity": humidity_val
        })

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