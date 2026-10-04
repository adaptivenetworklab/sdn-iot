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
| A5 state space | Tuntas | §III-B State Space | Dikoreksi 2026-10-05: skala observasi tetap (arrival/10 Mbps, utilisasi/2, delay/τ_p, rate/C; `train_online.py:68-83`); z-score (9) kini hanya untuk jendela latih generator. Sisa fakta: kalimat yang sama masih menyebut fitur state "measuring ... one-way delay", padahal di V2 delay adalah delay antrean simulator |
| B1 SLA thresholds | Tuntas | Table II dan catatannya | Dikoreksi 2026-10-05: ambang = parameter desain simulator; median riil-train per port; ambang P2 = median dataset sintetis V1; rujukan ke analisis sensitivitas (`[V2]`, tempatnya menunggu bingkai) |
| B2 arah klaim | Menunggu bingkai | §IV-B | Prosa `[V2]` |
| B3 port 3 | Tuntas | §III-A-2, Table II | - |
| C1 seed/CI/uji | Tuntas, form usang | §III-E paragraf akhir, Table III, tabel primer/sel | Form masih "10 seeds, Mann-Whitney" |
| C2 baseline statis | Tuntas, form usang | §III-E daftar baseline | Const Max dihapus, Equal Split ditambah; form perlu diperbarui |
| C3 detail DQN/DDQN | Tuntas, form usang | §III-E, Table III | Form masih "21 bins, sync 500" |
| C4 Table III lengkap | Tuntas, form usang | Table III, Table IV | - |
| C5 anggaran step | Tuntas, form usang | Table III, §III-E | Form masih "60,000 steps, episodes of 200" |
| C6 di mana training berjalan | Tuntas | §III-E paragraf perangkat | Dikoreksi 2026-10-05: CPU, model, RAM, versi perangkat lunak, waktu komputasi sweep |
| C7 ablation dan P2 | Menunggu bingkai | §IV-B, §IV-C | Tabel V2 ada; prosa `[V2]` |
| D1 duplikat referensi | Tuntas | References | - |
| D2 Holscher | Tuntas | §II-A | - |
| D3 Zhang | Tuntas | §II-A | - |
| D4 sitasi Arjovsky | Tuntas | §III-C paragraf 1 | Dikoreksi 2026-10-05: paragraf dan persamaan injeksi noise dihapus; diganti deskripsi pipeline V2 (`make_synth_trace.py`), Arjovsky dikutip untuk formulasi WGAN |
| D5 Mai et al. | Tuntas | b35 | - |
| E1 tabel related work | **Sebagian terbuka** | Table I | Baris "This work" = REWRITE (masih menyebut "ten seeds" dan kesimpulan V1) |
| E2 resolusi gambar | **Sebagian terbuka** | Fig. 3 dan Fig. 4 baru, 300 dpi, dari `scripts/paper_figures_v2.py` | Fig. 1 dan Fig. 2 masih 96 dpi, tanpa sumber vektor di repo; harus digambar ulang penulis |
| X1 cross-reference | Tuntas | seluruh dokumen | Compile tanpa referensi undefined |
| X2 penomoran prioritas | Tuntas | Table II, §III-A-2 | - |
| X3 reward vs klaim | Tuntas | §III-B-3, Eq. (7)-(8) | Dikoreksi 2026-10-05: (7) dinyatakan reward formulasi offline lama yang tidak dipakai; agen dilatih online dengan (8) dibagi reward scale (`slice_env.py:237-247`) |
| X4 restrukturisasi §III | Tuntas | §III | - |
| X5 fragmen ganda | Tuntas | §III-C | - |
| X6 sumber ambang | Tuntas | Table II | Lihat B1 |
| X7 drop-cap | Tuntas | §I | - |
| N1 heading ganda | Tuntas | semua heading | Terverifikasi di PDF compile |
| N2 angka hardcoded | Tuntas | Abstract, §V | Angka palsu hilang; prosa hasil `[V2]` |
| N3 evaluator nama-algoritma | Tuntas | §III-E, Eq. (18) | - |
| N4 unit safety | Tuntas | §III-D-2 | - |
| N5 demand_prop dilaporkan | Menunggu bingkai | Abstract/§IV/§V `[V2]`, kontribusi = REWRITE | Kalimat "not beaten by any learned policy" di daftar baseline masih ada (klaim, tidak diubah) |

## Ringkasan (34 item, diperbarui 2026-10-05)

- Tuntas: 23 (A2, A3, A4, A5, B1, B3, C6, D1, D2, D3, D4, D5, X1, X2, X3, X4, X5, X6, X7, N1, N2, N3, N4).
- Tuntas, form usang: 6 (A1, C1, C2, C3, C4, C5).
- Menunggu bingkai: 3 (B2, C7, N5).
- Terbuka / sebagian: 2 (E1 baris "This work", E2 Fig. 1-2).

## Di luar 34 item

- `Revision Form ICoICT 2026.xlsx` dan `Compliance Check.xlsx` masih memuat angka hasil V1 dan
  nomor baris lama; dipindah utuh ke `obsolete-v1/` (2026-10-05). Harus ditulis ulang setelah bingkai
  diputuskan.
- `README.md` folder ini merangkum hasil V1; diberi banner OBSOLETE (2026-10-05), isi lain tidak diubah.
- Compliance: blok penulis masih placeholder; panjang paper kini 14 halaman (batas ICoICT perlu
  dicek); jumlah kata abstrak perlu dihitung ulang setelah ditulis.
- `jawaban-reviewer.md` tidak disentuh dan masih menjelaskan V1.

## Inventaris Fig. 1 dan Fig. 2 (belum digambar ulang)

**Fig. 1 (`fig1_architecture.png`, 495x929 px, 96 dpi): arsitektur testbed.** Dari atas:
Monitoring (logo Grafana, "Ubuntu 20.04"), "Internal Network", Database (ikon); tiga panah
"Bridge" ke tiga kontainer "Controller Smart City", "Controller Healthcare", "Controller Smart
Building" (logo Ryu dan Kubernetes, "Ubuntu 20.04"); "FlowVisor" ("Ubuntu 14"); "OVS / Open
vSwitch" ("Ubuntu 20.04") dengan tiga port berlabel "camera", "max", "dht11"; "RaspberryPi 5" dengan
"GPIO"; "Camera Module Port", dua "Jumper"; sensor: SMART CITY (Person Detection, WAVESHARE),
HEALTH CARE (MAX30102, ALERT), SMART BUILDING (Client web, DHT11).
Bertentangan dengan V2: tidak ada label hybrid, dueling, EO-WGAN, atau pre-training. Gambar ini
hanya menggambarkan testbed pengumpul trace, konsisten dengan V2. Catatan: gambar menunjukkan
**satu** Raspberry Pi 5, sedangkan §III-A menulis "Each sector utilizes a Raspberry Pi gateway";
tidak ada agen RL di gambar ini.

**Fig. 2 (`fig2_framework.png`, 732x341 px, 96 dpi): "SDH-PPO framework".** Label: "Proposed
Framework", "PPO Update Engine", "Experience Relay Buffer" (sic), "Sampled Trajectories
(s, a, r, s')", "reward signal (r)", "Processing Layer", "Critic Network (V_φ)", "Actor Network
(π_θ)", "Predicted Value (V_t)", "Store Action", "Gradient Update (∇θ)", "State Observations
(s)", "Environment".
Bertentangan atau tidak lengkap terhadap V2:
- **Tidak ada safety-margin correction**: aksi aktor langsung ke Environment, padahal V2 menerapkan
  koreksi (17) sebelum `env.step` dan menjadikannya faktor on/off.
- **"Experience Relay Buffer" dengan transisi (s, a, r, s')** terbaca sebagai replay buffer
  off-policy. PPO V2 on-policy dengan rollout 2.048 step.
- Critic tidak digambarkan dengan dua head (value dan advantage-residual); nama "dueling" tidak ada.
- Tidak ada WGAN-GP atau jalur data sintetis; tidak ada varian residual atau BC init.
- Environment tidak ditandai sebagai simulator antrean berbasis trace.
- Tidak ada label hybrid, EO-WGAN, atau pre-training offline.

## Batas halaman ICoICT

Tidak ditemukan dokumen submission yang menyebut batas halaman di repo. Yang ada hanya
`revisi/conference-latex-template.zip` (template IEEE generik, teksnya: "Please observe the
conference page limits") dan form revisi. Angka "6 halaman" di `README.md` dan
`jawaban-reviewer.md` ditulis sebagai perkiraan ("umumnya"), bukan kutipan sumber. Batas resmi
harus dicek di CFP atau email panitia.
