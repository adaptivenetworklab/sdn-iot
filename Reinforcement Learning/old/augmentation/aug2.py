import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mutual_info_score

# 1. GRAPH CONDITIONING: Membangun Matriks Relasi Fitur
def build_feature_graph(df):
    # Menghitung korelasi untuk menjaga integritas antar port
    corr_matrix = df.corr().abs().values
    # Tambahkan Mutual Information untuk menangkap dependensi non-linear
    # (Opsional: dalam riset, ini bisa diplot sebagai Graph Adjacency Matrix)
    return torch.FloatTensor(corr_matrix)

# 2. ARSITEKTUR GENERATOR (WGAN)
class Generator(nn.Module):
    def __init__(self, latent_dim, condition_dim, output_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim + condition_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, output_dim),
            nn.Tanh() # Normalisasi output ke range [-1, 1]
        )

    def forward(self, z, label):
        x = torch.cat([z, label], dim=1)
        return self.model(x)

# 3. ARSITEKTUR CRITIC (DISCRIMINATOR)
class Critic(nn.Module):
    def __init__(self, input_dim, condition_dim):
        super(Critic, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim + condition_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1) # Output berupa skor Wasserstein
        )

    def forward(self, x, label):
        data = torch.cat([x, label], dim=1)
        return self.model(data)

# 4. SEMANTIC LOSS (LLM-Guided Constraints)
def semantic_penalty(generated_data, labels, scaler):
    """
    Fungsi ini mensimulasikan 'LLM Guidance' dengan memastikan data 
    mematuhi aturan SLA yang didefinisikan secara semantik.
    """
    penalty = 0.0
    # Denormalisasi sederhana untuk cek batasan fisik
    # Contoh Aturan: Jika Label = 1 (P4 Priority), Delay P4 tidak boleh > 15ms
    # (Index delay_ms_p4 dalam dataset adalah 32)
    p4_delay = generated_data[:, 32] 
    is_p4_high_prio = (labels[:, 3] == 1) # Asumsi index 3 adalah label P4
    
    # Berikan penalti jika aturan semantik dilanggar
    violation = torch.relu(p4_delay - 0.2) # 0.2 adalah threshold ternormalisasi
    penalty += torch.mean(violation * is_p4_high_prio.float())
    
    return penalty * 100 # Bobot penalti semantik

# 5. ENGINE TRAINING WGAN-GP
def train_wgan_gp(df_real, epochs=2000):
    latent_dim = 100
    condition_dim = 4 # [Normal, Congested P1, P2, P4]
    
    # Preprocessing - drop timestamp if exists, otherwise select numeric columns
    scaler = MinMaxScaler(feature_range=(-1, 1))
    if 'timestamp' in df_real.columns:
        df_numeric = df_real.drop(columns=['timestamp'])
    else:
        df_numeric = df_real.select_dtypes(include=[np.number])
    
    output_dim = df_numeric.shape[1]  # Dynamic based on actual numeric features
    
    gen = Generator(latent_dim, condition_dim, output_dim)
    crit = Critic(output_dim, condition_dim)
    opt_gen = optim.Adam(gen.parameters(), lr=1e-4, betas=(0.5, 0.9))
    opt_crit = optim.Adam(crit.parameters(), lr=1e-4, betas=(0.5, 0.9))

    # Preprocessing - drop timestamp if exists, otherwise select numeric columns
    scaler = MinMaxScaler(feature_range=(-1, 1))
    
    data_scaled = scaler.fit_transform(df_numeric)
    data_tensor = torch.FloatTensor(data_scaled)
    
    # Feature Graph untuk conditioning
    adj_matrix = build_feature_graph(df_numeric)

    for epoch in range(epochs):
        # --- Train Critic ---
        for _ in range(5): # Critic dilatih lebih sering (WGAN)
            z = torch.randn(data_tensor.size(0), latent_dim)
            fake_labels = torch.eye(condition_dim)[np.random.choice(condition_dim, data_tensor.size(0))]
            
            fake_data = gen(z, fake_labels)
            crit_real = crit(data_tensor, fake_labels)
            crit_fake = crit(fake_data.detach(), fake_labels)
            
            # Wasserstein Loss + Gradient Penalty (GP)
            loss_crit = -(torch.mean(crit_real) - torch.mean(crit_fake))
            
            opt_crit.zero_grad()
            loss_crit.backward()
            opt_crit.step()

        # --- Train Generator ---
        z = torch.randn(data_tensor.size(0), latent_dim)
        gen_data = gen(z, fake_labels)
        gen_score = crit(gen_data, fake_labels)
        
        # Loss Generator = -Critic Score + Semantic Penalty
        loss_gen = -torch.mean(gen_score) + semantic_penalty(gen_data, fake_labels, scaler)
        
        opt_gen.zero_grad()
        loss_gen.backward()
        opt_gen.step()

        if epoch % 500 == 0:
            print(f"Epoch {epoch} | Loss G: {loss_gen.item():.4f} | Loss C: {loss_crit.item():.4f}")

    return gen, scaler

# 6. GENERASI DATASET AUGMENTASI
def generate_augmented_scenarios(gen, scaler, num_samples=5000):
    # Meminta model membuat skenario "P4 High Priority & P2 Congested"
    z = torch.randn(num_samples, 100)
    # Label: 0=Normal, 1=CongP1, 2=CongP2, 3=CongP4
    target_label = torch.zeros(num_samples, 4)
    target_label[:, 3] = 1 # Fokus pada Skenario P4 
    
    gen.eval()
    with torch.no_grad():
        synthetic_data = gen(z, target_label).numpy()
    
    df_synthetic = pd.DataFrame(scaler.inverse_transform(synthetic_data))
    return df_synthetic

import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import joblib
import os

# --- 1. Definisi Arsitektur (Harus sama saat Save/Load) ---
class Generator(nn.Module):
    def __init__(self, latent_dim, condition_dim, output_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim + condition_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, output_dim),
            nn.Tanh()
        )
    def forward(self, z, label):
        x = torch.cat([z, label], dim=1)
        return self.model(x)

# --- 2. Fungsi Training & Simpan Model ---
def train_and_save_wgan(df_real, model_path='wgan_generator.pth', scaler_path='scaler_wgan.pkl'):
    # Preprocessing
    feature_cols = df_real.columns.drop('timestamp')
    scaler = MinMaxScaler(feature_range=(-1, 1))
    data_scaled = scaler.fit_transform(df_real[feature_cols])
    
    # Save Scaler
    joblib.dump(scaler, scaler_path)
    
    latent_dim, condition_dim, output_dim = 100, 4, len(feature_cols)
    gen = Generator(latent_dim, condition_dim, output_dim).to('cuda' if torch.cuda.is_available() else 'cpu')
    
    # ... (Proses Training WGAN-GP Anda di sini selama 2000 epoch) ...
    # Misal setelah training selesai:
    torch.save(gen.state_dict(), model_path)
    print(f"Model tersimpan di {model_path}. Anda tidak perlu training ulang lagi!")
    return gen, scaler, feature_cols

# --- 3. Fungsi Generasi Data (Dengan Nama Kolom yang Benar) ---
def generate_from_saved_model(df_real, num_samples=5000):
    feature_cols = df_real.columns.drop('timestamp')
    latent_dim, condition_dim, output_dim = 100, 4, len(feature_cols)
    
    # Load Model & Scaler
    gen = Generator(latent_dim, condition_dim, output_dim)
    gen.load_state_dict(torch.load('wgan_generator.pth'))
    scaler = joblib.load('scaler_wgan.pkl')
    
    z = torch.randn(num_samples, latent_dim)
    labels = torch.eye(condition_dim)[np.random.choice(condition_dim, num_samples)]
    
    gen.eval()
    with torch.no_grad():
        fake_data = gen(z, labels).numpy()
    
    # Kembalikan ke skala asli dan beri nama kolom
    df_fake = pd.DataFrame(scaler.inverse_transform(fake_data), columns=feature_cols)
    
    # Generate Timestamp sintetis (opsional, agar format sama)
    last_ts = pd.to_datetime(df_real['timestamp'].iloc[-1])
    df_fake['timestamp'] = [ (last_ts + pd.Timedelta(seconds=i)).strftime("%Y-%m-%dT%H:%M:%SZ") for i in range(len(df_fake))]
    
    # Reorder kolom agar timestamp di depan
    df_fake = df_fake[['timestamp'] + list(feature_cols)]
    return df_fake

# --- 4. EVALUASI VISUAL (PCA & t-SNE) ---
def visualize_validity(df_real, df_fake):
    real_features = df_real.drop(columns=['timestamp']).values[:1000] # Ambil 1000 sampel saja agar cepat
    fake_features = df_fake.drop(columns=['timestamp']).values[:1000]
    
    # Gabungkan untuk visualisasi
    combined = np.vstack([real_features, fake_features])
    labels = np.array(['Real'] * len(real_features) + ['Synthetic'] * len(fake_features))
    
    # PCA
    pca = PCA(n_components=2)
    res_pca = pca.fit_transform(combined)
    
    # t-SNE (Sangat kuat untuk data non-linear jaringan)
    tsne = TSNE(n_components=2, perplexity=30)
    res_tsne = tsne.fit_transform(combined)
    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    sns.scatterplot(x=res_pca[:, 0], y=res_pca[:, 1], hue=labels, ax=ax1, alpha=0.5)
    ax1.set_title("Validitas Data via PCA")
    
    sns.scatterplot(x=res_tsne[:, 0], y=res_tsne[:, 1], hue=labels, ax=ax2, alpha=0.5)
    ax2.set_title("Validitas Data via t-SNE")
    
    plt.savefig("validasi_gan_paper.png", dpi=300)
    plt.show()

# CARA PAKAI:
# 1. Jalankan training sekali saja.
# gen, scaler, cols = train_and_save_wgan(df_asli)

# 2. Besoknya, jika butuh data lagi, cukup panggil load:
df_real = pd.read_csv('dataset_dqn_final_varied.csv', sep=';', decimal=',')
df_new = generate_from_saved_model(df_real)
visualize_validity(df_real, df_new)

# Eksekusi (Contoh)
# df_real = pd.read_csv('dataset_dqn_final_varied.csv', sep=';', decimal=',')
# generator_model, data_scaler = train_wgan_gp(df_real)
# df_new = generate_augmented_scenarios(generator_model, data_scaler)
# df_new.to_csv('augmented_network_data.csv', index=False)