# [06] Deep Reinforcement Learning for Dynamic Network Slicing and Resource Orchestration in SD Critical Telecom Infrastructu

> Source file: `[06] Deep Reinforcement Learning for Dynamic Network Slicing and Resource Orchestration in SD Critical Telecom Infrastructu.pdf`

---

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
Deep Reinforcement Learning for Dynamic Network
Slicing and Resource Orchestration in Software-Defined
Critical Telecom Infrastructure
Vincent Onaji Ezekiel Adediji J ustin Njimgou Kehinde Ayano Phd David Olufemi
Dept of Systems McClure School of Zeyeum C o m p uter Science McClure School of
Engineering, Emerging Ohio Dominican Dept, Indiana Wesley Emerging
Purdue Communication University, USA University Communication Tech,
University, USA Technology, Ohio Ohio University
University
Abstract: The proliferation of diverse services in fifth generation (5G) and beyond networks necessitates dynamic, fine-grained
resource management to guarantee strict Quality of Service (QoS) for mission-critical applications. Traditional static resource
allocation models fail to address the highly variable traffic demands and heterogeneous requirements inherent in network slicing (NS)
within a Software-Defined Networking (SDN) framework. This paper proposes a novel framework utilizing Deep Reinforcement
Learning (DRL), specifically a Multi-Agent Deep Deterministic Policy Gradient (MA-DDPG) approach, to achieve autonomous and
optimal resource orchestration for dynamic NS in critical telecom infrastructure. Our proposed DRL agent learns a real-time mapping
between the evolving network state (e.g., slice demand, available resources, and congestion) and optimal resource allocation decisions
(e.g., CPU, memory, and bandwidth allocation across Virtual Network Functions, VNFs). Simulation results, comparing the MA-
DDPG approach against established benchmarks like Greedy and traditional Deep Q-Networks (DQN), demonstrate a significant
improvement in Service Level Agreement (SLA) violation rate reduction, resource utilization efficiency, and slice admission control
performance. This DRL-driven approach is critical for the reliable and efficient operation of future resilient, ultra-low-latency critical
communication systems
Keywords: Deep Reinforcement Learning (DRL), Network Slicing (NS), Resource Orchestration, Software-Defined Networking
(SDN), Critical Telecom Infrastructure, Multi-Agent Systems, Quality of Service (QoS), Deep Deterministic Policy Gradient (DDPG),
1. INTRODUCTION: The Resource Orchestration streaming demands high throughput with fluctuating
Challenge in Sliced SDN peak demand.
The current Management and Orchestration (MANO)
The transition to 5G and 6G networks relies systems, which oversee resource allocation across these
slices, face fundamental limitations:
fundamentally on two paradigm shifts: Software-
1. Complexity: The resource allocation problem is
Defined Networking (SDN) and Network Function
high-dimensional, involving continuous decisions for
Virtualization (NFV) for infrastructure
compute (CPU), memory (RAM), and bandwidth across
programmability, and Network Slicing (NS) for multi- numerous Virtual Network Functions (VNFs) and
tenant isolation and tailored service delivery [1]. physical host nodes.
Critical telecom infrastructure, such as networks 2. Dynamism: Traffic loads, service requests, and
channel conditions change rapidly, often requiring
supporting public safety, industrial control, and remote
resource adjustments within the order of milliseconds.
surgery, demands stringent performance guarantees
3. Conflict: Slices often compete for limited physical
ultra-high reliability, massive connection density, and
resources, necessitating a fair and optimal allocation
ultra-low latency (e.g., <1 ms) [2].
strategy that prioritizes critical services without wasting
resources.
1.1 Background: The Resource Orchestration Manual or heuristic allocation methods are inherently
Challenge in Sliced SDN reactive and sub-optimal, lacking the agility for the
millisecond-level reactions needed to prevent Service
Network Slicing allows a single physical infrastructure
Level Agreement (SLA) violations in critical slices. The
to be logically partitioned into multiple, end-to-end failure to dynamically adapt resource allocation leads to
virtual networks, each optimized for a specific service significant capital expenditure (CapEx) from over-
category, such as enhanced Mobile Broadband (eMBB), provisioning or service outages and SLA penalties from
massive Machine-Type Communications (mMTC), or under-provisioning. An intelligent, self-optimizing
Ultra-Reliable Low-Latency Communications framework is essential to maximize infrastructure
(uRLLC). The challenge lies in the heterogeneity and
utilization while guaranteeing the performance of
dynamism of these services. For example, a uRLLC critical services.
slice supporting remote surgery requires predictable
sub-millisecond latency, while an eMBB slice for video
www.ijcat.com 53

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
1.2 Problem Statement: Dynamic and Autonomous  1.4 Objectives and Contributions
Resource Orchestration
The primary objective of this paper is to develop and
The  core  research  problem  is  the  dynamic  and  evaluate  a  Deep  Reinforcement  Learning-based
autonomous  orchestration  of  virtualized  network  framework  for  dynamic,  autonomous,  and  optimal
resources  (e.g.,  compute,  storage,  and  bandwidth)  resource  orchestration  for  network  slicing  in  critical
across  multiple,  co-existing,  and  often  competing  telecom infrastructure.
| network  slices,  |     | each  with  | diverse  | and  time-varying  |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Quality of Service (QoS) requirements.  This paper makes the following key contributions:
Specifically, the problem is defined as: Designing an  1.  Novel MA-DDPG Formulation: We introduce a
intelligent control plane mechanism capable of learning  novel  Multi-Agent  Deep  Deterministic  Policy
Gradient (MA-DDPG) model specifically tailored
an optimal, real-time resource allocation policy  π(s) →
a  that maps the instantaneous complex network state  for network slicing. Each slice is modeled as an
(s)  to  an  action  (a),  such  that  the  collective  SLA  independent  agent,  utilizing  a  Centralized
|            |               |      |         |                |        |     | Training  | with  | Decentralized  |     | Execution  |     | (CTDE)  |
| ---------- | ------------- | ---- | ------- | -------------- | ------ | --- | --------- | ----- | -------------- | --- | ---------- | --- | ------- |
| violation  | rate  across  | all  | slices  | is  minimized  | while  |     |           |       |                |     |            |     |         |
maintaining high resource utilization efficiency of the  paradigm to manage the joint resource pool while
underlying physical infrastructure.   optimizing individual slice performance.
|                |       |       |      |              |       |     | 2.  Continuous  |     | Action  | Space  | Orchestration:  |     | We  |
| -------------- | ----- | ----- | ---- | ------------ | ----- | --- | --------------- | --- | ------- | ------ | --------------- | --- | --- |
| 1.3  Research  | Gap:  | Need  | for  | Multi-Agent  | Deep  |     |                 |     |         |        |                 |     |     |
Reinforcement Learning  leverage  the  DDPG  algorithm  to  allow  for  a
Existing research often falls short of providing a fully  continuous action space, enabling the DRL agent
autonomous,  scalable,  and  granular  solution  for  this  to  perform  fine-grained,  instantaneous  resource
complex problem:  adjustments  (e.g.,    )  instead  of  coarse,
•  Heuristic/Optimization  Gaps:  Traditional  discrete  block  allocations,  thereby  maximizing
optimization techniques (e.g., Linear Programming,
resource efficiency and minimizing disruption.
| Mixed  | Integer  | Programming)  |     | provide  | optimal  |     |     |     |     |     |     |     |     |
| ------ | -------- | ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
solutions but are computationally intractable for the  3.  Holistic  Reward  Design:  We  design  a  multi-
real-time, high-speed decision-making required in  objective reward function that effectively balances
the competing requirements of guaranteed QoS
5G/6G [3]. Heuristic algorithms are fast but often
yield sub-optimal performance, failing to adapt to
|     |     |     |     |     |     |     | (low  | SLA  | violation  | penalty  |     |   )  and  | high  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ---------- | -------- | --- | --------- | ----- |
unforeseen traffic patterns.
Resource Utilization Efficiency (RUE), a crucial
•  Single-Agent  DRL  Limitations:  While  Deep  trade-off in critical infrastructure management.
| Reinforcement  |     | Learning  |     | (DRL)  has  | shown  |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
promise,  most  existing  DRL  models  employ  a  4.  Comparative  Performance  Validation:  We
Single-Agent  formulation  [4].  This  approach  validate  the  proposed  MA-DDPG  framework
struggles  to  scale  efficiently  as  the  number  of  using a custom simulation environment (DENS-
network slices increases (leading to a combinatorial  Sim) and demonstrate its superior performance in
state-action space explosion) and fails to naturally  terms  of  SLA  violation  rate  reduction  and
capture  the  decentralized  nature  of  resource  resource  utilization  compared  to  traditional
competition  and  cooperation  among  independent  Greedy  allocation  and  centralized  DRL
| slices.  |     |     |     |     |     |     | benchmarks (DQN).  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
•  Lack of Granularity: Solutions that use discrete
action  spaces  (e.g.,  Deep  Q-Networks  or  DQN)  Research Questions (RQs):
| lack  the  | necessary  |     | granularity  | to  perform  | fine- |     |                                                |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------------ | ------------ | ----- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |            |     |              |              |       |     | •  RQ1: How can a Deep Reinforcement Learning  |     |     |     |     |     |     |
grained resource adjustments, which are essential
for minimizing waste and avoiding transient QoS  (DRL)  agent  be  formulated  to  model  the
degradation in critical slices.  dynamic, high-dimensional state-action space of
resource orchestration across multiple concurrent

network slices in an SDN/NFV environment?
This research addresses these gaps by proposing a novel
| framework         | utilizing  | Multi-Agent  |     | Deep  Deterministic  |     |     |          |      |     |              |     |      |           |
| ----------------- | ---------- | ------------ | --- | -------------------- | --- | --- | -------- | ---- | --- | ------------ | --- | ---- | --------- |
|                   |            |              |     |                      |     |     | •  RQ2:  | Can  | a   | Multi-Agent  |     | DRL  | approach  |
| Policy  Gradient  |            | (MA-DDPG).   |     | The  MA-DDPG         |     |     |          |      |     |              |     |      |           |
significantly outperform single-agent or heuristic
| approach  | offers  | a  scalable  |     | architecture  | with  |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------ | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
methods in terms of minimizing SLA violation
| decentralized  | execution  |     | for  faster  | decision-making,  |     |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
while the DDPG foundation provides the crucial ability  rates  and  maximizing  resource  utilization
efficiency for critical slices?
to learn optimal resource allocation from a continuous
action space.
|     |     |     |     |     |     |     | •  RQ3: What is the optimal design for the DRL  |           |     |              |     |                 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --------- | --- | ------------ | --- | --------------- | --- |
|     |     |     |     |     |     |     | reward                                          | function  |     | to  balance  |     | the  competing  |     |

|     |     |     |     |     |     |     | objectives  |     | of  satisfying  |     | heterogeneous  |     | QoS  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | -------------- | --- | ---- |

|                |     |     |     |     |     |     | demands  |     | (latency,  | throughput,  |     | reliability)  | and  |
| -------------- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ------------ | --- | ------------- | ---- |
| www.ijcat.com  |     |     |     |     |     |     |          |     |            |              |     |               | 54   |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
efficiently utilizing the shared physical • eMBB (enhanced Mobile Broadband):
infrastructure? Demands high throughput and capacity (e.g.,
4K/8K video streaming).
2. LITERATURE REVIEW • mMTC (massive Machine-Type
Theoretical Framework and Background Communications): Requires supporting
massive numbers of low-data-rate devices (e.g.,
This chapter establishes the foundational principles of IoT sensors).
The Management and Orchestration (MANO) layer
the critical telecom infrastructure, the virtualization
is the system component responsible for translating
technologies enabling it, and the Deep Reinforcement
service-level slice requests into VNF placements and
Learning (DRL) models used to achieve autonomous
resource assignments within the physical domain. The
resource orchestration. complexity arises from the need for the MANO layer to
simultaneously manage the lifecycle and resource
2.1 Software-Defined Networking (SDN), Network demands of dozens of heterogeneous, interacting slices
Function Virtualization (NFV), and Network Slicing in real-time.
(NS)
The foundation of modern, flexible telecom
infrastructure rests upon the combined principles of
SDN, NFV, and NS [3], [4].
2.1.1 SDN and NFV for Infrastructure Agility
Software-Defined Networking (SDN) fundamentally
transforms network management by decoupling the
control plane from the data plane [3]. This separation
enables the centralization of network intelligence in an
SDN Controller, which provides a programmable
interface for managing the underlying infrastructure.
This capability is vital for dynamic resource adjustment,
as the orchestrator can instantly modify forwarding
rules and resource limits across the entire network
based on policy decisions.
Network Function Virtualization (NFV)
complements SDN by migrating proprietary hardware-
based network functions (e.g., firewalls, load balancers,
Figure 1: Network Slicing on Common Physical
packet gateways) into software applications called
Infrastructure Managed by MANO
Virtual Network Functions (VNFs). VNFs run on
standard commercial off-the-shelf (COTS) servers,
2.2 Reinforcement Learning and the Markov
allowing network services to be deployed, scaled, and
Decision Process (MDP)
managed flexibly and efficiently [8]. The core resource
elements managed are compute (CPU, memory),
Multi-agent systems (MAS) have emerged as a
storage, and network bandwidth.
powerful architectural paradigm for enabling
decentralized and scalable security enforcement in
2.1.2 The Network Slicing Paradigm
modern network infrastructures. In MAS-based
Network Slicing (NS) leverages the flexibility of SDN architectures, individual agents are deployed across
and NFV to create multiple isolated, end-to-end virtual distributed nodes such as customer premises equipment
networks (slices) on a common physical infrastructure (CPE), base stations, or optical line terminals where
[4], [15]. Each slice is tailored to meet the specific and they operate semi-independently while contributing to a
stringent Quality of Service (QoS) requirements of a collective defense strategy. These agents observe local
particular service class. In critical infrastructure, three traffic conditions, detect potential anomalies, and
dominant slice types exist: collaborate to update global policies without
centralizing sensitive data. The MAS paradigm is
particularly well-suited for broadband environments,
• uRLLC (ultra-Reliable Low-Latency
where edge diversity, latency constraints, and data
Communications): Requires extreme
privacy must all be simultaneously addressed (Zhou et
reliability and latency below 1 ms (e.g.,
al., 2022).
industrial automation, telemedicine) [2].
www.ijcat.com 55

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
The  problem  of  dynamic  resource  orchestration,  approximators for the value function V(s) or the policy
| characterized  | by  sequential  | decision-making  | in  | a  (s) [21].  |     |     |     |     |
| -------------- | --------------- | ---------------- | --- | ------------- | --- | --- | --- | --- |
stochastic environment, is naturally modeled using the
Reinforcement Learning (RL) paradigm [5], [24].  One of the earliest and most impactful DRL algorithms
is Deep Q-Networks (DQN) [24], which approximates
2.2.1. The Markov Decision Process (MDP)  the Q-function   using a DNN. The Q-value is
updated based on the Temporal Difference (TD) error
RL is founded on the Markov Decision Process (MDP),
using the target network concept:
| a  mathematical  | framework  | for  modeling  | sequential  |     |     |     |     |     |
| ---------------- | ---------- | -------------- | ----------- | --- | --- | --- | --- | --- |
decision-making. The MDP is formally defined by the

| tuple  |     |     |     |               |                                 |     |     |     |
| ------ | --- | --- | --- | ------------- | ------------------------------- | --- | --- | --- |
|        |     |     |     | The TD-error  |  for a value function V(s) is:  |     |     |     |

Where:
|     |     |     |     | The DRL agent  | stores experienced transitions in an  |     |     |     |
| --- | --- | --- | --- | -------------- | ------------------------------------- | --- | --- | --- |
experience replay memory D:
•  S is the finite set of states (the network conditions
and slice demands).

| •  A  | is  the  finite  set  | of  actions  | (the  resource  |     |     |     |     |     |
| ----- | --------------------- | ------------ | --------------- | --- | --- | --- | --- | --- |
allocation decisions).
| P  is  the  | state  transition  | probability  | function,  |     |     |     |     |     |
| ----------- | ------------------ | ------------ | ---------- | --- | --- | --- | --- | --- |
, representing the probability of transitioning
from state s to state s' after taking action a.
•  R is the reward function, R(s, a), quantifying the
immediate benefit or cost of taking action a in
state s.
| •   |   is the discount factor, balancing the  |     |     |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
importance of immediate versus future rewards.
| The agent's goal is to find an optimal policy  |                |             |             |     |     |     |     |     |
| ---------------------------------------------- | -------------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| that  maximizes                                | the  expected  | cumulative  | discounted  |     |     |     |     |     |
reward, or the Return (G).
t

The Bellman optimality equation for the optimal value

function V*(s) is:
Figure 2: Deep Deterministic Policy Gradient (DDPG)
Architecture

2.3 Deep Deterministic Policy Gradient (DDPG)
The Bellman optimality equation for the optimal action- For our resource orchestration problem, the action space
value function  is:  (e.g., the exact percentage change in CPU allocation) is
continuous. DQN is limited to discrete action spaces.
|     |     |     |     | Therefore,    | we  utilize  | Policy         | Gradient  methods,  |     |
| --- | --- | --- | --- | ------------- | ------------ | -------------- | ------------------- | --- |
|     |     |     |     | specifically  | Deep         | Deterministic  | Policy  Gradient    |     |
|     |     |     |     | (DDPG) [6].   |              |                |                     |     |

2.2.2 Deep Reinforcement Learning (DRL)
DDPG is an off-policy, Actor-Critic algorithm designed
for continuous control.
In network orchestration, the state space (e.g., resource

utilization metrics, traffic statistics, QoS metrics across
|              |                   |              |              | •  2.3.1. Actor-Critic Architecture  |          |       |               |      |
| ------------ | ----------------- | ------------ | ------------ | ------------------------------------ | -------- | ----- | ------------- | ---- |
| N  slices)   | and  the  action  | space  are   | often  high- |                                      |          |       |               |      |
|              |                   |              |              | •  Actor                             | Network  | ( ):  | Approximates  | the  |
| dimensional  | or  continuous.   | Traditional  | tabular  RL  |                                      |          |       |               |      |
methods  cannot  handle  this  complexity.  Deep  deterministic policy  , which maps the state
Reinforcement Learning (DRL) resolves this by using  s directly to a specific continuous action a.
| Deep           | Neural  Networks  | (DNNs)  | as  function  |     |     |     |     |     |
| -------------- | ----------------- | ------- | ------------- | --- | --- | --- | --- | --- |
| www.ijcat.com  |                   |         |               |     |     |     |     | 56  |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
•  Critic Network (Q): Approximates the action- MA-DDPG operates on the Centralized Training with
value  function  ,  which  estimates  the  Decentralized Execution (CTDE) paradigm [7], which
expected return from taking action a in state s.  is  highly  effective  for  cooperative  tasks  in  non-
| The deterministic policy  |     |  is derived by:  |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stationary environments:

•  Decentralized Execution: Each agent i makes

decisions solely based on its local observation

|                         |     |     |     |     |     |     | x using its individual actor  |     |     |     | . This  |
| ----------------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ------- |
| 2.3.2 Learning Updates  |     |     |     |     |     |     | i                             |     |     |     |         |
ensures fast, scalable reaction times.
The Critic is trained by minimizing the Mean Squared
|     |     |     |     |     |     |     | •  Centralized Training: A centralized critic  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
Error (MSE) between the predicted Q-value and the  for each agent utilizes the joint observation
target value y:
|     |     |     |     |     |     |     |     |     |   and  | the  joint  | action  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ------- |
 of all N agents. This global
|     |     |     |     |     |     |     | view  | allows  the  | critic  | to  resolve  | non- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ------- | ------------ | ---- |
stationarity and coordinate the agents' actions
|     |     |     |     |     |     |     | effectively  | [11].                           | The  | experience  | replay  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------------------- | ---- | ----------- | ------- |
|     |     |     |     |     |     |     | memory       |  stores the joint transitions:  |      |             |         |
where y is the target value calculated using the target

networks [6]:

The centralized critic is updated using the loss function:

| The Actor is  | updated using the deterministic policy  |     |     |     |     |     |     |     |     |     |     |
| ------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

gradient, which guides the actor's parameters \theta^\mu

in the direction that maximizes the estimated Q-value
from the critic:  where the target y integrates the rewards and future
|     |     |     |     |     |     | estimated Q-values based on the joint policies  |     |     |     |     | :   |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |

|             |           |             |       |          |       |           |            |                 |              |                |            |
| ----------- | --------- | ----------- | ----- | -------- | ----- | --------- | ---------- | --------------- | ------------ | -------------- | ---------- |
|             |           |             |       |          |       | The       | actor  is  | updated  using  | the          | deterministic  | policy     |
|             |           |             |       |          |       | gradient  | based      | on  the         | centralized  | critic's       | estimate,  |
| To  ensure  | training  | stability,  | DDPG  | employs  | soft  |           |            |                 |              |                |            |
updates for the target networks \theta' (which are copies  ensuring global cooperation:
| of the main networks used to compute the target y):  |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.4.2. Resource Cost Metric

|        |                            |     |     |     |     | To           | efficiently  | guide  the       | agents              | toward  | maximizing  |
| ------ | -------------------------- | --- | --- | --- | --- | ------------ | ------------ | ---------------- | ------------------- | ------- | ----------- |
| where  |  is the soft update rate.  |     |     |     |     |              |              |                  |                     |         |             |
|        |                            |     |     |     |     | utilization  |              | and  minimizing  | over-provisioning,  |         | the         |
reward function must incorporate the resource cost [10].
|     |     |     |     |     |     | A   | weighted  | sum  | of  allocated  |     | resources  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------------- | --- | ---------- |
 for slice i is used as a
2.4 Multi-Agent Deep Deterministic Policy Gradient
|     |     |     |     |     |     | foundational cost metric  |     |     | :   |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
(MA-DDPG)

| The resource orchestration challenge involves multiple  |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
slice agents competing for shared resources, creating a  This cost factor is incorporated into the full reward
cooperative environment where the optimal action of  function  to  penalize  over-allocation.  The  overall
one  agent  depends  on  the  actions  of  all  others.  To  resource constraint must be maintained:
| address this, we extend DDPG to the Multi-Agent Deep  |              |           |       |                |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------ | --------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| Deterministic Policy Gradient (MA-DDPG) framework     |              |           |       |                |     |     |     |     |     |     |     |
| [7], [16].                                            |              |           |       |                |     |     |     |     |     |     |     |
|                                                       |              |           |       |                |     |     |     |     |     |     |     |
| 2.4.1.                                                | Centralized  | Training  | with  | Decentralized  |     |     |     |     |     |     |     |
Execution (CTDE)
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     | 57  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
| 3.  METHODOLOGY  |     |     | AND  | EXPERIMENTAL  |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SETUP
This chapter details the system model, formally defines
the resource orchestration problem within the Multi-
| Agent  | Deep  | Reinforcement  |     | Learning  |     | (DRL)  |     |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
framework, and describes the experimental environment
| and  simulation  |     | setup  used  | to  | evaluate  | the  | proposed  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
approach.
3.1. System Model and Problem Formulation
We model the critical telecom infrastructure as a shared
pool of physical resources hosting a set of dynamic
| network     | slices,  | constituting  |         | a  complex  |     | resource     |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------------- | ------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| allocation  | problem  | under         | strict  | Quality     |     | of  Service  |     |     |     |     |     |     |     |     |
(QoS) constraints [10].
We model the critical telecom infrastructure as a shared
| pool of physical resources hosting a set of dynamic  |          |               |     |             |     |           |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | -------- | ------------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| network                                              | slices,  | constituting  |     | a  complex  |     | resource  |     |     |     |     |     |     |     |     |
Figure 3: Physical Infrastructure Model in Virtualized
| allocation  | problem  | under  | strict  | Quality  |     | of  Service  |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------ | ------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Environment
(QoS) constraints [10].
3.1.2. Network Slice and Request Model
3.1.1. Physical Infrastructure Model
|                              |     |     |     |                          |     |     |     | A set of N network slices  |     |     |     |     |  are active  |     |
| ---------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | -------------------------- | --- | --- | --- | --- | ------------ | --- |
| The physical infrastructure  |     |     |     |  is assumed to be fully  |     |     |     |                            |     |     |     |     |              |     |
in the system, where N varies over time due to dynamic
virtualized and consists of the aggregate resources of a
|             |         |     |         |                   |     |       |     | arrivals  | and  | departures  |     | [2].  Each  | slice  | is  |
| ----------- | ------- | --- | ------- | ----------------- | --- | ----- | --- | --------- | ---- | ----------- | --- | ----------- | ------ | --- |
| core  data  | center  | or  | a  set  | of  Multi-access  |     | Edge  |     |           |      |             |     |             |        |     |
characterized by:
| Computing  | (MEC)  | nodes  | [12].  | The  | total  | available  |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ------ | ---- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
resources are partitioned into three fundamental types:  •  Time-Varying  Demand:  An  instantaneous
|     |                                    |     |     |     |     |     |     | resource  |     |     |     | demand  |     | vector  |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------- | --- | ------- |
| •   | Compute (CPU, measured in cores):  |     |     |     |     |     |     |           |     |     |     |         |     |         |
 is generated based on
•  Memory (RAM, measured in GB):    simulated  traffic  load  and  reflects  the  required
|     |     |     |     |     |     |     |     | resources  |     | for  | the  | slice's  Virtual  | Network  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ---- | ----------------- | -------- | --- |
Functions (VNFs) [19].
•  Bandwidth (Network throughput, measured in
|     | Gbps):  |     |     |     |     |     |     |                      |                |               |     |                    |              |          |
| --- | ------- | --- | --- | --- | --- | --- | --- | -------------------- | -------------- | ------------- | --- | ------------------ | ------------ | -------- |
|     |         |     |     |     |     |     |     | •  QoS               | Requirements:  |               |     | Minimum  required  |              | QoS  is  |
|     |         |     |     |     |     |     |     | defined by a vector  |                |               |     |                    |              | , where  |
|     |         |     |     |     |     |     |     |                      |   is           | the  maximum  |     | tolerable          | latency      | and      |
|     |         |     |     |     |     |     |     |                      |   is           | the  minimum  |     | required           | throughput.  |          |
Critical slices (uRLLC) have significantly lower
 (e.g., 1 ms) [13].
|     |     |     |     |     |     |     |     | The       | allocation  | vector  |                      | for  slice  i  | at  time  | t  is    |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | -------------------- | -------------- | --------- | -------- |
|     |     |     |     |     |     |     |     |           |             |         | ,                    | where          |           | is  the  |
|     |     |     |     |     |     |     |     | resource  |             |         |  allocated to slice  |                | .         |          |
3.1.3. Optimization Objective and Constraints
The overall objective is to find an optimal resource
|                |     |     |     |     |     |     |     | allocation policy             |     |     |     |  that maximizes the expected  |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
|                |     |     |     |     |     |     |     | cumulative discounted reward  |     |     |     | , which is equivalent to      |     |     |
| www.ijcat.com  |     |     |     |     |     |     |     |                               |     |     |     |                               |     | 58  |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
minimizing the overall SLA violation penalty    •  :  Observed  QoS
while maximizing resource utilization   [10], [17].  metrics (Latency and Throughput).
The global optimization objective, rooted in the Markov  •  :  Instantaneous
Decision Process (MDP) framework, is:
resource demand/traffic prediction for slice
[33].
|     |     |     |     | •   |     | :  QoS  | requirement  |
| --- | --- | --- | --- | --- | --- | ------- | ------------ |

vector, providing context to the agent on the
The primary capacity constraint ensures that the total
criticality of the slice.
allocated resources do not exceed the available physical
| capacity for each resource type  |     |  at any time  | :   |                   |                                       |     |     |
| -------------------------------- | --- | ------------- | --- | ----------------- | ------------------------------------- | --- | --- |
|                                  |     |               |     | The global state  |  includes all local observations and  |     |     |
the remaining capacity:

Where

,
The resource allocation must also satisfy a minimum
| viable  allocation  | constraint  |   for  admitted  | slices,  |     |     |     |     |
| ------------------- | ----------- | ---------------- | -------- | --- | --- | --- | --- |
is the vector of unallocated resources. This global state
| ensuring  VNF  | functionality  | and  preventing  | resource  |     |     |     |     |
| -------------- | -------------- | ---------------- | --------- | --- | --- | --- | --- |
is crucial for the centralized critic to understand the
oscillation:
|     |     |     |     | overall  | resource  scarcity  | and  inter-slice  | competition  |
| --- | --- | --- | --- | -------- | ------------------- | ----------------- | ------------ |
[18].

3.2.2. Continuous Action Space Definition (A)

|     |     |     |     | The  action  | a  i for  agent  | i  is  a  continuous  | vector  |
| --- | --- | --- | --- | ------------ | ---------------- | --------------------- | ------- |
3.2.  MA-DDPG  Agent  Design  for  Resource  representing the change in resource allocation   for
Orchestration
|     |     |     |     | the next time step  | . The continuous nature of the  |     |     |
| --- | --- | --- | --- | ------------------- | ------------------------------- | --- | --- |
action space, a hallmark of DDPG [6], provides the
The dynamic resource allocation problem is modeled as
|     |     |     |     | granularity  | needed  | for  precise,  | non-disruptive  |
| --- | --- | --- | --- | ------------ | ------- | -------------- | --------------- |
a cooperative multi-agent system where N agents (one
adjustments [23].
for each active slice) seek to maximize their individual
| rewards,  which  | are  coupled  | by  the  global  | resource  |     |     |     |     |
| ---------------- | ------------- | ---------------- | --------- | --- | --- | --- | --- |

| constraints, leveraging the  |     | Centralized Training  | with  |     |     |     |     |
| ---------------------------- | --- | --------------------- | ----- | --- | --- | --- | --- |
Decentralized Execution (CTDE) paradigm [7], [16].
where the change is constrained to a range:
| 3.2.1. State Space Formulation (S)  |        |                   |               |     |     | .   |     |
| ----------------------------------- | ------ | ----------------- | ------------- | --- | --- | --- | --- |
| The  environment                    | state  |   is  the  input  | to  the  DRL  |     |     |     |     |
The actual new allocation is calculated as:
| system. We define both the local observation  |     |     | for  |     |     |     |     |
| --------------------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
each  Actor  (decentralized  execution)  and  the  global  To guarantee action validity and stability, a constrained
state   for the Centralized Critic (centralized training).  activation  function  (e.g.,  a  normalized  hyperbolic
|     |     |     |     | tangent  | or  sigmoid  \sigma)  | is  used  | in  the  Actor  |
| --- | --- | --- | --- | -------- | --------------------- | --------- | --------------- |
The  local  observation    for  agent    is  a  vector  network's output layer:
capturing slice-specific information:
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Multi-Objective Reward Function (R)
Where:
The reward function R for agent i is critically important
i
•  :  Current  resource  as it shapes the learned policy (RQ3). It captures the
competing objectives of QoS guarantee and resource
| allocation to slice  |     | .   |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
| www.ijcat.com        |     |     |     |     |     |     | 59  |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
| efficiency,  | weighted  | by  importance  | factors  |     |     |     |     |     |
| ------------ | --------- | --------------- | -------- | --- | --- | --- | --- | --- |
 [29].

| 1.  SLA Violation Penalty  |     |     | : This term applies  |     |     |     |     |     |
| -------------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
a severe penalty if the slice violates its latency or
throughput requirements. The penalty is scaled by
| the  | degree  of  violation  | for  | smooth  gradient  |     |     |     |     |     |
| ---- | ---------------------- | ---- | ----------------- | --- | --- | --- | --- | --- |
learning:

| 2.  Resource  | Cost  | Penalty  | :  This  term  |     |     |     |     |     |
| ------------- | ----- | -------- | -------------- | --- | --- | --- | --- | --- |

encourages efficient usage by penalizing the total
resources currently allocated to the slice [10]:  Figure  1:  MA-DDPG  Orchestration  System
Architecture
|     |     |     |     | 3.3.  | Experimental  |     | Setup  and  | Simulation  |
| --- | --- | --- | --- | ----- | ------------- | --- | ----------- | ----------- |

Environment
| where  |   are  cost  | weights  reflecting  | the  relative  |     |     |     |     |     |
| ------ | ------------ | -------------------- | -------------- | --- | --- | --- | --- | --- |
3.3.1. Discrete-Event Network Slice Simulator (DENS-
expense or scarcity of resource r.
Sim)
3.  Slice Admission Reward  : A large,  We developed a custom Discrete-Event Network Slice
positive reward granted only upon the successful  Simulator (DENS-Sim) using Python, integrated with
|     |     |     |     | the  | OpenAI  | Gym  | framework  to  model  | the  non- |
| --- | --- | --- | --- | ---- | ------- | ---- | --------------------- | --------- |
initial admission of slice i. This incentivizes the
stationary, competitive network environment [20].
orchestrator to accept new profitable requests when
capacity is prudently managed.
Key Modeling Features:
| The total reward            |  passed to the centralized critic is the  |     |               |     |                                                 |     |     |     |
| --------------------------- | ----------------------------------------- | --- | ------------- | --- | ----------------------------------------------- | --- | --- | --- |
|                             |                                           |     |               |     | •  Network Topology: Models a simplified three- |     |     |     |
| sum of individual rewards,  |                                           |     | . To prevent  |     |                                                 |     |     |     |
tier network (Access, Aggregation, Core) hosting
high resource volatility, a penalty for the magnitude of
the VNFs.
| resource change  |  can also be added for stability [34]:  |     |     |     |                                                    |     |     |     |
| ---------------- | --------------------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
|                  |                                         |     |     |     | •  Traffic Model: Simulates heterogeneous traffic  |     |     |     |
generation. uRLLC traffic uses low-volume, time-
|     |     |     |     |     | sensitive Poisson arrivals. eMBB uses a heavy- |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
tailed (e.g., Pareto) distribution to mimic sudden
traffic surges and drops. mMTC uses a massive
number of sporadic, low-rate connections. This
mixed traffic profile introduces high volatility and
stress [33].
|     |     |     |     |     | •  QoS Calculation: Latency L(t) is modeled as a  |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
i
function of allocated resources and current traffic
|     |     |     |     |     | load,  | incorporating  | queuing  delay,  | processing  |
| --- | --- | --- | --- | --- | ------ | -------------- | ---------------- | ----------- |
delay, and propagation delay [28]:

| www.ijcat.com  |     |     |     |     |     |     |     | 60  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
| The  queuing  | delay  |   is  approximated  | using  | a   |     |     |     |     |
| ------------- | ------ | ------------------- | ------ | --- | --- | --- | --- | --- |
 model extension for VNF processing and is the
primary variable controlled by resource allocation. The
| latency  metric  | for  slice  | i  is  the  average  | observed  |     |     |     |     |     |
| ---------------- | ----------- | -------------------- | --------- | --- | --- | --- | --- | --- |
latency:

|     |     |     |     | Figure  | 2:  MA-DDPG  | Agent  | Neural  | Network  |
| --- | --- | --- | --- | ------- | ------------ | ------ | ------- | -------- |
Structure

3.3.3. Training and Hyperparameters

Figure  1:  DENS-Sim  Architecture  (Python-based,  The training process utilized off-policy learning with
mini-batch updates sampled from the experience replay
integrated with OPENI-Gym)
|     |     |     |     | buffer   [14].  |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
3.3.2. Neural Network Architecture
|     |     |     |     | Parameter  | Value/Range  | Unit  | Description  |     |
| --- | --- | --- | --- | ---------- | ------------ | ----- | ------------ | --- |
Below diagram showing the specific architecture of the
Actor  and  Centralized  Critic.  The  Actor  Network  Simulation  DRL  decision  interval
|                 |              |             |             |            | 10  | Seconds  |                             |     |
| --------------- | ------------ | ----------- | ----------- | ---------- | --- | -------- | --------------------------- | --- |
|                 |              |             |             | Time Step  |     |          | (orchestration frequency).  |     |
| (Input:  Local  | Observation  | ,  Output:  | Continuous  |            |     |          |                             |     |
Action  ) is a multi-layer perceptron (MLP) with three  Episode  Time  Total  simulated  period  per
1000
|                 |        |                   |              | Length (T)      |     | Steps  | training run (approx. 10 hours).  |                         |
| --------------- | ------ | ----------------- | ------------ | --------------- | --- | ------ | --------------------------------- | ----------------------- |
| hidden  layers  | (256,  | 128,  64  nodes)  | using  ReLU  |                 |     |        |                                   |                         |
|                 |        |                   |              | Total Physical  |     |        | Physical                          | compute  capacity  for  |
activation and a final layer with Tanh activation, scaled  128  Cores
|                                       |     |     |     | CPU    |     |     | the resource pool.  |     |
| ------------------------------------- | --- | --- | --- | ------ | --- | --- | ------------------- | --- |
| to map the output to the valid range  |     |     |     | .      |     |     |                     |     |
The Centralized Critic Network (Input: Joint State    Maximum  latency  requirement
|     |     |     |     | uRLLC  |   1.0  | ms  |     |     |
| --- | --- | --- | --- | ------ | ------ | --- | --- | --- |
for critical slice.
| and Joint Action  | , Output: Q-value  |     |     |     |     |     |          |             |
| ----------------- | ------------------ | --- | --- | --- | --- | --- | -------- | ----------- |
|                   |                    |     |     |     |     |     | Minimum  | throughput  |
is a deeper MLP (512, 256, 128 nodes), also utilizing  eMBB    500  Mbps
requirement for data slice.
ReLU activation.
DRL Discount
Controls the importance of long-
|     |     |     |     |               | 0.99   | -   |                       |                         |
| --- | --- | --- | --- | ------------- | ------ | --- | --------------------- | ----------------------- |
|     |     |     |     | Factor        |        |     | term rewards [5].     |                         |
|     |     |     |     | Soft  Update  |        |     | Controls              | the  update  speed  of  |
|     |     |     |     |               | 0.001  | -   |                       |                         |
|     |     |     |     | Rate          |        |     | target networks [6].  |                         |
|     |     |     |     |               |        |     | Capacity              | of  the  experience     |
Replay Buffer
Transitions memory
Size
   [7].
|     |     |     |     |             |       |              | Number  | of  samples  used  for  |
| --- | --- | --- | --- | ----------- | ----- | ------------ | ------- | ----------------------- |
|     |     |     |     | Batch Size  | 1024  | Transitions  |         |                         |
each gradient update.
|     |     |     |     | Learning Rate  |     |     | Standard  | Adam  optimizer  |
| --- | --- | --- | --- | -------------- | --- | --- | --------- | ---------------- |
-
|     |     |     |     | (Actor/Critic)  |     |     | learning rates [6].  |     |
| --- | --- | --- | --- | --------------- | --- | --- | -------------------- | --- |

| www.ijcat.com  |     |     |     |     |     |     |     | 61  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
3.3.4. Benchmarking Algorithms
| The  performance  | of  | the  MA-DDPG  | approach  | is  |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- |

benchmarked against two standard resource allocation
| strategies:  |     |     |     |     | 4.  SIMULATION AND ANALYSIS  |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |

1.  Greedy  Allocation:  A  heuristic  method  that  This  chapter  provides  a  detailed  exposition  of  the
processes slice requests sequentially. It allocates  simulation environment setup, the training process, the
the requested resources   if available. It is  convergence  properties  of  the  proposed  Multi-Agent
purely reactive and has no mechanism for future  Deep  Deterministic  Policy  Gradient  (MA-DDPG)
prediction, preemption, or optimization.  framework, and the key performance metrics used for
comparative analysis.
2.  Centralized Deep Q-Network (DQN): A single-
agent DRL approach [24]. The state is the global  4.1.  Simulation  Environment  and  Calibration
(DENS-Sim)
| state  , and the action space is discretized (e.g.,  |     |     |                |     |                  |     |     |      |           |          |
| ---------------------------------------------------- | --- | --- | -------------- | --- | ---------------- | --- | --- | ---- | --------- | -------- |
| increasing/decreasing resource by                    |     |     |  for a single  |     |                  |     |     |      |           |          |
|                                                      |     |     |                |     | The  evaluation  |     | of  | the  | proposed  | MA-DDPG  |
slice). This tests the advantage of the multi-agent  orchestration policy is performed within the Discrete-
| architecture  | and  | the  continuous  | action  space  |     |     |     |     |     |     |     |
| ------------- | ---- | ---------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Event Network Slice Simulator (DENS-Sim), a custom-
(RQ2).
built tool that accurately models the complex, dynamic
interactions between network slices and shared physical

resources in an SDN/NFV environment [20], [32].
3.4. Additional Mathematical Relations

| The Average Resource Utilization Efficiency  |     |     | is a  |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
4.1.1. Infrastructure and Resource Capacity Modeling
key performance indicator (KPI) calculated over the
testing duration T:  The  DENS-Sim  environment  was  calibrated  to
|     |     |     |     |     | represent    | a  typical  | high-capacity  |           | Multi-access  | Edge         |
| --- | --- | --- | --- | --- | ------------ | ----------- | -------------- | --------- | ------------- | ------------ |
|     |     |     |     |     | Computing    | (MEC)       | host           | or        | a  regional   | cluster  of  |
|     |     |     |     |     | virtualized  | resources,  |                | enabling  | edge-based    | critical     |

|     |     |     |     |     | services  | [12]. The  | physical  |     | resource  | capacities  were  |
| --- | --- | --- | --- | --- | --------- | ---------- | --------- | --- | --------- | ----------------- |
explicitly set based on common industry deployments:
| The overall Total Penalty  |     |     |  observed by the  |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
centralized critic is the sum of individual penalties:  •  Total CPU Cores  : 128 Cores.
|     |     |     |     |     | •   | Total RAM        |     | : 512 GB.  |              |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ------------ | --- |
|     |     |     |     |     | •   | Total Bandwidth  |     |            | : 100 Gbps.  |     |

|     |     |     |     |     | The time step for DRL decision-making,  |     |     |     |     | , was set to  |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | ------------- |
10 seconds. This interval is crucial, representing the
To enforce exploration in the continuous action space,
frequency at which the orchestration layer collects new
the Actor's output is perturbed by time-correlated noise
,  often  implemented  via  the  Ornstein-Uhlenbeck  state information and applies the resource allocation
|     |     |     |     |     | action  |     | ,  balancing  |     | the  need  | for  real-time  |
| --- | --- | --- | --- | --- | ------- | --- | ------------- | --- | ---------- | --------------- |
(OU) process:
responsiveness with computational feasibility.

4.1.2. Dynamic Slice and Traffic Modeling
The TD Target (y) in the critic update is explicitly
To ensure the simulation reflects realistic, challenging
| calculated using the target networks  |     |     | :   |     |              |            |     |                |                  |        |
| ------------------------------------- | --- | --- | --- | --- | ------------ | ---------- | --- | -------------- | ---------------- | ------ |
|                                       |     |     |     |     | operational  | scenarios  |     | for  critical  | infrastructure,  | three  |
heterogeneous network slices were modeled [15]:

The policy \pi must be learned to maximize the total
expected return:
| www.ijcat.com  |     |     |     |     |     |     |     |     |     | 62  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
|     |     |     |     |     | assumed  | minimal  | (due  to  VNF  | pre-instantiation),  |     |
| --- | --- | --- | --- | --- | -------- | -------- | -------------- | -------------------- | --- |
Primary  QoS  making    the  primary  variable  controlled  by
| Slice Type  | Traffic Model  |     | Allocation Ratio  |     |     |     |     |     |     |
| ----------- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Requirement
|     |     |     |     |     | resource allocation. The observed throughput  |     |     |                 |  is  |
| --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --------------- | ---- |
|     |     |     |     |     | capped by the allocated bandwidth             |     |     |  and inversely  |      |
Low  volume,
|        |         | Latency  |     |     | related  | to  congestion  | caused  | by  low  |   (VNF  |
| ------ | ------- | -------- | --- | --- | -------- | --------------- | ------- | -------- | ------- |
| uRLLC  | highly  |          |     |     |          |                 |         |          |         |
30% of total slices
| (Critical)  | sporadic  |     |     |     | processing bottleneck).  |     |     |     |     |
| ----------- | --------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
ms
Poisson bursts
|     | Heavy-tailed  | Throughput  |     |     |     |     |     |     |     |
| --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
eMBB  (High
|     | (Pareto)  |     | 50% of total slices  |     |     |     |     |     |     |
| --- | --------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Throughput)
distribution
Mbps
Consistent,
mMTC
low-rate traffic Connection
| (Massive  |     |     | 20% of total slices  |     |     |     |     |     |     |
| --------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
from numerous Density
IoT)
sources

| The Slice Arrival Rate  |     |     |  was dynamically varied  |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
between 5 to 15 new slice requests per hour (modeled
as a Poisson process), introducing non-stationarity and
the critical problem of dynamic slice admission and

| termination.  | The  | load  patterns  | included  | diurnal  |     |     |     |     |     |
| ------------- | ---- | --------------- | --------- | -------- | --- | --- | --- | --- | --- |
variations (low activity overnight, peak activity during
Figure 2: QQS Calculation Model in DENS-Sim
business hours) and sudden traffic surges (modeled as
short, high-intensity Pareto spikes in the eMBB slice  4.2. Training and Convergence Analysis
demand), which are designed to stress the orchestration
The MA-DDPG framework was trained iteratively over
| system  | and  force  | pre-emptive  | resource  | reallocation  |     |     |     |     |     |
| ------- | ----------- | ------------ | --------- | ------------- | --- | --- | --- | --- | --- |
500 episodes, each representing 10 simulated hours of
[28].
network operation (1000 time steps).

4.2.1. DRL Training Parameters
4.1.3. QoS and Delay Modeling
The stability and convergence of the continuous-action
| The  observed  |     | QoS  metrics:     | latency     |   and   |       |            |          |           |          |
| -------------- | --- | ----------------- | ----------- | ------- | ----- | ---------- | -------- | --------- | -------- |
|                |     |                   |             |         | DDPG  | algorithm  | heavily  | rely  on  | careful  |
| throughput     |     | are  dynamically  | calculated  | within  |       |            |          |           |          |
hyperparameter tuning [6]:
| DENS-Sim based on the instantaneous allocation  |     |     |                          |     |                  |        |                                     |             |            |
| ----------------------------------------------- | --- | --- | ------------------------ | --- | ---------------- | ------ | ----------------------------------- | ----------- | ---------- |
| and the current traffic load                    |     |     | .                        |     |                  |        |                                     |             |            |
|                                                 |     |     |                          |     | Parameter        | Value  | Description                         |             |            |
|                                                 |     |     |                          |     | Discount Factor  |        | High  value                         | emphasizes  | long-term  |
| The total observed latency                      |     |     |  for slice i is modeled  |     |                  |        |                                     |             |            |
|                                                 |     |     |                          |     |                  | 0.99   | performance and SLA adherence over  |             |            |

as the sum of propagation  , processing  ,  immediate gains [5].
and queuing delays   [28]:  Small    ensures  stable  updates  to
|     |     |     |     |     | Soft  | Update  |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- |
0.001
|     |     |     |     |     | Rate    |     | target networks, preventing oscillation  |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ---------------------------------------- | --- | --- |
during training [6].

|     |     |     |     |     |         |         | Large  buffer  | size  ensures  | the  off- |
| --- | --- | --- | --- | --- | ------- | ------- | -------------- | -------------- | --------- |
|     |     |     |     |     | Replay  | Buffer  |                |                |           |
policy sampling diversity needed for
| The processing delay  |          |  is inversely related to the  |                |      | Size  |     |                 |     |     |
| --------------------- | -------- | ----------------------------- | -------------- | ---- | ----- | --- | --------------- | --- | --- |
|                       |          |                               |                |      |       |     |   MA-DDPG [7].  |     |     |
| allocated             | compute  | resources                     | ,  reflecting  | VNF  |       |     |                 |     |     |
Large batch size for robust gradient
|     |     |     |     |     | Batch Size  | 1024  |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | --- |
estimation and stability.
| processing  | capacity.  | The  queuing  | delay  |     | is  |     |     |     |     |
| ----------- | ---------- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
Used to encourage exploration in the
inversely  related  to  allocated  bandwidth    and  Ornstein-
|     |     |     |     |     | Exploration  |     | continuous  | action  space,  | annealed  |
| --- | --- | --- | --- | --- | ------------ | --- | ----------- | --------------- | --------- |
Uhlenbeck
positively related to the incoming traffic rate    Noise  from 0.5 to 0.05 over 400 episodes
Process
| [31]. For critical uRLLC slices,  |     |     |  and  |  are  |     |     | [6].  |     |     |
| --------------------------------- | --- | --- | ----- | ----- | --- | --- | ----- | --- | --- |
| www.ijcat.com                     |     |     |       |       |     |     |       |     | 63  |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
|     |     |     |     |     |     |     |     |     | 1.  SLA  Violation  |         | Rate  (SVR):  | This        | is  the  most  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ------- | ------------- | ----------- | -------------- |
|     |     |     |     |     |     |     |     |     | critical            | metric  | for  the      | evaluation  | of  critical   |
4.2.2. Learning Stability and Convergence
infrastructure [28]. It is defined as the percentage
The Total Cumulative Reward per Episode serves as  of all time steps (T) where at least one active
|     |     |     |     |     |     |     |     |     | slice  |  violates its defined  |     |  requirement:  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------- | --- | -------------- | --- |
the primary metric for analyzing the learning progress.

|     |     |     |     |     |     |     |     |     | 2.  Slice  | Admission  | Ratio  | (SAR):  | Measures  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------ | ------- | -------------- |
system's ability to maximize revenue/utility by
accepting new slice requests:
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Graph 1: Convergence of Training
Above, a graph showing the moving average of the
| Total  Cumulative  |        | Reward     | per       | Episode    | for  | the  MA- |     |     |     |     |     |     |     |
| ------------------ | ------ | ---------- | --------- | ---------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
| DDPG               | agent  | over  500  | training  | episodes.  | The  | curve    |     |     |     |     |     |     |     |
demonstrates three distinct learning phases: Phase I (0-
100 episodes): Steep, rapid growth in reward, indicating
efficient initial exploration and finding basic feasible
resource policies. Phase II (100-350 episodes): Slower,
more volatile improvement as the agent fine-tunes the
| policy,   | balancing  | the       | complex   | trade-off  |      | between   |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | --------- | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
| resource  | cost       | and  SLA  | penalty.  | Phase      | III  | (350-500  |     |     |     |     |     |     |     |
episodes): Stable convergence to a near-optimal policy,
where the reward plateau demonstrates the agent has
| learned  | an  effective  | and  | reproducible  |     | orchestration  |     |     |     |     |     |     |     |     |
| -------- | -------------- | ---- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
strategy [35].

| The Centralized Critic Loss  |     |     |     |  was observed to  |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure: Comparative Performance Metrics for Network
decrease steadily throughout the training, confirming
Orchestration
that the critic network effectively learned to estimate
| the true value function  |     |     |     | , which is crucial for  |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.3.2. Resource Efficiency Metrics
| providing  | accurate  |     | gradient  | feedback  |     | to  the  |     |          |           |     |              |             |         |
| ---------- | --------- | --- | --------- | --------- | --- | -------- | --- | -------- | --------- | --- | ------------ | ----------- | ------- |
|            |           |     |           |           |     |          |     | Average  | Resource  |     | Utilization  | Efficiency  | (RUE):  |
decentralized actors [14]. The successful convergence
|                |         |            |     |            |           |     |     | Measures  | how  | effectively  |     | the  allocated  | physical  |
| -------------- | ------- | ---------- | --- | ---------- | --------- | --- | --- | --------- | ---- | ------------ | --- | --------------- | --------- |
| to  a  stable  | policy  | validates  |     | the  CTDE  | approach  |     | in  |           |      |              |     |                 |           |
managing  non-stationarity  introduced  by  multiple  resources  \mathcal{R}  are  utilized  over  time,
|     |     |     |     |     |     |     |     | considering all resource types  |     |     |     |     |  [10]:  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ------- |
interacting agents [7].

4.3. Comparative Performance Metrics
To rigorously assess the performance of the MA-DDPG
orchestrator, four key metrics were evaluated over a 10-
| hour, unseen testing dataset, comparing the MA-DDPG  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
policy against the Greedy Allocation and Centralized

DQN benchmarks.
where
4.3.1. Quality of Service (QoS) Metrics
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     |     | 64  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
|     |     |     | .   |     |     |     | modifications.  |     | This  reduces  |     | resource  | volatility  | and  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | --- | --------- | ----------- | ---- |
minimizes the risk of cascading failures [30].
|     | 3.  Resource  | Over-Provisioning  |     |     | Factor  (OPF):  |     |             |      |         |          |              |     |               |
| --- | ------------- | ------------------ | --- | --- | --------------- | --- | ----------- | ---- | ------- | -------- | ------------ | --- | ------------- |
|     |               |                    |     |     |                 |     | Crucially,  | the  | agents  | learned  | the  policy  |     | of  resource  |
Quantifies the degree of resource waste. It is
the ratio of allocated resources to the minimum  reclamation (or deflation): when monitoring the traffic
|     |            |                |     |           |                |     | of  an  | eMBB  | slice  | entering  | a   | lull  period,  | the  |
| --- | ---------- | -------------- | --- | --------- | -------------- | --- | ------- | ----- | ------ | --------- | --- | -------------- | ---- |
|     | resources  | theoretically  |     | required  | to  meet  the  |     |         |       |        |           |     |                |      |
corresponding agent would execute a negative change
|     | current demand  |     |  [34]:  |     |     |     |         |     |                                       |     |     |     |     |
| --- | --------------- | --- | ------- | --- | --- | --- | ------- | --- | ------------------------------------- | --- | --- | --- | --- |
|     |                 |     |         |     |     |     | action  |     | , releasing excess resources back to  |     |     |     |     |
the pool. This learned behavior is directly responsible
|     |     |     |     |     |     |     | for the low Over-Provisioning Factor (OPF) observed in  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
the results [34].

4.4.3. Multi-Agent Coordination
A value closer to 1.0 indicates high efficiency, while a
|     |     |     |     |     |     |     | The  decentralized  |     | execution  |     | provided  | by  | the  MA- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ---------- | --- | --------- | --- | -------- |
higher value indicates more resource waste.
DDPG architecture was key to its faster reaction time

compared to the centralized DQN. Each slice agent can
|     |     |     |     |     |     |     | execute  | its  allocation  |     | decision  |     | in  parallel.  | The  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | --------- | --- | -------------- | ---- |
4.4. Analysis of DRL Decision-Making
|     |     |     |     |     |     |     | centralized  | critic  | provided  |     | the  | necessary  | global  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --------- | --- | ---- | ---------- | ------- |
The  MA-DDPG  agents  learned  complex,  non-linear  coordination  to  prevent  agents  from  collectively
|           |       |          |           |           |             |     | violating  | the  | total  |     | resource  |     | constraint  |
| --------- | ----- | -------- | --------- | --------- | ----------- | --- | ---------- | ---- | ------ | --- | --------- | --- | ----------- |
| policies  | that  | exhibit  | superior  | resource  | allocation  |     |            |      |        |     |           |     |             |
 [16], [18]. This coordination ensures
| characteristics  |     | compared  | to  benchmarks,  |     | particularly  |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
under high load and dynamic demand shifts, validating  that while each agent acts locally to maximize its slice's
the need for an intelligent orchestration approach [19].  reward, the overall system remains stable and respects
the physical capacity boundaries, validating the design
4.4.1. Preemptive and Predictive Allocation  choice for a multi-agent solution (RQ2).
The MA-DDPG agents demonstrated preemptive and
|     |     |     |     |     |     |     | The  detailed  | quantitative  |     | results  | derived  |     | from  these  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | --- | -------- | -------- | --- | ------------ |
predictive  capabilities,  directly  addressing  the  analyses, including the explicit numerical comparisons
| limitations  |     | of  reactive  | heuristics  | [29].  | By  including  |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------- | ----------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
between the algorithms, are presented in Chapter 5.
| traffic      | prediction  | information                                 |     |     |   in  the  local  |     |     |     |     |     |     |     |     |
| ------------ | ----------- | ------------------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| observation  |             | , the agents learned to correlate incoming  |     |     |                   |     |     |     |     |     |     |     |     |
traffic patterns with future SLA violation risks.
|     |     |     |     |     |     |     | 5.  RESULTS AND DISCUSSION  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |

For instance, upon detecting the initiation of an eMBB
traffic  surge  pattern,  the  agents  serving  the  critical  This  chapter  presents  the  quantitative  results
uRLLC slices would proactively increase their resource
obtained from the comparative simulation of the
| allocation  |     |     | slightly before the congestion  |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proposed Multi-Agent Deep Deterministic Policy
manifests globally. This action is driven by the high
|                  |     |                                      |     |     |     |     | Gradient  | (MA-DDPG)  |     | orchestrator  |     | against  | the  |
| ---------------- | --- | ------------------------------------ | --- | --- | --- | --- | --------- | ---------- | --- | ------------- | --- | -------- | ---- |
| negative weight  |     |  assigned to the SLA penalty in the  |     |     |     |     |           |            |     |               |     |          |      |
Centralized Deep Q-Network (DQN) and the non-
| reward  | function,  | making  | preemptive  |     | action  highly  |     |           |         |             |     |             |     |      |
| ------- | ---------- | ------- | ----------- | --- | --------------- | --- | --------- | ------- | ----------- | --- | ----------- | --- | ---- |
|         |            |         |             |     |                 |     | learning  | Greedy  | Allocation  |     | benchmark.  |     | The  |
valuable. This proactive buffering effectively isolates
|     |     |     |     |     |     |     | analysis  | validates  | the  | research  |     | questions  | (RQs)  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---- | --------- | --- | ---------- | ------ |
the critical slices from the resource contention caused
|     |     |     |     |     |     |     | concerning  | performance,  |     |     | efficiency,  |     | and  the  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | ------------ | --- | --------- |
by non-critical traffic surges [28].
efficacy of the multi-agent approach.
4.4.2. Granular Adjustments and Resource Reclamation

| The  | use  of  | the  continuous  |     | action  space  | in  DDPG,  |     |     |     |     |     |     |     |     |
| ---- | -------- | ---------------- | --- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
5.1. Main Comparative Performance Results
|     |     |     | ,  provided  | the  | fine-grained  |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
control necessary for optimal orchestration [23]. Instead
|     |     |     |     |     |     |     | The  three  | resource  |     | orchestration  |     | policies  | were  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | -------------- | --- | --------- | ----- |
of large, disruptive discrete steps (as in DQN), the MA- evaluated over a 10-hour simulated testing period
| DDPG  | agents  | make  | small,  | smooth  | resource  |     |     |     |     |     |     |     |     |
| ----- | ------- | ----- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
under dynamic, mixed-traffic conditions, focusing
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     |     | 65  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
on  the  core  problem  of  balancing  strict  QoS  the MA-DDPG's effectiveness in mission-critical
| guarantees with resource efficiency [10].  |     |     |     |     |     |     | environments.  |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
SLA  Resource  Slice  Over- 5.2.2. Latency Distribution Analysis
|     | Violation  | Utilization  |     | Admission  | Provisioning  |     |     |     |     |     |     |     |
| --- | ---------- | ------------ | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Algorithm
Rate  Efficiency  Ratio  Factor  To  further  dissect  the  SVR  improvement,  we
|     | (SVR)  | (RUE)  |     | (SAR)  | (OPF)  |     |           |                  |     |               |     |           |
| --- | ------ | ------ | --- | ------ | ------ | --- | --------- | ---------------- | --- | ------------- | --- | --------- |
|     |        |        |     |        |        |     | analyzed  | the  cumulative  |     | distribution  |     | function  |
MA-DDPG
|     |     |     |     | 95.1%  |     |     | (CDF)  | of  the  | latency  | observed  | for  | the  uRLLC  |
| --- | --- | --- | --- | ------ | --- | --- | ------ | -------- | -------- | --------- | ---- | ----------- |

| (Proposed)  |     |     |     |     |     |     |                                      |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|             |     |     |     |     |     |     | slices across the three algorithms.  |     |     |     |     |     |
Centralized
|     | 2.15%  | 83.9\%  |     | 91.3%  | 1.15  |     |     |     |     |     |     |     |
| --- | ------ | ------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
DQN
Greedy
|     | 4.5%  | 75.2%  |     | 88.7%  | 1.25  |     |     |     |     |     |     |     |
| --- | ----- | ------ | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Allocation

The results unequivocally show that the proposed MA-
| DDPG       | framework   | significantly  |         | outperforms  |      | the       |     |     |     |     |     |     |
| ---------- | ----------- | -------------- | ------- | ------------ | ---- | --------- | --- | --- | --- | --- | --- | --- |
| benchmark  | algorithms  |                | across  | all  four    | key  | metrics,  |     |     |     |     |     |     |
validating the hypotheses underlying our research (RQ2
and RQ3).

5.2. Discussion on QoS Guarantee: Minimizing SLA
|     |     |     |     |     |     |     | Graph  | 2:  Latency  |     | Cumulative  |     | Distribution  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ----------- | --- | ------------- |
Violation Rate (SVR)
Function (CDF) for uRLLC Slices
The most critical performance metric for guaranteeing
the reliability of critical telecom infrastructure is the  Above  graph  showing  the  CDF  of  observed
SLA Violation Rate (SVR), particularly for the ultra- latency for uRLLC traffic over the testing period.
sensitive uRLLC slices [28].  The MA-DDPG curve is sharply skewed to the
left, indicating that a much higher percentage of
5.2.1. Dramatic Reduction in SVR
|     |     |     |     |     |     |     | traffic  | sessions  | met  | the  |     |   ms  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ---- | --- | ----- |
The MA-DDPG orchestrator achieved an SVR of
|     |     |     |     |     |     |     | requirement compared  |     |     | to the  | DQN  | and  Greedy  |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ------- | ---- | ------------ |
0.82%. This represents a dramatic improvement:
curves. The sharp drop in the MA-DDPG curve
|     |      |        |      |           |     |      | near  1.0  | ms  confirms  |     | its  high  | success  | rate  in  |
| --- | ---- | ------ | ---- | --------- | --- | ---- | ---------- | ------------- | --- | ---------- | -------- | --------- |
| •   | 64%  | lower  | SVR  | compared  | to  | the  |            |               |     |            |          |           |
adhering to the ultra-low latency requirement.
Centralized DQN (2.15%).
The MA-DDPG approach ensures that the tail of
•  82% lower SVR compared to the static
the latency distribution is aggressively curtailed,
Greedy approach (4.59%).
meaning fewer outliers suffer from excessive delay
[28]. This granular control is directly enabled by
This result directly validates the ability of the DRL
the continuous action space of DDPG (RQ1). The
agent to learn and execute optimal, dynamic, and
preventative allocation policies in real-time. The  agent can make minute resource adjustments (e.g.,
high penalty weight   assigned to SVR in the  0.5 core increase, 20 Mbps boost) necessary to
|     |     |     |     |     |     |     | keep  the  | latency  | profile  | flat,  | whereas  | DQN’s  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | ------ | -------- | ------ |
reward function drove the agents to prioritize QoS
|     |     |     |     |     |     |     | discrete  | actions  | forced  | larger,  |     | less  precise  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------- | -------- | --- | -------------- |
stability above all else, often making preemptive
adjustments that often led to transient overshoots
| resource    | boosts   | for        | critical     | slices  | when           | traffic  |       |         |     |     |     |     |
| ----------- | -------- | ---------- | ------------ | ------- | -------------- | -------- | ----- | ------- | --- | --- | --- | --- |
|             |          |            |              |         |                |          | past  |  [23].  |     |     |     |     |
| congestion  | was      | predicted  | [29].        | This    | ability        | to       |       |         |     |     |     |     |
| anticipate  | demand,  |            | facilitated  | by      | incorporating  |          |       |         |     |     |     |     |
5.3. Discussion on Resource Efficiency: RUE and
prediction models into the state space, confirms
OPF
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     | 66  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
Achieving  low  SVR  is  trivial  if  resources  are  Graph 3: Dynamic CPU Allocation vs. Traffic
| infinitely over-provisioned. The true success of the  |            |     |     |       |          |          |     | Demand  |     |     |     |     |     |     |
| ----------------------------------------------------- | ---------- | --- | --- | ----- | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| MA-DDPG                                               | framework  |     |     | lies  | in  its  | ability  | to  |         |     |     |     |     |     |     |
simultaneously  achieve  the  best  SVR  while  Above graph A time-series graph over 30 minutes
showing three lines: 1) The uRLLC Slice Traffic
| maximizing  |      | Resource    |     | Utilization  |                    | Efficiency  |     |         |          |             |     |          |          |     |
| ----------- | ---- | ----------- | --- | ------------ | ------------------ | ----------- | --- | ------- | -------- | ----------- | --- | -------- | -------- | --- |
|             |      |             |     |              |                    |             |     | Demand  | (highly  | variable),  |     | 2)  The  | MA-DDPG  |     |
| (RUE)       | and  | minimizing  |     | the          | Over-Provisioning  |             |     |         |          |             |     |          |          |     |
CPU Allocation (preemptive, smooth), and 3) The
Factor (OPF) [10].
Greedy Allocation (reactive, lagging). The MA-
5.3.1. Maximizing Utilization and Minimizing Waste  DDPG line shows allocations slightly ahead of the
demand curve, indicating anticipation, while the
MA-DDPG achieved the highest RUE at 88.5%
|     |     |     |     |     |     |     |     | Greedy  | allocation  | line  | is  | visibly  | lagging  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----- | --- | -------- | -------- | ---- |
and the lowest OPF at 1.07.
demand curve.
| The  Greedy  |            | Allocation  |       | method,  | which    | simply  |     |               |     |             |     |        |            |     |
| ------------ | ---------- | ----------- | ----- | -------- | -------- | ------- | --- | ------------- | --- | ----------- | --- | ------ | ---------- | --- |
|              |            |             |       |          |          |         |     | The  MA-DDPG  |     | allocation  |     | curve  | in  Graph  | 3   |
| allocates    | resources  |             | upon  | request  | without  | any     |     |               |     |             |     |        |            |     |
clearly demonstrates predictive control, leading the
| mechanism  | for    | reclamation  |      | or       | future  | planning,  |     |         |        |           |                   |     |     |           |
| ---------- | ------ | ------------ | ---- | -------- | ------- | ---------- | --- | ------- | ------ | --------- | ----------------- | --- | --- | --------- |
|            |        |              |      |          |         |            |     | demand  | curve  | slightly  | to  maintain low  |     |     | latency.  |
| resulted   | in  a  | low          | RUE  | (75.2%)  | and     | high  OPF  |     |         |        |           |                   |     |     |           |
The Greedy allocation curve follows the demand
| (1.25).   | This         | confirms  | that      | heuristic  |        | approaches  |     |            |                |     |       |         |            |     |
| --------- | ------------ | --------- | --------- | ---------- | ------ | ----------- | --- | ---------- | -------------- | --- | ----- | ------- | ---------- | --- |
|           |              |           |           |            |        |             |     | but  with  | a  noticeable  |     | time  | delay,  | resulting  | in  |
| lead  to  | substantial  |           | resource  |            | waste  | (CapEx      |     |            |                |     |       |         |            |     |
periods where the instantaneous demand exceeds
inefficiency) due to residual allocations from past
|     |     |     |     |     |     |     |     | the  allocated  | resource,  |     | causing  | an  | SLA  | breach.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --- | -------- | --- | ---- | -------- |
peak demands [34].
|               |     |        |               |     |     |               |     | This  visualization  |     | strongly  |         | supports  | the      | DRL  |
| ------------- | --- | ------ | ------------- | --- | --- | ------------- | --- | -------------------- | --- | --------- | ------- | --------- | -------- | ---- |
|               |     |        |               |     |     |               |     | agent’s  capability  |     | to        | handle  | the       | dynamic  | and  |
| The  MA-DDPG  |     | agent  | successfully  |     |     | learned  the  |     |                      |     |           |         |           |          |      |
crucial  trade-off  defined  in  the  reward  function  autonomous nature of the resource orchestration
(RQ3). The penalty on the Resource Cost    problem (RQ1) [19].
| incentivized  |     | the  agents  |     | to  | execute  | proactive  |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |

| resource  | reclamation.  |     | When  |     | an  eMBB  | slice's  |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ----- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
traffic  load  was  predicted  to  decrease,  the  5.4. Efficacy of the Multi-Agent Approach (RQ2)
corresponding agent learned to release the excess
|     |     |     |     |     |     |     |     | The  superior  | performance  |     |     | of  MA-DDPG  |     | over  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | --- | ------------ | --- | ----- |
allocated CPU and Bandwidth back to the pool.
Centralized DQN provides strong evidence for the
The OPF value of 1.07 is extremely close to the
necessity of the Multi-Agent (MA) architecture
| theoretical  | optimum  |     | of  | 1.0,  | highlighting  | the  |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --- | ----- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
for this problem domain.
superior economic efficiency and intelligence of
the learned DRL policy [10].
5.4.1. MA-DDPG vs. Centralized DQN
5.3.2. Dynamic Resource Allocation Visualization  While  both  MA-DDPG  and  Centralized  DQN
utilize DRL, MA-DDPG's SVR is 64\% lower, and
To illustrate the dynamic optimization capabilities,
|               |     |           |     |             |      |            |     | its  RUE  | is  4.6  | percentage  |     | points  | higher.  | This  |
| ------------- | --- | --------- | --- | ----------- | ---- | ---------- | --- | --------- | -------- | ----------- | --- | ------- | -------- | ----- |
| we  analyzed  |     | the  CPU  |     | allocation  | for  | a  single  |     |           |          |             |     |         |          |       |
performance gap is attributed to two factors:
critical uRLLC slice and the remaining capacity
over a turbulent 30-minute period.
|     |     |     |     |     |     |     |     | 1.  Continuous vs. Discrete Action Space: As  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
noted, DDPG's continuous action space offers
granularity, leading to more precise control
and lower SVR compared to the discrete-step
actions of DQN [23].
|     |     |     |     |     |     |     |     | 2.  Scalability and Reactivity: The Centralized  |     |       |                |     |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | ----- | -------------- | --- | ---------- | --- |
|     |     |     |     |     |     |     |     | Training                                         |     | with  | Decentralized  |     | Execution  |     |
(CTDE) paradigm in MA-DDPG allows each

slice agent to execute its resource adjustment
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     |     |     | 67  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
decision  in  parallel  based  on  its  local  coupling  effects  (e.g.,  thermal  throttling),  and
observation  . This decentralized execution  communication overhead between the orchestrator
reduces orchestration overhead and leads to  and the SDN controller are simplified. Validation
in a more realistic setup is required [22].
faster reaction times [16], which is vital for
| preventing  |     |     | millisecond-level  |     |     | latency  |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
5.5.2. Future Directions
violations in critical slices. The Centralized
DQN,  by  contrast,  must  process  the  full  Future work should prioritize:
global state and output a single, large action
vector, which scales poorly with the number  •  Hardware-in-the-Loop  (HIL)  Testing:
Validating the learned policy on a real-
| of  | slices  | N.  The  | centralized  |     | critic  | ensures  |     |     |     |     |     |     |     |     |
| --- | ------- | -------- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
time testbed with physical COTS servers
global coordination, effectively managing the
|     |     |     |     |     |     |     |     |     | and  | open-source  |     | orchestrators  |     | (e.g.,  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | -------------- | --- | ------- |
inter-slice dependencies and the total resource
Kubernetes) to measure the performance
constraint [18].
under actual physical constraints [32].
5.4.2. Slice Admission Control (SAR)
|     |     |     |     |     |     |     |     |     | •  Partial  |     | Observability:  |     | Investigating  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | -------------- | --- |
The high Slice Admission Ratio (SAR) of 95.1%
|     |     |     |     |     |     |     |     |     | decentralized  |     | training  |     | approaches  | (e.g.,  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ----------- | ------- |
for MA-DDPG demonstrates that the DRL policy
using Dec-POMDP models) where agents
| has  effectively  |     | learned  | the  | balance  | of  | resource  |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | ---- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
rely solely on local observations, which is
| utilization  | required  |     | to  accept  |     | new  | slices.  By  |     |     |       |     |         |     |          |        |
| ------------ | --------- | --- | ----------- | --- | ---- | ------------ | --- | --- | ----- | --- | ------- | --- | -------- | ------ |
|              |           |     |             |     |      |              |     |     | more  |     | robust  | to  | control  | plane  |
maintaining a minimal but optimal resource buffer
communication failures [17].
| (low  OPF)                                            | and  | continuously  |     | reclaiming  |     | unused  |     |     |             |     |      |              |          |              |
| ----------------------------------------------------- | ---- | ------------- | --- | ----------- | --- | ------- | --- | --- | ----------- | --- | ---- | ------------ | -------- | ------------ |
|                                                       |      |               |     |             |     |         |     |     | Security    |     | and  | Resilience:  |          | Integrating  |
| resources, the orchestrator ensures that capacity is  |      |               |     |             |     |         |     |     | •           |     |      |              |          |              |
|                                                       |      |               |     |             |     |         |     |     | mechanisms  |     | to   | defend       | against  | resource-    |
available to admit new, revenue-generating slices.
starvation attacks by modeling malicious
The lower SAR for Greedy (88.7%) is due to its
slice requests as an adversarial element,
high OPF wasted resources remain tied up, leading
to unnecessary rejection of new service requests.  potentially  utilizing  Adversarial  DRL
|     |     |     |     |     |     |     |     |     | techniques  |     | to  | enhance  | network  | security  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | -------- | -------- | --------- |

[27].
5.5. Limitations and Future Outlook

| While             | the  MA-DDPG  |               | framework  |          | demonstrates  |              |     |                                  |     |     |     |     |     |     |
| ----------------- | ------------- | ------------- | ---------- | -------- | ------------- | ------------ | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
|                   |               |               |            |          |               |              |     | 6.  CONCLUSION AND FUTURE WORK   |     |     |     |     |     |     |
| state-of-the-art  |               | performance,  |            | several  |               | limitations  |     |                                  |     |     |     |     |     |     |

warrant  discussion  and  motivate  future  work  This  chapter  summarizes  the  key  findings  and
(RQ3).  contributions  of  this  research  on  developing  an
|     |     |     |     |     |     |     |     | autonomous  |     | resource  | orchestration  |     | framework  | for  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------------- | --- | ---------- | ---- |
network slicing, followed by a detailed discussion of
5.5.1. Training Complexity and Real-World Fidelity
promising directions for future investigation.
| The primary drawback of the MA-DDPG approach  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

is its inherent training complexity and the lengthy
6.1. Summary of Contributions and Findings
| convergence  | time  |     | (500  | episodes).  |     | The  large  |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ----- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
number of interacting agents and the complexity of  This paper successfully proposed and validated a novel
|                   |     |         |     |          |     |              |     | Multi-Agent  |     | Deep  | Deterministic  |     | Policy  | Gradient  |
| ----------------- | --- | ------- | --- | -------- | --- | ------------ | --- | ------------ | --- | ----- | -------------- | --- | ------- | --------- |
| the  centralized  |     | critic  |     | network  |     | necessitate  |     |              |     |       |                |     |         |           |
(MA-DDPG) framework for dynamic network slicing
| significant  | computational  |     |     | resources  | and  | careful  |     |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | --- | ---------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
and resource orchestration in Software-Defined critical
hyperparameter tuning [35].  telecom infrastructure [1]. By directly addressing the
|     |     |     |     |     |     |     |     | critical  | challenge  |     | of  managing  |     | highly  heterogeneous  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------------- | --- | ---------------------- | --- |
Furthermore, the simulation environment (DENS- and  time-varying  Quality  of  Service  (QoS)
|     |     |     |     |     |     |     |     | requirements  |     | under  | finite  | resource  | constraints,  | this  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------- | --------- | ------------- | ----- |
Sim), while detailed, remains a simplification of a
|     |     |     |     |     |     |     |     | work  | provides  | a   | robust  | and  intelligent  | step  | toward  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ------- | ----------------- | ----- | ------- |
true  physical  network.  Factors  like  hardware- achieving the fully autonomous, self-optimizing "zero-
specific  VNF  placement  constraints,  cross-layer  touch" network management demanded by 5G and 6G
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     |     |     | 68  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
critical services [2], [10]. The DRL-driven policy offers  operating  large-scale  SDN/NFV  environments
a necessary technological leap beyond static, reactive,  where centralized bottlenecking must be avoided
| and heuristic allocation methods.  |     |     |     |     |     |     | [11], [18].  |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
The primary contributions and demonstrated findings,  •  High  Service  Adoption  and  Scalability:  The
derived  from  extensive  comparative  simulation,  are  DRL-learned  policy  maintained  a  high  Slice
summarized as follows:  Admission  Ratio  (SAR)  of  95.1%.  This  high
•  Novel MA-DDPG Formulation and Continuous  acceptance rate confirms that the efficient resource
Control  (RQ1  Validation):  We  successfully  utilization  policy  leaves  a  minimal  but  optimal
modeled the complex, high-dimensional resource  resource buffer, ensuring the system can fluidly
orchestration problem as a cooperative multi-agent  accommodate  new  revenue-generating  slice
learning  task  using  the  MA-DDPG  architecture.  requests without risking the performance stability
This  design,  which  employs  an  actor-critic  of existing critical services.
| structure with a continuous action space, allowed  |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
individual DRL agents to autonomously learn an  In  conclusion,  the  MA-DDPG  framework  offers  a
optimal resource allocation policy  . This  robust,  intelligent,  and  necessary  evolution  of  the
|           |              |          |                |     |      |     | Management  |     | and  Orchestration  |     | (MANO)  | layer  for  |
| --------- | ------------ | -------- | -------------- | --- | ---- | --- | ----------- | --- | ------------------- | --- | ------- | ----------- |
| inherent  | ability  to  | execute  | fine-grained,  |     | non- |     |             |     |                     |     |         |             |
disruptive  resource  adjustments  (e.g.,  small    future critical telecom networks, successfully moving
resource management beyond reactive heuristics toward
| values)  | is  essential  | for  | granular  | control  | and  |     |     |     |     |     |     |     |
| -------- | -------------- | ---- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
true autonomous self-optimization.
minimized resource oscillation [6], [7], [16].
| •  Significantly  | Superior  |     | QoS  Guarantee  |     | (SVR  |     |     |     |     |     |     |     |
| ----------------- | --------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
6.2. Future Research Directions
Minimization): The simulation results confirmed
| that  the  | MA-DDPG  | approach  |     | minimizes  | the  |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
While this research provides a strong foundation, the
| Service  | Level  Agreement  |     | (SLA)  | Violation  | Rate  |     |               |     |                     |             |     |           |
| -------- | ----------------- | --- | ------ | ---------- | ----- | --- | ------------- | --- | ------------------- | ----------- | --- | --------- |
|          |                   |     |        |            |       |     | path  toward  |     | a  fully  deployed  | zero-touch  |     | resource  |
(SVR), achieving an industry-leading rate of 0.82%
orchestrator presents several complex challenges that
| over  the  | testing  period.  |     | This  | remarkable  | result  |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | ----- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
delineate promising avenues for future work, bridging
represents an improvement of over 80% compared
|     |     |     |     |     |     |     | the  gap  | between  | simulation  |     | and  | real-world  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | --- | ---- | ----------- |
to the static Greedy allocation benchmark and 64%
implementation.
| over  the  | Centralized  |     | DQN.  | This  | dramatic  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |

| improvement  | validates    | the  | DRL          | agent's  | core        |     |                     |     |           |          |           |      |
| ------------ | ------------ | ---- | ------------ | -------- | ----------- | --- | ------------------- | --- | --------- | -------- | --------- | ---- |
|              |              |      |              |          |             |     | 6.2.1.  Addressing  |     | Enhanced  | Network  | Dynamics  | and  |
| capability   | to  execute  |      | predictive,  |          | preemptive  |     |                     |     |           |          |           |      |
Service Management
resource adjustments anticipating traffic surges and
| dynamically  | favoring  | sensitive  |     | uRLLC  | slices  |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
The current model focuses solely on resource allocation
thereby effectively mitigating the risk of critical
within fixed VNF deployments. Future research must
latency breaches [28], [29].  incorporate  the  broader  VNF  and  slice  life-cycle
•  Optimized Dual-Objective Resource Efficiency
management decisions to achieve end-to-end autonomy
| (RUE/OPF,  | RQ3  | Validation):  |     | The  | framework  |     |     |     |     |     |     |     |
| ---------- | ---- | ------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[22]:
successfully  balanced  the  conflicting  goals  of  •  VNF Migration and Auto-Scaling: The resource
| maximizing    | QoS  | and             | minimizing  |     | resource   |     |             |     |                |       |                 |       |
| ------------- | ---- | --------------- | ----------- | --- | ---------- | --- | ----------- | --- | -------------- | ----- | --------------- | ----- |
|               |      |                 |             |     |            |     | allocation  |     | action  space  | must  | be  integrated  | with  |
| consumption.  | It   | simultaneously  |             |     | maximized  |     |             |     |                |       |                 |       |
discrete actions for VNF placement optimization
Resource Utilization Efficiency (RUE) to 88.5%  (migration) and dynamic scaling (instantiating or
and achieved the lowest Over-Provisioning Factor
|        |              |             |     |            |      |     | terminating  |     | VNF  instances).  |     | This  | requires  |
| ------ | ------------ | ----------- | --- | ---------- | ---- | --- | ------------ | --- | ----------------- | --- | ----- | --------- |
| (OPF)  | of  .  This  | efficiency  |     | validates  | the  |     |              |     |                   |     |       |           |
transitioning to a hybrid discrete-continuous action
optimal  design  of  the  multi-objective  reward  space,  potentially  leveraging  algorithms  like
| function.  | The  agents  |     | learned  | the  | economic  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
Proximal Policy Optimization (PPO) or Soft Actor-
necessity of proactive resource reclamation actively
|     |     |     |     |     |     |     | Critic  | (SAC)  | with  specialized  |     | adaptations  | for  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------------------ | --- | ------------ | ---- |
releasing resources from under-utilized non-critical  mixed action sets [32]. These models are better
slices back to the shared pool ensuring maximum
|                 |             |     |                |     |            |     | suited  | to  | learning  complex,  | long-term  |     | migration  |
| --------------- | ----------- | --- | -------------- | --- | ---------- | --- | ------- | --- | ------------------- | ---------- | --- | ---------- |
| infrastructure  | efficiency  |     | and  economic  |     | viability  |     |         |     |                     |            |     |            |
policies that minimize service disruption costs.
| [10], [34].  |     |     |     |     |     |     | •  Cross-Domain,  |     | Hierarchical  |     | Orchestration:  |     |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------- | --- | --------------- | --- |
•  Validated Efficacy of Multi-Agent Control (RQ2
Extending the framework from a single MEC host
| Validation):  | The  |     | consistently  |     | superior  |     |     |     |     |     |     |     |
| ------------- | ---- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
to a multi-domain, hierarchical orchestration model
performance over the Centralized DQN benchmark  that spans core, regional, and edge networks. A
strongly validates the choice of the Multi-Agent  Hierarchical DRL (HDRL) approach [17] could be
(MA) architecture. The decentralized execution of
|     |     |     |     |     |     |     | employed,  |     | where a  high-level agent decides the  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------------------------- | --- | --- | --- |
policies within the MA-DDPG's CTDE paradigm  inter-domain  slice  placement  and  resource
allowed for faster, parallel decision-making across  partitioning,  while  the  existing  low-level  MA-
| numerous     | active               | slices,  | improving  |     | system     |     |       |         |          |                    |     |           |
| ------------ | -------------------- | -------- | ---------- | --- | ---------- | --- | ----- | ------- | -------- | ------------------ | --- | --------- |
|              |                      |          |            |     |            |     | DDPG  | agents  | perform  | the  fine-grained  |     | resource  |
| scalability  | and  responsiveness  |          |            | to  | localized  |     |       |         |          |                    |     |           |
tuning within their local domains, ensuring global
fluctuations,  which  are  key  requirements  for  consistency and local optimality.
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     | 69  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
•  Network Service Chaining (NSC) Optimization:  •  Adversarial  DRL  for  Security:  Investigating
Incorporating  the  sequencing,  functional  Adversarial DRL (ADRL) techniques to train the
placement, and optimization of VNFs within a slice  orchestrator  to  detect  and  neutralize  resource-
(Service Function Chain) into the DRL decision  starvation  attacks.  Malicious  actors  may
process.  This  requires  the  DRL  agent  to  learn  deliberately  submit  rapidly  fluctuating,  high-
optimal latency-aware VNF ordering and chaining  demand slice requests to induce system instability
subject  to  resource  and  dependency  constraints  and resource exhaustion. By modeling the attacker
[19],  moving  beyond  simple  resource  capacity  as an adversary in a two-player game (min-max
budgeting to topology optimization.  optimization),  the  DRL  orchestrator  can  learn
|     |     |     |     |     |     |     |     | policies       | that      | are  robust  |          | to  non-cooperative,  |      |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------ | -------- | --------------------- | ---- |
|     |     |     |     |     |     |     |     | unpredictable  | demands,  |              | thereby  | enhancing             | the  |
6.2.2. Robustness and Real-World Deployment  network's resilience [27].
|                |           |               |             |            |              |     |     | •  Fault  Tolerance  |          | and        | Recovery:  |      | Integrating  |
| -------------- | --------- | ------------- | ----------- | ---------- | ------------ | --- | --- | -------------------- | -------- | ---------- | ---------- | ---- | ------------ |
| Transitioning  |           | the  learned  | policy      | from       | simulation   |     | to  |                      |          |            |            |      |              |
|                |           |               |             |            |              |     |     | explicit             | failure  | detection  |            | and  | recovery     |
| deployment     | requires  |               | addressing  | practical  | operational  |     |     |                      |          |            |            |      |              |
mechanisms into the DRL framework. The agent
challenges and enhancing system robustness [35]:  should be trained not only to allocate resources
| •  Partial  |     | Observability  |     | and  | Decentralized  |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
optimally but also to proactively detect potential
Learning (Dec-POMDP): The current MA-DDPG  hardware/VNF  faults  and  execute  rapid  re-
relies on centralized training using the global state  allocation and re-routing policies to ensure system
| \mathbf{x}.  |     | In  | a  decentralized  |     | operational  |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
continuity for critical slices following a failure
| environment,  |     | communication  |     |     | delays  or  | failures  |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
event.
| might prevent a complete global view. Future work  |              |     |                |     |     |             |     |     |     |     |     |     |     |
| -------------------------------------------------- | ------------ | --- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| should                                             | investigate  |     | incorporating  |     |     | a  Partial  |     |     |     |     |     |     |     |

| Observability  |     |     | model  | (Dec-POMDP).  |     | This  |     |     |     |     |     |     |     |
| -------------- | --- | --- | ------ | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES:
| necessitates  |     | exploring  |     | decentralized  |     | DRL  |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |

architectures where agents rely only on their local
| observations  |     | x_i  | during  | training,  | perhaps  | using  |     |     |     |     |     |     |     |
| ------------- | --- | ---- | ------- | ---------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
coordination techniques like Value Decomposition  [1]  Sharafaldin, I., Lashkari, A. H., & Ghorbani, A. A.
|     |     |     |     |     |     |     |     | (2018).  | Toward  | generating  |     | a  new  | intrusion  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------- | --- | ------- | ---------- |
Networks (VDN) or QMIX to coordinate agents
implicitly using a shared utility function, enhancing  detection  dataset  and  intrusion  traffic
scalability and fault tolerance [17].  characterization.  In  Proceedings  of  the  4th
International Conference on Information Systems
| •  Hardware-in-the-Loop  |     |     |     | (HIL)  | Testing:  | The  |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ultimate validation of the policy must occur on a  Security  and  Privacy  (ICISSP)  (pp.  108–116).
real-time  hardware  testbed  [22].  This  involves  https://doi.org/10.5220/0006639801080116
| integrating  |     | the  DRL  | agent         | with  | an  actual  | SDN  |     |                                                         |     |     |     |     |     |
| ------------ | --- | --------- | ------------- | ----- | ----------- | ---- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|              |     |           |               |       |             |      |     | [2]  Silver, D., Huang, A., Maddison, C. J., Guez, A.,  |     |     |     |     |     |
| controller   |     | (e.g.,    | OpenDaylight  |       | or  ONOS)   | and  | a   |                                                         |     |     |     |     |     |
NFV orchestrator (e.g., OpenStack or Kubernetes)  Sifre, L., Van Den Driessche, G., ... & Hassabis, D.
(2016). Mastering the game of Go with deep neural
to measure the policy's effectiveness under real-
networks and tree search. Nature, 529(7587), 484–
| world  | resource  |     | contention,  |     | physical  | resource  |     |     |     |     |     |     |     |
| ------ | --------- | --- | ------------ | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
489. https://doi.org/10.1038/nature16961
| fragmentation,  |     | and  | network  | overhead,  |     | providing  |     |     |     |     |     |     |     |
| --------------- | --- | ---- | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
critical deployment feedback and calibration data.
|            |             |     |               |     |          |       |     | [3]  Patcha, A., & Park, J. M. (2007). An overview of  |     |     |     |     |            |
| ---------- | ----------- | --- | ------------- | --- | -------- | ----- | --- | ------------------------------------------------------ | --- | --- | --- | --- | ---------- |
| •  Energy  | Efficiency  |     | Integration:  |     | Current  | work  |     |                                                        |     |     |     |     |            |
|            |             |     |               |     |          |       |     | anomaly detection techniques: Existing                 |     |     |     |     | solutions  |
focuses  primarily  on  QoS  and  utilization.  The  and  latest  technological  trends.  Computer
| reward  | function  |     | can  be  | rigorously  | extended  |     | to  |            |     |          |     |     |             |
| ------- | --------- | --- | -------- | ----------- | --------- | --- | --- | ---------- | --- | -------- | --- | --- | ----------- |
|         |           |     |          |             |           |     |     | Networks,  |     | 51(12),  |     |     | 3448–3470.  |
include an energy consumption penalty   to  https://doi.org/10.1016/j.comnet.2006.09.001
drive green network operation:
|     |     |     |     |     |     |     |     | [4]  Olufemi, O. D., Ejiade, A. O., Ogunjimi, O., &  |          |          |                |                  |             |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | -------- | -------- | -------------- | ---------------- | ----------- |
|     |     |     |     |     |     |     |     | Ikwuogu,                                             | F.  O.   | (2024).  | AI-enhanced    |                  | predictive  |
|     |     |     |     |     |     |     |     | maintenance                                          | systems  |          | for  critical  | infrastructure:  |             |
Cloud-native architectures approach. World Journal
| The  DRL   | agent  | could  | then     | learn  | to  consolidate  |              |     |               |     |              |     |             |      |
| ---------- | ------ | ------ | -------- | ------ | ---------------- | ------------ | --- | ------------- | --- | ------------ | --- | ----------- | ---- |
|            |        |        |          |        |                  |              |     | of  Advanced  |     | Engineering  |     | Technology  | and  |
| workloads  | onto   | fewer  | servers  |        | during           | low-traffic  |     |               |     |              |     |             |      |
periods,  enabling  the  shutdown  of  idle  physical  Sciences,  13(02),  229–257.
infrastructure  (deep  sleep  modes)  to  minimize  https://doi.org/10.30574/wjaets.2024.13.2.0552
operational expenditure (OpEx) [18].
|     |     |     |     |     |     |     |     | [5]  Mohassel, P., & Zhang, Y. (2017). SecureML: A  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |

6.2.3. Security and Resilience Enhancement  system  for  scalable  privacy-preserving  machine
learning. In 2017 IEEE Symposium on Security
and Privacy (SP) (pp. 19–38). IEEE.
| Given      | the  focus  | on  | critical  | telecom    | infrastructure,  |      |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --------- | ---------- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| enhancing  | resilience  |     | against   | malicious  | activities       | and  |     |     |     |     |     |     |     |
unpredictable failures is paramount [27]:
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     |     |     | 70  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
[6] McMahan, H. B., Moore, E., Ramage, D., (2024). Infrastructure-as-code for 5G RAN, core
Hampson, S., & y Arcas, B. A. (2017). and SBI deployment: A comprehensive review.
Communication-efficient learning of deep International Journal of Science and Research
networks from decentralized data. In Artificial Archive, 21(3), 144–167.
Intelligence and Statistics (pp. 1273–1282). PMLR. https://doi.org/10.30574/gjeta.2024.21.3.0235
[7] Bobie-Ansah, D., Olufemi, D., & Agyekum, E. K. [17] Yang, Q., Liu, Y., Chen, T., & Tong, Y. (2019).
(2024). Adopting infrastructure as code as a cloud Federated machine learning: Concept and
security framework for fostering an environment of applications. ACM Transactions on Intelligent
trust and openness to technological innovation Systems and Technology (TIST), 10(2), 1–19.
among businesses: Comprehensive review. https://doi.org/10.1145/3298981
International Journal of Science & Engineering
Development Research, 9(8), 168–183. [18] Li, T., Sahu, A. K., Talwalkar, A., & Smith, V.
http://www.ijrti.org/papers/IJRTI2408026.pdf (2020). Federated learning: Challenges, methods,
and future directions. IEEE Signal Processing
[8] Kairouz, P., McMahan, H. B., Avent, B., Bellet, A., Magazine, 37(3), 50–60.
Bennis, M., Bhagoji, A. N., ... & Zhao, S. (2019). https://doi.org/10.1109/MSP.2020.2975749
Advances and open problems in federated learning.
arXiv preprint arXiv:1912.04977. [19] Arulkumaran, K., Deisenroth, M. P., Brundage, M.,
& Bharath, A. A. (2017). Deep reinforcement
[9] Hasselt, H. V., Guez, A., & Silver, D. (2016). Deep learning: A brief survey. IEEE Signal Processing
reinforcement learning with double Q-learning. In Magazine, 34(6), 26–38.
Proceedings of the AAAI Conference on Artificial https://doi.org/10.1109/MSP.2017.2743240
Intelligence (Vol. 30, No. 1).
[20] Shokri, R., & Shmatikov, V. (2015). Privacy-
[10] Zhao, Y., Li, M., Lai, L., Suda, N., Civin, D., & preserving deep learning. In Proceedings of the
Chandra, V. (2018). Federated learning with non- 22nd ACM SIGSAC Conference on Computer and
IID data. arXiv preprint arXiv:1806.00582. Communications Security (pp. 1310–1321).
[11] Moustafa, N., & Slay, J. (2015). UNSW-NB15: A [21] Geyer, R. C., Klein, T., & Nabi, M. (2017).
comprehensive data set for network intrusion Differentially private federated learning: A client
detection systems (UNSW-NB15 network data set). level perspective. arXiv preprint arXiv:1712.07557.
In 2015 Military Communications and Information
Systems Conference (MilCIS) (pp. 1–6). IEEE. [22] Olufemi, O. D., Oladejo, A. O., Anyah, V.,
Oladipo, K., & Ikwuogu, F. U. (2025). AI enabled
[12] Kiumarsi, B., Modares, H., Lewis, F. L., & observability: Leveraging emerging networks for
Karimpour, A. (2017). Optimal and autonomous proactive security and performance monitoring.
control using reinforcement learning: A survey. International Journal of Innovative Research and
IEEE Transactions on Neural Networks and Scientific Studies, 8(3), 2581–2606.
Learning Systems, 29(6), 2042–2062. https://doi.org/10.53894/ijirss.v8i3.7054
https://doi.org/10.1109/TNNLS.2017.2671045
[23] Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N.,
[13] Zhang, J., Chen, J., & Sun, Q. (2023). Federated AI Erez, T., Tassa, Y., ... & Wierstra, D. (2015).
agents for autonomous security policy Continuous control with deep reinforcement
enforcement. ACM Transactions on Internet learning. arXiv preprint arXiv:1509.02971.
Technology, 24(2), 1–27.
https://doi.org/10.1145/3643012 [24] Samek, W., Montavon, G., Vedaldi, A., Hansen, L.
K., & Müller, K.-R. (2019). Explainable AI:
[14] Chen, L., Jordan, S., Liu, Y.-K., Moody, D., Interpreting, explaining and visualizing deep
Peralta, R., Perlner, R., ... & Dang, Q. (2022). learning. Springer. https://doi.org/10.1007/978-3-
Report on post-quantum cryptography. NISTIR 030-28954-6
8105. https://doi.org/10.6028/NIST.IR.8105
[25] Bonawitz, K., Ivanov, V., Kreuter, B., Marcedone,
[15] Adewa, A., Anyah, V., Olufemi, O. D., Oladejo, A. A., McMahan, H. B., Patel, S., ... & Seth, K.
O., & Olaifa, T. (2025). The impact of intent-based (2017). Practical secure aggregation for privacy-
networking on network configuration management preserving machine learning. In Proceedings of the
and security. Global Journal of Engineering and 2017 ACM SIGSAC Conference on Computer and
Technology Advances, 22(01), 063–068. Communications Security (pp. 1175–1191).
https://doi.org/10.30574/gjeta.2025.22.1.0012 https://doi.org/10.1145/3133956.3133982
[16] Olufemi, O. D., Ikwuogu, O. F., Kamau, E.,
Oladejo, A. O., Adewa, A., & Oguntokun, O.
www.ijcat.com 71

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
[26] Satyanarayanan, M. (2017). The emergence of edge  Networks,  24(4),  1279–1297.
computing.  Computer,  50(1),  30–39.  https://doi.org/10.1007/s11276-016-1346-2
https://doi.org/10.1109/MC.2017.9
[36] Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.
[27] Zhang, C., Xie, Y., Bai, Y., Yu, R., & Zhang, Y.  A., Veness, J., Bellemare, M. G., ... & Hassabis, D.
(2020).  Batchcrypt:  Efficient  homomorphic  (2015).  Human-level  control  through  deep
encryption  for  cross-silo  federated  learning.  In  reinforcement  learning.  Nature,  518(7540),  529–
USENIX  Conference  on  Networked  Systems  533. https://doi.org/10.1038/nature14236
Design and Implementation (NSDI).
[37] Yang, D., Wang, D., Zhang, Y., & Wang, J. (2021).
[28] Bobie-Ansah, D., & Affram, H. (2024). Impact of  A survey on federated learning and its applications
secure cloud computing solutions on encouraging  in edge computing. IEEE Access, 9, 86712–86736.
small and medium enterprises to participate more  https://doi.org/10.1109/ACCESS.2021.3088870
| actively  | in  e-commerce.  |     | International  |     | Journal  | of  |     |     |     |     |     |
| --------- | ---------------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
Science  &  Engineering  Development  Research,  [38] Sutton,  R.  S.,  &  Barto,  A.  G.  (2018).
Reinforcement learning: An introduction (2nd ed.).
| 9(7),                                         |     |     |     |     | 469–483.  |     |             |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --------- | --- | ----------- | --- | --- | --- | --- |
| http://www.ijrti.org/papers/IJRTI2407064.pdf  |     |     |     |     |           |     | MIT Press.  |     |     |     |     |
[29] Kim, G., Lee, S., & Kim, S. (2014). A novel hybrid  [39] Sommer,  R.,  &  Paxson,  V.  (2010).  Outside  the
|            |            |     |         |              |          |     | closed  | world:  On  using  | machine  | learning  | for  |
| ---------- | ---------- | --- | ------- | ------------ | -------- | --- | ------- | ------------------ | -------- | --------- | ---- |
| intrusion  | detection  |     | method  | integrating  | anomaly  |     |         |                    |          |           |      |
detection with misuse detection. Expert Systems  network  intrusion  detection.  In  2010  IEEE
with  Applications,  41(4),  1690–1700.  Symposium  on  Security  and  Privacy  (pp.  305–
| https://doi.org/10.1016/j.eswa.2013.08.066  |     |     |     |     |     |     | 316). IEEE.  |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
[40] Ahmed, M., Mahmood, A. N., & Hu, J. (2016). A
[30] David Olufemi, Ayodeji Olutosin Ejiade, Friday
Ogochukwu  Ikwuogu,  Phebe  Eleojo  Olufemi,  survey of network anomaly detection techniques.
Deligent Bobie-Ansah (2025). Securing Software- Journal of Network and Computer  Applications,
|     |     |     |     |     |     |     | 60,  |     |     |     | 19–31.  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- |
Defined Networks (SDN) Against Emerging Cyber
Threats  in  5G  and  Future  Networks  –  A  https://doi.org/10.1016/j.jnca.2015.11.016
| Comprehensive  |     | Review.  |     | INTERNATIONAL  |     |     |                       |      |             |      |              |
| -------------- | --- | -------- | --- | -------------- | --- | --- | --------------------- | ---- | ----------- | ---- | ------------ |
|                |     |          |     |                |     |     | [41] Francois-Lavet,  | V.,  | Henderson,  | P.,  | Islam,  R.,  |
JOURNAL OF ENGINEERING RESEARCH &
|             |     |     |           |     |          |     | Bellemare,  | M.  G.,  | &  Pineau,  | J.  (2018).  | An  |
| ----------- | --- | --- | --------- | --- | -------- | --- | ----------- | -------- | ----------- | ------------ | --- |
| TECHNOLOGY  |     |     | (IJERT),  |     | 14(02).  |     |             |          |             |              |     |
https://doi.org/10.1145/2810103.2813687  introduction  to  deep  reinforcement  learning.
|     |     |     |     |     |     |     | Foundations and Trends® in Machine  |     |     |     | Learning,  |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ---------- |
[31] Molnar, C. (2022). Interpretable machine learning  11(3–4),  219–354.
https://doi.org/10.1561/2200000071
| (2nd  |     |     |     |     | ed.).  |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
https://christophm.github.io/interpretable-ml-book/
|     |     |     |     |     |     |     | [42] Garcia-Teodoro,  | P.,  | Diaz-Verdejo,  |     | J.,  Macia- |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ---- | -------------- | --- | ----------- |
[32] Oladejo, A. O., Olufemi, O. D., Kamau, E., Mike- Fernandez, G., & Vazquez, E. (2009). Anomaly-
|     |     |     |     |     |     |     | based  network  | intrusion  | detection:  |     | Techniques,  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ----------- | --- | ------------ |
Ewewie, D. O., Olajide, A. L., & Williams, D.
(2025). AI-driven cloud-edge synergy in telecom:  systems  and  challenges.  Computers  &  Security,
An  approach  for  real-time  data  processing  and  28(1–2),  18–28.
https://doi.org/10.1016/j.cose.2008.08.003
latency optimization. World Journal of Advanced
Engineering Technology and Sciences, 14(3), 462–
[43] Chandola, V., Banerjee, A., & Kumar, V. (2009).
495.
https://doi.org/10.30574/wjaets.2025.14.3.0166  Anomaly detection:  A  survey. ACM Computing
|     |     |     |     |     |     |     | Surveys  | (CSUR),  |     | 41(3),  | 1–58.  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------- | ------ |
https://doi.org/10.1145/1541880.1541882
[33] Schulman, J., Wolski, F., Dhariwal, P., Radford,
| A.,  &  | Klimov,  | O.  | (2017).  | Proximal  | policy  |     |     |     |     |     |     |
| ------- | -------- | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
optimization  algorithms.  arXiv  preprint  [44] Feng, H., Liu, Y., Chen, W., & Xia, Y. (2022).
Trust-aware federated learning for secure edge AI
arXiv:1707.06347.
in 5G. IEEE Transactions on Network and Service
[34] Zhao, Z., Zhang, X., & Li, Y. (2023). Toward AI- Management,  19(1),  341–355.
native  broadband  security:  Opportunities  and  https://doi.org/10.1109/TNSM.2021.3132711
| challenges.  | IEEE  |     | Network,  |     | 37(1),  8–15.  |     |     |     |     |     |     |
| ------------ | ----- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
[45] Henderson, P., Islam, R., Bachman, P., Pineau, J.,
https://doi.org/10.1109/MNET.011.2200262
|     |     |     |     |     |     |     | Precup,  | D.,  &  Meger,  | D.  | (2018).  | Deep  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | -------- | ----- |
[35] Shamsi, J. A., & Al-Dubai, A. Y. (2018). Secure  reinforcement learning that matters. In Proceedings
network coding and cryptographic approaches for  of the AAAI Conference on Artificial Intelligence
(Vol. 32, No. 1).
security in wireless networks: A survey. Wireless
| www.ijcat.com  |     |     |     |     |     |     |     |     |     |     | 72  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

International Journal of Computer Applications Technology and Research
Volume 14–Issue 11, 53 – 73, 2025, ISSN:-2319–8656
DOI:10.7753/IJCATR1411.1006
[46] Lee, H., Park, S., & Kim, J. (2023). Lightweight AI [50] Lundberg, S. M., & Lee, S. I. (2017). A unified
deployment on edge nodes: Challenges and approach to interpreting model predictions. In
solutions. ACM Computing Surveys, 55(3), 1–38. Advances in Neural Information Processing
https://doi.org/10.1145/3520543 Systems (Vol. 30).
[47] Liao, H. J., Lin, C. H. R., Lin, Y. C., & Tung, K. Y. [51] Alshahrani, A., & Qureshi, K. N. (2022). AI-driven
(2013). Intrusion detection system: A anomaly detection in 5G networks: A survey.
comprehensive review. Journal of Network and Computer Networks, 208, 108901.
Computer Applications, 36(1), 16–24. https://doi.org/10.1016/j.comnet.2022.108901
https://doi.org/10.1016/j.jnca.2012.09.004
[52] Ribeiro, M. T., Singh, S., & Guestrin, C. (2016).
[48] Tavallaee, M., Bagheri, E., Lu, W., & Ghorbani, A. "Why should I trust you?": Explaining the
A. (2009). A detailed analysis of the KDD CUP 99 predictions of any classifier. In Proceedings of the
data set. In 2009 IEEE Symposium on 22nd ACM SIGKDD International Conference on
Computational Intelligence for Security and Knowledge Discovery and Data Mining (pp. 1135–
Defense Applications (pp. 1–6). IEEE. 1144). https://doi.org/10.1145/2939672.2939778
[49] Smith, V., Chiang, C. K., Sanjabi, M., & [53] Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L.
Talwalkar, A. (2017). Federated multi-task (2016). Edge computing: Vision and challenges.
learning. In Advances in Neural Information IEEE Internet of Things Journal, 3(5), 637–646.
Processing Systems (pp. 4424–4434). https://doi.org/10.1109/JIOT.2016.2579198
www.ijcat.com 73