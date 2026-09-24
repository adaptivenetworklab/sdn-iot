Berikut adalah tabel *research gap* yang diekstrak secara terstruktur dari sumber-sumber ilmiah di dalam notebook Anda, diurutkan dari yang paling relevan dengan **orkestrasi resource SDN-IoT berbasis DRL**:

| Penulis (tahun) | Pendekatan/algoritma | Action space (diskret/kontinu/hybrid) | Lingkungan evaluasi (simulasi/testbed fisik) | Kelebihan utama | Keterbatasan yang diakui penulis sendiri | Keterbatasan yang terlihat dari luar |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ScienceDirect / RDDQN Study (2025)** | Reinforced Dueling Deep Q-Network (RDDQN) + *Ultimatum Queuing Game* + Slicing RNN (SRNN) pada controller SDN | Diskret (alokasi resource & keputusan antrean) | Simulasi (Mininet / SDN *multi-controller*) | Mengatasi kongesti URLLC pada controller SDN, mencapai *throughput* rata-rata 579.34 kbps dan latensi keputusan <4.5 ms | Membutuhkan *synchronization overhead* bobot terfederasi (*federated weight synchronization*) pada skenario *multi-controller* | Membutuhkan kompresi model (kuantisasi 8-bit) dan akselerator keras (FPGA/GPU) jika ingin diterapkan pada *data plane* SDN riil berkecepatan tinggi |
| **ScienceDirect / SDN-NFV-DQN Study (2025)** | Deep Q-Network (DQN) terintegrasi dengan orkestrasi SDN/NFV untuk penjadwalan *workload* IoT | Diskret | Simulasi (Mininet, Python, TensorFlow) | Secara dinamis menyesuaikan alokasi CPU, memori, *storage*, energi, dan latensi secara *real-time* untuk beban kerja IoT | Lingkungan simulasi belum mereplikasi batasan perangkat keras, variabilitas jaringan riil, dan risiko keamanan fisik secara penuh | Belum mengintegrasikan mekanisme keamanan canggih (seperti *Moving Target Defense* atau mitigasi DDoS) untuk skenario IoT skala besar |
| **TSP CMC (2025)** | Deep Q-Network (DQN) + Graph Neural Network (GNN / Message-Passing NN) pada SDN Controller & NFVO | Diskret (penempatan instans VNF & alokasi resource SFC) | Simulasi (Mininet, mini-NFV, Ryu SDN Controller, TensorFlow) | Mampu mengekstrak fitur topologi *non-Euclidean* graf IoT, meminimalkan *delay* eksekusi VNF, dan menekan *service drop ratio* | Tidak disebutkan | Kompleksitas komputasi pelatihan model DRL-GNN meningkat seiring bertambahnya jumlah *node edge* dan rantai SFC |
| **Nagib dkk. (2025)** (*SafeSlice*) | Risk-sensitive Sigmoid DRL + Supervised Learning Cost Model Safety Layer | Hybrid / Diskret terproyeksi (*nearest safe action*) | Testbed fisik / *Live O-RAN setting* (dengan trafik VR *gaming* riil) | Menjamin kepatuhan SLA instantensial dan kumulatif, menekan pelanggaran latensi hingga 93.24% serta penghematan resource 22.13% | Diperlukan integrasi kombinasi *transfer learning* dan *constrained DRL* untuk meningkatkan generalisasi sambil mempertahankan jaminan keselamatan | Sangat bergantung pada akurasi prediksi model *regressor* keselamatan saat menghadapi lonjakan trafik ekstrem yang belum pernah dilatih (*unseen scenarios*) |
| **Raftopoulos dkk. (2024)** | DRL-based xApp untuk alokasi *slicing* O-RAN terhadap variabel SLA dinamis | Diskret (alokasi jumlah Physical Resource Blocks / PRB) | Emulasi / Testbed O-RAN (OpenRAN Gym) | Beradaptasi terhadap perubahan SLA latensi secara *on-the-fly* tanpa *retraining*, mengurangi pelanggaran SLA 8.3x–14.4x dibanding Q-learning/DQN | Terbatas pada evaluasi dua konfigurasi ambang batas latensi (30 ms dan 110 ms) karena batasan ruang penulisan paper | Evaluasi belum mencakup koordinasi *multi-cell* berskala besar dengan interaksi berbagai jenis trafik yang terinterferensi |
| **SliceFed (2026)** | Federated Multi-Agent Constrained DRL (F-MARL) dengan Primal-Dual PPO berbasis CMDP | Kontinu / Diskret (alokasi spektrum per-gNB) | Simulasi | Menjamin batasan QoS/URLLC dan *inter-cell interference* sekaligus menjaga privasi data lokal antar-gNB | Membutuhkan eksplorasi lebih lanjut untuk agregasi terfederasi asinkron (*asynchronous federated aggregation*) dan integrasi dengan arsitektur O-RAN | Membutuhkan *overhead* komunikasi antar-gNB dan server terfederasi saat koordinasi pengali Lagrange dilakukan |
| **Qi dkk. (2022)** | Augmented Lagrangian Soft Actor-Critic (AL-SAC) dengan arsitektur aksi hierarkis | Hybrid (kombinasi diskret dan kontinu) | Simulasi | Menangani *hybrid action space* pada IIoT dan mematuhi batasan konstrain ketat melalui jaringan pengali Lagrange | Tidak disebutkan | Pelatihan *offline* terpusat berpotensi mengalami keterlambatan adaptasi jika topologi atau kebutuhan IIoT berubah secara mendadak |
| **Liu, Ding, & Liu (2020)** | Constrained DRL menggunakan Adaptive Interior-Point Policy Optimization (IPO) dan *projection layer* | Kontinu | Simulasi | Efektif mengelola konstrain jaringan tanpa ketergantungan tinggi pada pemodelan matematika eksplisit atau bobot penalti manual | Membutuhkan formulasi batas teoritis yang lebih kuat, peningkatan efisiensi sampel (*sample efficiency*), serta evaluasi di lingkungan dunia nyata (*real world evaluations*) | Belum mengikutsertakan arsitektur SDN terdistribusi atau integrasi dengan *edge computing/microservices* |

---

💡 **Apakah Anda ingin saya bantu menyusun narasi paragraf *Related Work* atau merumuskan bagian *Novelty / Contribution* paper Anda berdasarkan tabel *research gap* di atas?**

Berikut adalah jawaban peninjauan komprehensif berdasarkan seluruh sumber yang tersedia di dalam notebook Anda:

---

### **1. Hybrid Action Space (Kombinasi Aksi Diskret & Kontinu dalam Satu Policy)**

**Jumlah:** **3 paper** yang memformulasikan *hybrid action space* khusus untuk *network slicing* / *resource allocation* / *task offloading*.

*   **Paper 1:** *"Augmented Lagrangian-Based Reinforcement Learning for Network Slicing in IIoT"* (Qiang Liu et al., MDPI Electronics, 2022)
    *   **Formulasi Matematis:**
        *   **Aksi Diskret (\\(a_1\\)):** Asosiasi perangkat dengan Base Station (BS), \\(a_1 = \{x_{nm}\}\\), di mana \\(x_{nm} \in \{0, 1\}\\) menentukan apakah perangkat \\(n\\) terhubung ke BS \\(m\\).
        *   **Aksi Kontinu (\\(a_2\\)):** Alokasi bandwidth oleh BS, \\(a_2 = \{b_{nm}\}\\), di mana \\(b_{nm} > 0\\) hanya jika \\(x_{nm} = 1\\).
        *   **Struktur Policy:** Menggunakan *Hierarchical Policy Network* 2-stage (AL-SAC): Stage-1 memilih aksi asosiasi diskret \\(a_1\\) berdasarkan state \\(s\\), lalu Stage-2 memilih aksi kontinu \\(a_2\\) berdasarkan pasangan \\(\{s, a_1\}\\).
*   **Paper 2:** *"Joint Offloading and Resource Allocation for Hybrid Cloud and Edge Computing in SAGINs: A Decision Assisted Hybrid Action Space Deep Reinforcement Learning Approach"* (Chong Huang et al., arXiv, 2024)
    *   **Formulasi Matematis:**
        *   **Aksi Diskret:** Keputusan *offloading* / pemilihan server (apakah tugas diproses lokal, di UAV, Satelit LEO, atau Cloud).
        *   **Aksi Kontinu:** Jumlah alokasi sumber daya komputasi MEC, bandwidth, dan daya pancar transmisi.
        *   **Struktur Policy:** Mendekopel ruang aksi menjadi dua agen SAC terpisah (agen diskret dan agen kontinu) yang dilatih secara independen, kemudian digabungkan menggunakan algoritma *Maximum A Posteriori Policy Optimization* (MAPO).
*   **Paper 3:** *"HyAR-PPO: Hybrid Action Representation Learning for Incentive-Driven Task Offloading in Vehicular Edge Computing"* (Wentao Wang, Mingmeng Li, Honghai Wu, MDPI Sensors, 2026)
    *   **Formulasi Matematis:**
        *   **Aksi Diskret:** Lokasi eksekusi tugas / pemilihan *Assisting Vehicle* atau RSU (\\(k \in \{1, \dots, K\}\\)).
        *   **Aksi Kontinu:** Jumlah alokasi sumber daya komputasi (\\(f_{ij}\\)).
        *   **Struktur Policy:** Memetakan aksi diskret melalui *learnable embedding table* \\(E_\zeta(k)\\) dan variabel kontinu melalui *Conditional Variational Autoencoder* (CVAE) \\(q_\phi, p_\psi\\) ke dalam *latent continuous representation space* bersatu \\(z_x \sim \mathcal{N}(\mu_z(s), \sigma_z(s))\\), lalu dioptimalkan menggunakan PPO clipped objective.

*(Catatan: Terdapat paper lain di notebook yang menggunakan hybrid action space tetapi di luar domain orkestrasi jaringan/slicing, seperti kontrol sinyal lalu lintas ("A Parallel Hybrid Action Space RL Model...") dan robotika ("Overestimation Bias Analysis..."))*.

---

### **2. Generative Model (GAN/VAE/Diffusion) untuk Augmentasi Data Trafik sebelum RL**

**Jumlah:** **0 paper (Nol)**.

*   **Penjelasan:** Tidak ada paper penelitian primer di notebook ini yang mengimplementasikan *generative model* (GAN/VAE/Diffusion) khusus untuk membuat sintetis data trafik jaringan sebagai tahap pra-pemrosesan (*data augmentation*) sebelum melatih agen RL.
*   *Catatan Tambahan:* Paper *survey* (seperti *"Deep Reinforcement Learning for Resource Management on Network Slicing: A Survey"*, 2022) menyitir literatur luar (misalnya Hua et al., 2020 *"GAN-Powered Deep Distributional RL"*), dan paper lain menggunakan GAN/VAE untuk klasifikasi IDS/klasifikasi trafik (*GraphCWGAN-GP*), namun tidak ada paper eksperimental di notebook ini yang membagikan pipeline augmentasi data trafik berbasis generative model untuk agen RL-nya.

---

### **3. Validasi di Testbed Fisik / Hardware Riil (Bukan Hanya Simulasi)**

**Jumlah:** **5 paper**.

1.  **xSlice:** *"Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep Reinforcement Learning"* (Huacheng Zeng et al., 2025)
    *   **Hardware:** 4x Server Intel Core i9-14900K (24 core) untuk 5G Core (OAICN), O-CU, O-DU (OpenAirInterface), dan Near-RT RIC (Mosaic5G FlexRIC); O-RU menggunakan USRP N310 (4x4 MIMO, pita TDD n78 @ 3.319 GHz, subcarrier spacing 30 kHz) dengan GPSDO CDA-2990; Switch Netgear GS308v3; serta 10 smartphone COTS (OnePlus, Google Pixel, Motorola, Samsung Galaxy).
2.  **OpenRAN Gym / Colosseum:** *"DRL-based Latency-Aware Network Slicing in O-RAN with Time-Varying SLAs"* (Raftopoulos et al., 2024)
    *   **Hardware:** Colosseum Standard Radio Nodes (SRNs) yang menggabungkan server berperforma tinggi dengan **USRP X310 SDRs**, dipadukan dengan *Massive Channel Emulator* (MCHEM) berbasis FPGA skala besar untuk emulasi sinyal RF Over-The-Air.
3.  **SafeSlice:** *"SafeSlice: Enabling SLA-Compliant O-RAN Slicing via Safe Deep Reinforcement Learning"* (Nagib et al., 2025)
    *   **Hardware/Platform:** Dideploy langsung pada *live O-RAN setting* menggunakan Near-RT/Non-RT RIC xApp via antarmuka E2/A1 dengan jejak trafik *Virtual Reality (VR) gaming* riil.
4.  **Dynamic Slicing Fronthaul:** *"Real-time Dynamic Network Slicing for the 5G Radio Access Network"* (Zenodo)
    *   **Hardware:** Ettus USRP B210 SDR (Dual Channel Transceiver 70MHz-6GHz) sebagai eNB, 2x Raspberry Pi (Raspbian OS) berantarmuka Huawei E3372 Dongle LTE sebagai UE, serta FlexRAN SDN controller.
5.  **SDN 5G Testbed:** *"SDN-Based Slicing Testbed for 5G Networks"* (Bertrand et al., 2025)
    *   **Hardware:** Hypervisor Proxmox VE, Open5GS Core, srsRAN dengan Ettus SDR, OpenDaylight SDN controller, Open vSwitch (OVS), serta ponsel komersial dengan *custom SIM card*.

---

### **4. Penerapan Safety Constraint / Action Masking / Constrained RL**

**Jumlah:** **5 paper** utama dalam orkestrasi/slicing jaringan.

1.  **SafeSlice** (Nagib et al., 2025)
    *   **Formulasi:** 
        *   *Cumulative Constraints:* Diintegrasikan ke dalam fungsi reward melalui komponen penalti berbasis sigmoid: \\(R_l = W_l \sum \frac{W_s}{1 + e^{c_{1,s}(l_s - c_{2,s})}}\\).
        *   *Instantaneous Constraints & Action Masking:* *Safety layer* di ujung policy DRL menggunakan model regresi XGBoost untuk memprediksi *cost* latensi \\(C_i(s,a)\\). Jika aksi terprediksi melanggar ambang batas \\(\omega_i\\), aksi tersebut dimask/dibatalkan dan diproyeksikan ke aksi aman terdekat menggunakan *Euclidean distance projection*: \\(\min_{a'} \frac{1}{2} \|a' - a\|^2 \quad \text{s.t. } C_i(s,a') \le \omega_i\\).
2.  **SliceFed** (2026)
    *   **Formulasi:** Memformulasikan *slicing* per-gNB sebagai *Local Constrained Markov Decision Process* (CMDP) dengan konstrain latensi URLLC dan interferensi antar-sel. Diselesaikan dengan algoritma **Lagrangian-based primal-dual PPO** di mana variabel dual (\\(\lambda\\)) diperbarui secara *online*.
3.  **AL-SAC** (MDPI Electronics, 2022)
    *   **Formulasi:** Memformulasikan masalah sebagai *Constrained MINLP* / CMDP. Mengintegrasikan **Augmented Lagrangian Method** ke dalam SAC dengan jaringan saraf khusus untuk pengali Lagrange (\\(\lambda\\)) dan fungsi *cost* (\\(C\\)), serta suku penalti kuadratik pada fungsi reward untuk memenuhi konstrain QoS secara ketat.
4.  **Constrained RL for Network Slicing** (Liu, Ding, & Liu, 2021)
    *   **Formulasi:** Memformulasikan jaringan sebagai CMDP. Menggunakan **Adaptive Interior-Point Policy Optimization (IPO)** (*logarithmic barrier functions*) untuk konstrain kumulatif, serta **Projection Layer** (memproyeksikan aksi ke ruang *feasible* terdekat) untuk konstrain instan.
5.  **Dynamic Virtual Resource Allocation for 5G** (arXiv)
    *   **Formulasi:** Memformulasikan alokasi subchannel dan daya sebagai CMDP dengan konstrain antrean, energi, dan latensi. Diselesaikan menggunakan *Approximate Dynamic Programming* (ADP) dengan pembaruan terdistribusi pengali Lagrange (LM).

---

### **5. Paper yang Menggabungkan Lebih dari Dua Kategori di Atas**

**Jumlah:** **0 paper (Nol)**.

Tidak ada satu pun paper di dalam notebook ini yang menggabungkan **3 atau 4** kriteria di atas sekaligus. Namun, terdapat beberapa paper yang berhasil menggabungkan **2 kriteria**:
*   **SafeSlice (Nagib et al., 2025):** Menggabungkan *Physical/Live O-RAN Testbed* (Kategori 3) + *Safety Layer & Action Masking/Constrained RL* (Kategori 4).
*   **AL-SAC (MDPI, 2022):** Menggabungkan *Hybrid Action Space* (Kategori 1) + *Constrained RL / Augmented Lagrangian* (Kategori 4).
*   **HyAR-PPO (MDPI, 2026):** Menggabungkan *Hybrid Action Space* (Kategori 1) + *Action Masking untuk MINLP* (Kategori 4).

Berikut adalah tabel perbandingan lingkungan evaluasi serta jawaban atas pertanyaan-pertanyaan Anda mengenai validasi di testbed fisik berdasarkan sumber-sumber di dalam notebook ini.

---

### **Tabel Perbandingan Lingkungan Evaluasi**

| Sumber (judul, penulis, tahun) | Lingkungan evaluasi (simulator / emulator / hardware fisik) | Nama simulator atau hardware spesifiknya | Skala (jumlah node, switch, tenant, slice) | Agen RL dilatih di mana vs di-deploy di mana | Klaim mereka terkait lingkungan evaluasi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **xSlice: Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN...** (Huacheng Zeng et al., 2025) | Hardware Fisik (Live O-RAN Over-The-Air) | 4 Server (5GC OAICN, O-CU, O-DU OAI, Near-RT RIC FlexRIC), Ettus USRP N310 SDR (4x4 MIMO, GPSDO), Switch Netgear GS308v3, 10 Ponsel COTS (Samsung Galaxy, Google Pixel, OnePlus, Motorola) | 1 O-RU/gNB, 10 UEs (ponsel COTS), multi-session / multi-slice | Dilatih & di-deploy sebagai Near-RT RIC xApp (Python/FlexRIC) secara *live* di testbed | *"Unlike prior DRL approaches that are either based on simulation evaluation, our framework operates in a live O-RAN system using real KPM data... We implement xSlice as a Near-RT RIC xApp in a 5G O-RAN testbed and conduct extensive over-the-air experiments with smartphones running realistic application traffic."* |
| **Real-time Dynamic Network Slicing for the 5G Radio Access Network** (P. Bertrand et al., Zenodo, 2020) | Hardware Fisik (LTE/5G Fronthaul Testbed) | Ettus USRP B210 SDR, 2x **Raspberry Pi** (Raspbian OS) dengan Modem USB Huawei E3372 LTE, LTE Duplexer & Radio Splitter, OpenAirInterface (OAI) eNB/Core, FlexRAN Controller | 1 eNB, 2 UEs (Raspberry Pi), 2 irisan/slice (Mobile Broadband & Video Streaming) | Algoritma *dynamic slicing* (Python) di-deploy di FlexRAN SDN Controller untuk mengontrol eNB | *"According to our analysis, even though these approaches provide the optimal solutions for dynamic slice selection and configuration, they are far from a physical application in a real scenario, where the communication channel is subjected to sudden variations..."* |
| **SDN-Based Network Slicing Mechanism for a Scalable Mobile Private Cloud...** (E. C. C. et al., MDPI Sensors, 2021) | Hardware Fisik + Private Cloud (OpenStack / Kubernetes) | 3x Workstation HP Z240 (OpenStack Private Cloud + 3-node Kubernetes cluster), eNB Nokia FZM, ESP32 + sensor, **Raspberry Pi** (BalenaOS), Open vSwitch (OVS) | 2 eNB Nokia, 2 switch OVS backhaul, 3 compute nodes, sensor ESP32/Raspberry Pi, multi-UPF CNF/slice | Skrip orkestrasi & *load-balancing* di-deploy pada private cloud controller / Kubernetes | *"The second experiment focuses on implementing an end-to-end testbed in order to deliver different types of traffic... through specific network slices when network congestion is detected."* |
| **SDN-Based Slicing Testbed for 5G Networks** (Pablo Bertrand et al., IEEE, 2025) | Hardware Fisik + Virtualisasi Proxmox | Proxmox VE hypervisor (1 physical node hosting 9 VMs), Open5GS 5GC, UERANSIM & srsRAN dengan Ettus SDR (USB), OpenDaylight (ODL) SDN Controller, Open vSwitch (OVS), ponsel komersial + custom SIM | 1 physical host, 9 VMs (1 Core control, 2 UPF/slice, gNB, ODL, OVS), 1 ponsel komersial | Pengontrol adaptif (LSTM & threshold-based) dijalankan sebagai skrip Python via ODL REST API / OVSDB | *"We present an open-source, SDN-driven testbed for 5G standalone network slicing... This modular platform opens a reproducible path for rapid prototyping of slice orchestration policies and paves the way for advanced AI/ML-driven slicing."* |
| **Data-driven Online Slice Admission Control and Resource Allocation for 5G and Beyond Networks** (arXiv, 2025) | Hardware Fisik (3-Node Kubernetes Cluster) | High-performance PC (32 CPU core, 32 GB RAM) untuk RAN, 2x Intel NUC PC (8 CPU core, 16 GB RAM) untuk Transport & Core, Switch Netgear 1 Gbps, ONOS SDN Controller, OVS | 3 physical nodes, 1 physical switch, profil trafik Poisson 1–35 Mbps | Data dikumpulkan dari PCAP testbed fisik, model *data-driven* dilatih secara *offline* dan dioptimalkan secara *online* | *"In many practical scenarios, testing various resource allocation policies directly on actual networks is infeasible... traditional network simulators (e.g., ns-3) simulate the network at the packet-level and require substantial computation and time... Additionally, these simulators often struggle to accurately replicate real-world conditions..."* |
| **Enhancing Microservice Security Through Adaptive Moving Target Defense Policies...** (MDPI, 2024) | Hardware Fisik + Virtual Machines | Physical host (24 CPU core, 128 GB RAM, NVIDIA RTX 3090Ti GPU) + 5 Virtual Machines (4 CPU core, 8 GB RAM) | 1 physical host, 5 VMs, sistem microservice heterogen | Modul DRL berjalan di physical host GPU; sistem microservice berjalan di kluster VM | *"To emulate a realistic microservice environment, this paper constructs a heterogeneous testbed consisting of a physical host and five virtual machines (VMs)."* |
| **DRL-based Latency-Aware Network Slicing in O-RAN with Time-Varying SLAs** (Raftopoulos et al., 2024) | Emulasi Hardware Nirkabel Skala Besar (Colosseum) | Colosseum Standard Radio Nodes (SRNs: Server + USRP X310 SDRs) + FPGA-based *Massive Channel Emulator* (MCHEM), SCOPE, OpenRAN Gym, ColO-RAN | Puluhan SRNs/gNBs & UEs (LXC containers), 2 slices | Dilatih di ColO-RAN / OpenRAN Gym, di-deploy sebagai xApp di Near-RT RIC | *"other methodologies... rely upon simulations, thus emphasizing the need for real-world testing and validation."* |
| **SafeSlice: Enabling SLA-Compliant O-RAN Slicing via Safe Deep Reinforcement Learning** (Ahmad Nagib et al., arXiv, 2025) | Live O-RAN Setting / Guided Domain Randomization | O-RAN Near-RT/Non-RT RIC workflows, data jejak (*traffic traces*) VR *gaming* riil, VoNR, & Video | 3 slices (VR gaming, VoNR, Video), multiple discretized RA levels | Pre-train via Guided Domain Randomization di Non-RT RIC, di-deploy & di-tune secara *online* di Near-RT RIC | *"evaluate the performance under varying and extreme network conditions, especially in an O-RAN deployment setting for immersive 6G applications."* |
| **DYNAMIC RESOURCE MANAGEMENT FOR 5G NETWORK SLICING USING O-RAN NEAR-RT RIC** (B. Chand et al., 2022) | Simulator (ns-3 + 5G-LENA + ns3-gym) | ns-3 v3.40 dengan modul 5G-LENA NR, *co-simulated* dengan Python RIC via ns3-gym | 1 gNB, 45 UEs (5 uRLLC, 10 eMBB, 30 mMTC), 3 BWPs/slices | Algoritma Python BWP Manager di Near-RT RIC berkomunikasi dengan ns-3 setiap 100 ms via OpenGym interface | *"The idealized modelling assumptions and their implications for real deployments are discussed as limitations."* |
| **SDN-Based NFV deployment for multi-objective resource allocation in edge computing...** (ScienceDirect, 2025) | Simulator / Emulator (Mininet + TensorFlow) | Mininet (OpenFlow switches + Ryu), TensorFlow untuk DQN | 25 hingga 200 edge nodes, 100 perangkat IoT, topologi Mesh | Agen DQN dilatih dan dieksekusi di dalam lingkungan simulasi Mininet | *"Our study focuses on a simulation-based evaluation... However, real-world deployment can be significantly more complex due to hardware limitations, network variability, and security risks..."* |

---

### **Jawaban atas Pertanyaan Evaluasi**

#### **1. Berapa banyak sumber yang benar-benar memakai hardware fisik?**
Terdapat **6 paper** di notebook ini yang benar-benar menggunakan *hardware* fisik riil (SDR, bare-metal server, Intel NUC, HP Workstation, ponsel COTS, ESP32, atau Raspberry Pi):
1. **Huacheng Zeng et al. (2025)** (*xSlice*): Menggunakan 4 server, SDR USRP N310, switch Netgear, dan 10 ponsel COTS.
2. **P. Bertrand et al. (Zenodo, 2020)**: Menggunakan SDR USRP B210 dan 2 unit Raspberry Pi dengan modem LTE Huawei.
3. **E. C. C. et al. (MDPI Sensors, 2021)**: Menggunakan 3 Workstation HP Z240 (OpenStack + Kubernetes), eNB Nokia FZM, sensor ESP32, dan Raspberry Pi.
4. **Pablo Bertrand et al. (IEEE, 2025)**: Menggunakan server Proxmox, SDR Ettus, dan ponsel komersial dengan *custom* SIM.
5. **Data-driven Online Slice Admission Control (arXiv, 2025)**: Menggunakan PC 32-core, 2 unit Intel NUC PC, dan switch Netgear 1 Gbps.
6. **Enhancing Microservice Security (MDPI, 2024)**: Menggunakan *physical host* (GPU RTX 3090Ti) + kluster VM.
*(Catatan: Terdapat pula 1 paper oleh **Raftopoulos et al. (2024)** yang menggunakan platform **Colosseum**, yaitu emulasi hardware RF berbasis FPGA skala besar dengan SDR USRP X310).*

#### **2. Adakah yang memakai single-board computer seperti Raspberry Pi?**
**Ya, ada 2 paper eksperimental** yang secara langsung mengintegrasikan Raspberry Pi sebagai node/UE dalam testbed fisik mereka:
* **Paper 1 (*Zenodo, 2020*):** Memakai **2 unit Raspberry Pi** (Raspbian OS) yang dilengkapi dengan *dongle* USB Huawei E3372 LTE untuk bertindak sebagai perangkat end-user (UE) yang terhubung ke eNB berbasis USRP B210.
* **Paper 2 (*MDPI Sensors, 2021*):** Memakai **Raspberry Pi** (menjalankan BalenaOS) bersama dengan mikrokontroler ESP32 sebagai perangkat IoT *edge*.
*(Selain itu, paper survey/review "Offloading Mechanisms Based on RL..." dan paper "IIETA 2026" juga mendiskusikan penggunaan Raspberry Pi 4 sebagai rencana future work/testbed).*

#### **3. Adakah sumber yang secara eksplisit mengklaim validasi di testbed fisik sebagai kontribusi? Bagaimana cara merumuskannya?**
**Ya, beberapa paper secara tegas mencantumkan validasi testbed fisik sebagai salah satu poin kontribusi utama mereka.** Anda dapat meniru tingkat kehati-hatian dan objektivitas formulasi klaim berikut:

* **Contoh Formulasi 1 (*xSlice - Huacheng Zeng et al., 2025*):**
  > *"Unlike prior DRL approaches that are either based on simulation evaluation, our framework operates in a live O-RAN system using real KPM data... We implement xSlice as a Near-RT RIC xApp in a 5G O-RAN testbed and conduct extensive over-the-air experiments with smartphones running realistic application traffic."*
  *(Formulasi ini menonjolkan perbedaan langsung dengan pendekatan simulasi tanpa merendahkannya, serta menyebutkan secara objektif perangkat yang digunakan).*

* **Contoh Formulasi 2 (*Real-time Dynamic Network Slicing - Zenodo, 2020*):**
  > *"According to our analysis, even though these approaches provide the optimal solutions for dynamic slice selection and configuration, they are far from a physical application in a real scenario, where the communication channel is subjected to sudden variations... Second, we define a real scenario within our testbed... Third, we test our dynamic slicing model alongside a static slicing baseline model on top of our testbed..."*
  *(Formulasi ini menyoroti klaim kebaruan dengan menunjukkan bahwa simulasi matematis murni sering kali tidak menangkap variasi mendadak pada saluran komunikasi riil).*

* **Contoh Formulasi 3 (*Data-driven Online Slice Admission Control - arXiv, 2025*):**
  > *"In many practical scenarios, testing various resource allocation policies directly on actual networks is infeasible... traditional network simulators (e.g., ns-3) simulate the network at the packet-level and require substantial computation and time... Additionally, these simulators often struggle to accurately replicate real-world conditions, particularly in wireless environments. We use this testbed to collect our dataset..."*

#### **4. Adakah sumber yang membahas keterbatasan evaluasi berbasis simulasi untuk memotivasi pilihan testbed fisik?**
**Ya, banyak sumber di notebook ini yang membahas keterbatasan simulasi dan dapat Anda kutip untuk memotivasi pilihan testbed fisik Anda:**

1. **AI Methods in Network Slice Life-Cycle Phases: A Survey (MDPI, 2025):**
   > *"Moreover, the proposed methods are mostly evaluated through simulations with synthetic data, which limits their practical reliability. Hence, real-world performance evaluation is crucial for ensuring commercial acceptance and effective deployment."*

2. **Deep Reinforcement Learning for Resource Management on Network Slicing: A Survey (MDPI Sensors, 2022):**
   > *"RL/DRL solutions in networking have usually been evaluated in simulated scenarios, hindering their practical deployment... As the real world is very different from simulations/emulations, it is necessary to answer additional questions: How do RL/DRL-based solutions adapt to real dynamic data traces? How do RL-DRL-based solutions scale in real dynamic networks?"*

3. **JAIT / Reward Shaping in DRL Study (2025):**
   > *"The significant disadvantage [of synthetic datasets and simulators] is abstraction from real data, such that factors such as hardware latency, variation of user behavior, and unpredictable patterns of interference may influence performance... evaluation under an emulated or experimental 5G testbed would close the loop between trial-and-error development in simulations and future deployment realism..."*

4. **How to Do Statistical Evaluations in ECE/CS Papers (arXiv):**
   > *"Most systems and networking papers rely on simulators. Simulators are convenient and almost always wrong in some way that matters; the question is whether the way they are wrong undermines the claim."*

---

💡 **Rekomendasi untuk Paper Anda:** 
Menjelaskan bahwa testbed Anda dibangun menggunakan **Raspberry Pi 5, Open vSwitch, Ryu Controller, dan Kubernetes** ditempatkan pada posisi yang sangat kuat secara akademik. Anda dapat merumuskannya secara proporsional seperti:
> *"While simulation frameworks (e.g., ns-3, Mininet) provide controlled environments, they often abstract away hardware execution delays, real OS container scheduling overheads, and physical network noise. To validate our proposed DRL orchestration policy under realistic execution constraints, we implement a physical prototype testbed utilizing Raspberry Pi 5 single-board computers, Open vSwitch, Ryu SDN controller, and Kubernetes..."*

Tentu, berikut adalah pemetaan komprehensif mengenai lingkungan evaluasi, penggunaan perangkat keras fisik, dan justifikasi *sim-to-real gap* dari sumber-sumber di notebook Anda untuk membantu menyusun klaim kebaruan secara proporsional.

---

### Tabel Perbandingan Lingkungan Evaluasi Penelitian

| Sumber (judul, penulis, tahun) | Lingkungan evaluasi (simulator / emulator / hardware fisik) | Nama simulator atau hardware spesifiknya | Skala (jumlah node, switch, tenant, slice) | Agen RL dilatih di mana vs di-deploy di mana | Klaim mereka terkait lingkungan evaluasi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **"OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning"** (Qiang Liu, Nakjung Choi, Tao Han, 2021) | Hardware Fisik (Testbed E2E) | 2x Workstation PC (eNB/gNB), USRP B210 (RF front-end 2,6 GHz & 3,5 GHz), Octo-clock, Faraday Cage, 3x POCO F2 Pro 5G, Ruckus ICX SDN switch, OpenAirInterface (OAI), OpenDaylight [cite: 222, 223] | Lintas domain (RAN, TN, CN, EN), 3 irisan jaringan (*slices*), 3 smartphone 5G [cite: 222, 224] | Dilatih secara *online* langsung di testbed fisik (dengan inisialisasi *imitation learning*), di-deploy di Workstation PC [cite: 30, 223] | Mampu mengeksekusi konfigurasil ulang E2E dalam skala sub-detik langsung pada testbed fisik tanpa mengganggu stabilitas [cite: 31]. |
| **"AI-based Network Slicing in O-RAN for Dynamic Traffic Demands" / LS-RLSlice** (Adhwaa Alchaab, Ayman Younis, Dario Pompili, 2025) | Hardware Fisik / Testbed Publik | POWDER testbed (USRP SDRs, COTS x86 server), OAI 5G Core/RAN, Docker, Kubernetes, O-RAN Software Community (OSC) platform (RICs) [cite: 14, 18] | Multi-node Kubernetes cluster (control plane, master, worker nodes), multiple network slices [cite: 18, 19] | LTRA dilatih/di-deploy di Non-RT RIC (rApp) dan STRS di Near-RT RIC (xApp) di POWDER testbed [cite: 18, 21] | Berhasil memvalidasi alokasi sumber daya *near-real-time* (<10 ms) pada infrastruktur fisik POWDER O-RAN [cite: 14, 20]. |
| **"RL-Loop: Reinforcement Learning-Driven Real-Time 5G Slice Control..."** (Lara Tarkh dkk., 2026) | Hardware Fisik / Emulasi Testbed | Hyper-V host (Intel Xeon Gold 6348, 512 GB RAM), Ubuntu 24.04 VMs, Open5GS, UERANSIM (gNB & UE emulation) [cite: 256] | 1 slice eMBB, 1 gNB, 1–5 UE/detik (streaming video 4K) [cite: 256] | Dilatih *offline* dari log CSV testbed, di-deploy *online* sebagai feedback controller (PPO) di testbed [cite: 254, 257] | Mengoperasikan kontrol umpan balik *real-time* pada testbed fisik 5G dan menghemat >55% CPU dibanding acuan static [cite: 254, 333]. |
| **"REACH: Reinforcement Learning for Adaptive Microservice"** (Xu Bai, Adel N. Toosi, Rajkumar Buyya, Muhammed Tawfiqul Islam, 2024) | Hibrida (Simulator CEEnv + Testbed Fisik Kubernetes) | Simulator CEEnv (Python) + Testbed Kubernetes di OpenStack Cloud (VMs dengan inter-region delay ~50 ms, intra-region <1 ms) [cite: 244, 246, 247] | 4 node VM Kubernetes, 4 mikroservis fungsional [cite: 246] | *Pre-training* di simulator CEEnv, lalu di-transfer/deploy ke testbed Kubernetes fisik [cite: 243, 244] | Menyediakan *sim-to-real pipeline* yang mentransfer kebijakan RL dari simulasi ke klaster Kubernetes fisik [cite: 242, 244]. |
| **"ChainsFormer: A Chain Latency-Aware Resource Provisioning..."** (Chenghao Song, Minxian Xu, Kejiang Ye, Huaming Wu, dkk., 2024) | Testbed Fisik / Bare-metal | Klaster Kubernetes (5 node physical, Intel Xeon E5-2660, 64 GB RAM), Jaeger tracing, Locust (Alibaba trace) [cite: 56] | 5 node bare-metal (1 master, 4 worker), aplikasi mikroservis Train-Ticket [cite: 56] | Dilatih *offline* dari data telemetri historis testbed, di-deploy *online* di klaster Kubernetes [cite: 37] | Membuktikan efektivitas penskalaan multi-dimensi pada klaster Kubernetes riil dengan memotong latensi 26% [cite: 38]. |
| **"Protocol-Based Traffic Flow Regulation on SDN with Ryu’s REST APIs..."** (Sultan Çoğay, Ayça Tulum, Gökhan Seçinti, 2024) | Hardware Fisik | Raspberry Pi 4B (8GB RAM), Open vSwitch v2.15 (7 bridges: Br1–Br7), Ryu Controller, Network Namespaces [cite: 174, 180, 181] | 7 OVS virtual switches, 4 server (HTTP, FTP, DNS, SMTP), 2 hosts [cite: 180] | N/A (Aturan QoS rule-based via REST API) [cite: 179, 181] | Memilih Raspberry Pi 4B karena ukurannya kecil, murah, dan mampu mereplikasi batasan jaringan dunia nyata [cite: 174]. |
| **"GNN-enhanced Traffic Anomaly Detection for Next-Generation SDN..."** (2024) | Hardware Fisik | 2x Raspberry Pi 5 (16GB RAM) + 1x Raspberry Pi 4 (8GB RAM), Open vSwitch, ONOS Controller [cite: 168] | 3 Raspberry Pi nodes (1 Controller & NAD, 1 OVS Switch, 1 CE Device) [cite: 168] | N/A (Klasifikasi GNN) [cite: 168] | Menggunakan Raspberry Pi sebagai platform berbiaya rendah namun kuat untuk mengemulasi jaringan SDN-IoT riil [cite: 168]. |
| **"Lightweight Session-Key Rekeying Framework for Secure IoT–Edge Communication"** (Haranath Rakshit dkk., 2025) | Hardware Fisik | ESP32-DevKitC v4 (Client), Raspberry Pi 5 (16GB RAM, Edge Server), Dockerized Mosquitto MQTT, sensor DHT11 [cite: 209, 210] | 1 ESP32 IoT Node, 1 Raspberry Pi 5 Edge Node, >6,500 paket data [cite: 209, 210, 212] | N/A (Framework rekeying keamanan) [cite: 209] | Divalidasi langsung pada testbed IoT–Edge nyata untuk mengukur latensi dan *throughput* steady-state [cite: 209, 212]. |
| **"EASE-6G: An Energy-Aware SDN Framework with Proactive Slicing..."** (2026) | Simulator | OMNeT++ v6.0 + Simu5G library + Ryu SDN framework + Python (socket linkage) [cite: 128] | Skala 6G-IoT terdensifikasi (hingga \\(10^6\\) perangkat/km²) [cite: 38] | Dilatih dan dievaluasi sepenuhnya di simulator OMNeT++/Simu5G [cite: 128] | Dievaluasi dalam lingkungan simulasi *discrete-event* terkontrol OMNeT++ dan Simu5G [cite: 128]. |

---

### Jawaban atas Pertanyaan Evaluasi

#### 1. Berapa banyak sumber yang benar-benar memakai hardware fisik?
Dari 160 sumber di notebook Anda, terdapat **8 paper yang dievaluasi/divalidasi pada hardware fisik atau testbed nyata** (bukan sekadar Mininet/NS-3/OMNeT++ murni):
1. **OnSlicing** (Qiang Liu dkk., 2021) [cite: 222]
2. **LS-RLSlice** (Adhwaa Alchaab dkk., 2025) [cite: 14]
3. **RL-Loop** (Lara Tarkh dkk., 2026) [cite: 254]
4. **REACH** (Xu Bai dkk., 2024) [cite: 242, 244]
5. **ChainsFormer** (Chenghao Song dkk., 2024) [cite: 56]
6. **Lightweight Session-Key Rekeying Framework** (Haranath Rakshit dkk., 2025) [cite: 209]
7. **GNN-enhanced Traffic Anomaly Detection** (2024) [cite: 168]
8. **Protocol-Based Traffic Flow Regulation on SDN** (Sultan Çoğay dkk., 2024) [cite: 174]

*(Catatan: Beberapa sumber survei juga mengatalogkan testbed fisik seperti Colosseum, POWDER, COSMOS, dan Arena [cite: 94, 97]).*

---

#### 2. Adakah yang memakai single-board computer seperti Raspberry Pi?
**Ya, ada 4 paper** yang memakai Raspberry Pi secara eksplisit dalam testbed fisik mereka:
1. **"GNN-enhanced Traffic Anomaly Detection..."** (2024): Memakai **2x Raspberry Pi 5 (16GB RAM)** (1 sebagai Controller ONOS, 1 sebagai Switch OVS) dan **1x Raspberry Pi 4 (8GB RAM)** sebagai perangkat penerbit trafik [cite: 168].
2. **"Lightweight Session-Key Rekeying Framework..."** (Haranath Rakshit dkk., 2025): Memakai **Raspberry Pi 5 (16 GB RAM)** sebagai *Edge Server/MQTT Broker* berbasis Docker [cite: 209, 210].
3. **"ITU Journal of Wireless Communications and Cybersecurity"** (*Protocol-Based Traffic Flow Regulation*, Sultan Çoğay dkk., 2024): Memakai **Raspberry Pi 4B (8GB RAM)** yang menjalankan Open vSwitch (OVS v2.15) dan terhubung ke Ryu Controller [cite: 174, 181, 184].
4. **"Machine Learning-Based Real-Time Detection and Mitigation of DoS Attacks in SDN-Based 5G Network"** (2024): Memakai **Raspberry Pi 3 (1.4 GHz CPU, 1 GB RAM)** sebagai switch SDN fisik berbasis Open vSwitch [cite: 214, 215].

---

#### 3. Adakah sumber yang secara eksplisit mengklaim validasi di testbed fisik sebagai kontribusi? Bagaimana mereka merumuskannya?

**Ya, beberapa paper secara eksplisit menonjolkan validasi di testbed fisik sebagai kontribusi utama.** Berikut adalah rumusan dan kutipan langsungnya:

* **LS-RLSlice / "AI-based Network Slicing in O-RAN for Dynamic Traffic Demands"** (Adhwaa Alchaab dkk., 2025):
  > *"Finally, our proposed solution is validated using the real-world POWDER testbed supporting the O-RAN stack and provides configuration setups for Non-Real-Time and Near-Real-Time RAN Intelligent Controllers (Non-RT RIC and Near-RT RIC)."* [cite: 14]
  * **Cara Merumuskan**: Menempatkan kalimat ini di poin penutup *Abstract* dan bab pendahuluan sebagai bukti bahwa algoritma tidak hanya bekerja secara teoritis tetapi juga patuh pada batasan *real-time* O-RAN [cite: 14, 20].

* **REACH** (Xu Bai dkk., 2024):
  > *"Evaluating MSA placement strategies in real-world testbeds remains a significant challenge... To address these challenges, we propose REACH... a sim-to-real deployment pipeline that transfers the strategies learned in simulation directly to a real-world Kubernetes-based cloud–edge continuum testbed."* [cite: 241, 242, 244]
  * **Cara Merumuskan**: Membingkai kurangnya validasi testbed di literatur sebagai *challenge/gap*, lalu mencantumkan *sim-to-real pipeline* ke testbed Kubernetes fisik sebagai poin kontribusi (*bullet point*) utama [cite: 241, 244].

* **OnSlicing** (Qiang Liu dkk., 2021):
  > *"We evaluate the performance of OnSlicing on an end-to-end physical testbed... We design four domain managers... that realize sub-second E2E resource slicing."* [cite: OnSlicing, 28, 31]
  * **Cara Merumuskan**: Menekankan keberhasilan merancang manajer domain kustom yang memungkinkan rekonfigurasi parameter perangkat keras fisik secara *online* dan *sub-detik* [cite: 31].

---

#### 4. Adakah sumber yang membahas keterbatasan evaluasi berbasis simulasi (untuk memotivasi pilihan testbed fisik)?

**Ya, sangat banyak.** Anda dapat menggunakan kutipan-kutipan langsung berikut untuk menyusun bab latar belakang atau *motivation* paper Anda:

1. **REACH** (Xu Bai dkk., 2024):
   > *"As a result, most existing studies rely on simulation environments to validate their algorithms. However, such simulations may not fully capture the complexity and variability of real deployments, thereby limiting the applicability and effectiveness of these algorithms in production scenarios."* [cite: 241, 242]

2. **Analisis Komparatif Validasi Testbed Fisik dalam Orkestrasi Jaringan Berbasis Reinforcement Learning**:
   > *"Meskipun platform simulasi menawarkan kemudahan dalam merekayasa topologi skala besar, model-model tersebut sering kali mengabaikan kendala perangkat keras yang terjadi pada sistem nyata. Keterbatasan ini dikenal sebagai simulation-to-reality discrepancy, di mana variasi latensi tingkat kernel, penundaan penjadwalan antrean (queue scheduling jitter), dan biaya komputasi dari proses pengambilan keputusan agen tidak terepresentasi secara akurat."* [cite: 26]

3. **"Deep Reinforcement Learning for 6G AI-RAN: A Comprehensive Survey"** (2026):
   > *"A policy that appears effective in a simplified simulator may become unstable when it receives delayed measurements, when users move according to unmodeled mobility patterns, when the channel statistics shift, or when the action has to be transported through an actual RIC-to-RAN control loop."* [cite: 95]

4. **"AI Methods in Network Slice Life-Cycle Phases: A Survey"** (MDPI, 2024):
   > *"Moreover, the proposed methods are mostly evaluated through simulations with synthetic data, which limits their practical reliability. Hence, real-world performance evaluation is crucial for ensuring commercial acceptance and effective deployment."* [cite: 9]

5. **"Realistic Performance Assessment of Machine Learning Algorithms for 6G Network Slicing"** (MDPI, 2025):
   > *"A significant gap exists between the high accuracy achieved in laboratory conditions and the performance achieved in real-world scenarios. Most studies are limited to controlled simulation environments, where the same level of success cannot be guaranteed in real networks."* [cite: 281]

---

💡 **Rekomendasi Pemosisian Klaim Kebaruan Paper Anda:**
1. **Jangan mengklaim** bahwa Anda adalah yang *pertama kali* membuat testbed fisik (karena proyek seperti OnSlicing dan POWDER sudah ada) [cite: 14, 28].
2. **Tonjolkan**:
   * **Aksesibilitas & Reproduksibilitas Berbiaya Rendah (*Low-cost Reproducible Testbed*)**: Menggabungkan Raspberry Pi 5, OVS, Ryu, dan Kubernetes menghadirkan testbed fisik yang terjangkau bagi peneliti lain dibanding infrastruktur mahal seperti USRP B210 [cite: 42, 49, 174].
   * **Orkestrasi Lintas Lapisan Terintegrasi (*Cross-Layer Co-design*)**: Mengintegrasikan kontrol jaringan *data-plane* SDN (Ryu + OVS) dan orkestrasi kontainer aplikasi (Kubernetes) secara simultan di bawah satu agen RL [cite: 46, 49].