# Protokol Eksperimen V2

Tanggal: 2026-09-25, direvisi 2026-09-26 (versi final, menunggu persetujuan untuk dikunci)
Status: **draf, menunggu persetujuan.** Sweep final belum dijalankan; test split belum disentuh.
Aturan berhenti di §10 berlaku begitu dokumen ini disetujui.
Pendahulu: `06-v1-closure.md`

Dokumen ini adalah pra-registrasi. Setelah disetujui, tidak boleh diubah berdasarkan hasil.

---

## 0. Ringkasan perubahan dari V1

| Cacat V1 | Perbaikan V2 |
|---|---|
| Tidak ada split train/eval | Split temporal 60/20/20; test dikunci di balik `--allow-test` |
| Tidak ada metode yang konvergen | Anggaran step dipilih dari pilot pada kurva val; reward dinormalisasi |
| Safety layer hanya untuk Proposed | Faktor ortogonal `--safety {on,off}` untuk **semua** metode |
| `const_max` = `no_control` | `const_max` dihapus; alokasi awal diacak; `equal_split` ditambahkan |

---

## 1. Split data

Trace: 1.022 baris, `rx_mbps_p{1,2,4}` dari `dataset_dqn_rich.csv`.

| Split | Proporsi | Baris | Peran |
|---|---|---|---|
| train | 60% | 0–612 (613) | Melatih agen; sumber **seluruh** statistik |
| val | 20% | 613–816 (204) | Memilih anggaran step; smoke test; seluruh keputusan desain |
| test | 20% | 817–1021 (205) | **Disentuh satu kali**, hanya pada run final V2 |

Usulan proporsi train/val: **75/25 di dalam 80% awal**, menghasilkan 60/20/20 keseluruhan.

Test dilindungi di kode: `--phase test` atau `--eval-phase test` gagal tanpa `--allow-test`.

**Statistik hanya dari train.** Mean permintaan `demand_prop`, konstanta normalisasi reward, dan
skala normalisasi state seluruhnya diestimasi pada train. Diterapkan tanpa perubahan pada val
dan test.

### 1.1 `episode_len` harus 50

| Split | Baris | Start valid @200 | @100 | @50 |
|---|---|---|---|---|
| train | 613 | 413 | 513 | 563 |
| val | 204 | **4** | 104 | 154 |
| test | 205 | **5** | 105 | 155 |

`episode_len=200` memberi val hanya 4 titik start — seluruh episode evaluasi praktis identik.
**Ditetapkan `episode_len = 50`** (≈1 menit waktu jaringan).

### 1.2 Split tidak exchangeable — wajib dilaporkan

| Split | Mean per slice (Mbps) | Total |
|---|---|---|
| train | [3,554 3,554 4,274] | **11,38** |
| val | [4,355 4,356 5,076] | **13,79** |
| test | [4,244 4,242 4,970] | **13,46** |

Beban val/test **21% lebih tinggi** daripada train. Trace 20 menit ini memiliki gradien beban.

Konsekuensi: agen dilatih pada rezim underload lalu diuji pada rezim overload. Ini uji
generalisasi yang sah dan informatif, tetapi **harus dinyatakan terbuka di paper** sebagai
distribution shift, bukan disembunyikan.

**Kapasitas link** ditetapkan dari train saja agar tidak mengintip test:
`C = 1,05 × 11,38 = 11,95 ≈ 12,0 Mbps`.

---

## 2. Anggaran training

Pilot: 4 metode learning × 2 level safety × 2 seed = 16 run, batas atas 300.000 step, probe val
tiap 25.000 step (5 episode), **hanya train/val**.

Kriteria pemilihan: satu `max_steps` yang **sama untuk semua metode**, yaitu titik ketika kurva
val mendatar menurut kriteria `|Δ| < 0,10` rentang — kriteria yang sama dipakai
`plot_convergence.py`.

### 2.1 Hasil pilot

16 run selesai. **Kondisi tabel ini, dinyatakan eksplisit:** probe val **5 episode** yang dibaca
dari kurva training, digabung **safety on + off** (4 run per sel). Tabel tuning di §2.4 memakai
kondisi yang berbeda — eval 20 episode, safety off saja — jadi kedua tabel tidak boleh
dibandingkan langsung. Rinci di §2.2.

| step | PPO | SDH-PPO | DQN | DDQN |
|---|---|---|---|---|
| 25k | 48,31 | 45,49 | 49,53 | 46,60 |
| 50k | 48,95 | 48,18 | 47,23 | 44,97 |
| 75k | 48,02 | 47,32 | 43,60 | 46,83 |
| 100k | 46,71 | 45,84 | 43,97 | 46,03 |
| 125k | 47,11 | 47,39 | 42,67 | 40,90 |
| 150k | 46,98 | 47,05 | 36,67 | **34,13** |
| **175k** | 44,76 | 44,03 | **33,60** | 37,63 |
| 200k | 47,94 | 46,72 | 37,50 | 36,17 |
| 225k | 46,94 | 44,62 | 35,57 | 36,17 |
| 250k | **44,53** | **41,84** | 35,20 | 37,80 |
| 275k | 46,04 | 44,07 | 41,33 | 40,23 |
| 300k | 47,15 | 46,02 | — | — |

**Dipisah per level safety** (probe 5 episode, mean 2 seed). Penggabungan di tabel atas
menyembunyikan spread sampai 11,8 poin, jadi versi terpisah inilah yang dipakai:

| step | PPO off | PPO on | SDH-PPO off | SDH-PPO on | DQN off | DQN on | DDQN off | DDQN on |
|---|---|---|---|---|---|---|---|---|
| 25k | 56,07 | 37,00 | 48,67 | 35,27 | 51,47 | 47,60 | 51,60 | 41,60 |
| 50k | 56,40 | 45,00 | 55,27 | 42,60 | 50,47 | 44,00 | 50,73 | 39,20 |
| 75k | 53,80 | 46,73 | 54,93 | 46,47 | 51,40 | 35,80 | 52,27 | 41,40 |
| 100k | 46,73 | 37,40 | 46,87 | 35,73 | 49,67 | 38,27 | 51,07 | 41,00 |
| 125k | 52,53 | 41,07 | 50,93 | 40,87 | 47,00 | 38,33 | 46,27 | 35,53 |
| 150k | 58,60 | 50,93 | 56,27 | 51,60 | 38,20 | 35,13 | 38,60 | **29,67** |
| 175k | 48,20 | 37,27 | 47,47 | 37,60 | **34,13** | **33,07** | 43,80 | 31,47 |
| 200k | 52,93 | 48,07 | 50,60 | 45,80 | 35,60 | 39,40 | 36,60 | 35,73 |
| 225k | 52,20 | 41,07 | 50,27 | 35,53 | 34,33 | 36,80 | 35,40 | 36,93 |
| 250k | **45,53** | 39,80 | 44,53 | **32,73** | 35,53 | 34,87 | 39,33 | 36,27 |
| 275k | 53,47 | 49,47 | 53,93 | 48,40 | 39,00 | 43,67 | 36,80 | 43,67 |
| 300k | 49,27 | 44,13 | 51,13 | 41,13 | — | — | — | — |

Dua pola yang berbeda:

- **PPO dan SDH-PPO nyaris tidak belajar.** Bergerak dari ~48 ke ~45 lalu berosilasi dalam pita
  44–48 sepanjang 300k step. Tidak ada tren jelas setelah 25k.
- **DQN dan DDQN belajar, lalu memburuk.** Optimum val di 175k (DQN 33,60) dan 150k
  (DDQN 34,13), setelah itu naik kembali ke 40–41 pada 275k — pola divergensi overestimasi yang
  khas.

### 2.2 Aturan seleksi checkpoint — FINAL

Menggantikan anggaran global 175.000 step (arsip di §2.3).

- Batas atas **300.000 step, sama untuk semua metode**.
- Probe val tiap **25.000 step**, **20 episode**, pada **himpunan episode tetap**.
- **Tepat 12 probe untuk keempat metode.**
- **Checkpoint dengan val terbaik dipulihkan** di akhir training; step terpilih dicatat sebagai
  `best_val_step`, jumlah probe sebagai `n_val_probes`.

Alasan penggantian anggaran global: 175k adalah optimum DQN tetapi memotong PPO sebelum nilai
terbaiknya, sementara 300k merugikan DQN/DDQN 6-8 poin karena divergensi pasca-optimum. Seleksi
checkpoint memberi tiap metode titik terbaiknya sendiri tanpa menguntungkan metode mana pun.
Pemilihan selalu pada val, tidak pernah pada test.

#### Dua cacat pada implementasi pertama aturan ini

Ditemukan saat menelusuri selisih §2.1 vs §2.4. Keduanya cacat kode, bukan pilihan desain, dan
keduanya sudah diperbaiki sebelum protokol dikunci.

**Cacat A - anggaran probe tidak identik.** Blok probe di `run_ppo` berada di dalam loop rollout
tanpa gerbang, sehingga PPO melakukan probe **setiap rollout (2.048 step)**, sedangkan `run_dqn`
digerbangi `eval_every`. Terukur dari CSV: **PPO/SDH-PPO 147 probe per run, DQN/DDQN 11**. argmin
untuk PPO diambil dari 13x lebih banyak undian derau. Klaim "anggaran identik" tidak berlaku
untuk langkah seleksi.

**Cacat B - probe bukan himpunan validasi tetap.** `probe()` tidak me-reseed RNG environment,
sedangkan `evaluate()` me-reseed. Tiap probe memakai 5 episode yang berbeda dan bergeser,
sehingga argmin memilih probe yang beruntung, bukan kebijakan yang baik. Terukur pada config
terpilih SDH-PPO seed 0:

| | nilai |
|---|---|
| probe minimum (5 episode) | **40,13** pada step 282.624 |
| eval 20 episode dari checkpoint yang sama persis | **51,50** |
| **optimisme** | **11,37 poin** |

**Arah bias kedua cacat merugikan PPO/SDH-PPO**, yaitu metode Proposed - bukan menguntungkannya.

Perbaikan: `probe()` me-reseed ke `seed + 20_000` tiap pemanggilan (offset berbeda dari
`evaluate()` yang memakai `seed + 10_000`, sehingga himpunan seleksi dan himpunan yang dilaporkan
bukan episode yang sama); `--probe-episodes` naik 5 ke 20 agar metrik seleksi punya varians yang
sama dengan metrik yang dilaporkan; gerbang probe yang sama dipakai `run_ppo` dan `run_dqn`. Di
`run_dqn` blok probe dinaikkan keluar dari cabang training supaya jadwalnya tidak bergantung pada
terisinya replay buffer.

Konsekuensi: seluruh 64 run tuning dijalankan ulang. Hasil lama diarsipkan di `results/tuning/`,
tidak dihapus dan tidak dipakai; yang baru di `results/tuning-v2/`.

Terverifikasi: probe parity 12/12/12/12; dua run dengan seed sama menghasilkan deret `val_viol`
identik.

### 2.2a (arsip) Anggaran 175.000 step — tidak dipakai lagi

Alasan:

- Tepat pada optimum val DQN dan berdekatan dengan optimum DDQN (150k).
- Untuk PPO/SDH-PPO, nilai di 175k (44,76 / 44,03) berada dalam pita derau dibanding nilai
  terbaiknya di 250k (44,53 / 41,84) — selisih 0,23 dan 2,19 poin, sementara osilasi
  antar-titik berdekatan mencapai 3 poin.
- Menaikkan ke 300k **merugikan** DQN/DDQN sebesar 6–8 poin karena divergensi.

Pemilihan dilakukan pada **val**, yang memang perannya, dan **satu angka yang sama** dipakai
seluruh metode. Test tidak dilibatkan.

### 2.3 Baseline heuristik pada val yang sama

Konteks yang harus dibaca bersama tabel di atas (seed 0, 20 episode):

| Kebijakan | Safety off | Safety on |
|---|---|---|
| `demand_prop` | **32,37** | 32,47 |
| `no_control` | 58,60 | 35,03 |
| `equal_split` | 53,77 | 40,13 |
| `threshold` | 68,43 | 67,03 |

Tiga hal yang dicatat sebagai hipotesis untuk diuji formal di sweep penuh:

1. **`demand_prop` tetap terbaik (32,4)**, tetapi jaraknya ke DQN (33,6) kini kecil — bukan 12
   poin seperti pada V1 in-sample.
2. **PPO dan SDH-PPO (41,8–44,5) lebih buruk daripada `no_control` + safety layer (35,0).**
3. **Safety layer memberi manfaat besar justru pada kebijakan yang lemah** (`no_control`
   58,6 → 35,0) dan hampir nol pada kebijakan yang sudah baik (`demand_prop` 32,4 → 32,5).
   Interpretasi yang masuk akal: safety layer itu sendiri sebuah pengendali reaktif, sehingga ia
   menggantikan kendali yang sudah disediakan `demand_prop`.

Butir 3 penting bagi narasi paper: kemungkinan besar **lapisan safety itulah kontribusinya,
bukan RL-nya**. Keluarga perbandingan (a) dirancang tepat untuk menguji ini.

Catatan: `threshold` (aturan yang gue usulkan di §4) ternyata buruk — 67–68% violation, terburuk
dari semua. Dipertahankan di desain sebagai lantai pembanding, bukan sebagai kandidat serius.

---

### 2.4 Hasil tuning anggaran setara - putaran final

96 run selesai: 4 metode x 8 konfigurasi x 2 seed, ditambah 2 arm residual x 8 x 2. Anggaran
identik (300k step, 12 probe val, seleksi checkpoint), dilatih pada train dan dipilih pada val.
Safety layer dimatikan agar efek hyperparameter tidak tercampur. Diturunkan oleh
`scripts/summarize_tuning.py` dari `results/tuning-v2/selection.csv`; tidak ada angka yang ditulis
tangan.

**Perbaikan probe bekerja, dan besarnya terukur:**

| | Putaran 1 (arsip) | Putaran final |
|---|---|---|
| Probe per run | **11-147** (tidak setara) | **12-12** (setara) |
| Gap probe ke eval, mean | **11,12 poin** | **1,98 poin** |
| Gap, rentang | 3,60 sampai 16,13 | -2,30 sampai 6,03 |

Optimisme seleksi turun dari sekitar sebelas poin menjadi sekitar dua. Angka 11,12
poin itu dihitung atas seluruh 64 run putaran pertama, bukan satu run sial: **setiap**
checkpoint putaran itu dipilih pada probe yang menaksir dirinya terlalu bagus.

**Konfigurasi terpilih:**

| Metode | Konfigurasi terbaik | Val viol % (sd) | gap probe ke eval | Putaran 1 (arsip) |
|---|---|---|---|---|
| DQN | `lr3e-4_ts2000_b11_ed30000` | **35,93** (1,23) | 0,33 | 37,42 (`lr3e-4_ts500_b11_ed100000`) |
| DDQN | `lr3e-4_ts2000_b11_ed30000` | **35,98** (0,40) | 1,25 | 38,80 (`lr3e-4_ts2000_b21_ed100000`) |
| PPO | `lr3e-4_ent0.01_clip_rs19.0106` | **51,50** (3,06) | 2,90 | 51,87 (`lr3e-4_ent0.01_clip_rs19.0106`) |
| SDH-PPO | `lr1e-4_ent0.0_clip_rs19.0106` | **51,58** (0,87) | 1,85 | 51,77 (`lr3e-4_ent0.01_clip_rs19.0106`) |

**Arm residual, keluarga (e):**

| Arm | Konfigurasi terbaik | Val viol % (sd) | gap probe ke eval |
|---|---|---|---|
| SDH-PPO residual | `lr1e-4_ent0.01_clip_rs1.0` | **33,10** (0,80) | 2,35 |
| SDH-PPO + BC init | `lr1e-4_ent0.01_tanh_rs19.0106` | **33,28** (0,78) | 2,62 |

**Yang berubah dari putaran pertama, dan yang tidak.**

- **DQN dan DDQN membaik**: 37,42 ke 35,93
  dan 38,80 ke 35,98. Keduanya kini
  memilih konfigurasi yang sama (`lr3e-4_ts2000_b11_ed30000`). Seleksi yang jujur menemukan
  checkpoint yang lebih baik, bukan yang kebetulan bagus di lima episode.
- **PPO dan SDH-PPO praktis tidak berubah**: 51,87 ke
  51,50 dan 51,77 ke
  51,58. Cacat probe bukan penyebab kegagalan PPO. Itu
  membatalkan satu hipotesis lagi: kegagalannya bukan artefak seleksi.
- **`lr = 3e-4` tidak lagi menang di semua metode.** SDH-PPO terpilih pada
  `lr1e-4_ent0.0_clip_rs19.0106`. Untuk DQN/DDQN `lr = 1e-4` jelas lebih buruk (49-51 lawan
  36-38), jadi satu-satunya faktor yang konsisten sekarang ada di keluarga Q, bukan lintas semua
  metode.
- **Dua hipotesis diagnostik tetap terbantah.** `clip` tetap menang untuk PPO dan SDH-PPO, jadi
  mis-spesifikasi densitas nyata tetapi tidak mengikat. `ent_coef` tidak menentukan: pemenang PPO
  memakai 0,01 dan pemenang SDH-PPO memakai 0. Diperiksa ulang terhadap data baru, bukan
  diwariskan dari putaran lama.
- **2 seed masih tipis.** sd mencapai 5,68 pada satu konfigurasi. Sweep final
  memakai 10 seed.

### 2.5 Uji behavior cloning — representasi bukan kendalanya

Aktor PPO yang sama, dilatih supervised meniru aksi `demand_prop` pada train:

| | Val viol % |
|---|---|
| BC dari aktor PPO | **33,18** |
| `demand_prop` asli | **32,88** |
| Selisih | **+0,30** (MSE akhir 0,002) |

Kelas kebijakan **mampu** merepresentasikan heuristik itu hampir persis. Jadi kegagalan PPO
bukan soal representasi, bukan soal observasi, dan — setelah §2.4 — bukan pula soal
parameterisasi aksi atau bonus entropi.

**Yang tersisa sebagai penjelasan:** sinyal belajarnya sendiri. Reward per langkah tampaknya
terlalu lemah relatif deraunya untuk memandu policy gradient, sementara Q-learning yang
melakukan bootstrap masih bisa mengekstrak sinyal. Ini hipotesis, belum diuji, dan harus
dinyatakan sebagai hipotesis di paper.

### 2.6 Posisi seluruh metode pada val

| Kebijakan | Val viol % |
|---|---|
| `demand_prop` | 32,37 |
| BC dari aktor PPO (probe) | 33,03 |
| **SDH-PPO residual** (tuned) | 33,10 |
| **SDH-PPO + BC init** (tuned) | 33,28 |
| `no_control` + safety | 35,03 |
| DQN (tuned) | 35,93 |
| DDQN (tuned) | 35,98 |
| `equal_split` + safety | 40,13 |
| PPO (tuned) | 51,50 |
| SDH-PPO (tuned) | 51,58 |
| `threshold` | 67,03 |

**`demand_prop` masih tidak terkalahkan (32,37).** Learner terbaik adalah arm residual pada
33,10 - dan arm itu *diberi* `demand_prop` sebagai titik awalnya. Selisihnya
0,73 poin, **berbalik merugikan metode learning**.

Yang berubah dari putaran pertama: jaraknya menyempit drastis. Dulu learner terbaik (DQN
37,42) tertinggal 5,05 poin; kini arm residual tertinggal
0,73 poin. Tetapi penyempitan itu datang dari **memberikan heuristiknya kepada
agen**, bukan dari agen mempelajarinya.

**Keluarga (e), H0 "koreksinya nol": DITOLAK - dan itu kabar buruk.**

Koreksi residual **tidak** nol. Terukur pada saat evaluasi, kebijakan terpilih menerapkan koreksi
rata-rata **0,086** dari batas 0,25 (34% batas), dan **93% langkah** menerima koreksi lebih besar
dari 0,01. Pada rollout, `res_mean_abs` rata-rata **0,152**, yaitu 61% batas.

Jadi agennya bukan diam. Ia aktif menggeser aksi menjauh dari heuristik, sebanyak sepertiga
anggaran koreksinya, dan hasilnya **lebih buruk** 0,73 poin. Nilai tambahnya bukan
nol; nilai tambahnya negatif kecil.

Perlu dicatat sebagai pembanding kewajaran: aktor Gaussian yang belum terlatih dengan
`std = 0,607` menghasilkan mean nilai mutlak aksi sekitar 0,48, yang setelah dikalikan batas 0,25
menjadi sekitar 0,12 - tidak jauh dari 0,152 yang terukur. Jadi besaran koreksi itu **konsisten
dengan kebijakan yang nyaris tidak terlatih**, bukan bukti bahwa ia mempelajari sesuatu. Kedua
pembacaan itu dilaporkan; membedakannya butuh uji yang belum dijalankan.

**Delapan konfigurasi residual mendarat dalam pita 33,10-33,75.** Keseragaman itu sendiri
informatif: hasilnya hampir tidak bergantung pada hyperparameter, yang wajar bila heuristiknya
yang menanggung kinerja dan koreksi RL-nya derau di atasnya.

Uji BC (§2.5) memberi angka pembanding langsung: 33,03 lawan
`demand_prop` 32,88, selisih 0,15.
Meniru heuristik secara supervised mendekatinya; melatih RL di atasnya tidak memperbaikinya.

---

### 2.7 Arm residual - desain

Dua arm yang menjadikan `demand_prop` prior alih-alih pesaing. Keduanya dijalankan di atas
`sdhppo`, karena keluarga (e) adalah klaim tentang metode Proposed. Flag-nya ortogonal, jadi
berlaku juga untuk `ppo` bila diperlukan.

| Arm | Flag | Mekanisme |
|---|---|---|
| BC-init | `--actor-init bc` | Aktor di-pretrain supervised meniru aksi `demand_prop` pada train (20.000 transisi, 200 epoch, lr 1e-3), lalu PPO berjalan normal dari bobot itu |
| Residual | `--residual on` | Aksi yang dieksekusi `clip(a_demand_prop + 0,25 * a_agen, -1, 1)` |

Rutin BC-nya **satu implementasi** (`bc_pretrain()` di `scripts/train_online.py`), dipakai
bersama oleh arm ini dan oleh uji BC §2.5, sehingga keduanya tidak bisa menyimpang.

Komposisi residual dipakai **identik di rollout, probe, dan eval**, dan diterapkan **sebelum**
`safety_mask`, sehingga lapisan safety selalu melihat aksi yang benar-benar akan dieksekusi.

`residual_bound = 0,25` **ditetapkan di muka dan tidak masuk grid**: koreksi dibatasi seperempat
rentang aksi, supaya agen tidak bisa sekadar menimpa heuristik. Konsekuensinya sensitivitas
terhadap nilai itu belum diukur; dicatat sebagai penyimpangan.

Ruang dan anggaran tuning **sama persis dengan PPO**: grid setengah-fraksi 2^4 yang sama
(lr x ent_coef x parameterisasi aksi x `reward_scale`), 8 konfigurasi, 2 seed, 300k step, seleksi
checkpoint, dilatih di train, dipilih di val, safety off. 2 arm x 8 x 2 = **32 run**.

Terverifikasi sebelum sweep: pada `--residual-bound 0` arm residual menghasilkan violation dan
reward **identik** dengan `demand_prop` (33,2 / 31,0 / 32,9 dan -1,166), yang membuktikan
komposisinya benar.

---

## 3. Desain faktorial safety layer

Setiap metode dijalankan dengan dan tanpa safety layer.

**Metode kontinu (PPO, SDH-PPO).** `safety_mask` diterapkan pada aksi sebelum `env.step`, baik
saat rollout training maupun evaluasi.

**Metode diskret (DQN, DDQN).** Pilihan diskret didekode lebih dulu menjadi vektor kontinu
`bins[argmax]`, lalu `safety_mask` yang **sama persis** diterapkan padanya. Tidak ada penyesuaian
khusus: karena aksi akhir selalu berupa vektor kontinu di `[-1, 1]`, lapisan itu tidak peduli
asal-usulnya diskret atau kontinu.

**Heuristik.** Keluaran `heuristic_action` juga vektor kontinu, sehingga `safety_mask`
diterapkan langsung tanpa perubahan.

**Rumus safety layer:**

```
ratio_p = delay_p / sla_p
hot_p   = ratio_p > margin                                (margin = 0,8)
a_p    := clip(a_p + gain * (ratio_p - margin), -1, +1)   untuk p yang hot
a      := clip(a, -1, +1)                                 (gain = 2,0)
```

Kedua sisi perbandingan berada dalam satuan relatif terhadap SLA. Versi V1 lama membandingkan
z-score dengan ambang milidetik sehingga aktif hanya pada 0,11% baris.

---

## 4. Baseline non-learning

| Baseline | Aksi |
|---|---|
| `no_control` | `a = 0`; mempertahankan alokasi awal |
| `equal_split` | bergerak menuju `C/3` per slice |
| `demand_prop` | bergerak menuju `mean_demand_train / Σ × C` |
| `threshold` | `a_p = clip(delay_p / sla_p − 1, −1, +1)` — **cacat, lihat §4.2** |

### 4.1 Aturan `threshold` cacat — catatan lengkap

Terukur di val: **68,43** (safety off) / **67,03** (safety on) — terburuk dari seluruh kebijakan,
termasuk kalah dari tidak melakukan apa-apa.

Cacatnya di **cabang negatif**. Ketika `delay_p < sla_p`, rasio < 1 sehingga `ratio − 1` bernilai
negatif dan aturan itu **menurunkan** rate slice yang sedang sehat. Slice itu lalu dibuat
kelaparan sampai melanggar SLA, dan aturan baru bereaksi setelah terlambat. Aturan ini secara
aktif merusak keadaan yang sudah baik.

Perbaikan yang benar adalah satu sisi:

```
a_p = clip(max(0, delay_p / sla_p - 1), 0, 1)
```

atau memakai margin seperti `safety_mask` (bertindak pada `ratio > 0,8`, bukan `ratio > 1`).

**Keputusan:** aturan cacat dipertahankan apa adanya di V2 sebagai **lantai pembanding**, bukan
kandidat. Mengubahnya sekarang berarti menyetel baseline setelah melihat hasilnya. Versi yang
diperbaiki boleh ditambahkan sebagai baseline terpisah dan bernama jujur, tidak menggantikan
yang lama.

### 4.2 Jawaban lengkap item 2 — `const_max` = `no_control`

Terverifikasi numerik pada `slice_env`:

```
rates awal:                 [4. 4. 4.]  sum 12.0 = C
proyeksi a = +1 (seragam):  [4. 4. 4.]
proyeksi a =  0:            [4. 4. 4.]
proyeksi a = [+1, 0, -1]:   [4.8 4.  3.2]
```

Aksi adalah perubahan **multiplikatif relatif** (`rates * (1 + gain * a)`) yang kemudian
diproyeksikan ke `Σ rates ≤ C`. Menaikkan seluruh slice dengan faktor sama lalu menormalkan
kembali ke kapasitas menghasilkan alokasi yang persis sama. **Aksi seragam adalah no-op.**

Ruang aksi efektif memiliki **2 derajat kebebasan, bukan 3**; hanya perbedaan relatif antar
slice yang berpengaruh.

**Usulan: `const_max` DIHAPUS, bukan diperbaiki.** Di bawah parameterisasi aksi relatif,
"maksimalkan" tidak memiliki makna — jumlahnya selalu diproyeksikan kembali ke kapasitas.
Memperbaikinya memerlukan perubahan ke aksi absolut, yang mengubah seluruh formulasi. Perannya
sebagai lantai sanity check digantikan `no_control` dan `equal_split`.

`equal_split` **juga akan degenerate** bila alokasi awal selalu seragam, karena `C/3 = 4,0`
persis sama dengan kondisi awal. Karena itu V2 **mengacak alokasi awal tiap episode** (Dirichlet
pada simpleks kapasitas). Terverifikasi memisahkan ketiganya: `no_control` 61,87 lawan
`equal_split` 50,93 total violation pada smoke test.

---

## 5. Normalisasi reward

Identik untuk seluruh metode learning:

```
r_raw = -( Σ_p max(0, d_p / sla_p - 1) + Σ_p drop_p )
σ_ref = std( r_raw ) di bawah kebijakan no_control, pada split TRAIN saja
r     = r_raw / σ_ref
```

Terukur: `σ_ref = 19,0106` (10.000 langkah, 5 seed, `no_control`, train, alokasi awal acak).

Satu skalar tetap, dihitung sekali dari train, dicatat di metadata tiap run, dipakai sama persis
oleh PPO, SDH-PPO, DQN, dan DDQN. **Tidak ada normalisasi berjalan** yang bisa berbeda antar
metode.

---

## 6. Arm augmentasi dan ablation

| Arm | Data training | Evaluasi |
|---|---|---|
| `full` | trace riil train + trace sintetis | val / test riil |
| `real_only` | trace riil train saja | val / test riil |
| `aug_subsample` | trace sintetis saja, panjang sama dengan train | val / test riil |
| `no_dueling` | sama dengan `full` | val / test riil |

`real_only` mengisolasi kontribusi augmentasi; `aug_subsample` mengontrol volume data sehingga
efek augmentasi terpisah dari efek jumlah sampel.

**Pembangkit trace sintetis** (`scripts/make_synth_trace.py`, belum ditulis): WGAN-GP dilatih
pada jendela geser `rx_mbps` **split train saja**, menghasilkan trace sepanjang train.
Arsitektur dan hyperparameter mengikuti `DataAugmentation.ipynb` (latent 100, GP λ=10, lr 1e-4,
betas (0.5, 0.9), batch 64, 301 epoch, generator update tiap 5 epoch).

Perbedaan penting dari V1: augmentasi kini beroperasi pada **deret waktu arrival**, bukan pada
baris dataset `(s, a, r, s')`. Di V1 kolom policing rate ditimpa `np.random.uniform` setelah
generator berjalan; hal itu tidak terjadi di sini karena policing rate adalah aksi agen, bukan
fitur data.

Evaluasi ketiga arm **selalu pada trace riil**, tidak pernah pada sintetis.

### 6.1 Generator sudah dibuat — dan mengalami mode collapse

`scripts/make_synth_trace.py` selesai dan diuji (301 epoch, 613 baris keluaran). Statistiknya:

| | P1 | P2 | P4 |
|---|---|---|---|
| Mean riil (train) | 3,554 | 3,554 | 4,274 |
| Mean sintetis | 3,411 | 3,420 | 4,143 |
| **Std riil** | **0,961** | **0,960** | **0,975** |
| **Std sintetis** | **0,323** | **0,334** | **0,332** |

Mean cocok dalam ~4%, tetapi **standar deviasi kolaps ke sepertiga nilai aslinya**. Trace
sintetis jauh lebih mulus daripada trafik sebenarnya.

Ini harus dilaporkan sebelum arm augmentasi ditafsirkan. Variabilitas trafik justru yang
menekan SLA; trace yang lebih mulus adalah **masalah yang lebih mudah**. Kalau `aug_subsample`
nanti tampak unggul, penjelasan paling mungkin adalah agennya dilatih pada beban yang lebih
jinak, bukan augmentasinya berguna. Perbandingan yang sahih harus menyertakan statistik ini.

Smoke test `real_only` dan `aug_subsample` lolos, 2 seed.

#### Satu upaya perbaikan - GAGAL, generator lama dipertahankan

Ambang lolos **ditetapkan sebelum upaya dijalankan** dan tidak direvisi sesudahnya. Dihitung pada
**train saja**; ketiganya harus lolos untuk ketiga slice. Tertulis sebagai konstanta di
`scripts/make_synth_trace.py`:

| Kriteria | Ambang lolos |
|---|---|
| Rasio std sintetis/riil per fitur | dalam [0,80 ; 1,25] |
| KS statistik marginal per slice | D <= 0,15 |
| Selisih autokorelasi lag-1 | selisih mutlak <= 0,15 |

Upaya: fitur **minibatch-stddev** pada masukan critic (penangkal mode collapse yang paling
standar) ditambah **jadwal WGAN-GP baku** - generator diperbarui tiap 5 **batch**, bukan tiap
epoch ke-5. Kode lama `if epoch % gen_every == 0` melatih generator hanya pada 1 dari 5 epoch,
bukan rasio critic:generator 5:1 yang dimaksud WGAN-GP. Poin kedua adalah penyimpangan sadar dari
`DataAugmentation.ipynb`.

Hasil kedua upaya, metrik identik:

| | std ratio P1/P2/P4 | KS D P1/P2/P4 | Verdict |
|---|---|---|---|
| Upaya 1 (asli) | 0,336 / 0,348 / 0,341 | 0,352 / 0,347 / 0,362 | **FAIL** |
| Upaya 2 (perbaikan) | 0,405 / 0,419 / 0,423 | 0,285 / 0,312 / 0,325 | **FAIL** |

Upaya 2 **lebih baik pada setiap metrik** tetapi masih jauh dari ambang. Sesuai aturan yang
ditetapkan di muka, arm augmentasi memakai **generator lama (upaya 1)** dan collapse dicatat
sebagai keterbatasan. Aturannya bisa diterapkan persis seperti tertulis, jadi tidak ada
improvisasi - tetapi dicatat di sini bahwa upaya 2 seragam lebih baik, kalau nanti mau ditukar.

Metrik kedua upaya ada di `data/synth/train_synth_trace_quality.json`; keluaran keduanya disimpan
sebagai `train_synth_trace_attempt{1,2}.csv`. Upaya 1 direproduksi oleh versi
`make_synth_trace.py` pada commit `f596d03`; skrip sekarang mereproduksi upaya 2.

**Konsekuensi untuk interpretasi:** std sintetis sepertiga nilai riil. Variabilitas trafik justru
yang menekan SLA, jadi `aug_subsample` melatih agen pada **masalah yang lebih mudah**. Kalau arm
itu tampak unggul, penjelasan paling mungkin adalah beban yang lebih jinak, bukan augmentasi yang
berguna.

---

## 7. Jumlah run dan estimasi waktu

### 7.1 Sudah dijalankan (train/val saja, test tidak disentuh)

| Blok | Run | Status |
|---|---|---|
| Pilot: 4 learner x 2 safety x 2 seed | 16 | selesai |
| Tuning putaran 1: 4 metode x 8 konfigurasi x 2 seed | 64 | selesai, **diarsipkan** (cacat probe §2.2) |
| Tuning putaran 2: 4 metode x 8 konfigurasi x 2 seed | 64 | putaran final |
| Tuning arm residual: 2 arm x 8 konfigurasi x 2 seed | 32 | putaran final |
| Uji BC | 2 | selesai |
| Smoke test skenario dan residual | 6 | selesai |

Putaran final tuning = 96 run, 300k step, `--device cpu`, 12 proses paralel.

### 7.2 Sweep final V2 - belum dijalankan

10 seed per konfigurasi. `max_steps` 300k dengan seleksi checkpoint.

| Blok | Run |
|---|---|
| 8 metode x 2 safety x 10 seed (arm `full`) | 160 |
| 4 learner x 2 arm augmentasi x 2 safety x 10 seed | 160 |
| `sdhppo` `no_dueling` x 2 safety x 10 seed | 20 |
| 2 arm residual x 2 safety x 10 seed | 40 |
| **Total** | **380** (300 learner, 80 heuristik) |

Skenario non-stasioner **tidak menambah run**: `--eval-scenario` menilai kebijakan yang sama
setelah eval utama di proses yang sama, jadi biayanya hanya 2 x 20 episode per run.

Heuristik praktis instan (<1 detik). Pada 300k step, rata-rata per learner ~50 menit:

| | Serial | 12 proses paralel |
|---|---|---|
| 300 run learner | ~250 jam | **~21 jam** |

Bila terlalu lama, ruang pemangkasan paling wajar tetap arm augmentasi (menghemat 160 run) - dan
§6.1 memberi alasan tambahan untuk itu, karena generatornya kolaps.

---

## 8. Perbandingan primer

Koreksi Holm diterapkan **di dalam tiap keluarga**, bukan lintas keluarga.

| Keluarga | Perbandingan | Jumlah |
|---|---|---|
| **(a)** Efek safety layer | on vs off, per metode | 8 |
| **(b)** Proposed+safety vs demand_prop+safety | 1 | 1 |
| **(c)** Efek augmentasi | `full` vs `real_only` vs `aug_subsample`, per learner | 12 |
| **(d)** Efek dueling | `sdhppo` `full` vs `no_dueling` | 1 |
| **(e)** Nilai tambah di atas heuristik | `res_sdhppo`+safety dan `bc_sdhppo`+safety, masing-masing vs `demand_prop`+safety | 2 |

Metrik primer: **total violation rate** (rata-rata violation lintas tiga slice).
Metrik sekunder: violation per slice, delay rata-rata per slice, total drop, reward.

Uji: Mann-Whitney U (tidak mengasumsikan normalitas, n=10) dan Welch's t sebagai pendamping;
effect size rank-biserial; CI 95% bootstrap. Selisih tidak signifikan dilaporkan apa adanya.

Keluarga (e) mengubah pertanyaannya. (b) menanyakan "apakah RL mengalahkan heuristik"; (e)
menanyakan "apakah RL menambah nilai **di atas** heuristik yang baik". Hipotesis nol yang sehat
untuk (e): **koreksinya nol**. `res_mean_abs` dan `res_sat_frac` dicatat per rollout supaya klaim
itu bisa diperiksa terhadap H0 tersebut, bukan diasumsikan.

**Seluruh perbandingan lain berlabel EKSPLORATIF** dan dilaporkan tanpa klaim signifikansi.

---

## 9. Analisis sekunder

### 9.1 Skenario trafik non-stasioner - DUA TERIMPLEMENTASI

Trace saat ini hanya 20 menit dengan satu pola, dan sudah menunjukkan gradien beban 21%. Tiga
skenario berikut menguji ketahanan terhadap perubahan rezim yang lebih tajam. **Skenario 1 dan 2
terimplementasi** sebagai `scenario_diurnal()` dan `scenario_flash()` di `scripts/slice_env.py`,
dipanggil lewat `--eval-scenario`. Skenario 3 tetap ditulis-tidak-dijalankan.

1. **Ramp diurnal.** Beban diskalakan mengikuti profil harian (rendah malam, puncak siang).
   Dasar: pola diurnal adalah karakteristik yang paling konsisten dilaporkan pada trafik seluler
   dan IoT, dan menjadi motivasi utama penskalaan sumber daya elastis pada literatur network
   slicing.
2. **Flash crowd.** Lonjakan mendadak 3–5× pada satu slice selama 30–60 detik, lalu kembali.
   Dasar: lonjakan mendadak adalah kasus uji standar untuk mekanisme isolasi antar-slice;
   inilah kondisi ketika isolasi benar-benar diuji, bukan pada beban tunak.
3. **Kedatangan dan kepergian slice** - **TIDAK DIJALANKAN.** Slice masuk atau keluar di
   tengah episode, mengubah jumlah penuntut kapasitas. Dasar: multi-tenancy dinamis adalah premis
   network slicing. Alasan tidak dijalankan: ini satu-satunya dari ketiganya yang **bukan**
   transformasi trace - ia butuh masking slice mati di observasi, di aksi, dan di proyeksi
   simpleks kapasitas, yaitu perubahan struktural `slice_env` yang lebih besar dari dua skenario
   lain digabung. Dinyatakan sebagai batas ruang lingkup, bukan sebagai hasil.

Keduanya dibangkitkan sebagai transformasi atas trace **eval**, dan dinilai dengan kebijakan yang
sudah dilatih **tanpa pelatihan ulang**, untuk mengukur generalisasi di luar distribusi.
Parameternya ditetapkan sebelum hasil apa pun dilihat:

| Skenario | Parameter | Dasar |
|---|---|---|
| `diurnal` | amplitudo +/-35%, periode **100 baris** | `dt` = 1 s, `episode_len` = 50, jadi satu episode melihat setengah siklus dan beban benar-benar naik-turun **di dalam** episode |
| `flash` | slice P2, faktor 4x, durasi **45 baris**, mulai di 40% trace | 45 s berada di dalam pita 30-60 s; P2 dipilih karena SLA-nya di tengah |

**Rancangan diurnal sempat salah dan diperbaiki sebelum evaluasi apa pun.** Versi pertama memakai
satu siklus penuh sepanjang split. Pada 613 baris itu berarti satu episode 50-step melihat di
bawah 8% siklus - faktor skala konstan, bukan perubahan rezim. Terukur: std per slice justru
**turun** ke 0,958 / 0,958 / 1,026 dari trace riil. Dengan periode 100 baris, std naik ke 1,519 /
1,517 / 1,603. Diperbaiki berdasarkan properti transformasinya sendiri, bukan berdasarkan hasil
kebijakan mana pun.

**Keterbatasan yang dicatat:** split val hanya 204 detik, jadi yang diuji adalah **bentuk** beban
naik-turun, bukan skala waktu 24 jam. Menyebutnya "diurnal" adalah analogi bentuk.

### 9.2 Residual RL di atas `demand_prop`

Karena `demand_prop` mengungguli seluruh metode learning di V1, varian yang wajar adalah
menjadikannya prior alih-alih pesaing:

```
a_total = a_heuristik(s) + a_agen(s)
```

Agen hanya mempelajari **koreksi** terhadap heuristik, sehingga titik awalnya sudah kompetitif
dan yang dipelajari adalah selisihnya. Ini memberi pertanyaan yang lebih jujur bagi paper: bukan
"apakah RL mengalahkan heuristik", melainkan "apakah RL menambah nilai di atas heuristik yang
baik". Hipotesis nol yang sehat: koreksinya nol.

**Naik dari analisis sekunder menjadi perbandingan primer.** Idenya ditulis di sini, tetapi
implementasi dan desain tuningnya ada di §2.7 dan perbandingan formalnya di keluarga (e) §8.
Koreksinya dibatasi: `clip(a_demand_prop + 0,25 * a_agen, -1, 1)`. H0 "koreksinya nol" diperiksa
lewat `res_mean_abs` yang dicatat per rollout, bukan diasumsikan.

---

## 10. Aturan berhenti

Berlaku begitu protokol ini disetujui.

1. **Tidak ada perubahan desain.** Tidak ada penambahan atau pengurangan arm, metode, baseline,
   skenario, metrik, keluarga uji, atau hyperparameter terpilih. Tidak ada perubahan pada
   `slice_env`, pada aturan seleksi checkpoint, atau pada definisi metrik.
2. **Setiap ide setelah titik ini berlabel EKSPLORATIF** dan dilaporkan tanpa klaim signifikansi,
   tanpa koreksi Holm, dan tanpa masuk ke keluarga primer (a)-(e).
3. **Test dibuka sekali.** Hanya di run final V2, di belakang `--allow-test`. Tidak ada
   pemilihan, penyetelan, atau pembacaan apa pun pada test sebelum itu.
4. **Hasil dilaporkan apa adanya.** Termasuk bila Proposed kalah, bila tidak ada learner
   mengalahkan `demand_prop`, atau bila koreksi residual nol.
5. **Kegagalan tetap tercetak.** Upaya WGAN yang gagal, dua cacat probe, dan cacat aturan
   `threshold` tetap ada di dokumen ini; tidak ada yang dihapus setelah hasil final diketahui.
6. **Yang boleh berubah** hanyalah perbaikan bug yang terbukti dan koreksi salah tulis. Setiap
   perbaikan semacam itu dicatat di "Penyimpangan dari rencana" beserta tanggalnya, dan bila ia
   mengubah angka, angka lamanya tetap tercetak sebagai arsip.

---

## Lampiran — jawaban diagnostik item 4, 5, 6, 7

### Item 4 — mengapa `real_only` dan `aug_subsample` tidak ada di V1

`train_online.py` V1 hanya memiliki `ARMS = ["full", "no_mask", "no_dueling"]`. Kedua arm
augmentasi dirancang untuk pipeline **offline** yang beroperasi pada baris dataset
`(s, a, r, s')` hasil WGAN-GP. Pipeline online tidak memakai dataset itu sama sekali: arrival
diambil langsung dari `rx_mbps` trace riil, dan WGAN-GP tidak berperan di mana pun. Yang
dibutuhkan adalah definisi ulang augmentasi sebagai pembangkit trace arrival — dispesifikasikan
di §6.

### Item 5 — kronologi bug unit safety layer

| Peristiwa | Waktu |
|---|---|
| Run sweep V1 paling awal | 2026-09-24 14:02:20 UTC |
| Run sweep V1 paling akhir | 2026-09-24 14:50:34 UTC |
| Commit `1b6345b` (`train_online.py`) | 2026-09-24 14:54 UTC |

Versi bermasalah (membandingkan z-score `state[10]` dengan ambang milidetik) berada di
`scripts/sweep.py` dan **sengaja dipertahankan** sebagai port setia notebook lama. Versi
diperbaiki ditulis baru di `train_online.py`; versi bermasalah **tidak pernah ada** di pipeline
online. 100 job menghasilkan 100 file `_eval.csv`: **tidak ada run yang dibuang atau diulang**.

### Item 6 — usaha memasang safety layer ke baseline

**10–15 baris, tanpa perubahan arsitektur** — sudah diimplementasikan untuk V2 (§3).
`safety_mask` bersifat generik terhadap representasi aksi, sehingga metode diskret dan heuristik
memakainya tanpa modifikasi.

### Item 7 — stasioneritas dan asal arrival

Arrival **tidak dibangkitkan model**; diputar ulang dari `rx_mbps_p{1,2,4}` pada
`dataset_dqn_rich.csv` (1.022 baris, 19 menit 59 detik, interval ~1,17 detik).
`slice_env._arrival()` mengindeks `(start + t) % len(arrivals)`.

Trace ini satu realisasi pendek dari satu pola trafik; tidak ada variasi rezim dan **tidak ada
uji stasioneritas formal yang dijalankan**. Bukti tidak langsung menunjukkan **tidak stasioner**:
mean beban naik 21% dari train ke val/test (§1.2). Wrap modulo menyambung akhir trace ke awal,
menciptakan diskontinuitas buatan pada episode yang melewati batas — dampaknya kecil pada
`episode_len=50` tetapi tetap dicatat.

---

## Penyimpangan dari rencana, dicatat terbuka

**Normalisasi observasi tidak divariasikan di grid tuning.** Rencana menyebut faktor
"normalisasi observasi/reward"; yang divariasikan hanya normalisasi **reward**
(`reward_scale` 19,0106 lawan 1,0). Skala observasi dibiarkan tetap dan identik lintas metode,
karena justru keidentikan itu yang menjadi properti keadilan protokol — memvariasikannya per
metode akan merusaknya. Konsekuensinya: efek normalisasi observasi belum diukur.

**Bug penjaga resume pada batch tuning pertama.** Path keluaran tidak memuat nomor seed,
sehingga setelah seed 0 selesai menulis, seed 1 ikut di-skip. Terdeteksi saat hanya 46 dari 64
run muncul; 19 run yang kurang dijalankan ulang dengan penjaga sadar-seed. Seluruh 64
konfigurasi kini punya 2 seed. Tidak ada hasil yang dibuang — yang hilang belum pernah
dijalankan.

**Merge `890d787` dari sesi lain.** Hanya menambah `API-DATABASE/Penjelasan.md` (+54 baris).
Tidak menyentuh `scripts/`, `results/`, `docs/`, maupun kode environment.

**Dua cacat probe pada seleksi checkpoint.** Rinci di §2.2. Konsekuensi: 64 run tuning dijalankan
ulang, angka §2.4 dan §2.6 diturunkan ulang, hasil lama diarsipkan.

**Jadwal generator WGAN diubah.** `DataAugmentation.ipynb` menggerbangi update generator pada
`epoch % 5`; upaya 2 memakai rasio 5:1 per **batch**. Upaya 2 gagal, jadi generator yang dipakai
tetap upaya 1 dengan jadwal asli. Rinci di §6.1.

**`residual_bound` ditetapkan di muka tanpa tuning.** 0,25, seperempat rentang aksi, supaya
koreksi tidak bisa menimpa heuristik. Tidak masuk grid, jadi sensitivitasnya terhadap nilai itu
belum diukur.

**Periode diurnal diperbaiki sebelum evaluasi.** Rinci di §9.1. Rancangan pertama terukur bukan
perubahan rezim; diperbaiki berdasarkan properti transformasi, bukan berdasarkan hasil kebijakan.

**Driver sweep pertama tidak terlacak di git.** 64 run tuning putaran pertama dijalankan dari
shell inline yang tidak pernah di-commit. Ditutup dengan `scripts/run_tuning.sh`, yang juga
memuat penjaga resume sadar-seed dan mode `DRY=1` untuk memeriksa antrean sebelum menghabiskan
jam CPU.

## Verifikasi protokol

- `--phase test` dan `--eval-phase test` menolak berjalan tanpa `--allow-test`.
- Hash `results/tables/per_seed_summary.csv` (V1) tetap identik.
- Self-check `slice_env` lolos **7** properti: 6 properti MDP ditambah properti transformasi
  skenario (diurnal mempertahankan mean dan menaikkan std; flash hanya menyentuh slice sasaran di
  jendelanya).
- **Probe parity:** tiap run tuning menghasilkan tepat 12 baris `val_viol`, keempat metode sama.
- **Probe deterministik:** dua run dengan seed sama menghasilkan deret `val_viol` identik.
- **Komposisi residual benar:** `--residual on --residual-bound 0` menghasilkan violation dan
  reward identik dengan `demand_prop` (33,2 / 31,0 / 32,9 dan -1,166).
- Smoke test seluruh sel faktorial lolos sebelum sweep penuh.
- Pilot dan smoke test hanya menulis ke `results/pilot/` dan `results/smoke/`.
