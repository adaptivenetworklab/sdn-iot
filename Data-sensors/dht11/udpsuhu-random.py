#!/bin/python3
import time
import socket
import json
import random

# --- KONFIGURASI SENSOR FISIK ---
device0 = "/sys/bus/iio/devices/iio:device0"

# --- KONFIGURASI JARINGAN ---
OVS_IP = "192.168.15.238" 
OVS_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --- KONFIGURASI INTERVAL ---
CONFIG_UPDATE_INTERVAL = 600   # Update jeda setiap 10 menit (600 detik)

# --- INISIALISASI ---
current_send_delay = random.randint(1, 5) # Jeda awal 1-5 detik
last_config_update = time.time()

def readFirstLine(filename):
    try:
        with open(filename, "rt") as f:
            value = int(f.readline())
            return True, value
    except (ValueError, OSError):
        return False, 0

print(f"[INFO] Sensor DHT11 FISIK dimulai. Target: {OVS_IP}:{OVS_PORT}")
print(f"[INFO] Jeda pengiriman saat ini: {current_send_delay} detik")

try:
    while True:
        now = time.time()

        # 1. Cek apakah sudah 10 menit untuk merandom ulang interval
        if now - last_config_update >= CONFIG_UPDATE_INTERVAL:
            current_send_delay = random.randint(1, 5)
            last_config_update = now
            print(f"\n🔄 [CONFIG UPDATE] Interval baru untuk 10 menit ke depan: {current_send_delay}s\n")

        # 2. Baca Data Fisik dari Sensor
        FlagT, RawTemp = readFirstLine(device0 + "/in_temp_input")
        temp_val = (RawTemp // 1000) if FlagT else 0

        FlagH, RawHum = readFirstLine(device0 + "/in_humidityrelative_input")
        hum_val = (RawHum // 1000) if FlagH else 0

        # 3. Buat Payload JSON dengan TIMESTAMP
        payload = {
            "Temperature": temp_val,
            "Humidity": hum_val,
            "timestamp": now
        }

        # 4. Kirim via UDP
        message = json.dumps(payload)
        try:
            sock.sendto(message.encode(), (OVS_IP, OVS_PORT))
            print(f"[{time.strftime('%H:%M:%S')}] SENT | Delay: {current_send_delay}s | Data: {message}")
        except Exception as e:
            print(f"[ERROR] Gagal kirim: {e}")

        # 5. Jeda Pengiriman sesuai hasil random
        time.sleep(current_send_delay)

except KeyboardInterrupt:
    print("\n[INFO] Program dihentikan.")
finally:
    sock.close()
