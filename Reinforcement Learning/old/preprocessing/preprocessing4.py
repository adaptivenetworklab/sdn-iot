import pandas as pd
import numpy as np
import os
import io

# --- Konfigurasi Optimasi Paper ---
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

def run_preprocessing(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = [line.strip().strip('"') for line in f if line.strip()]
    df = pd.read_csv(io.StringIO('\n'.join(lines)), sep=';', decimal=',')
    
    # Normalisasi State
    for col in [c for c in df.columns if any(x in c for x in ['mbps', 'pps', 'util'])]:
        df[f'norm_{col}'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-6)

    rl_rows = []
    for i in range(len(df)):
        row = df.iloc[i]
        # --- Logika Reward Baru di Preprocessing ---
        for action_id, weights in ACTIONS.items():
            total_reward = 0
            sim_res = {}
            for p in ['p1', 'p2', 'p4']:
                d = simulate_delay(weights[p] * TOTAL_CAPACITY_KBPS, row[f'rx_mbps_{p}'] * 1000)
                sim_res[p] = d
                
                # 1. Skor Dasar
                r = (100.0 / (d + 1))
                
                # 2. Bonus Kontras (Inti Perbaikan)
                if d <= SLA_DELAY_MS[p]:
                    r += 50  # Bonus besar jika berhasil menjaga SLA
                else:
                    r -= 150 if p == 'p4' else 75 # Penalti sangat berat jika melanggar
                    
            # 3. Penalti "Aksi Statis" (Opsional)
            # Jika kondisi jaringan sibuk tapi AI pilih Balanced, beri penalti kecil
            # agar AI terdorong mencari aksi prioritas (0, 1, 2)
            if action_id == 3:
                total_reward -= 10 

            total_reward += r
            rl_rows.append({
                'timestamp': row['timestamp'],
                's_pps_p1': row.get('norm_rx_pps_p1', 0), 's_util_p1': row.get('norm_util_rx_pct_p1', 0),
                's_pps_p2': row.get('norm_rx_pps_p2', 0), 's_util_p2': row.get('norm_util_rx_pct_p2', 0),
                's_pps_p4': row.get('norm_rx_pps_p4', 0), 's_util_p4': row.get('norm_util_rx_pct_p4', 0),
                'action_id': action_id, 'reward': round(total_reward, 4),
                'sim_delay_p1': round(sim_res['p1'], 2), 'sim_delay_p2': round(sim_res['p2'], 2), 'sim_delay_p4': round(sim_res['p4'], 2)
            })
    pd.DataFrame(rl_rows).to_csv(output_path, index=False)
    print("Preprocessing Selesai!")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "dataset_dqn_rich.csv")
    output_csv = os.path.join(script_dir, "dqn_final_v3.csv")
    
    if not os.path.exists(input_csv):
        print(f"Error: Input file not found at {input_csv}")
    else:
        run_preprocessing(input_csv, output_csv)