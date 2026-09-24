import pandas as pd
import numpy as np
import os
import io

# --- Konfigurasi ---
TOTAL_CAPACITY_KBPS = 13000 
SLA_DELAY_MS = {'p1': 15.0, 'p2': 12.0, 'p4': 3.5}

ACTIONS = {
    0: {'p1': 0.1, 'p2': 0.6, 'p4': 0.3}, # Prio Camera
    1: {'p1': 0.1, 'p2': 0.2, 'p4': 0.7}, # Prio Heart Rate
    2: {'p1': 0.5, 'p2': 0.2, 'p4': 0.3}, # Prio DHT
    3: {'p1': 0.3, 'p2': 0.3, 'p4': 0.4}  # Balanced
}

def simulate_delay(alloc, demand):
    margin = alloc - demand
    if margin > 1000: return 2.0 + (500.0 / margin)
    elif margin > 0: return 5.0 + (1000.0 / margin)
    else: return 20.0 + (abs(margin) / (alloc + 1)) * 50

def run_smart_augmentation(input_path, output_path, num_gen=2000):
    # 1. Load Data Asli sebagai referensi distribusi
    with open(input_path, 'r') as f:
        lines = [line.strip().strip('"') for line in f if line.strip()]
    df_base = pd.read_csv(io.StringIO('\n'.join(lines)), sep=';', decimal=',')
    
    # Bersihkan nama kolom jika ada whitespace
    df_base.columns = [c.strip() for c in df_base.columns]

    augmented_data = []
    print(f"Generating {num_gen} timestamps based on {input_path} distribution...")

    for t in range(num_gen):
        progress = t / num_gen
        # Ambil sampel acak dari data asli sebagai "base"
        base_row = df_base.sample(n=1).iloc[0]
        
        row = {'timestamp': f'AUG_{t}'}
        
        # Tentukan port mana yang akan kena 'burst'
        burst_ports = []
        if progress < 0.15: burst_ports = ['p1']
        elif progress < 0.30: burst_ports = ['p2']
        elif progress < 0.45: burst_ports = ['p4']
        elif progress < 0.60: burst_ports = ['p1', 'p2']
        elif progress < 0.75: burst_ports = ['p4', 'p2']
        elif progress < 0.90: burst_ports = [] # Stabil
        else: burst_ports = ['p1', 'p2', 'p4'] # Burst Semua

        for p in ['p1', 'p2', 'p4']:
            # Ambil nilai asli
            mbps = float(base_row[f'rx_mbps_{p}'])
            
            # Jika masuk dalam jadwal burst, naikkan nilainya secara signifikan
            if p in burst_ports:
                mbps = np.random.uniform(6.0, 9.5)
            else:
                # Beri sedikit variasi (noise) agar tidak persis sama dengan data asli
                mbps *= np.random.uniform(0.8, 1.2)

            # Hitung variabel lainnya berdasarkan mbps yang baru agar sinkron
            demand_kbps = mbps * 1000
            pps = (mbps * 10**6) / (8 * 64) * np.random.uniform(0.9, 1.1)
            util = min(0.95, demand_kbps / TOTAL_CAPACITY_KBPS)
            
            # State Priority: Pastikan P4 tidak terendah
            if p == 'p4':
                prio = np.random.randint(4, 8) 
            else:
                prio = np.random.randint(0, 5)

            # State Rate Limit & Payload (Varying)
            rate_limit = np.random.uniform(5000, 15000)
            avg_payload = np.random.uniform(64, 1000)
            
            # State Latency (Simulasi kondisi 'sebelum' aksi diambil)
            current_delay = simulate_delay(TOTAL_CAPACITY_KBPS/3, demand_kbps)

            row[f'rx_mbps_{p}'] = mbps
            row[f'rx_pps_{p}'] = pps
            row[f'util_rx_pct_{p}'] = util
            row[f'avg_rx_pkt_bytes_{p}'] = avg_payload
            row[f'priority_tag_{p}'] = prio
            row[f'policing_rate_kbps_{p}'] = rate_limit
            row[f'delay_ms_{p}'] = current_delay
            
        augmented_data.append(row)

    df_aug = pd.DataFrame(augmented_data)

    # 2. Proses menjadi dataset RL (8000 baris)
    state_keys = ['rx_mbps', 'delay_ms', 'util_rx_pct', 'rx_pps', 'avg_rx_pkt_bytes', 'priority_tag', 'policing_rate_kbps']
    
    # Normalisasi fitur state
    for p in ['p1', 'p2', 'p4']:
        for k in state_keys:
            col = f'{k}_{p}'
            df_aug[f'norm_{col}'] = (df_aug[col] - df_aug[col].min()) / (df_aug[col].max() - df_aug[col].min() + 1e-6)

    rl_rows = []
    for i in range(len(df_aug)):
        row = df_aug.iloc[i]
        for action_id, weights in ACTIONS.items():
            total_reward = 0
            sim_res = {}
            for p in ['p1', 'p2', 'p4']:
                demand_kbps = row[f'rx_mbps_{p}'] * 1000
                alloc_kbps = weights[p] * TOTAL_CAPACITY_KBPS
                d = simulate_delay(alloc_kbps, demand_kbps)
                sim_res[p] = d
                
                # Reward Logic
                r = (100.0 / (d + 1))
                if d <= SLA_DELAY_MS[p]: r += 50
                else: r -= 150 if p == 'p4' else 75
                total_reward += r
            
            if action_id == 3: total_reward -= 10 

            entry = {'timestamp': row['timestamp'], 'action_id': action_id, 'reward': round(total_reward, 4)}
            for p in ['p1', 'p2', 'p4']:
                for k in state_keys:
                    entry[f's_{k}_{p}'] = row[f'norm_{k}_{p}']
                entry[f'sim_delay_{p}'] = round(sim_res[p], 2)
            rl_rows.append(entry)
            
    pd.DataFrame(rl_rows).to_csv(output_path, index=False)
    print(f"Dataset v4 Selesai! Total: {len(rl_rows)} baris.")

# Jalankan
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "dataset_dqn_rich.csv")
    output_csv = os.path.join(script_dir, "dqn_final_v4.csv")
    
    if not os.path.exists(input_csv):
        print(f"Error: Input file not found at {input_csv}")
    else:
        run_smart_augmentation(input_csv, output_csv, num_gen=2000)