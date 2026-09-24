# Prompt untuk NotebookLM — Verifikasi Referensi & Penguatan Sumber

Tujuan: memperbaiki kluster D (referensi), E1 (tabel research gap), dan X6 (sumber ambang SLA).

**Sebelum mulai:** pastikan notebook berisi PDF/sumber dari 44 referensi paper (atau sebanyak yang kamu punya). Tambahkan juga dua paper WGAN yang hilang:
- Arjovsky, Chintala, Bottou. *Wasserstein Generative Adversarial Networks*. ICML 2017.
- Gulrajani et al. *Improved Training of Wasserstein GANs*. NeurIPS 2017.

**Catatan cara pakai:** NotebookLM hanya menjawab dari sumber di notebook. Kalau ia bilang tidak menemukan sesuatu, itu informasi yang berguna — artinya sumbernya belum ada atau klaimnya memang tidak didukung. Jangan paksa ia menyimpulkan.

---

## Prompt N1 — Verifikasi sitasi yang dicurigai salah (item D2, D3, D4)

```
Aku sedang mengecek ketepatan sitasi di draft paperku. Untuk setiap klaim
di bawah, cari di sumber-sumber notebook ini dan jawab: sumber MANA yang
sebenarnya mendukung klaim ini? Sebutkan judul dan penulisnya.

1. "Integrasi logika orkestrasi microservice langsung ke dalam SDN data plane
   melalui switch, yang mengurangi latency untuk rute yang sudah didefinisikan,
   tetapi rentan ketika terjadi flow table miss sehingga request harus melewati
   controller pusat."

2. "Model manajemen request berbasis AI yang diamankan dengan blockchain,
   menggunakan Diffie-Hellman key exchange dan konsensus distributed ledger
   untuk autentikasi identitas microservice."

3. "Penambahan Gaussian noise menstabilkan pelatihan GAN dan menjamin
   konvergensi bahkan ketika overlap antara distribusi data riil dan sintetis
   sangat kecil."

4. "Objective function critic WGAN dengan gradient penalty berbasis norm L2
   pada gradien terhadap sampel interpolasi, untuk memenuhi kondisi
   1-Lipschitz continuity."

Untuk masing-masing, kutip kalimat spesifik dari sumber yang mendukungnya.
Kalau tidak ada sumber di notebook ini yang mendukung, katakan begitu.
```

---

## Prompt N2 — Ambang SLA yang bisa dipertanggungjawabkan (item B1, X6)

```
Paperku memakai ambang SLA latency untuk tiga jenis trafik IoT dan sumbernya
saat ini lemah (satu blog vendor, satu paper RAN slicing yang tidak relevan).

Cari di sumber-sumber notebook ini nilai ambang latency yang didukung
untuk masing-masing:

1. Telemetri lingkungan (sensor suhu/kelembapan, DHT11) — trafik best-effort
2. Video/citra dari kamera surveillance — trafik eMBB
3. Telemetri medis (heart rate, SpO2) — trafik URLLC / IoMT

Untuk setiap kategori, sebutkan:
- Nilai ambang yang direkomendasikan dan satuannya
- Sumber persisnya (judul, penulis, tahun)
- Kutipan kalimat aslinya
- Apakah sumber itu standar (ITU-T, 3GPP, IEEE) atau hasil eksperimen

Kalau ada beberapa nilai yang berbeda antar sumber, tampilkan semuanya
beserta konteksnya, jangan dirata-ratakan.
```

---

## Prompt N3 — Bahan tabel research gap (item E1)

```
Aku perlu membuat tabel research gap untuk bagian Related Work. Bantu aku
mengekstrak informasi terstruktur dari sumber-sumber di notebook ini.

Untuk setiap paper yang membahas DRL untuk network slicing, resource
allocation di SDN, atau orkestrasi microservice, buat entri dengan format:

| Penulis (tahun) | Pendekatan/algoritma | Action space (diskret/kontinu/hybrid) | Lingkungan evaluasi (simulasi/testbed fisik) | Kelebihan utama | Keterbatasan yang diakui penulis sendiri | Keterbatasan yang terlihat dari luar |

Aturan:
- Kolom "keterbatasan yang diakui penulis sendiri" harus dari bagian
  limitations/future work paper tersebut, bukan interpretasimu
- Kalau suatu kolom tidak disebutkan di paper, tulis "tidak disebutkan"
- Jangan menyimpulkan hal yang tidak tertulis

Urutkan dari yang paling relevan dengan orkestrasi resource SDN-IoT
berbasis DRL.
```

---

## Prompt N4 — Cek posisi kebaruan (item E1, dan sanity check klaim A1)

```
Berdasarkan seluruh sumber di notebook ini, jawab dengan jujur:

1. Berapa banyak paper yang memakai hybrid action space (kombinasi aksi
   diskret dan kontinu dalam satu policy) untuk network slicing atau
   resource allocation? Sebutkan mana saja dan bagaimana mereka
   memformulasikannya secara matematis.

2. Berapa banyak yang memakai generative model (GAN/VAE/diffusion) untuk
   augmentasi data trafik jaringan sebelum melatih agen RL? Sebutkan
   mana saja dan model apa yang dipakai.

3. Berapa banyak yang divalidasi di testbed fisik (bukan hanya simulasi
   NS-3/Mininet)? Hardware apa yang dipakai?

4. Berapa banyak yang menerapkan safety constraint / action masking /
   constrained RL pada orkestrasi jaringan? Bagaimana mereka
   memformulasikannya?

5. Adakah paper yang menggabungkan lebih dari dua hal di atas sekaligus?

Untuk setiap jawaban sertakan nama paper. Kalau jumlahnya nol untuk
suatu kategori, katakan nol.
```

---

## Prompt N5 — Formulasi safety layer dari literatur (pendukung item A2)

```
Aku perlu menulis formulasi matematis untuk "safety layer" pada agen RL
yang mengalokasikan bandwidth, yaitu mekanisme yang membatasi atau
memproyeksikan aksi agen sebelum dieksekusi, berdasarkan prediksi
pelanggaran SLA.

Dari sumber-sumber di notebook ini, kumpulkan:

1. Semua formulasi safety layer, action projection, action masking,
   shielding, atau constrained policy optimization yang ada. Tulis
   persamaannya persis seperti di sumber, sebutkan notasinya.
2. Bagaimana masing-masing pendekatan menangani kasus ketika aksi yang
   aman tidak tersedia?
3. Bagaimana safety layer berinteraksi dengan update gradient PPO —
   apakah gradien mengalir melalui layer tersebut atau tidak?
4. Metrik apa yang biasa dipakai untuk mengevaluasi efektivitas safety layer?

Kalau notebook ini tidak punya sumber tentang constrained/safe RL,
katakan begitu — berarti aku perlu menambahkan sumber baru.
```

---

## Prompt N6 — Melengkapi metadata referensi (item D5)

```
Salah satu referensiku tidak lengkap metadatanya. Cari di sumber notebook
ini dan lengkapi:

T. Mai, H. Yao, N. Zhang, W. He, D. Guo, M. Guizani,
"Transfer Reinforcement Learning aided Distributed Network Slicing
Optimization in Industrial IoT"

Aku butuh: nama jurnal/konferensi, volume, nomor, halaman, tahun, DOI.

Sekalian verifikasi apakah paper ini benar-benar mendukung klaim bahwa
"orkestrasi network slice pada microservice berbasis container membutuhkan
alokasi persentase yang fleksibel dan kontinu untuk memenuhi constraint QoS
dinamis" — itu konteks tempat aku menyitasinya. Kalau tidak mendukung,
sebutkan sumber mana di notebook yang lebih tepat.
```

---

## Prompt N7 — Deteksi klaim tak berdasar (sapu bersih)

```
Aku akan menempelkan beberapa kalimat dari draft paperku. Untuk setiap
kalimat, katakan apakah ada sumber di notebook ini yang mendukungnya,
dan sumber mana. Kalau tidak ada, katakan "tidak didukung sumber di notebook".

Jangan mencoba membenarkan kalimatku. Aku justru ingin menemukan yang lemah.

[Tempel di sini kalimat-kalimat bersitasi dari Section I dan Section II
 yang belum kamu verifikasi, sekitar 10-15 kalimat per batch]
```

Gunakan prompt ini secara batch untuk menyapu seluruh Section I dan II. Cara paling efisien: ambil setiap kalimat yang punya nomor sitasi, tempel 10–15 sekaligus.

---

## Alur kerja yang disarankan

1. `N1` dulu — ini langsung menyelesaikan D2, D3, D4
2. `N6` — cepat, menyelesaikan D5
3. `N2` — menentukan angka final untuk B1 bersama hasil audit kode
4. `N3` + `N4` — bahan mentah untuk tabel research gap (E1)
5. `N5` — hanya perlu kalau audit kode menunjukkan safety layer memang ada, untuk mencari cara memformulasikannya sesuai konvensi literatur
6. `N7` — terakhir, sebagai penyaring akhir sebelum submit

Simpan semua output NotebookLM ke satu dokumen, lalu bawa ke sini bersama hasil audit Claude Code.
