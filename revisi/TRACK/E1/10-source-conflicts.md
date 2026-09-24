# Audit konflik sumber — E1 Related Work (Sumber1.md vs Sumber2.md)

Dibuat setelah T2 (tabel) + T1 (bib) jadi, mengikuti urutan kerja yang direvisi: cuma 11 key yang benar-benar kepake di `related-work-table.md` yang diverifikasi web, plus 5 item yang di-flag eksplisit. Semua 11 key **berhasil diverifikasi** (paper riil, bukan halusinasi) — lihat catatan `VERIFIED`/`CORRECTION` di tiap entry `references-new.bib`.

## 1. TODO-VERIFY yang masih tersisa (diurutkan dari yang paling sering disitasi)

| Key | Field | Kenapa masih TODO | Prioritas |
|---|---|---|---|
| `rsppo2026` | `author` | Web search nemuin venue (Telecom MDPI vol.7 no.3 p.75, 2026) tapi nama penulis gak muncul di hasil pencarian | Sedang — dipakai 1x di tabel |
| `nagib2025safeslice` | `doi` | Venue (ICMLCN 2025) + arXiv ID (2503.12753) ketemu, DOI resmi publikasi belum | Sedang — dipakai di tabel + T3 |
| `alchaab2025lsrlslice` | `doi` | IEEE Xplore document ID ketemu (11026997) tapi DOI string belum diekstrak | Rendah |
| `tarkh2026rlloop` | `doi` | Belum ketemu, masih arXiv-only reference | Rendah |
| `bai2024reach` | `doi` | Masih arXiv preprint (2510.06675), belum ada DOI conference/journal resmi | Rendah — dipakai di tabel + T4 |
| `liu2021constrained` | `doi` | IEEE Xplore document ID ketemu (9472202), DOI string belum diekstrak | Rendah |
| `raftopoulos2024` | `doi`, nama lengkap co-author ke-3/4 | arXiv 2401.05042 + IEEE Xplore 10556357 ketemu, tapi daftar penulis lengkap (4 orang, cuma 2 ketemu: Raftopoulos, D'Oro) belum lengkap | Rendah |

Entry di kerangka bibtex awal yang **TIDAK dipakai** di tabel (Raftopoulos versi dari Sumber1's "Testbed Fisik" list yang beda dari yang di tabel Related Work, plus semua entry Kelompok 3/4/6/7/8 yang gak lolos ke 11 baris) **dihapus** dari `references-new.bib`, sesuai instruksi ("Entri yang tidak terpakai jangan disimpan sebagai TODO-VERIFY — hapus saja").

## 2. Konflik metadata Sumber1.md vs Sumber2.md (dan konflik internal Sumber2.md sendiri)

| # | Konflik | Sumber A bilang | Sumber B bilang | Resolusi |
|---|---|---|---|---|
| 1 | Penulis AL-SAC | Sumber2.md tabel pertama (baris "Qi dkk. (2022)") | Sumber2.md bagian detail ("Paper 1: ...(Qiang Liu et al., MDPI Electronics, 2022)") | **Konflik internal Sumber2.md sendiri**, bukan antar-file. **RESOLVED via web search**: penulis asli = Qi, Lin, Guo, Chen, Deng, Lin, Sun, Chen — "Qi dkk." BENAR, "Qiang Liu et al." adalah kekeliruan (ketuker sama penulis OnSlicing, orang berbeda meski nama depan sama "Qiang"/"Qi"). |
| 2 | Tahun Liu-Ding-Liu (constrained RL) | Sumber2.md tabel pertama: "Liu, Ding, & Liu (2020)" | Sumber2.md bagian detail: "Constrained RL for Network Slicing (Liu, Ding, & Liu, 2021)" | **Konflik internal Sumber2.md sendiri**. **RESOLVED via web search**: venue = IEEE ICNP, tahun = **2020** benar. |
| 3 | Venue "AI Methods in Network Slice Life-Cycle Phases: A Survey" | Sumber2.md bagian 4 (kutipan simulasi): "(MDPI, 2025)" | Sumber2.md bagian keterbatasan simulasi: "(MDPI, 2024)" | **Konflik internal Sumber2.md sendiri**. **RESOLVED tanpa web search** — paper ini sudah jadi referensi `b3` di `main.tex` (dari sesi revisi sebelumnya) dengan metadata lengkap terverifikasi: *E. Thomatos, A. Sgora, A. Tsipis, P. Chatzimisios, "AI Methods in Network Slice Life-Cycle Phases: A Survey," Oct. 2025, MDPI, DOI 10.3390/electronics14204053.* **2025 benar.** |
| 4 | Bertrand 2020 (Zenodo) vs Bertrand 2025 (IEEE) — paper sama atau beda? | Sumber2.md tabel pertama baris "Real-time Dynamic Network Slicing... (Zenodo, 2020)": 2x Raspberry Pi sbg UE, USRP B210, FlexRAN | Sumber2.md tabel kedua baris "SDN-Based Slicing Testbed for 5G Networks (IEEE, 2025)": Proxmox VE, Open5GS, OpenDaylight, OVS | **Kemungkinan besar 2 paper BEDA** oleh grup riset yang sama (Pablo Bertrand), bukan duplikat — arsitektur/hardware yang dideskripsikan jelas berbeda (fronthaul testbed vs Proxmox virtualized testbed). Web search konfirmasi paper 2025 penulis "Pablo Bertrand" + IEEE Xplore doc 11185773, tapi **tidak berhasil mengkonfirmasi daftar penulis lengkap paper 2020** untuk memastikan ini bukan orang berbeda dengan nama sama. **Belum 100% resolved** — kedua entry TIDAK dimasukkan ke `references-new.bib` (gak kepake di 11 baris tabel), jadi risiko sitasi-ganda saat ini nihil; kalau nanti dipakai, verifikasi ulang daftar penulis paper 2020 dulu. |
| 5 | `rakshit2025rekeying` — resiko halusinasi tertinggi (diminta cek prioritas) | Testbed: ESP32-DevKitC v4 + DHT11 + Raspberry Pi 5 16GB, >6.500 paket, Dockerized Mosquitto MQTT | — | **VERIFIED REAL**, bukan halusinasi. arXiv 2511.02924 (Nov 2025), penulis Haranath Rakshit, judul "Lightweight Session-Key Rekeying Framework for Secure IoT–Edge Communication". Setup hardware persis seperti dideskripsikan, bahkan ada dataset pendamping di IEEE DataPort ("PSK Baseline Encrypted–Decrypted IoT–Edge Communication Dataset (ESP32 + DHT11 → Raspberry Pi 5 over MQTT)"). **Catatan**: paper ini TIDAK dimasukkan ke 11 baris tabel Related Work (domain keamanan sesi-key, bukan orkestrasi DRL) — cuma relevan sebagai justifikasi kelas hardware testbed (Raspberry Pi 5), bisa disitasi di paragraf motivasi testbed kalau perlu contoh tambahan. |

## 3. Paper yang muncul di kedua file dengan nama/atribusi berbeda (risiko sitasi ganda)

| Paper | Nama di Sumber1.md | Nama di Sumber2.md | Key yang dipakai |
|---|---|---|---|
| OnSlicing | "Qiang Liu, Nakjung Choi, Tao Han (2021)" | "Qiang Liu, Nakjung Choi, Tao Han, 2021" (tabel kedua) | `liu2021onslicing` — konsisten, gak ada risiko |
| SafeSlice | tidak muncul di Sumber1.md | "Nagib dkk. (2025)" / "Ahmad Nagib et al." (beda ejaan minor, sama orang) | `nagib2025safeslice` — konsisten |
| REACH | "Xu Bai, Adel N. Toosi, Rajkumar Buyya, Muhammed Tawfiqul Islam (2024)" | "Xu Bai, Adel N. Toosi, Rajkumar Buyya, Muhammed Tawfiqul Islam, 2024" — urutan nama sama, **tahun sama-sama salah (2024)** di kedua sumber | `bai2024reach` — **tahun asli 2025** (arXiv Oct 2025), dikoreksi di bib meski key masih pakai "2024" (key cuma identifier, gak diubah biar gak pecah referensi lain) |
| ChainsFormer | "Chenghao Song, Minxian Xu, Kejiang Ye, Huaming Wu, dkk. (2024)" | "Chenghao Song, Minxian Xu, Kejiang Ye, Huaming Wu, dkk., 2024" | `song2024chainsformer` — **tahun asli 2023** (ICSOC 2023), dikoreksi di bib, key tetap "2024" |
| LS-RLSlice | "Adhwaa Alchaab, Ayman Younis, Dario Pompili (2025)" | sama | `alchaab2025lsrlslice` — konsisten, cuma judul aslinya ada prefix "Slice-on-the-Fly:" yang di-drop di kedua sumber |

## 4. Entry paling berisiko halusinasi NotebookLM (judul sangat spesifik, penulis tidak disebut)

Dicek semua entry yang dipakai di tabel — **tidak ada yang terbukti halusinasi**. Yang paling mencurigakan di awal (`rakshit2025rekeying`, karena hardware setup-nya mirip banget sama testbed kita) sudah diverifikasi REAL (lihat poin 2.5 di atas).

Entry lain yang PERNAH terlihat berisiko (judul spesifik + penulis minim) tapi **tidak masuk 11 baris tabel** sehingga tidak diverifikasi lebih lanjut sesi ini:
- `rsppo2026` — penulis sama sekali gak disebut di Sumber1/2.md ("Penulis Jurnal MDPI Telecom (2026)"), tapi venue+DOI-page sudah terverifikasi real via web search, jadi bukan halusinasi — cuma metadata penulis yang kurang.
- Entry-entry di Kelompok 6 kerangka awal (testbed SBC) yang tidak dipakai di tabel — belum diverifikasi, tidak direkomendasikan disitasi tanpa verifikasi tambahan kalau nanti dipakai.
