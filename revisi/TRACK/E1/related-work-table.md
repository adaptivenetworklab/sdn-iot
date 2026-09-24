# Related Work Table (E1) — pengganti Table I

Sumber: `Sumber1.md` (basis urutan, domain SDN-IoT) + `Sumber2.md` (tambahan: SafeSlice, AL-SAC, HyAR-PPO, Liu-Ding-Liu, Raftopoulos, per instruksi T2). 11 baris pembanding + 1 baris PROPOSE = 12 baris (batas maksimal).

Dibuang dari kandidat karena paling jauh dari domain SDN-IoT/mikroservis: EASE-6G (2026, murni 6G energy/signaling, gak ada RL orchestration data-plane), DRASTIC (2026, domain Tactile Internet/telerobotics).

## Format Markdown

| Ref | Pendekatan | Action space | Augmentasi generatif | Lingkungan evaluasi | Keterbatasan |
|---|---|---|---|---|---|
| `liu2021onslicing` | Individualized per-slice DRL, constraint-aware policy update, proactive baseline switching, action modifier (CMDP) | Hybrid (diskret: penjadwalan/path · kontinu: bandwidth/MCS/CPU/RAM) | – | Testbed fisik E2E (OpenAirInterface 4G/5G NR, OpenDayLight SDN, USRP B210) | *(diakui penulis)* pada skala besar, state space membesar & enforcement-delay antar-aksi heterogen berpotensi menambah beban trafik transport; dievaluasi di testbed skala kecil |
| `nagib2025safeslice` | Risk-sensitive sigmoid-penalty DRL + safety layer berbasis regresi XGBoost, proyeksi Euclidean ke aksi aman terdekat | Hybrid / diskret-terproyeksi | – | Live O-RAN setting (testbed fisik, trafik VR gaming riil) | *(diakui penulis)* perlu integrasi transfer learning + constrained DRL lebih lanjut untuk generalisasi sambil menjaga jaminan keselamatan |
| `alsac2022` | Augmented Lagrangian SAC, hierarchical 2-stage policy (asosiasi BS diskret → bandwidth kontinu) | Hybrid | – | Simulasi | *(tidak disebutkan penulis; terlihat dari luar)* pelatihan offline terpusat berpotensi lambat beradaptasi bila topologi/kebutuhan IIoT berubah mendadak |
| `wang2026hyarppo` | Hybrid Action Representation: embedding table (diskret) + CVAE (kontinu) disatukan ke latent space, dioptimasi PPO clipped | Hybrid | – *(CVAE dipakai untuk representasi aksi, bukan augmentasi data trafik)* | TODO-VERIFY *(tidak eksplisit di Sumber1/2.md)* | *(tidak tercantum di sumber)* |
| `alchaab2025lsrlslice` | Dual-time-scale Actor-Critic: LSTM rApp (jangka panjang) + DDPG xApp (jangka pendek) | Kontinu | – | Testbed fisik POWDER (OAI 5G, Docker, Kubernetes, OSC O-RAN) | *(tidak disebutkan penulis; terlihat dari luar)* fokus lapisan RAN/RIC O-RAN, tidak mengintegrasikan manajemen antrean mikroservis lapisan aplikasi edge |
| `rsppo2026` | Reward-Shaped PPO + GCN state abstraction + action masking + prioritized N-step replay | Hybrid (PRB diskret biner + DBA kontinu) | – | Simulasi (standar 3GPP mmWave + dinamika GPON DBA) | *(diakui penulis, tersirat dari future work)* topologi single-PON, belum divalidasi di O-RAN/PON fisik; rencana ke depan: multi-PON, meta-learning, FPGA |
| `tarkh2026rlloop` | Closed-loop feedback controller berbasis PPO, menyesuaikan alokasi CPU slice 5G real-time dari KPI | Diskret | – | Testbed fisik Open5GS + UERANSIM (VM Hyper-V) | *(diakui penulis)* delay inheren testbed antara penerapan limit CPU baru & pengamatan efek penuh dapat mengaburkan hubungan action-reward; trafik hanya 1 workload video-streaming, 1 slice |
| `bai2024reach` | PPO + RSDQL (Reward Sharing DQN) untuk adaptive microservice rescheduling/placement | Diskret | – | Simulasi + testbed Kubernetes fisik (sim-to-real pipeline) | *(diakui penulis)* rencana ke depan: optimasi multi-objective, integrasi antrean request & metrik bandwidth |
| `song2024chainsformer` | DRL berbasis Transformer untuk resource provisioning klaster mikroservis, analisis rantai call antar-mikroservis | Diskret | – | Testbed fisik bare-metal Kubernetes (5 node) | *(tidak disebutkan penulis; terlihat dari luar)* tidak mencakup orkestrasi rute jaringan atau pembagian slice pada data plane SDN/transport |
| `liu2021constrained` | Constrained RL: Adaptive Interior-Point Policy Optimization (IPO) + Projection Layer, CMDP | Kontinu | – | Simulasi | *(diakui penulis)* perlu formulasi batas teoritis lebih kuat, peningkatan efisiensi sampel, evaluasi dunia nyata |
| `raftopoulos2024` | DRL-based xApp untuk alokasi slicing O-RAN terhadap SLA dinamis | Diskret (alokasi jumlah PRB) | – | Emulasi/testbed O-RAN (OpenRAN Gym / Colosseum) | *(diakui penulis)* evaluasi terbatas pada 2 konfigurasi ambang latensi (30ms, 110ms) karena batasan ruang tulisan paper |
| **PROPOSE (SDH-PPO, kita)** | Continuous-action Actor-Critic (Dueling Critic value+advantage-residual head) + rule-based safety-margin correction (inference-time) + augmentasi WGAN-GP, dilatih offline dari data testbed fisik | **Continuous** (1 skalar global, diterapkan ke 3 port dengan koefisien tetap berbeda — bukan hybrid, bukan per-port independen) | **WGAN-GP** | Testbed fisik (Raspberry Pi + OVS + Ryu + Flowvisor) untuk koleksi data traffic asli; training & evaluasi RL **offline** (evaluasi delay via counterfactual perturbation dari log, bukan live replay) | *(jujur, dari audit kode)* 1 aksi skalar dipakai untuk P1/P2/P4 sekaligus (bukan kontrol independen per-port); evaluasi delay counterfactual bukan simulasi jaringan hidup; P2 violation masih tinggi (29.5%) karena reward hanya beri insentif throughput P2 (bukan penalti delay P2 langsung); threshold SLA di reward training (12/10/3.5ms) beda dari threshold evaluasi (6/70/7ms) |

## Format LaTeX (table* untuk 2-kolom)

```latex
\begin{table*}[t]
\centering
\caption{Related Work Comparison for DRL-Based SDN-IoT Resource Orchestration}
\label{tab:related-work}
\scriptsize
\begin{tabular}{p{1.6cm}p{3.6cm}p{2.0cm}p{1.5cm}p{2.8cm}p{4.2cm}}
\toprule
Ref & Pendekatan & Action space & Augmentasi generatif & Lingkungan evaluasi & Keterbatasan \\
\midrule
\cite{liu2021onslicing} & Individualized per-slice DRL, constraint-aware policy update, proactive baseline switching, action modifier (CMDP) & Hybrid (discrete sched./path + continuous BW/MCS/CPU/RAM) & -- & Physical E2E testbed (OAI 4G/5G NR, OpenDayLight SDN, USRP B210) & At scale, expanding state space \& heterogeneous enforcement delay may add transport traffic overhead; evaluated on small-scale testbed \\
\cite{nagib2025safeslice} & Risk-sensitive sigmoid-penalty DRL + XGBoost cost-regressor safety layer, Euclidean projection to nearest safe action & Hybrid / projected-discrete & -- & Live O-RAN setting (physical testbed, real VR gaming traffic) & Requires further transfer-learning + constrained-DRL integration for generalization while preserving safety guarantees \\
\cite{alsac2022} & Augmented Lagrangian SAC, hierarchical 2-stage policy (discrete BS association $\to$ continuous bandwidth) & Hybrid & -- & Simulation & Centralized offline training may adapt slowly if IIoT topology/demand shifts abruptly (not stated by authors) \\
\cite{wang2026hyarppo} & Hybrid Action Representation: discrete embedding table + continuous CVAE unified into latent space, PPO-clipped & Hybrid & -- (CVAE for action representation, not traffic augmentation) & TODO-VERIFY & Not stated in source \\
\cite{alchaab2025lsrlslice} & Dual-time-scale Actor-Critic: LSTM rApp (long-term) + DDPG xApp (short-term) & Continuous & -- & Physical POWDER testbed (OAI 5G, Docker, Kubernetes, OSC O-RAN) & Focused on RAN/RIC O-RAN layer, does not integrate application-layer microservice queue management (not stated by authors) \\
\cite{rsppo2026} & Reward-Shaped PPO + GCN state abstraction + action masking + prioritized N-step replay & Hybrid (discrete PRB + continuous DBA) & -- & Simulation (3GPP mmWave + GPON DBA dynamics) & Single-PON topology, not validated on physical O-RAN/PON hardware; future work: multi-PON, meta-learning, FPGA \\
\cite{tarkh2026rlloop} & PPO-based closed-loop feedback controller, real-time CPU allocation from KPIs & Discrete & -- & Physical Open5GS + UERANSIM testbed (Hyper-V VM) & Inherent testbed delay between CPU limit application and observed effect may obscure action-reward relationship; single video-streaming workload, single slice \\
\cite{bai2024reach} & PPO + RSDQL for adaptive microservice rescheduling/placement & Discrete & -- & Simulator + physical Kubernetes testbed (sim-to-real pipeline) & Future work: multi-objective optimization, request queue \& bandwidth metric integration \\
\cite{song2024chainsformer} & Transformer-based DRL for microservice cluster resource provisioning, call-chain analysis & Discrete & -- & Physical bare-metal Kubernetes testbed (5 nodes) & Does not cover network routing or SDN/transport data-plane slice orchestration (not stated by authors) \\
\cite{liu2021constrained} & Constrained RL: Adaptive Interior-Point Policy Optimization + Projection Layer, CMDP & Continuous & -- & Simulation & Requires stronger theoretical bounds, improved sample efficiency, real-world evaluation \\
\cite{raftopoulos2024} & DRL-based xApp for O-RAN slice allocation under dynamic SLAs & Discrete (PRB count allocation) & -- & O-RAN emulation/testbed (OpenRAN Gym / Colosseum) & Evaluation limited to two latency thresholds (30ms, 110ms) due to paper space constraints \\
\textbf{PROPOSE (ours)} & Continuous-action Actor-Critic (Dueling Critic value+advantage-residual head) + rule-based safety-margin correction (inference-time) + WGAN-GP augmentation, offline-trained from physical testbed data & \textbf{Continuous} (single global scalar, applied to 3 ports w/ fixed per-port coefficients -- not hybrid, not per-port independent) & \textbf{WGAN-GP} & Physical testbed (Raspberry Pi + OVS + Ryu + Flowvisor) for real traffic collection; RL training/eval \textbf{offline} (counterfactual delay perturbation, not live replay) & Single action scalar shared across P1/P2/P4 (not independently controlled per port); counterfactual (non-live) delay evaluation; P2 violation remains high (29.5\%) since reward only incentivizes P2 throughput, not P2 delay directly; training-time SLA thresholds (12/10/3.5ms) differ from evaluation thresholds (6/70/7ms) \\
\bottomrule
\end{tabular}
\end{table*}
```

## Catatan
- `wang2026hyarppo`: lingkungan evaluasi TODO-VERIFY karena Sumber1.md/Sumber2.md gak nyebut eksplisit (fokus keduanya cuma soal formulasi action space-nya, konteks aslinya "Vehicular Edge Computing").
- Semua baris "Augmentasi generatif" selain PROPOSE diisi "–" karena baik Sumber1.md atau Sumber2.md sama-sama gak nemuin generative model (GAN/VAE/Diffusion) dipakai buat traffic augmentation di 11 paper ini — Sumber2.md eksplisit bilang "0 paper (Nol)" buat kategori ini, Sumber1.md nemuin 3 paper generative augmentation TAPI ketiganya (Javeed GAN-DDPG, Diffusion-6G, SpectraGAN) ada di luar 11 paper yang masuk tabel (domain beda: bukan orkestrasi SDN-IoT/mikroservis) — dicatat terpisah di `references-new.bib` kelompok 5, dipakai buat paragraf novelty (T3) bukan baris tabel.
