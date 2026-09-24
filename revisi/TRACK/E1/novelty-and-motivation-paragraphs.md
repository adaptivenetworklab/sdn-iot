# T3 — Paragraf posisi kebaruan (novelty)

Ditempatkan tepat setelah tabel Related Work (`related-work-table.md`).

> While several works address individual aspects of DRL-based network orchestration, none combine them in the configuration this paper targets. OnSlicing integrates a hybrid action space, physical testbed validation, and constrained-RL safety mechanisms within a single end-to-end slicing framework \cite{liu2021onslicing}, and SafeSlice enforces SLA compliance through a learned cost-regressor with Euclidean projection to the nearest safe action \cite{nagib2025safeslice} --- both are close precedents for the safety and physical-validation aspects of this work. However, these systems operate at the RAN/O-RAN control layer, relying on SDR front-ends and server-class compute (USRP, Colosseum, POWDER). Separately, REACH and ChainsFormer manage microservice placement and provisioning within Kubernetes but do not reach into the SDN data plane (OpenFlow flow-table/policing-rate control) governing the network resources those microservices depend on \cite{bai2024reach}, \cite{song2024chainsformer}. The specific combination pursued here --- generative (WGAN-GP) traffic augmentation, direct SDN data-plane orchestration for containerized microservices, and validation on low-cost single-board-computer hardware rather than SDR/server infrastructure --- was not found together in the reviewed corpus.

(≈175 kata. Gak nyebut jumlah paper, gak pakai "first"/"novel" buat komponen tunggal — kebaruan diletakkan pada kombinasi + kelas hardware.)

---

# T4 — Paragraf motivasi testbed fisik

Buat Section I atau III (motivasi kenapa testbed fisik, bukan simulasi murni).

> While simulation and emulation frameworks (e.g., ns-3, Mininet, OMNeT++) provide controlled, reproducible environments for exploring large-scale topologies, they typically abstract away execution-level effects that matter for real-time orchestration decisions: kernel-level packet scheduling latency, container/OS scheduling jitter under resource contention, and the wall-clock inference cost of the orchestration agent itself \cite{bai2024reach}, \cite{b3}. These effects can shift a policy's effective operating point relative to what was observed in simulation. To validate the proposed orchestration policy under these execution-level constraints, this work deploys a physical prototype testbed built from Raspberry Pi single-board computers, Open vSwitch, and the Ryu SDN controller, complementing --- rather than replacing --- the simulation-based results reported elsewhere in the literature.

(≈112 kata, 2 sitasi: `bai2024reach` [REACH, baru] + `b3` [referensi yang UDAH ADA di `main.tex`, "AI Methods in Network Slice Life-Cycle Phases: A Survey" — dipakai ulang, bukan entry baru]. Gak merendahkan simulasi, framing komplementer.)
