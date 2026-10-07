# Protokol V3: Studi lanjutan setelah hasil V2

**Status:** draf, belum dikunci. Protokol berlaku setelah di-commit dan di-tag `protocol-v3-final`, dan tag itu harus dibuat **sebelum** run V3 mana pun dijalankan.

**Posisi terhadap V2:** protokol ini ditulis setelah hasil V2 dibuka (tag `results-v2`). Semua hipotesisnya berasal dari pengamatan eksploratif V2 atau dari temuan konfirmatori V2 yang belum dijelaskan. Karena itu:
- V2 tetap menjadi hasil konfirmatori utama dan dilaporkan apa adanya;
- V3 dilaporkan sebagai studi lanjutan yang dirancang setelah V2, tetapi dikunci sebelum datanya ada.

---

## 0. Gerbang sebelum tag

| Gerbang | Isi | Status |
|---|---|---|
| G1 | `scripts_v3/run_v3.py` mereproduksi `_eval.csv`, `_eval_diurnal.csv`, dan `_eval_flash.csv` arsip V2 secara identik per baris untuk tiga run verifikasi | lolos: 9 file (3 run × `_eval`, `_eval_diurnal`, `_eval_flash`) byte-identik dengan `sdn-iot-archive/final-v2-raw-csv.zip`, 1.000 baris masing-masing, 0 baris berbeda, argumen sama dengan V2 (`scripts_v3/verify_v2_repro.py`, 2026-10-06) |
| G2 | CRN skenario untuk seed 20–39 (dqn, ddqn, demand_prop, arm baru) | lolos (`check_crn_scenarios.py`); diulang 2026-10-06 setelah `moment_matched` ditambahkan: lolos untuk `var_matched` dan `moment_matched`, per arm 280 reset training dan 3.600 reset evaluasi |
| G3 | Statistik input arm `moment_matched` dicatat (mean, std, ACF lag 1 per port, jumlah baris ter-clip) | lolos: mean 3,4107 / 3,4198 / 4,1425, std 0,3230 / 0,3337 / 0,3324, ACF lag 1 0,8883 / 0,8884 / 0,8773 (p1 / p2 / p4); 0 dari 613 baris ter-clip (`scripts_v3/arm_input_stats.py`) |
| G4 | `scripts_v3/analyze_v3.py` sudah ditulis, diuji struktur keluarannya, dan di-commit | lolos: uji struktur dengan data V2 seed 0–19 dan data tiruan berlabel untuk arm baru menghasilkan 4 / 6 / 8 perbandingan dengan m = 4 / 6 / 8 dan n = 20; keluaran uji dihapus; di-commit bersama tag ini |
| G5 | MDE tiap keluarga dihitung dari V2 dan dicatat di §7 | lolos: lihat bagian 7 (`scripts_v3/mde_v3.py`) |

Kalau G1 gagal, V3 tidak dijalankan sama sekali. Kegagalannya dilaporkan, dan kode V2 tidak diubah untuk memperbaikinya.

---

## 1. Pertanyaan

- **Q1:** Apakah pengamatan eksploratif V2, yaitu DQN dan DDQN tanpa safety layer memiliki `viol_total` lebih rendah daripada `demand_prop` di skenario diurnal, bereplikasi pada seed training yang independen?
- **Q2:** Apakah safety layer menaikkan `viol_total` kebijakan yang kinerjanya baik di skenario diurnal dan flash?
- **Q3:** Faktor apa di trace sintetis yang menjelaskan efek arm `aug_subsample` (sintetis saja) pada DQN dan DDQN di test?

---

## 2. Yang tidak berubah dari V2

Semua hal berikut sama persis dengan V2 (07, 08):
- environment, kapasitas C, buffer, dan reward;
- split temporal;
- hyperparameter terpilih (`results/tuning-v2/selection.csv`);
- 300.000 step, probe val tiap 25.000 step (20 episode), checkpoint val terbaik, evaluasi test 20 episode;
- definisi skenario diurnal dan flash;
- ambang SLA;
- definisi `viol_total` (`analyze_v2.py:66`).

Kode V2 tidak diubah. Semua run dijalankan lewat `scripts_v3/run_v3.py`, yang juga menyimpan checkpoint.

---

## 3. Seed

Seed 20–39 (N = 20). Seed 0–19 tidak dipakai dalam uji V3 karena sudah membentuk hipotesis. Data V2 dan V3 tidak digabung untuk uji konfirmatori. Penggabungan deskriptif boleh dilakukan, dengan label "deskriptif, gabungan V2+V3".

---

## 4. Sel

**Blok A (Q1, Q2):**

| Metode | Arm | Safety |
|---|---|---|
| dqn, ddqn | aug_subsample, full, real_only | off |
| dqn, ddqn | aug_subsample | on |
| demand_prop | (arm tidak relevan, identifier V2 `full`) | off, on |

**Blok B (Q3):**

| Metode | Arm | Safety |
|---|---|---|
| dqn, ddqn | var_matched, moment_matched | off |

Sel `aug_subsample` dan `real_only` dengan safety off di Blok A juga dipakai di Q3, dengan seed yang sama, sehingga perbandingannya berpasangan.

**Total:** 240 run learning (120 dqn, 120 ddqn) dan 40 run heuristik.

Sel lain tidak dijalankan. Sel yang tidak melayani hipotesis membuka peluang analisis post hoc.

### Definisi arm baru
Semua statistik dihitung dari 613 baris riil train dan dari trace sintetis upaya 1. Tidak ada statistik dari val maupun test.
- **`var_matched`:** `x' = μ_r + (x − μ_r) · σ_s/σ_r` per port. Mean dan struktur temporal mengikuti data riil, std mengikuti data sintetis.
- **`moment_matched`:** `x' = μ_s + (x − μ_r) · σ_s/σ_r` per port. Mean dan std mengikuti data sintetis, struktur temporal mengikuti data riil.

Pada kedua arm, nilai negatif di-clip ke 0 dan jumlah baris yang ter-clip dicatat. μ dan σ adalah mean dan std per port; r = riil train, s = sintetis.

---

## 5. Endpoint

Endpoint per run adalah `viol_total` (`analyze_v2.py:66`), yaitu rata-rata dari 20 episode evaluasi, sama seperti V2.
- Q1 dan Q2 memakai `viol_total` pada skenario yang disebut.
- Q3 memakai `viol_total` pada test tanpa skenario.

---

## 6. Hipotesis dan uji

Ketentuan untuk semua keluarga:
- uji Wilcoxon signed-rank berpasangan per seed, dua sisi, α = 0,05, dengan koreksi Holm di dalam keluarga;
- dilaporkan: selisih rata-rata, CI 95% bootstrap selisih berpasangan (10.000 resample), dan rank-biserial;
- klaim "tidak berbeda" dilaporkan sebagai CI, bukan sebagai kesetaraan.

### Keluarga H1: replikasi diurnal (4 perbandingan)
Skenario diurnal, safety off. Perbandingan {dqn, ddqn} × {aug_subsample, full} masing-masing terhadap `demand_prop`.

- **Prediksi:** violation learner lebih rendah.
- **Kriteria replikasi:** signifikan setelah Holm **dan** selisihnya searah prediksi.
- Sel `real_only` dilaporkan secara deskriptif dengan CI, di luar keluarga.
- Skenario flash dilaporkan secara deskriptif saja, karena V2 tidak memberi dasar untuk prediksi arah di flash.

### Keluarga H2: efek safety layer di skenario (6 perbandingan)
Perbandingan safety on vs off untuk dqn `aug_subsample`, ddqn `aug_subsample`, dan `demand_prop`, masing-masing di diurnal dan di flash.

- **Prediksi:** violation dengan safety on lebih tinggi.
- Efek safety di test tanpa skenario tidak diuji ulang, karena sudah diuji di V2 keluarga (a).

### Keluarga H3: dekomposisi efek data sintetis (8 perbandingan)
Test tanpa skenario, safety off. Untuk dqn dan ddqn masing-masing ada empat perbandingan:

1. replikasi: `aug_subsample` vs `real_only`;
2. langkah variansi: `var_matched` vs `real_only`;
3. langkah mean: `moment_matched` vs `var_matched`;
4. langkah residual: `aug_subsample` vs `moment_matched`.

**Aturan tafsir (ditetapkan sekarang):**
- Kalau perbandingan 1 tidak bereplikasi untuk suatu metode, dekomposisi metode itu dilaporkan deskriptif saja, tanpa klaim mekanisme.
- Suatu faktor disebut berkontribusi hanya jika langkahnya signifikan setelah Holm **dan** selisihnya menurunkan violation.
- Langkah yang CI-nya memuat nol dilaporkan sebagai "tidak terdeteksi", disertai CI.
- Kalau langkah residual signifikan, sisa perbedaannya hanya boleh disebut "perbedaan lain antara trace sintetis dan data riil yang tidak didekomposisi", misalnya struktur temporal, bentuk distribusi, atau sambungan antar-jendela 50 baris. Faktor-faktor ini tidak dibedakan satu sama lain.
- Dekomposisi ini berurutan. Urutan lain bisa memberi atribusi berbeda kalau ada interaksi antarfaktor. Hal ini dicatat sebagai keterbatasan.

Hasil Blok B di skenario diurnal dilaporkan deskriptif.

---

## 7. Daya statistik

MDE untuk tiap keluarga dihitung **sebelum tag**, dari SD selisih berpasangan V2 (seed 0–19) pada sel yang sesuai, dengan N = 20, α Holm terburuk di keluarga, dan daya 0,8. Untuk sel yang tidak ada di V2 (arm baru), dipakai batas konservatif ρ = 0, seperti di V2.

| Keluarga | MDE | Dasar |
|---|---|---|
| H1 | 2,37 sampai 5,58 poin | SD selisih berpasangan V2 seed 0–19 (df 19) pada `scen_diurnal`; α = 0,05/4; paired t eksak (noncentral t) dikali sqrt(1/0,955), metode yang sama dengan 07 bagian 8.1 |
| H2 | 0,45 sampai 2,87 poin | SD selisih berpasangan V2 seed 0–19 (df 19) pada `scen_diurnal` dan `scen_flash`; α = 0,05/6 |
| H3 | 3,78 sampai 7,14 poin | Langkah 1: SD selisih berpasangan V2 seed 0–19 (df 19) pada `viol_total`. Langkah 2–4: ρ = 0, σ arm baru = SD terbesar V2 metode itu di antara `aug_subsample`, `full`, `real_only` safety off (untuk dqn dan ddqn: `aug_subsample`), keputusan 2026-10-06; α = 0,05/8 |

---

## 8. Analisis

- Semua uji dijalankan oleh `scripts_v3/analyze_v3.py`, yang di-commit sebelum tag (G4).
- Sebelum tag, skrip hanya diuji pada data V2 untuk memeriksa struktur keluaran. Hasil uji itu tidak dipakai sebagai hasil V3.
- Tabel dan angka di paper dibangkitkan dari skrip, seperti di V2.

---

## 9. Pelaporan

- Semua hasil V3 dilaporkan, apa pun arahnya.
- Paper menyebut V3 sebagai studi lanjutan yang dirancang setelah hasil V2 dan dikunci sebelum dijalankan.
- Analisis di luar §6 diberi label eksploratif.

---

## 10. Aturan berhenti

1. Sweep dijalankan sekali.
2. Run yang gagal karena crash dijalankan ulang dengan seed yang sama, dan setiap pengulangan dicatat. Run yang selesai tidak diulang.
3. Setelah tag, tidak boleh menambah sel, seed, arm, skenario, maupun mengubah hyperparameter.
4. Setiap deviasi dicatat beserta tanggal dan alasannya di `10-results-v3.md`.
5. Checkpoint V3 tidak dievaluasi pada skenario atau trace lain kecuali dengan label eksploratif.

---

## 11. Eksekusi

- Perkiraan biaya dari durasi V2: dqn 120 × 50,7 menit dan ddqn 120 × 58,6 menit, total sekitar 218 jam-run. Dengan sekitar 14 proses paralel, kira-kira 16 jam wall clock. Angka per run dari V2 adalah batas atas (`operations.log:3-13`).
- Power throttling Windows dimatikan selama sweep dan dikembalikan sesudahnya.
- Jangan menjalankan eksperimen lain (termasuk gnn-mappo) secara bersamaan kalau waktu menjadi pertimbangan. Hasil tidak terpengaruh karena semua run ber-seed.
- Semua kejadian operasional dicatat di `results/v3/operations.log`.

## 12. Keluaran

- Hasil mentah: `results/v3/`.
- Checkpoint: `results/v3/checkpoints/`.
- Hasil dan deviasi: `docs/experiments/10-results-v3.md`.
- Arsip CSV mentah beserta SHA256 dan manifest, seperti V2.
