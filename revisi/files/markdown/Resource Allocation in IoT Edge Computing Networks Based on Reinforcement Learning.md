# Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

> Source file: `Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning.pdf`

---

590

Intelligent Transportation and Smart Cities
V. Mezhuyev et al. (Eds.)
© 2025 The Authors.
This article is published online with Open Access by IOS Press and distributed under the terms
of the Creative Commons Attribution Non-Commercial License 4.0 (CC BY-NC 4.0).
doi:10.3233/ATDE250295

Resource Allocation in IoT Edge
Computing Networks Based on
Reinforcement Learning

Xian CUI1
Tai'an Aolifeng Community Medical Service Center, Tai'an, Shandong, 271000,
China

Abstract.  Efficient  resource  allocation  in  Internet  of  Things  (IoT)  networks
integrated  with  edge  computing  capabilities  is  critical  for  optimizing  system
performance,  reducing  latency,  and  managing  the  complex  interplay  between
heterogeneous devices. This paper proposes a novel reinforcement learning-based
framework to dynamically allocate resources in IoT edge computing networks. By
leveraging deep reinforcement learning (DRL), the proposed approach models the
intricate  relationships  between  varying  workloads,  device  heterogeneity,  and
fluctuating network conditions. The framework  employs adaptive task offloading
strategies  and  real-time  decision-making  to  improve  resource  utilization,  reduce
energy  consumption,  and  enhance  Quality  of  Service  (QoS).  Importantly,  this
interdisciplinary  method
intelligence,
integrates  advancements
distributed computing, and network optimization to address challenges across IoT-
enabled  domains  such  as  smart  cities,  healthcare,  and  industrial  automation.
Experimental evaluations on benchmark IoT scenarios demonstrate that the DRL-
based  method  significantly  outperforms  traditional  optimization  techniques  in
terms  of  computational  efficiency,  scalability,  and  robustness.  The  findings
underscore  the  potential  of  reinforcement  learning  in  tackling  complex  resource
allocation challenges in IoT edge computing networks, paving the way for smarter,
more adaptive network management solutions.

in  artificial

Keywords. IoT, edge computing, resource allocation, reinforcement learning, deep
learning, quality of service, dynamic optimization

1. Introduction

The convergence of the Internet of Things (IoT) and edge computing has transformed
how  data  is  processed  and  resources  are  managed  across  distributed  systems.  IoT
networks  generate  vast  amounts  of  real-time  data,  driving  the  need  for  efficient
resource  allocation  to  meet  the  dynamic  demands  of  applications  like  smart  cities,
precision healthcare, and industrial automation. Traditional optimization methods often
fall  short  in  addressing  the  challenges  posed  by  device  heterogeneity,  constrained
resources,  and  fluctuating  workloads  in  IoT  environments.  Reinforcement  learning
(RL), particularly deep reinforcement learning (DRL), has emerged as a powerful tool
for designing adaptive resource allocation strategies. DRL combines machine learning

(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)(cid:2)
1(cid:2)Corresponding Author: Xian Cui, xxzxcx@126.com.(cid:2)

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

591

with decision-making, enabling systems to autonomously optimize performance based
on  real-time  feedback.  By  bridging  concepts  from  computer  science,  operations
research,  and  network  engineering,  DRL  holds  potential  for  revolutionizing  resource
management in IoT-enabled systems.

Chen  et  al.  proposed  iRAF,  a  deep  reinforcement  learning  approach  for
collaborative mobile edge computing in IoT networks, demonstrating its capability to
enhance  resource  utilization  and  reduce  latency  in  dynamic  scenarios [1].  Chen  et  al.
further extended the application of DRL for dynamic resource management in mobile
IoT,  showcasing  significant
edge  computing  environments  within
improvements  in  computational  efficiency  [2].  Similarly,  Liu  et  al.  applied  DRL  to
optimize  offloading  and  resource  allocation  in  vehicle  edge  computing  networks,
achieving enhanced task execution efficiency and system performance [3].

industrial

In  mobile  edge  computing  (MEC),  advanced  optimization  methods  have  been
introduced to tackle multi-objective resource allocation problems. Vimal et al. utilized
a  reinforcement  learning-based  multi-objective  ant  colony  optimization  algorithm
(MOACO) to improve resource allocation efficiency in industrial IoT environments [4].
Tianqing  et  al.  explored  concurrent  federated  reinforcement  learning  for  resource
allocation in IoT edge computing, enabling distributed learning across multiple agents
to optimize resource utilization [5].

Blockchain  technology  has  also  been  integrated  with  reinforcement  learning  for
resource  allocation  in  IoT  edge  computing.  He  et  al.  proposed  a  blockchain-based
approach  that  leverages  DRL  to  ensure  secure  and  efficient  resource  allocation  while
maintaining  data  integrity  and  reducing  latency  [6].  Similarly,  Liu  et  al.  examined
resource  allocation  with  edge  computing  using  machine
techniques,
highlighting the potential of these methods to optimize task execution in heterogeneous
IoT networks [7].

learning

Reinforcement  learning  has  also  been  employed  in  multi-agent  systems  for
resource  allocation.  Liu  et  al.  introduced  a  multi-agent  reinforcement  learning
framework for IoT networks with edge computing, allowing agents to collaboratively
optimize  resources  under  dynamic  conditions  [8].  Another  multi-agent  approach  was
explored by Liu et al., demonstrating effective resource allocation for multiple users in
IoT edge computing environments [9].

Incorporating  deep  reinforcement  learning  into  IoT  edge  computing  has  led  to
further  advancements.  Xiong  et  al.  utilized  DRL  for  resource  allocation,  achieving
improved  system  efficiency  and  scalability  in  IoT  networks  [10].  Pei  et  al.  reviewed
federated  learning  methods  in  heterogeneous  scenarios,  providing  insights  into  how
federated  reinforcement  learning  can  be  applied  to  optimize  distributed  resource
allocation [11].

Khani  et  al.  proposed  a  deep  reinforcement  learning-based  resource  allocation
framework  for  multi-access  edge  computing  (MEC)  environments,  demonstrating  its
ability to optimize resource utilization under varying workloads. Their work highlights
the potential of DRL in addressing dynamic and heterogeneous resource management
challenges in edge computing scenarios [12]. Aghapour et al. developed a DRL-based
task  offloading  and  resource  allocation  algorithm  for  distributed  AI  execution  in  IoT
edge environments, demonstrating its applicability to complex computational tasks [13].
Tran-Dang  et  al.  conducted  a  comprehensive  review  of  reinforcement  learning
techniques  for  resource  management  in  fog  computing  environments,  identifying  key
challenges  and  open  issues.  Their  study  emphasizes  the  importance  of  adaptive
learning-based  methods  for  efficient  resource  allocation  in  distributed  systems  with

592

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

constrained resources [14].

This paper builds upon these advancements by proposing a reinforcement learning-
based  framework  for  resource  allocation  in  IoT  edge  computing  networks.  The
proposed approach leverages deep reinforcement learning to address the dynamic and
heterogeneous  nature  of  IoT  applications,  optimizing  resource  allocation  while
ensuring high QoS and energy efficiency. The remainder of this paper is structured as
follows:  Section  2  details  the  methodology,  including  the  reinforcement  learning
framework  and  system  architecture.  Section  3  presents  the  experimental  setup  and
results. Finally, Section 4 concludes with insights and future research directions.

2. Method

This  section  outlines  the  proposed  reinforcement  learning-based  resource  allocation
framework for IoT edge computing. The methodology integrates a deep reinforcement
learning  (DRL)  model  with  a  dynamic  task  allocation  strategy  to  optimize  resource
usage  and  minimize  latency  across  heterogeneous  IoT  networks.  The  framework  is
designed to adapt to varying workloads and device conditions, ensuring high efficiency
and scalability in edge environments.

2.1 System Architecture

The  system  architecture  of  the  proposed  reinforcement  learning-based  IoT  edge
computing framework is designed to efficiently manage the dynamic allocation of tasks
and  resources  in  a  distributed  environment.  The  architecture  integrates  IoT  devices,
edge  servers,  and  a  cloud  server  into  a  hierarchical  structure,  ensuring  scalability,
adaptability,  and  optimal  performance.  The  components  and  their  interactions  are
depicted in Figure 1, with the following key elements:

(cid:2)

IoT Devices: These devices serve as task generators, producing data-intensive
workloads  characterized  by  computational  requirements,  data  size,  and
latency  constraints.  Examples  include  sensors,  smart  appliances,  and  mobile
devices  that  are  part  of  an  IoT  ecosystem.  Each  device  is  equipped  with
communication capabilities to interact with nearby edge servers.

(cid:2)  Edge  Servers:  Acting  as  intermediate  computational  nodes,  edge  servers
provide localized processing to reduce latency and alleviate the workload on
the cloud server. They execute tasks offloaded from IoT devices and provide
real-time feedback on resource availability and execution status. Each server
is equipped with computational resources (e.g., CPU and GPU), memory, and
communication modules.

(cid:2)  Cloud Server: The cloud server functions as a central coordinator, managing
long-term  model  training,  storing  historical  data,  and  optimizing  global
resource  allocation  strategies.  It  periodically  updates  the  reinforcement
learning policy based on aggregated feedback from the edge servers.

(cid:2)  Communication  Layer:  This  layer  ensures  seamless  data  exchange  between
IoT  devices,  edge  servers,  and
the  cloud.  It  supports  bi-directional
communication  for  task  offloading,  resource  feedback,  and  policy  updates,
with mechanisms to minimize latency and bandwidth usage.

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

593

The architecture operates as follows: 1. IoT devices generate computational tasks
and  transmit  them  to  the  nearest  edge  servers.  2.  Edge  servers  analyze  the  incoming
tasks and determine whether to process them locally or offload them to the cloud server
using  the  reinforcement  learning-based  decision-making  framework.  3.  The  cloud
server aggregates feedback from all edge servers, optimizes the reinforcement learning
model,  and  updates  the  policies  distributed  to  the  edge  nodes.  4.  Real-time
communication  ensures  minimal  delay  in  task  execution  while  maintaining  efficient
resource utilization.

Figure 1. System architecture for IOT edge computing with reinforcement learning.

This  hierarchical  and  distributed  architecture  enables  scalable  and  adaptive
resource management, making it suitable for the dynamic and heterogeneous nature of
IoT edge computing environments.

2.2 Reinforcement Learning Framework

The  reinforcement  learning  (RL)  framework  is  the  core  component  of  the  proposed
system,  designed  to  dynamically  allocate  resources  and  offload  tasks  in  IoT  edge
computing  environments.  The  framework  leverages  the  Markov  Decision  Process
(MDP) to model the decision-making process, ensuring optimal performance in terms
of  task  latency,  resource  utilization,  and  energy  efficiency.  The  key  elements  of  the
framework are detailed below.

2.2.1. Problem Formulation

The  IoT  edge  computing  resource  allocation  problem  is  formulated  as  an  MDP  [15],
represented by a tuple (cid:2)(cid:3)(cid:4) (cid:5)(cid:4) (cid:6)(cid:4) (cid:7)(cid:4) (cid:8)(cid:9), where:

(cid:2)

(cid:10)(cid:4) (cid:7)(cid:15)

State  ((cid:3)):  The  system  state  includes  the  current  workload  of  IoT  devices,
resource availability at edge servers, and network conditions. Formally, (cid:3)(cid:10) (cid:11)
(cid:10) represents  the
(cid:12)(cid:13)(cid:14)
available resources of server (cid:19), and (cid:16)(cid:10) refers to the network bandwidth.
(cid:2)  Action  ((cid:5)):  The  action  space  consists  of  decisions  regarding  task  offloading
and  resource  allocation.  Actions  include  choosing  a  target  server  for

(cid:10) denotes  the  workload  of  device (cid:18), (cid:7)(cid:15)

(cid:10)(cid:4) (cid:16)(cid:10)(cid:17),  where (cid:13)(cid:14)

594

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

offloading and the amount of computational resources allocated.

(cid:2)  Transition  Probability  ((cid:6)):  The  probability  of  transitioning  to  a  new  state
given  the  current  state  and  action, (cid:6)(cid:2)(cid:3)(cid:10)(cid:20)(cid:21)(cid:22)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9),  is governed  by  the  system
dynamics and network conditions.

(cid:2)  Reward ((cid:7)): The reward function incentivizes actions that minimize latency,

energy consumption, and system overhead. It is defined as:

(cid:7)(cid:10) (cid:11) (cid:23)(cid:2)(cid:24) (cid:25) (cid:26)(cid:10) (cid:27) (cid:28) (cid:25) (cid:29)(cid:10) (cid:27) (cid:8) (cid:25) (cid:30)(cid:10)(cid:9)
(1)
where (cid:26)(cid:10)  is  the  task  latency, (cid:29)(cid:10)  is  the  energy  consumption,  (cid:30)(cid:10)  is  the  resource

utilization, and (cid:24)(cid:4) (cid:28)(cid:4) (cid:8) are weight parameters.

(cid:2)  Discount  Factor  ((cid:8)):  A  factor (cid:2)(cid:31)   (cid:8)   !(cid:9) that  balances  the  importance  of

immediate rewards versus long-term benefits.

2.2.2. Deep Q-learning Implementation

To  handle  the  high-dimensional  and  continuous  state-action  space,  we  implement  a
deep Q-learning (DQL) approach, which combines Q-learning with a neural network to
approximate the Q-value function. The Q-value function "(cid:2)(cid:3)(cid:4) (cid:5)(cid:9) is updated iteratively
as:

"(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9) # "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9) (cid:27) (cid:24) $(cid:7)(cid:10) (cid:27) (cid:8)%&’
()

"(cid:2)(cid:3)(cid:10)(cid:20)(cid:21)(cid:4) (cid:5)*(cid:9) (cid:23) "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9)+

(2)

where (cid:24) is the learning rate.
The  neural  network,  parameterized  by  , ,  predicts  "(cid:2)(cid:3)(cid:4) (cid:5)(cid:9)  and  is  trained  by

minimizing the loss function:

(cid:26)(cid:2),(cid:9) (cid:11) - $./(cid:10) (cid:23) "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)0 ,(cid:9)1

2

+

(3)

where  /(cid:10) (cid:11) (cid:7)(cid:10) (cid:27) (cid:8)%&’()"(cid:2)(cid:3)(cid:10)(cid:20)(cid:21)(cid:4) (cid:5)*0 ,3(cid:9)  and  ,3  represents  the  target  network

parameters.

2.2.3. Exploration-exploitation Trade-off
The 4-greedy policy is used to balance exploration and exploitation. With probability 4,
the agent selects a random action to explore new strategies, and with probability ! (cid:23) 4,
it chooses the action with the highest Q-value. The exploration rate 4 decays over time
to favor exploitation as the learning progresses.

2.2.4. Multi-agent Coordination

Given  the  distributed  nature  of  IoT  edge  computing,  the  RL  framework  employs  a
multi-agent  reinforcement  learning  (MARL)  approach.  Each  edge  server  acts  as  an
agent, independently optimizing resource allocation while collaborating through shared
policy  updates.  The  centralized  cloud  server  aggregates  these  updates  and  refines  the
global policy using federated learning techniques.

2.2.5. Workflow of the RL Framework

The workflow of the RL framework proceeds as follows: 1. IoT devices generate tasks
and  send  them  to  edge  servers.  2.  Each  edge  server,  as  an  RL  agent,  evaluates  the

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

595

current  state (cid:3)(cid:10) and  selects  an  action (cid:5)(cid:10) based  on  its  policy.  3.  The  selected  action  is
executed,  and  the  resulting  reward (cid:7)(cid:10)  and  new  state (cid:3)(cid:10)(cid:20)(cid:21)  are  recorded.  4.  The  Q-
network  is  updated  based  on  the  observed  transitions,  and  the  policy  is  refined.  5.
Periodically,  the  cloud  server  aggregates  local  models,  performs  global  updates,  and
distributes the refined policy back to the edge servers.

This  reinforcement  learning  framework  enables  adaptive  and  efficient  resource
allocation in dynamic IoT environments, ensuring low latency, energy efficiency, and
high system throughput.

2.3. Dynamic Task Allocation Strategy

The  dynamic  task  allocation  strategy  lies  at  the  core  of  the  proposed  reinforcement
learning-based  framework,  enabling  the  efficient  distribution  of  computational  tasks
across  IoT  devices,  edge  servers,  and  cloud  resources.  The  strategy  is  designed  to
dynamically  adapt  to  the  varying  computational  demands,  resource  availability,  and
network  conditions,  ensuring  optimal  utilization  of  resources  and  maintaining  high
system performance.

The  task  allocation  process  is  formalized  as  an  optimization  problem,  where  the
objective  is  to  minimize  a  cost  function 5 representing  the  trade-off  between  latency,
energy consumption, and task completion rate. The cost function is defined as:

5 (cid:11) (cid:24) (cid:25) (cid:26) (cid:27) (cid:28) (cid:25) (cid:29) (cid:27) (cid:8) (cid:25) (cid:7)

where:

(4)

(cid:26) is the total task latency.

(cid:2)
(cid:2)  (cid:29) is the total energy consumption.
(cid:2)  (cid:7) is the penalty for unmet task deadlines.
(cid:2)  (cid:24)(cid:4) (cid:28)(cid:4) (cid:8) are weight coefficients that balance the trade-offs among the objectives.
State Representation: The system state at time 6 is represented as:
(cid:3)(cid:10) (cid:11) (cid:12)7(cid:10)(cid:4) (cid:7)(cid:10)(cid:4) (cid:16)(cid:10)(cid:17)
(5)
where 7(cid:10) denotes the set of incoming tasks with their computational demands and
deadlines, (cid:7)(cid:10)  represents  the  available  computational  and  network  resources,  and (cid:16)(cid:10)
reflects the network conditions (e.g., bandwidth, latency).

Action Space: The action space includes possible task allocation decisions:
(cid:5)(cid:10) (cid:11) (cid:12)8(cid:14)(cid:4)(cid:15)9(cid:22)98(cid:14)(cid:4)(cid:15) (cid:11) ! if task (cid:18) is assigned to resource (cid:19)(cid:4) else (cid:31)(cid:17)

(6)

where 8(cid:14)(cid:4)(cid:15) is a binary variable indicating whether task (cid:18) is allocated to resource (cid:19).
Reward  Function:  The  reward  function  is  designed  to  guide  the  reinforcement

learning agent toward optimal task allocation. It is defined as:

(cid:7)(cid:10) (cid:11) (cid:23)5(cid:10) (cid:27) : (cid:25) (cid:30)(cid:10)
(7)
where 5(cid:10)  is  the  cost  function, (cid:30)(cid:10)  represents  the  resource  utilization,  and : is  a

scaling factor that emphasizes resource efficiency.

Policy  Learning:  The  task  allocation  strategy  is  learned  using  a  deep  Q-learning
network  (DQN).  The  Q-value "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9) represents  the  expected  cumulative  reward  of
taking  action (cid:5)(cid:10) in  state (cid:3)(cid:10) and  following  the  learned  policy  thereafter.  The  Q-values
are updated iteratively as:

596

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

"(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9) # "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9) (cid:27) ; <(cid:7)(cid:10) (cid:27) (cid:8)%&’
(=>?

"(cid:2)(cid:3)(cid:10)(cid:20)(cid:21)(cid:4) (cid:5)(cid:10)(cid:20)(cid:21)(cid:9) (cid:23) "(cid:2)(cid:3)(cid:10)(cid:4) (cid:5)(cid:10)(cid:9)@

(8)

where:

; is the learning rate.
(cid:8) is the discount factor.

(cid:2)
(cid:2)
(cid:2)  (cid:7)(cid:10) is the immediate reward for action (cid:5)(cid:10).
(cid:2)

(cid:3)(cid:10)(cid:20)(cid:21) is the next state after taking action (cid:5)(cid:10).

Exploration and Exploitation: To balance exploration and exploitation, an 4-greedy
policy  is  employed.  The  agent  selects  a  random  action  with  probability  4  and  the
optimal action based on current Q-values with probability ! (cid:23) 4. The exploration rate 4
decays over time to encourage convergence toward the optimal policy.

Dynamic Adaptation: The dynamic task allocation strategy continuously monitors
system  states  and  updates  its  allocation  decisions  in  real-time.  When  resource
availability  or  network  conditions  change,  the  learned  policy  adapts  by  re-evaluating
the  Q-values  and  reallocating  tasks  as  necessary.  This  adaptability  ensures  resilience
against dynamic and uncertain IoT environments.

Illustrative  Example:  Consider  a  scenario  with  three  tasks A(cid:21)(cid:4) A2(cid:4) AB and  two  edge
servers (cid:29)(cid:21)(cid:4) (cid:29)2 .  Each  task  has  specific  computational  demands,  and  each  server  has
limited capacity. The dynamic strategy evaluates all possible allocations, computes the
associated costs, and selects the allocation minimizing 5. For instance, A(cid:21) C (cid:29)(cid:21), A2 C
(cid:29)2, and AB C (cid:29)(cid:21) might yield the best balance of latency and energy consumption.

This  dynamic

learning,
demonstrates the ability to optimize resource utilization and system performance while
adapting to real-time changes in IoT edge computing environments.

task  allocation  strategy,  driven  by  reinforcement

2.4. Workflow of the Framework

The  workflow  of  the  proposed  framework  can  be  summarized  as  follows:  1.  IoT
devices  generate  tasks  and  send  their  descriptions  to  edge  servers.  2.  Edge  servers
evaluate  the  tasks  and  make  offloading  decisions  using  the  DRL  model.  3.  Tasks  are
processed  locally or  offloaded  to  the  cloud based  on  the decisions. 4. Feedback  from
task execution is used to update the DRL model and improve future decisions.

This  framework  ensures  efficient  resource  allocation  and  high-quality  service

delivery, making it suitable for diverse IoT edge computing scenarios.

3. Experiment

3.1. Experimental Setup and Procedure

To  evaluate  the  effectiveness  of  the  proposed  reinforcement  learning-based  resource
allocation  framework,  we  conducted  extensive  experiments  in  a  simulated  IoT  edge
computing  environment.  The  environment  simulates  a  real-world  scenario  involving
IoT  devices,  edge  servers,  and  network  conditions.  The  experimental  setup  and
procedure are detailed as follows:

(1)  Simulation  Environment:  The  simulated  IoT  network  consists  of  100  IoT
devices, 10 edge servers, and a centralized cloud server. The IoT devices generate tasks

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

597

with  random  computational  demands  and  deadlines.  Each  edge  server  has  limited
computational  resources  and  serves  a  specific  geographical  region.  The  simulation
includes dynamic network bandwidth variations and server load fluctuations to mimic
real-world conditions.

(2)  Baseline  Methods:  We  compared  the  proposed  method  with  the  following

baseline approaches:

(cid:2)  Greedy  Algorithm:  Allocates  resources  to  tasks  based  on  the  lowest  current

latency without considering future states.

(cid:2)  Round  Robin  (RR):  Cyclically  assigns  tasks  to  edge  servers,  ensuring  equal

distribution but ignoring task-specific requirements.

(cid:2)  Heuristic  Optimization  (HO):  Utilizes  pre-defined  rules  for  task  offloading

and resource allocation.

(cid:2)  Traditional Q-Learning (QL): Applies basic Q-learning for resource allocation

without deep learning enhancements.

(3) Performance Metrics: The evaluation metrics include:
(cid:2)  Task Latency: The average time taken to complete a task.
(cid:2)  Energy Consumption: Total energy consumed by the IoT network.
(cid:2)  Resource  Utilization:  The  percentage  of  available  resources  utilized  by  the

(cid:2)

system.
System Throughput: The total number of tasks successfully processed within
a time frame.

(4)  Training  Configuration:  The

framework  was
implemented  using  Python  and  PyTorch.  The  Q-network  consists  of  three  fully
connected  layers  with  ReLU  activation  functions.  The  learning  rate was  set  to  0.001,
and  the  discount  factor  ((cid:8))  was  set  to  0.9.  The  exploration  rate  (4)  started  at  1.0  and
decayed  to  0.1  over  100  episodes.  Each  experiment  was  conducted  for  500  episodes,
and the results were averaged over 10 runs for consistency.

reinforcement

learning

3.2. Results and Analysis

The experimental results demonstrate the effectiveness of the proposed reinforcement
learning framework in optimizing resource allocation and task offloading. Key findings
are presented and analyzed below.

Task Latency: Figure 2 shows the average task latency for different methods. The
proposed framework achieved the lowest latency, reducing it by 25% compared to the
greedy  algorithm  and  18%  compared  to  traditional  Q-learning.  This  improvement  is
attributed  to  the  dynamic  adaptability  of  the  RL-based  approach,  which  optimally
assigns resources based on real-time system states.

Energy  Consumption:  Figure  3  illustrates  the  energy  consumption  of  the  IoT
network. The proposed method consumed 15% less energy than heuristic optimization
and  20%  less  than  the  round-robin  approach.  By  minimizing  unnecessary  task
migrations  and  allocating  resources  efficiently,  the  framework  significantly  reduces
energy usage.

Resource  Utilization:  The  resource  utilization rates  are  depicted  in  Figure  4.  The
proposed method achieved a utilization rate of 92%, outperforming all baselines. This
indicates  the  ability  of  the  framework  to  fully  leverage  available  resources  while

598

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

avoiding over-provisioning.

Figure 2. Comparison of task latency across different methods.

Figure 3. Comparison of energy consumption across different methods.

Figure 4. Comparison of resource utilization across different methods.

System  Throughput:  The  proposed  framework  also  demonstrated  higher
throughput, processing 30% more tasks than the greedy algorithm and 15% more than
heuristic  optimization.  The  adaptability  of  the  RL-based  approach  allows  it  to  handle
more tasks efficiently, even under high-load conditions.

3.3. Discussion of Results

the  superior  performance  of

The  experimental  results  validate
the  proposed
reinforcement  learning  framework  in  optimizing  IoT  edge  computing  resource
allocation.  The  reduction  in  latency  and  energy  consumption  is  primarily  due  to  the
ability of the framework to make informed decisions based on real-time system states.
Additionally,  the  high  resource  utilization  and  system  throughput  highlight  the
scalability  and  robustness  of  the  approach.  While  the  framework  outperforms
traditional  methods,  its  performance  can  be  further  enhanced  by  incorporating
advanced techniques such as transfer learning and multi-agent coordination for larger-
scale networks.

X. Cui / Resource Allocation in IoT Edge Computing Networks Based on Reinforcement Learning

599

4. Conclusion

traditional  methods

in  IoT  edge  computing,  effectively  reducing

This study proposes a reinforcement learning-based framework for optimizing resource
latency,  energy
allocation
consumption, and improving resource utilization. Experimental results demonstrate its
superiority  over
in  adaptability  and  efficiency.  However,
challenges  remain,  such  as  high  computational  costs  in  training  and  sensitivity  to
network  fluctuations.  Future  work  will  focus  on  integrating  federated  learning  for
distributed  model  training,  enhancing  scalability  through  multi-agent  reinforcement
learning, and incorporating hybrid AI techniques for improved decision-making. These
advancements  will  further  strengthen  the  framework’s  applicability  in  large-scale,
dynamic IoT environments.

task

Reference

[1]  Chen J, Chen S, Wang Q, et al. iRAF: A deep reinforcement learning approach for collaborative mobile

edge computing IoT networks. IEEE Internet of Things Journal, 2019 6(4):7011-7024.

[2]  Chen Y, Liu Z, Zhang Y, et al. Deep reinforcement learning-based dynamic resource management for
mobile  edge  computing  in  industrial  internet  of  things.  IEEE  Transactions  on  Industrial  Informatics,
2020 17(7):4925-4934.

[3]  Liu Y, Yu H, Xie S, et al. Deep reinforcement learning for offloading and resource allocation in vehicle
edge computing and networks. IEEE Transactions on Vehicular Technology. 2019 68(11):11158-11168.
[4]  Vimal  S,  Khari  M,  Dey  N,  et  al.  Enhanced  resource  allocation  in  mobile  edge  computing  using
reinforcement learning based MOACO algorithm for IIOT. Computer Communications. 2020 151:355-
364.

[5]  Tianqing Z, Zhou W, Ye D, et al. Resource allocation in IoT edge computing via concurrent federated

reinforcement learning. IEEE Internet of Things Journal. 2021 9(2):1414-1426.

[6]  He  Y,  Wang  Y,  Qiu  C,  et  al.  Blockchain-based  edge  computing  resource  allocation  in  IoT:  A  deep

reinforcement learning approach. IEEE Internet of Things Journal. 2020 8(4):2226-2237.

[7]  Liu  X,  Yu  J,  Wang  J,  et  al.  Resource  allocation  with  edge  computing  in  IoT  networks  via  machine

learning. IEEE Internet of Things Journal. 2020 7(4):3415-3426.

[8]  Liu  X,  Qin  Z,  Gao  Y.  Resource  allocation  for  edge  computing  in  IoT  networks  via  reinforcement
learning//ICC 2019-2019 IEEE international conference on communications (ICC). IEEE. 2019 1-6.
[9]  Liu X, Yu J, Feng Z, et al. Multi-agent reinforcement learning for resource allocation in IoT networks

with edge computing. China Communications. 2020 17(9):220-236.

[10]  Xiong X, Zheng K, Lei L, et al. Resource allocation based on deep reinforcement learning in IoT edge

computing. IEEE Journal on Selected Areas in Communications. 2020 38(6):1133-1146.

[11]  Pei J, Liu W, Li J, et al. A Review of Federated Learning Methods in Heterogeneous scenarios. IEEE

Transactions on Consumer Electronics. 2024.

[12]  Khani M, Sadr M M, Jamali S. Deep reinforcement learning‐based resource allocation in multi‐access
edge computing. Concurrency and Computation: Practice and Experience, 2024, 36(15): e7995.
[13]  Aghapour Z, Sharifian S, Taheri H. Task offloading and resource allocation algorithm based on deep
reinforcement  learning  for  distributed  AI  execution  tasks  in  IoT  edge  computing  environments.
Computer Networks. 2023 223:109577.

[14]  Tran-Dang H, Bhardwaj S, Rahim T, et al. Reinforcement learning based resource management for fog
computing  environment:  Literature  review,  challenges,  and  open  issues.  Journal  of  Communications
and Networks. 2022 24(1):83-98.

[15]  Aghapour Z, Sharifian S, Taheri H. Task offloading and resource allocation algorithm based on deep
reinforcement  learning  for  distributed  AI  execution  tasks  in  IoT  edge  computing  environments.
Computer Networks. 2023 223:109577.

