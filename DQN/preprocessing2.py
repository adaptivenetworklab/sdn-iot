import pandas as pd
import numpy as np
import os
import io

# --- Konfigurasi Berdasarkan Jurnal & SLA ---
TOTAL_CAPACITY_KBPS = 13000  # Kapasitas diturunkan agar efek kemacetan terasa
SLA_DELAY_MS = {'p1': 20, 'p2': 18, 'p4': 6}

ACTIONS = {
    0: {'p1': 0.1, 'p2': 0.6, 'p4': 0.3}, # Prio Camera
    1: {'p1': 0.1, 'p2': 0.2, 'p4': 0.7}, # Prio HR
    2: {'p1': 0.5, 'p2': 0.2, 'p4': 0.3}, # Prio DHT
    3: {'p1': 0.3, 'p2': 0.3, 'p4': 0.4}  # Balanced
}

def remove_outliers(df, columns):
    """Menghapus baris yang memiliki nilai anomali di luar 1.5 * IQR"""
    initial_rows = len(df)
    for col in columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(f"Pembersihan Anomali: Menghapus {initial_rows - len(df)} baris data pencilan.")
    return df

def simulate_delay(alloc, demand):
    margin = alloc - demand
    if margin > 1000:   
        return 2.0 + (500.0 / margin)
    elif margin > 0:    
        return 5.0 + (1000.0 / margin)
    else:              
        return 20.0 + (abs(margin) / (alloc + 1)) * 50
        
def final_preprocessing(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} tidak ditemukan!")
        return

    with open(input_path, 'r') as f:
        lines = [line.strip().strip('"') for line in f if line.strip()]
    
    df = pd.read_csv(io.StringIO('\n'.join(lines)), sep=';', decimal=',')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # 1. Normalisasi (Semua Port)
    cols_to_norm = [c for c in df.columns if any(x in c for x in ['mbps', 'pps', 'util'])]
    for col in cols_to_norm:
        min_v, max_v = df[col].min(), df[col].max()
        df[f'norm_{col}'] = (df[col] - min_v) / (max_v - min_v) if max_v > min_v else 0

    # 2. Transformasi ke Format RL
    rl_rows = []
    for i in range(len(df)):
        row = df.iloc[i]
        ts = row['timestamp']
        
        # Tiap timestamp akan menghasilkan 4 baris (satu untuk tiap kemungkinan aksi)
        for action_id, weights in ACTIONS.items():
            total_reward = 0
            sim_delays = {}
            
            for p in ['p1', 'p2', 'p4']:
                demand_kbps = row[f'rx_mbps_{p}'] * 1000
                alloc_kbps = weights[p] * TOTAL_CAPACITY_KBPS
                
                # Panggil fungsi simulasi
                current_sim_delay = simulate_delay(alloc_kbps, demand_kbps)
                sim_delays[p] = current_sim_delay
                
                # Hitung Reward per Port
                reward_p = (100.0 / (current_sim_delay + 1))
                if current_sim_delay > SLA_DELAY_MS[p]:
                    reward_p -= 50 if p == 'p4' else 10
                if p == 'p4' and weights['p4'] == min(weights.values()):
                    reward_p -= 100
                
                total_reward += reward_p

            # Simpan data lengkap (Timestamp + Semua Port + Action + Reward)
            rl_rows.append({
                'timestamp': ts,
                # State p1
                's_pps_p1': row.get('norm_rx_pps_p1', 0),
                's_util_p1': row.get('norm_util_rx_pct_p1', 0),
                # State p2
                's_pps_p2': row.get('norm_rx_pps_p2', 0),
                's_util_p2': row.get('norm_util_rx_pct_p2', 0),
                # State p4
                's_pps_p4': row.get('norm_rx_pps_p4', 0),
                's_util_p4': row.get('norm_util_rx_pct_p4', 0),
                # Metadata Policy
                'action_id': action_id,
                'reward': round(total_reward, 4),
                # Hasil Simulasi (Next State info)
                'sim_delay_p1': round(sim_delays['p1'], 2),
                'sim_delay_p2': round(sim_delays['p2'], 2),
                'sim_delay_p4': round(sim_delays['p4'], 2),
                'done': False
            })

    pd.DataFrame(rl_rows).to_csv(output_path, index=False)
    print(f"Dataset RL Komplit disimpan di: {output_path}")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_path, "dataset_dqn_rich.csv")
    output_file = os.path.join(base_path, "dqn_final_training_data_multiport.csv")
    final_preprocessing(input_file, output_file)