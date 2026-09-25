# Protokol Eksperimen V2

Tanggal: 2026-09-25
Status: **draf, menunggu persetujuan.** Sweep final belum dijalankan; test split belum disentuh.
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

16 run selesai. Kurva val (total violation %, rata-rata 2 seed × 2 level safety):

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

Dua pola yang berbeda:

- **PPO dan SDH-PPO nyaris tidak belajar.** Bergerak dari ~48 ke ~45 lalu berosilasi dalam pita
  44–48 sepanjang 300k step. Tidak ada tren jelas setelah 25k.
- **DQN dan DDQN belajar, lalu memburuk.** Optimum val di 175k (DQN 33,60) dan 150k
  (DDQN 34,13), setelah itu naik kembali ke 40–41 pada 275k — pola divergensi overestimasi yang
  khas.

### 2.2 DIGANTI — seleksi checkpoint menggantikan anggaran global

> Aturan 175.000 step di bawah **tidak lagi berlaku**. Lihat §2.4.

Aturan yang berlaku:

- Batas atas **300.000 step, sama untuk semua metode**.
- Probe val tiap **25.000 step** (5 episode).
- **Checkpoint dengan val terbaik disimpan dan dipulihkan** di akhir training; step terpilih
  dicatat di metadata tiap run sebagai `best_val_step`.

Alasan penggantian: anggaran global tunggal memaksa kompromi. 175k adalah optimum DQN tetapi
memotong PPO sebelum nilai terbaiknya, sementara 300k merugikan DQN/DDQN 6–8 poin karena
divergensi pasca-optimum. Seleksi checkpoint memberi tiap metode titik terbaiknya sendiri tanpa
menguntungkan metode mana pun: batas step, frekuensi probe, dan split evaluasi identik.
Pemilihan dilakukan pada val, tidak pernah pada test.

Terverifikasi: run uji memilih step 6144, bukan step terakhir 8192.

### 2.3 (arsip) Anggaran 175.000 step — tidak dipakai lagi

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

### 2.4 Hasil tuning anggaran setara

64 run selesai: 4 metode × 8 konfigurasi × 2 seed, anggaran identik (300k step, seleksi
checkpoint), dilatih pada train dan dipilih pada val. Safety layer dimatikan agar efek
hyperparameter tidak tercampur.

**Konfigurasi terpilih:**

| Metode | Konfigurasi terbaik | Val viol % (sd) |
|---|---|---|
| DQN | `lr 3e-4, target_sync 500, bins 11, eps_decay 100k` | **37,42** (0,59) |
| DDQN | `lr 3e-4, target_sync 2000, bins 21, eps_decay 100k` | **38,80** (0,47) |
| PPO | `lr 3e-4, ent_coef 0,01, clip, reward_scale 19,0106` | **51,87** (3,58) |
| SDH-PPO | `lr 3e-4, ent_coef 0,01, clip, reward_scale 19,0106` | **51,77** (0,38) |

`lr = 3e-4` menang pada keempat metode — satu-satunya faktor yang konsisten.

**Dua hipotesis diagnostik TIDAK didukung tuning.** Ini penting dicatat apa adanya:

1. **`tanh` tidak menolong.** Diagnosis menunjukkan densitas Gaussian-di-clip salah spesifikasi
   dan 32,5% aksi tersaturasi, sehingga `tanh` dengan koreksi Jacobian diharapkan memperbaiki.
   Ternyata konfigurasi terbaik untuk **kedua** varian PPO justru memakai `clip`. Mis-spesifikasi
   itu nyata, tetapi bukan kendala yang mengikat.
2. **Bonus entropi bukan biang keladinya.** Diagnosis menunjukkan entropi naik sepanjang
   training dan menduga `ent_coef` mengalahkan gradien kebijakan. Ternyata `ent_coef = 0,01`
   menang atas `ent_coef = 0` pada kedua varian PPO.

**PPO justru memburuk dengan data lengkap.** Pada 46 run parsial, PPO terbaik tampak 48,73
(n=1); dengan 2 seed penuh menjadi 51,87. Angka n=1 itu derau. Ini juga peringatan bahwa 2 seed
masih tipis — sd mencapai 7,85 (DQN `lr1e-4`) dan 6,29 (PPO).

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
| `demand_prop` | **32,4** |
| BC dari aktor PPO | 33,2 |
| `no_control` + safety | 35,0 |
| DQN (tuned) | 37,4 |
| DDQN (tuned) | 38,8 |
| `equal_split` + safety | 40,1 |
| SDH-PPO (tuned) | 51,8 |
| PPO (tuned) | 51,9 |
| `threshold` | 67,0 |

**Tidak satu pun metode learning mengalahkan heuristik satu baris**, bahkan setelah tuning
anggaran setara dan seleksi checkpoint. Jarak terbaik-learner ke `demand_prop` adalah 5 poin,
berbalik merugikan metode learning.

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

### 4.2 Aturan `threshold` cacat — catatan lengkap

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

### 4.1 Jawaban lengkap item 2 — `const_max` = `no_control`

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

---

## 7. Jumlah run dan estimasi waktu

10 seed per konfigurasi.

| Blok | Run |
|---|---|
| 8 metode × 2 safety × 10 seed (arm `full`) | 160 |
| 4 learner × 2 arm tambahan × 2 safety × 10 seed | 160 |
| `sdhppo` `no_dueling` × 2 safety × 10 seed | 20 |
| **Total** | **340** (260 learner, 80 heuristik) |

Heuristik praktis instan (<1 detik). Estimasi learner bergantung `max_steps` hasil pilot:

| `max_steps` | Rata-rata per run | Serial | 12 proses paralel |
|---|---|---|---|
| 100k | ~17 menit | 74 jam | **~6 jam** |
| 150k | ~25 menit | 108 jam | **~9 jam** |
| 300k | ~50 menit | 217 jam | **~18 jam** |

Bila terlalu lama, ruang pemangkasan paling wajar adalah arm augmentasi (menghemat 160 run).

---

## 8. Perbandingan primer

Koreksi Holm diterapkan **di dalam tiap keluarga**, bukan lintas keluarga.

| Keluarga | Perbandingan | Jumlah |
|---|---|---|
| **(a)** Efek safety layer | on vs off, per metode | 8 |
| **(b)** Proposed+safety vs demand_prop+safety | 1 | 1 |
| **(c)** Efek augmentasi | `full` vs `real_only` vs `aug_subsample`, per learner | 12 |
| **(d)** Efek dueling | `sdhppo` `full` vs `no_dueling` | 1 |

Metrik primer: **total violation rate** (rata-rata violation lintas tiga slice).
Metrik sekunder: violation per slice, delay rata-rata per slice, total drop, reward.

Uji: Mann-Whitney U (tidak mengasumsikan normalitas, n=10) dan Welch's t sebagai pendamping;
effect size rank-biserial; CI 95% bootstrap. Selisih tidak signifikan dilaporkan apa adanya.

**Seluruh perbandingan lain berlabel EKSPLORATIF** dan dilaporkan tanpa klaim signifikansi.

---

## 9. Analisis sekunder — DITULIS, TIDAK DIJALANKAN

### 9.1 Skenario trafik non-stasioner

Trace saat ini hanya 20 menit dengan satu pola, dan sudah menunjukkan gradien beban 21%. Tiga
skenario berikut menguji ketahanan terhadap perubahan rezim yang lebih tajam.

1. **Ramp diurnal.** Beban diskalakan mengikuti profil harian (rendah malam, puncak siang).
   Dasar: pola diurnal adalah karakteristik yang paling konsisten dilaporkan pada trafik seluler
   dan IoT, dan menjadi motivasi utama penskalaan sumber daya elastis pada literatur network
   slicing.
2. **Flash crowd.** Lonjakan mendadak 3–5× pada satu slice selama 30–60 detik, lalu kembali.
   Dasar: lonjakan mendadak adalah kasus uji standar untuk mekanisme isolasi antar-slice;
   inilah kondisi ketika isolasi benar-benar diuji, bukan pada beban tunak.
3. **Kedatangan dan kepergian slice.** Slice masuk atau keluar di tengah episode, mengubah
   jumlah penuntut kapasitas. Dasar: multi-tenancy dinamis adalah premis network slicing;
   kebijakan yang hanya baik pada himpunan slice tetap belum menjawab masalah sebenarnya.

Ketiganya dibangkitkan sebagai transformasi atas trace train, dan dievaluasi dengan kebijakan
yang sudah dilatih (tanpa pelatihan ulang) untuk mengukur generalisasi di luar distribusi.

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

## Verifikasi protokol

- `--phase test` dan `--eval-phase test` menolak berjalan tanpa `--allow-test`.
- Hash `results/tables/per_seed_summary.csv` (V1) tetap identik.
- Self-check `slice_env` lolos 6 properti setelah alokasi awal diacak.
- Smoke test seluruh sel faktorial lolos sebelum sweep penuh.
- Pilot dan smoke test hanya menulis ke `results/pilot/` dan `results/smoke/`.
