import time
import random
import json
import socket

# --- KONFIGURASI JARINGAN (Sesuai Script Asli Anda) ---
OVS_IP = "192.168.15.240"
OVS_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --- KONFIGURASI LOGIKA DUMMY ---
# Rentang Nilai
BPM_MIN, BPM_MAX = 67, 75
SPO2_MIN, SPO2_MAX = 95, 100

# Interval Update
STATE_UPDATE_INTERVAL = 5   # Nilai sensor berubah tiap 5 detik
CONFIG_UPDATE_INTERVAL = 600 # Jeda pengiriman berubah tiap 1 menit

# --- INISIALISASI STATE AWAL ---
current_bpm = random.randint(BPM_MIN, BPM_MAX)
current_spo2 = random.randint(SPO2_MIN, SPO2_MAX)
current_send_delay = random.randint(1, 4)

last_state_update = 0
last_config_update = 0

def clamp(val, min_val, max_val):
    """Memastikan nilai tetap dalam rentang yang ditentukan"""
    return max(min_val, min(max_val, val))

print(f"🚀 Memulai Simulator Vital Signs (UDP)")
print(f"Target: {OVS_IP}:{OVS_PORT}")
print(f"Delay Awal: {current_send_delay}s\n")

try:
    while True:
        now = time.time()

        # 1. Update Parameter Pengiriman (Setiap 1 Menit)
        if now - last_config_update >= CONFIG_UPDATE_INTERVAL:
            current_send_delay = random.randint(1, 4)
            last_config_update = now
            print(f"🔄 [CONFIG UPDATE] Jeda pengiriman baru: {current_send_delay}s")

        # 2. Update Nilai Sensor (Setiap 5 Detik)
        if now - last_state_update >= STATE_UPDATE_INTERVAL:
            # Perubahan hanya 1-2 poin (volatilitas rendah)
            bpm_change = random.randint(-2, 2)
            spo2_change = random.randint(-1, 1) # SpO2 biasanya lebih stabil dari BPM

            current_bpm = clamp(current_bpm + bpm_change, BPM_MIN, BPM_MAX)
            current_spo2 = clamp(current_spo2 + spo2_change, SPO2_MIN, SPO2_MAX)
            
            last_state_update = now
            print(f"📊 [SENSOR UPDATE] BPM: {current_bpm} | SpO2: {current_spo2}%")

        # 3. Susun Payload JSON
        payload = {
            "HeartRate": current_bpm,
            "SpO2": float(current_spo2),
            "timestamp": now # Kunci untuk analisis QoS/Delay di SDN
        }
        
        # 4. Kirim via UDP
        message = json.dumps(payload)
        try:
            sock.sendto(message.encode(), (OVS_IP, OVS_PORT))
            print(f"[SENT] {message}")
        except Exception as e:
            print(f"[ERROR UDP] {e}")

        # 5. Jeda Pengiriman
        time.sleep(current_send_delay)

except KeyboardInterrupt:
    print("\n[INFO] Simulator dihentikan.")
finally:
    sock.close()
