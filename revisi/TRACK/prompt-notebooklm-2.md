# Prompt NotebookLM #2 — Gap L8–L13

Notebook kedua, berisi sumber untuk enam gap terakhir. Penomoran dilanjutkan dari `prompt-notebooklm.md` (yang berhenti di N7) supaya tidak tabrakan saat kamu mencatat hasilnya.

| Prompt | Gap | Untuk item revisi |
|---|---|---|
| N8 | L8 — GAN untuk sintesis trafik jaringan | Tabel I, II, III.C |
| N9 | L9 — Static heuristic baseline | C2 |
| N10 | L10 — Gaussian noise sebagai augmentasi RL | A4, III.C Eq 1 |
| N11 | L11 — Konstanta ukuran paket 80 | III.C Eq 6 |
| N12 | L12 — Pengganti referensi `[23]` | D-tambahan |
| N13 | L13 — Testbed fisik untuk RL jaringan | Tabel I, klaim kebaruan |

---

## Cara pakai (berbeda dari pencarian web)

NotebookLM hanya menjawab dari sumber yang ada di notebook. Konsekuensinya:

- **Jangan minta dia mencari paper baru atau menyebut DOI.** Dia akan mengarang. Minta dia menyebut *judul sumber* yang ada di notebook.
- **Selalu minta kutipan aslinya.** Ini pagar utama terhadap halusinasi.
- **Selalu beri izin menjawab "tidak ada".** Tanpa ini, NotebookLM cenderung memaksakan jawaban dari sumber yang paling mirip. Setiap prompt di bawah sudah memuat kalimat ini — jangan dihapus.
- **Satu prompt per kirim.** Kalau ditumpuk, jawaban untuk pertanyaan belakangan jadi dangkal.
- **Kalau hasilnya nihil, itu tetap informasi berharga.** Artinya sumbernya belum kamu punya, dan gap itu perlu pencarian web (pakai `prompt-literature-search.md`).

---

## N8 — GAN untuk sintesis trafik jaringan

```
Aku memakai WGAN-GP untuk mengaugmentasi data telemetri trafik jaringan
sebelum melatih agen reinforcement learning. Aku perlu menempatkan pendekatan
ini dalam konteks literatur yang ada di notebook ini.

Dari sumber-sumber di notebook ini, buat tabel dengan kolom:

| Sumber (judul, penulis, tahun) | Model generatif yang dipakai | Jenis data yang disintesis | Tujuan sintesis | Metrik evaluasi kualitas data sintetis | Apakah data sintetis dipakai untuk melatih agen RL? |

Setelah tabel, jawab:
1. Berapa banyak sumber yang memakai data sintetis untuk melatih agen RL,
   bukan hanya untuk anomaly detection atau intrusion detection?
2. Metrik evaluasi apa yang paling sering muncul lintas sumber?
3. Bagaimana mereka menangani sifat time-series dan korelasi antar fitur
   pada data jaringan?
4. Adakah sumber yang membandingkan WGAN-GP dengan varian GAN lain
   untuk data jaringan? Apa kesimpulannya?

Sertakan kutipan langsung untuk setiap klaim. Kalau suatu kolom tidak
disebutkan di sumber, tulis "tidak disebutkan". Kalau tidak ada sumber
yang relevan untuk suatu pertanyaan, katakan begitu secara eksplisit.
```

---

## N9 — Static heuristic baseline

```
Di paperku ada baseline pembanding bernama "static heuristic" untuk alokasi
bandwidth di network slicing, tapi aku belum mendefinisikannya secara formal
maupun menyitasinya.

Dari sumber-sumber di notebook ini:

1. Baseline non-learning apa saja yang dipakai sebagai pembanding di
   paper-paper ini? Sebutkan namanya, sumbernya, dan definisi formalnya
   (persamaan atau pseudocode kalau ada). Contoh yang kucari: fixed
   allocation, proportional fair, weighted round-robin, priority queueing,
   threshold-based allocation.
2. Untuk masing-masing, tulis persis bagaimana sumber tersebut
   mendeskripsikan cara kerjanya.
3. Baseline mana yang paling sering muncul lintas sumber? Itu yang
   kemungkinan dianggap standar minimum di bidang ini.
4. Apakah ada sumber yang menjelaskan mengapa baseline tertentu dipilih,
   atau membahas kelemahan memakai baseline yang terlalu lemah?

Kalau tidak ada sumber di notebook ini yang mendefinisikan baseline
non-learning secara formal, katakan begitu.
```

---

## N10 — Gaussian noise sebagai augmentasi

```
Di paperku ada klaim ini, dan sitasinya saat ini salah sasaran:

"Penambahan Gaussian noise merupakan strategi augmentasi data yang efektif
untuk agen reinforcement learning, karena dapat meningkatkan generalisasi
dan mencegah overfitting terhadap pola trafik tertentu. Nilai 0.5 standar
deviasi ditentukan sebagai hyperparameter yang di-tuning secara empiris."

Dari sumber-sumber di notebook ini:

1. Sumber mana yang mendukung bahwa penambahan noise pada observasi atau
   data pelatihan meningkatkan generalisasi agen RL? Kutip kalimat aslinya.
2. Apakah bukti yang ada berlaku untuk reinforcement learning, atau hanya
   untuk supervised learning? Bedakan dengan jelas — ini penting buatku.
3. Adakah sumber yang memberi panduan pemilihan besaran noise, atau yang
   melaporkan nilai sigma yang mereka pakai?
4. Adakah sumber yang membahas penambahan noise pada input diskriminator
   GAN sebagai teknik stabilisasi, dan kaitannya dengan overlap distribusi
   data riil dan sintetis?
5. Adakah sumber yang justru menunjukkan hasil sebaliknya, bahwa noise
   memperburuk performa RL? Kalau ada, sebutkan — aku ingin tahu sisi ini juga.

Jangan mencoba membenarkan klaimku. Kalau dukungannya lemah atau tidak ada,
katakan begitu.
```

---

## N11 — Konstanta ukuran paket

```
Di persamaan packet drop di paperku, aku mengalikan kelebihan bitrate dengan
konstanta 80 sebagai estimasi rata-rata ukuran paket, tanpa sitasi.

Dari sumber-sumber di notebook ini:

1. Adakah sumber yang melaporkan hasil pengukuran distribusi atau rata-rata
   ukuran paket di jaringan IoT, jaringan sensor, atau trafik telemetri?
   Sebutkan angkanya dan satuannya (byte atau bit), beserta kutipan aslinya.
2. Adakah sumber yang menyebut ukuran payload untuk jenis trafik ini:
   telemetri sensor berbasis JSON, video streaming, atau data vital sign medis?
3. Apakah ada sumber yang memodelkan packet drop dari selisih bitrate dan
   kapasitas? Bagaimana persis formulanya?

Kalau tidak ada sumber yang membahas ukuran paket sama sekali, katakan begitu.
```

---

## N12 — Pengganti referensi `[23]`

> **Catatan:** referensi `[23]` (Rachakonda & Lakshmikanth, theaspd.com) perlu diganti karena publisher-nya tidak kredibel. NotebookLM tidak bisa mencarikan paper baru dari luar, jadi prompt ini diarahkan untuk mencari pengganti **dari sumber yang sudah ada di notebook**. Kalau nihil, baru cari di web.

```
Aku punya satu referensi yang harus kubuang karena publisher-nya tidak
kredibel. Referensi itu kupakai untuk mendukung klaim tentang optimasi
QoS-aware dan aspek keamanan pada arsitektur network slicing 6G.

Dari sumber-sumber di notebook ini:

1. Sumber mana yang membahas optimasi QoS-aware pada network slicing?
   Sebutkan judul dan kutip kalimat yang paling relevan.
2. Sumber mana yang membahas aspek keamanan pada arsitektur slicing 5G/6G?
3. Adakah sumber yang membahas keduanya sekaligus, sehingga bisa
   menggantikan satu referensi dengan satu referensi?
4. Untuk setiap kandidat, sebutkan venue publikasinya kalau tercantum
   di sumber.

Kalau tidak ada kandidat yang cocok di notebook ini, katakan begitu —
berarti aku perlu mencari di luar.
```

---

## N13 — Testbed fisik untuk RL orkestrasi jaringan

```
Klaim kebaruan paperku sebagian bertumpu pada validasi di testbed fisik
(Raspberry Pi 5, Open vSwitch, Ryu controller, Kubernetes), bukan simulasi.
Aku perlu memastikan klaim ini proporsional, tidak berlebihan.

Dari sumber-sumber di notebook ini, buat tabel:

| Sumber (judul, penulis, tahun) | Lingkungan evaluasi (simulator / emulator / hardware fisik) | Nama simulator atau hardware spesifiknya | Skala (jumlah node, switch, tenant, slice) | Agen RL dilatih di mana vs di-deploy di mana | Klaim mereka terkait lingkungan evaluasi |

Setelah tabel, jawab:
1. Berapa banyak sumber yang benar-benar memakai hardware fisik, bukan
   NS-3, Mininet, OMNeT++, atau simulator lain?
2. Di antara yang memakai hardware fisik, adakah yang memakai
   single-board computer seperti Raspberry Pi?
3. Adakah sumber yang secara eksplisit mengklaim validasi di testbed fisik
   sebagai kontribusi? Bagaimana persis mereka merumuskan klaimnya?
   Aku ingin meniru tingkat kehati-hatiannya.
4. Adakah sumber yang membahas keterbatasan evaluasi berbasis simulasi,
   yang bisa kupakai untuk memotivasi pilihan testbed fisik?

Sertakan kutipan langsung. Kalau kolom tidak disebutkan, tulis
"tidak disebutkan". Jawab jujur meskipun hasilnya menunjukkan bahwa
testbed fisik sudah umum dipakai.
```

---

## Setelah selesai

Catat hasilnya di tabel `revision-map.md`. Untuk setiap gap, tandai salah satu:

- **TERTUTUP** — ada sumber di notebook yang mendukung, tinggal disitasi
- **SEBAGIAN** — ada sumber tapi hanya mendukung sebagian klaim, klaimnya perlu dipersempit
- **NIHIL** — tidak ada sumber, lanjut ke pencarian web dengan `prompt-literature-search.md`

Tiga prompt yang paling mungkin menghasilkan NIHIL adalah N11, N12, dan N10 poin 1–2. Itu wajar, jangan dipaksakan.

Satu hal yang perlu kamu jaga: kalau NotebookLM menjawab N10 dengan mengatakan bukti Gaussian noise hanya berlaku untuk supervised learning dan bukan RL, terima jawaban itu. Klaim di draftmu memang perlu dipersempit, bukan dicarikan pembenaran.
