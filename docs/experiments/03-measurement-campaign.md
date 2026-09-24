# Protokol Kampanye Pengukuran — Sweep Policing Rate

Tanggal: 2026-09-24
Status: siap dijalankan di testbed fisik
Tooling: `pengujian/allport/sweep_policing.sh` (baru) + `pengujian/allport/collect_policy.sh` (sudah ada)

Kampanye ini menjawab blocker di `02-blocker-no-action-variance.md`: tidak ada satu pun
observasi tentang apa yang terjadi pada delay ketika policing rate diubah.

---

## 1. Jalur kontrol dan pengukuran yang sudah ada

Hasil pemetaan kode, agar tidak ada mesin baru yang diciptakan tanpa perlu.

### Kontrol — bagaimana rate di-set

Knobnya adalah **`ovs-vsctl set interface <if> ingress_policing_rate=<kbps>`**.

Penting: **tidak ada satu pun script di repo yang men-set nilai ini.** Aplikasi Ryu
(`flowvisor/deploy_ryu/*.py`, `k8s-deployment/ryudht2.py`) tidak memuat `OFPMeterMod`,
`set_queue`, maupun `ovs-vsctl`. Kolektor hanya **membaca**:

```bash
# collect_policy.sh:101-102
rate=$(sudo ovs-vsctl get interface "$ifname" ingress_policing_rate 2>/dev/null | tr -d '\r')
burst=$(sudo ovs-vsctl get interface "$ifname" ingress_policing_burst 2>/dev/null | tr -d '\r')
```

Inilah sebab mekanis nilai 1.000.000 kbps konstan sepanjang kampanye lama: rate di-set
sekali secara manual, lalu tidak pernah disentuh lagi.

**Konsekuensi desain yang menguntungkan:** karena kolektor sudah membaca rate setiap interval,
driver sweep cukup mengubah rate dari luar — kolektor akan merekamnya sendiri. Tidak perlu
mengubah `collect_policy.sh` sama sekali.

### Pemetaan port

| Slice | Port OVS | Interface | Sumber trafik |
|---|---|---|---|
| P1 | 1 | `dht11` | sensor DHT11 |
| P2 | 2 | `camera` | kamera |
| P4 | 4 | `max` | sensor MAX30102 |

Bridge `br0`. Tidak ada port 3 — konsisten dengan temuan bahwa port 3 tidak pernah ada di
state maupun reward.

### Pengukuran — bagaimana delay dihitung

`pengujian/udp_listener_v2.py:50`:

```python
oneway_delay_ms = (recv_ts - send_ts) * 1000.0
```

Delay **satu arah**, dihitung dari selisih stempel waktu pengirim (Raspberry Pi) dan penerima
(host OVS). Statistik throughput (`rx_mbps`, `pps`, `drop`) berasal dari delta counter
`ovs-ofctl dump-ports` (`collect_policy.sh:41-62`).

Catatan: `collect_policy.sh:75-83` mengambil **sampel terakhir** per device dari 800 baris
terakhir `delay_log.csv`, bukan rata-rata sepanjang interval. Jadi `delay_ms_p*` adalah
snapshot paket terakhir, bukan agregat.

---

## 2. PRASYARAT WAJIB — sinkronisasi waktu

Ini harus dibereskan **sebelum** kampanye dijalankan, atau data baru akan sama tercemarnya
dengan data lama.

Pemeriksaan `pengujian/delay_log.csv` (47.938 baris, tiga format bertumpuk):

| Format | Device | n | mean (ms) | std | min | max |
|---|---|---|---|---|---|---|
| v1 (4 kolom) | camera | 3.654 | 732,554 | 4084,502 | **−1557,091** | 50093,369 |
| v1 | dht11 | 4.566 | 655,993 | 3980,301 | **−3477,017** | 49959,815 |
| v1 | max | 5.363 | 533,771 | 2980,114 | **−253,633** | 49405,773 |
| v2 (6 kolom) | camera | 6.674 | 9,171 | 49,439 | 5,126 | 2467,764 |
| v2 | dht11 | 13.315 | 9,178 | 122,425 | 3,893 | 8628,438 |
| v2 | max | 14.226 | 8,789 | 105,592 | 3,921 | 7206,736 |

**6.321 dari 47.938 pengukuran (13,19%) bernilai NEGATIF.**

Delay satu arah negatif mustahil secara fisika. Yang terukur adalah selisih jam antara dua
mesin, bukan waktu tempuh paket. Pada format v1 skalanya ekstrem (mean ratusan milidetik,
std ribuan) — jam benar-benar melayang. Format v2 jauh lebih stabil, tetapi baseline ~6,5 ms
pada `dataset_dqn_rich.csv` tetap patut dicurigai didominasi **offset jam konstan**, bukan
delay antrean.

Kalau baseline itu memang offset jam, maka sinyal antrean yang sesungguhnya hanya sebagian
kecil dari 6,5 ms, dan seluruh perbandingan terhadap ambang SLA 3,5 / 6 / 7 ms kehilangan
makna.

### Yang harus dilakukan, pilih salah satu

1. **Sinkronkan jam** dengan PTP (`linuxptp`) atau NTP lokal (`chrony`) antara Raspberry Pi
   dan host OVS. Verifikasi offset < 100 µs sebelum mulai. Ini opsi terbaik.
2. **Ganti ke RTT** — pantulkan paket kembali ke pengirim dan ukur pulang-pergi memakai satu
   jam saja. Kebal offset, tetapi mengukur dua arah.

### Verifikasi sebelum merekam

Jalankan listener 5 menit dengan policing rate tidak dibatasi, lalu pastikan:

- **0%** delay negatif;
- delay minimum masuk akal dan stabil (tidak melayang sepanjang jendela);
- delay p50 pada kondisi tanpa beban konsisten antar tiga device.

Kalau salah satu gagal, **jangan lanjut merekam**. Perbaiki sinkronisasi dulu.

---

## 3. Desain sweep

### Grid rate

```
1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 1000000  (kbps)
```

Alasannya: trafik terukur ~3,85 Mbps (P1, P2) dan ~4,57 Mbps (P4). Grid ini menjepit titik
operasi dari **kelaparan** (1 Mbps, jauh di bawah kebutuhan) melewati **pas** (4–5 Mbps)
sampai **tanpa batas** (1 Gbps, kondisi kampanye lama). Tanpa titik di bawah kebutuhan, efek
aksi tidak akan pernah terlihat.

Burst mengikuti rasio lama (10% dari rate), dengan lantai 100 kbps agar rate kecil tetap
dapat mengirim.

### Fase A — sweep satu port (`./sweep_policing.sh single`)

Satu port divariasikan, dua port lain dibiarkan tanpa batas. Mengisolasi **efek langsung**
rate terhadap delay port itu sendiri.

3 interface × 10 titik × 3 pass × 60 s = **90 menit**.

### Fase B — sweep gabungan (`./sweep_policing.sh joint`)

Seluruh port dibatasi bersamaan pada 1000, 2000, 4000, 6000, 10000, 1000000 kbps. Menguji
**kopling antar-slice**: apakah membatasi satu slice memengaruhi slice lain.

6 titik × 3 pass × 60 s = **18 menit**.

Fase B penting secara khusus. Karena `ingress_policing` bekerja per-interface, bisa jadi
**tidak ada kopling sama sekali**. Kalau memang begitu, itu temuan yang harus dilaporkan
jujur, karena seluruh premis "orkestrasi multi-tenant dengan sumber daya bersama" bergantung
pada adanya kopling. Simulator tidak boleh mengarang kopling yang tidak ada di perangkat keras.

### Randomisasi

Urutan kunjungan grid diacak dengan seed tetap (`SEED=42`, berbeda per pass). Tujuannya agar
drift lambat pada testbed — termal, beban latar, drift jam — tidak tertukar sebagai efek rate.
Determinisme sudah diuji: pass yang sama menghasilkan urutan identik, pass berbeda menghasilkan
urutan berbeda, dan seluruh 10 elemen terjaga.

### Settle time

5 detik pertama setelah tiap perubahan dicatat di `sweep_plan.csv` dan **dibuang saat analisis**,
memberi waktu token bucket dan antrean mencapai keadaan tunak.

---

## 4. Cara menjalankan

```bash
# Terminal 1 -- kolektor (tidak berubah dari kampanye lama)
cd pengujian/allport
./collect_policy.sh br0 7200 1 10000

# Terminal 2 -- driver sweep
./sweep_policing.sh single     # Fase A, ~90 menit
./sweep_policing.sh joint      # Fase B, ~18 menit
```

Pastikan generator trafik (sender DHT11, kamera, MAX) berjalan sepanjang kampanye, dan
`udp_listener_v2.py` aktif.

Parameter dapat ditimpa lewat environment: `DWELL`, `REPEATS`, `SETTLE`, `SEED`, `BRIDGE`.

Driver menyimpan rate awal dan **mengembalikannya saat keluar**, termasuk bila diinterupsi
Ctrl-C.

### Catatan `LINK_CAP_Mbps`

`collect_policy.sh` memakai default kapasitas link **10000 Mbps**, sehingga `util_rx_pct`
bernilai sangat kecil (~0,04%) dan praktis tidak informatif. Untuk kampanye ini, isi argumen
keempat dengan kapasitas link yang sebenarnya agar utilisasi bermakna.

---

## 5. Skema keluaran dan penggabungan

Dua file, digabung berdasarkan timestamp:

| File | Skema | Format |
|---|---|---|
| `dataset_dqn_rich.csv` | `timestamp` + 12 metrik × 3 port | `;`-delimited, desimal koma |
| `sweep_plan.csv` | `ts_utc,phase,pass,target_iface,rate_p1_kbps,rate_p2_kbps,rate_p4_kbps` | `,`-delimited |

Keduanya memakai ISO-8601 UTC (`%Y-%m-%dT%H:%M:%SZ`), jadi penggabungan dilakukan dengan
`merge_asof` mundur: tiap baris pengukuran memperoleh setting sweep yang berlaku saat itu.

Sebetulnya `dataset_dqn_rich.csv` sudah memuat `policing_rate_kbps_p*` hasil pembacaan
langsung dari OVS, sehingga penggabungan bersifat **redundan tapi berguna** — `sweep_plan.csv`
memberi label fase, nomor pass, dan port target, yang tidak dapat disimpulkan dari kolom rate
saja.

---

## 6. Pemeriksaan validitas sebelum data dipercaya

Wajib dijalankan atas data hasil kampanye, sebelum dipakai mengkalibrasi apa pun:

1. **Variansi aksi ada.** `policing_rate_kbps_p*` memiliki `nunique >= 10`. Inilah tepatnya
   yang gagal pada kampanye lama.
2. **Nol delay negatif.** Kalau masih ada, sinkronisasi jam belum beres — ulangi.
3. **Monotonisitas.** Delay p50 harus naik seiring turunnya rate, minimal pada rate di bawah
   kebutuhan trafik. Kalau delay datar di seluruh grid, policing tidak berefek pada delay dan
   **premis kontrol paper gugur** — laporkan apa adanya.
4. **Drop muncul pada rate rendah.** Kampanye lama memiliki `drop_* = 0` di seluruh baris. Pada
   rate 1–2 Mbps dengan trafik ~4 Mbps, drop harus bukan-nol. Kalau tetap nol, policing tidak
   benar-benar aktif.
5. **Reprodusibilitas antar-pass.** Tiga pass pada rate sama harus menghasilkan delay p50 yang
   berdekatan. Sebaran lebar menandakan perancu yang belum terkendali.
6. **Kopling (Fase B).** Bandingkan delay P1 saat hanya P1 dibatasi lawan saat semua dibatasi.
   Selisihnya adalah besar kopling — bisa saja nol.

Butir 3 dan 4 bersifat menentukan. Bila keduanya gagal, tidak ada gunanya melanjutkan ke
simulator, dan paper harus di-reframe.

---

## 7. Pemanfaatan untuk simulator

Data kampanye ini memiliki dua peran:

1. **Kalibrasi.** Fit model antrean/token-bucket `delay = f(arrival_rate, policing_rate)` pada
   titik-titik sweep. Menggantikan koefisien karangan `k` pada `d = raw × (1 − k·a)` dengan
   parameter yang diestimasi dari pengukuran.
2. **Validasi.** Sisihkan sebagian titik grid (misal 3000 dan 8000 kbps) dari proses fit,
   lalu laporkan galat prediksi simulator pada titik tersebut. Angka inilah yang membuat
   simulator dapat dipertahankan di hadapan reviewer — galatnya dilaporkan, bukan
   diasumsikan nol.

Pembagian titik hold-out ditetapkan **sebelum** melihat hasil fit, dan dicatat di protokol
Fase 2.
