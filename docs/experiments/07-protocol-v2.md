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

> **Hasil pilot dan angka `max_steps` terpilih diisi di sini setelah pilot selesai.**
> Kurva: `results/pilot/`.

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
| `threshold` | `a_p = clip(delay_p / sla_p − 1, −1, +1)` |

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

## Verifikasi protokol

- `--phase test` dan `--eval-phase test` menolak berjalan tanpa `--allow-test`.
- Hash `results/tables/per_seed_summary.csv` (V1) tetap identik.
- Self-check `slice_env` lolos 6 properti setelah alokasi awal diacak.
- Smoke test seluruh sel faktorial lolos sebelum sweep penuh.
- Pilot dan smoke test hanya menulis ke `results/pilot/` dan `results/smoke/`.
