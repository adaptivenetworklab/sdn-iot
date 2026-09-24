# Revision Map — SDH-PPO Paper

**Draft:** `SDN-IoT.docx` (SDH-PPO Driven Resource Orchestration for IoT-Aware Multi-Tenant Network Slicing in Microservices-Based SDN)
**Sumber revisi:** `Cek_Draft_Paper_-_Draft_SDH-PPOv2_5__21082026_.docx` (24 poin) + 7 temuan tambahan hasil audit draft
**Repo:** `github.com/adaptivenetworklab/sdn-iot`

**Legenda kolom Sumber Jawaban:**
`CC` = Claude Code di repo · `NLM` = NotebookLM (sumber referensi) · `MAN` = manual/keputusan penulis · `EXP` = butuh eksperimen ulang

---

## Ringkasan status

| Kluster | Jumlah item | Effort | Blocking? |
|---|---|---|---|
| A. Metodologi | 5 | Berat | Ya — tanpa ini paper tidak bisa dievaluasi |
| B. Kontradiksi angka | 3 | Rendah | Ya — alasan penolakan instan |
| C. Rigor eksperimen | 7 | Sedang–berat | Ya |
| D. Referensi | 5 | Rendah | Tidak, tapi merusak kredibilitas |
| E. Presentasi | 2 | Rendah–sedang | Tidak |
| X. Temuan tambahan | 7 | Rendah | Sebagian ya (X2, X3) |
| **Total** | **29** | | |

---

## Kluster A — Metodologi (Section III)

Semua klaim kontribusi di Section I tidak punya pasangan deskripsi di Section III. Ini akar masalahnya.

| ID | Isu | Diklaim di | Harus ditulis di | Kondisi sekarang | Sumber jawaban | Status |
|---|---|---|---|---|---|---|
| A1 | **Hybrid action space** — "continuous bandwidth adjustment and discrete port selection" | Abstract, Intro | III.E | III.E hanya mendeskripsikan Actor yang memetakan state ke *continuous* action space. Tidak ada parameterized action space (mis. PADQN), tidak ada arsitektur | CC | ☑ |
| A2 | **Safety layer / mathematical security layer based on action predictions** | Kontribusi #2 (Intro), III.F ("safety layer"), IV.B | III.E atau subsection baru | Nol persamaan. Eq 1–15 semuanya komponen standar (PPO, GAE, WGAN-GP, z-score) | CC | ☑ |
| A3 | **Dueling Critic** | III.F ("duel layer"), IV.B ("Dueling Critic architecture") | III.E | Tidak pernah didefinisikan. Dueling itu konsep DQN; kalau dipakai di actor-critic PPO harus dijelaskan bagaimana critic dipecah jadi state-value dan advantage stream. *Catatan: reviewer menulis "hanya muncul di Kesimpulan", padahal sebenarnya di III.F dan akhir IV.B* | CC | ☑ |
| A4 | **EO-WGAN** — "Enhanced Optimization" tidak pernah didefinisikan | Abstract, Intro, IV.A | III.C | Eq 2–4 persis WGAN-GP standar (Gulrajani et al. 2017) yang tidak dikutip. **Bukti tambahan: Kesimpulan sendiri menulis "WGAN-GP-based data growth models", bukan EO-WGAN** → penamaan tidak konsisten di dalam paper | CC + MAN | ☑ |
| A5 | **37 state features** tidak dienumerasi | III.F (satu kalimat) | III.A / MDP formulation | State space tidak didefinisikan formal | CC | ☑ |

**Keputusan yang harus diambil dulu:** apakah A1/A2/A3 benar-benar ada di kode? Kalau ada → tulis deskripsinya. Kalau tidak → turunkan klaim di Abstract, Intro, dan Kesimpulan supaya konsisten. Jangan tulis metode yang tidak dijalankan.

---

## Kluster B — Kontradiksi angka (kerjakan pertama, murah)

| ID | Isu | Lokasi persis | Perbaikan | Sumber | Status |
|---|---|---|---|---|---|
| B1 | **Ambang SLA tidak seragam** | Tabel II (III.A): P1 `<10ms`, P2 `<150ms`, P4 `<10ms` · Fig. 4 caption + IV.A + IV.B: P1 `6ms`, P2 `7ms`, P4 `7ms` · IV.B paragraf hasil P4: `"10 ms threshold"` | Tentukan satu sumber kebenaran, seragamkan di 4 tempat. Gap terbesar: P2 150ms vs 7ms | CC + NLM | ☐ |
| B2 | **Arah klaim terbalik** | IV.B: *"recorded an overall error rate of 10.3%, which is 9.2 percentage points **higher** than the standard PPO and significantly **higher** than the DQN (48.9%), the DDQN (51.6%), and the static model (44.8%)"* | Ganti `higher` → `lower` di 3 tempat. **Angkanya sendiri sudah benar:** 19.5−10.3 = 9.2 pp; (19.5−10.3)/19.5 = 47.2%; (44.8−10.3)/44.8 = 77.0%; (48.9−10.3)/48.9 = 78.9%; (51.6−10.3)/51.6 = 80.0% | MAN | ☐ |
| B3 | **Port 3 hilang + sistem prioritas tidak didefinisikan** | III.A mendefinisikan Slice 3 (Smart Building), tapi hasil hanya memuat port 1, 2, 4 | Jelaskan ke mana port 3, atau tambahkan hasilnya. Sekalian definisikan pemetaan port → slice → priority level secara eksplisit | CC | ☑ |

---

## Kluster C — Rigor eksperimen

Sebagian besar jawabannya ada di repo, bukan hal yang perlu dieksperimen ulang. Kecuali C1.

| ID | Isu | Lokasi | Yang dibutuhkan | Sumber | Status |
|---|---|---|---|---|---|
| C1 | Tidak ada jumlah seed, confidence interval, uji signifikansi | Tabel V + seluruh IV.B | Semua angka terlihat hasil satu run. Klaim *"consistently outperforms"* tidak didukung. Minimal 5–10 seed + mean ± 95% CI, plus uji (Welch's t-test / Mann-Whitney) | CC lalu EXP | ☐ |
| C2 | Static heuristic baseline tidak didefinisikan | III.F, satu kalimat (`γ=0.99 over 2,000 steps` — γ untuk heuristik non-AI juga janggal) | Bagaimana ia mengalokasikan resource? Fixed policing rate? Round-robin? Tanpa ini "76.9% improvement" tidak bermakna | CC | ☑ |
| C3 | Detail implementasi DQN/DDQN hilang | III.F | ε-greedy schedule, target network update freq, replay buffer size, arsitektur. Kalau value-based dipaksa pakai protokol training PPO (2000 "epochs", batch 64), perbandingannya tidak adil | CC | ☑ |
| C4 | Tabel III nyaris kosong | III.F | Tambah: PPO clip ratio ε, GAE λ, entropy coefficient, value loss coef, jumlah layer + aktivasi + lebar, dan **seluruh hyperparameter GAN** (λ gradient penalty, n_critic, lr generator/critic, latent dim, batch, epoch GAN) | CC | ☑ |
| C5 | "2000 epochs" ambigu | III.F + Tabel III | Updates atau episodes? Artinya beda untuk DQN vs PPO. Sebutkan total environment steps supaya sebanding | CC | ☑ |
| C6 | Di mana training berjalan? | Tidak ada | Model Pi 5 + RAM, lokasi training (offline di PC?), runtime per epoch, dan apa persisnya yang jalan di Pi 5 saat deployment (inference only?). Klaim "physical testbed" justru butuh detail ini | CC + MAN | ☑ |
| C7 | Tidak ada ablation study + diskusi P2 (29.5%) dan trade-off konvergensi | Tidak ada | Ablation: −safety layer, −dueling critic, −EO-WGAN, −hybrid action. Plus diskusi kenapa P2 masih 29.5% dan kenapa konvergensi 2× lebih lambat itu dapat diterima | EXP + MAN | ☐ |

---

## Kluster D — Referensi

| ID | Isu | Detail terverifikasi | Aksi | Status |
|---|---|---|---|---|
| D1 | 4 pasang duplikat | `[1]`=`[26]` Wijethilaka & Liyanage (COMST) · `[13]`=`[29]` Xu & Yu (Computer Networks) · `[16]`=`[32]` Sittakul et al. (JNCA) · `[37]`=`[38]` Zhang et al. (ICC Workshops) | Hapus duplikat, renumber. 44 → 40 entri unik | ☑ |
| D2 | Sitasi Holscher salah | II.A: *"Holscher integrated microservice orchestration logic... via switches[21]"*. `[21]` = Fernandez et al. Holscher = `[31]` | Ganti ke `[31]` | ☑ |
| D3 | Sitasi blockchain salah | II.A: *"...AI and secured by blockchain[21]"*. Harusnya Zhang et al. = `[37]`/`[38]`. Kalimat berikutnya di paragraf sama sudah benar pakai `[38]` → jelas typo | Ganti ke `[37]` | ☑ |
| D4 | Sitasi WGAN salah | III.C: klaim stabilisasi Arjovsky disitasi ke `[44]` = C. Tan, *"Comparative Study of RL Performance Based on PPO and DQN"* — tidak ada kaitan dengan WGAN | Tambah 2 referensi baru: Arjovsky et al., *Wasserstein GAN*, ICML 2017 (`dl.acm.org/doi/10.5555/3305381.3305404`) dan Gulrajani et al., *Improved Training of Wasserstein GANs*, NeurIPS 2017 (`papers.nips.cc/paper_files/paper/2017/hash/892c3b1c6dccd52936e27cbd0ff683d6-Abstract.html`). Kutip Gulrajani di Eq 2–4 | ☑ |
| D5 | `[39]` tidak lengkap | T. Mai, H. Yao, N. Zhang, W. He, D. Guo, M. Guizani, *"Transfer Reinforcement Learning aided Distributed Network Slicing Optimization in Industrial IoT"* — tanpa venue, tahun, DOI | Lengkapi metadata (kemungkinan IEEE TII) | ☑ |

---

## Kluster E — Presentasi

| ID | Isu | Detail | Sumber | Status |
|---|---|---|---|---|
| E1 | Tabel research gap di Related Work | Tabel I sudah ada tapi hanya centang/strip. Reviewer minta tabel yang menyampaikan **kelebihan dan keterbatasan** tiap studi, ditutup dengan baris yang memunculkan keunggulan metode yang diajukan | NLM | ☑ |
| E2 | Resolusi gambar | Audit file media di `.docx`: `image1` 495×929 @96dpi (Fig.1) · `image2` 732×341 @96dpi (Fig.2) · `image3` 572×478 @96dpi (**Fig.3, yang dikeluhkan**) · `image4` 1191×1059 @220dpi (Fig.4) · `image5–8` ~950×300 @96dpi (Fig.5–8). **Bukan cuma Fig.3 — semua kecuali Fig.4 di 96 dpi, dan Fig.4 pun masih di bawah 300 dpi standar IEEE.** Regenerate semua plot sebagai vektor (PDF/EPS/SVG) atau raster ≥300 dpi | CC | ☐ |

---

## Kluster X — Temuan tambahan (di luar catatan reviewer)

| ID | Isu | Lokasi | Sumber | Status |
|---|---|---|---|---|
| X1 | **Cross-reference tabel salah** | III.F: *"As summarized in Table 2"* → maksudnya Tabel III. Awal Section IV: *"summarized in Table 3"* → maksudnya Tabel V. Penomoran Arab dan Romawi tercampur | MAN | ☑ |
| X2 | **Penomoran prioritas bertentangan dengan penomoran slice** | III.A: Slice 1 (Healthcare) = prioritas tertinggi. Tapi hasil menyebut healthcare sebagai **"Priority 4 (P4)"** dan P1 = DHT11 (smart building = best-effort). Pembaca akan bingung mana yang prioritas tinggi | CC + MAN | ☑ |
| X3 | **Reward function tidak cocok dengan klaim hasil** | Eq 10 hanya menghukum latency P4 (`Plat_p4`); Eq 8 hanya menghitung throughput port 2 (`RX_p2/T_p2`). Tapi IV.B mengklaim perbaikan signifikan di P1 dan P2. Perlu dijelaskan kenapa agen memperbaiki port yang tidak masuk reward, atau reward function di paper belum lengkap | CC | ☑ |
| X4 | **Struktur III.C / III.D salah tempat** | III.C "Augmentation" memuat Eq 5–6 (bandwidth utilization, packet drop) = logika *environment*. III.D "Pre-Processing" memuat Eq 7–11 (reward function, action formulation) = *MDP formulation*. Usulan restrukturisasi: `III.A Environment` → `III.B MDP Formulation (state/action/reward)` → `III.C Augmentation (EO-WGAN)` → `III.D Proposed Framework (hybrid actor, safety layer, dueling critic)` → `III.E Baselines & Experimental Setup` | MAN | ☐ |
| X5 | **Kalimat duplikat** | III.C: *"...even when the overlap between the distributions of real and synthetic data is minimal[44]. When the overlap between the distributions of real and synthetic data is small[44]."* Fragmen kedua sisa editing | MAN | ☐ |
| X6 | **Kualitas sumber ambang SLA lemah** | `[41]` Z. Gdali, *"Edge Computing vs Cloud: Latency Impact"*, Firecell = blog vendor. `[43]` Mu et al. *CoMEx* = paper RAN slicing, tidak berkaitan dengan SLA heart rate. `[23]` tanpa volume/halaman dari theaspd.com. Ambang SLA medis sebaiknya dari standar (IEEE 11073, 3GPP URLLC) atau literatur IoMT yang peer-reviewed | NLM | ☐ |
| X7 | **Typo huruf awal hilang (artefak drop cap) + format tabel** | *"hE Ongoing progress"* (Intro) · *"he proposed framework consists"* (III.E) · *"he resulting visualization"* (IV.A) · *"able V shows"* (IV.B). Tabel V baris `Static` punya sel kosong berlebih | MAN | ☐ |

---

## Urutan pengerjaan

### Tahap 1 — Kredibilitas cepat (1–2 hari, tanpa dependensi)
`B2` · `D1` · `D2` · `D3` · `D4` · `D5` · `X1` · `X5` · `X7`
Semuanya editorial. Tidak butuh repo, tidak butuh eksperimen. Selesaikan dulu supaya draft berikutnya tidak ditolak karena hal remeh.

### Tahap 2 — Ekstraksi ground truth dari repo (jalankan Claude Code)
`A1` · `A2` · `A3` · `A4` · `A5` · `B1` · `B3` · `C2` · `C3` · `C4` · `C5` · `C6` · `X2` · `X3` · `E2`
Output tahap ini menentukan bentuk tahap 3.

### Tahap 3 — Penulisan ulang Section III
`A1`–`A5` + `X4`. Paling berat. Bentuknya tergantung hasil tahap 2:
- Kalau hybrid/safety/dueling **ada di kode** → tulis deskripsi + persamaan formalnya
- Kalau **tidak ada** → turunkan klaim di Abstract, Intro, Kesimpulan, dan Tabel I (kolom "Hybrid/Action Space" untuk baris PROPOSE)

### Tahap 4 — Rigor + presentasi
`C1` (seeds/CI, kemungkinan butuh re-run) · `C7` (ablation) · `E1` (tabel research gap) · `X6` (sumber SLA)

---

## Tracking

Ubah `☐` jadi `☑` saat selesai. Catat keputusan penting (terutama hasil tahap 2 untuk A1–A4) di bawah ini supaya tidak hilang:

### Log keputusan

| Tanggal | Item | Keputusan | Alasan |
|---|---|---|---|
| 2026-09-23 | Semua item | **Catatan penting**: revision-map ini ditulis terhadap draft yang berbeda dari `revisi/paper/main.tex` (hasil convert `Draft_SDH-PPO (2).docx`). File `SDN-IoT.docx`/`Cek_Draft_Paper_-_Draft_SDH-PPOv2_5__21082026_.docx` yang disebut di header gak ada di repo. Akibatnya beberapa item (B2, X5, X7) kutipan teksnya gak ketemu persis di `main.tex` — kemungkinan draft yang direview reviewer lebih baru/lengkap (ada Section III.F, Table V, 44 referensi) dibanding yang ada sekarang (Section III.A-E, Table I-IV, 39 referensi). Item yang diprioritaskan: yang substansinya tetap relevan (gap metodologi A1-A5, kontradiksi kode C2-C6, referensi D1-D5, dll) dikerjakan berdasar ground truth kode `Reinforcement Learning/final/`, bukan quote reviewer yang gak match. |
| 2026-09-23 | Pipeline ground truth | Pakai `Reinforcement Learning/final/allModel1.ipynb` + `Preprocessing.ipynb` + `DataAugmentation.ipynb` (SLA P1=12ms/P2=10ms/P4=3.5ms) — bukan `revision/allModel2-4.ipynb` (SLA 6/70/7ms) — karena ini yang match Table IV `main.tex` yang udah ke-compile, gak perlu regenerate tabel/angka | Keputusan user, supaya gak perlu re-run eksperimen buat sinkronin angka |
| 2026-09-23 | A1 | Klaim "hybrid action space" (continuous+discrete port) **diturunkan** jadi "continuous action space" murni. `PPOActor` di kode cuma punya 1 output scalar (`mu`, tanh); `action_dim_discrete=3` cuma dipakai baseline DQN/DDQN, gak pernah nyambung ke actor SDH-PPO | Kode = ground truth, gak nulis metode yang gak dijalanin (instruksi revision-map sendiri) |
| 2026-09-23 | A2 | Klaim "mathematical Safety Layer based on action projection" **direframe** jadi "rule-based safety-margin action correction" — proportional-error correction (K=2.0) + hard clip, cuma jalan pas evaluasi, ditulis persamaannya (Eq.16 baru) | `get_action_with_mask()` di kode bukan projection formal, dan gak dipanggil pas training |
| 2026-09-23 | A3 | Klaim Dueling Critic **dipertahankan** (valid, ada di kode `DuelingCritic`), tapi ditambah catatan `a.mean()` itu rata-rata batch bukan per-sample (beda dari Dueling DQN standar) | Transparansi soal detail implementasi, biar reviewer gak ketipu nyangka ini Dueling DQN klasik |
| 2026-09-23 | A4 | "EO-WGAN" diganti "WGAN-GP" di semua tempat (Abstract, Intro) biar konsisten sama Kesimpulan dan kode. Ditambah sitasi Arjovsky (WGAN) + Gulrajani (WGAN-GP) sebagai `b38`/`b39` | Kode cuma implement WGAN-GP standar, gak ada mekanisme "Enhanced Optimization" tambahan |
| 2026-09-23 | A5 | "37 state features" diganti "12" (4 fitur × 3 port P1/P2/P4), dienumerasi eksplisit di III.A subsection baru "State Space Formulation" | `Preprocessing.ipynb` + runtime print `INPUT_DIM=12` konfirmasi 12, bukan 37 |
| 2026-09-23 | X3 | Eq.10 (total reward) ditulis ulang: dari cuma penalti P4 jadi penalti P1+P2+P4 (P4 bobot 2x) + throughput P2 + drop penalty, sesuai kode `calculate_sdh_reward()` | Ini juga jawab kenapa hasil P1/P2 ikut membaik walau awalnya kelihatan cuma P4 yang dihukum |
| 2026-09-23 | C6 / Pi 5 | Klaim "Validation on a physical Raspberry Pi 5-based edge computing infrastructure" **direframe**: testbed fisik (Pi+sensor+OvS+Ryu+Flowvisor) dipakai buat **kumpulin data traffic asli**, RL dilatih **offline** dari dataset itu (real + augmentasi WGAN-GP) — bukan training/inference jalan di atas Pi 5 | Gak ada file model RL (.pth) yang di-deploy ke Pi manapun di repo; `torch.cuda.is_available()` di notebook nunjukin training di PC/laptop. Sesuai keputusan user: "testbed pake data asli, cuman diaugmentasi abis itu pake data synthesize" |
| 2026-09-23 | Belum dikerjakan | **X4** (restrukturisasi urutan subsection III), **C1** (seed/CI), **C7** (ablation), **X6** (ganti sumber SLA lemah) — belum dikerjakan. C1/C7/X6 butuh eksperimen/riset literatur terpisah. X4 di-skip demi fokus ke akurasi konten | Prioritas: benerin klaim yang salah > tambah polish presentasi |
| 2026-09-23 | **Angka Table III/IV fabricated** | Ditemukan `Reinforcement Learning/final/allModel1.ipynb` (dipakai sesi sebelumnya buat Table III/IV) ternyata training loop-nya `np.random.uniform()` hardcoded, bukan hasil eval model asli. Angka asli ditemukan sudah ada di `Reinforcement Learning/revision/sla_violation_report.csv` (dari `allModel4.ipynb`, real forward pass + real gradient training). **Table IV, SLA threshold (12/10/3.5→6/70/7ms), Fig.4-8, dan paragraf IV.A/IV.B di `main.tex` sudah di-swap ke angka asli** (Proposed Total Viol 10.3%, bukan 27.3% fabricated) | Integritas data — gak boleh publish angka yang di-hardcode menangin hipotesis sendiri |
| 2026-09-23 | Fig.5-8 "Reward Progress" panel | Ditemukan kolom Reward di `training_convergence_*.csv` identik persis di ke-4 model (bukan reward per-model, cuma reward batch offline yang sama karena ke-4 model di-update dari 1 batch yang sama tiap iterasi). Panel Reward **dihapus** dari Fig.5-8, tinggal panel Loss (real, beda per model) | Keputusan user: gak nampilin data yang menyesatkan meski keliatan "lebih meyakinkan" |
| 2026-09-23 | E1 selesai | `references-new.bib` (11 entry terverifikasi web, TODO-VERIFY cuma untuk field yang emang gak ketemu), `related-work-table.md` (11 baris + PROPOSE, markdown+LaTeX), paragraf novelty (T3) + motivasi testbed (T4), `10-source-conflicts.md` (T5) — semua di `revisi/TRACK/E1/`. Belum di-merge ke `main.tex` (nunggu review user) | Sesuai instruksi user: verifikasi web dilakukan SETELAH tabel jadi, cuma buat key yang kepake + 5 item konflik yang di-flag |
| 2026-09-23 | Ditunda | Nama akronim SDH-PPO (huruf H) dan nasib final klaim A3 (Dueling Critic) — masih ditunda sesuai keputusan user sebelumnya | Kosmetik, ganti 2x lebih mahal dari nunggu |
