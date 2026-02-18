import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import os
import io
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 1. SETUP & PATHS
MODEL_PATH = "wgan_generator.pth"
SCALER_PATH = "wgan_scaler.pkl"
DATA_INPUT = "dataset_dqn_rich.csv"
OUTPUT_CSV = "augmented_network_data.csv"

# 2. LOAD & CLEAN DATA
with open(DATA_INPUT, 'r') as f:
    lines = [line.strip().strip('"') for line in f if line.strip()]
df_real = pd.read_csv(io.StringIO("\n".join(lines)), sep=';', decimal=',')

# Identifikasi nama fitur (tanpa timestamp)
feature_names = [col for col in df_real.columns if col != 'timestamp']
df_numeric = df_real[feature_names].copy()

# 3. WGAN-GP ARCHITECTURE
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

class Critic(nn.Module):
    def __init__(self, input_dim, condition_dim):
        super(Critic, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim + condition_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1)
        )
    def forward(self, x, label):
        data = torch.cat([x, label], dim=1)
        return self.model(data)

# 4. TRAINING FUNCTION (With Checkpoint)
def train_or_load_wgan(df, epochs=1000):
    latent_dim = 100
    condition_dim = 4
    output_dim = len(feature_names)
    
    scaler = MinMaxScaler(feature_range=(-1, 1))
    data_scaled = scaler.fit_transform(df)
    
    gen = Generator(latent_dim, condition_dim, output_dim)
    crit = Critic(output_dim, condition_dim)

    if os.path.exists(MODEL_PATH):
        print("[INFO] Model ditemukan. Melewati proses training...")
        gen.load_state_dict(torch.load(MODEL_PATH))
        scaler = joblib.load(SCALER_PATH)
    else:
        print("[INFO] Memulai training WGAN-GP (Ini memakan waktu)...")
        optimizer_G = optim.Adam(gen.parameters(), lr=1e-4, betas=(0.5, 0.9))
        optimizer_C = optim.Adam(crit.parameters(), lr=1e-4, betas=(0.5, 0.9))
        
        data_tensor = torch.FloatTensor(data_scaled)
        
        for epoch in range(epochs + 1):
            # Train Critic (Standard WGAN-GP loop simplified)
            z = torch.randn(data_tensor.size(0), latent_dim)
            labels = torch.eye(condition_dim)[np.random.choice(condition_dim, data_tensor.size(0))]
            
            fake_data = gen(z, labels)
            loss_C = -torch.mean(crit(data_tensor, labels)) + torch.mean(crit(fake_data.detach(), labels))
            
            optimizer_C.zero_grad(); loss_C.backward(); optimizer_C.step()
            
            # Train Generator
            loss_G = -torch.mean(crit(gen(z, labels), labels))
            optimizer_G.zero_grad(); loss_G.backward(); optimizer_G.step()
            
            if epoch % 200 == 0:
                print(f"Epoch {epoch}/{epochs} | Loss G: {loss_G.item():.4f}")

        # Save Checkpoint
        torch.save(gen.state_dict(), MODEL_PATH)
        joblib.dump(scaler, SCALER_PATH)
        print("[SUCCESS] Model disimpan.")
        
    return gen, scaler

# 5. DATA GENERATION (With Correct Headers)
def generate_and_save(gen, scaler, num_samples=2000):
    gen.eval()
    latent_dim = 100
    condition_dim = 4
    
    z = torch.randn(num_samples, latent_dim)
    labels = torch.eye(condition_dim)[np.random.choice(condition_dim, num_samples)]
    
    with torch.no_grad():
        fake_data = gen(z, labels).numpy()
    
    # Inverse Transform & Mapping Headers
    final_data = scaler.inverse_transform(fake_data)
    df_fake = pd.DataFrame(final_data, columns=feature_names)
    
    # Tambahkan Timestamp Dummy (Urutan detik)
    start_time = pd.to_datetime(df_real['timestamp'].iloc[-1])
    df_fake['timestamp'] = [ (start_time + pd.Timedelta(seconds=i)).strftime("%Y-%m-%dT%H:%M:%SZ") for i in range(num_samples)]
    
    # Reorder columns agar timestamp di depan
    cols = ['timestamp'] + feature_names
    df_fake = df_fake[cols]
    
    df_fake.to_csv(OUTPUT_CSV, index=False, sep=';', decimal=',')
    return df_fake

# 6. VISUAL EVALUATION (PCA & t-SNE)
def evaluate_visual(real_df, fake_df):
    print("[INFO] Melakukan Evaluasi Visual (PCA & t-SNE)...")
    
    # Ambil subset agar t-SNE tidak terlalu lama
    n_samples = min(500, len(real_df), len(fake_df))
    real_sample = real_df[feature_names].sample(n_samples).values
    fake_sample = fake_df[feature_names].sample(n_samples).values
    
    combined = np.vstack([real_sample, fake_sample])
    labels = np.array(['Real'] * n_samples + ['Synthetic'] * n_samples)
    
    # PCA
    pca = PCA(n_components=2)
    pca_res = pca.fit_transform(combined)
    
    # t-SNE
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    tsne_res = tsne.fit_transform(combined)
    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    sns.scatterplot(x=pca_res[:,0], y=pca_res[:,1], hue=labels, ax=ax1, palette=['blue', 'red'], alpha=0.6)
    ax1.set_title("PCA: Sebaran Data Real vs Synthetic")
    
    sns.scatterplot(x=tsne_res[:,0], y=tsne_res[:,1], hue=labels, ax=ax2, palette=['blue', 'red'], alpha=0.6)
    ax2.set_title("t-SNE: Struktur Manifold Real vs Synthetic")
    
    plt.savefig("visual_evaluation.png", dpi=300)
    plt.show()

# RUN ALL
gen_model, scaler_model = train_or_load_wgan(df_numeric, epochs=1000)
df_synthetic = generate_and_save(gen_model, scaler_model)
evaluate_visual(df_real, df_synthetic)