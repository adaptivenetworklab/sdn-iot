# Protokol Eksperimen V2

Tanggal: 2026-09-25, direvisi 2026-09-26 dan 2026-10-03 (keputusan K1-K6, menunggu persetujuan untuk dikunci)
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

**Seleksi di val juga berlaku di run final (A7).** Hasil final adalah checkpoint yang dipilih
oleh probe val, lalu dievaluasi **sekali** di test; bukan checkpoint terbaik yang diukur di test.
Sampai 2026-10-02 kode belum menjamin ini: probe memakai env evaluasi, sehingga run final dengan
`--eval-phase test` akan memilih checkpoint **di test**. Diperbaiki sebelum run final mana pun:
probe kini selalu membangun env dari split val (`split_arrivals()` di `train_online.py`),
terlepas dari `--eval-phase`. Diverifikasi oleh `scripts/check_crn.py`. Untuk run tuning
(`--eval-phase val`) perubahan ini tidak mengubah apa pun, karena env probe lama dan baru
memuat baris yang sama dengan seed yang sama.

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

**Catatan 2026-10-03: tabel di atas adalah seed 0 saja.** Nilai heuristik bergantung pada
himpunan episode evaluasi (`seed + 10_000`) dan alokasi awal acak, jadi satu seed bukan estimasi
yang representatif. Tabel 20 seed di val, dibangkitkan `scripts/final_plan_stats.py` dari
`results/diagnostic/heur_val20/` (DIAGNOSTIC):

<!-- BEGIN GENERATED heur -->
Heuristik di val, 20 seed (violation %):

| Kebijakan | Safety | mean | sd | min | max | seed 0 |
|---|---|---|---|---|---|---|
| `demand_prop` | off | 29,77 | 3,83 | 23,47 | 35,90 | 32,37 |
| `demand_prop` | on | 29,87 | 3,80 | 23,73 | 36,03 | 32,47 |
| `no_control` | off | 60,04 | 2,74 | 55,90 | 64,73 | 58,60 |
| `no_control` | on | 32,61 | 3,80 | 26,40 | 38,87 | 35,03 |
| `equal_split` | off | 51,61 | 2,50 | 47,20 | 56,13 | 53,77 |
| `equal_split` | on | 37,79 | 3,23 | 32,23 | 43,27 | 40,13 |
| `threshold` | off | 67,06 | 1,76 | 64,37 | 69,97 | 68,43 |
| `threshold` | on | 65,81 | 1,85 | 62,60 | 69,03 | 67,03 |
<!-- END GENERATED heur -->

Pembandingan learner (2 seed) dengan heuristik (1 seed) di §2.3 dan §2.6 karena itu tidak setara.
Tabel aslinya tidak diubah dan tetap tercetak sebagai arsip.

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
  memakai 20 seed (K1, 2026-10-03).

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

Catatan 2026-10-03: angka heuristik di tabel ini seed 0; lihat tabel 20 seed di §2.3.

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

**Implementasi `full` (2026-10-02).** Sampai tanggal itu `full` tidak pernah memuat trace
sintetis: kodenya jatuh ke trace riil train, sehingga `full` dan `real_only` identik
byte-per-byte. Kini `full` (dan `no_dueling`) dilatih pada **613 baris riil train diikuti 613 baris
sintetis upaya 1**, total 1.226 baris (`np.vstack`, riil lebih dulu). Titik start episode diundi
seragam di seluruh 1.226 baris, jadi episode yang melintasi baris 613 mencampur ujung riil dan
awal sintetis. Diskontinuitas ini sama sifatnya dengan wrap modulo di Lampiran item 7, dan dicatat.

**Konsekuensi untuk tuning.** Seluruh 96 run tuning berlabel `full`, padahal datanya riil saja.
Hyperparameter terpilih karena itu dipilih pada data `real_only`, lalu dipakai apa adanya untuk
arm `full` yang kini memuat sintetis. Tidak ada tuning ulang. `scripts/run_tuning.sh` kini memakai
`--arm real_only` secara eksplisit supaya tuning itu tetap bisa direproduksi.

`data/synth/*.csv` gitignored. Trace upaya 1 direproduksi oleh `make_synth_trace.py` pada commit
`f596d03`; md5 `train_synth_trace.csv` = md5 `train_synth_trace_attempt1.csv`
(`7687de3b3b66977cf49c813d22939bf1`).

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

**Keputusan K6 (2026-10-03).** Generator tetap upaya 1, sesuai aturan yang ditetapkan di muka.
Kedua upaya dilaporkan di paper sebagai keterbatasan: upaya 1 gagal ketiga kriteria, upaya 2 lebih
baik di setiap metrik tetapi tetap gagal, dan arm augmentasi memakai generator yang lebih buruk
dari keduanya karena itulah yang ditetapkan sebelum upaya 2 dijalankan.

### 6.2 Fidelitas generator - pelaporan saja (C4)

Dilaporkan di samping hasil arm augmentasi. Tidak ada ambang lolos baru, tidak ada pembangkitan
ulang, tidak ada keputusan yang bergantung padanya.

| Metrik | Dihitung atas | Keterangan |
|---|---|---|
| KS statistik D | marginal per slice | sama dengan §6.1 |
| Wasserstein-1 | marginal per slice | dalam Mbps |
| Selisih ACF | lag 1 sampai 10 per slice | §6.1 hanya lag 1 |
| AUC discriminator | jendela 50 x 3 | classifier sederhana, 5-fold CV; 0,5 = tak terbedakan |

**Pembanding: batas intra-dataset.** Metrik yang sama dihitung antara **riil-train dan riil-val**.
Angka itu adalah seberapa jauh dua potongan trace riil sendiri berbeda. Generator dinilai relatif
terhadap batas itu, bukan terhadap nol. Catatan: riil-train vs riil-val sudah memuat pergeseran
beban 21% (§1.2), jadi batas itu longgar dan harus dibaca demikian. Test tidak dipakai.

Dasar pemilihan metrik: "Benchmarking of Synthetic Network Data", 2025 **[belum diverifikasi]**.

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

**20 seed per konfigurasi (K1, 2026-10-03), tanpa pilot variansi terpisah.** `max_steps` 300k
dengan seleksi checkpoint di val. Seed 0-19 untuk setiap sel.

Driver: `scripts/run_final.py` (38 sel x 20 seed). Konfigurasi tiap learner dibaca dari
`results/tuning-v2/selection.csv` (argmin val), bukan diketik. `no_dueling` dan arm augmentasi
memakai konfigurasi learner-nya. Driver menolak jalan di atas perubahan yang belum di-commit di
`scripts/` atau protokol ini, sehingga hash commit di JSON tiap run adalah kode yang benar-benar
berjalan; ia juga menulis `manifest_*.json` (hash, tag, konfigurasi terpilih). Run yang gagal
diulang sekali dengan perintah identik dan dicatat di `failures.log`.

Jumlah run dan waktu dibangkitkan oleh `scripts/final_plan_stats.py`. Detik per run diukur dari
`results/tuning-v2/run.log` per metode; keluarga Q dua sampai tiga kali lebih lambat dari keluarga
PPO, jadi satu angka rata-rata lintas metode tidak dipakai.

<!-- BEGIN GENERATED sweep -->
| Blok | Run | CPU-jam (serial) |
|---|---|---|
| arm `full`, 4 learner | 160 | 84,20 |
| arm `full`, 4 heuristik | 160 | 0,00 |
| `real_only` + `aug_subsample`, 4 learner | 320 | 168,41 |
| `no_dueling` (SDH-PPO) | 40 | 11,67 |
| residual + BC init | 80 | 24,11 |
| **Total** | **760** | **288,38** |

Wall clock ideal pada 12 proses: **24,03 jam** (total / 12, tanpa ekor antrean). Heuristik dihitung 0 s. Rata-rata detik per run (train + eval): ddqn 2990, dqn 2528, ppo 1010, sdhppo 1050, sdhppo+bc 1119, sdhppo+res 1050.
<!-- END GENERATED sweep -->

Skenario non-stasioner **tidak menambah run**: `--eval-scenario` menilai kebijakan yang sama
setelah eval utama di proses yang sama, jadi biayanya hanya 2 x 20 episode per run.

Angka wall clock adalah batas bawah: diukur saat 12 proses tuning berjalan bersamaan, tetapi tanpa
beban lain di mesin. Bila CPU dipakai proyek lain, waktunya memanjang sebanding.

Bila terlalu lama, ruang pemangkasan paling wajar tetap arm augmentasi - dan §6.1 memberi alasan
tambahan untuk itu, karena generatornya kolaps. Pemangkasan semacam itu adalah perubahan desain
dan hanya boleh diputuskan **sebelum** protokol dikunci.

---

## 8. Perbandingan primer

Koreksi Holm diterapkan **di dalam tiap keluarga**, bukan lintas keluarga.

| Keluarga | Perbandingan | Jumlah |
|---|---|---|
| **(a)** Efek safety layer | on vs off, per metode (4 learner + 4 heuristik) | 8 |
| **(b)** Proposed+safety vs demand_prop+safety | 1 | 1 |
| **(c)** Efek augmentasi | `full` vs `real_only` vs `aug_subsample`: tiga pasangan per learner, **safety off** | 12 |
| **(e)** Nilai tambah di atas heuristik | `res_sdhppo`+safety dan `bc_sdhppo`+safety, masing-masing vs `demand_prop`+safety | 2 |

**Level safety untuk (c), ditetapkan saat persetujuan (2026-10-03).** Arm augmentasi dijalankan
pada kedua level safety, tetapi protokol sebelumnya tidak menyebut level mana yang membawa tes
primer. Ditetapkan **safety off**: mengisolasi efek augmentasi dari safety layer, konsisten dengan
tuning, dan konsisten dengan SD yang dipakai di §8.1. Perbandingan yang sama pada safety on
dilaporkan sebagai EKSPLORATIF (CI selisih, tanpa uji). Celah ini ditemukan saat dry-run skrip
analisis, sebelum test dibuka.

**(d) Efek dueling dipindah ke EKSPLORATIF (2026-10-03).** Alasannya struktural, bukan hasil.
Critic SDH-PPO mengestimasi **V(s)**, bukan Q(s,a); ia tidak menerima aksi
(`train_online.py`, kelas `Critic`):

```
h      = ReLU(base(s))
V(s_i) = v(h_i) + a(h_i) - (1/B) * sum_j a(h_j)
```

v dan a sama-sama head skalar, dan rata-ratanya diambil di dimensi **batch** (`dim=0`). Saat
rollout dan bootstrap B = 1, sehingga V = v(h) persis. Saat update B = 64, sehingga nilai satu
state bergantung pada state lain di minibatch. Dueling yang benar dengan head skalar runtuh menjadi
v(s), identik dengan `no_dueling`. Yang diukur `sdhppo` vs `no_dueling` adalah efek head auxiliary
yang di-centering per batch, bukan dekomposisi value/advantage. Kode **tidak** diubah, karena
tuning dijalankan dengan critic ini. Run `no_dueling` tetap dijalankan, dilaporkan sebagai CI
selisih tanpa uji signifikansi, dan paper tidak boleh menyebut critic ini "dueling" tanpa
penjelasan di atas.

Metrik primer: **total violation rate** (rata-rata violation lintas tiga slice, per run, atas 20
episode evaluasi). Metrik sekunder: violation per slice, delay rata-rata per slice, total drop,
reward.

### Desain berpasangan (K2)

Untuk seed ke-i, **seluruh metode** melihat realisasi environment yang sama:

- **Training:** urutan episode identik. RNG env hanya dipakai di `reset()`, yang terjadi setiap 50
  step untuk semua metode. Arm BC kini melakukan pretraining pada salinan env, karena sebelumnya
  ia menghabiskan sekitar 400 reset dan berlatih pada episode berbeda (diperbaiki 2026-10-02).
- **Probe val:** himpunan episode tetap, `seed + 20_000`.
- **Evaluasi:** himpunan episode tetap, `seed + 10_000`, termasuk heuristik.

Diverifikasi oleh `scripts/check_crn.py`. Yang tetap berbeda antar metode hanya keacakan internal
agen (inisialisasi bobot, eksplorasi, minibatch). Arm augmentasi berlatih pada trace berbeda karena
memang itu perlakuannya, tetapi tetap berbagi himpunan episode evaluasi. Karena itu **unit analisis
adalah seed, dan setiap perbandingan dipasangkan menurut seed.**

### Uji dan pelaporan (C1, C2, K3)

Diimplementasikan di `scripts/analyze_v2.py`, **dibekukan** bersama protokol ini (tag
`protocol-v2-final`) dan dijalankan tanpa modifikasi setelah sweep. `scripts/make_tables.py` adalah
generator tabel **V1** (Mann-Whitney, penamaan V1, menulis `results/tables/` yang hash-nya
dibekukan) dan tidak dipakai untuk V2; `analyze_v2.py` memakai ulang helper-nya (`boot_ci`, `holm`)
tanpa mengubahnya, dan menulis tabel LaTeX V2 ke `results/analysis-v2/`.

Dry-run sebelum test dibuka (2026-10-03), dua-duanya hanya val:

1. Atas data yang ada (konfigurasi terpilih tuning-v2, safety off, 2 seed; heuristik val 20 seed):
   `results/diagnostic/dryrun-v2-existing/analysis/`. Sel tanpa data dilaporkan "data tidak
   tersedia"; pengecekan re-threshold 1x (delay tersimpan mereproduksi flag violation) lolos untuk
   seluruh 172 run.
2. Gladi end-to-end: `run_final.py --eval-phase val --steps 4096 --seeds 3` (114 run, 0 gagal),
   lalu `analyze_v2.py`. Seluruh 38 sel, setiap keluarga, IQM, PoI, skenario, sensitivitas, dan
   kurva terisi.

Satu bug analisis diperbaiki saat dry-run: Holm sempat menghitung m hanya dari perbandingan yang
datanya ada; kini perbandingan yang hilang tetap dihitung dengan p = 1, sehingga sel yang hilang
tidak pernah melonggarkan koreksi. Satu celah desain ditemukan dan diputuskan user: level safety
untuk keluarga (c). `make_tables.py` V1 di-dry-run ke direktori sementara: `per_seed_summary.csv`,
`table_main.tex`, dan `table_stats.tex` identik; `stats_main.csv` berbeda 2e-20 (derau floating
point), verdict identik.

1. **Wilcoxon signed-rank** dua sisi atas selisih berpasangan `d_i = X_i - Y_i`, n = 20, Holm di
   dalam keluarga. Menggantikan Mann-Whitney U, yang mengabaikan pemasangan. Paired t sebagai
   pendamping. Effect size: matched-pairs rank-biserial.
2. **CI 95% bootstrap** (percentile, 10.000 resample atas seed) untuk rata-rata selisih
   berpasangan.
3. **IQM** per metode dengan CI 95% percentile bootstrap, dan **probability of improvement**
   P(X < Y), karena violation lebih kecil lebih baik. Dihitung dengan `rliable` atau implementasi
   numpy yang setara; `rliable` belum terpasang. Dilaporkan **berdampingan** dengan p-value Holm,
   tidak menggantikannya, dan tidak dipakai untuk klaim signifikansi. Dasar: Agarwal et al. 2021
   **[belum diverifikasi]**.
4. **Klaim "tidak ada perbedaan" (K3)** ditulis sebagai interval, misalnya "selisih berada dalam
   [a, b] poin (CI 95%)", tidak pernah "tidak ada efek". Berlaku khusus untuk (e) residual/BC vs
   `demand_prop` dan untuk (d).

Keluarga (e) mengubah pertanyaannya. (b) menanyakan "apakah RL mengalahkan heuristik"; (e)
menanyakan "apakah RL menambah nilai **di atas** heuristik yang baik". Hipotesis nol yang sehat
untuk (e): **koreksinya nol**. `res_mean_abs` dan `res_sat_frac` dicatat per rollout supaya klaim
itu bisa diperiksa terhadap H0 tersebut, bukan diasumsikan.

**Seluruh perbandingan lain berlabel EKSPLORATIF** dan dilaporkan tanpa klaim signifikansi.

### 8.1 Power analysis - dilaporkan, tidak untuk memilih N

N = 20 ditetapkan oleh K1 sebelum angka di bawah dihitung. Tabel ini menyatakan selisih terkecil
yang bisa dideteksi dengan power 0,8; ia tidak dipakai untuk menaikkan atau menurunkan N. Dasar:
Colas et al. 2018 **[belum diverifikasi]**.

**Metode.** Paired t dua sisi, n = 20, df = 19, diselesaikan eksak dengan noncentral t, lalu
dikali sqrt(1/0,955) (efisiensi relatif asimtotik Wilcoxon terhadap t di bawah normalitas).
**Koreksi α:** Holm di dalam keluarga mengurutkan p-value dan menguji yang terkecil pada α/m, yang
berikutnya pada α/(m-1), dan seterusnya sampai α. MDE karena itu dilaporkan pada α/m (langkah
pertama, kasus terburuk) dan pada α = 0,05 (langkah terakhir, kasus terbaik). m: (a) 8, (b) 1,
(c) 12, (e) 2. Holm di dalam keluarga **tidak** mengendalikan error lintas keluarga; kolom
Bonferroni lintas seluruh tes primer menunjukkan ongkos bila itu diinginkan.

**Sumber SD dan keandalannya.**
- Learner: tuning-v2 dengan safety off, 2 seed per konfigurasi. SD dipool di dalam konfigurasi
  atas 8 konfigurasi per metode (df = 8, mengasumsikan varians setara antar konfigurasi). SD
  konfigurasi terpilih sendiri hanya punya df = 1.
- Heuristik: 20 seed di val (df = 19).
- Tidak ada data berpasangan antar metode di atas n = 2, sehingga sigma_d dibatasi dengan ρ = 0.
  Himpunan episode bersama membuat ρ positif, jadi batas ini **konservatif**.
- Estimasi berpasangan n = 2 dicetak di sampingnya dan **tidak andal** (df = 1; CI 95% sigma pada
  df = 1 membentang kira-kira 0,45x sampai 32x estimasinya).
- Untuk (a) learner tidak ada data safety on di bawah aturan seleksi final, jadi SD safety off
  dipakai untuk keduanya.
- Untuk (c) tidak ada data arm augmentasi di bawah protokol final, jadi SD arm `full` dipakai.

<!-- BEGIN GENERATED mde -->
SD learner dari tuning-v2 (val, safety off):

| Arm | SD pooled (df) | SD config terpilih (df) |
|---|---|---|
| SDH-PPO + BC init | 1,55 (8) | 0,78 (1) |
| DDQN | 2,16 (8) | 0,40 (1) |
| DQN | 2,30 (8) | 1,23 (1) |
| PPO | 3,37 (8) | 3,06 (1) |
| SDH-PPO residual | 1,29 (8) | 0,80 (1) |
| SDH-PPO | 2,28 (8) | 0,87 (1) |

MDE pada N = 20, power 0.8, dua sisi, dalam poin persentase violation. CI 95% dari CI chi-square SD. Kolom alpha/23: Bonferroni lintas seluruh tes primer.

| Perbandingan | sigma_d | dasar | MDE @ alpha/m | CI 95% | MDE @ alpha | MDE @ alpha/23 | sigma_d berpasangan n=2 |
|---|---|---|---|---|---|---|---|
| (a) `demand_prop` on vs off | 0,19 | berpasangan, df 19 | 0,17 | [0,13; 0,25] | 0,13 | 0,19 | - |
| (a) `no_control` on vs off | 3,89 | berpasangan, df 19 | 3,53 | [2,69; 5,16] | 2,63 | 3,97 | - |
| (a) `equal_split` on vs off | 0,80 | berpasangan, df 19 | 0,72 | [0,55; 1,06] | 0,54 | 0,81 | - |
| (a) `threshold` on vs off | 0,30 | berpasangan, df 19 | 0,27 | [0,21; 0,39] | 0,20 | 0,30 | - |
| (a) PPO on vs off | 4,77 | rho = 0, df 8/8 | 4,33 | [2,93; 8,30] | 3,22 | 4,87 | - |
| (a) SDH-PPO on vs off | 3,22 | rho = 0, df 8/8 | 2,93 | [1,98; 5,61] | 2,18 | 3,29 | - |
| (a) DQN on vs off | 3,25 | rho = 0, df 8/8 | 2,95 | [1,99; 5,65] | 2,19 | 3,32 | - |
| (a) DDQN on vs off | 3,05 | rho = 0, df 8/8 | 2,77 | [1,87; 5,31] | 2,06 | 3,11 | - |
| (b) SDH-PPO+safety vs `demand_prop`+safety | 4,43 | rho = 0, df 8/19 | 2,99 | [2,21; 4,77] | 2,99 | 4,52 | 0,07 |
| (c) PPO, tiap pasangan arm (3x) | 4,77 | rho = 0, df 8/8 | 4,54 | [3,07; 8,70] | 3,22 | 4,87 | - |
| (c) SDH-PPO, tiap pasangan arm (3x) | 3,22 | rho = 0, df 8/8 | 3,07 | [2,07; 5,87] | 2,18 | 3,29 | - |
| (c) DQN, tiap pasangan arm (3x) | 3,25 | rho = 0, df 8/8 | 3,09 | [2,09; 5,92] | 2,19 | 3,32 | - |
| (c) DDQN, tiap pasangan arm (3x) | 3,05 | rho = 0, df 8/8 | 2,90 | [1,96; 5,56] | 2,06 | 3,11 | - |
| (e) SDH-PPO residual+safety vs `demand_prop`+safety | 4,01 | rho = 0, df 8/19 | 3,03 | [2,28; 4,60] | 2,71 | 4,10 | 0,14 |
| (e) SDH-PPO + BC init+safety vs `demand_prop`+safety | 4,10 | rho = 0, df 8/19 | 3,10 | [2,32; 4,76] | 2,77 | 4,19 | 0,16 |
| (d) SDH-PPO vs no_dueling [EKSPLORATIF] | 3,22 | rho = 0, df 8/8 | 2,18 (tanpa koreksi) | [1,47; 4,17] | 2,18 | - | - |
<!-- END GENERATED mde -->

### 8.2 Sensitivitas ambang SLA - EKSPLORATIF (K4)

Ambang SLA **tidak diubah**: `{p1: 6,0; p2: 70,0; p4: 7,0}` ms (`slice_env.py:59`). Evaluasi
menyimpan delay per langkah per port (`delay_p1`, `delay_p2`, `delay_p4` di setiap `*_eval.csv`,
juga di CSV skenario), dan meta tiap run kini mencatat `sla_ms`. Karena itu violation bisa
dihitung ulang pada ambang lain tanpa run ulang.

Rentang ditetapkan sekarang, sebelum hasil test ada: **0,5x, 0,75x, 1,5x, 2x** ambang tiap port,
diskalakan serentak untuk ketiga port. Dilaporkan sebagai EKSPLORATIF, tanpa Holm, di luar keluarga
(a), (b), (c), (e).

**Titik tambahan `real_train_median` (ditetapkan saat persetujuan, 2026-10-03):**
`{p1: 6,50; p2: 8,23; p4: 6,52}` ms, ditulis sebagai konstanta `REAL_TRAIN_MEDIAN` di
`scripts/analyze_v2.py`. Eksploratif, sama seperti titik pengali di atas. Catatan asal angka:
nilai ini adalah median delay terukur atas **seluruh** trace riil (1.022 baris, tabel di bawah),
bukan atas split train saja; median split train adalah 6,49 / 8,37 / 6,52 ms. Angkanya dipakai
persis seperti ditetapkan, dan selisih nama ini dicatat, bukan dikoreksi. Yang dipakai adalah
delay **ukur**, bukan hasil kebijakan apa pun, jadi tidak ada informasi hasil test yang masuk.

Batasan titik ini, sama dengan seluruh §8.2 tetapi lebih tajam: agen, reward, dan safety layer
dilatih dan bertindak dengan ambang 6/70/7. Analisis ini mengukur **ketahanan kebijakan** yang
sudah ada terhadap garis lain, bukan kinerja yang akan dicapai bila dilatih pada ambang
tersebut. Ambang utama tetap 6/70/7 (K4).

Batas tafsir: hanya **metriknya** yang di-threshold ulang. Kebijakan, reward, dan safety layer
selama training dan evaluasi tetap memakai ambang asli. Ini mengukur seberapa bergantung
peringkat metode pada letak garis, bukan bagaimana metode akan berperilaku bila dilatih dengan
ambang lain.

**Asal-usul ambang (A2) - temuan, dilaporkan, tidak diperbaiki.** Paper revisi
(`revisi/hasil-revisian/main.tex`, catatan Tabel slice) menyatakan ambang ini sebagai median delay
satu arah trace tanpa policing. Median dihitung ulang oleh `scripts/final_plan_stats.py`:

<!-- BEGIN GENERATED sla -->
| Sumber | baris | median P1 (ms) | median P2 (ms) | median P4 (ms) |
|---|---|---|---|---|
| **Ambang di `slice_env.py`** | - | 6,00 | 70,00 | 7,00 |
| trace riil `dataset_dqn_rich.csv` | 1022 | 6,50 | 8,23 | 6,52 |
| sintetis V1 `final/synthetic_15k_complete_final.csv` | 15000 | 6,07 | 70,77 | 6,88 |
| sintetis V1 `revision/drl_preprocessed_final.csv` | 14999 | 6,07 | 70,77 | 6,88 |
<!-- END GENERATED sla -->

Median trace riil tidak mereproduksi ambangnya, terutama P2. Median yang cocok muncul di dataset
sintetis WGAN V1. Jadi ambang P2 berasal dari data sintetis, bukan pengukuran.

Di luar asal-usulnya, ada ketidakcocokan besaran. Delay terukur didominasi offset jam (13,19%
sampel negatif, `03-measurement-campaign.md`). Delay di simulator adalah delay antrean murni
`backlog / rate`, yang nol saat tidak ada antrean. Ambang yang diturunkan dari satu besaran
diterapkan ke besaran lain. Paper harus menyatakan ambang ini sebagai titik operasi yang dipilih,
bukan turunan pengukuran. Kalimat di `revisi/hasil-revisian/main.tex` milik sesi lain dan tidak
disentuh.

### 8.3 Kurva belajar (C3)

Dari kolom `val_viol` di `*_train.csv`, 12 titik probe per run:

- rata-rata lintas 20 seed per metode, dengan pita CI 95% bootstrap atas seed;
- kurva **setiap** seed digambar tipis di belakangnya, supaya divergensi satu seed tidak
  tersembunyi di dalam rata-rata;
- titik `best_val_step` tiap seed ditandai.

Kurva ini dihitung atas himpunan probe, yaitu himpunan yang juga dipakai untuk **memilih**
checkpoint. Minimumnya karena itu optimis (gap probe ke eval §2.4), dan hal itu dinyatakan di
keterangan gambar.

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
   slicing **[belum diverifikasi]**.
2. **Flash crowd.** Lonjakan mendadak 3–5× pada satu slice selama 30–60 detik, lalu kembali.
   Dasar: lonjakan mendadak adalah kasus uji standar untuk mekanisme isolasi antar-slice;
   inilah kondisi ketika isolasi benar-benar diuji, bukan pada beban tunak **[belum diverifikasi]**.
3. **Kedatangan dan kepergian slice** - **TIDAK DIJALANKAN.** Slice masuk atau keluar di
   tengah episode, mengubah jumlah penuntut kapasitas. Dasar: multi-tenancy dinamis adalah premis
   network slicing **[belum diverifikasi]**. Alasan tidak dijalankan: ini satu-satunya dari ketiganya yang **bukan**
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
   tanpa koreksi Holm, dan tanpa masuk ke keluarga primer (a), (b), (c), (e).
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

## 11. Rujukan

Semua rujukan literatur di protokol ini **[belum diverifikasi]**: belum dibaca dari sumbernya, dan
judul, tahun, serta klaim yang dikaitkan padanya harus dicek sebelum masuk paper.

| Rujukan | Dipakai untuk | Status |
|---|---|---|
| Colas et al., 2018 (jumlah seed dan uji statistik untuk RL) | §8.1 power analysis | [belum diverifikasi] |
| Agarwal et al., 2021 (IQM, bootstrap CI, probability of improvement; `rliable`) | §8 butir 3 | [belum diverifikasi] |
| "Benchmarking of Synthetic Network Data", 2025 | §6.2 metrik fidelitas | [belum diverifikasi] |
| Literatur pola diurnal, flash crowd, dan slice dinamis (tanpa rujukan spesifik) | §9.1 | [belum diverifikasi] |

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

**2026-10-02: arm `full` tidak pernah memuat sintetis.** `full` = `real_only` di kode. Diperbaiki
sesuai §6 atas keputusan user. Seluruh tuning karena itu dijalankan pada data riil saja. Rinci
di §6.

**2026-10-02: probe membaca split evaluasi, bukan val.** Run final dengan `--eval-phase test` akan
memilih checkpoint di test. Diperbaiki sebelum run final; tuning tidak terdampak. Rinci di §2.2.

**2026-10-02: arm BC berlatih pada episode berbeda.** `bc_pretrain` memakai env training yang sama
dan menghabiskan sekitar 400 reset RNG-nya. Kini memakai salinan env (K2). Run tuning BC
dijalankan sebelum perbaikan ini; seleksinya tetap sah karena hanya urutan episode training yang
bergeser, bukan himpunan probe atau eval.

**2026-10-03: critic "dueling" adalah V(s) dengan centering per batch.** Tidak diubah. Family (d)
dipindah ke eksploratif. Rinci di §8.

**2026-10-03: asal-usul ambang SLA tidak cocok dengan klaim paper.** Dilaporkan di §8.2, ambang
tidak diubah (K4).

**2026-10-03: N naik dari 10 ke 20 (K1), Mann-Whitney diganti Wilcoxon signed-rank berpasangan
(K2, C1).** Ditetapkan sebelum sweep final dan sebelum test disentuh.

**2026-10-03: CSV mentah `results/tuning-v2/` gitignored (K5).** Konsisten dengan
`results/tuning/`. Arsip di luar repo:
`D:\Kuliah\Semester 6\Riset\sdn-iot-archive\tuning-v2-raw-csv.zip` (192 file), dengan
`tuning-v2-raw-csv.zip.sha256` (`318095abdc1b445c77c2076b7c5ec85ffd8174d730733a97f7cd988143b5bf84`)
dan manifest SHA256 per file `tuning-v2-raw-csv.manifest.sha256`. JSON per run, `selection.csv`,
dan `run.log` tetap di-track.

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
- **CRN dan seleksi di val:** `python scripts/check_crn.py` memeriksa bahwa ppo, sdhppo, dqn,
  ddqn, residual, dan BC berlatih pada urutan episode identik; bahwa probe dan eval berbagi himpunan
  episode, termasuk heuristik; bahwa probe membaca val apa pun `--eval-phase`-nya; dan bahwa
  `full` = 1.226 baris.
- **Antrean tuning:** `DRY=1 bash scripts/run_tuning.sh results/tuning-v2 12 2 300000` mengantrekan
  0 run.
