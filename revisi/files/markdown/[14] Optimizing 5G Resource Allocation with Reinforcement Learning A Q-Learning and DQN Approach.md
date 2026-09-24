# [14] Optimizing 5G Resource Allocation with Reinforcement Learning A Q-Learning and DQN Approach

> Source file: `[14] Optimizing 5G Resource Allocation with Reinforcement Learning A Q-Learning and DQN Approach.pdf`

---

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
Optimizing 5G Resource Allocation with
Reinforcement Learning: A Q-Learning and Deep
Q-Network (DQN) Approach

|     |     | Basem M. Alrifai  |     |     | 1,*, Loiy Alsbatin  | 2, and Firas Zawaideh  |     |     |     | 3   |     |     |
| --- | --- | ----------------- | --- | --- | ------------------- | ---------------------- | --- | --- | --- | --- | --- | --- |
1 Faculty of Information Technology, Computer Science Department, Jadara University, Irbid, Jordan
2 Electrical Engineering Department, Al-Balqa Applied University, Amman 11134, Jordan
3 Faculty of Information Technology, Networks and Cybersecurity Department, Jadara University, Irbid, Jordan
Email: b.rifai@jadara.edu.jo (B.M.A.); loiy.alsbatin@bau.edu.jo (L.A.); f.zawaideh@jadara.edu.jo (F.Z.)
*Corresponding author

Abstract—Simulation using a Network Simulator-3 (NS-3)- However, current solutions still fall short when it comes
based setup enables realistic testing under varying network  to real-time adaptability and generalization across varying
| densities  | and  channel  | conditions.  |     | The  proposed  | Deep   |     |     |     |     |     |     |     |
| ---------- | ------------- | ------------ | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
5G use cases. Rule-based methods struggle with scalability,
Q-Network (DQN)-based approach is benchmarked against
while conventional Machine learning (ML) techniques
| recent  deep  | reinforcement  |     | learning  | methods,  | achieving  |     |     |     |     |     |     |     |
| ------------- | -------------- | --- | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
often require large labeled datasets and lack the ability to
performance improvements of up to 25.7% in throughput,
learn dynamically. As 5G networks evolve to support
31.5% latency reduction, and 27.4% energy savings. Q-
|     |     |     |     |     |     | Ultra-Reliable  | Low-Latency  |     | Communication  |     | (URLLC)  |     |
| --- | --- | --- | --- | --- | --- | --------------- | ------------ | --- | -------------- | --- | -------- | --- |
Learning offers simpler scalability and faster convergence in
and massive Internet of Things (IoT) deployments, there is
| low-complexity  | scenarios.  |     | These  findings  |     | confirm  the  |     |     |     |     |     |     |     |
| --------------- | ----------- | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
promise of reinforcement learning as a core enabler for  a  growing  need  for  intelligent  systems  capable  of
autonomous and adaptive 5G resource management and as  autonomous learning and rapid adaptation. This research
an  efficient  and  scalable  method  for  intelligent  5G  is motivated by the pressing demand for such solutions,
management. The success of DQN in this domain can be  aiming to explore reinforcement learning strategies that
attributed to its integration of deep neural architectures that
|     |     |     |     |     |     | can  effectively  |     | balance  | throughput,  | latency,  |     | energy  |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ------------ | --------- | --- | ------- |
can learn intricate interactions among channel quality, user
efficiency, and fairness in complex wireless environments.
| demand,  | and  interference  |     | patterns,  | in  conjunction  | with  |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | ---------- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Reinforcement learning, in contrast with supervised
experience replay and target networks. Notably, this method
attained significant fairness and energy efficiency without the  methods, allows agents to discover optimal policies by
need  for  explicit  fairness  constraints  in  the  reward  interacting with an environment via trial-and-error. Two of
formulation,  underscoring  the  robustness  of  the  the leading RL methods, such as Q-Learning and Deep
generalizability of the learned policies.
Q-Networks (DQN), provide promising avenues for real-
|     |     |     |     |     |     | time resource management by relating perceived network  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Keywords—fifth-Generation  (5G),  reinforcement  learning,  states  to  optimal  actions,  such  as  allocating  power,
Q-Learning, Deep Q-Network (DQN), resource allocation,  frequency, or bandwidth.
network slicing
Our work bridges this essential gap in adaptive and

|     |     |     |     |     |     | scalable  5G       | resource  |                   | management  | by              | providing  | a    |
| --- | --- | --- | --- | --- | --- | ------------------ | --------- | ----------------- | ----------- | --------------- | ---------- | ---- |
|     |     |     |     |     |     | comparative study  |           | and  application  |             | of  Q-Learning  |            | and  |
I.  INTRODUCTION
DQN algorithms. We make the following contributions:
The  development  of  wireless  communication  has  •  An  in-depth  literature  review  of  5G  resource
brought about the use of fifth-Generation (5G) cellular  management using Reinforcement Learning.
networks with features, such as ultra-low latency, massive
|     |     |     |     |     |     | •  A  | theoretical  | underpinning  |     | of  Q-Learning  |     | and  |
| --- | --- | --- | --- | --- | --- | ----- | ------------ | ------------- | --- | --------------- | --- | ---- |
connectivity, and large communication capacity. Yet these  DQN, such as mathematical modeling.
| capabilities are only possible with efficient and intelligent  |     |     |     |     |     | •   |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Suggested structure with details of implementation.
| resource  | management  | schemes.  |     | Static  or  | rule-based  |     |     |     |     |     |     |     |
| --------- | ----------- | --------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
•  Experimental testing with Network Simulator-3
methods  are  not  suited  for  dealing  with  the  high- (NS-3) over synthetic datasets.
| dimensional  | and  | stochastic  | nature  | of  | modern  5G  |     |     |     |     |     |     |     |
| ------------ | ---- | ----------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
•  Comparative performance metrics against baseline
| environments.  | Consequently,  |     |     | machine  | learning,  |     |     |     |     |     |     |     |
| -------------- | -------------- | --- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
and traditional models.
particularly Reinforcement Learning (RL), has been a  The rest of this paper is structured in the following way:
promising solution for these issues.
Section II contains a literature review. Section III discusses
the methods and the proposed framework. Section IV
discusses the results. Section V concludes with future
|     |     |     |     |     |     | directions.  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Manuscript received June 12, 2025; revised June 27, 2025; accepted
August 6, 2025; published November 14, 2025.
| doi: 10.12720/jait.16.11.1586-1594 |     |     |     |     |     | 1586 |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
II. LITERATURE REVIEW continuous state spaces, Q-Learning faces issues with
scalability.
Exponential growth in mobile traffic demands and
This limitation is catered for by Deep Q-Networks
device connectivity, especially with 5G evolution, has
(DQN), which employ deep networks to approximate the
attracted significant interest in intelligent resource
Q-function. Zhou et al. [12] apply DQN to radio and cache
allocation methods. Heuristic-based methods and classical
optimisation by employing knowledge transfer between
optimization techniques, though optimal in some special
segments of networks. Liu et al. [13] employ DQN with
circumstances, are incapable of addressing dynamic,
massive MIMO Channel State Information (CSI) to
high-dimensional wireless environments. Reinforcement
improve accuracy in downlink beamforming.
Learning (RL), especially model-free methodologies, such
Sun et al. [14] show that DQN is applicable for green fog
as Q-Learning and Deep Q-Networks (DQN), has been a
computing by optimal computation offloading and power
promising approach to increase 5G network adaptability
levels. These papers all indicate reduced latency and
and performance. This section critically overviews the
increased spectral efficiency over traditional or greedy
literature under five thematic topics: (1) 5G network
allocation.
resource allocation, (2) techniques in wireless networks
There have been comparative assessments conducted in
based on ML, (3) 5G application of RL, (4) Q-Learning
various studies. Chen et al. [15] and Alsharoa et al. [16]
and DQN models, and (5) comparative studies.
compared rule-based, convex optimization, and RL-based
5G networks present new performance indicators like
approaches, with RL optimizing better under changing
ultra-low latency, high density of devices, and increased
user loads and channel conditions. Comparing deep RL
throughput that require adaptive resource
with traditional interference coordination methods,
allocation [1, 2]. Li et al. [2] discuss how network slicing
Mismar et al. [1] established up to 23% gains in
makes radio resource allocation complex due to
throughput. Liu et al. [17] made a comparison between
heterogeneity in Service-Level Agreements (SLAs).
computational costs of DQN and Q-Learning, determining
Zhang et al. [3] discuss the problem of mobility-aware
trade-offs between performance and convergence time.
allocation in network slicing, pointing to the shortcomings
Ye et al. [7] show that although tabular Q-Learning
of static scheduling mechanisms.
converges better earlier, over time, DQN’s ability to
Machine learning (ML) has been widely applied to
generalise is better, particularly in non-stationary
enhance network optimization. Zhang et al. [3] offer a
environments. Elsayed and Erol-Kantarci [18] identify
Deep Learning (DL) survey of wireless network
some of the challenges of deploying RL, such as reward
applications, highlighting their performance in
engineering, state observability, and delayed feedback.
classification, prediction, and decision-making. Similarly,
While Q-Learning and DQN have been studied
Chen et al. [4] describe how neural networks and
comprehensively, most past work centers on individual
supervised learning can be implemented across various
sub-problems like caching, edge computing, or
layers of the wireless stack. Supervised methods need to
beamforming. End-to-end multi-objective resource
use sizable labeled collections of examples, however,
management frameworks that trade off between latency,
which fail in unknown environments, such as the shortfalls
throughput, and energy remain under-exploited.
that support the popularity of RL.
Surprisingly, comparative study of Q-Learning and DQN
In contrast, reinforcement learning is naturally
under benchmark 5G scenarios is scarce. This paper
applicable in dynamic environments. Shi et al. [5]
attempts to address these shortfalls by conceiving and
illustrate that RL-based slice methods perform better than
comparing both Q-Learning and DQN under an end-to-end
traditional rule-based policies in Radio Access Network
5G resource management unified framework.
(RAN) slicing. Zhou et al. [6] extend to multi-agent
Despite the abundance of recent literature finding
correlated Q-Learning for simultaneous radio and cache
significant advances toward the extension of RL to 5G
management. Ye et al. [7] and He et al. [8] illustrate that
networks, the bulk of the prior work is narrow-scope or
RL systems can adaptively modify resource allocations in
focuses on a single component such as beamforming [1],
vehicular and Mobile Edge Computing (MEC) networks
network slicing [2], or vehicular networks [7]. For
with minimized latency and better Quality of Service
example, Mismar et al. [1] explored joint beamforming
(QoS).
and interference coordination by DRL, while
Sun et al. [9] examine RL-based mode choice and
Zhou et al. [6] used multi-agent Q-learning to slicing, but
mobility management in fog radio access networks,
did not compare base RL algorithms like Q-Learning and
indicating the strength of RL in long-term reward
DQN by benchmarking. Liu et al. [17] addressed massive
maximization. Tang et al. [10] warn that performance
MIMO by DRL yet did not mention the discussion about
benefits of RL are often tied to parameterizing exploration-
the analysis of the convergence and the trade-off of
exploitation trade-offs and reward functions, in exchange
scalability. Additionally, a series of papers [4, 13] offer
for stability and convergence rates.
introductions about DL/DRL for wireless systems, yet
Basic Q-Learning is implemented in early works for
avoid running and comparing several RL algorithms
optimizing user association and spectrum allocation.
through a single setup of a 5G scenario. In an effort to
Wang et al. [11] employ tabular Q-Learning to perform
cover these gaps, our work presents a comparative analysis
uplink/downlink resource scheduling with better energy
of Q-Learning and DQN, which were both validated
efficiency compared to heuristics. Yet, with large or
through a virtual 5G RAN setup by NS-3. Table I
1587

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
summarizes recent work and shows the novelty of the  Cao   et  al.  [21],  through  simulation,  compare  DQN,
current work.  Double DQN, and Dueling DQN for co-serving eMBB and
In  more  recent  studies,  Habib  et  al.  [19]  employ  URLLC, and show improved network utility and QoE.
DQN‑based traffic steering of 5G multi‑RAT systems and  Though these studies are complementary to our work, none
achieve  significant  throughput  and  delay  advantages.  of  them  make  a  direct  tabular  Q‑Learning  vs  deep
Kalbkhani and Kunz [20] put forward an energy‑efficient  Q‑networks  head‑to‑head  comparison  within  the  same
DRL‑based  RAN  slicing  resource  allocation  strategy.  NS‑3 modeled 5G system.
TABLE I. SUMMARY OF RECENT DRL-BASED 5G RESOURCE ALLOCATION STUDIES
|     | Study  | Method  |     | Focus  |     |     | Limitation  |     | Gap addressed by our work  |     |     |     |     |
| --- | ------ | ------- | --- | ------ | --- | --- | ----------- | --- | -------------------------- | --- | --- | --- | --- |
Beamforming,
Mismar et al. [1]  DRL  No QL vs DQN benchmarking  We compare both methods head-to-head
interference
MA-Q-
Zhou et al. [6]  Learning  RAN slicing  No scalability testing  We test on 100 UEs under congestion
Zhou et al. [12]  Transfer DQN  Caching + Radio  No analysis of tabular methods  We include both tabular QL and DQN
No convergence trade-off
Liu et al. [17]  DRL  Massive MIMO  We compare convergence and scalability
study
[3, 4, 13]  Surveys  ML in wireless  No experimental evaluation  We simulate NS-3 and analyze results
Sun et al. [14]  DRL  Fog RANs  Limited to power offloading  We optimize multiple KPIs (QoS, energy,
fairness)

Algorithm 1: Q-Learning Pseudocode
III. MATERIALS AND METHODS  1:  Initialize Q(s, a) arbitrarily for all s   S, a   A
2:  Repeat for each episode:
In order to construct an effective reinforcement learning
|     |     |     |     |     |     |     | 3:  Initialize state s  |     |     |     | ∈ ∈ |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
approach to 5G resource scheduling, there is a need to  4:  Repeat for each step:
comprehend the governing mathematical concepts of Q- 5:      Choose action a from s using ε-greedy policy
Learning, together with Deep Q-Networks (DQN). This  6:      Take action a, observe reward r and next state s’
7:      Update Q(s, a):
section discusses the major concepts, formalisms, and
8:      Q(s, a) ← Q(s, a) + α [r + γ max_a’ Q(s’, a’) - Q(s, a)]
issues involved with these learning algorithms in dynamic,
9:       s← s’
high-dimensional wireless network scenarios.
10:  until s is terminal
| A.  | Reinforcement Learning Foundations  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Q-Learning works well in small, discrete state-action
|     | Reinforcement  | Learning  |     | (RL)  is  | a  goal-oriented  |     |     |     |     |     |     |     |     |
| --- | -------------- | --------- | --- | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
spaces but suffers from state-space explosion in high-
learning paradigm wherein an agent interacts with an
environment ε over discrete time steps. The agent selects  dimensional environments like 5G networks.
|           |     |                                     |     |     |                |     | DQN            | addresses  | Q-Learning’s  |       | limitations  |       | by      |
| --------- | --- | ----------------------------------- | --- | --- | -------------- | --- | -------------- | ---------- | ------------- | ----- | ------------ | ----- | ------- |
| actions a |     | ∈A based on the current state s     |     |     | ∈δ, receives   |     |                |            |               |       |              |       |         |
|           |     | t                                   |     |     | t              |     | approximating  | the        | Q-function    | with  | a            | Deep  | Neural  |
| a reward  |     | ℝ, and transitions to a new state s |     |     | t+1 . The aim  |     |                |            |               |       |              |       |         |
Network (DNN) parameterized by weights θ.
| is to learn a policy π:δ→A |     |                       |     | that maximizes the expected  |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                            |     | 𝑡𝑡                    |     |                              |     |     |     |     |     |     |     |     |     |
| cumulativ𝑟𝑟e               |     |  d∈iscounted reward:  |     |                              |     |     |     |     |     |     |     |     |     |
Algorithm 2: DQN Pseudocode
|     |     |     |  ∞ |    |     |     | 1:  Initialize Q-network with weights θ  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
∑γtr
  E  (1)  2:  Initialize target network with weights θ⁻ ← θ
 t 
|     |     |     | t=0 |     |     |     | 3:  Initialize replay memory D  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
4:  Repeat for each episode:
| where  |     |  is  | the  discount  | factor  | indicating  | the  |     |     |     |     |     |     |     |
| ------ | --- | ---- | -------------- | ------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
5:      Initialize state s
| importance of future rewards  |     |     |     |     |     |     | 6:      Repeat for each step:  |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
𝛾𝛾 ∈[0,1) 7:          With probability ε select random action a
B.  Q-Learning
8:          Otherwise select a = argmax_a Q(s, a; θ)
Q-Learning is an off-policy, model-free RL algorithm  9:          Execute action a, observe r, s’
that learns an action-value function Q(s, a), representing  10:        Store (s, a, r, s’) in D
11:        Sample mini-batch from D
the expected reward for taking action a in state s, and
12:        For each (s_j, a_j, r_j, s’_j) compute:
thereafter following the optimal policy. The Q-value is
13:           y_j = r_j + γ max_a’ Q(s’_j, a’; θ⁻)
updated using the Bellman equation:
14:      Perform gradient descent on (y_j - Q(s_j, a_j; θ))²
Q(s,a)←Q(s,a)+α ,a′)−Q(s,a)  15:        Every C steps: θ⁻ ← θ
|     |     |     | r   | +γmaxQ(s |     |  (2)  |                    |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | ----- | ------------------ | --- | --- | --- | --- | --- | --- |
|     | t t | t t | t  | a′ t+1   | t   | t    | 16:        s ← s’  |     |     |     |     |     |     |
17:  until s is terminal
where:

•  α is the learning rate.  We chose to investigate tabular Q-Learning and Deep
•  r  is the immediate reward.
|     | t   |     |     |     |     |     | Q-Network  | (DQN)  | because  | they  | represent  | two  | key  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ----- | ---------- | ---- | ---- |
•  γ is the discount factor.  approaches in model-free RL, each suitable for different
•  maxQ(s ,a′)  estimates  the  future  reward  complexity levels in 5G resource allocation.
t+1
a′
assuming optimal actions.
1588

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
•
|     | Q-Learning is virtually optimal in discrete and  |     |     |     |     |     |     | D.  Proposed Framework  |     |     |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
small-scale  state  spaces  and  features  fast  In  response  to  the  dynamic  and  multi-dimensional
convergence with minimal computation. It remains
|     |     |     |     |     |     |     |     | nature  | of  5G  | resource  | allocation,  | we  introduce  | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --------- | ------------ | -------------- | --- |
fully interpretable through its Q-value tables and  reinforcement  learning-based  approach  with  both
can  converge  to  optimal  policies  with  enough  Q-Learning and Deep Q-Networks (DQN). This approach
exploration and training.
targets resource allocation in the Radio Access Network
•
DQN, by contrast, replaces the Q-table with a  (RAN)  layer,  optimizing  spectral  efficiency,  reducing
neural  network  approximator,  enabling  it  to  latency, and saving energy in high-density user scenarios.
|     | manage  |     | high-dimensional  |     | and           | continuous  | state  |                          |     |     |     |     |     |
| --- | ------- | --- | ----------------- | --- | ------------- | ----------- | ------ | ------------------------ | --- | --- | --- | --- | --- |
|     | spaces  |     | efficiently.      | It  | incorporates  | experience  |        | E.  Problem Formulation  |     |     |     |     |     |
replay  and  a  target  network,  which  stabilize  We model the 5G resource allocation task as a Markov
learning in complex environments.  Decision Process (MDP) defined by the tuple:
For instance, in grid-world domains with small state
=(δ,A,P,R,γ)
|     |     |     |     |     |     |     |     |     |     | M   |     |     | (4)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
spaces, tabular Q-Learning typically outperforms DQN
due to lower complexity and variance.
where:
However, when state spaces are large—as is common in
•  S: Set of environment states (e.g., traffic load,
5G  scenarios  including  CQI  levels,  buffer  statuses,  channel quality, user location).
interference, and UE mobility—a neural network-based
|           |     |       |               |     |            |     |             | •   | A : Set of actions (e.g., assigning RBs, scheduling  |     |     |     |     |
| --------- | --- | ----- | ------------- | --- | ---------- | --- | ----------- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
| approach  |     | like  | DQN  becomes  |     | essential  | to  | generalize  |     |                                                      |     |     |     |     |
time slots, adjusting power levels).
effectively across previously unseen states.
•  P: State transition probabilities (learned implicitly).
By comparing these two complementary methods under
•  R: Reward function (based on throughput, energy,
| identical  |     | NS-3  | simulations,  |     | our  study  | examines  | the   |     |     |     |     |     |     |
| ---------- | --- | ----- | ------------- | --- | ----------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
latency).
| trade-offs     |     | between   |     | simplicity,  |              | interpretability,  |     |     |               |     |         |                            |     |
| -------------- | --- | --------- | --- | ------------ | ------------ | ------------------ | --- | --- | ------------- | --- | ------- | -------------------------- | --- |
|                |     |           |     |              |              |                    |     | •   | γ:  Discount  |     | factor  | to  prioritize  long-term  |     |
| computational  |     | demands,  |     | and          | performance  | scalability,       |     |     |               |     |         |                            |     |
performance.
providing practitioners with clear guidance on choosing an
appropriate approach based on system constraints.
|     |     |     |     |     |     |     |     | F.  State Space Design  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
The DQN uses experience replay and target networks to
Each agent (e.g., base station or scheduler) observes a
stabilize training:
|     |     |     |     |     |     |     |     | state vector  |     | ℝ   | , consisting of:  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ----------------- | --- | --- |
•  Channel Qu𝑛𝑛ality Indicator (CQI) for each user.
|     |     |     | (  | xQ(s′,a′;θ−)−Q(s,a;θ) |     |     | )2 |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L(θ)=E (s,a,r,s′)~D r+γm a   (3)  Buff𝑠𝑠e 𝑡𝑡 r ∈length/Queue size.
|     |     |     |    | a ′ |     |     |    | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•  Resource Block (RB) usage.
where:
•  User Equipment (UE) location or mobility level.
•  ℒ is Loss Function.
•  Interference level.
•  D is a replay buffer of past experiences.  The  high  dimensionality  of  this  state  makes  DQN
|     | •   |  are weights of the target network, periodically  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
particularly suitable.
u−pda0ted from θ.
|     |     |     |     |     |     |     |     | G.  Action Space  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
DQN𝜃𝜃 significantly improves learning in continuous or
large-scale state spaces typical in 5G environments, such  Actions a ∈A  are composed of:
t
| as  | channel  |     | states,  | user  | positions,  | and  | load  |     |     |     |     |     |     |
| --- | -------- | --- | -------- | ----- | ----------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
•  RB assignment: Which RB to allocate to each UE.
levels  [4,  5,  22].
•  Power level: Transmission power per RB.
C.  Challenges in Reinforcement Learning (RL) for 5G  •  Scheduling: Time slot selection.
For Q-Learning, discrete actions are used. For DQN, we
Resource Allocation
Despite their strength, both Q-Learning and DQN have  use a parameterized action space encoded as a vector to be
fed into the neural network.
individual challenges in wireless environments:
•  Exploration vs. Exploitation: An ε-greedy policy
|     |     |     |     |     |     |     |     | H.  Reward Function Design  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
will not perform well in swiftly changing channels.
|     |     |     |     |     |     |     |     | The  | reward  | function  | balances  | three  competing  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | --------- | ----------------- | --- |
•  Reward Engineering: Informative reward design is
objectives:
complicated in multi-objective environments, such
|     |     |     |     |     |     |     |     | r   | =λ⋅throughput |     | −λ⋅latency | −λ⋅energy |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | --------- | --- |
as  achieving  latency,  energy,  and  throughput    τ τ τ τ    (5)
|     |     |     |     |     |     |     |     |     | 1   |     | 2   | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
balances.
where:
|     | •  Scalability:                                   |     | State  | and  | action  | spaces  | grow  |     |       |                                       |     |     |     |
| --- | ------------------------------------------------- | --- | ------ | ---- | ------- | ------- | ----- | --- | ----- | ------------------------------------- | --- | --- | --- |
|     |                                                   |     |        |      |         |         |       | •   | λ , λ | , λ are weights set via grid search.  |     |     |     |
|     | exponentially with an increase in network sizes.  |     |        |      |         |         |       |     | 1 2   | 3                                     |     |     |     |
•  Throughput is measured in Mbps.
|     | •  Partial  | Observability:  |     | Owing  |     | to  CSI  | delay  and  |     |     |     |     |     |     |
| --- | ----------- | --------------- | --- | ------ | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
mobility, agents usually respond to partial state  •  Latency is penalized above a QoS threshold.
•  Energy is measured per bit transmitted.
information.
Double  DQN,  Prioritized  Experience  Replay,  and  This multi-objective reward helps train policies that
Multi-Agent Reinforcement Learning (MARL) have been  prioritize system-wide efficiency.

| proposed  |     | in  | literature  |     | to  | counter  | these  |     |     |     |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
shortcomings  [2,  3,  11].
1589

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
I. Q-Learning Architecture L. Experimental Setup
We implement standard Q-Learning using a Q-table In order to assess the performance of our proposed
with states indexed by discretized CQl, buffer size, and UE reinforcement learning system, we implemented an
distance. Due to scalability issues, this is tested only for extensive simulation environment that mimics a standard
small network topologies. 5G Radio Access Network (RAN). This environment
enables controlled but realistic experimentation with
Algorithm 3: Simplified Q-Learning Resource Allocation dynamic user movement, variable channel conditions, as
1: Initialize Q-table for all state-action pairs well as interference modeling. The test setup was made
2: Repeat for each frame t:
such that both tabular Q-Learning and Deep Q-Network
3: Observe state s_t = [CQI, Buffer, Location]
(DQN) agents could be trained and tested under similar
4: Choose a_t using ε-greedy policy
conditions.
5: Execute a_t: allocate RB and power
We established the simulation environment using
6: Observe reward r_t and next state s_{t+1}
7: Update Q(s_t, a_t) ← Q(s_t, a_t) + α[r_t + γ max Q(s_{t+1}, Network Simulator-3 (NS-3), which is well known for
a’) - Q(s_t, a_t)] being extensible as well as providing accurate modeling of
8: s_t ← s_{t+1} wireless protocols. We utilized the 5G New Radio (NR)
module to incorporate major features, such as Time
J. Deep Q-Network (DQN) Architecture Division Duplexing (TDD), dynamic access spectrums,
and separation between the control-plane and user-plane.
DQN leverages a 3-layer feedforward neural network
We simulated a small cell deployment environment in a
with ReLU activations and dropout. The input is the
1 km² urban grid with several gNodeBs (gNBs) and up to
normalized state vector, and the output layer predicts Q-
100 mobile UE nodes. User movement was modeled with
values for all possible actions. Table II shows the network
a random waypoint model with velocity distributions from
specifications for input, output, and hidden layers.
0 to 5 m/s for simulating pedestrian-level movements. The
• Replay Buffer: Stores 100,000 transitions.
UEs generate bursty traffic sessions based on a Poisson
• Batch Size: 64.
arrival process, while the channels of the wireless link
• Optimizer: Adam (lr = 0.0001).
were modeled based on 3 GPP Urban Microcell path loss
• Target Update Frequency: Every 500 steps.
with Rayleigh fading models to represent realistic link
behavior.
TABLE II. NETWORK SPECIFICATIONS
For Q-Learning and DQN trials, the state space was
Layer Type Size Activation formulated from the present Channel Quality Indicators
Input Dense 128 neurons ReLU (CQIs), UE queuing lengths, resource block use, and
Hidden 1 Dense 256 neurons ReLU
estimated inter-cell interference. State parameters in Q-
Hidden 2 Dense 128 neurons ReLU
Output Dense - A Learning were discretized to ensure manageable Q-table
sizes, but with state vector normalization passed to a neural
network approximator in DQN. Action spaces in both
K. Architecture Diagram
methods consisted of RB allocation, adjustment of power
Both Q-Learning and DQN agents are modularly levels, and scheduling each UE, but in different forms:
integrated by the architecture. Q-Learning achieves fast index-based in Q-Learning versus vectorized encoding in
convergence for small-scale scenarios (e.g., ≤ 10 UEs). DQN.
But, for practical deployments (e.g., 100 UEs, dynamic The training dataset and evaluation dataset were
topology), DQN is advantageous in terms of being synthesized using simulations. Two data sets were
scalable, adaptive, and sustaining better QoS, which is prepared through the NS-3 simulator—a training set and a
depicted in Fig. 1. testing set. Each set contains roughly 50,000 transitions,
which are rich with dynamic interactions of the agents with
the network environment. State vector contains the
following five major parameters: Channel Quality
Indicator (CQI), buffer size of the UE, resource block
utilization, user location (mobility level), and interference
estimate. Action space includes the RB allocation, power
level adjustment, and scheduling-related decisions.
The benefits of a synthetic dataset include good
parameter control, deterministic simulation worlds, and
the ability to select variable load conditions for the
purposes of a benchmark. However, the significant
disadvantage is abstraction from real data, such that factors
such as hardware latency, variation of user behavior, and
unpredictable patterns of interference may influence
performance.
Fig. 1. Architecture diagram.
1590

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
Several limitations structured our experimental design. IV. RESULT AND DISCUSSION
In the first place, NS-3 models don’t exactly replicate real
In this section, we provide an end-to-end evaluation of
fading behavior with heavy mobility, which might affect
the proposed reinforcement learning-based approach with
generalizability. We had complete CSI at all decision
both Q-Learning and Deep Q-Network (DQN) methods.
points as well—best-case, essentially-never-achievable
Performance is compared with respect to main metrics,
conditions for real-time systems. The simulation ran with
such as system throughput, average latency, energy
a static traffic trace, with no bursty nor streaming sources,
efficiency, fairness, and convergence behavior under
which might minimize peak-time variation. Hardware,
various network loads. These are selected to represent
running DQN with an NVIDIA RTX 3090, was
main Quality of Service (QoS) requirements for 5G.
constrained by 24 GB VRAM, which set the ceiling for
Performance is compared with that of a standard greedy
batch size and replay buffer size. Finally, the state-space
baseline scheduler and a rule-based heuristic model widely
was binned down to five features, which constrains our
applied in LTE and the early 5G rollouts.
exploration of higher-dimensional encodings of the state.
Tens of thousands of transitions were produced by each A. System Throughput
run in the simulations, which were pooled together and
System throughput, expressed in aggregate UE data rate
stored in a replay buffer for DQN or were fed directly to
over all equipment, is an important metric of spectral
updates of the Q-table in Q-Learning. Specifically, the use
efficiency. Under light load (20 UE), all methods showed
of experience replay for DQN was particularly helpful,
similar performance. But with increasing network density,
with a buffer capacity of 100,000 transitions retained to
gains of learning-based allocation were increasingly
remove temporal dependency between experiences.
evident. Under 100 UE conditions, DQN performed better
During each training step, mini-batches of 64 were drawn
than Q-Learning and heuristics baselines by 18.3% and
uniformly before performing gradient updates by descent.
25.7%, respectively. This improvement stems from
Minimization of squared difference between predicted and
DQN’s capability to learn over high-dimensional state
target Q-values was done using loss function, with an
representations and to adaptively maximize high-quality
Adam optimizer with a learning rate of 0.0001.
transmission chances. Q-Learning is not so efficient under
Additionally, there was an auxiliary target network that
conditions of congestion but still registered an 11.6%
was updated every 500 training steps to stabilize learning.
improvement compared with the rule-based scheduler.
Training in Q-Learning was carried out over 5,000
episodes, Both the Q-Learning episodes and DQN B. Average Latency
episodes had a 10-second simulation interval, which was Latency was measured as the mean end-to-end delay
equivalent to 5,000 episodes for full training. For DQN, suffered by packets under simulation runs. DQN was able
the agent was trained for 100,000-time steps, while early to decrease latency under heavy traffic because of its
stopping was enabled when the average cumulative reward dynamic scheduling along with load-aware allocation of
remained unchanged for a window of 1,000 steps. For a resources. Under full load, DQN decreased average
balance of the tendency to converge and the number of latency by 31.5% over the greedy baseline and by 21.2%
iterations, these parameters were chosen after preliminary over Q-Learning. This is consistent with work by
tests to avoid overfitting and to enable proper learning Zhou et al. [6] and Sun et al. [14], which found that
convergence, with one episode consisting of a 10-second DQN’s temporal abstraction allowed for more anticipatory
simulation interval. Learning rates (ααα) and discount traffic control. Q-Learning improved latency but was
factors (γγγ) were 0.1 and 0.99, respectively, with slower to respond under sudden traffic changes because of
exploration done through an ε-greedy policy decaying less representational capacity.
from 1.0 to 0.1 over training time. For DQN, training was
C. Energy Efficiency
carried out over 100,000-time steps with early stopping
initiated if average reward was constant over 1,000 steps. Energy consumed per transmitted bit was taken as a
All model training and simulations were carried out on measure for energy efficiency. DQN performed better in
a system with an Intel Core i9 processor (3.6 GHz, 16 terms of energy saving, especially with varying
cores), 64 GB RAM, and an NVIDIA RTX 3090 GPU with interference. Thanks to adaptive power control developed
24 GB memory. TensorFlow 2.9.0 was used to implement through training, DQN avoided redundant transmissions
models for DQN, and NumPy was used for Q-Learning. and unwanted retransmissions. With respect to the
Matplotlib and Pandas were used for logging, heuristic model, energy consumption per megabit was
visualization, and evaluation. reduced by 27.4% using DQN and 15.2% using Q-
It was tested under different load scenarios: light Learning. Results validate existing work [5, 16], which
(20 UEs), moderate (50 UEs), and heavy (100 UEs) to indicate the capability of RL in adapting physical layer
ensure the stability of the proposed RL-based methods. factors with network-level goals.
Statistical performance was obtained for each setup over
D. Fairness Index
10 random trials to consider random initialization and
Jain’s Fairness Index (JFI) was adopted to measure
environmental randomness. Performance indicators, such
resource distribution fairness among users. During
as throughput, average delay, energy efficiency, and
medium and heavy loads, DQN achieved a greater fairness
convergence time, were captured and analyzed in the
score (0.94) than Q-Learning (0.89) and the heuristic
subsequent section.
approach (0.81). This means that the neural network was
1591

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
successful in detecting under-served users and giving them  latency, as well as a 27.4% boost in energy efficiency, with
priority  without  degrading  overall  performance.  similar or better efficiency despite a comparatively simpler
Significantly, we achieved fairness gains even without  design. While multi-agent and transfer-based techniques
explicitly adding fairness terms to the reward function,  promote  expanded  scalability  and  efficiency  during
indicating that multi-dimensional state inputs naturally led  learning, the techniques are coupled with greater system
to more fair decisions.  sophistication and computation overhead. Our work finds
a balance point between the rewards of performance and
E.  Convergence Behavior
the realizability of the design in real-world 5G systems.
|     | Convergence  |     | of  training  | was  | tracked  | by  | observing  |                   |        |           |     |               |
| --- | ------------ | --- | ------------- | ---- | -------- | --- | ---------- | ----------------- | ------ | --------- | --- | ------------- |
|     |              |     |               |      |          |     |            | Future  research  | could  | continue  | to  | extend  such  |
moving average of cumulative rewards for episodes. Q- benchmarking  through  the  actual  implementation  of
Learning converged swiftly under light-load environments
|      |          |              |     |        |     |          |            | Dueling  DQN  | or  MARL  | structures  | for  | additional  |
| ---- | -------- | ------------ | --- | ------ | --- | -------- | ---------- | ------------- | --------- | ----------- | ---- | ----------- |
| but  | stopped  | progressing  |     | early  | in  | densely  | populated  |               |           |             |      |             |
performance characterization under distributed settings.
environments with its poor generalization. By comparison,  Figs. 2–4 visualize these comparisons with box plots and
DQN  made  slower  early  gains  but  recorded  better  convergence curves.
| cumulative  |     | rewards  |     | later  on  | with  | complex  | policy  |     |     |     |     |     |
| ----------- | --- | -------- | --- | ---------- | ----- | -------- | ------- | --- | --- | --- | --- | --- |

architectures optimized by network weights. Interestingly,
DQN stabilized at around 40,000 steps, with Q-Learning
converging in 2,000 episodes in light-load environments.
These findings are consistent with trade-offs presented by
Tang et al. [10] and Liu et al.  [17], supporting choice
based on application scope.
|     | The  | Q-Learning  |     | method  | required  | much  | fewer  |     |     |     |     |     |
| --- | ---- | ----------- | --- | ------- | --------- | ----- | ------ | --- | --- | --- | --- | --- |
computations since it utilized tabular Q-values and state-
action mappings that were discrete. For training with more
than 5,000 episodes, it took roughly 12 Minutes per CPU
(Intel Core i9, 3.6 GHz) with minimal use of the GPU. For

DQN, as a contrast, a deep neural net was required to be
learned by 100,000-time steps, which consumed roughly  Fig. 2. Throughput comparison.
2.5 h with extensive use of the GPU (NVIDIA RTX 3090,
~20–24 GB VRAM used). Memory usage was likewise
| higher  | for  | DQN,  | as  | a  result  | of  the  | buffer  | holding  |     |     |     |     |     |
| ------- | ---- | ----- | --- | ---------- | -------- | ------- | -------- | --- | --- | --- | --- | --- |
experiences (100,000 transitions) as well as the weights of
the network. Such figures establish the trade-off between.
performance and resource usage: Q-Learning enables fast
| convergence  |     | for  | small  | environments,  |     | while  | DQN  has  |     |     |     |     |     |
| ------------ | --- | ---- | ------ | -------------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
improved scaling properties though it necessitates higher
computation and time.
F.  Comparative Summary
|     | Table III summarizes the quantitative results across key  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
metrics, averaged over 10 trials for statistical robustness.  Fig. 3. Latency over time.
TABLE III. PERFORMANCE COMPARISON OF Q-LEARNING, DQN, AND
BASELINE MODELS
|     | Metric               |     |     | Baseline  | Q-Learning  |       | DQN       |     |     |     |     |     |
| --- | -------------------- | --- | --- | --------- | ----------- | ----- | --------- | --- | --- | --- | --- | --- |
|     | Throughput (Mbps)    |     |     | 125.6     | 140.2       |       | 165.3     |     |     |     |     |     |
|     | Latency (ms)         |     |     | 78.4      |             | 62.7  | 53.7      |     |     |     |     |     |
|     | Energy (mJ/Mb)       |     |     | 12.1      |             | 10.3  | 8.8       |     |     |     |     |     |
|     | Fairness Index       |     |     | 0.81      |             | 0.89  | 0.94      |     |     |     |     |     |
|     | Convergence (steps)  |     |     | N/A       | ~2,000      |       | ~40,000   |     |     |     |     |     |
|     | DR (%)               |     |     | 86.5±2.2  | 91.3±1.8    |       | 94.7±1.5  |     |     |     |     |     |
|     | Jitter (ms)          |     |     | 14.2±2.5  | 11.8±1.9    |       | 10.1±1.6  |     |     |     |     |     |

|     | To  further  | validate  |     | our  results,  |     | we  compared  | the  |     |     |     |     |     |
| --- | ------------ | --------- | --- | -------------- | --- | ------------- | ---- | --- | --- | --- | --- | --- |
intended Q-Learning and DQN models with the work of

existing deep reinforcement learning techniques put forth
Fig. 4. DQN convergence curve.
| in  | the  literature.  |     | For  | instance,  | Mismar  |     | et  al.  [1]  |     |     |     |     |     |
| --- | ----------------- | --- | ---- | ---------- | ------- | --- | ------------- | --- | --- | --- | --- | --- |
demonstrated a 23% improvement in throughput via actor- These figures confirm that while both Q-Learning and
critic-based coordination, while Zhou et al. [12] utilized
DQN significantly outperform conventional approaches,
transfer-learning-based DQN for resource caching. For a
DQN remains the most suitable solution for high-density
point of contrast, our DQN model demonstrated a 25.7%  5G environments where scalability and adaptability are
| better improvement in throughput, a 31.5% reduction in  |     |     |     |     |     |     |     | critical.   |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
1592

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
In order to analyze the strength of the DQN model, a hardware, as well as unforeseen interference sources.
sensitivity analysis was performed for the discount factor Providing safe exploration and policy stability during real
(γ) and the learning rate (α) since these have a significant deployments remains another major problem, which
effect on convergence and performance. We changed γ should be addressed through appropriate validation and
from 0.85 to 0.99 and α from 0.00005 to 0.001. As can be fail-safe mechanisms in spite of these encouraging results,
witnessed from the data listed in Table IV, a γ of 0.99 and there are certain challenges and limitations. Use of
a 0.0001 learning rate provided the optimum balance of synthetic datasets and simulator-based training, albeit
balance and speed of learning. Lower values of γ resulted methodologically strong, restrict direct deployment in the
in short-sighted policies, while too high values of α real world. The training process, particularly for DQN, is
resulted in unstable learning. also computationally expensive with the need for manual
hyperparameters tuning to ensure convergence. Further,
TABLE IV. SENSITIVITY OF DQN PERFORMANCE TO Γ AND LEARNING this study’s reward function was handcrafted and may not
RATE comprehensively represent all performance goals of
γ / α 0.00005 0.0001 0.001 operating 5G networks.
0.85 153.2 Mbps 156.0 Mbps 145.7 Mbps In view of these restrictions, we identify various
0.95 160.8 Mbps 164.3 Mbps 150.1 Mbps avenues for future work. In light of the positive results of
0.99 162.5 Mbps 165.3 Mbps 151.4 Mbps
this work, several improvements are recommended as
0.85 153.2 Mbps 156.0 Mbps 145.7 Mbps
future work. First, the adoption of Multi-Agent
Reinforcement Learning (MARL) would enable
V. CONCLUSION
distributed agents (e.g., a number of gNodeBs) to produce
In this paper, we introduced an end-to-end joint decisions for improved scalability. Secondly,
reinforcement learning paradigm for dynamic resource Federated Reinforcement Learning (FRL) could train
management in 5G networks based on both standard models in geographically expanded networks while
Q-Learning and Deep Q-Network (DQN) methodologies. preserving user privacy and reducing data transmission
We showed, via large-scale simulation-based overhead. Moreover, compatibility with real-time SDN
experimentation over an accurate 5G RAN test bed controllers and edge computing infrastructures could
simulated in NS-3, that learning-based policies can enable on-the-fly learning and adaptive decision-making.
considerably beat rule-based and heuristics approaches in Lastly, executing the models over a real or emulated 5G
major performance metrics like throughput, latency, testbed would provide assurance about the robustness and
energy efficiency, and fairness among users. practicality of the approach outside simulation.
Our findings indicated that DQN with function Advantages of the Proposed System:
approximation ability and temporal abstraction performed • Joint comparison: Unlike previous work, our
better than Q-Learning in scenarios with high-density experiment supplies a vigorous, head-to-head
users and dynamic channel conditions in wireless systems. analysis of tabular Q-Learning and DQN under the
Q-Learning achieved better convergence speeds on small same simulation conditions.
scales but lacked generalizability in large state spaces • Performance enhancements: DQN achieves 25.7%
since it is based on tables. DQN, on the contrary, could higher throughputs, 31.5% lower latency, and
learn and implement better allocation policies under 27.4% energy savings than the existing RL-based
rapidly changing environments with up to 25.7% and heuristic algorithms.
improvement in terms of throughput performance and • Computational balance: Q-Learning achieves fast
31.5% decrease in latency over traditional schedulers. learning with low hardware, and DQN achieves
The achievement of DQN in this area can be credited to scalability for varying scenarios—providing
its combination of deep neural architectures with the practitioners with adaptability depending on the
ability to learn complex interaction between channel availability of resources.
quality, user demand, and interference patterns, along with • Holistic optimization of KPI: Both approaches
experience replay, and target networks. Notably, the
improve fairness and packet delivery, enabling
approach achieved high fairness and energy efficiency
better QoS for a number of 5G performance
without using explicit fairness constraints in the
metrics.
formulation of reward, which highlights the strength of
• Simplified deployment: Installation on NS-3 with
generalizability of the learnt policies.
standard Python libraries ensures reproducibility
Despite promising simulation outcomes, several
and future incorporation into testbeds.
deployment challenges continue to hinder extending these
One direction is the use of Multi-Agent Reinforcement
reinforcement learning models to real 5G systems.
Learning (MARL), by which distributed agents learn
Inaccurate and late collection of real-time CSI at a central
together to maximize resources at connected base stations.
point can hinder decision-making. Real-time
This would improve scalability and better represent
inference/training at the edge involves ultra-low latency
decentralized networks in the real world. Another way is
processing, which may become difficult to achieve with
to use Federated Reinforcement Learning (FRL) for model
resource constraints. Generalizability of the models is
training between geographically dispersed nodes without
another problem, as the network itself dynamically
central collection of data to preserve privacy and keep
changes with changing user demands, variation of
communication overhead minimal.
1593

Journal of Advances in Information Technology, Vol. 16, No. 11, 2025
In addition, Hierarchical Reinforcement Learning [6] H. Zhou, M. Elsayed, and M. Erol-Kantarci, “RAN resource slicing
(HRL) could facilitate more organized decision-making so in 5G using multi-agent correlated Q-learning,” IEEE Trans. Netw.
Service Manag., vol. 18, no. 3, pp. 3060–3073, 2021.
that individual agents could manage such sub-tasks as
doi: 10.1109/TNSM.2021.3092235
power distribution, RB scheduling, and mobility [7] H. Ye, G. Y. Li, and B. Juang, “Deep reinforcement learning based
management. Future developments could extend to resource allocation for V2V communications,” IEEE Trans. Veh.
scenarios of real-time deployment with online learning Technol., vol. 68, no. 4, pp. 3163–3173, 2019.
doi: 10.1109/TVT.2019.2894764
mechanisms, coupled with live network telemetry for
[8] Y. He, N. Zhao, and H. Yin, “Integrated networking, caching, and
ongoing policy optimization. Finally, evaluation under an computing for connected vehicles: A deep reinforcement learning
emulated or experimental 5G testbed would close the loop approach,” IEEE Trans. Veh. Technol., vol. 67, no. 1, pp. 44–55,
between trial-and-error development in simulations and 2018. doi: 10.1109/TVT.2017.2754640
[9] Y. Sun, M. Peng, Y. Zhou et al., “Application of machine learning
future deployment realism with impactful findings on
in wireless networks: Key techniques and open issues,” IEEE
system resilience, latency under hardware limits, and with Commun. Surv. Tutor., vol. 21, no. 4, pp. 3072–3108, 2019.
SDN platforms. doi: 10.1109/COMST.2019.2912562
In short, this piece reaffirms the potential of [10] J. Tang et al., “Enabling deep learning for 5G with system-level
considerations,” IEEE Netw., vol. 32, no. 6, pp. 28–34, 2018.
reinforcement learning, especially DQN, as an efficient
doi: 10.1109/MNET.2018.1800100
and scalable method for intelligent 5G management. By [11] S. Wang, Y. Wang, and J. Zhang, “Energy efficient resource
filling in gaps present so far and expanding the model via allocation method for 5G access network based on deep Q-network,”
distributed, federated, and real-time learning frameworks, J. Netw. Comput. Appl., vol. 190, no. 103141, 2021.
doi: 10.1016/j.jnca.2021.103141
future studies can further unlock AI-driven wireless
[12] H. Zhou, M. Erol-Kantarci, and H. V. Poor, “Learning from peers:
communication network potential. Deep transfer reinforcement learning for joint radio and cache
resource allocation in 5G RAN slicing,” IEEE J. Sel. Areas
Commun., vol. 39, no. 8, pp. 2380–2394, 2021.
CONFLICT OF INTEREST
doi: 10.1109/JSAC.2021.3079387
The authors declare no conflict of interest. [13] Y. Liu, Y. Shi, and Y. T. Hou, “Deep learning for next-generation
wireless networks: A comprehensive survey,” IEEE Commun.
Surv. Tutor., vol. 22, no. 4, pp. 2693–2724, 2020.
AUTHOR CONTRIBUTIONS doi: 10.1109/COMST.2020.2993603
[14] H. Sun et al., “Deep reinforcement learning-based mode selection
Study conception and design: Basem Mohamad Alrifai, and resource management for green fog radio access networks,”
Firas Zawaideh; data collection: Loiy Alsbatin; analysis IEEE Internet Things J., vol. 6, no. 2, pp. 1960–1971, 2019.
and interpretation of results: Basem Mohamad Alrifai, doi: 10.1109/JIOT.2018.2878323
[15] X. Chen, L. Jiao, W. Li, and X. Fu, “Efficient multi-user
Loiy Alsbatin; draft manuscript preparation: Basem
computation offloading for mobile-edge cloud computing,”
Mohamad Alrifai, Firas Zawaideh. All authors reviewed IEEE/ACM Trans. Netw., vol. 24, no. 5, pp. 2795–2808, 2016.
the results and approved the final version of the doi: 10.1109/TNET.2015.2487344
manuscript. [16] A. Alsharoa et al., “Energy-efficient resource allocation for cache-
enabled cloud radio access networks with mobile edge computing,”
IEEE Trans. Green Commun. Netw., vol. 3, no. 3, pp. 664–681,
ACKNOWLEDGMENT 2019. doi: 10.1109/TGCN.2019.2911494
[17] J. Liu, Y. Shi, and L. Xie, “Energy-efficient resource allocation for
The authors are grateful to the Deanship of Scientific
5G massive MIMO with deep reinforcement learning,” IEEE Trans.
Research at Jadara University for providing financial Veh. Technol., vol. 68, no. 6, pp. 6264–6276, 2019.
support for this publication. doi: 10.1109/TVT.2019.2915155
[18] M. Elsayed and M. Erol-Kantarci, “AI-enabled future wireless
networks: Challenges, opportunities, and open issues,” IEEE Veh.
REFERENCES Technol. Mag., vol. 14, no. 3, pp. 70–77, 2019.
doi: 10.1109/MVT.2019.2921162
[1] F. B. Mismar, B. L. Evans, and A. Alkhateeb, “Deep reinforcement
[19] M. A. Habib, H. Zhou, P. E. Iturria-Rivera et al., “Traffic steering
learning for 5G networks: Joint beamforming, power control, and
for 5G multi-RAT deployments using deep reinforcement learning,”
interference coordination,” IEEE Trans. Commun., vol. 68, no. 3,
in 2023 IEEE 20th Consumer Communications & Networking
pp. 1581–1592, 2020. doi: 10.1109/TCOMM.2020.2964209
Conference (CCNC), 2023, pp. 164–169.
[2] X. Li, X. Wang, and V. C. M. Leung, “Network slicing for 5G:
[20] H. Kalbkhani and T. Kunz, “Energy efficient deep reinforcement
Challenges and opportunities,” IEEE Internet Things J., vol. 6, no.
learning assisted resource allocation for 5G RAN slicing,” IEEE
2, pp. 1249–1271, 2019. doi: 10.1109/JIOT.2018.2881537
Trans. Veh. Technol., vol. 71, no. 5, pp. 5387–5402, 2023.
[3] C. Zhang, P. Patras, and H. Haddadi, “Deep learning in mobile and
doi: 10.1109/TVT.2022.3142318
wireless networking: A survey,” IEEE Commun. Surv. Tutor., vol.
[21] T. Cao et al., “Slicing resource allocation based on dueling DQN
21, no. 3, pp. 2224–2287, 2019.
for eMBB and URLLC in 5G,” Sensors, vol. 23, no. 5, p. 2518,
doi: 10.1109/COMST.2019.2904897
2023. doi: 10.3390/s23052518
[4] M. Chen, U. Challita, W. Saad et al., “Artificial neural networks-
[22] J. Wang, C. Jiang, H. Zhang et al., “Thirty years of machine
based machine learning for wireless networks: A tutorial,” IEEE
learning: The road to Pareto-optimal wireless networks,” IEEE
Commun. Surv. Tutor., vol. 21, no. 4, pp. 3039–3071, 2019.
Commun. Surv. Tutor., vol. 22, no. 3, pp. 1472–1514, 2020.
doi: 10.1109/COMST.2019.2926624
doi: 10.1109/COMST.2020.2986183
[5] Y. Shi, Y. E. Sagduyu, and T. Erpek, “Reinforcement learning for
dynamic resource optimization in 5G radio access network slicing,”
IEEE Trans. Cogn. Commun. Netw., vol. 6, no. 3, pp. 763–773, Copyright © 2025 by the authors. This is an open access article
2020. doi: 10.1109/TCCN.2020.2992922 distributed under the Creative Commons Attribution License which
permits unrestricted use, distribution, and reproduction in any medium,
provided the original work is properly cited (CC BY 4.0).
1594