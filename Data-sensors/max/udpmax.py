import max30102
import time
import numpy as np
import socket
import json  # Library wajib untuk JSON

# --- KONFIGURASI UDP ---
OVS_IP = "192.168.15.240"
OVS_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

# --- KONFIGURASI SENSOR ---
BATCH_SIZE = 100 

def calculate_vital_signs(red_data, ir_data):
    """
    Fungsi kalkulasi BPM & SpO2
    """
    r = np.array(red_data)
    ir = np.array(ir_data)
    
    r_mean = np.mean(r)
    ir_mean = np.mean(ir)
    
    if r_mean == 0 or ir_mean == 0: return 0, 0
        
    r_ac = r - r_mean
    ir_ac = ir - ir_mean
    
    r_ac_rms = np.sqrt(np.mean(r_ac**2))
    ir_ac_rms = np.sqrt(np.mean(ir_ac**2))
    
    R = (r_ac_rms / r_mean) / (ir_ac_rms / ir_mean)
    spo2 = 110 - (25 * R)
    
    if spo2 > 100: spo2 = 99.9
    if spo2 < 50: spo2 = 0 
    
    peaks = 0
    for i in range(1, len(ir_ac)):
        if ir_ac[i-1] < 0 and ir_ac[i] >= 0:
            if (ir_ac[i] - ir_ac[i-1]) > 5: 
                peaks += 1
    
    sampling_duration_sec = 2
    bpm = peaks * (60 / sampling_duration_sec)
    
    return int(bpm), float(round(spo2, 1))

def send_udp(message):
    try:
        sock.sendto(message.encode(), (OVS_IP, OVS_PORT))
        # Print JSON yang dikirim agar terlihat jelas strukturnya
        print(f"[SENT] {message} --> {OVS_IP}:{OVS_PORT}")
    except Exception as e:
        print(f"[ERROR UDP] {e}")

# --- MAIN PROGRAM ---
m = max30102.MAX30102()

print(f"[INFO] Sensor MAX30102 (JSON Mode) dimulai. Target: {OVS_IP}:{OVS_PORT}")

try:
    while True:
        # 1. Pengumpulan Data
        red_buf = []
        ir_buf = []
        
        while len(ir_buf) < BATCH_SIZE:
            r, i = m.read_sequential()
            if r and i:
                red_buf.extend(r)
                ir_buf.extend(i)
        
        red_buf = red_buf[:BATCH_SIZE]
        ir_buf = ir_buf[:BATCH_SIZE]
        
        # 2. Validasi & Kalkulasi
        ir_avg = sum(ir_buf) / len(ir_buf)
        
        # Default Value (Angka 0, bukan string)
        bpm_val = 0
        spo2_val = 0.0
        
        if ir_avg > 50000:
            calc_bpm, calc_spo2 = calculate_vital_signs(red_buf, ir_buf)
            
            # Filter Noise
            if 40 < calc_bpm < 180:
                bpm_val = calc_bpm
                spo2_val = calc_spo2
        
        # 3. Format JSON Payload
        # Membuat Dictionary Python
        payload = {
            "HeartRate": bpm_val,
            "SpO2": spo2_val
        }
        
        # Konversi Dictionary ke JSON String
        message = json.dumps(payload)
        
        send_udp(message)
        
except KeyboardInterrupt:
    print("\n[INFO] Dihentikan oleh pengguna.")
finally:
    m.shutdown()
    sock.close()
    print("[INFO] Socket ditutup.")
