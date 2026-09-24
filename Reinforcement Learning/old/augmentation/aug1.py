import pandas as pd
import numpy as np
import io
import os
from datetime import datetime, timedelta

def generate_augmented_network_dataset(input_file, output_file):
    # 1. Membaca pola dasar dari data asli
    with open(input_file, 'r') as f:
        lines = [line.strip().strip('"') for line in f if line.strip()]
    df_orig = pd.read_csv(io.StringIO("\n".join(lines)), sep=';', decimal=',')

    def generate_row(timestamp, policing_rate, traffic_loads, priority_map):
        """
        traffic_loads: dict {'p1': 'high'/'low', ...}
        priority_map: dict {'p1': int, 'p2': int, 'p4': int}
        """
        row = {'timestamp': timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")}
        
        # A. Simulasi Permintaan Trafik (Traffic Demand) dalam Kbps
        traffic_kbps = {}
        for p in ['p1', 'p2', 'p4']:
            if traffic_loads[p] == 'high':
                # Trafik tinggi (300-700 Mbps) untuk memicu overload
                traffic_kbps[p] = np.random.uniform(300000, 700000) 
            else:
                # Trafik normal/rendah (1-20 Mbps)
                traffic_kbps[p] = np.random.uniform(1000, 20000)
                
        # B. Alokasi Bandwidth Berdasarkan Prioritas (Resource Slicing)
        # Port dengan priority_tag lebih besar diproses lebih dulu
        sorted_ports = sorted(['p1', 'p2', 'p4'], key=lambda x: priority_map[x], reverse=True)
        
        remaining_bw = policing_rate
        allocated_bw = {}
        for p in sorted_ports:
            req = traffic_kbps[p]
            alloc = min(req, remaining_bw)
            allocated_bw[p] = alloc
            remaining_bw -= alloc
            
        # C. Pembuatan Metrik untuk Setiap Port
        for p in ['p1', 'p2', 'p4']:
            rx_kbps = traffic_kbps[p]
            alloc_kbps = allocated_bw[p]
            rx_mbps = rx_kbps / 1000.0
            
            # Logika Slicing: Jika alokasi < permintaan, terjadi drop dan delay
            if rx_kbps > alloc_kbps:
                drop_ratio = (rx_kbps - alloc_kbps) / rx_kbps
                delay = np.random.uniform(100, 300) # Delay tinggi (ms)
            else:
                drop_ratio = 0.0
                util_p = rx_kbps / policing_rate
                # Delay rendah, sedikit naik jika utilisasi mendekati kapasitas
                delay = np.random.uniform(5, 12) + (util_p * 15)
                
            pps = (rx_kbps * 1024) / (8 * 64) # Estimasi Packet per Second
            
            row.update({
                f'rx_mbps_{p}': rx_mbps,
                f'tx_mbps_{p}': rx_mbps * np.random.uniform(1.1, 1.4),
                f'rx_pps_{p}': pps,
                f'tx_pps_{p}': pps * 1.05,
                f'avg_rx_pkt_bytes_{p}': np.random.uniform(64, 128),
                f'util_rx_pct_{p}': rx_kbps / policing_rate,
                f'drop_{p}': drop_ratio,
                f'delay_ms_{p}': delay,
                f'last_payload_bytes_{p}': 140 if p=='p1' else (2824 if p=='p2' else 135),
                f'priority_tag_{p}': priority_map[p],
                f'policing_rate_kbps_{p}': policing_rate,
                f'policing_burst_kbps_{p}': 100000
            })
        return row

    # 2. Definisi Skenario Prioritas (P4 tidak boleh terendah)
    priority_scenarios = [
        {'p1': 1, 'p2': 0, 'p4': 2}, # P4 Tertinggi
        {'p1': 0, 'p2': 1, 'p4': 2}, # P4 Tertinggi
        {'p1': 2, 'p2': 0, 'p4': 1}, # P4 Menengah (P1 Tertinggi)
        {'p1': 0, 'p2': 2, 'p4': 1}, # P4 Menengah (P2 Tertinggi)
        {'p1': 1, 'p2': 1, 'p4': 2}, # P4 Tertinggi, lainnya setara
        {'p1': 0, 'p2': 0, 'p4': 1}, # P4 Tertinggi, lainnya setara
    ]

    # 3. Definisi Skenario Beban Trafik (Full Combinations)
    load_scenarios = [
        ('low', 'low', 'low'), ('high', 'low', 'low'),
        ('low', 'high', 'low'), ('low', 'low', 'high'),
        ('high', 'high', 'low'), # Skenario P1 & P2 Overload
        ('high', 'low', 'high'), ('low', 'high', 'high'),
        ('high', 'high', 'high') # Stress Test Total
    ]

    # 4. Proses Eksekusi Generate Data
    final_data_rows = []
    current_ts = datetime.now()
    
    for prio in priority_scenarios:
        for load in load_scenarios:
            l_map = {'p1': load[0], 'p2': load[1], 'p4': load[2]}
            # Generate 500 sampel untuk setiap kombinasi sub-skenario
            for _ in range(500):
                current_ts += timedelta(seconds=1)
                # Variasi policing rate 1.000.000 +/- 1% (step 10.000)
                pol_rate = 1000000 + (np.random.randint(-1, 2) * 10000)
                final_data_rows.append(generate_row(current_ts, pol_rate, l_map, prio))

    # 5. Konversi ke DataFrame dan Simpan
    df_final = pd.DataFrame(final_data_rows)
    df_final.to_csv(output_file, index=False, sep=';', decimal=',')
    print(f"Dataset berhasil dibuat: {output_file} dengan {len(df_final)} baris.")

# Jalankan Script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'dataset_dqn_rich.csv')
output_path = os.path.join(script_dir, 'dataset_dqn_final_varied.csv')
generate_augmented_network_dataset(input_path, output_path)