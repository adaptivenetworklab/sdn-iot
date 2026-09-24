# Fase 1 — Verifikasi dan Pembungkusan Training Loop

Tanggal: 2026-09-24
Sumber: `Reinforcement Learning/revision/allModel4.ipynb` (10 cell, seluruhnya code)
Keluaran fase ini: `scripts/sweep.py`

---

## 1. Verifikasi: apakah training loop benar-benar berjalan?

**Ya, untuk keempat algoritma yang dilatih.** Terdapat forward pass nyata, loss nyata, `.backward()` nyata, dan `optimizer.step()` nyata. Tidak ada simulasi kurva seperti pada `final/allModel1.ipynb`.

Loop tunggal berada di **cell 4**, `for epoch in range(2000)`.

| Algoritma | Loss | `.backward()` | `.step()` | Verdict |
|---|---|---|---|---|
| DQN | `nn.MSELoss()(q_values, target_q)` | `allModel4.ipynb:359` | `:361` | **NYATA** |
| DDQN | `nn.MSELoss()(q_values_ddqn, target_q_ddqn)` | `:375` | `:377` | **NYATA** |
| PPO Standard | `loss_critic_ppo + loss_actor_ppo` | `:406` | `:408` | **NYATA** |
| SDH-PPO (critic) | `nn.MSELoss()(values_sdh, target_values_sdh)` | `:434` | `:436` | **NYATA** |
| SDH-PPO (actor) | `actor_loss_sdh - 0.05*entropy` | `:439` | `:441` | **NYATA** |
| Static | — | — | — | **TIDAK ADA MODEL** (§4.1) |

Detail yang ikut terverifikasi nyata:

- Gradient clipping `clip_grad_norm_(..., max_norm=0.5)` pada `:360`, `:376`, `:407`, `:435`, `:440`.
- `LinearLR` decay 3e-4 → 1e-5 pada kelima optimizer, di-`step()` pada akhir tiap epoch.
- Target network sync tiap 10 epoch untuk DQN dan DDQN.
- DDQN adalah double-Q yang sah: jaringan online memilih aksi (`ddqn_model(next_states).max(1)[1]`), target network mengevaluasi (`ddqn_target(next_states).gather(1, next_actions)`).

**Kode mati yang tidak boleh ikut di-port:** cell 2 berisi `memory = deque(maxlen=10000)` dan `def optimize_model(...)` dengan `loss.backward()` pada `:121`. Tidak ada yang pernah menambah isi `memory`, dan `optimize_model` tidak pernah dipanggil. Sudah dikecualikan dari `scripts/sweep.py`.

### 1.1 Kualifikasi penting

Training loop nyata, tetapi **sifatnya offline batch TD learning pada dataset tetap**, bukan RL dengan rollout:

- `batch = train_df.sample(batch_size)` — sampling dari dataset, bukan interaksi dengan environment.
- `dones = torch.zeros(...)` — tidak pernah ada terminal state.
- Tidak ada replay buffer insertion, tidak ada eksplorasi, tidak ada action selection saat training.

Konsekuensinya sudah dicatat di `00-contamination-audit.md` §4.2: reward tidak mengandung aksi, sehingga advantage tidak membawa informasi aksi. Loop-nya berjalan; yang dipelajarinya yang bermasalah.

---

## 2. Output CSV yang pernah dihasilkan notebook

Seluruh file di `Reinforcement Learning/revision/` bertanggal **2026-09-22 08:58**. Angka itu adalah waktu checkout dari `git pull`, bukan waktu eksekusi notebook — seluruh file masuk dalam satu commit sehingga mtime-nya seragam dan tidak informatif. Tanggal eksekusi sebenarnya tidak terekam di mana pun; tidak ada metadata run di repo. Ini salah satu alasan Fase 4 mewajibkan sidecar `.json`.

| File | Baris | Ditulis oleh |
|---|---|---|
| `training_convergence_{DQN,DDQN,PPO_Standard,Proposed_(SDH-PPO)}.csv` | 2000 | `allModel4.ipynb:464` |
| `viz_detail_{DQN,DDQN,PPO_Standard,Proposed_(SDH-PPO),Static}.csv` | 3000 | `allModel4.ipynb:556` |
| `model_comparison_results.csv` | 5 | `allModel4.ipynb:603` |
| `sla_violation_report.csv` | 5 | `allModel4.ipynb:761` |

Tiga file **tanpa provenans**: `viz_detail_Proposed_(Hard_Mask).csv`, `..._(Soft_Mask).csv`, `..._(Sigmoid_Mask).csv`. Tidak ada satu pun dari keempat notebook yang menghasilkannya — kemungkinan sisa dari run ablation yang notebooknya sudah tertimpa.

Tiga file **status diragukan**: `delay_tracking_plot_P{1,2,4}.csv`. Cell 8 tidak memuat `to_csv` sama sekali, sehingga file ini berasal dari versi notebook yang mengandung offset `data_viz = data_viz + 0.6` (lihat `00-contamination-audit.md` §5.9).

`final/sla_violation_report.csv` bertanggal **2026-03-04** — inilah keluaran `allModel1.ipynb` yang memfabrikasi, dan sumber angka Abstract yang masih hidup di paper.

---

## 3. Konversi ke CLI

`scripts/sweep.py`. Logika training **tidak diubah sama sekali** — kelas jaringan, loss, urutan optimizer, scheduler, dan rumus evaluasi ditranskripsi apa adanya.

```
python scripts/sweep.py --algo {dqn,ddqn,ppo,sdhppo,static} \
                        --arm {full,no_mask,no_dueling,no_aug} \
                        --seed N --steps 2000 --out results/raw \
                        [--device {auto,cpu,cuda}] [--fair-eval]
```

### 3.1 Keputusan desain

**Reproduksi RNG.** Di notebook, keempat algoritma dilatih dalam satu loop dan berbagi batch yang sama tiap epoch. Agar run per-algoritma menghasilkan angka identik dengan run gabungan, `build_models()` tetap **mengonstruksi seluruh jaringan dalam urutan asli** (DQN, DQN-target, DDQN, DDQN-target, PPO, SDH-actor, SDH-critic) sehingga aliran RNG torch cocok, lalu hanya algoritma yang diminta yang di-`step()`. Sedikit mubazir, tapi setia.

**Konstanta bias dinaikkan jadi flag, bukan diperbaiki.** Nilai yang sebelumnya hardcoded kini menjadi argumen CLI dengan **default yang mereproduksi notebook persis**:

| Flag | Default | Catatan |
|---|---|---|
| `--k-p4-proposed` | `0.15` | Hanya berlaku untuk `--algo sdhppo` |
| `--k-p4-other` | `0.10` | Untuk seluruh baseline |
| `--k-p1`, `--k-p2` | `0.1` | Sama untuk semua |
| `--dqn-bins` | `0.0,0.1,-0.1` | Sumber ketimpangan aksi 10× |
| `--safety-margin` | `0.5` | Ambang mask |
| `--mask-gain` | `2.0` | Gain proporsional mask |
| `--fair-eval` | off | Memaksa `k_p4_proposed = k_p4_other` |

Rasionalnya: bias berpindah dari kode tersembunyi ke konfigurasi yang terlihat dan tercatat di metadata tiap run, tanpa mengubah perilaku default. Keputusan untuk benar-benar mengubahnya adalah keputusan protokol (Fase 2), bukan keputusan implementasi.

**`--audit`** mencetak daftar tujuh cacat yang sengaja dipertahankan, dan daftar yang sama disalin ke tiap file metadata.

### 3.2 Struktur keluaran

```
results/raw/{algo}_{arm}_seed{N}_train.csv   per-epoch: epoch, loss, loss_critic,
                                             loss_actor, entropy, mu_mean, sigma,
                                             q_mean, batch_reward_mean
results/raw/{algo}_{arm}_seed{N}_eval.csv    per-test-sample: sample_idx, action,
                                             action_raw, raw_p1/p2/p4, d1/d2/d4
results/raw/{algo}_{arm}_seed{N}.json        metadata lengkap
```

Sesuai aturan work order, CSV memuat **data mentah, bukan metrik teragregasi**. Tidak ada violation rate, tidak ada rata-rata. Agregasi seluruhnya menjadi tugas `scripts/make_tables.py` di Fase 5 sehingga dapat diaudit dan dihitung ulang.

Dua kolom diagnostik ditambahkan yang tidak ada di notebook, keduanya mentah dan tidak memengaruhi perhitungan:

- `action_raw` — aksi sebelum mask diterapkan. Memungkinkan pengukuran langsung seberapa sering mask benar-benar aktif.
- `mu_mean`, `sigma`, `entropy` per epoch — memungkinkan deteksi saturasi `tanh` yang menjadi penyebab angka Table IV.

Metadata `.json` memuat: seluruh argumen CLI, `k_p4_used` efektif, commit hash git, waktu mulai/selesai UTC, durasi train dan eval terpisah, versi Python/torch/numpy/pandas, device, nama GPU, platform, processor, dan daftar cacat yang dipertahankan.

### 3.3 Bukti kesetiaan port — **TERVERIFIKASI**

Klaim "port setia" tidak boleh dipercaya begitu saja, jadi diuji angka. `scripts/check_fidelity.py` menghitung ulang metrik Table IV dari keluaran mentah `sweep.py` lalu membandingkannya dengan `revision/sla_violation_report.csv` milik notebook.

```
python scripts/check_fidelity.py
```

Hasil dengan `--seed 42 --steps 2000` pada kelima algoritma:

```
worst abs diff 0.0333 (tol 0.05); 0/30 metrics outside tolerance
```

Seluruh **30 metrik** (5 algoritma × 6 metrik) cocok. Selisih terbesar 0.0333 seluruhnya berasal dari pembulatan notebook sendiri — laporan notebook menulis persentase dengan 1 desimal (`13.2%`) sedangkan port menghitung `13.1667%`. Toleransi 0.05 adalah granularitas pembulatan itu, bukan ambang yang dilonggarkan agar lulus.

Contoh sampel:

| Algoritma | Metrik | Notebook | Port | Selisih |
|---|---|---|---|---|
| Proposed (SDH-PPO) | P1 Avg (ms) | 5.46 | 5.4629 | 0.0029 |
| Proposed (SDH-PPO) | P4 Avg (ms) | 5.87 | 5.8657 | 0.0043 |
| Proposed (SDH-PPO) | P4 Viol (%) | 0.00 | 0.0000 | 0.0000 |
| DDQN | P4 Avg (ms) | 6.93 | 6.9298 | 0.0002 |

Konsekuensinya: `sweep.py` adalah pengganti sah untuk notebook, dan seluruh temuan Fase 0 kini dapat direproduksi dari baris perintah.

**Konfirmasi saturasi.** Keluaran run mencetak `mean|action| = 0.9999` untuk SDH-PPO. Ini membuktikan langsung dugaan audit §3.1: aktor jenuh ke `tanh ≈ 1.0`, sehingga `6.903 × (1 − 0.15 × 1.0) = 5.868` — persis angka Table IV. Table IV memang rumus tertutup, bukan hasil belajar. Sekarang terbukti dari data run, bukan dari pembacaan kode.

---

## 4. Yang masih hilang sebelum sweep bisa jalan

Ini butir yang memerlukan keputusan, bukan implementasi.

### 4.1 Definisi static baseline — **HILANG**

Tidak ada kebijakan statis di kode. Yang ada:

```python
if m == 'Static':
    action = row['action_continuous']   # Static tetap pada baseline offline
```

Ini **memutar ulang aksi yang tercatat di log**, yaitu `(rate_{t+1} − rate_t)/rate_t` dari trace SDN asli. Dua masalah:

1. Ini behavior-policy replay, bukan alokasi statis. Namanya keliru dan reviewer akan menangkapnya.
2. Nilainya mencapai **+6.32** dan tidak di-clip, sedangkan arm lain dibatasi `tanh ∈ [−1, 1]`. Kolom delay-nya tidak sebanding dengan arm mana pun.

**Butuh keputusan:** definisikan baseline statis yang sebenarnya (misal `action = 0` konstan, atau policing rate tetap pada nilai nominal SLA), tulis pseudocode-nya, dan putuskan apakah behavior-replay tetap dipertahankan sebagai arm terpisah bernama jujur (misal "Logged Policy").

### 4.2 Jumlah bin diskretisasi DQN/DDQN — **ADA TAPI TIMPANG**

Dua tahap. Preprocessing membagi aksi kontinu menjadi **3 bin** dengan deadband ±0.05:

```python
if   action_cont >  0.05: action_disc = 1   # Increase
elif action_cont < -0.05: action_disc = 2   # Decrease
else:                     action_disc = 0   # Maintain
```

Distribusi hasilnya: `1: 7010`, `2: 7009`, `0: 980`.

Saat evaluasi dipetakan balik ke `{0: 0.0, 1: +0.1, 2: −0.1}`. Inilah sumber ketimpangan 10×: DQN maksimum ±0.1, arm kontinu ±1.0.

**Butuh keputusan:** berapa bin, dan pada rentang berapa. Agar adil, bin harus menjangkau rentang aksi yang sama dengan arm kontinu (misal 9 bin dari −1.0 sampai +1.0 dengan langkah 0.25, atau 21 bin langkah 0.1). Ini mengubah `action_discrete` di dataset, sehingga preprocessing harus dijalankan ulang.

### 4.3 Protokol evaluasi — **SEBAGIAN ADA**

Yang sudah ada dan sah: `.eval()` dipanggil, `torch.no_grad()` dipakai, kebijakan deterministik (`mu` dipakai, `sigma` dibuang), test split sama untuk semua algoritma.

Yang hilang:

- **Jumlah episode / panjang window tidak terdefinisi.** Evaluasi menilai 3000 baris test secara independen, satu per satu. Tidak ada rollout, tidak ada episode, tidak ada dinamika beruntun. "Window 100 terakhir" yang dipakai Fig. 4 tidak dijustifikasi di mana pun.
- **Test split tidak stratified** (`train_test_split(df, test_size=0.2, random_state=SEED)`). `allModel1` menggunakan stratifikasi; `allModel4` tidak.
- **Definisi violation rate tidak tunggal.** Kolom "Total Viol" saat ini adalah `(v1+v2+v4)/3`, rata-rata tak-berbobot dari tiga persentase — bukan tingkat pelanggaran agregat dan tanpa interpretasi operasional.

**Butuh keputusan:** definisi tunggal violation rate untuk seluruh arm, dan apakah evaluasi tetap per-sampel atau menjadi rollout berepisode.

### 4.4 Epsilon = 0 saat evaluasi — **TIDAK BERLAKU**

Tidak ada epsilon sama sekali di notebook. Tidak ada ε-greedy, tidak ada jadwal eksplorasi, tidak ada gate `np.random.rand()`. Satu-satunya token `epsilon` adalah parameter clip PPO (`:160`, `:163`, `:399`, `:429`).

Ini konsekuensi desain offline: agen tidak pernah memilih aksi saat training, sehingga tidak ada yang perlu dieksplorasi. Saat evaluasi, Q-network memakai `argmax()` telanjang dan aktor memakai mean deterministik. **Evaluasi sudah deterministik-greedy; tidak ada yang perlu di-nol-kan.**

Catatan: `sdh_critic.eval()` tidak dipanggil di notebook. Tidak berdampak (tidak ada dropout/batchnorm), tapi sudah dirapikan di `sweep.py`.

### 4.5 Arm `no_aug` — **TERBLOKIR, BUTUH DATA**

Arm ini memerlukan dataset hasil preprocessing yang **hanya berisi data riil**. Dataset itu tidak ada.

`drl_preprocessed_final.csv` (14.999 baris) dibangun dari `synthetic_15k_complete_final.csv`, yaitu keluaran WGAN-GP. Data riil yang terukur ada di `dataset_dqn_rich.csv` — hanya **1.022 baris**, dan formatnya bermasalah: delimiter titik-koma dengan seluruh header terbungkus satu pasang tanda kutip ganda, sehingga `pd.read_csv` default menghasilkan satu kolom.

`sweep.py --arm no_aug` saat ini keluar dengan pesan yang menjelaskan hal ini, bukan diam-diam menjalankan arm yang salah.

**Butuh keputusan:** jalankan ulang Preprocessing pada 1.022 baris riil (dengan `sep=';'` dan penanganan kutip), lalu terima bahwa arm ini memiliki 14× lebih sedikit data — yang membuat perbandingannya tidak setara budget. Alternatifnya, subsample dataset augmented ke 1.022 baris sebagai kontrol ukuran-data, sehingga efek augmentasi terpisah dari efek jumlah sampel.

### 4.6 Arm `no_dueling` — **BISA JALAN, TAPI MUNGKIN TIDAK BERMAKNA**

Sudah diimplementasikan (`PlainCritic`, lebar dan kedalaman sama, satu value head). Tetapi seperti dicatat di audit §5.2, `DuelingCritic` asli sudah setara MLP dua-kepala karena `action_dim = 1` membuat dekomposisi dueling hampa. Arm ini kemungkinan besar mengukur selisih mendekati nol — dan itu justru hasil yang informatif: ia membuktikan klaim "duel layer" di paper tidak memiliki efek.

### 4.7 Arm `no_mask` — **BISA JALAN, EFEK DIPERKIRAKAN ≈ NOL**

Sudah diimplementasikan. Karena mask aktif pada hanya 0,11% baris (audit §5.1), selisihnya diperkirakan mendekati nol. Kolom `action_raw` di CSV keluaran memungkinkan pengukuran langsung frekuensi aktivasi mask, sehingga klaim ini dapat diverifikasi angka, bukan diperdebatkan.

### 4.8 Lingkungan komputasi — **SUDAH SIAP**

Tidak ada venv di repo saat audit. Kini dibuat `.venv/` (Python 3.13.5) berisi torch CUDA, pandas, scikit-learn, scipy, matplotlib. GPU terdeteksi: NVIDIA GeForce RTX 4060 Laptop, 8 GB, driver CUDA 13.4.

**Terukur: CPU lebih cepat daripada GPU untuk beban ini.** SDH-PPO, 2000 step, seed 42:

| Device | Train | Eval | Total |
|---|---|---|---|
| CUDA (RTX 4060) | 23.3 s | 1.9 s | 25.2 s |
| CPU | 14.3 s | 0.6 s | **14.9 s** |

GPU **1,7× lebih lambat**. Penyebabnya jaringan terlalu kecil (12 → 256 → 128, batch 64): waktu habis di overhead kernel launch dan transfer host-device, bukan di komputasi. Untuk sweep penuh, `--device cpu` adalah pilihan yang benar. Flag `--device` tetap ada agar keputusan ini dapat diukur ulang, bukan diasumsikan.

Catatan determinisme: aliran RNG torch berbeda antara CPU dan CUDA, sehingga seed yang sama pada device berbeda tidak menghasilkan bobot yang identik. Satu device harus dipilih untuk seluruh kampanye dan dicatat di protokol. Uji fidelitas §3.3 dijalankan pada CUDA.

Waktu per run (CPU, 2000 step): DQN ~14 s, DDQN ~17 s, PPO ~17 s, SDH-PPO ~15 s, Static ~0,1 s.

`2requirements.txt` adalah file dependensi RL (`requirements.txt` di root adalah stack YOLO/Raspberry Pi dan tidak berkaitan). Pin di dalamnya (`torch==2.2.1`, `numpy==1.26.4`) tidak memiliki wheel untuk Python 3.13, sehingga `.venv` memakai versi yang lebih baru. Perbedaan versi terekam di metadata tiap run.

---

## 5. Ringkasan untuk STOP 2

Sudah selesai:

- Training loop terverifikasi nyata untuk keempat algoritma, dengan `path:baris` (§1).
- Output lama terinventarisasi, termasuk tiga file tanpa provenans dan tiga file yang diragukan (§2).
- `scripts/sweep.py` selesai — port setia, bias dinaikkan jadi flag terlihat, keluaran mentah + metadata (§3).
- **Kesetiaan port terbukti angka**: 30/30 metrik cocok dengan notebook dalam batas pembulatannya sendiri, via `scripts/check_fidelity.py` (§3.3).
- Saturasi `tanh ≈ 1.0` terkonfirmasi dari data run, membuktikan Table IV adalah rumus tertutup (§3.3).
- Lingkungan komputasi siap. Terukur: CPU 1,7× lebih cepat daripada GPU untuk beban ini (§4.8).

Butuh keputusanmu sebelum Fase 2 dapat ditulis:

| # | Butir | Pertanyaan |
|---|---|---|
| 1 | Static baseline (§4.1) | Definisi apa yang dipakai? Apakah logged-replay dipertahankan sebagai arm terpisah dengan nama jujur? |
| 2 | Bin DQN/DDQN (§4.2) | Berapa bin dan rentang berapa? Ini mengharuskan preprocessing dijalankan ulang. |
| 3 | Violation rate (§4.3) | Definisi tunggal yang mana? Apakah evaluasi tetap per-sampel atau menjadi rollout berepisode? |
| 4 | Arm `no_aug` (§4.5) | Jalankan ulang preprocessing pada 1.022 baris riil, atau subsample data augmented sebagai kontrol ukuran? |
| 5 | Koefisien `k` (§3.1) | Kapan `--fair-eval` menjadi default? Ini keputusan protokol Fase 2, bukan implementasi. |

Dan satu butir yang lebih besar dari kelimanya, terbawa dari Fase 0: **selama environment tetap berupa rumus tertutup `d = raw × (1 − k·a)` yang monoton dan tanpa biaya, sweep berapa pun seed-nya tidak menghasilkan perbandingan yang bermakna.** Menyetel kelima butir di atas membuat sweep *adil*, tetapi belum membuatnya *bermakna*. Keputusan arah environment masih terbuka.
