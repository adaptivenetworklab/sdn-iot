# Diagnostik pasca-sweep

Tanggal: 2026-09-24
Hasil primer: commit `1ab5ceb`, **dibekukan**. Dokumen ini tidak mengubahnya.
Verifikasi: md5 `results/tables/per_seed_summary.csv` dan `table_main.tex` identik sebelum dan
sesudah seluruh pekerjaan di bawah.

Seluruh keluaran diagnostik berada di `results/diagnostic/` dan diberi label
"DIAGNOSTIC - not for paper".

---

## 1. Kebocoran `demand_prop` — ada, tetapi tidak material

**Sumber mean.** `scripts/train_online.py:389-390` (versi saat sweep dijalankan):

```python
arrivals = load_arrival_trace()        # seluruh 1.022 baris
mean_demand = arrivals.mean(axis=0)    # mean atas seluruhnya
```

Mean dihitung atas seluruh trace, termasuk baris yang kemudian dievaluasi.

**Temuan yang lebih luas.** Baris 391 memberikan objek `arrivals` yang sama ke environment untuk
training maupun evaluasi. `evaluate()` hanya mengganti seed RNG untuk titik start episode. Dengan
`episode_len=200` pada trace 1.022, start acak jatuh di `[0, 822]`, sehingga episode training dan
evaluasi beririsan besar.

**Tidak ada split train/eval di eksperimen online — untuk metode mana pun.** Ini bukan cacat
khusus `demand_prop`.

**Perhitungan ulang.** Ditambahkan flag `--demand-source {full,train}` (default `full`, sehingga
perilaku hasil primer tidak berubah). Versi `train` memakai mean dari 80% awal trace.

```
mean demand FULL  (1022 baris): [3.8520  3.8520  4.5739]
mean demand TRAIN ( 817 baris): [3.7538  3.7542  4.4745]
selisih relatif               : [-2.55%  -2.54%  -2.17%]
```

| Varian | n | P1 | P2 | P4 | Total Viol % [CI 95%] | reward |
|---|---|---|---|---|---|---|
| `demand_prop` mean FULL | 10 | 16,31 | 15,08 | 16,89 | **16,10** [14,79, 17,33] | −10,560 |
| `demand_prop` mean TRAIN | 10 | 16,31 | 15,08 | 16,72 | **16,04** [14,74, 17,26] | −10,554 |

Mann-Whitney U: **p = 0,7337**. Selisih −0,058 poin.

**Kesimpulan:** kebocoran nyata tetapi tidak menjelaskan apa pun. Trafik cukup stabil sehingga
mean 80% awal hampir sama dengan mean keseluruhan. `demand_prop` tetap mengungguli Proposed
(28,25%) dengan selisih sekitar 12 poin. Memperbaiki kebocoran ini tidak menyelamatkan klaim
paper.

---

## 2. `const_max` identik dengan `no_control` — konsekuensi desain, bukan bug kode

Verifikasi numerik pada `slice_env.SliceEnv`:

```
rates awal:                    [4. 4. 4.]  sum 12.0 = C
proyeksi a = +1 (seragam):     [4. 4. 4.]
proyeksi a =  0:               [4. 4. 4.]
proyeksi a = [+1, 0, -1]:      [4.8 4.  3.2]
```

Aksinya perubahan **multiplikatif relatif** (`slice_env.py` `step()`:
`rates * (1 + action_gain * a)`), lalu diproyeksikan ke `sum(rates) <= C`. Menaikkan seluruh
slice dengan faktor sama lalu menormalkan kembali ke kapasitas menghasilkan alokasi yang persis
sama. Aksi seragam adalah no-op.

**Implikasi:** ruang aksi efektif memiliki **2 derajat kebebasan, bukan 3**. Hanya perbedaan
relatif antar slice yang berpengaruh. `const_max` bukan baseline "maksimalkan" yang bermakna —
ia duplikat `no_control`, dan tabel hasil primer memuat dua baris yang secara struktural identik.

Sesuai instruksi, tidak diperbaiki.

---

## 3. Konvergensi — tidak satu pun metode learning konvergen

Anggaran sweep: `--steps 60000`, `--rollout 2048` → PPO hanya menerima **30 update rollout**.

`scripts/plot_convergence.py` membaca `results/online/*_train.csv` yang sudah ada (tanpa
retraining) dan menghasilkan `results/diagnostic/convergence_all.png` serta
`convergence_flatness.csv`.

Uji kedataran: perubahan kuartal terakhir terhadap kuartal pertama, dinyatakan sebagai fraksi
rentang tiap kurva. Ambang konvergen `|delta| < 0,10`.

| Metode | Metrik | delta (fraksi rentang) | std | Konvergen |
|---|---|---|---|---|
| PPO | mean_reward | **+0,5199** | 0,1733 | **TIDAK** |
| SDH-PPO | mean_reward | **+0,2017** | 0,1042 | **TIDAK** |
| PPO | loss_critic | −0,0155 | 0,2655 | ya |
| SDH-PPO | loss_critic | **−0,1563** | 0,1125 | **TIDAK** |
| DQN | loss | +0,0739 | 0,0341 | ya |
| DDQN | loss | **+0,1067** | 0,0316 | **TIDAK** |

Reward PPO masih bergerak sebesar 52% rentangnya pada kuartal terakhir. Keduanya masih menanjak,
artinya kedua metode dihentikan di tengah proses belajar.

`loss_critic` SDH-PPO berada di kisaran 56.000–120.000 pada akhir training. Reward per langkah
bernilai −10 sampai −30 tanpa normalisasi; return berdiskonto sepanjang 200 langkah menghasilkan
target value berorde ribuan. Itu penyebab paling mungkin.

**Kesimpulan:** perbandingan primer adalah antara empat agen yang belum konvergen. Klaim
"Proposed mengungguli PPO/DQN/DDQN" belum tentu bertahan dengan anggaran training memadai, dan
tidak boleh dilaporkan tanpa kualifikasi ini.

---

## 4. Arm `real_only` dan `aug_subsample` tidak ada — belum terdefinisi secara konseptual

`train_online.py:53`: `ARMS = ["full", "no_mask", "no_dueling"]`.

Kedua arm tersebut dirancang untuk pipeline **offline**, yang beroperasi pada baris dataset
`(s, a, r, s')` hasil WGAN-GP. Pipeline online tidak memakai dataset itu sama sekali: arrival
diambil langsung dari `rx_mbps` trace riil, dan WGAN-GP tidak berperan di mana pun.

**Yang dibutuhkan agar dapat dijalankan dengan protokol identik:**

1. Definisikan ulang augmentasi sebagai **pembangkit trace arrival**, bukan pembangkit baris
   dataset. WGAN dilatih pada deret `rx_mbps` dari split train, menghasilkan trace sintetis.
2. Split trace riil lebih dulu (butir 1 di atas), latih WGAN hanya pada bagian train.
3. `real_only`: training memakai trace riil bagian train saja.
   `aug_subsample`: training memakai trace sintetis dengan panjang sama, sebagai kontrol volume.
   Evaluasi kedua arm tetap pada trace riil hold-out yang sama.
4. Tambahkan pemuat trace ke `SliceEnv` yang menerima trace train dan eval terpisah.

Ini keputusan desain tersendiri, bukan sekadar menambah nama arm.

---

## 5. Kronologi bug safety layer — tidak ada run yang dibuang

| Peristiwa | Waktu |
|---|---|
| Run sweep paling awal | 2026-09-24 14:02:20 UTC |
| Run sweep paling akhir | 2026-09-24 14:50:34 UTC |
| Commit `1b6345b` (`train_online.py`) | 2026-09-24 14:54 UTC |

- Versi bermasalah (membandingkan z-score `state[10]` dengan ambang milidetik) berada di
  `scripts/sweep.py`, **sengaja dipertahankan** sebagai port setia notebook lama.
- Versi diperbaiki ditulis baru di `train_online.py` (`safety_mask`), membandingkan rasio delay
  terhadap SLA sehingga kedua sisi bersatuan sepadan. Versi bermasalah **tidak pernah ada** di
  pipeline online.
- 100 job = 100 file `_eval.csv`. Tidak ada run yang dibuang atau diulang.

---

## 6. Safety layer untuk baseline — usaha rendah, dan ini masalah keadilan

**Estimasi: 10–15 baris, tanpa perubahan arsitektur.**

`safety_mask()` sudah generik: menerima action dan env, mengembalikan action yang disesuaikan.

- **PPO standar:** lepas gate `args.algo == "sdhppo"` pada penentuan `use_mask`. Fungsinya sudah
  dipanggil di jalur PPO, baik saat rollout maupun evaluasi.
- **DQN/DDQN:** terapkan pasca-hoc di dalam closure `policy()`, satu baris, persis seperti jalur
  PPO.
- Tambahkan nama arm agar dapat dinyalakan per metode.

**Mengapa ini penting.** Saat ini **hanya `sdhppo`** yang memperoleh safety layer. Ablation
menunjukkan lapisan itu menyumbang **22 poin** violation (28,25% → 50,11%, p = 0,0004) —
kontributor tunggal terbesar, jauh melampaui dueling critic yang nol.

Artinya sebagian besar keunggulan Proposed atas PPO mungkin sekadar keunggulan "punya safety
layer" lawan "tidak punya", bukan keunggulan algoritma. Secara struktural ini pola yang sama
dengan koefisien 0,15 lawan 0,10 pada notebook lama: satu komponen menguntungkan yang hanya
diberikan kepada metode yang diusulkan.

Tidak diimplementasikan, sesuai instruksi.

---

## 7. Stasioneritas dan asal arrival

**Arrival tidak dibangkitkan model.** Diputar ulang dari kolom `rx_mbps_p{1,2,4}` pada
`dataset_dqn_rich.csv`: 1.022 baris, 19 menit 59 detik, interval ~1,17 detik.

`slice_env.py` `_arrival()` mengindeks `(start + t) % len(arrivals)` — wrap modulo.

- **Split:** tidak ada. Training dan evaluasi menarik dari 1.022 baris yang sama; yang berbeda
  hanya titik start episode.
- **Stasioner?** Trace ini satu realisasi pendek dari satu pola trafik. Korelasi temporal dalam
  episode terjaga, tetapi tidak ada variasi rezim, tidak ada perubahan beban, dan **tidak ada uji
  stasioneritas yang dijalankan**. Bukti tidak langsung dari butir 1: mean 80% awal hanya berbeda
  ~2,5% dari mean keseluruhan, konsisten dengan trafik yang cukup stabil sepanjang 20 menit.
- **Artefak wrap:** modulo menyambung akhir trace kembali ke awal, menciptakan diskontinuitas
  buatan pada episode yang melewati batas.

---

## Ringkasan dampak terhadap hasil primer

| # | Temuan | Dampak |
|---|---|---|
| 1 | Kebocoran `demand_prop` | **Tidak material** (p = 0,73). Heuristik tetap unggul ~12 poin |
| 1b | Tidak ada split train/eval untuk metode mana pun | **Besar** — seluruh angka bersifat in-sample |
| 2 | `const_max` degenerate | Sedang — satu baris tabel tidak bermakna |
| 3 | Tidak ada metode yang konvergen | **Besar** — ranking belum tentu stabil |
| 5 | Kronologi bersih | Tidak ada |
| 6 | Safety layer hanya untuk Proposed | **Besar** — perbandingan tidak setara |

Butir 1b, 3, dan 6 masing-masing cukup untuk mengubah interpretasi. Hasil primer tetap sah
sebagai catatan jujur dari satu konfigurasi eksperimen, tetapi belum dapat dipakai mengklaim
keunggulan algoritma.
