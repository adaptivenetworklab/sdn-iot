Tentu, berikut adalah tabel ekstraksi informasi terstruktur untuk bagian *Related Work* / *Research Gap*, yang disusun dan diurutkan berdasarkan tingkat relevansinya dengan **orkestrasi resource SDN-IoT berbasis DRL** (dimulai dari yang paling relevan mengintegrasikan SDN, IoT, DRL, dan slicing/orkestrasi):

| Penulis (tahun) | Pendekatan/algoritma | Action space (diskret/kontinu/hybrid) | Lingkungan evaluasi (simulasi/testbed fisik) | Kelebihan utama | Keterbatasan yang diakui penulis sendiri | Keterbatasan yang terlihat dari luar |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Penulis EASE-6G (2026)** | Hybrid Deep Learning & DRL (LSTM untuk prediksi trafik + Signaling-aware Deep Q-Network [DQN] dengan *Proactive Flow Installation*) | Diskret | Simulasi (OMNeT++ v6.0 dengan Simu5G library dan Ryu SDN controller) | Mengurangi konsumsi energi *control plane* sebesar 36,8%, *signaling overhead* sebesar 36,7%, dan latensi sebesar 35,6% pada skala 6G-IoT terdensifikasi (hingga \\(10^6\\) perangkat/km²). | Simulasi OMNeT++/Simu5G tidak memodelkan secara eksplisit *imperfect Channel State Information* (CSI) atau interferensi mmWave terlokalisasi. Penulis mencatat *future work* mencakup: (1) *federated learning* untuk kerahasiaan *edge-slice*; (2) evaluasi pada *testbed* fisik O-RAN; dan (3) *stress-testing* konfigurasi aturan proaktif terhadap *overhead* kriptografi tahan-kuantum. | Evaluasi masih berbasis *discrete-event simulator* (OMNeT++/Simu5G) dan belum divalidasi pada *testbed* perangkat keras fisik. |
| **Qiang Liu, Nakjung Choi, Tao Han (2021)** *(OnSlicing)* | Individualized DRL per *slice* dengan *constraint-aware policy update*, *proactive baseline switching*, *action modification*, dan *parameter coordination* (dilengkapi *offline imitation learning* dari solusi berbasis aturan) | Hybrid (kombinasi variabel *uplink/downlink radio bandwidth*, *MCS offset*, algoritma penjadwalan, *transport bandwidth*, *reserved path*, serta alokasi CPU & RAM) | Testbed fisik (*Testbed E2E* berbasis OpenAirInterface 4G LTE/5G NR, platform SDN OpenDayLight, dan core OpenAir-CN) | Mencapai alokasi sumber daya lintas-domain minimal dengan *SLA violation* hampir nol (0,06%) selama fase *online learning*, serta mengurangi penggunaan sumber daya hingga 61,3% dibanding solusi berbasis aturan dan 12,5% dibanding SOTA *online* DRL. | Ketika disebarkan pada jaringan skala besar, potensi tantangan dapat muncul saat *state space* diperluas menjadi sangat besar dan *action space* bersifat heterogen dalam hal *enforcement delay*, sehingga pengumpulan *state* dapat menambah beban trafik jaringan transpor; selain itu sistem dievaluasi pada *testbed* skala kecil. | Kualitas saluran radio dijaga konstan selama emulasi untuk menjaga stabilitas platform emulasi. |
| **Adhwaa Alchaab, Ayman Younis, Dario Pompili (2025)** *(LS-RLSlice)* | Dual-time-scale Actor-Critic DRL (LS-RLSlice) memisahkan LTRA (*Long-Term Resource Allocation* berbasis LSTM sebagai rApp) dan STRS (*Short-Term Resource Scheduling* berbasis DDPG sebagai xApp) | Kontinu | Testbed fisik (POWDER *testbed* dengan OpenAirInterface 5G, *stack* OSC O-RAN, Docker, Kubernetes) | Berhasil mendekopling tugas alokasi jangka panjang dan jangka pendek di Non-RT dan Near-RT RIC untuk mengoptimalkan penggunaan *resource block* (RB) dan menjamin QoS O-RAN di bawah dinamika trafik heterogen. | tidak disebutkan | Fokus utama berada pada lapisan RAN/RIC O-RAN tanpa mengintegrasikan manajemen antrean mikroservis di lapisan aplikasi *edge*. |
| **Penulis Jurnal MDPI Telecom (2026)** *(RS-PPO mmWave-PON)* | Reward-Shaped Proximal Policy Optimization (RS-PPO) yang dilengkapi *Graph Convolutional Network* (GCN) *state abstraction*, *action masking*, dan *prioritized N-step replay* | Hybrid (keputusan alokasi *Dynamic Bandwidth Allocation* [DBA] pada PON dan PRB pada mmWave RAN) | Simulasi (Simulasi berstandar 3GPP untuk *mmWave channel* dan dinamika GPON DBA) | Memecahkan kebuntuan koordinasi terpisah antara PON *fronthaul* dan mmWave RAN, mengurangi latensi *E2E* URLLC sebesar 37% (menjadi 0,87 ms) dan meningkatkan utilisasi PRB sebesar 28% dengan inferensi sub-5 ms. | Pekerjaan masa depan akan memperluas kerangka kerja ke topologi *multi-PON*, mengeksplorasi *meta-learning* untuk campuran *slice* non-stasioner, dan mengimplementasikan inferensi sub-milisepeda berbasis FPGA. | Eksperimen dilakukan pada simulasi topologi *single-PON* dan belum divalidasi pada perangkat keras fisik O-RAN/PON nyata. |
| **Penulis arXiv:2604.02461 (2026)** *(RL-Loop)* | *Closed-loop feedback controller* berbasis PPO (*Proximal Policy Optimization*) yang menyesuaikan alokasi CPU fungsi *slice* 5G secara *real-time* berdasarkan pengukuran KPI langsung | Diskret | Testbed fisik (*Testbed* 5G terintegrasi Open5GS + UERANSIM) | Beroperasi secara stabil pada *testbed* 5G fisik dan mampu mengoperasikan fungsi *slice* dengan alokasi rata-rata CPU lebih dari 50% lebih rendah dibanding titik operasi acuan (MicroOpt). | Lingkungan *testbed* menimbulkan *delay* inheren antara penerapan limit CPU baru dan pengamatan efek penuhnya yang dapat mengaburkan hubungan *action-reward*; model trafik hanya mengandalkan satu *workload video-streaming* dan satu *slice*; serta statistik *throughput* dan SLA diturunkan dari prapaket kasar yang mengabaikan aspek QoS halus seperti *jitter*. | Ruang aksi terbatas pada kontrol alokasi CPU dan tidak mengontrol alokasi *bandwidth* jaringan SDN atau PRB radio secara simultan. |
| **Xu Bai, Adel N. Toosi, Rajkumar Buyya, Muhammed Tawfiqul Islam (2024)** *(REACH)* | Deep Reinforcement Learning (PPO dan RSDQL/*Reward Sharing* DQN) untuk penjadwalan ulang dan penempatan mikroservis adaptif (*adaptive microservice rescheduling/placement*) | Diskret | Simulasi dan Testbed fisik (Evaluasi pada simulator klaster dan *testbed* Kubernetes fisik) | Mempertimbangkan *overhead* redistribusi/penjadwalan ulang mikroservis akibat kegagalan *node* dan fluktuasi beban secara dinamik, bukan sekadar rencana penjadwalan satu kali. | Pekerjaan masa depan direncanakan untuk memperluas REACH ke optimasi *multi-objective* dengan mengintegrasikan antrean *request* dan metrik *bandwidth*, serta menggabungkan *pre-training* berbasis simulasi dengan *online learning* di *testbed* fisik. | Beroperasi pada lapisan orkestrasi kontainer (Kubernetes) di atas OS/Aplikasi, sehingga tidak mengontrol parameter SDN *data plane* (seperti aturan OpenFlow/*flow table*) secara langsung. |
| **Penulis arXiv:2603.27364 (2026)** *(DRASTIC)* | Advantage Actor-Critic (A2C) yang diintegrasikan dengan optimasi Lyapunov *drift-plus-penalty* dan *differentiable exponential surrogate* | Diskret | Simulasi (Simulasi skenario *Tactile Internet* / *telerobotics* dengan kedatangan MMPP) | Menghubungkan dinamika *control closed-loop* haptik/telerobotik dengan alokasi sumber daya jaringan untuk memenuhi batas latensi probabilistik. | tidak disebutkan | Pengujian terbatas pada skenario simulasi numerik *single-cell* tanpa validasi eksperimental pada *testbed* O-RAN fisik. |
| **Chenghao Song, Minxian Xu, Kejiang Ye, Huaming Wu, dkk. (2024)** *(ChainsFormer)* | DRL berbasis Transformer (ChainsFormer) untuk penyediaan sumber daya (*resource provisioning*) klaster mikroservis | Diskret | Testbed fisik / Simulasi (Klaster Kubernetes) | Mampu menganalisis rantai pemanggilan antar-mikroservis (*microservice call chains*) untuk mencegah terakumulasinya latensi pada rantai dependensi. | tidak disebutkan | Tidak mencakup orkestrasi rute jaringan atau pembagian *slice* pada *data plane* SDN/transport. |

---

💡 **Saran kelanjutan draf paper Anda:** 
Apakah Anda ingin saya membantu merangkum narasi *paragraph summary* dari *research gap* di atas untuk dituliskan tepat di bawah tabel *Related Work* Anda?

Berikut adalah jawaban jujur, transparan, dan terukur berdasarkan analisis komprehensif terhadap seluruh sumber di notebook ini:

---

### 1. Hybrid Action Space (Kombinasi Aksi Diskret & Kontinu dalam Satu Policy)
**Jumlah: 3 paper**

* **Paper 1: "OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning"** (Qiang Liu, Nakjung Choi, Tao Han).
  * **Formulasi Matematis**: Ruang aksi \\(a_t\\) diformulasikan sebagai vektor gabungan elemen diskret dan kontinu: \\(a_t = [U_u, U_m, U_a, U_d, U_s, U_g, U_b, U_l, U_c, U_r]\\).
    * **Komponen Diskret**: Algoritma penjadwalan *uplink/downlink* (\\(U_a, U_g\\)) dan jalur terisolasi pada *transport network* (\\(U_l\\)).
    * **Komponen Kontinu/Numerik**: Alokasi *bandwidth* radio *uplink/downlink* (\\(U_u, U_d\\)), *offset* MCS (\\(U_m, U_s\\)), *bandwidth transport* (\\(U_b\\)), serta alokasi CPU (\\(U_c\\)) dan RAM (\\(U_r\\)) untuk SGPW-U dan *edge server*.
* **Paper 2: "Slice-Aware and Computationally Efficient Resource Orchestration for Converged mmWave–PON O-RAN: A Reward-Shaped PPO Approach for Joint DBA and PRB Allocation"**.
  * **Formulasi Matematis**: Ruang aksi \\(\mathcal{A}\\) diformulasikan sebagai *hybrid*:
    * **Komponen Diskret**: Alokasi *Physical Resource Block* (PRB) mmWave \\(K\\), di mana setiap PRB dipetakan secara biner ke *Radio Unit* (RU) tertentu atau *idle*.
    * **Komponen Kontinu**: Alokasi hibah *Dynamic Bandwidth Allocation* (DBA) pada PON upstream \\(g(t) = [g_1(t), \dots, g_N(t)] \in [0, g_{max}]^N\\) yang tunduk pada batasan kapasitas total \\(\sum_{n=1}^N g_n(t) \le C_{PON} \cdot T_{DBA}\\).
* **Paper 3: "Deep Reinforcement Learning for 6G AI-RAN: A Comprehensive Survey"**.
  * **Formulasi**: Sebagai makalah survei, paper ini mengategorikan penelitian *hybrid action space* di O-RAN (seperti EExAPP yang menggabungkan vektor diskret *RU sleep-scheduling* dengan rasio kontinu alokasi PRB per *slice*, dan ASH-MARL yang menggabungkan D3QN diskret untuk *VNF scaling* dengan TD3 kontinu untuk daya pancar & CPU).

---

### 2. Generative Model (GAN / VAE / Diffusion) untuk Augmentasi Data Trafik
**Jumlah: 3 paper** (Tidak ada paper yang memakai VAE; model yang ditemukan adalah cGAN dan Diffusion Model/DDPM).

* **Paper 1: "GAN-Enhanced Deep Deterministic Policy Gradient Framework for Semantic-Aware Resource Allocation in 6G Network Slicing"** (D. B. Javeed dkk.).
  * **Model**: **Conditional GAN (cGAN)**.
  * **Penerapan**: cGAN digunakan untuk menyintesis pola permintaan trafik (*Traffic Demand Patterns* / TDP) secara bersyarat berdasarkan tipe *slice* (eMBB/mMTC/URLLC) dan kebutuhan QoS guna memperkaya variasi *dataset* pelatihan agen DDPG hingga 40% lebih beragam sebelum dan selama pelatihan policy.
* **Paper 2: "Intelligent Network Slicing in 6G Networks Using Generative Reinforcement Learning and Diffusion Models"**.
  * **Model**: **Denoising Diffusion Probabilistic Model (DDPM / Diffusion Model)**.
  * **Penerapan**: Diffusion model berfungsi sebagai *scenario broker* yang menyintesis skenario kondisi trafik ekstrem (*edge-case traffic demands*) dari *trace* aliran jaringan Uni-Cauca riil (dengan *experience mixing coefficient* \\(\lambda = 0.6\\)) untuk melatih kerangka kerja *Generative RL* (GRL) di bawah pengujian beban hingga 150%.
* **Paper 3: "SpectraGAN: spectrum based generation of city scale spatiotemporal mobile network traffic data"** (Kai Xu, Marco Fiore, Mahesh K. Marina, dkk. - CoNEXT '21).
  * **Model**: **Conditional GAN (SpectraGAN)**.
  * **Penerapan**: Menyintesis data trafik seluler spasio-temporal skala kota berbasis fitur konteks lingkungan untuk digunakan dalam pengujian optimasi alokasi sumber daya dan penghematan daya RAN.

---

### 3. Validasi di Testbed Fisik (Perangkat Keras Riil)
**Jumlah: 8 paper**

1. **"OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning"** (Qiang Liu dkk.).
   * **Hardware**: 2x PC Intel i7 (menjalankan eNB & gNB OAI), Ettus USRP B210 (RF *front-end* 2,6 GHz & 3,5 GHz), 3x *Smartphone* 5G (POCO F2 Pro), *Faraday Cage*, Ettus Octo-clock (*external reference clock*), *switch* SDN Ruckus ICX series, dan *Workstation PC*.
2. **"AI-based Network Slicing in O-RAN for Dynamic Traffic Demands"** (*LS-RLSlice*) (Adhwaa Alchaab, Ayman Younis, Dario Pompili).
   * **Hardware**: **POWDER Testbed** (infrastruktur nirkabel perkotaan *sub-6 GHz* berbasis COTS, OAI 5G Core/RAN, Docker, Kubernetes cluster, serta platform O-RAN OSC untuk Non-RT RIC & Near-RT RIC).
3. **"RL-Loop: Reinforcement Learning-Driven Real-Time 5G Slice Control for Connected and Autonomous Mobility Services"** (Lara Tarkh dkk.).
   * **Hardware**: Server Hyper-V (Prosesor Intel Xeon Gold 6348, RAM 512 GB) yang menjalankan VM Ubuntu 24.04 LTS terintegrasi dengan Open5GS (5G Core) dan UERANSIM (gNB & UE emulation).
4. **"Deep Reinforcement Learning for End-to-End Network Slicing: Challenges and Solutions"**.
   * **Hardware**: Ettus USRP B210 sebagai RF *front-end* Base Station (OpenAirInterface + FlexRAN), *switch* SDN Ruckus ICX series dengan OpenFlow 1.3, dan *workstation* GPU dengan PyTorch.
5. **"Exploring Reinforcement Learning for Scheduling in Cellular Networks"**.
   * **Hardware**: Server COTS sebagai Baseband Unit (BBU), Remote Radio Head (RRH 2x2), 3x *RF cages* untuk pengujian *user equipment*, serta *Variable Attenuators* (V/A) untuk mengontrol *path loss* pada sel LTE 10 MHz.
6. **"Lightweight Session-Key Rekeying Framework for Secure IoT–Edge Communication"**.
   * **Hardware**: Mikrokontroler **ESP32-DevKitC v4** (Xtensa LX6 @ 240 MHz) dengan sensor suhu/kelembapan DHT11 sebagai *IoT Node*, dan **Raspberry Pi 5** (Quad-core Cortex-A76 @ 2,4 GHz, RAM 16 GB) sebagai *Edge-node*.
7. **"ITU Journal of Wireless Communications and Cybersecurity"** (Protocol-Based Traffic Flow Regulation).
   * **Hardware**: **Raspberry Pi 4B** yang terhubung dengan *virtual Open vSwitches* dan *network namespaces* untuk mereplikasi pembatasan jaringan riil dan protokol HTTP/FTP/DNS/ICMP.
8. **"Towards End-to-End Latency Guarantee in MEC Live Video Analytics with App-RAN Mutual Awareness"**.
   * **Hardware**: PC Intel i9 (menjalankan srsRAN-5G), Ettus USRP X310 (pita TDD n78) dengan *Precision GPS Reference Clock*, Server Intel Xeon Gold 5128 dengan **8x GPU NVIDIA RTX 2080 Ti**, dan *smartphone* Google Pixel 6a dengan SIM card terprogram (sysmoISIM-SJA2).

---

### 4. Safety Constraint / Action Masking / Constrained RL
**Jumlah: 7 paper utama** (ditambah 1 survei)

* **Paper 1: "Resource Allocation Method for Network Slicing Using Constrained Reinforcement Learning"** (Yongshuai Liu, Jiaxin Ding, Xin Liu).
  * **Formulasi**: *Constrained Markov Decision Process* (CMDP) \\((\mathcal{S}, \mathcal{A}, R, C, \gamma)\\).
  * **Metode**: Menggunakan *Interior-point Policy Optimization* (IPO) untuk batasan kumulatif (\\(\mathbb{E}[\sum C_i] \le d_i\\)) dan *Projection Layers* (memproyeksikan keputusan RL ke keputusan terdekat yang *feasible*) untuk batasan instan.
* **Paper 2: "OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning"** (Qiang Liu dkk.).
  * **Formulasi**: CMDP dengan batas kegagalan SLA \\(\mathbb{E}_{\pi}[\frac{1}{T}\sum c(s_t, a_t)] \le C_{max}\\).
  * **Metode**: *Constraint-aware policy update* (penalti adaptif pada fungsi *reward*), *Proactive baseline switching* (memotong eksekusi DRL dan mengalihkan ke *rule-based policy* jika SLA diprediksi akan terlanggar), dan *Action modifier* (*supervised neural network* untuk memproyeksikan aksi agar memenuhi batasan fisik infrastruktur).
* **Paper 3: "SliceFed: Federated Constrained Multi-Agent DRL for Dynamic Spectrum Slicing in 6G"**.
  * **Formulasi**: Local CMDP di setiap gNB dengan batasan eksplisit pada interferensi antarsel, rasio PRB (\\(\sum_s a_n^s(t) \le 1\\)), dan batas latensi keras URLLC.
  * **Metode**: Algoritma PPO *Lagrangian primal-dual* yang secara dinamis memperbarui pengali Lagrange \\(\lambda\\) untuk menghukum pelanggaran batasan.
* **Paper 4: "Slice-Aware and Computationally Efficient Resource Orchestration for Converged mmWave–PON O-RAN..."**.
  * **Formulasi**: CMDP dengan batasan kapasitas PON \\(\sum_n g_n(t) \le C_{PON} T_{DBA}\\).
  * **Metode**: *Reward-shaped PPO* dikombinasikan dengan *action masking*.
* **Paper 5: "DRASTIC: A Dynamic Resource Allocation Framework over 6G Network Slicing..."**.
  * **Formulasi**: Batasan latensi probabilistik URLLC yang diubah menjadi *differentiable exponential surrogate*.
  * **Metode**: *Lyapunov drift-plus-penalty reformulation* yang membentuk optimasi *min-max* dengan variabel penalti adaptif untuk menjaga stabilitas antrean dan keandalan latensi.
* **Paper 6: "REACH: Reinforcement Learning for Adaptive Microservice Rescheduling in the Cloud–Edge Continuum"**.
  * **Metode**: *Action masking* pada tingkat *logits* *neural network* selama fase pelatihan dan inferensi untuk mencegah agen memilih aksi penempatan/penjadwalan ulang mikroservis yang tidak valid.
* **Paper 7: "Latency-Aware Workflow Placement in Edge-Cloud Environments: A Reinforcement Learning Approach"**.
  * **Metode**: *Action masking* selama pelatihan dan inferensi untuk menjamin penempatan tugas tidak melanggar batasan kapasitas fisik *node edge*.

---

### 5. Paper yang Menggabungkan Lebih dari Dua Hal Sekaligus
**YA, ADA.** 

Paper yang paling menonjol menggabungkan **tiga (3) kategori sekaligus** adalah:
* **"OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning"** (Qiang Liu, Nakjung Choi, Tao Han, dipublikasikan di *ACM CoNEXT '21*).
  1. **Hybrid Action Space**: Menggabungkan variabel keputusan diskret (algoritma penjadwalan & rute terisolasi) dan kontinu (alokasi *bandwidth*, *offset* MCS, CPU, dan RAM) dalam satu *action space*.
  2. **Testbed Fisik**: Divalidasi secara langsung pada *testbed* fisik E2E berbasis OpenAirInterface (4G/5G NR), OpenDayLight SDN, USRP B210, *smartphone* 5G POCO F2 Pro, dan *switch* SDN Ruckus.
  3. **Safety Constraint / Constrained RL**: Menerapkan formulasi CMDP, *constraint-aware policy update*, *proactive baseline switching*, serta *action modifier*.

Selain itu, terdapat paper yang menggabungkan **dua (2) kategori**:
* **"Slice-Aware and Computationally Efficient Resource Orchestration for Converged mmWave–PON O-RAN..."**: Menggabungkan **Hybrid Action Space** (diskret PRB mmWave + kontinu PON DBA) dan **Constrained RL / Action Masking**.

---

💡 **Saran tindak lanjut:** Apakah Anda ingin saya membuat draf naskah sintesis ringkas (*narrative synthesis*) dari hasil di atas untuk langsung disisipkan ke dalam bab *Discussion* atau *Research Gap* di draf paper Anda?

