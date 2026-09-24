# Prompt Pencarian Literatur — Menutup Klaim Tanpa Sumber

Tujuan: mencari paper **baru** untuk klaim-klaim di draft yang saat ini tidak punya sitasi, punya sitasi salah, atau bersumber lemah. Berbeda dari `prompt-notebooklm.md` yang hanya menggali sumber yang sudah ada di notebook.

**Tool yang cocok:** Google Scholar, Semantic Scholar, Elicit, Consensus, Connected Papers, atau Claude/GPT dengan web search. Untuk prompt bertanda 🔬 pakai deep research kalau tersedia.

**Aturan pakai:**
- Setiap kandidat paper harus kamu verifikasi sendiri (buka DOI-nya, baca abstract). Jangan percaya judul yang disodorkan tool tanpa dicek — LLM bisa mengarang referensi yang terdengar masuk akal.
- Prioritaskan: jurnal Q1/Q2, konferensi tier-1 (NeurIPS, ICML, ICLR, INFOCOM, ICC, NOMS), atau standar resmi (ITU-T, 3GPP, IEEE).
- Hindari: preprint tanpa peer review sebagai sumber tunggal, blog vendor, jurnal tanpa DOI, publisher yang tidak dikenal.

---

## Ringkasan gap

| ID | Klaim di draft | Kondisi sitasi sekarang | Prioritas |
|---|---|---|---|
| L1 | Hybrid action space (diskret + kontinu dalam satu policy) | **Tidak ada sitasi sama sekali** | Tinggi |
| L2 | Safety layer berbasis prediksi aksi | **Tidak ada sitasi sama sekali** | Tinggi |
| L3 | Dueling critic pada actor-critic | **Tidak ada sitasi** (hanya dueling-DQN via `[13]`,`[16]`) | Tinggi |
| L4 | WGAN-GP (Eq 2–4) | Disitasi ke `[44]` yang salah topik | Tinggi |
| L5 | Ambang SLA per kelas trafik | `[41]` blog vendor, `[43]` topik tidak nyambung | Tinggi |
| L6 | Metrik evaluasi data sintetis (PCD, Wasserstein Distance) | **Tidak ada sitasi** | Sedang |
| L7 | Protokol pelaporan RL (seeds, CI, uji signifikansi) | **Tidak ada sitasi** | Sedang |
| L8 | GAN untuk sintesis trafik jaringan | **Tidak ada sitasi** | Sedang |
| L9 | Static heuristic sebagai baseline | **Tidak ada sitasi** | Sedang |
| L10 | Gaussian noise σ=0.5 sebagai augmentasi RL | Disitasi ke `[44]` yang salah | Sedang |
| L11 | Konstanta 80 byte sebagai rata-rata ukuran paket (Eq 6) | **Tidak ada sitasi** | Rendah |
| L12 | Pengganti `[23]` (publisher meragukan) | Perlu substitusi | Rendah |
| L13 | Testbed fisik edge untuk RL orkestrasi jaringan | Perlu pembanding untuk Tabel I | Sedang |

---

## L1 — Hybrid / parameterized action space 🔬

**Klaim di draft (Abstract):** *"utilizes a hybrid action space for continuous bandwidth adjustment and discrete port selection"*

```
Aku butuh paper yang memformulasikan reinforcement learning dengan action
space hybrid, yaitu satu policy yang secara simultan menghasilkan komponen
diskret (memilih dari himpunan terbatas) dan komponen kontinu (nilai real),
bukan dua agen terpisah.

Yang aku cari:
1. Paper metode fundamental yang memperkenalkan formulasi ini, terutama
   yang berbasis policy gradient / actor-critic / PPO, bukan hanya DQN
2. Bagaimana log-probability gabungan dihitung untuk PPO ratio ketika ada
   dua jenis distribusi (kategorikal dan Gaussian) dalam satu policy
3. Bagaimana entropy bonus dihitung untuk policy hybrid
4. Penerapan action space hybrid spesifik di domain jaringan: network
   slicing, resource allocation, SDN, edge computing, atau NFV

Untuk setiap paper sebutkan: judul, penulis, venue, tahun, DOI, dan
persamaan kunci yang memformulasikan policy hybrid-nya.

Utamakan paper yang persamaannya bisa langsung kuadaptasi, bukan sekadar
menyebut "hybrid" di abstract.
```

**Query pencarian:**
- `parameterized action space reinforcement learning`
- `hybrid action space PPO`
- `discrete-continuous action space policy gradient`
- `hybrid action space network slicing resource allocation`

**Seed paper untuk diverifikasi** (aku ingat judul-judul ini tapi **cek sendiri** metadatanya):
- Masson, Ranchod, Konidaris — *Reinforcement Learning with Parameterized Actions*, AAAI 2016
- Xiong et al. — *Parametrized Deep Q-Networks Learning* (P-DQN), 2018
- Fan et al. — *Hybrid Actor-Critic Reinforcement Learning in Parameterized Action Space* (H-PPO), IJCAI 2019
- Neunert et al. — *Continuous-Discrete Reinforcement Learning for Hybrid Control in Robotics*, CoRL 2019

H-PPO paling relevan karena berbasis PPO, sama seperti SDH-PPO.

---

## L2 — Safety layer / constrained RL 🔬

**Klaim di draft (kontribusi #2):** *"Formulation of a mathematical security layer based on action predictions to proactively guide the agents' decision-making"*

```
Aku butuh paper tentang mekanisme yang membatasi atau memodifikasi aksi
agen RL sebelum dieksekusi ke lingkungan, berdasarkan prediksi konsekuensi
aksi tersebut terhadap constraint keselamatan.

Konteksku: agen PPO mengalokasikan bandwidth di jaringan SDN, dan aku ingin
mencegah aksi yang diprediksi akan melanggar SLA latency.

Yang aku cari:
1. Paper yang memakai istilah "safety layer" secara spesifik, terutama yang
   memprediksi pelanggaran constraint dari state-action lalu memproyeksikan
   aksi ke himpunan aman
2. Pendekatan alternatif dan perbandingannya: action masking, shielding,
   constrained policy optimization, Lagrangian methods, control barrier function
3. Bagaimana masing-masing menangani gradien — apakah gradien mengalir
   melalui safety layer saat backprop, atau layer itu diperlakukan
   sebagai bagian environment
4. Penerapan safe RL di domain jaringan atau telekomunikasi

Untuk setiap paper sebutkan judul, penulis, venue, tahun, DOI, dan
persamaan proyeksi/constraint-nya.
```

**Query pencarian:**
- `safety layer reinforcement learning continuous action`
- `safe reinforcement learning action projection constraint`
- `shielded reinforcement learning`
- `constrained reinforcement learning network slicing SLA`

**Seed paper untuk diverifikasi:**
- Dalal et al. — *Safe Exploration in Continuous Action Spaces*, 2018 — ini yang literal memakai istilah "safety layer", paling dekat dengan klaimmu
- Alshiekh et al. — *Safe Reinforcement Learning via Shielding*, AAAI 2018
- Achiam et al. — *Constrained Policy Optimization*, ICML 2017
- García & Fernández — *A Comprehensive Survey on Safe Reinforcement Learning*, JMLR 2015

> **Catatan penting:** kalau hasil audit Claude Code menunjukkan safety layer **tidak ada di kode**, jangan pakai prompt ini untuk mengarang justifikasi. Pakai untuk memutuskan apakah mau mengimplementasikannya, atau turunkan klaim.

---

## L3 — Dueling architecture di luar DQN

**Klaim di draft (III.F, IV.B):** *"duel layer"*, *"the Safety Layer and Dueling Critic architecture"*

```
Dueling network architecture aslinya diperkenalkan untuk DQN dengan memecah
Q-function menjadi state-value stream dan advantage stream. Aku butuh tahu
apakah konsep ini pernah diterapkan pada critic di metode actor-critic
seperti PPO, A2C, atau SAC.

Yang aku cari:
1. Paper asli dueling architecture untuk referensi dasar
2. Paper mana pun yang menerapkan value/advantage decomposition pada
   critic actor-critic, bukan pada Q-network
3. Kalau ada, bagaimana mereka menjelaskan interaksinya dengan Generalized
   Advantage Estimation, yang sudah menghitung advantage secara terpisah?
   Apakah tidak redundan?
4. Kalau ternyata tidak ada paper yang melakukannya, katakan begitu secara
   eksplisit — itu informasi yang sama pentingnya buatku

Sebutkan judul, penulis, venue, tahun, DOI.
```

**Query pencarian:**
- `dueling network architecture deep reinforcement learning`
- `dueling critic actor-critic`
- `value advantage decomposition PPO critic`

**Seed paper:** Wang et al. — *Dueling Network Architectures for Deep Reinforcement Learning*, ICML 2016.

> **Ekspektasi realistis:** ada kemungkinan besar hasilnya nihil untuk poin 2, karena dueling secara konseptual memang untuk Q-learning. Kalau nihil, itu justru sinyal bahwa istilah "Dueling Critic" di papermu perlu diganti atau dijelaskan ulang dari nol.

---

## L4 — WGAN dan WGAN-GP (menggantikan sitasi `[44]`)

**Klaim di draft (III.C, Eq 2–4):** stabilisasi Arjovsky + gradient penalty

Dua referensi ini **sudah pasti**, tinggal ditambahkan:

- Arjovsky, Chintala, Bottou — *Wasserstein Generative Adversarial Networks*, ICML 2017
  `https://dl.acm.org/doi/10.5555/3305381.3305404`
- Gulrajani, Ahmed, Arjovsky, Dumoulin, Courville — *Improved Training of Wasserstein GANs*, NeurIPS 2017
  `https://papers.nips.cc/paper_files/paper/2017/hash/892c3b1c6dccd52936e27cbd0ff683d6-Abstract.html`

Sitasi Arjovsky untuk klaim stabilisasi dan Wasserstein distance; sitasi Gulrajani untuk Eq 2–4 (gradient penalty dan interpolasi).

**Tambahan opsional** kalau mau memperkuat pembahasan Gaussian noise (lihat juga L10):
```
Cari paper yang membahas penambahan noise pada input diskriminator GAN
sebagai teknik stabilisasi pelatihan, beserta analisis teoretisnya tentang
overlap distribusi. Aku sudah punya Arjovsky ICML 2017 — apakah ada
paper lain yang membahas ini lebih spesifik, terutama yang memberi panduan
pemilihan nilai sigma?
```

---

## L5 — Ambang SLA per kelas trafik 🔬

**Klaim di draft (Tabel II):** ambang latency untuk DHT11, kamera, dan heart rate. Sumber saat ini `[41]` blog vendor Firecell dan `[43]` paper RAN slicing yang tidak berkaitan.

```
Aku butuh sumber yang bisa dipertanggungjawabkan untuk ambang latency SLA
tiga kelas trafik IoT di paper akademik:

1. Telemetri lingkungan (sensor suhu/kelembapan) — trafik best-effort,
   toleran latency
2. Video surveillance / citra kamera — trafik eMBB
3. Telemetri medis vital sign (heart rate, SpO2, ECG) — trafik URLLC / IoMT

Untuk setiap kelas, cari:
- Standar resmi yang menetapkan angkanya (ITU-T, 3GPP, IEEE, IETF).
  Sebutkan nomor dokumen dan tabel/bagian persisnya
- Kalau tidak ada standar, cari paper peer-reviewed yang menetapkan
  atau mensurvei angka tersebut
- Rentang nilai yang berbeda antar sumber, jangan dirata-ratakan

Khusus untuk kelas medis, bedakan antara:
- monitoring pasien rutin (tidak seketat yang orang kira)
- telesurgery / haptic feedback (ini yang butuh sub-milidetik)
Papermu memakai heart rate monitoring, jadi jangan pakai angka telesurgery
kalau memang berbeda.

Sebutkan kutipan aslinya untuk setiap angka.
```

**Query pencarian:**
- `ITU-T G.1010 end-user multimedia QoS categories`
- `3GPP TS 22.261 service requirements 5G latency`
- `IEEE 11073 personal health device communication`
- `URLLC latency requirements healthcare IoT survey`
- `medical IoT latency requirements patient monitoring`

> **Catatan:** `[42]` ITU-T G.1010 (2001) di draftmu sebenarnya sumber yang sah untuk kelas multimedia, hanya tahunnya tua. Cari padanan modernnya di 3GPP.

---

## L6 — Metrik evaluasi data sintetis

**Klaim di draft (IV.A, Tabel IV):** PCD dan Wasserstein Distance dipakai tanpa sitasi.

```
Aku memakai dua metrik untuk mengevaluasi kualitas data tabular sintetis
hasil GAN: Pairwise Correlation Difference (PCD) dan Wasserstein Distance.
Keduanya tidak kusitasi.

Cari:
1. Sumber asal metrik Pairwise Correlation Difference untuk evaluasi
   data sintetis — siapa yang memperkenalkan, bagaimana definisi formalnya
2. Konvensi pelaporan PCD: apakah dilaporkan sebagai persentase atau nilai
   absolut? Semakin tinggi semakin baik atau sebaliknya?
3. Paper survei tentang metrik evaluasi data sintetis tabular secara umum
4. Metrik lain yang lazim dilaporkan bersamaan, supaya evaluasiku tidak
   terlihat cherry-picked

Sebutkan definisi matematis persisnya untuk masing-masing.
```

> **Peringatan:** draftmu melaporkan `PCD = 71%` dan mendeskripsikannya sebagai indikator kemiripan yang tinggi. Perlu dicek — PCD adalah metrik **difference**, jadi normalnya nilai kecil berarti bagus. Kalau 71% itu benar-benar difference, itu buruk, bukan bagus. Verifikasi definisi yang dipakai di kode (lihat juga Prompt 7 di `prompt-claude-code.md`).

---

## L7 — Protokol pelaporan hasil RL

**Kebutuhan:** justifikasi metodologis untuk menambahkan multi-seed + CI (item C1), dan sekaligus melindungi diri dari pertanyaan reviewer.

```
Aku perlu referensi metodologis tentang cara melaporkan hasil eksperimen
deep reinforcement learning secara benar.

Cari paper yang membahas:
1. Berapa jumlah random seed yang memadai untuk klaim perbandingan antar
   algoritma RL, dan mengapa
2. Cara melaporkan ketidakpastian: confidence interval, bootstrap,
   interquartile mean, performance profile
3. Uji statistik mana yang tepat untuk membandingkan dua algoritma RL,
   dan kesalahan umum apa yang harus dihindari
4. Kritik terhadap praktik pelaporan hasil single-run di literatur RL

Aku ingin mengutip ini di bagian experimental setup sebagai justifikasi
protokol evaluasiku.
```

**Seed paper untuk diverifikasi:**
- Henderson et al. — *Deep Reinforcement Learning That Matters*, AAAI 2018
- Agarwal et al. — *Deep Reinforcement Learning at the Edge of the Statistical Precipice*, NeurIPS 2021
- Colas, Sigaud, Oudeyer — *How Many Random Seeds?*, 2018

Mengutip ini punya efek samping bagus: reviewer melihat kamu sadar standar metodologi, bukan sekadar menambal kritik.

---

## L8 — GAN untuk sintesis trafik jaringan

**Kebutuhan:** menempatkan EO-WGAN dalam konteks literatur, dan mengisi kolom "Generative Augmentation" di Tabel I.

```
Cari paper yang memakai generative model untuk mensintesis atau
mengaugmentasi data trafik jaringan.

Yang aku cari:
1. GAN untuk sintesis trafik jaringan atau data telemetri time-series
   jaringan — model apa yang dipakai, bagaimana dievaluasi
2. Khususnya yang datanya kemudian dipakai untuk melatih agen
   reinforcement learning, bukan hanya untuk anomaly detection
3. Perbandingan GAN vs VAE vs metode statistik untuk keperluan ini
4. Bagaimana mereka menangani sifat time-series dan korelasi antar fitur

Sebutkan judul, penulis, venue, tahun, DOI, dan metrik evaluasi
yang mereka pakai.
```

**Query pencarian:**
- `GAN synthetic network traffic generation`
- `generative adversarial network data augmentation reinforcement learning network`
- `synthetic time series network telemetry GAN`

**Seed paper untuk diverifikasi:**
- Lin et al. — *Using GANs for Sharing Networked Time Series Data* (DoppelGANger), IMC 2020
- Ring et al. — *Flow-based network traffic generation using Generative Adversarial Networks*, Computers & Security 2019

---

## L9 — Static heuristic baseline

**Kebutuhan:** baseline yang bisa disitasi, bukan sekadar "static" tanpa definisi (item C2).

```
Di paperku ada baseline non-AI bernama "static heuristic" untuk alokasi
bandwidth di network slicing, tapi tidak kudefinisikan dan tidak kusitasi.

Cari:
1. Baseline non-learning yang lazim dipakai sebagai pembanding di paper
   network slicing / resource allocation: fixed allocation, proportional
   fair, weighted round-robin, priority queueing, threshold-based
2. Paper yang mendefinisikan baseline tersebut secara formal sehingga
   bisa kusitasi
3. Konvensi di literatur: baseline mana yang dianggap standar minimum
   untuk domain ini?

Aku ingin baseline-ku bisa dibandingkan dengan paper lain, bukan
definisi buatan sendiri.
```

---

## L10 — Gaussian noise sebagai augmentasi untuk RL

**Klaim di draft (III.C, Eq 1):** *"the addition of Gaussian noise constitutes an effective data augmentation strategy for reinforcement learning agents... the value of 0.5 standard deviations is determined by a hyperparameter that is empirically tuned"*

```
Cari paper yang mendukung penambahan Gaussian noise pada observasi/state
sebagai teknik augmentasi data atau regularisasi untuk agen reinforcement
learning, dengan tujuan meningkatkan generalisasi dan robustness.

Yang aku butuhkan:
1. Bukti empiris bahwa teknik ini efektif untuk RL, bukan hanya untuk
   supervised learning
2. Panduan pemilihan besaran noise
3. Kaitannya dengan domain randomization dan robust RL

Kalau bukti untuk RL ternyata lemah atau berlawanan, katakan begitu.
```

**Query pencarian:**
- `observation noise data augmentation reinforcement learning generalization`
- `domain randomization sim-to-real reinforcement learning`
- `state perturbation robust reinforcement learning`

---

## L11 — Konstanta ukuran paket 80 byte

**Klaim di draft (III.C, Eq 6):** *"multiplying it by the constant 80, which is an estimate of the average packet size"*

```
Aku memakai konstanta 80 sebagai estimasi rata-rata ukuran paket untuk
mengonversi kelebihan bitrate menjadi jumlah paket yang di-drop.

Cari:
1. Studi pengukuran distribusi ukuran paket di jaringan IoT atau jaringan
   sensor, yang bisa kupakai untuk menjustifikasi angka ini
2. Apakah 80 byte itu masuk akal untuk trafik telemetri IoT berbasis JSON?
3. Satuannya perlu diklarifikasi — 80 byte atau 80 bit? Berdasarkan
   literatur, mana yang lazim untuk payload sensor?

Kalau angkanya tidak realistis untuk trafik yang kudeskripsikan
(JSON dari DHT11, kamera, dan heart rate monitor), katakan berapa
yang lebih tepat.
```

> Ini item kecil tapi tipe yang sering dicolek reviewer detail. Sekalian cek satuannya di kode.

---

## L12 — Pengganti referensi `[23]`

`[23]` (Rachakonda & Lakshmikanth, dari theaspd.com) tidak punya volume, halaman, atau DOI.

```
Cari paper peer-reviewed dengan DOI yang membahas optimasi QoS-aware dan
aspek keamanan pada arsitektur network slicing 6G. Aku butuh pengganti
untuk sebuah referensi yang publisher-nya tidak kredibel.

Utamakan: IEEE, ACM, Elsevier, Springer, atau MDPI, terbit 2022 atau
setelahnya, dan yang relevan dengan slicing berbasis DRL.
```

---

## L13 — Testbed fisik untuk RL orkestrasi jaringan 🔬

**Kebutuhan:** klaim kebaruan "physical testbed" di Tabel I butuh pembanding yang jujur.

```
Klaim kebaruan paperku sebagian bertumpu pada validasi di testbed fisik
(Raspberry Pi 5 + Open vSwitch + Ryu + Kubernetes), bukan simulasi.
Aku perlu memastikan klaim ini tidak berlebihan.

Cari paper yang mengevaluasi agen reinforcement learning untuk network
slicing, SDN, atau orkestrasi resource pada hardware fisik nyata,
bukan simulator seperti NS-3 atau Mininet.

Untuk masing-masing sebutkan:
- Hardware apa yang dipakai
- Skala testbed (jumlah node, switch, tenant)
- Apakah RL dilatih di hardware itu atau hanya di-deploy
- Apa yang mereka klaim sebagai kontribusi terkait testbed fisiknya

Aku ingin tahu seberapa umum praktik ini, supaya klaim kebaruanku
proporsional. Kalau ternyata sudah banyak yang melakukannya, katakan.
```

---

## Setelah selesai mencari

Untuk setiap referensi baru, catat di tabel ini lalu masukkan ke `revision-map.md`:

| ID gap | Paper (penulis, tahun) | Venue | DOI | Sudah diverifikasi? | Disitasi di bagian mana |
|---|---|---|---|---|---|
| L1 | | | | ☐ | |
| L2 | | | | ☐ | |
| L3 | | | | ☐ | |
| L4 | Arjovsky et al., 2017 | ICML | 10.5555/3305381.3305404 | ☐ | III.C |
| L4 | Gulrajani et al., 2017 | NeurIPS | — | ☐ | III.C, Eq 2–4 |
| L5 | | | | ☐ | Tabel II |
| L6 | | | | ☐ | IV.A |
| L7 | | | | ☐ | III.F / experimental setup |
| L8 | | | | ☐ | II, III.C |
| L9 | | | | ☐ | III.F |
| L10 | | | | ☐ | III.C, Eq 1 |
| L11 | | | | ☐ | III.C, Eq 6 |
| L12 | | | | ☐ | II.A |
| L13 | | | | ☐ | II, Tabel I |

**Verifikasi wajib sebelum menyitasi:** buka DOI-nya, pastikan judul dan penulis cocok, dan pastikan isi paper benar-benar mendukung klaimmu. Sitasi yang salah arah persis seperti `[21]`, `[43]`, dan `[44]` di draft sekarang adalah cara tercepat kehilangan kepercayaan reviewer.

**Urutan yang disarankan:** L4 dan L5 dulu (langsung menutup sitasi salah), lalu L1–L3 setelah hasil audit kode keluar — karena kalau ternyata safety layer atau dueling critic tidak ada di implementasi, kamu tidak perlu mencarikan sumbernya sama sekali.
