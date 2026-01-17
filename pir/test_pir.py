from gpiozero import MotionSensor
from signal import pause

# Inisialisasi PIR pada GPIO 27 (Pin 13)
pir = MotionSensor(27)

print("--- Test Sensor PIR Dimulai ---")
print("Menunggu gerakan... (Tekan Ctrl+C untuk berhenti)")

def gerakan_terdeteksi():
    print("✅ Gerakan Terdeteksi!")

def gerakan_berhenti():
    print("--- Gerakan Berhenti ---")

# Menghubungkan event dengan fungsi
pir.when_motion = gerakan_terdeteksi
pir.when_no_motion = gerakan_berhenti

pause()
