# Handoff SDH-PPO: hasil V2 selesai, paper menunggu bingkai

Tanggal: 2026-10-06
Untuk: sesi Claude Code berikutnya di repo ini
Commit terakhir saat ditulis: `579f48f`. Tag: `protocol-v2-final` (b732904), `results-v2` (a42e755).

Dokumen ini operasional. Isinya hal yang tidak terbaca dari kode atau git history: aturan user yang
masih berlaku, status, file mana yang benar, dan jebakan yang sudah memakan waktu. Handoff lama
(2026-10-02, sebelum sweep final) sudah ditimpa; isinya ada di git history (`0752c76`).

Dokumen pendamping, urut baca:

1. `docs/experiments/07-protocol-v2.md`: protokol beku, termasuk daftar deviasi tercatat.
2. `docs/experiments/08-results-v2.md`: hasil sweep final, semua tabel dibangkitkan skrip.
3. `revisi/hasil-revisian/revision-status-v2.md`: status 34 item reviewer, inventaris Fig. 1/2,
   catatan keterbatasan yang menunggu §IV.D.

## 1. Status

| Bagian | Status |
|---|---|
| Sweep final V2 (760 run, 38 sel x 20 seed, split test, CPU, 300k step) | selesai, 0 gagal |
| Analisis beku `analyze_v2.py` | dijalankan sekali, tanpa modifikasi |
| C4 fidelitas generator (deviasi tercatat, train/val saja) | selesai, commit `391b8af` |
| `08-results-v2.md` | selesai, tag `results-v2` |
| Paper `revisi/hasil-revisian/main.tex` | fakta desain V2 selesai; klaim dan prosa hasil menunggu bingkai |
| Split test | sudah dibuka sekali di sweep final. **Jangan dibuka lagi.** |

Kesimpulan utama sudah ada di `08-results-v2.md` §1 dan tidak boleh diringkas ulang dengan angka
ketikan: Proposed (SDH-PPO + safety) tidak mengalahkan `demand_prop`. Laporkan apa adanya.

**Gate saat ini: bingkai paper.** Pembimbing belum memutuskan bingkai (framing) paper. Semua
bagian bertanda `\textcolor{red}{[REWRITE: menunggu bingkai]}` dan semua prosa `\textcolor{red}{[V2]}`
menunggu keputusan itu. Jangan menulis narasi klaim sebelum user memberi bingkai.

## 2. Aturan berdiri dari user

1. Jangan pernah menulis angka hasil secara manual, di mana pun. Semua angka dari skrip yang membaca
   CSV. Berlaku juga untuk paper: tabel lewat `\input{tables/v2_*.tex}`, angka fakta lewat skrip
   ter-commit (mis. `scripts/sla_medians.py`).
2. Tidak ada tuning berdasarkan hasil, tidak ada cherry-pick seed, tidak ada ubah ambang setelah
   melihat hasil.
3. Kode yang menghasilkan angka sintetis, hardcode, atau mock: laporkan, jangan perbaiki diam-diam.
4. Kalau Proposed kalah, laporkan apa adanya.
5. Hormati setiap STOP. Kalau keputusan tidak bisa diterapkan persis, berhenti dan laporkan.
6. Tidak ada run baru dan analisis baru tanpa izin eksplisit. Ide setelah protokol beku berlabel
   EKSPLORATIF, tanpa klaim signifikansi (protokol §10).
7. Koreksi label/fakta setelah sweep dicatat sebagai deviasi di 07 dan 08, bukan ditimpa diam-diam.
8. Kalau premis user keliru menurut data, katakan dengan fakta dan skrip sumbernya.

## 3. Batasan sesi

- Semua run `--device cpu`.
- Jangan commit `Reinforcement Learning/final/allModel1.ipynb` (dimodifikasi lokal, bukan milik
  kampanye ini).
- Jangan sentuh `revisi/hasil-revisian/jawaban-reviewer.md` (untracked, masih menjelaskan V1),
  Revision Form, atau isi bagian bertanda REWRITE. Bagian REWRITE cukup dilaporkan.
- Paper: commit hanya `main.tex`, `tables/`, `figures/` (yang V2), `IEEEtran.cls`,
  `revision-status-v2.md`. PDF/aux/log tidak di-commit.
- Komunikasi ke user dalam Bahasa Indonesia, ringkas. Kode dan commit message dalam bahasa Inggris.
- Setiap putaran paper diakhiri: compile dari clone bersih, commit, laporkan.

## 4. Peta file

**Eksperimen**

| Path | Isi |
|---|---|
| `scripts/slice_env.py` | simulator queueing; drop = luapan buffer (Mb), baris 218; reward 237-247 |
| `scripts/train_online.py` | training/eval; skala observasi tetap baris 68-83 |
| `scripts/run_final.py` | driver sweep final (beku) |
| `scripts/analyze_v2.py` | analisis beku. Kolom `sens_real_train_median` salah nama: nilainya median trace penuh (deviasi 2026-10-05, 07 §8.2) |
| `scripts/fill_results_v2.py` | mengisi blok GENERATED di 08 |
| `scripts/fidelity_c4.py` | C4: KS, W1, ACF, AUC; train/val saja |
| `results/final-v2/` | log, JSON, `operations.log`; CSV mentah di arsip |
| `results/analysis-v2/` | seluruh keluaran analisis + `fidelity_c4*` |
| `../sdn-iot-archive/` (di luar repo) | `final-v2-raw-csv.zip` (2.880 CSV) dan `tuning-v2-raw-csv.zip`, masing-masing dengan `.sha256` dan manifest |

**Paper** (`revisi/hasil-revisian/`)

| Path | Isi |
|---|---|
| `main.tex` | paper; 12 persamaan, penomoran lewat `\ref` |
| `tables/v2_{cells,primary,exploratory,fidelity}.tex` | dari `scripts/paper_tables_v2.py` |
| `figures/fig3_fidelity_v2.png`, `fig4_seed_distribution_v2.png` | dari `scripts/paper_figures_v2.py`, 300 dpi |
| `figures/fig1_architecture.png`, `fig2_framework.png` | asli 96 dpi, belum digambar ulang (E2) |
| `revision-status-v2.md` | status reviewer + keterbatasan |
| `obsolete-v1/` (untracked) | kedua xlsx V1, dipindah utuh |
| `README.md` (untracked) | banner OBSOLETE, isinya V1 |
| `fig3_tsne.png`, `fig4_seed_distribution.png` (untracked) | gambar V1, arsip lokal |

`scripts/sla_medians.py` adalah sumber angka fakta paper: ambang SLA, median delay (trace penuh,
split train, sintetis V1), delay negatif per port dan per format log, rentang waktu trace, kolom drop
trace, dan policing rate.

## 5. Perintah

```bash
python scripts/analyze_v2.py          # jangan diubah; hanya untuk reproduksi
python scripts/fidelity_c4.py
python scripts/fill_results_v2.py     # blok GENERATED di 08
python scripts/paper_tables_v2.py     # tabel paper
python scripts/paper_figures_v2.py    # Fig. 3 dan Fig. 4
python scripts/sla_medians.py         # angka fakta paper
```

Compile dari clone bersih (pola yang dipakai tiap putaran):

```bash
git clone -q --no-checkout <repo> <scratch>/clean && cd <scratch>/clean
git sparse-checkout set revisi/hasil-revisian scripts pengujian \
  "Reinforcement Learning/revision" "Reinforcement Learning/final"
git checkout -q main
cd revisi/hasil-revisian && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

Lolos bila tidak ada baris `!` di log dan tidak ada referensi/sitasi undefined. Overfull kecil yang
sudah ada sejak awal: Table I (baris 133, 145), Table II (216-225), `v2_cells` (2,76 pt).

## 6. Pekerjaan terbuka

**Menunggu bingkai (jangan dikerjakan tanpa keputusan user):**

- Lima penanda REWRITE: paragraf T4 (Introduction), daftar kontribusi, baris "This work" Table I,
  paragraf T3 (Related Work), §IV.D Limitations.
- Semua prosa `[V2]`: abstrak, §IV.A-C, kesimpulan.
- Item reviewer B2, C7, N5; form usang A1, C1-C5 (Revision Form dan Compliance Check harus ditulis
  ulang setelah bingkai).

**Yang harus ikut diperbaiki saat REWRITE dikerjakan:**

- §IV.D masih menulis "13.19 percent of one-way delay samples in the collected trace are negative".
  Salah untuk trace yang dipakai (0 negatif). Samakan dengan §III-E: nilai negatif hanya di log
  mentah format 4 kolom, 14-17 Jan 2026, sebelum trace 19 Jan; sinkronisasi jam tidak diverifikasi.
- §IV.D masih menyebut "measured delay" sebagai ground truth.
- T4 (baris ~88) menyebut "Raspberry Pi single-board computers" (jamak). Testbed memakai satu
  Raspberry Pi 5 untuk ketiga sektor; gateway per sektor hanya rancangan deployment.
- Keterbatasan (a) gateway bersama dan (b) delay negatif/offset jam: teksnya di
  `revision-status-v2.md` §"Catatan keterbatasan".

**Terbuka, tidak bergantung bingkai:**

- E2: Fig. 1/2 hanya 96 dpi, tidak ada sumber vektor. Jangan di-upscale palsu.
- Batas halaman ICoICT tidak ditemukan di repo. Paper 14 halaman. Jangan menebak; minta user cek
  CFP.
- Blok penulis masih placeholder.
- Docstring `scripts/slice_env.py` (~baris 19) masih menulis delay negatif secara umum. Kode,
  belum diubah.

## 7. Fakta yang sering salah

- **Median.** Titik sensitivitas memakai median trace penuh (1.022 baris), bukan median split train.
  Label sudah dikoreksi sebagai deviasi. Ambang P2 70 ms berasal dari median dataset sintetis V1,
  bukan pengukuran.
- **Delay negatif.** Trace yang dipakai (`Reinforcement Learning/revision/dataset_dqn_rich.csv`,
  19 Jan 2026) tidak memuat delay negatif. Angka 13,19% berasal dari log mentah
  `pengujian/delay_log.csv`, seluruhnya di baris format 4 kolom sebelum trace dikumpulkan.
- **Drop.** Kolom drop trace bernilai 0 di semua baris (policing tetap 1.000.000 kbps). Drop di V2
  hanya ada di simulator.
- **Testbed.** Satu Raspberry Pi 5 sebagai gateway untuk P1, P2, P4. Testbed fisik sudah dibongkar;
  tidak ada pengukuran baru yang mungkin.
- **Learner.** Enam: PPO, SDH-PPO, DQN, DDQN (double + dueling), SDH-PPO residual, SDH-PPO + BC init.
  Baseline: No Control, Equal Split, Threshold, Demand Proportional. Const Max dihapus (= No Control).
- **Uji.** Wilcoxon signed-rank berpasangan, Holm di dalam keluarga (a) m=8, (b) 1, (c) 12,
  (e) 2; (d) dueling eksploratif. Bukan Mann-Whitney, bukan 10 seed (itu rencana lama).

## 8. Jebakan yang sudah memakan waktu

- **Windows power throttling.** Proses CPU yang dilepas (detached) dicekik sekitar 2,7x. Perbaikan:
  `SetProcessInformation(ProcessPowerThrottling)` per PID, diulang untuk worker baru. Prioritas
  Normal saja tidak cukup. 16 worker tidak lebih cepat dari 12.
- **GateGuard hook** meminta fakta (permintaan user, file terdampak, rollback) sebelum Bash/Edit/
  Write pertama dan sebelum perintah destruktif. Sebutkan faktanya lalu ulangi perintah yang sama.
- **PowerShell quoting** merusak `python -c` dan commit message berisi tanda kutip. Pakai file di
  scratchpad dan `git commit -F`.
- **soul + `\rev{}`.** `\cite`, `\ref`, `\eqref`, `\m` harus di-`\soulregister` tipe 7; `\emph`,
  `\textbf`, `\textit` tipe 1. Sudah di preamble; jangan dihapus.
- **Persamaan panjang** pakai `multline` atau `split`; tabel lebar pakai `\resizebox{\linewidth}{!}`
  (sudah di `paper_tables_v2.py`).
- **Regex blok GENERATED** harus mendukung blok kosong (sudah diperbaiki di `fill_results_v2.py`).
- **`desktop.ini` di `.git/`** merusak ref (`warning: ignoring broken ref refs/tags/desktop.ini`).
  Artefak Windows. Perbaikan: `find .git -iname desktop.ini -delete`.
- **Wall time.** Keluarga Q dua sampai tiga kali lebih lambat dari PPO. Jangan pakai satu rata-rata
  untuk estimasi durasi.
