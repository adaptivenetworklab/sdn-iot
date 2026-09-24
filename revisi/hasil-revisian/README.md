# Hasil Revisian — SDH-PPO Paper

Output revisi terhadap `revisi/paper/main.tex`, mengacu ke `revisi/TRACK/revision-map.md`
dan `docs/experiments/00-contamination-audit.md`.

## Isi folder

| File | Keterangan |
|---|---|
| `main.tex` | Paper hasil revisi. Semua bagian yang direvisi **disorot kuning**. |
| `Compliance Check.xlsx` | Format sama dengan `TRACK/Compliance Check.xlsx`, isi disesuaikan paper ini. |
| `Revision Form ICoICT 2026.xlsx` | Format sama dengan template ICoICT, 34 item revisi + lokasi barisnya. |
| `main.pdf` | Hasil compile, 13 halaman. Untuk mengecek cepat tanpa compile sendiri. |
| `figures/` | `fig1`–`fig3` disalin apa adanya; `fig4_seed_distribution.png` **baru**, 300 dpi. |
| `IEEEtran.cls` | Disalin supaya folder ini bisa di-compile berdiri sendiri. |

## Cara compile

```bash
pdflatex main.tex && pdflatex main.tex     # 2x supaya \ref dan nomor tabel benar
```

**Sudah diverifikasi compile.** pdfLaTeX (TeX Live 2026), 2 pass:
**13 halaman, 0 error, 0 referensi menggantung, overfull terburuk 5pt.**
Hasilnya ada di `main.pdf` di folder ini sebagai pembanding.

Paket yang dipakai: `cite`, `amsmath`, `graphicx`, `textcomp`, `xcolor[table]`,
`booktabs`, `soul` — semua ada di TeX Live / Overleaf standar.

## Konvensi sorotan kuning

- `\rev{...}` — teks berjalan yang baru atau diubah (74 span).
- Baris header tabel berwarna kuning — menandai tabel yang **baru sepenuhnya**.

**Aturan wajib kalau menambah sorotan baru.** `soul` (mesin di balik `\hl`) tidak bisa
memproses sembarang isi. Dua hal ini menggagalkan compile atau merusak output:

| Jangan | Pakai |
|---|---|
| `\rev{... \ref{tab:1} ...}` | `\rev{... \mbox{\ref{tab:1}} ...}` |
| `\rev{... $\tau_p$ ...}` | `\rev{... \mbox{$\tau_p$} ...}` |

`\ref` telanjang di dalam sorotan membuat compile **berhenti total**
(`Missing \endcsname inserted`). Math telanjang menghasilkan `Missing $ inserted` dan
render yang salah. `\cite`, `\emph`, `\textbf`, `\textit` aman karena sudah
didaftarkan lewat `\soulregister{...}{1}` di preamble — perhatikan argumennya `1`,
bukan `0`; `0` juga menggagalkan compile.

**Teks yang hanya dipindah posisi (restrukturisasi Section III, item X4) sengaja TIDAK
disorot.** Kalau ikut disorot, sekitar 60% Section III jadi kuning dan sorotannya kehilangan
guna. Yang kuning = benar-benar berubah isinya.

### Untuk camera-ready

Ganti satu baris di preamble, sorotan hilang, isi tetap:

```latex
\renewcommand{\rev}[1]{#1}
```

## Perubahan paling berdampak

Angka hasil **diganti total**, bukan diselaraskan. Dasarnya `00-contamination-audit.md`:

1. Angka Abstract & Kesimpulan lama (27.3%, 47.6%, 2.71 ms) berasal dari
   `np.random.uniform()` yang di-hardcode, bukan dari model yang dilatih.
2. Table IV lama (10.3%) dihitung evaluator yang memilih koefisien per-port dengan
   mencocokkan **nama algoritma** — baris `'Proposed (SDH-PPO)'` dapat 0.15, semua
   baseline dapat 0.10. Audit melarang menyalin angka ini ke Abstract.

Penggantinya: `results/` — simulator antrean kapasitas bersama, 10 seed, bootstrap 95% CI,
Mann-Whitney + koreksi Holm, plus ablation. Ini sekaligus menutup item **C1** dan **C7**.

Konsekuensi yang harus disadari sebelum submit:

- SDH-PPO **menang** atas semua baseline yang dilatih (28.25% vs PPO 48.19%, DQN 51.13%,
  DDQN 47.26%), p = 0.0013, separasi penuh antar seed.
- SDH-PPO **kalah** dari heuristik demand-proportional (16.10%), p sama, separasi penuh ke
  arah sebaliknya. Ini dilaporkan di Abstract, kontribusi, hasil, dan kesimpulan.
- Safety layer terbukti nyata: −21.9 poin persen kalau dicabut (p = 0.0004).
- Dueling critic **nihil** (p = 0.97). Dilaporkan sebagai null result, tidak ada klaim
  performa untuknya.

## Status item revision-map

29 item ter-map + 5 temuan baru = 34 item, semua masuk `Revision Form`.

**Satu item belum tuntas — E2 (resolusi gambar).** Fig. 4–8 lama sudah dibuang dan Fig. 4
baru dibuat 300 dpi. Tapi Fig. 1, 2, 3 masih 96 dpi dan **tidak ada sumber vektor atau
resolusi lebih tinggi di repo** (sudah dicari: tidak ada `.svg`, `.drawio`, atau PDF
figure). Jadi:

- **Fig. 1 & 2** — diagram arsitektur, harus digambar ulang oleh penulis lalu ekspor PDF/SVG.
- **Fig. 3** — t-SNE, bisa di-ekspor ulang dari `Reinforcement Learning/revision/DataAugmentation.ipynb`
  dengan `savefig(..., dpi=300)`.

## Yang masih perlu keputusan penulis

- **Identitas** — blok `\author` masih placeholder IEEE, dan Paper ID / Authors / Editor
  di kedua xlsx sengaja dikosongkan sesuai permintaan.
- **Kolom `Page` di Revision Form** diisi `-`. Nomor halaman baru bisa ditentukan setelah
  compile; kolom `Paragraph/Line number` sudah presisi ke nomor baris `main.tex`.
- **Panjang paper.** Versi ini **13 halaman** (draft lama 12). ICoICT umumnya membatasi
  6 halaman, jadi pemangkasan hampir pasti perlu. Section II paling longgar.
- **Akronim SDH-PPO.** Huruf "H" berasal dari "Hybrid", padahal klaim hybrid sudah
  diturunkan. Penamaan dibiarkan apa adanya sesuai keputusan sebelumnya di revision-map.
