#!/usr/bin/python3
import time
import random
import json
import socket

# --- KONFIGURASI JARINGAN ---
OVS_IP = "192.168.15.240"   # IP OVS listener
OVS_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)  # timeout tunggu ACK biar gak nge-freeze

# --- ID DEVICE ---
DEVICE_ID = "max"     # port 4
DEVICE_TYPE = "sensor"

# --- KONFIGURASI LOGIKA DUMMY ---
BPM_MIN, BPM_MAX = 67, 75
SPO2_MIN, SPO2_MAX = 95, 100

STATE_UPDATE_INTERVAL = 5     # nilai berubah tiap 5 detik
CONFIG_UPDATE_INTERVAL = 600  # delay pengiriman berubah tiap 10 menit

current_bpm = random.randint(BPM_MIN, BPM_MAX)
current_spo2 = random.randint(SPO2_MIN, SPO2_MAX)
current_send_delay = 1

last_state_update = time.time()
last_config_update = time.time()

seq = 0

def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

print(f"[INFO] MAX simulator started -> {OVS_IP}:{OVS_PORT}")
print(f"[INFO] Current send delay: {current_send_delay}s")
print("[INFO] RTT mode: waiting ACK from OVS listener...\n")

try:
    while True:
        now = time.time()



        # update state tiap 5 detik
        if now - last_state_update >= STATE_UPDATE_INTERVAL:
            bpm_change = random.randint(-2, 2)
            spo2_change = random.randint(-1, 1)

            current_bpm = clamp(current_bpm + bpm_change, BPM_MIN, BPM_MAX)
            current_spo2 = clamp(current_spo2 + spo2_change, SPO2_MIN, SPO2_MAX)

            last_state_update = now
            print(f"[SENSOR UPDATE] BPM={current_bpm} | SpO2={current_spo2}%")

        seq += 1

        payload = {
            "device_id": DEVICE_ID,
            "type": DEVICE_TYPE,

            "seq": seq,
            "send_ts": time.time(),  # epoch seconds

            "HeartRate": int(current_bpm),
            "SpO2": float(current_spo2),
        }

        # encode dulu untuk tau ukuran bytes real
        msg_bytes = json.dumps(payload).encode()
        payload["payload_bytes"] = len(msg_bytes)

        # encode ulang biar payload_bytes ikut terkirim
        msg_bytes = json.dumps(payload).encode()

        # kirim + hitung RTT
        t0 = time.time()
        try:
            sock.sendto(msg_bytes, (OVS_IP, OVS_PORT))
            print(f"[{time.strftime('%H:%M:%S')}] SENT seq={seq} delay={current_send_delay}s payload={len(msg_bytes)}B")
        except Exception as e:
            print(f"[ERROR] UDP send failed: {e}")
            time.sleep(current_send_delay)
            continue

        # tunggu ACK dari OVS listener
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
            print("   [WARN] ACK timeout (OVS overload / packet lost / listener not running)")

        except Exception as e:
            print(f"   [WARN] ACK error: {e}")

        time.sleep(current_send_delay)

except KeyboardInterrupt:
    print("\n[INFO] MAX simulator stopped.")
finally:
    sock.close()
