import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

def final_sla_preprocessing(input_csv, window_size=4):
    """
    Preprocessing dengan SLA-Aware Reward Shaping untuk riset komparatif.
    Target: Memaksimalkan throughput sambil menjaga delay di bawah ambang batas SLA.
    """
    # 1. Load Dataset
    df = pd.read_csv(input_csv, sep=';', decimal=',')
    print(f"[INFO] Data loaded: {df.shape}")

    # 2. Feature Engineering
    # Global Bottleneck Awareness
    df['total_rx_mbps'] = df['rx_mbps_p1'] + df['rx_mbps_p2'] + df['rx_mbps_p4']
    
    # Delta Trends (Mendeteksi lonjakan trafik)
    for p in ['p1', 'p2', 'p4']:
        df[f'delta_rx_{p}'] = df[f'rx_mbps_{p}'].diff().fillna(0)
    
    # Log Transformation untuk Delay (Agar model sensitif pada ms kecil)
    for p in ['p1', 'p2', 'p4']:
        df[f'delay_log_{p}'] = np.log1p(df[f'delay_ms_{p}'])

    # 3. SLA-Aware Reward Shaping (Kunci Keunggulan Model Proposed)
    def calculate_reward(row):
        # --- A. Benefit (Throughput Gain) ---
        # Prioritas utama diberikan ke Port 4
        benefit = (row['rx_mbps_p4'] * 1.0) + (row['rx_mbps_p1'] * 0.2) + (row['rx_mbps_p2'] * 0.1)
        
        # --- B. SLA Delay Thresholds (Batas Toleransi) ---
        SLA_P4 = 15.0      # ms (Sangat ketat untuk Heartrate)
        SLA_OTHERS = 50.0  # ms (Lebih longgar untuk DHT/Camera)
        
        penalty_sla = 0
        
        # Penalti Pelanggaran SLA Port 4 (Eksponensial)
        if row['delay_ms_p4'] > SLA_P4:
            # Semakin jauh melanggar, penalti semakin mematikan
            penalty_sla += 150 * (row['delay_ms_p4'] / SLA_P4)
            
        # Penalti Pelanggaran SLA Port lain
        if row['delay_ms_p1'] > SLA_OTHERS: penalty_sla += 20
        if row['delay_ms_p2'] > SLA_OTHERS: penalty_sla += 10
        
        # --- C. Reliability Penalty (Packet Drops) ---
        # Drop pada Port 4 adalah kegagalan sistem total
        penalty_drop = (row['drop_p4'] * 300) + (row['drop_p1'] * 50) + (row['drop_p2'] * 20)
        
        return benefit - penalty_sla - penalty_drop

    # Hitung Reward
    df['reward'] = df.apply(calculate_reward, axis=1)

    # 4. Seleksi Fitur State (X) - 19 Fitur
    state_features = [
        'rx_mbps_p1', 'util_rx_pct_p1', 'drop_p1', 'delay_log_p1', 'priority_tag_p1',
        'rx_mbps_p2', 'util_rx_pct_p2', 'drop_p2', 'delay_log_p2', 'priority_tag_p2',
        'rx_mbps_p4', 'util_rx_pct_p4', 'drop_p4', 'delay_log_p4', 'priority_tag_p4',
        'total_rx_mbps', 'delta_rx_p1', 'delta_rx_p2', 'delta_rx_p4'
    ]

    # 5. Normalisasi Global [0, 1]
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[state_features] = scaler.fit_transform(df[state_features])
    joblib.dump(scaler, 'rl_global_scaler_v2.pkl')

    # 6. Temporal Frame Stacking
    def stack_frames(data, window):
        stacked = []
        for i in range(len(data) - window + 1):
            stacked.append(data[i : i + window])
        return np.array(stacked)

    X_final = stack_frames(df_scaled[state_features].values, window_size)
    Y_final = df_scaled['reward'].values[window_size-1:]

    # 7. Save Dataset Training
    np.save('X_state_tensor2.npy', X_final)
    np.save('Y_reward_tensor2.npy', Y_final)
    
    print("\n[SUCCESS] Preprocessing dengan SLA Reward Selesai!")
    print(f"Final Tensor Shape: {X_final.shape}")
    print(f"Reward Mean: {Y_final.mean():.2f}")
    
    return X_final, Y_final

# Eksekusi
X, Y = final_sla_preprocessing('dataset_dqn_final_varied.csv')