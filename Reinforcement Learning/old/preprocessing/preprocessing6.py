import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

def final_preprocessing_pipeline(input_csv, window_size=4):
    """
    Pipeline preprocessing untuk riset perbandingan DQN, DDQN, PPO, dan Proposed Algo.
    Menggunakan teknik Frame Stacking dan Reward Shaping.
    """
    # 1. Load Dataset Augmented
    df = pd.read_csv(input_csv, sep=';', decimal=',')
    print(f"[INFO] Dataset loaded: {df.shape}")

    # 2. Feature Engineering: Bottleneck & Trends
    # Menghitung total throughput untuk kesadaran kapasitas global
    df['total_rx_mbps'] = df['rx_mbps_p1'] + df['rx_mbps_p2'] + df['rx_mbps_p4']
    
    # Menghitung Delta (perubahan) untuk mendeteksi lonjakan trafik mendadak
    for p in ['p1', 'p2', 'p4']:
        df[f'delta_rx_{p}'] = df[f'rx_mbps_{p}'].diff().fillna(0)

    # 3. Log Transformation (Khusus untuk Delay)
    # Sangat penting agar nilai delay 300ms tidak mendominasi nilai delay 6ms secara linear
    for p in ['p1', 'p2', 'p4']:
        df[f'delay_log_{p}'] = np.log1p(df[f'delay_ms_{p}'])

    # 4. Seleksi Fitur State (X)
    # Total 19 fitur per time-step
    state_features = [
        'rx_mbps_p1', 'util_rx_pct_p1', 'drop_p1', 'delay_log_p1', 'priority_tag_p1',
        'rx_mbps_p2', 'util_rx_pct_p2', 'drop_p2', 'delay_log_p2', 'priority_tag_p2',
        'rx_mbps_p4', 'util_rx_pct_p4', 'drop_p4', 'delay_log_p4', 'priority_tag_p4',
        'total_rx_mbps', 'delta_rx_p1', 'delta_rx_p2', 'delta_rx_p4'
    ]

    # 5. Global Scaling (Min-Max Scaling [0, 1])
    # Konsistensi scaling sangat krusial untuk perbandingan antar model
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[state_features] = scaler.fit_transform(df[state_features])
    
    # Simpan skaler agar bisa digunakan saat testing/real-time SDN
    joblib.dump(scaler, 'rl_global_scaler.pkl')

    # 6. Reward Shaping (Target Y)
    # Logika: Keberhasilan Port 4 bernilai 10x lebih tinggi dari port lain.
    # Penalti Drop pada Port 4 dibuat sangat eksponensial.
    def calculate_reward(row):
        # Benefit dari throughput yang berhasil dikirim
        benefit = (row['rx_mbps_p4'] * 0.5) + (row['rx_mbps_p1'] * 0.1) + (row['rx_mbps_p2'] * 0.05)
        # Penalti Drop (Port 4/Heartrate adalah Prioritas Utama)
        penalty_drop = (row['drop_p4'] * 100) + (row['drop_p1'] * 10) + (row['drop_p2'] * 5)
        # Penalti Latensi
        penalty_delay = (row['delay_log_p4'] * 2.0) + (row['delay_log_p1'] * 0.5)
        
        return benefit - penalty_drop - penalty_delay

    df_scaled['reward'] = df.apply(calculate_reward, axis=1)

    # 7. Frame Stacking (Mengubah data menjadi format Sequence)
    # Format ini diperlukan untuk menangkap aspek temporal di jaringan
    def stack_frames(data, window):
        stacked = []
        for i in range(len(data) - window + 1):
            stacked.append(data[i : i + window])
        return np.array(stacked)

    X_final = stack_frames(df_scaled[state_features].values, window_size)
    Y_final = df_scaled['reward'].values[window_size-1:]

    # 8. Simpan hasil akhir (Format Numpy untuk efisiensi training)
    np.save('X_state_tensor.npy', X_final)
    np.save('Y_reward_tensor.npy', Y_final)
    
    print("\n[SUCCESS] Preprocessing Selesai!")
    print(f"Shape State (Samples, Window, Features): {X_final.shape}")
    print(f"Shape Reward: {Y_final.shape}")
    print(f"File disimpan: X_state_tensor.npy, Y_reward_tensor.npy, rl_global_scaler.pkl")
    return X_final, Y_final

# Jalankan pipeline
X, Y = final_preprocessing_pipeline('dataset_dqn_final_varied.csv', window_size=4)