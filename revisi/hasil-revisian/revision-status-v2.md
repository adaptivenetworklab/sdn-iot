# Status item revisi setelah V2 (2026-10-05)

Audit 34 item `Revision Form ICoICT 2026.xlsx` terhadap `main.tex` saat ini (setelah hasil V2
masuk, commit `2e6b24d` dan sesudahnya). Tidak ada angka hasil di dokumen ini; angka hasil hanya
ada di tabel yang di-`\input` dari `results/analysis-v2`.

Status:
- **Tuntas**: sudah ditangani di `main.tex` dan masih benar untuk V2.
- **Tuntas, form usang**: `main.tex` benar untuk V2, tetapi kolom "Revision" di xlsx masih
  menjelaskan V1 (10 seed, Mann-Whitney, 60.000 step, 21 bin, angka V1) dan harus ditulis ulang.
- **Tuntas, catatan fakta**: item reviewer tertangani, tetapi teks terkait memuat fakta V1 yang
  belum dikoreksi.
- **Menunggu bingkai**: prosa masih `[V2]` atau bagian ditandai `[REWRITE: menunggu bingkai]`.
- **Terbuka / sebagian**: belum atau baru sebagian ditangani.

| Item | Status | Lokasi sekarang | Sisa |
|---|---|---|---|
| A1 hybrid action | Tuntas, form usang | Abstract, §III-B Action Space, §III-D Actor | Akronim "Safe-Driven **Hybrid** PPO" di §I tetap (keputusan penamaan); baris "This work" Table I = REWRITE |
| A2 safety equations | Tuntas | Eq. (17), §III-D-2 | Kuantifikasi kini keluarga (a) di tabel primer; prosa §IV-C `[V2]` |
| A3 Dueling Critic definisi | Tuntas | §III-D Dueling Critic bullet | Hasil kini eksploratif (d) di tabel eksploratif; prosa `[V2]` |
| A4 EO-WGAN | Tuntas | 0 kemunculan di `main.tex` | - |
| A5 state space | Tuntas, catatan fakta | §III-B State Space | Teks menyebut "running z-score"; V2 memakai skala observasi tetap (protokol A5). Belum dikoreksi |
| B1 SLA thresholds | **Sebagian terbuka** | Table II | Format tuntas. Catatan di bawah Table II menyebut ambang = median trace tanpa policing (6.07/71.60/6.90); protokol §8.2 menunjukkan median trace riil tidak mereproduksi ambang P2, yang berasal dari data sintetis V1. Catatan perlu dikoreksi |
| B2 arah klaim | Menunggu bingkai | §IV-B | Prosa `[V2]` |
| B3 port 3 | Tuntas | §III-A-2, Table II | - |
| C1 seed/CI/uji | Tuntas, form usang | §III-E paragraf akhir, Table III, tabel primer/sel | Form masih "10 seeds, Mann-Whitney" |
| C2 baseline statis | Tuntas, form usang | §III-E daftar baseline | Const Max dihapus, Equal Split ditambah; form perlu diperbarui |
| C3 detail DQN/DDQN | Tuntas, form usang | §III-E, Table III | Form masih "21 bins, sync 500" |
| C4 Table III lengkap | Tuntas, form usang | Table III, Table IV | - |
| C5 anggaran step | Tuntas, form usang | Table III, §III-E | Form masih "60,000 steps, episodes of 200" |
| C6 di mana training berjalan | **Sebagian terbuka** | Abstract, §I (T4), §III-E | Reframing ke trace-collection sudah ada, tetapi perangkat dan waktu training (CPU, versi torch, durasi run) belum dinyatakan di paper |
| C7 ablation dan P2 | Menunggu bingkai | §IV-B, §IV-C | Tabel V2 ada; prosa `[V2]` |
| D1 duplikat referensi | Tuntas | References | - |
| D2 Holscher | Tuntas | §II-A | - |
| D3 Zhang | Tuntas | §II-A | - |
| D4 sitasi Arjovsky | Tuntas, catatan fakta | §III-C | Paragraf injeksi noise Gaussian (σ = 0,5) tempat sitasi itu berada tidak ada di pipeline V2 (`make_synth_trace.py`). Belum dikoreksi |
| D5 Mai et al. | Tuntas | b35 | - |
| E1 tabel related work | **Sebagian terbuka** | Table I | Baris "This work" = REWRITE (masih menyebut "ten seeds" dan kesimpulan V1) |
| E2 resolusi gambar | **Sebagian terbuka** | Fig. 3 dan Fig. 4 baru, 300 dpi, dari `scripts/paper_figures_v2.py` | Fig. 1 dan Fig. 2 masih 96 dpi, tanpa sumber vektor di repo; harus digambar ulang penulis |
| X1 cross-reference | Tuntas | seluruh dokumen | Compile tanpa referensi undefined |
| X2 penomoran prioritas | Tuntas | Table II, §III-A-2 | - |
| X3 reward vs klaim | Tuntas, catatan fakta | §III-B-3, Eq. (7)-(8) | Eq. (7) disebut reward "pre-training on the collected dataset"; V2 berlatih online dengan reward Eq. (8) dibagi 19,0106. Belum dikoreksi |
| X4 restrukturisasi §III | Tuntas | §III | - |
| X5 fragmen ganda | Tuntas | §III-C | - |
| X6 sumber ambang | **Sebagian terbuka** | Table II | Sitasi lemah sudah dihapus; catatan asal ambang perlu dikoreksi (lihat B1) |
| X7 drop-cap | Tuntas | §I | - |
| N1 heading ganda | Tuntas | semua heading | Terverifikasi di PDF compile |
| N2 angka hardcoded | Tuntas | Abstract, §V | Angka palsu hilang; prosa hasil `[V2]` |
| N3 evaluator nama-algoritma | Tuntas | §III-E, Eq. (18) | - |
| N4 unit safety | Tuntas | §III-D-2 | - |
| N5 demand_prop dilaporkan | Menunggu bingkai | Abstract/§IV/§V `[V2]`, kontribusi = REWRITE | Kalimat "not beaten by any learned policy" di daftar baseline masih ada (klaim, tidak diubah) |

## Ringkasan (34 item)

- Tuntas: 17 (A2, A3, A4, B3, D1, D2, D3, D5, X1, X2, X4, X5, X7, N1, N2, N3, N4).
- Tuntas, form usang: 6 (A1, C1, C2, C3, C4, C5).
- Tuntas, catatan fakta belum dikoreksi: 3 (A5, D4, X3).
- Menunggu bingkai: 3 (B2, C7, N5).
- Terbuka / sebagian: 5 (B1, X6, C6, E1, E2).

## Di luar 34 item

- `Revision Form ICoICT 2026.xlsx` dan `Compliance Check.xlsx` masih memuat angka hasil V1 dan
  nomor baris lama. Harus ditulis ulang setelah bingkai diputuskan.
- `README.md` folder ini masih menyatakan "Belum di-compile" dan merangkum hasil V1.
- Compliance: blok penulis masih placeholder; panjang paper kini 14 halaman (batas ICoICT perlu
  dicek); jumlah kata abstrak perlu dihitung ulang setelah ditulis.
- `jawaban-reviewer.md` tidak disentuh dan masih menjelaskan V1.
