# Penutupan V1

Tanggal: 2026-09-25
Status: **DITUTUP.** Hasil disimpan, tidak dihapus, **tidak dipakai di paper**.
Artefak: commit `1ab5ceb` (`results/online/`, `results/tables/`), diagnostik `b4567d3`
(`results/diagnostic/`).

V1 adalah sweep 100 run: 10 konfigurasi × 10 seed, simulator antrean `slice_env`, aksi
per-slice 3 dimensi. Angkanya sah sebagai catatan jujur dari satu konfigurasi eksperimen, dan
tetap disimpan utuh untuk jejak audit. Tetapi tiga cacat struktural membuatnya tidak dapat
dipakai mengklaim keunggulan algoritma.

---

## Cacat 1 — Tidak ada split train/eval

**Bukti.** `scripts/train_online.py` (versi commit `1b6345b`) memuat seluruh 1.022 baris trace
lalu memberikan objek yang sama ke environment untuk training maupun evaluasi. `evaluate()`
hanya mengganti seed RNG untuk titik start episode.

Dengan `episode_len=200` pada trace 1.022 baris, start acak jatuh di `[0, 822]`, sehingga
episode training dan evaluasi beririsan besar.

**Dampak.** Seluruh angka V1 bersifat **in-sample**, untuk setiap metode — bukan hanya untuk
heuristik. Tidak ada satu pun bilangan di `results/tables/table_main.tex` yang mengukur
generalisasi.

**Catatan penting.** Kebocoran pada `demand_prop` (mean permintaan dihitung dari seluruh trace)
sempat dicurigai sebagai penyebab kemenangannya. Diperiksa dan **bukan**: dihitung ulang dengan
mean dari 80% awal, hasilnya tak terbedakan secara statistik.

| Varian | Total Viol % [CI 95%] |
|---|---|
| mean FULL | 16,10 [14,79, 17,33] |
| mean TRAIN | 16,04 [14,74, 17,26] |

Mann-Whitney U **p = 0,7337**. Jadi cacat ini nyata, tetapi tidak menjelaskan hasil.

---

## Cacat 2 — Tidak satu pun metode learning konvergen

**Bukti.** `results/diagnostic/convergence_flatness.csv`. Uji kedataran: perubahan kuartal
terakhir terhadap kuartal pertama, sebagai fraksi rentang tiap kurva; ambang konvergen
`|Δ| < 0,10`.

| Metode | Metrik | Δ (fraksi rentang) | Konvergen |
|---|---|---|---|
| PPO | mean_reward | **+0,5199** | TIDAK |
| SDH-PPO | mean_reward | **+0,2017** | TIDAK |
| SDH-PPO | loss_critic | **−0,1563** | TIDAK |
| DDQN | loss | **+0,1067** | TIDAK |
| PPO | loss_critic | −0,0155 | ya |
| DQN | loss | +0,0739 | ya |

Reward PPO masih bergerak 52% rentangnya pada kuartal terakhir — dihentikan jauh di tengah
proses belajar. `loss_critic` SDH-PPO berakhir di kisaran 56.000–120.000.

**Sebab.** Reward −10 sampai −30 per langkah tanpa normalisasi; return berdiskonto sepanjang
200 langkah menghasilkan target value berorde ribuan. Anggaran `--steps 60000` dengan
`--rollout 2048` hanya memberi PPO **30 update rollout**.

**Dampak.** Perbandingan V1 adalah antara empat agen yang belum konvergen dan sebagian divergen.
Ranking belum tentu stabil dengan anggaran training memadai.

---

## Cacat 3 — Safety layer hanya diberikan ke Proposed

**Bukti.** `train_online.py` V1 menetapkan
`use_mask = args.algo == "sdhppo" and args.arm != "no_mask"`. Hanya metode yang diusulkan yang
memperoleh lapisan itu; PPO, DQN, dan DDQN tidak.

Ablation V1 mengukur kontribusinya:

| Arm | Total Viol % | p (Holm) |
|---|---|---|
| Proposed | 28,25 | — |
| Proposed tanpa safety layer | 50,11 | 0,000365 |
| Proposed tanpa dueling critic | 27,81 | 0,970 |

Safety layer menyumbang **22 poin** — kontributor tunggal terbesar. Dueling critic menyumbang
nol.

**Dampak.** Sebagian besar keunggulan Proposed atas PPO kemungkinan adalah keunggulan "punya
safety layer" lawan "tidak punya", bukan keunggulan algoritma. Secara struktural ini pola yang
sama dengan koefisien 0,15 lawan 0,10 pada notebook lama: satu komponen menguntungkan yang
hanya diberikan kepada metode yang diusulkan.

---

## Cacat tambahan yang tercatat saat diagnostik

- **`const_max` identik dengan `no_control`.** Aksi bersifat multiplikatif relatif lalu
  diproyeksikan ke simpleks kapasitas, sehingga aksi seragam adalah no-op. Ruang aksi efektif
  punya 2 derajat kebebasan, bukan 3. Tabel V1 memuat dua baris yang secara struktural identik.
- **Trace tidak stasioner.** Split 60/20/20 menunjukkan beban train 11,38 Mbps lawan val 13,79
  dan test 13,46 — naik 21%. V1 tidak menyadari ini karena tidak memakai split.

---

## Yang tetap berlaku dari V1

- `slice_env` beserta self-check enam propertinya.
- Temuan bahwa heuristik sederhana `demand_prop` mengungguli Proposed dengan selisih besar.
  Ini bertahan lintas seluruh cacat di atas dan tetap menjadi tantangan utama bagi klaim paper.
- Seluruh perkakas: `train_online.py`, `make_tables.py`, `plot_convergence.py`.

## Status arsip

`results/online/` dan `results/tables/` **tidak dihapus**. Hash `per_seed_summary.csv`
terverifikasi tidak berubah sepanjang sesi diagnostik. Setiap rujukan ke angka V1 dalam dokumen
mana pun harus menyebutkan status penutupan ini.

Lanjutannya ada di `07-protocol-v2.md`.
