# Blocker — Variabel aksi tidak pernah divariasikan di testbed

Tanggal: 2026-09-24
Status: **MEMBLOKIR seluruh klaim kontrol/RL di paper**
Ditemukan saat: eksekusi Tahap 1 remediasi kebocoran data (STOP 3)

---

## Temuan

`Reinforcement Learning/revision/dataset_dqn_rich.csv` adalah satu-satunya data terukur di
repo ini: 1.022 baris, 37 kolom, rentang waktu **19 menit 59 detik** (mulai
2026-01-19T07:45:17Z, interval ~1,17 detik).

Di dalamnya, **variabel yang dikendalikan agen bernilai konstan**:

| Kolom | nunique | Nilai |
|---|---|---|
| `policing_rate_kbps_p1` | 1 | 1.000.000 |
| `policing_rate_kbps_p2` | 1 | 1.000.000 |
| `policing_rate_kbps_p4` | 1 | 1.000.000 |
| `policing_burst_kbps_p1/p2/p4` | 1 | 100.000 |
| `drop_p1` / `drop_p2` / `drop_p4` | 1 | 0 |
| `priority_tag_p1` / `p2` / `p4` | 1 | 0 / 0 / 1 |

Aksi didefinisikan di `Preprocessing.ipynb` cell 0 sebagai

```python
action_cont = (rate_t_plus_1 - rate_t) / rate_t
```

Karena `rate` konstan, seluruh 1.021 transisi menghasilkan aksi nol:

```
action_continuous dari data riil: nunique = 1, min = 0.0, max = 0.0, nonzero = 0
```

Testbed berjalan 20 menit dengan policing rate terkunci 1 Gbps (nilai default OVS, praktis
tanpa batas) pada seluruh port. Yang benar-benar bervariasi hanya `rx_mbps_*` dan `delay_ms_*`.

| Kolom | nunique | mean | std | min | max |
|---|---|---|---|---|---|
| `delay_ms_p1` | 195 | 6,595 | 0,382 | 6,425 | 12,512 |
| `delay_ms_p2` | 318 | 9,190 | 31,924 | 7,280 | 1028,601 |
| `delay_ms_p4` | 194 | 6,597 | 0,306 | 6,453 | 10,884 |
| `rx_mbps_p1` | 1009 | 3,852 | 1,324 | 0,310 | 8,039 |
| `rx_mbps_p2` | 1010 | 3,852 | 1,327 | 0,297 | 8,113 |
| `rx_mbps_p4` | 1009 | 4,574 | 1,336 | 0,339 | 8,772 |

---

## Konsekuensi

### 1. Tidak ada bukti observasional tentang efek aksi

Tidak ada satu pun pengamatan di repo ini tentang apa yang terjadi pada delay ketika policing
rate diubah, karena policing rate tidak pernah diubah. Nol eksperimen memanipulasinya.

Inilah sebab struktural mengapa evaluator berupa rumus karangan `d = raw × (1 − k·a)`
(`allModel4.ipynb:542-548`): tidak ada data untuk mengestimasi efek aksi, sehingga koefisien
`k` harus dikarang. Lalu `k` dibuat 1,5× lebih besar khusus untuk metode Proposed.

Urutan sebabnya penting: bias koefisien bukan penyebab masalah, melainkan **gejala** dari
ketiadaan data efek aksi.

### 2. Seluruh variasi aksi pada dataset lama adalah derau buatan

`DataAugmentation.ipynb` menimpa keluaran generator untuk kolom policing rate:

```python
df_synth[f'policing_rate_kbps_{p}'] = np.random.uniform(2000, 15000, 15000)
df_synth[f'policing_burst_kbps_{p}'] = df_synth[f'policing_rate_kbps_{p}'] * 0.1
```

Jadi rentang `action_continuous ∈ [−0,863, +6,320]` pada `drl_preprocessed_final.csv`:

- bukan hasil pengukuran — data riil memberi nol;
- bukan pula hasil belajar WGAN-GP — kolomnya ditimpa **setelah** generator berjalan.

Nilainya adalah `np.random.uniform` independen. Agen dilatih memprediksi derau seragam yang
tidak berkorelasi dengan state maupun reward.

Perhatikan skalanya: riil konstan 1.000.000 kbps, sintetis uniform 2.000–15.000 kbps. Dua
distribusi ini bahkan tidak beririsan — berbeda dua orde besaran.

### 3. Memperbaiki split data tidak menyembuhkan ini

Kebocoran WGAN-GP (STOP 3) adalah cacat nyata dan tetap perlu diperbaiki. Tetapi di bawahnya
ada kendala yang lebih mendasar:

> Kebijakan alokasi sumber daya tidak dapat dipelajari maupun dievaluasi dari data yang
> alokasi sumber dayanya tidak pernah divariasikan.

Arm `real_only` yang direncanakan akan memiliki aksi ≡ 0 pada seluruh baris. DQN/DDQN hanya
memakai satu bin; target aksi kontinu konstan nol. Tidak ada yang bisa dilatih maupun
dibandingkan.

### 4. Term `p_drop` pada reward adalah kode mati

`drop_p1 = drop_p2 = drop_p4 = 0` pada seluruh 1.022 baris, sehingga

```python
total_drop = row.get('drop_p1', 0) + row.get('drop_p2', 0) + row.get('drop_p4', 0)
p_drop = np.clip(total_drop, 0, 5)
```

selalu bernilai 0. Komponen ini tidak pernah memengaruhi reward.

Pada data sintetis, `drop_*` dihitung ulang oleh aturan buatan tangan
(`rx_mbps × 1000 > policing_rate`, selisihnya dibagi 80), sehingga satu-satunya sumber variasi
drop pun berasal dari policing rate acak di butir 2.

### 5. Ambang SLA tidak konsisten dengan data riil

`delay_ms_p4` riil bermean 6,597 ms, sedangkan ambang reward saat training 3,5 ms. Hampir
setiap baris riil melanggar SLA **by construction**, sebelum agen bertindak. Ambang evaluasi
7,0 ms duduk persis di sekitar mean, menjamin tingkat pelanggaran baseline mendekati 50%.

`delay_ms_p2` memiliki ekor sangat berat (mean 9,19 ms, std 31,9 ms, max 1028,6 ms) sementara
ambangnya 70 ms. Statistik mean pada distribusi seperti ini menyesatkan; median dan persentil
jauh lebih informatif.

---

## Yang tetap valid

Temuan ini tidak membatalkan pekerjaan Fase 0–1:

- `docs/experiments/00-contamination-audit.md` tetap akurat.
- `scripts/sweep.py` tetap port setia, dibuktikan 30/30 metrik oleh `scripts/check_fidelity.py`.
- Karakterisasi delay multi-slice dari 1.022 baris riil tetap data yang sah.

Yang gugur adalah premis bahwa terdapat data pendukung untuk klaim kontrol adaptif.

---

## Arah yang diputuskan

Pemilik penelitian memilih **kombinasi dua jalur**:

1. **Kampanye pengukuran baru** yang menyapu policing rate pada testbed fisik, merekam delay
   dan throughput per port. Satu-satunya cara memperoleh data efek aksi yang nyata.
2. **Simulator berprinsip** (model antrean / token bucket) yang **dikalibrasi pada hasil sweep
   itu**, lalu divalidasi pada titik sweep yang di-hold-out.

Kombinasi ini lebih kuat daripada salah satunya sendirian: simulator memperoleh dasar empiris
alih-alih koefisien karangan, dan pengukuran memperoleh jangkauan yang tidak mungkin dicapai
hanya dengan eksperimen fisik. Kesalahan simulator terhadap titik hold-out menjadi angka yang
dapat dilaporkan, bukan asumsi yang disembunyikan.

Pembagian kerja: kampanye pengukuran dijalankan pemilik penelitian di testbed fisik; tooling
sweep, protokol, dan simulator disiapkan di repo ini.

## Langkah berikutnya

1. Petakan jalur kontrol (bagaimana OVS meter / policing rate di-set oleh aplikasi Ryu) dan
   jalur pengukuran (bagaimana delay dihitung) dari kode di `flowvisor/` dan `pengujian/`.
2. Tulis protokol kampanye pengukuran: grid rate, dwell time, pengulangan, urutan acak untuk
   menghindari perancu drift waktu, dan skema keluaran.
3. Bangun driver sweep yang dapat dijalankan pemilik penelitian di testbed.
4. Bangun simulator dan kalibrasinya setelah data sweep tersedia.
