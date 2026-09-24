# Prompt untuk Claude Code — Audit Repo `adaptivenetworklab/sdn-iot`

Tujuan: ground-truth semua klaim metodologi di paper terhadap kode yang benar-benar dijalankan.

**Cara pakai:** jalankan `claude` di root repo, lalu tempel prompt satu per satu berurutan. Prompt 0 dulu (orientasi), baru sisanya. Simpan setiap output ke file terpisah.

**Aturan penting yang berlaku untuk semua prompt:** minta Claude Code selalu menyertakan `path/file.py:nomor_baris` sebagai bukti, dan menjawab **"TIDAK DITEMUKAN"** kalau memang tidak ada. Jangan biarkan ia menyimpulkan dari nama variabel saja.

---

## Prompt 0 — Orientasi repo

```
Aku sedang merevisi paper akademik berdasarkan repo ini. Aku butuh peta kode
yang akurat sebelum menulis ulang bagian Methodology.

Tolong petakan repo ini dan jawab:

1. Entry point training untuk tiap algoritma (SDH-PPO, PPO standar, DQN, DDQN,
   static heuristic). File mana, fungsi mana?
2. Di mana definisi environment (state, action, reward, step)? File dan class-nya.
3. Di mana kode GAN/WGAN untuk augmentasi data?
4. Di mana kode yang berjalan di Raspberry Pi (runtime/deployment) versus kode
   yang berjalan saat training?
5. Ada file config/YAML/JSON untuk hyperparameter? Di mana?
6. Ada script untuk generate figure/plot hasil? Di mana output-nya disimpan?
7. Apakah ada eksperimen yang jelas sudah usang atau tidak dipakai di paper?
   Tandai supaya aku tidak salah rujuk.

Untuk setiap jawaban sertakan path file dan nomor baris. Jangan menebak.
Kalau tidak ada, tulis "TIDAK DITEMUKAN".

Tulis hasilnya ke `docs/audit/00-repo-map.md`.
```

---

## Prompt 1 — Hybrid action space (item A1)

```
Paper ini mengklaim SDH-PPO memakai "hybrid action space" yaitu continuous
bandwidth adjustment DAN discrete port selection dalam satu policy PPO.

Verifikasi klaim ini terhadap kode. Jawab spesifik:

1. Apa persis bentuk action space agen SDH-PPO? Tunjukkan definisinya
   (gym.spaces.* atau ekuivalennya) dengan path:baris.
2. Apakah ada komponen diskret di action? Kalau ya, berapa dimensinya dan
   apa artinya? Kalau tidak, katakan "TIDAK ADA KOMPONEN DISKRET".
3. Bagaimana output head Actor network dibentuk? Berapa head, masing-masing
   menghasilkan apa (mean/std Gaussian? logits kategorikal?).
4. Kalau memang hybrid: bagaimana log-probability gabungan dihitung untuk
   PPO ratio? Tunjukkan kodenya.
5. Bagaimana entropy dihitung kalau ada dua jenis distribusi?
6. Apakah arsitekturnya cocok dengan pendekatan yang ada di literatur
   (parameterized action space / P-DQN / PADQN / hybrid PPO), atau ini
   pendekatan sendiri? Jelaskan.
7. Bandingkan dengan action space PPO standar di repo ini. Apa bedanya persis?

Sertakan cuplikan kode relevan. Tulis ke `docs/audit/01-action-space.md`.
```

---

## Prompt 2 — Safety layer (item A2)

```
Paper mengklaim kontribusi berupa "mathematical security layer based on action
predictions" (disebut juga "safety layer") yang memandu keputusan agen secara
proaktif. Di paper tidak ada satu pun persamaan untuk ini.

Cari implementasinya di kode:

1. Apakah ada modul/fungsi/class yang memodifikasi, membatasi, memproyeksikan,
   atau memveto action sebelum dieksekusi ke environment? Cari juga di luar
   nama "safety" (misalnya clamp, clip, constrain, guard, shield, mask,
   projection, fallback, threshold).
2. Kalau ada: tulis logikanya sebagai pseudocode dan sebagai formula matematis
   yang bisa langsung kutulis di paper. Sebutkan semua konstanta/threshold
   beserta nilainya dan dari mana asalnya.
3. Apakah safety layer ini aktif saat training, saat inference, atau keduanya?
4. Apakah ia memakai prediksi (misal predicted delay/violation) sebagai input?
   Kalau ya, prediksi itu dari mana — Critic, model terpisah, atau heuristik?
5. Kalau tidak ada sama sekali, katakan "TIDAK DITEMUKAN" dan sebutkan
   mekanisme apa saja yang paling mendekati, supaya aku bisa memutuskan
   apakah menurunkan klaim atau mendeskripsikan yang ada.

Tulis ke `docs/audit/02-safety-layer.md`.
```

---

## Prompt 3 — Dueling critic (item A3)

```
Paper menyebut "Dueling Critic" dan "duel layer" sebagai bagian arsitektur
SDH-PPO, tapi tidak pernah mendefinisikannya. Dueling itu konsep dari DQN.

Verifikasi di kode:

1. Apakah Critic network SDH-PPO dipecah menjadi dua stream (state-value dan
   advantage)? Tunjukkan definisi arsitekturnya dengan path:baris.
2. Kalau ya: bagaimana kedua stream digabungkan? Tulis formulanya.
   Bagaimana ini berinteraksi dengan GAE, yang sudah menghitung advantage sendiri?
3. Kalau tidak: apakah "duel layer" merujuk ke sesuatu yang lain di kode
   (misalnya dua critic terpisah ala TD3, atau dua hidden layer)? Jelaskan.
4. Tunjukkan arsitektur lengkap Actor dan Critic SDH-PPO: jumlah layer,
   lebar tiap layer, fungsi aktivasi, inisialisasi.
5. Bandingkan dengan arsitektur Actor-Critic PPO standar di repo ini.

Tulis ke `docs/audit/03-critic-architecture.md`.
```

---

## Prompt 4 — EO-WGAN (item A4)

```
Paper menyebut "Enhanced Optimization-Wasserstein GAN (EO-WGAN)" sebagai
kontribusi, tapi persamaan yang ditulis persis WGAN-GP standar (Gulrajani 2017).
Kesimpulan paper malah menyebutnya "WGAN-GP". Aku perlu tahu mana yang benar.

Periksa kode GAN di repo:

1. Loss function critic dan generator: tulis persis seperti di kode. Apakah
   ada suku tambahan di luar WGAN-GP standar?
2. Gradient penalty: bagaimana diimplementasikan? Nilai lambda berapa?
3. Apakah ada modifikasi non-standar? Cek: optimizer khusus, learning rate
   schedule, arsitektur generator/critic yang tidak biasa, spectral norm,
   noise injection, curriculum, loss tambahan, teknik seleksi sampel.
4. Apakah Gaussian noise sigma=0.5 (Eq 1 di paper) benar-benar ada di kode?
   Di mana diterapkan — pada input real, pada latent, atau di tempat lain?
5. Berapa persis semua hyperparameter GAN: n_critic, lr generator, lr critic,
   betas Adam, latent dim, batch size, jumlah epoch, arsitektur tiap network?
6. Kesimpulan: apakah ini WGAN-GP standar, atau ada enhancement nyata?
   Kalau ada, sebutkan persis apa yang di-enhance. Kalau tidak, katakan
   "STANDAR WGAN-GP, TIDAK ADA ENHANCEMENT".

Tulis ke `docs/audit/04-eowgan.md`.
```

---

## Prompt 5 — State space, reward, dan pemetaan port (item A5, B1, B3, X2, X3)

```
Aku perlu definisi formal environment untuk ditulis di paper.

1. **State space.** Paper menyebut "37 state features" tanpa enumerasi.
   Enumerasi semua 37 fitur dari kode: nama, satuan, sumber (dari metrik apa),
   dan rentang nilainya. Kalau jumlahnya bukan 37, katakan berapa sebenarnya.
   Bagaimana normalisasinya (z-score? min-max? running mean)?

2. **Reward function.** Tulis reward function persis seperti di kode,
   termasuk semua bobot dan konstanta. Paper menulis:
   `R_total = 0.4*R_thr - 0.6*P_lat_p4 - 0.2*P_drop`
   Verifikasi apakah ini benar. Khususnya:
   - Apakah penalti latency HANYA untuk port 4, atau ada juga untuk port 1 dan 2?
   - Apakah reward throughput HANYA dari port 2?
   - Kalau benar hanya P4 dan P2, jelaskan mekanisme apa yang membuat agen
     tetap memperbaiki SLA di port 1 (paper mengklaim 1.5% violation di P1).

3. **Pemetaan port, slice, dan priority.** Ini membingungkan di paper.
   Dari kode, buat tabel: port ID → sensor/traffic type → slice → priority level
   → SLA threshold. Sertakan port 3 kalau ada.

4. **Ambang SLA.** Nilai threshold berapa yang benar-benar dipakai di kode
   untuk tiap port saat evaluasi? Paper punya tiga versi berbeda
   (10/150/10 ms di Tabel II, 6/7/7 ms di hasil, dan "10 ms" di teks P4).
   Mana yang benar? Tunjukkan konstantanya di kode.

5. **Port 3.** Apakah ada di environment? Kalau ada, kenapa tidak muncul di
   hasil? Kalau tidak ada, sejak kapan dihilangkan?

Sertakan path:baris untuk semua. Tulis ke `docs/audit/05-mdp-definition.md`.
```

---

## Prompt 6 — Baseline dan protokol training (item C2, C3, C5)

```
Reviewer mempertanyakan keadilan perbandingan antar algoritma. Aku perlu
detail implementasi semua baseline.

1. **Static heuristic.** Bagaimana persis ia mengalokasikan resource?
   Fixed policing rate? Round-robin? Proporsional? Tulis algoritmanya sebagai
   pseudocode. Paper menyebut "evaluated for gamma=0.99 over 2000 steps" —
   gamma untuk heuristik non-AI itu janggal, verifikasi apa maksudnya.

2. **DQN dan DDQN.** Untuk masing-masing:
   - epsilon schedule (nilai awal, akhir, decay, dan apakah epsilon dimatikan
     saat evaluasi)
   - target network update frequency (hard atau soft/tau)
   - replay buffer size, warmup steps, batch size
   - bagaimana action space kontinu didiskretisasi, berapa bin
   - arsitektur network

3. **PPO standar dan SDH-PPO.** Untuk masing-masing:
   - clip ratio epsilon, GAE lambda, entropy coefficient, value loss coefficient
   - jumlah update epoch per rollout, rollout length, minibatch size
   - gradient clipping, advantage normalization
   - apakah reward di-normalisasi/di-scale

4. **"2000 epochs" itu apa?** Updates, episodes, atau environment steps?
   Untuk tiap algoritma, hitung berapa total environment steps yang dijalani.
   Apakah semua algoritma mendapat budget interaksi yang sama? Kalau tidak,
   sebutkan perbedaannya — ini isu fairness yang akan ditanya reviewer.

5. Buat satu tabel hyperparameter lengkap yang siap kupasang di paper,
   dengan kolom per algoritma. Tandai parameter yang shared vs algorithm-specific.

Tulis ke `docs/audit/06-baselines-hyperparams.md`.
```

---

## Prompt 7 — Seeds, reproducibility, dan hasil (item C1)

```
Reviewer menolak klaim "consistently outperforms" karena tidak ada seed,
confidence interval, atau uji signifikansi.

1. Apakah kode men-set random seed? Di mana, dan untuk library apa saja
   (python random, numpy, torch, environment)?
2. Berapa run yang benar-benar dijalankan untuk menghasilkan angka di paper
   (1.5%, 29.5%, 0.0%, 10.3%, dst)? Cari di logs, results, checkpoints,
   atau nama file output.
3. Apakah ada hasil multi-seed yang tersimpan tapi belum dipakai di paper?
4. Bagaimana metrik "violation rate" dihitung persis? Tunjukkan kodenya.
   Berapa panjang window evaluasi, berapa sampel?
5. Apakah evaluasi memakai policy stochastic atau deterministic/greedy?
   Untuk DQN/DDQN, apakah epsilon di-set 0 saat evaluasi?
6. Berapa lama satu run memakan waktu, dan di hardware apa?
7. Apa yang perlu kutambahkan ke kode supaya bisa menjalankan N seed dan
   menghasilkan mean ± 95% CI plus uji signifikansi? Buatkan rencana konkret
   (file mana yang diubah, script apa yang perlu dibuat). Jangan jalankan
   dulu, cukup rencananya.

Tulis ke `docs/audit/07-reproducibility.md`.
```

---

## Prompt 8 — Hardware, deployment, dan figure (item C6, E2)

```
1. **Deployment.** Apa persis yang berjalan di Raspberry Pi 5 saat runtime?
   Training penuh, inference saja, atau hanya kolektor metrik? Tunjukkan
   kodenya. Apakah ada model checkpoint yang di-load di Pi?
2. Apakah ada dokumentasi/script yang menyebut spesifikasi hardware:
   model Pi 5, RAM, OS, versi Python, versi PyTorch/TF, versi Ryu, OvS,
   Flowvisor, Kubernetes? Kumpulkan semuanya. Cek juga requirements.txt,
   Dockerfile, docker-compose, manifest k8s, README, dan Ansible/setup script.
3. Kalau training dilakukan di mesin lain (bukan Pi), cari buktinya dan
   sebutkan spesifikasinya.
4. Berapa runtime per epoch dan total, kalau tercatat di log?
5. **Figure.** Script mana yang menghasilkan plot di paper (scatter augmentasi,
   port delay track, kurva konvergensi)? Apakah menyimpan sebagai PNG dengan
   dpi default? Tunjukkan baris `savefig`-nya. Aku butuh semua figure
   di-regenerate sebagai vektor (PDF/SVG) atau minimal 300 dpi — buatkan
   perubahan yang diperlukan.

Tulis ke `docs/audit/08-deployment-figures.md`.
```

---

## Prompt 9 — Sintesis akhir

```
Baca semua file di `docs/audit/`. Buat satu ringkasan eksekutif yang menjawab
pertanyaan tunggal ini:

Untuk masing-masing dari 4 klaim metodologi paper —
(a) hybrid action space, (b) safety layer, (c) dueling critic, (d) EO-WGAN —
klasifikasikan sebagai salah satu dari:

  ADA PENUH      : diimplementasi dan dipakai di run yang menghasilkan
                   angka paper. Sertakan formula/pseudocode siap tulis.
  ADA SEBAGIAN   : ada tapi berbeda dari deskripsi paper. Jelaskan bedanya.
  ADA TAPI MATI  : ada di kode tapi tidak aktif di run yang dipakai
                   (flag off, dead code, cabang tak terpakai).
  TIDAK ADA      : tidak ditemukan.

Untuk setiap klaim, beri rekomendasi: "deskripsikan di Section III" atau
"turunkan klaim di Abstract/Intro/Kesimpulan/Tabel I".

Terakhir: daftar semua ketidakcocokan lain antara kode dan angka/pernyataan
di paper yang kau temukan selama audit, yang belum kusebutkan.

Tulis ke `docs/audit/09-summary.md`.
```

---

## Setelah selesai

Bawa isi `docs/audit/09-summary.md` kembali ke sini. Itu yang menentukan apakah Section III ditulis ulang untuk mendeskripsikan implementasi yang ada, atau klaim paper yang perlu diturunkan.
