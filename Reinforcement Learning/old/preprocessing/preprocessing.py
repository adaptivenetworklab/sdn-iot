import pandas as pd
import numpy as np
import os
from scipy import stats

# --- Konfigurasi Berdasarkan Jurnal & SLA ---
TOTAL_CAPACITY_KBPS = 2500000  # 2.5 Gbps
SLA_DELAY_MS = {'p1': 7200, 'p2': 8200, 'p4': 7100} # Sesuai input Anda sebelumnya

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

def final_preprocessing(input_file, output_file):
    # Membaca file (menangani delimiter ; atau , secara otomatis)
    try:
        df = pd.read_csv(input_file, sep=';').fillna(0)
        if len(df.columns) < 10: # Jika gagal baca, coba koma
            df = pd.read_csv(input_file, sep=',').fillna(0)
    except:
        print("Gagal membaca file. Pastikan format CSV benar.")
        return

    # 1. Pembersihan Anomali sebelum Processing
    # Kita fokus pada delay dan throughput sebagai indikator anomali
    cols_to_check = ['delay_ms_p1', 'delay_ms_p2', 'delay_ms_p4', 'rx_mbps_p4']
    df = remove_outliers(df, cols_to_check)

    # 2. Feature Engineering: Packet Loss Rate (%)
    for p in ['p1', 'p2', 'p4']:
        df[f'loss_rate_{p}'] = np.where(df[f'tx_pps_{p}'] > 0, 
                                        ((df[f'tx_pps_{p}'] - df[f'rx_pps_{p}']).clip(lower=0) / df[f'tx_pps_{p}']) * 100, 
                                        0)
        
    # 3. Normalisasi Min-Max sesuai Persamaan (2) Jurnal
    cols_to_norm = [c for c in df.columns if any(x in c for x in ['mbps', 'pps', 'delay', 'loss_rate', 'util'])]
    for col in cols_to_norm:
        min_v, max_v = df[col].min(), df[col].max()
        df[f'norm_{col}'] = (df[col] - min_v) / (max_v - min_v) if max_v > min_v else 0

    # 4. Transformasi ke Format RL
    rl_rows = []
    for i in range(len(df) - 1):
        row = df.iloc[i]
        
        for action_id, weights in ACTIONS.items():
            total_reward = 0
            sim_results = {}
            
            for p in ['p1', 'p2', 'p4']:
                demand_kbps = row[f'rx_mbps_{p}'] * 1000
                alloc_kbps = weights[p] * TOTAL_CAPACITY_KBPS
                
                # Simulasi Fisika Jaringan (M/M/1 Queueing)
                margin = alloc_kbps - demand_kbps
                if margin > 0:
                    sim_delay = 2.0 + (1000.0 / margin)
                else:
                    sim_delay = 100.0 + (abs(margin) / (alloc_kbps + 1)) * 50
                
                # Reward Dasar (Inverse Delay)
                reward_p = (100.0 / (sim_delay + 1))
                
                # Penalti SLA Violation
                if sim_delay > SLA_DELAY_MS[p]:
                    reward_p -= 50 if p == 'p4' else 10
                
                # Aturan Keselamatan: p4 (HR) dilarang punya bobot paling rendah
                if p == 'p4' and weights['p4'] == min(weights.values()):
                    reward_p -= 100
                
                total_reward += reward_p
                sim_results[p] = sim_delay

            rl_rows.append({
                's_pps_p4': row['norm_rx_pps_p4'],
                's_util_p4': row['norm_util_rx_pct_p4'],
                's_prio_p4': row['priority_tag_p4'],
                's_bw_limit_p4': row['policing_rate_kbps_p4'],
                'action': action_id,
                'reward': round(total_reward, 4),
                'next_delay_p4': sim_results['p4'],
                'next_prio_p4': 2 if weights['p4'] == max(weights.values()) else 1,
                'done': False
            })

    pd.DataFrame(rl_rows).to_csv(output_file, index=False)
    print(f"Dataset RL Final berhasil dibuat: {output_file} ({len(rl_rows)} baris).")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "dataset_dqn_rich.csv")
    output_file = os.path.join(script_dir, "dqn_final_training_data2.csv")
    
    final_preprocessing(input_file, output_file)