# Fase 0 — Audit Kontaminasi

Tanggal audit: 2026-09-24
Ruang lingkup: seluruh repo + `revisi/paper/main.tex`

Dokumen ini hanya mencatat temuan. Tidak ada perbaikan yang dilakukan pada fase ini.

---

## Ringkasan eksekutif

Kontaminasi terjadi pada **tiga tingkat berbeda**, dan hanya tingkat pertama yang sesuai dugaan awal (`np.random` yang di-hardcode).

| Tingkat | Sifat | Dampak |
|---|---|---|
| 1. Fabrikasi murni | `np.random.uniform` menghasilkan metrik langsung | Angka Abstract + Kesimpulan |
| 2. Evaluator dicurangi | Angka dihitung, tapi rumusnya dikunci per nama algoritma | Seluruh Table IV |
| 3. Tidak ada environment | Reward tidak mengandung aksi; delay adalah rumus tertutup | Seluruh premis eksperimen |

Implikasi utama: **menjalankan sweep multi-seed pada kode saat ini tidak menghasilkan angka jujur.** Sweep hanya akan mereproduksi rumus tertutup yang sama sebanyak N seed, lalu membungkusnya dengan confidence interval dan p-value — sehingga terlihat lebih rigor padahal lebih menyesatkan daripada kondisi sekarang.

---

## 1. Peta angka di `main.tex`

Penomoran aktual di paper berbeda dari penomoran pada work order. Tidak ada Table V.

| Label | Nomor tampil | Isi |
|---|---|---|
| `tab:1` | Table I | Matriks perbandingan SOTA (checkmark, tanpa metrik) |
| `tab:2` | Table II | Hyperparameter training |
| `tab:2b` | Table III | Hyperparameter WGAN-GP |
| `tab:3` | **Table IV** | **Satu-satunya tabel hasil** |

### 1.1 Tabel provenans

| Lokasi di main.tex | Angka | Asal-usul | Status |
|---|---|---|---|
| `:25` Abstract | total violation **27.3%** | `final/sla_violation_report.csv`, dihasilkan `final/allModel1.ipynb:176-194` via `np.random` | **FABRIKASI** |
| `:25` Abstract | perbaikan **47.6%** | Turunan aritmetik dari angka fabrikasi di atas | **FABRIKASI** |
| `:25` Abstract | P4 **0.0%**, latensi **2.71 ms** | `np.random.uniform(2.0, 3.4)` dengan komentar "Konsisten di bawah SLA 3.5" | **FABRIKASI** |
| `:513` Kesimpulan | **27.3%**, **47.6%**, **2.71 ms** | Identik dengan Abstract, sumber sama | **FABRIKASI** |
| `:513` Kesimpulan | "≈2× epoch untuk konvergen" | Artefak dua konstanta peluruhan yang diketik tangan: `0.5*exp(-i/500)` vs `0.8*exp(-i/400)` | **FABRIKASI** |
| `:484-488` Table IV | seluruh 35 sel | `revision/sla_violation_report.csv`, dihasilkan `revision/allModel4.ipynb:761` | **TERKONTAMINASI STRUKTURAL** — dihitung dari training nyata, tapi lewat evaluator yang dicurangi (§3) |
| `:491` Section IV.B | 10.3 / 47.2 / 77.0 / 78.9 / 80.0% | Turunan aritmetik dari Table IV | **TERKONTAMINASI STRUKTURAL** |
| `:491` Section IV.B | P4 0.0% @ 5.87 ms; P1 1.5%; P2 29.5–51.9% | Turunan dari Table IV | **TERKONTAMINASI STRUKTURAL** |
| `:387-405` Table II | hyperparameter training | Cocok dengan literal di `allModel4.ipynb` cell 4 | **TERVERIFIKASI** (konfigurasi, bukan hasil) |
| `:412-425` Table III | hyperparameter WGAN-GP | Cocok dengan `DataAugmentation.ipynb` | **TERVERIFIKASI** (konfigurasi, bukan hasil) |
| `:430-437` Section IV.A | — | Deskripsi kualitatif t-SNE, tanpa angka | **TERVERIFIKASI** (tidak ada klaim numerik) |

### 1.2 Kontradiksi internal paper

Abstract dan Kesimpulan melaporkan **27.3% / 2.71 ms**. Table IV melaporkan **10.3% / 5.87 ms**. Kedua angka berasal dari dua notebook berbeda, dan Abstract tidak pernah diperbarui setelah re-run revisi. Paper saat ini bertentangan dengan dirinya sendiri dan akan langsung terlihat oleh reviewer.

Catatan penting: **kontradiksi ini tidak boleh diperbaiki dengan menyalin angka Table IV ke Abstract.** Table IV sendiri terkontaminasi (§3). Menyelaraskannya hanya mencuci angka yang tetap tidak valid.

---

## 2. Tingkat 1 — Fabrikasi murni

### `Reinforcement Learning/final/allModel1.ipynb:176-194`

Model dan optimizer dibangun, lalu tidak pernah dipakai. Tidak ada forward pass, tidak ada loss, tidak ada `.backward()`, tidak ada `.step()` di seluruh file.

```python
for i in range(epochs):
    batch = train_data.sample(64)
    # Simulasi training dan penarikan performa...
    base_r = np.mean(batch['reward'].values)
    if 'Proposed' in name:
        r  = base_r + (i/epochs)*0.4 + np.random.normal(0, 0.01) + 0.1
        l  = max(0.01, 0.5 * np.exp(-i/500) + np.random.normal(0, 0.001))
        d4 = np.random.uniform(2.0, 3.4)   # Konsisten di bawah SLA 3.5
    elif 'Static' in name:
        r, l, d4 = base_r - 0.2, 0.0, np.random.uniform(3.0, 4.5)
    else:
        r  = base_r + (i/epochs)*0.25 + np.random.normal(0, 0.05)
        l  = max(0.05, 0.8 * np.exp(-i/400) + np.random.normal(0, 0.01))
        d4 = np.random.uniform(2.5, 4.2)
    log['delay_p1'].append(np.random.uniform(10, 14))
    log['delay_p2'].append(np.random.uniform(8, 11))
    log['delay_p4'].append(d4)
    log['violation'].append(1 if d4 > SLA_P4 else 0)
```

Bukti niat, bukan sekadar kelalaian:

1. Komentar pada baris `d4` menyatakan rentang `(2.0, 3.4)` dipilih agar **seluruhnya** di bawah threshold 3.5 — sehingga P4 violation dijamin tepat 0.0%.
2. Baseline diberi rentang `(2.5, 4.2)` yang menyeberangi threshold, sehingga dijamin melanggar.
3. Konstanta peluruhan loss dibedakan (`/500` untuk Proposed vs `/400` untuk baseline) — inilah satu-satunya sumber klaim konvergensi di Kesimpulan.
4. Proposed mendapat bonus reward `+0.1` dan slope `0.4` vs `0.25` untuk baseline.

Output: `final/sla_violation_report.csv` (ditulis pada `:384`). Kolom P1/P2 pada file itu (11.98 / 9.5 ms) adalah nilai tengah `np.random.uniform(10,14)` dan `(8,11)`, tidak berhubungan sama sekali dengan angka revisi (5.46 / 64.36).

**Status: notebook ini harus dikarantina. Tidak ada satu pun keluarannya yang layak masuk paper.**

---

## 3. Tingkat 2 — Evaluator dicurangi

`revision/allModel4.ipynb` memiliki training loop yang **asli**: forward pass nyata, `nn.MSELoss()`, `loss.backward()`, `clip_grad_norm_`, `opt.step()`, LR scheduler. Terkonfirmasi untuk DQN (`:359-361`), DDQN (`:375-377`), PPO (`:406-408`), SDH-PPO (`:434-441`).

Namun angka Table IV tidak dihasilkan oleh proses belajar itu. Angka tersebut berasal dari evaluator pada cell 5, yang memiliki tiga bias struktural independen — masing-masing sudah cukup untuk menentukan ranking akhir.

### 3.1 Koefisien dikunci per nama algoritma — `allModel4.ipynb:542-548`

```python
d1 = raw_p1 * (1 - 0.1 * action)
d2 = raw_p2 * (1 - 0.1 * action)

if m == 'Proposed (SDH-PPO)':
    d4 = raw_p4 * (1 - 0.15 * action)
else:
    d4 = raw_p4 * (1 - 0.10 * action)
```

Metode yang diusulkan menerima daya-aksi 50% lebih besar pada P4 dibanding seluruh baseline, ditentukan lewat perbandingan string nama. Ini bukan properti algoritma; ini konstanta di dalam environment.

**Verifikasi aritmetik.** Mean dataset: `raw_delay_p1 = 6.071`, `raw_delay_p4 = 6.903`. Aktor SDH-PPO jenuh ke `tanh ≈ +1.0`.

- P1: `6.071 × (1 − 0.10 × 1.0) = 5.464` → Table IV melaporkan **5.46** ✓
- P4: `6.903 × (1 − 0.15 × 1.0) = 5.868` → Table IV melaporkan **5.87** ✓

Table IV adalah rumus tertutup yang dievaluasi pada aksi jenuh. Bukan hasil pembelajaran.

### 3.2 Ruang aksi timpang 10× — `allModel4.ipynb:530-534`

```python
elif m in ['DQN', 'DDQN']:
    model = dqn_model if m == 'DQN' else ddqn_model
    action_idx = model(st_tensor).argmax().item()
    mapping = {0: 0.0, 1: 0.1, 2: -0.1}
    action = mapping.get(action_idx, 0.0)
```

DQN/DDQN dibatasi pada aksi maksimum ±0.1. PPO dan SDH-PPO menghasilkan `tanh ∈ [−1, 1]`. Di bawah rumus `d = raw × (1 − k·a)`, DQN secara struktural tidak mungkin bersaing, sebaik apa pun ia belajar. Nilai terukur `DQN P1 Avg = 6.07` persis sama dengan baseline mentah 6.071, yang berarti DQN selalu memilih bin 0 (Maintain).

### 3.3 Kapasitas model tidak disetarakan — `allModel4.ipynb:140-196`

| Arm | Aktor | Kritik |
|---|---|---|
| Proposed (SDH-PPO) | 256 → 128 | 256 |
| PPO Standard | 64 → 64 | 64 |
| DQN | 64 → 64 | — |
| DDQN | 128 (dueling) | — |

Klaim keunggulan arsitektur tercampur dengan perbedaan jumlah parameter.

### 3.4 Baseline "Static" bukan static — `allModel4.ipynb` cell 5

```python
if m == 'Static':
    action = row['action_continuous']   # Static tetap pada baseline offline
```

Ini memutar ulang aksi yang tercatat di log, bukan alokasi statis. Nilainya mencapai 6.32 dan tidak di-clip, sementara arm lain dibatasi [−1, 1] — sehingga kolom delay-nya tidak sebanding. Istilah "Static" di paper adalah misnomer.

---

## 4. Tingkat 3 — Tidak ada environment

Ini masalah terdalam dan tidak dapat diperbaiki dengan menyetel hyperparameter.

### 4.1 Transisi tidak bergantung pada aksi

`drl_preprocessed_final.csv` berisi tuple (state, action, reward, next_state) tetap dari trace log. `next_state` diambil dari baris berikutnya di dataset; ia tidak merespons aksi agen. `dones` bernilai 0 selamanya. Tidak ada rollout, tidak ada replay buffer, tidak ada eksplorasi.

### 4.2 Reward tidak mengandung aksi — `Preprocessing.ipynb` cell 0

```python
def calculate_sdh_reward(row):
    penalty_p4 = 10 * sigmoid_penalty(row['delay_ms_p4'], threshold=SLA_DELAY_P4)
    penalty_p1 =  5 * sigmoid_penalty(row['delay_ms_p1'], threshold=SLA_DELAY_P1)
    penalty_p2 =  5 * sigmoid_penalty(row['delay_ms_p2'], threshold=SLA_DELAY_P2)
    r_throughput_p2 = 5 * np.clip(row['rx_mbps_p2'] / TARGET_THROUGHPUT_P2, 0, 1)
    total_drop = row.get('drop_p1', 0) + row.get('drop_p2', 0) + row.get('drop_p4', 0)
    p_drop = np.clip(total_drop, 0, 5)
    return r_throughput_p2 - penalty_p4 - penalty_p1 - penalty_p2 - p_drop
```

Reward adalah fungsi murni dari baris log berikutnya. Variabel aksi tidak muncul di dalamnya. Konsekuensinya, advantage `A = r + γV(s′) − V(s)` tidak membawa informasi apa pun tentang aksi, sehingga gradien kebijakan `A·∇log π(a|s)` hanya mendorong probabilitas aksi yang tercatat di log, ditimbang residual state-value. Ini bukan PPO, dan juga bukan offline RL yang benar — tidak ada importance weighting, tidak ada mekanisme konservatif (CQL/BCQ).

### 4.3 Delay saat evaluasi tidak diukur maupun disimulasikan

Rumus `d = raw × (1 − k·a)` bersifat monoton terhadap aksi dan **tanpa biaya**. Menaikkan policing rate satu slice tidak mengambil kapasitas dari slice lain. Karena itu kebijakan optimal bersifat sepele: `a = +1` selalu. Tidak ada trade-off, sehingga tidak ada yang bisa dipelajari — dan tidak ada dasar untuk membedakan satu algoritma dari yang lain.

---

## 5. Tingkat 4 — Bug yang mencabut klaim spesifik paper

### 5.1 Safety layer praktis tidak pernah aktif — `allModel4.ipynb:203-233`

```python
def get_action_with_mask(state, raw_action, thresholds):
    delay_p4 = state[10]
    limit_p4 = thresholds['P4']
    safety_margin = 0.5
    if delay_p4 > (limit_p4 * safety_margin):
        ...
```

`state[10]` adalah nilai **z-score** (StandardScaler di `Preprocessing.ipynb`), sedangkan `thresholds['P4']` bernilai **7.0 milidetik**. Cabang ini aktif ketika `z > 3.5`.

Terukur pada 14.999 baris: `max(state[:,10]) = 4.234`, dan proporsi baris dengan `state[:,10] > 3.5` adalah **0.11%**. Cabang fairness lebih parah: `state[2] > 6.0` sementara `max(state[:,2]) = 3.473` — **tidak pernah aktif**; `state[6] > 70.0` sementara `max = 4.501` — **tidak pernah aktif**.

Safety layer adalah no-op pada 99,89% test set. Klaim safety-margin di Abstract tidak didukung kode. Konsekuensi untuk Fase 3: arm ablation "tanpa safety layer" akan mengukur perbedaan mendekati nol.

Catatan tambahan: komentar mengatakan intervensi dimulai pada "85% dari batas SLA", tetapi `safety_margin = 0.5` (50%). Komentar dan kode tidak cocok.

### 5.2 Dueling critic hampa — `allModel4.ipynb:181-193`

```python
class DuelingCritic(nn.Module):
    def __init__(self, input_dim):
        self.base       = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.value_head = nn.Linear(256, 1)
        self.adv_head   = nn.Linear(256, 1)
    def forward(self, x):
        x = self.base(x)
        v = self.value_head(x)
        a = self.adv_head(x)
        return v + (a - a.mean())
```

Dua cacat. Pertama, `adv_head` menghasilkan **1** unit, dan `a.mean()` tanpa argumen `dim=` merata-ratakan seluruh batch, bukan seluruh aksi. Kedua, dan lebih mendasar: dengan `action_dim = 1`, dekomposisi dueling `Q = V + (A − mean A)` hampa secara definisi — tidak ada beberapa aksi untuk dibandingkan. Modul ini secara fungsional adalah MLP dua-kepala yang dijumlahkan. Istilah "duel layer" di paper tidak dapat dipertahankan.

`DuelingDQN` (`:125-138`) untuk arm DDQN adalah dueling yang sah (`advantage.mean(dim=1, keepdim=True)` dengan `action_dim = 3`).

### 5.3 Clip PPO tidak pernah aktif — `allModel4.ipynb:394-396`

```python
dist_ppo = torch.distributions.Normal(mu_ppo, sigma_ppo)
current_log_probs_ppo = dist_ppo.log_prob(actions_continuous)
old_log_probs_ppo = current_log_probs_ppo.detach()
```

`old` diambil dari `current` yang sama pada iterasi yang sama, sehingga `ratio = exp(current − old) ≡ 1.0` secara numerik pada setiap iterasi. Clip `[1−ε, 1+ε]` tidak pernah aktif.

Klarifikasi teknis yang penting: gradien **tetap mengalir**. Karena `old` di-detach, `d(ratio)/dθ = ratio · ∇log π ≠ 0`, dan pada `ratio = 1.0` nilai ini berada di interior clip sehingga tidak terpotong. Yang terjadi bukan gradien nol, melainkan degenerasi menjadi **vanilla policy gradient (setara A2C satu-epoch)**. Implikasinya: hyperparameter `epsilon = 0.2` di Table II adalah parameter mati, dan penyebutan "PPO clip" di paper tidak menggambarkan yang dijalankan kode.

### 5.4 Threshold training ≠ threshold evaluasi

| Sumber | P1 | P2 | P4 |
|---|---|---|---|
| Reward (`Preprocessing.ipynb`) | 12.0 | 10.0 | 3.5 |
| Evaluasi (`allModel4.ipynb` cell 0 `:39`) | 6.0 | 70.0 | 7.0 |
| Mean dataset terukur | 6.071 | 71.599 | 6.903 |

Threshold evaluasi ditetapkan praktis pada median dataset, yang menjamin baseline melanggar sekitar 50% **by construction**. Agen dilatih untuk satu objektif lalu dinilai dengan objektif yang berbeda. Perbedaan ini diungkap di `main.tex:446`, tetapi pemilihan nilainya tidak dibenarkan di mana pun.

### 5.5 Target aksi di luar jangkauan representasi

`action_continuous` pada dataset berkisar **[−0.863, +6.320]** (mean 0.321, std 1.079), sedangkan seluruh aktor menghasilkan `tanh ∈ [−1, 1]`. Sebagian besar distribusi aksi log berada di luar himpunan yang dapat direpresentasikan kebijakan.

### 5.6 Metrik agregat tidak sahih — `allModel4.ipynb` cell 5

```python
'Avg_Total_Viol': round((v1+v2+v4)/3, 2)
```

Kolom "Total Viol (%)" adalah rata-rata tak-berbobot dari tiga persentase, bukan tingkat pelanggaran agregat. Angka ini tidak memiliki interpretasi operasional.

### 5.7 Kritik SDH-PPO divergen

`revision/training_convergence_Proposed_(SDH-PPO).csv`: loss epoch 1 = 246.45, epoch 2000 = 486.01, puncak 559.65 pada epoch 1999. Kritik tidak konvergen, tetapi hal ini tidak disebut di paper.

### 5.8 Kurva reward pada Fig. 5–8 bukan progres belajar

```python
training_results[...]['reward'].append(rewards.mean().item())
```

Yang dicatat adalah rata-rata reward dari batch **dataset**, bukan reward yang diperoleh kebijakan. Nilainya identik secara ekspektasi untuk keempat algoritma dan sepenuhnya independen dari kebijakan. Kurva "Reward Progress" pada Fig. 5–8 adalah noise dataset yang datar (sekitar −15.2).

Kolom `Loss` pada CSV yang sama memang nyata. Jadi Fig. 5–8 **setengah terkontaminasi**: sumbu loss sah, sumbu reward tidak.

### 5.9 Offset kosmetik pada figure — `revision/add_csv_to_plots.py:30`

```python
old_data_viz = "data_viz = data_viz + 0.6 \n            # ---..."
```

Script ini mencari string `data_viz = data_viz + 0.6` sebagai jangkar edit — sebuah offset konstan +0.6 ms yang ditambahkan ke kurva delay sebelum dirender. String tersebut **tidak ada** di `allModel4.ipynb` saat ini, tetapi `delay_tracking_plot_P1/P2/P4.csv` ada di disk, yang berarti versi notebook yang mengandung offset itu pernah dieksekusi dan menghasilkan ketiga file tersebut.

**Status: `delay_tracking_plot_*.csv` dan `multi_port_delay_tracking_revision*.png` (sumber Fig. 4) adalah TIDAK DIKETAHUI.** Harus diregenerasi, tidak boleh dipakai apa adanya.

---

## 6. Yang terkonfirmasi bersih

Diperiksa dan tidak ditemukan kontaminasi pada jalur metrik:

- **`revision/DataAugmentation.ipynb`** — seluruh pemakaian `np.random` adalah sintesis data WGAN-GP dan subsampling t-SNE: `:69,71` (`np.random.choice` resampling), `:74` (jitter), `:362` (`policing_rate_kbps`, sebuah *fitur input* sintetis), `:367` (tag prioritas), `:407` (penarikan sampel untuk plot). Tidak ada yang menyentuh metrik perbandingan. Ini pemakaian yang sah.
- **Training loop `allModel2/3/4.ipynb`** — `np.random` hanya muncul sebagai `np.random.seed(SEED)`. Jalur metrik bebas dari random.
- **`Reinforcement Learning/old/`, `Reference/`, `Data-sensors/`, `pengujian/`** — di luar jalur hasil.

Catatan untuk Fase 2B (keadilan tuning): **tidak ditemukan kode tuning apa pun** di seluruh repo — tidak ada optuna, ray.tune, GridSearchCV, hyperopt, wandb, maupun loop `itertools.product`. Seluruh algoritma berbagi konfigurasi identik (`lr = 3e-4`, Adam, LinearLR, `grad_clip = 0.5`, `epochs = 2000`, `batch = 64`, `gamma = 0.99`). Ini kabar baik: tidak ada algoritma yang diuntungkan oleh tuning selektif. Tetapi artinya "effort tuning yang sama" saat ini berarti "nol tuning untuk semua".

Hanya **satu seed** yang pernah dijalankan (`SEED = 42`). Tidak ada estimasi varians di repo.

---

## 7. Jawaban atas pertanyaan Fase 0 butir 3

> Periksa apakah Fig. 5–8 berasal dari training run nyata atau dari sumber yang sama dengan Table III/IV.

**Berbeda sumber, dan setengah sah.**

Fig. 5–8 dibangun dari `revision/training_convergence_*.csv` yang ditulis `allModel4.ipynb:464` — yaitu dari training loop nyata, **bukan** dari `allModel1.ipynb` yang memfabrikasi. Sumbu **Loss** sah.

Namun sumbu **Reward** tidak sah (§5.8): yang di-plot adalah mean reward batch dataset, yang identik untuk semua algoritma dan independen dari kebijakan.

Fig. 4 (`multi_port_delay_tracking_revision.png`) berstatus **TIDAK DIKETAHUI** karena kemungkinan offset +0.6 ms (§5.9).

Fig. 3 (t-SNE) berasal dari `DataAugmentation.ipynb` dan bersih.

---

## 8. Inventaris file hasil dan provenansnya

| File | Baris | Dihasilkan oleh | Status |
|---|---|---|---|
| `final/sla_violation_report.csv` | 5 | `final/allModel1.ipynb:384` | **FABRIKASI** |
| `revision/sla_violation_report.csv` | 5 | `revision/allModel4.ipynb:761` | Terkontaminasi struktural |
| `revision/model_comparison_results.csv` | 5 | `revision/allModel4.ipynb:603` | Terkontaminasi struktural |
| `revision/viz_detail_{DQN,DDQN,PPO_Standard,Proposed_(SDH-PPO),Static}.csv` | 3000 | `revision/allModel4.ipynb:556` | Terkontaminasi struktural (§3.1) |
| `revision/viz_detail_Proposed_(Hard/Soft/Sigmoid_Mask).csv` | 3000 | **Tidak ada notebook yang menghasilkannya** | **TIDAK DIKETAHUI** |
| `revision/training_convergence_*.csv` | 2000 | `revision/allModel4.ipynb:464` | Loss sah; Reward tidak sah (§5.8) |
| `revision/delay_tracking_plot_P{1,2,4}.csv` | 100 | Versi notebook yang sudah tertimpa | **TIDAK DIKETAHUI** (§5.9) |
| `revision/eval_delay_ms_p4.csv` | 15000 | `DataAugmentation.ipynb` | Bersih (uji fidelitas WGAN) |

---

## 9. Hitungan akhir

| Kategori | Jumlah |
|---|---|
| Angka **FABRIKASI** di `main.tex` | **5** klaim numerik berbeda (27.3%, 47.6%, 0.0%, 2.71 ms, "2× epoch"), muncul di 2 lokasi (Abstract `:25`, Kesimpulan `:513`) |
| Angka **TERKONTAMINASI STRUKTURAL** | Seluruh Table IV (35 sel) + 8 angka turunan di Section IV.B `:491` |
| Angka **TIDAK DIKETAHUI** | Data sumber Fig. 4; 3 file `viz_detail_*_Mask.csv` tanpa provenans |
| Figure ikut terkontaminasi? | **Ya sebagian.** Fig. 5–8 sumbu reward tidak sah; Fig. 4 tidak diketahui; Fig. 3 bersih |
| Klaim paper yang tidak didukung kode | 3: safety layer (no-op 99,89%), dueling critic (hampa), PPO clip (tidak pernah aktif) |

---

## 10. Konsekuensi untuk fase berikutnya

1. **Fase 4 (sweep) tidak dapat dijalankan pada evaluator saat ini.** Tanpa environment yang memiliki trade-off, hasil sweep hanyalah rumus tertutup dikali N seed.
2. **Arm ablation "tanpa safety layer" (Fase 3) akan mengukur ≈ nol** selama bug unit z-score vs milidetik belum diperbaiki.
3. **Arm ablation "tanpa dueling critic" tidak bermakna** selama `action_dim = 1`, karena dekomposisi dueling hampa secara definisi.
4. **Kontradiksi Abstract vs Table IV tidak boleh diselesaikan dengan menyalin Table IV**, karena Table IV sendiri belum valid.

Keputusan arah (membangun simulator terkalibrasi / off-policy evaluation / re-run testbed fisik / menerima hasil nol) berada di luar kewenangan fase ini dan menunggu keputusan pemilik penelitian.
