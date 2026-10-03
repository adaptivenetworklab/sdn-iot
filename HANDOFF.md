# Handoff kampanye eksperimen SDH-PPO

Tanggal: 2026-10-02
Untuk: sesi Claude Code berikutnya di repo ini
Commit terakhir: `c5637d5`
Dokumen pendamping: `docs/experiments/07-protocol-v2.md` (protokol final), `00-06` (rantai audit)

Dokumen ini operasional, bukan narasi. Isinya hal-hal yang tidak bisa dibaca dari kode maupun git
history: aturan yang diberikan user dan masih berlaku, keputusan yang sudah terkunci, dan jebakan
yang sudah memakan waktu.

## 1. Status dan gate sekarang

Kampanye berhenti di satu titik: **protokol V2 menunggu persetujuan user**. Sampai user menyetujui
`docs/experiments/07-protocol-v2.md`, sweep final tidak boleh dijalankan.

| Pemeriksaan | Nilai saat handoff |
|---|---|
| Proses training berjalan | 0 |
| File hasil dari split test | 0 |
| Run tuning putaran final selesai | 96 dari 96 |
| Hash V1 `results/tables/per_seed_summary.csv` | `9bf540a14140af920667114be731e26f` |

Jangan tafsirkan "semua run selesai" sebagai izin lanjut. Yang selesai adalah tuning di train/val.
Sweep final dan split test masih di balik gate persetujuan.

## 2. Aturan berdiri dari user

Enam aturan ini diberikan di awal kampanye dan masih berlaku. Bukan sejarah.

1. Jangan pernah menulis angka hasil secara manual, di mana pun. Semua angka harus datang dari
   skrip yang membaca CSV.
2. Jangan menyetel apa pun berdasarkan hasilnya. Tidak ada cherry-pick seed, tidak ada perubahan
   ambang setelah melihat hasil.
3. Kalau menemukan kode lain yang menghasilkan angka secara sintetis, hardcode, atau mock,
   laporkan. Jangan perbaiki diam-diam.
4. Kalau hasilnya menunjukkan Proposed tidak menang, laporkan apa adanya.
5. Tujuan kampanye ini perbandingan yang adil, bukan perbandingan yang dimenangkan.
6. Hormati setiap STOP.

Aturan 1 bukan formalitas. Tabel di `07-protocol-v2.md` §2.4 dan §2.6 dibangkitkan dari
`results/tuning-v2/selection.csv` lewat skrip, lalu disisipkan. Kalau tabel itu perlu diperbarui,
bangkitkan ulang; jangan ketik ulang angkanya.

## 3. Batasan sesi

- Jangan edit apa pun di `revision/`, termasuk `main.tex`. Ada sesi Claude lain yang bekerja di
  sana. Membaca boleh.
- Jangan ubah `.gitignore`.
- Semua run pakai `--device cpu`.
- Output diagnostik ke `results/diagnostic/`, setiap file diberi label "DIAGNOSTIC, bukan untuk
  paper".
- Kalau sebuah keputusan ternyata tidak bisa diterapkan persis seperti tertulis, berhenti dan
  laporkan. Jangan improvisasi, jangan pilih alternatif sendiri.

Batasan terakhir itu sudah terpakai sekali. Upaya perbaikan WGAN gagal sementara upaya kedua
seragam lebih baik dari yang pertama. Aturan yang ditetapkan di muka berbunyi "kalau gagal, pakai
generator lama", dan aturan itu bisa diterapkan persis, jadi generator lama yang dipakai dan
keunggulan upaya kedua hanya dicatat. Bukan ditukar sendiri.

## 4. Yang sudah dijalankan dan di mana hasilnya

| Blok | Run | Lokasi | Status |
|---|---|---|---|
| Pilot, 4 learner x 2 safety x 2 seed | 16 | `results/pilot/` | selesai |
| Tuning putaran 1 | 64 | `results/tuning/` | diarsipkan, tidak dipakai |
| Tuning putaran final | 96 | `results/tuning-v2/` | selesai, dipakai |
| Uji behavior cloning | 2 | `results/diag2/bc_probe.csv` | selesai |
| Smoke test skenario dan residual | 6 | `results/smoke/round2/` | selesai, gitignored |
| V1 (kampanye lama) | 100 | `results/tables/` | beku, tidak dipakai di paper |

Putaran 1 diarsipkan karena aturan seleksinya cacat, bukan karena hasilnya tidak disukai. Rinci di
§7. Hasilnya tidak dihapus.

Wall time terukur dari `results/tuning-v2/run.log`, berguna untuk estimasi sweep final:

| Metode | n | Rentang | Rata-rata |
|---|---|---|---|
| PPO | 16 | 951 sampai 1136 s | 1009 s |
| SDH-PPO | 16 | 992 sampai 1171 s | 1049 s |
| SDH-PPO residual | 16 | 1008 sampai 1172 s | 1049 s |
| SDH-PPO + BC init | 16 | 1079 sampai 1244 s | 1118 s |
| DQN | 16 | 1895 sampai 2816 s | 2527 s |
| DDQN | 16 | 2152 sampai 3422 s | 2989 s |

Keluarga Q dua sampai tiga kali lebih lambat karena melakukan update tiap step, bukan tiap
rollout. Jangan pakai satu angka rata-rata untuk seluruh metode saat memperkirakan durasi; itu
kesalahan yang sempat membuat estimasi ke user meleset tiga kali lipat.

## 5. Keputusan pra-registrasi yang terkunci

Aturan berhenti ada di `07-protocol-v2.md` §10. Begitu protokol disetujui, tidak ada perubahan
desain, dan setiap ide sesudahnya berlabel EKSPLORATIF tanpa klaim signifikansi.

**Seleksi checkpoint.** Batas 300.000 step sama untuk semua metode, probe val tiap 25.000 step, 20
episode per probe, himpunan episode probe tetap, tepat 12 probe untuk keempat metode, checkpoint
dengan val terbaik dipulihkan di akhir. Step terpilih dicatat sebagai `best_val_step`.

Konfigurasi terpilih, dari `results/tuning-v2/selection.csv`:

| Metode | Konfigurasi | Val viol % (sd) | Putaran 1 |
|---|---|---|---|
| DQN | `lr3e-4_ts2000_b11_ed30000` | 35,93 (1,23) | 37,42 |
| DDQN | `lr3e-4_ts2000_b11_ed30000` | 35,98 (0,40) | 38,80 |
| PPO | `lr3e-4_ent0.01_clip_rs19.0106` | 51,50 (3,06) | 51,87 |
| SDH-PPO | `lr1e-4_ent0.0_clip_rs19.0106` | 51,58 (0,87) | 51,77 |
| SDH-PPO residual | `lr1e-4_ent0.01_clip_rs1.0` | 33,10 (0,80) | tidak ada |
| SDH-PPO + BC init | `lr1e-4_ent0.01_tanh_rs19.0106` | 33,28 (0,78) | tidak ada |

Baseline heuristik di val yang sama, dari `results/pilot/`: `demand_prop` 32,37 (safety off) dan
32,47 (on), `no_control` 58,60 dan 35,03, `equal_split` 53,77 dan 40,13, `threshold` 68,43 dan
67,03.

Parameter lain yang sudah terkunci dan tidak boleh di-tuning:

- `residual_bound = 0,25`, ditetapkan di muka dan sengaja tidak masuk grid. Konsekuensinya
  sensitivitas terhadap nilai itu belum diukur, dan itu sudah dicatat sebagai penyimpangan.
- Skenario `diurnal`: amplitudo 0,35, periode 100 baris. Skenario `flash`: slice P2, faktor 4,
  durasi 45 baris, mulai di 40% trace.
- Arm augmentasi memakai generator upaya 1. Ambang lolos tertulis sebagai konstanta di
  `scripts/make_synth_trace.py` dan tidak boleh dilonggarkan.
- Aturan `threshold` punya cacat di cabang negatifnya dan sengaja tidak diperbaiki, supaya
  baseline tidak disetel setelah hasilnya terlihat. Rinci di `07-protocol-v2.md` §4.1.

Keluarga uji primer (a) sampai (e) ada di §8, dengan koreksi Holm di dalam tiap keluarga, bukan
lintas keluarga.

## 6. Perintah untuk melanjutkan

Sweep final, hanya setelah protokol disetujui: 380 run, 10 seed per konfigurasi, sekitar 21 jam
dengan 12 proses paralel. Bentuknya ada di `07-protocol-v2.md` §7.2. Skenario non-stasioner tidak
menambah run karena `--eval-scenario` menilai kebijakan yang sama di proses yang sama.

Periksa antrean sebelum menghabiskan jam CPU:

```bash
DRY=1 bash scripts/run_tuning.sh results/tuning-v2 12 2 300000
```

Keluaran harus 0 run karena semuanya sudah selesai. Kalau bukan 0, ada yang hilang.

Turunkan ulang seleksi dan gate-nya:

```bash
python scripts/summarize_tuning.py                      # terpilih + probe parity + gap
python scripts/summarize_tuning.py --dir results/tuning # pembanding putaran 1 yang cacat
```

Satu run tunggal, misalnya untuk smoke test:

```bash
python scripts/train_online.py --algo sdhppo --phase train --eval-phase val \
  --safety off --seed 0 --steps 300000 --episode-len 50 --eval-every 25000 \
  --probe-episodes 20 --eval-episodes 20 --random-init-alloc --device cpu \
  --reward-scale 19.0106 --out results/smoke/cek
```

Flag yang perlu diketahui: `--residual {off,on}` dengan `--residual-bound`,
`--actor-init {random,bc}`, `--eval-scenario {diurnal,flash}` (boleh diulang),
`--safety {on,off}`, `--phase` dan `--eval-phase`.

Split test ada di balik `--allow-test` dan dibuka sekali saja, di run final V2. Tanpa flag itu
`train_online.py` menolak berjalan, dan penolakan itu memang disengaja.

## 7. Jebakan yang sudah ditemukan

Semua ini sudah terjadi di sesi sebelumnya dan sudah diperbaiki. Dicatat supaya tidak terulang.

**`xargs -P 0` berarti paralelisme tak terbatas, bukan nol.** Satu tes dry-run melahirkan 96
proses sekaligus. Satu launcher yatim lolos dari pembersihan dan baru ketahuan tiga jam kemudian,
sambil mencuri satu core dari sweep yang asli. Pakai `DRY=1`, bukan `-P 0`, untuk memeriksa
antrean.

Variabel multi-baris pecah di xargs. `COMMON` di `scripts/run_tuning.sh` sengaja ditulis satu
baris panjang. Versi yang terbungkus tiga baris membuat 96 job menjadi 288 perintah terpotong yang
tetap berjalan karena argumen sisanya terisi default.

Penjaga resume gagal dua kali, dengan sebab berbeda. Versi pertama memakai path tanpa nomor seed,
jadi seed 0 yang selesai menutupi seed 1 yang belum jalan, dan 18 dari 64 run terlewat tanpa pesan
apa pun. Versi kedua sadar seed tetapi hanya mencocokkan `*_seed$s_eval.csv`, sementara arm
residual dan BC menulis `..._seed0_res0.25_eval.csv` dan `..._seed0_init-bc_eval.csv`. Akibatnya 32
run yang sudah selesai selalu terlihat belum jalan, dan `DRY=1` mengantrekan 32 bukan 0. Ketemu
saat verifikasi handoff ini, lalu diperbaiki dengan menambahkan pola kedua `*_seed$s_*_eval.csv`.
Pelajarannya: uji penjaga resume dengan `DRY=1` setelah selesai, bukan sebelum, dan harapkan
antreannya nol.

Direktori konfigurasi yang masih kosong bukan tanda run gagal. `train_online.py` baru membuat
direktori keluaran di akhir proses. Baca `run.log`, jangan simpulkan dari daftar direktori. Ini
sempat membuat kesimpulan keliru bahwa seluruh sweep sedang gagal.

`results/tuning/_verify/` mencemari statistik gap kalau prefiks arm tidak difilter. Run verifikasi
pendek di sana hanya punya 2 probe, sehingga minimum probe terlaporkan 2 bukan 11, dan jumlah run
65 bukan 64. `summarize_tuning.py` sudah memfilter; skrip ad hoc apa pun harus memfilter juga.

`desktop.ini` muncul di dalam `.git/` dan merusak ref. Gejalanya `fatal: bad object
refs/desktop.ini` pada `git log --all`. Perbaikan:

```bash
find .git -iname "desktop.ini" -delete
```

Ini sedang terjadi lagi saat handoff ini ditulis (`.git/logs/refs/desktop.ini` ada). Artefak
Windows, bukan kerusakan repo.

Satu lagi yang bukan bug kode: laptop pernah mati di tengah tuning dan seluruh batch hilang karena
output hanya ditulis di akhir run. Penjaga resume menutupi ini sekarang, tapi run yang terpotong
tetap harus diulang dari nol.

## 8. Yang masih terbuka

**192 CSV di `results/tuning-v2/` tidak tertrack git.** `.gitignore` menutup
`results/tuning/**/*_eval.csv` tapi tidak `tuning-v2`. Aturan user melarang mengubah `.gitignore`,
jadi ini keputusan user, bukan sesuatu untuk diperbaiki sendiri. Yang sudah di-commit: 96 file
JSON metadata, `selection.csv`, dan `run.log`, cukup untuk menurunkan ulang seluruh tabel.

Mode collapse generator tetap jadi keterbatasan yang harus ditulis di paper. Std sintetis sekitar
sepertiga std riil pada kedua upaya. Variabilitas trafik justru yang menekan SLA, jadi arm
`aug_subsample` melatih agen pada beban yang lebih jinak. Kalau arm itu tampak unggul, penjelasan
paling mungkin adalah soal itu, bukan manfaat augmentasi.

Skenario kedatangan dan kepergian slice tidak diimplementasikan. Ia satu-satunya dari tiga skenario
yang bukan transformasi trace; ia butuh masking slice mati di observasi, di aksi, dan di proyeksi
simpleks kapasitas. Dinyatakan sebagai batas ruang lingkup di §9.1, bukan sebagai hasil.

`main.tex:25` (Abstract) dan `:513` (Conclusion) masih memuat 27,3% / 47,6% / 2,71 ms, sementara
Table IV di dokumen yang sama menunjukkan 10,3% / 5,87 ms. File itu milik sesi lain. Hanya
dilaporkan, tidak disentuh.

Testbed fisik sudah dihapus permanen, termasuk seluruh VM, Raspberry Pi, dan sensornya. Tidak ada
pengukuran baru yang mungkin. Yang tersisa adalah trace `rx_mbps` 1.022 baris di
`Reinforcement Learning/revision/dataset_dqn_rich.csv` dan simulator queueing di
`scripts/slice_env.py`. Hubungan aksi ke delay adalah teori queueing, bukan hasil ukur, dan itu
harus dinyatakan di paper.

## 9. Tiga temuan yang menentukan arah paper

**Cacat probe nyata, terukur, dan bukan penyebab PPO gagal.** Seleksi checkpoint putaran 1 memakai
probe 5 episode yang episodenya bergeser tiap kali, dan jumlah probe tidak setara antar metode:
147 untuk PPO, 11 untuk DQN. Gap antara probe yang memilih sebuah checkpoint dan evaluasi penuh
atas bobot yang sama adalah +11,12 poin rata-rata atas seluruh 64 run, rentang +3,60 sampai +16,13.
Setelah diperbaiki, gap itu turun ke +1,98 (rentang -2,30 sampai +6,03) dan probe menjadi 12 untuk
semua metode. Yang dibeli perbaikan itu: DQN naik 1,49 poin dan DDQN 2,82 poin, sementara PPO dan
SDH-PPO praktis tidak bergerak. Jadi cacat seleksi bukan alasan PPO gagal, dan satu hipotesis lagi
tercoret.

`demand_prop` masih tidak terkalahkan. Heuristik satu baris itu 32,37 di val. Learner terbaik
adalah arm residual pada 33,10, dan arm itu diberi `demand_prop` sebagai titik awalnya. Uji BC
memberi 33,03 lawan 32,88, selisih +0,15, yang berarti kelas kebijakannya mampu merepresentasikan
heuristik itu hampir persis. Representasi, observabilitas, parameterisasi aksi, dan bonus entropi
semuanya sudah tercoret sebagai penyebab.

Hipotesis nol "koreksi residual nol" ditolak ke arah yang merugikan. Di evaluasi, kebijakan
residual terpilih menerapkan koreksi rata-rata 0,086 dari batas 0,25, nonzero di 93% langkah, dan
hasilnya 0,73 poin lebih buruk dari heuristik yang ia tumpangi. Agennya bukan diam; ia aktif
menggeser aksi menjauh dari heuristik dan membayarnya. Catatan pembanding yang jujur: aktor
Gaussian belum terlatih dengan `std = 0,607` menghasilkan sekitar 0,12 setelah dikali batas, tidak
jauh dari 0,152 yang terukur di rollout, jadi besaran itu juga konsisten dengan kebijakan yang
nyaris tak terlatih. Dua pembacaan itu dilaporkan di §2.6; memisahkannya butuh uji yang belum
dijalankan.

Dua hipotesis diagnostik lain terbantah dan tetap tercatat terbantah: `tanh` dengan koreksi
Jacobian tidak menolong (pemenang kedua varian PPO tetap `clip`), dan bonus entropi bukan biang
keladinya (pemenang PPO memakai `ent_coef = 0,01`, pemenang SDH-PPO memakai 0).

## 10. Reproducibility

**Environment.** `requirements-v2.txt` (koreksi 2026-10-03: `requirements.txt` di root adalah env
Raspberry Pi testbed, dan versi yang dulu tertulis di sini, torch 2.11.0+cu128 / numpy 2.5.3, salah).
Yang tercatat di `env_versions` seluruh 96 run tuning: Python 3.13.5, torch 2.7.1+cpu (build CPU
saja), numpy 2.3.0, Windows 11. Seluruh run memakai `--device cpu`.

Perintah. Tuning: `bash scripts/run_tuning.sh results/tuning-v2 12 2 300000`. Seleksi:
`python scripts/summarize_tuning.py`. Tabel paper: `python scripts/make_tables.py`. Generator
sintetis: `python scripts/make_synth_trace.py`. Self-check environment:
`python scripts/slice_env.py`. Bukti bahwa port notebook ke CLI setia:
`python scripts/check_fidelity.py`.

Split data. Temporal 60/20/20 atas trace 1.022 baris, tanpa pengacakan, karena datanya deret waktu.
Train 613 baris, val 204. Seluruh statistik (mean `demand_prop`, konstanta normalisasi,
`reward_scale`) diestimasi dari train saja. Test di balik `--allow-test` dan belum pernah disentuh.
Splitnya tidak exchangeable: mean beban naik 21% dari train ke val/test, dan itu wajib dilaporkan,
bukan disembunyikan. Rinci di `07-protocol-v2.md` §1.2.

Pemilihan hyperparameter. Setengah fraksi dari desain 2^4 sehingga setiap efek utama masih dapat
diestimasi dari 8 run. PPO dan variannya memvariasikan lr, `ent_coef`, parameterisasi aksi, dan
`reward_scale`. DQN dan DDQN memvariasikan lr, `target_sync`, `bins`, dan `eps_decay`. Anggaran
identik lintas metode. Pemilihan dilakukan di val, tidak pernah di test. Grid-nya ada di
`scripts/run_tuning.sh` sebagai `PPO_GRID` dan `DQN_GRID`.

Variance. Tuning memakai 2 seed, dan itu tipis: sd mencapai 3,06 pada konfigurasi PPO terpilih.
Sweep final memakai 10 seed dengan Mann-Whitney U, Welch t sebagai pendamping, effect size
rank-biserial, dan CI 95% bootstrap. Angka satu seed tanpa variance tidak dipakai untuk klaim apa
pun; satu kasus di putaran 1 (PPO tampak 48,73 pada n=1, menjadi 51,87 pada n=2) sudah membuktikan
bahayanya.

Compute, termasuk yang dibuang. Putaran final 96 run, 300k step, 12 proses paralel, sekitar 3 jam
wall clock. Yang dibuang dan tetap disimpan: 64 run putaran 1 (diarsipkan karena cacat seleksi),
satu upaya WGAN yang gagal ambang, satu batch tuning yang hilang karena laptop mati, dan seluruh
kampanye V1 100 run yang ditutup karena tiga cacat struktural. Sweep final diperkirakan 21 jam
pada 12 proses.

Keterbatasan. Hubungan aksi ke delay adalah simulasi queueing, bukan hasil ukur; testbed fisiknya
sudah tidak ada. Trace-nya satu realisasi 20 menit dari satu pola trafik, tanpa uji stasioneritas
formal. Generator augmentasi mengalami mode collapse. Skenario slice dinamis tidak
diimplementasikan. Tidak ada metode learning yang mengalahkan heuristik satu baris, bahkan setelah
tuning anggaran setara dan seleksi checkpoint yang diperbaiki.

Ketersediaan. Repo ini publik (`adaptivenetworklab/sdn-iot`). Skrip, protokol, dan metadata per run
di-commit. CSV mentah hasil tuning sebagian tidak tertrack, lihat §8. Direktori `revisi/`
gitignored sehingga draf paper tidak punya git history.
