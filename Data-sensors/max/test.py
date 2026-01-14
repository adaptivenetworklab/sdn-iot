import max30102
import time

# Inisialisasi sensor
# Saat baris ini jalan, driver otomatis menulis konfigurasi default ke sensor
m = max30102.MAX30102()

try:
    print("--- MONITOR SENSOR AKTIF (Revisi) ---")
    print("Tempelkan jari. Cari posisi sampai angka IR > 50.000")
    print("Tekan Ctrl+C untuk berhenti.")
    
    while True:
        # Baca tumpukan data (batch)
        # Driver ini membaca 100 sampel sekaligus (memakan waktu sekitar 1 detik)
        red, ir = m.read_sequential()
        
        # Validasi agar tidak crash jika data kosong
        if ir and red and len(ir) > 0:
            # Hitung rata-rata
            avg_red = sum(red) / len(red)
            avg_ir = sum(ir) / len(ir)
            
            # Logika Status Sederhana
            status = "KOSONG"
            # Ambang batas ini mungkin perlu disesuaikan dengan jari Anda
            if avg_ir > 50000:
                status = "JARI TERDETEKSI"
            elif avg_ir > 20000:
                status = "SINYAL LEMAH"
            
            # Print hasil
            print(f"Status: {status} | IR: {int(avg_ir)} | Red: {int(avg_red)}")
            
        # Tidak perlu sleep lama-lama karena read_sequential sudah blocking
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStop.")
    m.shutdown()
except Exception as e:
    print(f"\nError: {e}")
    m.shutdown()
