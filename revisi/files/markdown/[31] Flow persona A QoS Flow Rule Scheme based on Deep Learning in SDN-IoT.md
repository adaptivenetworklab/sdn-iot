# [31] Flow persona A QoS Flow Rule Scheme based on Deep Learning in SDN-IoT

> Source file: `[31] Flow persona A QoS Flow Rule Scheme based on Deep Learning in SDN-IoT.pdf`

---

Computer Networks 273 (2025) 111784
Contents lists available at ScienceDirect
Computer Networks
journal homepage: www.elsevier.com/locate/comnet
Flow persona: A QoS Flow Rule Scheme based on Deep Learning in
SDN-IoT
Hao She a,b,c, Lixing Yana,b,c, Xin Ana,b,c, Chuanfeng Mao a,b,c, Yongan Guo a,b,c,∗
aCollege of Telecommunications & Information Engineering, Nanjing University of Posts and Telecommunications, Nanjing, 210003, China
bJiangsu Key Laboratory of Intelligent Information Processing and Communication Technology, Nanjing University of Posts and Telecommunications, Nanjing, 210003,
China
cEdge Intelligence Research Institute, Nanjing University of Posts and Telecommunications, Nanjing, 210003, China
a r t i c l e i n f o a b s t r a c t
Keywords: With the proliferation of Internet of Things (IoT) devices and increasing network flow, traditional network ar-
SDN-IoT chitectures struggle to manage complex flow and meet evolving Quality of Service (QoS) requirements. These
Flow Persona architectures lack flexibility in resource allocation and optimization, limiting their support for diverse IoT ap-
ARIMA
plications. To address these issues, we propose a QoS Flow Rule Scheme based on Deep Learning in Software
APSO
Defined Networking-IoT (SDN-IoT) called Flow Persona. This scheme integrates user personas and QoS require-
QoS flow classification
ments, employs an ARIMA model for traffic prediction, and leverages a Convolutional Neural Network (CNN)
optimized by Adaptive Particle Swarm Optimization (APSO) for flow classification. Simulation results show that
flow persona improves QoS flow classification accuracy by about 4.6% over traditional and existing algorithms.
It also significantly enhances precision, recall, and F-score, while improving QoS routing efficiency and reducing
network delay.
1. Introduction paradigm, has become a foundational technology in modern 5G and IoT
communication networks [1]. By decoupling the data plane from the
In recent years, with the rapid development of network technol- control plane, SDN provides a centralized global view of the network and
ogy, the network has evolved towards intelligence. In this context, user enables flexible programmability, which allows dynamic resource man-
needs and business types are becoming more diverse and dynamic. For agement and protocol enforcement. In practical deployments such as 5G
example, from traditional voice and text communications to new ap- service slicing, ultra-reliable low-latency communication (URLLC), and
plications such as real-time audio and video streaming, large-scale on- massive IoT scenarios, SDN plays a critical role in ensuring QoS by en-
line games, and virtual reality, higher requirements are placed on net- abling real-time flow classification, latency-aware routing, and adaptive
work performance, stability, and response speed. However, the defini- bandwidth allocation [2]. The data plane is responsible for forward-
tion and analysis of flows in the current network are still insufficient, ing packets, while the control plane maintains holistic awareness and
making it difficult to describe complex and diverse business needs ac- determines appropriate QoS flow rules based on global network condi-
curately.This limitation hinders effective resource allocation and path tions. Consequently, optimizing data transmission quality-by accounting
selection, thereby compromising the efficiency of service quality assur- for diverse service requirements and dynamic traffic behaviors-remains
ance in dynamic network environments. Especially in intelligent sce- a key challenge and research focus in SDN-based QoS frameworks
narios, the lack of in-depth understanding of dynamic flow character- [3].
istics and real-time optimization mechanisms has become an impor- QoS evaluates the network’s ability to deliver services based on
tant bottleneck restricting improving network routing efficiency. The parameters like bandwidth, delay, jitter, and packet loss. Traditional
network status information required by the intelligent network needs QoS flow classification algorithms typically make decisions based on
to be implemented through the Software Defined Networking (SDN) overall network needs, neglecting the specific requirements of individ-
framework. ual users or streams. Additionally, their complexity often hinders net-
The implementation of end-to-end Quality of Service (QoS) in tra- work managers from promptly and accurately determining appropriate
ditional networks faces significant challenges. SDN, a well-established QoS policies. Unlike traditional networks, SDN controllers, with their
∗ Corresponding author.
E-mail addresses: 2021010112@njupt.edu.com (H. She), yanlixing58@126.com (L. Yan), xina0310@outlook.com (X. An), 2481445289@qq.com (C. Mao),
guo@njupt.edu.cn (Y. Guo).
https://doi.org/10.1016/j.comnet.2025.111784
Received 21 April 2025; Received in revised form 21 September 2025; Accepted 13 October 2025
Available online 17 October 2025
1389-1286/© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

H. She et al. Computer Networks 273 (2025) 111784
global network view, can monitor the network, calculate protocols, and 2. Background and Motivation
manage data flow more effectively, ensuring better adherence to QoS
requirements. 2.1. Persona
Currently, the lack of consensus on QoS flow classification leads to
inaccurate analysis across different services, compromising network sta- Persona, a marketing tool with significant strategic value, was first
bility and the ability to meet growing service demands. In this context, introduced by Alan Cooper in 1999 [4], focusing on developing user-
persona becomes a powerful tool by analyzing and understanding user centered profiles. It involves creating a highly realistic and representa-
preferences and behaviors to create a comprehensive user persona. Per- tive fictional user image [5]. With the rapid advancement of technol-
sona offers valuable insights for refining QoS flow classification, ad- ogy, the application of persona has extended well beyond the design
dressing specific user needs, enhancing network stability, and delivering field [6],[7]. Leveraging its sharp insight into users’ real and potential
high-quality services. needs, persona enables refined behavioral feature cluster analysis using
The integration of AI technology has introduced smarter, more tag attributes. This approach has significantly enhanced the efficiency of
efficient methods for Internet of Things (IoT) data transmission. By matching supply and demand in public cultural services and improved
using deep learning prediction models, time series data from termi- the differentiation in resource integration [7]. In cutting-edge areas like
nal devices can be analyzed and predicted, allowing dynamic ad- e-commerce, social media, fintech, healthcare, and short video recom-
justments to data transmission based on the time characteristics of mendations, persona has demonstrated strong adaptability and practi-
different flows. This enhances network resource utilization and op- cality, becoming a driving force for industry innovation and develop-
timizes transmission. Additionally, AI can predict data flow fluctua- ment [8].
tions by analyzing historical data and recognizing patterns, enabling However, the research and application of persona in the crucial area
network managers to proactively adjust for flow peaks and troughs. of network analysis and management remain limited [9],[10]. Chal-
This proactive approach improves resource utilization and perfor- lenges such as the insufficient accuracy of user behavior prediction and
mance. AI also facilitates real-time decisions and optimizations during inflexible QoS adjustments highlight the need for enhanced tools. Per-
data transmission, dynamically adjusting strategies to achieve optimal sona, with its powerful user behavior analysis capabilities, has the po-
QoS. tential to address these issues [11]. By deeply analyzing user behav-
Thus, we proposed a QoS flow prediction method that combines the ior patterns, persona can offer precise demand forecasts and dynamic
ARIMA model and the Levinson-Durbin algorithm, which can monitor service adjustment strategies, driving network services towards greater
the network status in real-time and optimize flow management. By in- personalization and accuracy. This, in turn, can significantly enhance
troducing the concept of flow persona, flow classification is performed network management and QoS. Therefore, exploring the potential of
based on user behavior preferences and historical data, which improves persona in QoS optimization and flow analysis is essential for fostering
resource allocation efficiency. Finally, the APSO optimized CNN classi- the sustainable and healthy development of the network industry.
fication model we proposed effectively improves search efficiency and
avoids the local optimal problem. Our main contributions are summa- 2.2. QoS Flow
rized as follows.
In traditional network architecture, QoS flow classification policies
are widely used to optimize network performance and resource allo-
• We introduce a strategy using the Autoregressive Integrated Mov- cation by distinguishing and prioritizing critical data flow to meet the
ing Average (ARIMA) model statistical algorithm to collect key per- performance needs of various applications. Wang et al. [12] introduces
formance indicators via the NetFlow protocol and other methods. an innovative approach that combines feature generation with a Long
Differential processing is then applied to remove trend components Short-Term Memory (LSTM) model, providing a new method for QoS
and ensure data stability. The Levinson-Durbin algorithm refines the flow classification. This approach formulates forwarding rules based on
parameters of autoregression and moving average to accurately fit the characteristics of different data flow, ensuring the reliability and
QoS flow time series data. This approach not only enhances predic- stability of QoS, thereby significantly enhancing user experience. Gar-
tion accuracy but also improves network flow management and user zon et al. [13] addresses the flow distribution challenge in 5G backhaul
experience, ensuring that the proposed QoS flow rule scheme can networks by integrating precise optimization with heuristic techniques,
monitor network status in real- time and converge quickly. which ensures a high flow acceptance rate and meets the determinis-
• By integrating QoS flow rule with user persona, flow categorization tic QoS requirements of critical flows. Hu et al. [14] explores a flow
based on data characteristics and QoS requirements is enabled. This classification method based on graph neural networks, which markedly
creates ‘flow persona’ that describe and analyze each category. Flow improves QoS performance and classification accuracy by converting
persona visualize network conditions, and optimize resource alloca- network packets into undirected graphs and utilizing two-layer graph
tion. This approach improves network flow management, enhancing convolutional networks along with three distinct aggregation strategies.
service quality and resource efficiency. Zhang et al. [15] proposes an adaptive model update mechanism that ef-
• This paper presents a classification model that utilizes Adaptive Par- fectively reduces data transmission delays and packet loss by accurately
ticle Swarm Optimization (APSO) optimization Convolutional Neu- identifying and prioritizing key data streams, thereby ensuring the QoS
ral Network (CNN). The proposed model improves exploration of the requirements of various applications.
search space, leading to faster convergence towards the optimal solu- In an SDN environment, the complexity of network management in-
tion. Moreover, it effectively addresses the issue of getting trapped in creases significantly, necessitating a comprehensive approach that con-
local optima by overcoming the limitations posed by inappropriate siders routing policies, load balancing, and QoS assurance. Ibrar et al.
initial positions. [16] introduces a flow allocation algorithm for smart cities based on
SDN and fog computing, which enhances the performance of delay-
sensitive services by taking into account the reliability level of links
The structure of this paper is outlined as follows: Section 2 provides during flow allocation. Huang et al. [1] presents a near-optimal flow
a concise overview of the related work and the motivation behind our control method for hybrid SDN, exploring SDN migration sequences
research. Section 3 introduces the system model. The implementation to maximize controllable flow, and achieves QoS optimization through
details of our approach are described in Section 4. The convergence deep reinforcement learning algorithms. Liu et al. [17] combines SDN
and performance evaluation of our approach are presented in Section 5. with a LSTM network and a proximal policy optimization algorithm
Finally, Section 6 concludes the paper. to perform feature extraction, state perception, and decision-making,
2

H. She et al. Computer Networks 273 (2025) 111784
generating dynamic flow scheduling policies that meet QoS objectives To address these issues, we propose a QoS flow rule scheme called
in service scenarios, thereby further enhancing QoS guarantee capabil- ‘flow persona’, to optimize flow transport in the SDN-IoT environment.
ities. Saha et al. [18] discusses the implementation of QoS-based flow This scheme integrates persona into network flow management by ana-
rule aggregation in SDN networks, highlighting how the Q-Flag algo- lyzing and modeling user characteristics and behaviors using DL models.
rithm can significantly improve network performance and service qual- It classifies and schedules network flow based on user needs and pref-
ity, ensuring QoS reliability and stability, and providing a better user erences, offering more personalized and efficient service.
experience and service assurance for IoT applications. Although these Recent advancements such as RDG-TE [26] have demonstrated the
studies have made significant strides in designing QoS flow rules, chal- effectiveness of combining deep reinforcement learning with graph neu-
lenges remain in adapting to the rapidly changing network environment. ral networks to optimize traffic engineering strategies in SDN. These
For instance, existing schemes often lack the agility to quickly adjust approaches primarily focus on network-centric objectives, utilizing
to dynamic changes, potentially causing delays and misjudgments in topology-aware metrics such as path reliability, latency, and conges-
real-world applications. This limitation makes it difficult to meet the tion for routing optimization. In contrast, the FlowPersona framework
demands for fine-grained QoS guarantees and real-time responsiveness. proposed in this work adopts a user-centric modeling perspective by
Additionally, network managers often struggle to fully understand the incorporating behavioral preferences, historical service patterns, and
characteristics of each data stream, complicating the scheduling and context-aware flow differentiation. Instead of optimizing routing paths
management of refined QoS flows, which ultimately impacts end-user directly, FlowPersona generates adaptive flow rules aligned with user-
experience and satisfaction. level QoS expectations, enabling personalized and service-intent-aware
traffic management.
To further clarify this distinction and enhance the positioning of our
2.3. AI-Based Network Flow Classification
method, Table 1 provides a conceptual comparison between FlowPer-
sona and representative DRL-based flow optimization and classification
Network flow classification is crucial for network measurement and
methods. Key differences in modeling perspective, input features, learn-
management. Emerging AI algorithms have become viable solutions for
ing mechanisms, and system-level objectives are summarized to high-
flow classification and are widely applied in data flow classification
light the unique contributions of FlowPersona.
tasks. Suguna et al. [19] proposes a heterogeneous network flow clas-
The Flow Persona mechanism is designed to support differentiated
sification method based on ensemble learning, called Cat-ANTC. This
QoS slicing in SDN-IoT environments, enabling the classification and
method uses the CatBoost algorithm to automatically classify multiple
management of flows according to service-specific requirements. In
types of flow, achieving high prediction accuracy and incorporating
particular, the proposed scheme targets three primary slice types: 1)
model regularization to reduce overfitting and improve efficiency ef-
latency-sensitive slices for services such as smart healthcare and indus-
fectively. Xie et al. [20] proposes a two-stage online elephant flow pre-
trial control systems; 2) high-throughput slices for video surveillance
diction method using data flow mining. By mapping the trained classifi-
and real-time media streaming; and 3) delay-tolerant slices for applica-
cation and prediction decision tree models to the corresponding action
tions like environmental monitoring and smart agriculture. By aligning
pipeline of a programmable switch, the models and parameters can be
flow rules with user behavior and service context, Flow Persona enables
updated online, enabling dynamic load balancing. Zhang et al. [21] pro-
intent-aware, slice-adaptive flow control that enhances service quality
poses an autonomous model update mechanism for AI-based flow clas-
across heterogeneous IoT domains.
sifiers, focusing on scenarios where these classifiers are used to handle
network flow from both known and unknown applications.
Although existing research has made progress in applying artificial 3. System Model
intelligence to classify network flow, several limitations remain. Many
methods struggle with the dynamic nature and diverse needs of het- In this section, we will introduce the network model and flow per-
erogeneous network flow, resulting in weak generalization ability and sona model that we have developed. Our research is centered around
difficulty adapting to complex network environments [22]. Addition- leveraging flow persona to establish a QoS flow rule scheme, enabling
ally, traditional models rely heavily on hyperparameters and feature effective QoS flow analysis and efficient classification. Please refer to
selection, and improper parameter settings can negatively impact clas- Table 2 for a list of symbols utilized in this article.
sification performance [23],[24]. The lack of real-time processing and
resource efficiency further limits the applicability of these methods in
high-flow scenarios [25]. To address these challenges, this paper pro- 3.1. Network Model
poses an innovative approach that combines QoS flow rules and persona
Next, we will establish specific configurations for the designed net-
construction, an efficient time-series prediction strategy, and an APSO
work model. We develop a model architecture for wireless networks that
optimization CNN classification model. This approach not only enhances
considers user needs, business goals, and network dynamics in SDN-IoT
prediction accuracy and resource management efficiency but also opti-
settings. To achieve an effective QoS flow rule scheme, we need to de-
mizes user experience, providing more reliable support for high-quality
services in complex network environments.
fine and examine the network topology 𝐺, wireless transmission rate 𝐶,
and quality of service 𝑄.
2.4. Motivation 1) Network Topology: The flow persona model discussed in this pa-
per is designed for an SDN-IoT scenario. The network topology 𝐺
With the rise of diverse new services in the 5G and cloud era, and we created is illustrated in Fig. 1. It features a mesh structure with
the rapid development of IoT, cloud storage networks, and SDN, QoS numerous Segment Routing (SR) nodes deployed. This architecture
flow classification faces new challenges. Integrating persona into QoS provides multiple paths, ensuring network connectivity and stability
flow classification is expected to enhance service personalization and ac- even in the event of node failures. The multipath capability supports
curacy. Persona improves network service efficiency by analyzing user load balancing and minimizes the risk of overloading any single path,
behavior and historical data, ensuring a consistently high-quality QoS thus preserving overall network performance and efficiency. Addi-
experience. Despite SDN’s flexibility and scalability, QoS flow classifi- tionally, the structure offers high flexibility and scalability, allowing
cation models still face issues with accuracy and convergence speed, network administrators to dynamically adjust routing policies based
largely due to manual parameter adjustments and a lack of intelligent, on flow demands and real-time network load, effectively meeting
dynamic optimization methods. diverse QoS requirements.
3

H. She et al. Computer Networks 273 (2025) 111784
Table 1
Conceptual comparison between FlowPersona and representative DRL-based flow optimization/classification methods.
Aspect FlowPersona (This Work) Representative DRL-Based Flow Optimization Methods
Primary Objective QoS-aware flow classification and adaptive rule enforcement End-to-end traffic engineering and routing optimization
Modeling Perspective User-centric: behavior-driven and preference-aware Network-centric: topology- and metric-driven
Input Features Historical user behavior, service preference, QoS attributes Link delay, reliability, congestion status, topology state
Learning Mechanism ARIMA-based flow prediction + APSO-optimized CNN classification DRL agents (e.g., DQN, DDPG) combined with GNN or MLP
Application Layer Flow classification and QoS policy generation at the control plane Routing path decision and resource allocation in SDN
Personalization Support High: personalized rules based on user persona Low: generalized treatment of flows
Table 2
Notations.
Notation Description
𝐺 Flow persona network topology diagram
𝐶 Wireless transmission rate
𝑄 Referring to QoS
𝑙 A specific flow within the graph 𝐺
 A collection of all flows, 𝑙∈
𝐹 The magnitude of traffic for flow 𝑙
𝑙
𝐹 The cumulative traffic of all flows in the network, 𝐹=∑𝐹
𝑙
𝐷 𝑙(𝑡) The data volume transmitted by flow 𝑙 within a specific time frame, typically measured in units such as bits or bytes at time 𝑡
𝑇 𝑙(𝑡) The duration, expressed in seconds (s), required for flow 𝑙 to transfer the data amount 𝐷
𝑙
at time 𝑡
𝑇ℎ 𝑙(𝑡) The throughput of flow 𝑙 at time 𝑡, 𝑇ℎ 𝑙(𝑡)=𝐷 𝑙(𝑡)∕𝑇 𝑙(𝑡)
𝑞 𝑑𝑒(𝑡) End-to-end delay between SR nodes at time 𝑡
𝑞 𝑡ℎ(𝑡) Throughput at time 𝑡
𝑞 𝑙𝑜(𝑡) Package loss rate at time 𝑡
𝜉 The difference value of the time series
𝑦 𝑦 ′𝑡 The value of the time series after difference at time 𝑡
𝑎
𝑡
The autoregressive coefficient of step 𝑖
𝑖
𝑦̂
𝑡+ℎ
The predicted value of step 𝑡+ℎ
and can be adjusted to meet varying application scenarios and user
needs.
𝑄={𝑞 ,𝑞 ,𝑞 } (1)
𝑑𝑒 𝑡ℎ 𝑙𝑜
Naturally, in practical application scenarios, QoS service quality must
consider additional factors, including availability, jitter, and bandwidth
guarantee, among others. Nonetheless, the QoS flow rule scheme based
on flow persona provides a scalable solution. It allows for flexible adjust-
ment of rule schemes based on specific requirements, accommodating
various application scenarios and user demands effectively.
In our simulation, the SDN-IoT mesh network topology consists of
50 SR nodes, forming a scalable multi-path architecture. This topology
enables dynamic flow rerouting and is designed to accommodate large-
scale IoT scenarios by supporting horizontal expansion with minimal
Fig. 1. Part of the network topology. reconfiguration overhead. Each SR node is equipped with basic edge
computing capabilities to simulate distributed intelligence. The consid-
ered application-layer data rates are as follows: video streaming services
2) Wireless Transmission Rate: Our QoS flow classification strategy
are modeled with bitrates ranging from 2 Mbps to 5 Mbps (representing
leverages efficient wireless transmission technology to monitor flow,
standard and high-definition streams), audio streaming services are as-
optimize paths in real-time, and prevent network congestion and
signed 64-128 kbps depending on codec assumptions, and ordinary data
service degradation. In both our network model and simulations,
services, such as sensor telemetry or background sync, operate at 10-50
we use the 802.11ac standard to achieve high-speed wireless trans-
kbps. These settings reflect typical bandwidth requirements observed in
mission, with a maximum transmission rate of 𝐶 up to 1.3Gbps,
practical IoT deployments.
thereby enhancing user experience. This is used solely to simulate
3.2. Flow Persona Model
high-bandwidth scenarios such as video streaming and does not im-
ply applicability to all IoT contexts.In addition, other state-of-the-art
To illustrate the specific challenges addressed by FlowPersona, con-
wireless technologies such as 5G New Radio , Wi-Fi 6/802.11ax, and
sider a simplified SDN-IoT scenario involving three representative user
LTE-Advanced could equally serve as evaluation baselines. The Flow
types:
Persona framework remains independent of the underlying trans-
mission technology, ensuring adaptability across heterogeneous net- • User1 primarily engages in ordinary data services such as brows-
work environments. ing and background synchronization, which are delay-tolerant and
3) QoS: To address computational complexity and NP-complete issues, bandwidth-insensitive.
we establish three core indicators: delay, throughput, and packet • User2 frequently uses audio-related services like music streaming
loss rate, denoted as 𝑄=𝑞 ,𝑞 ,𝑞 . These indicators ensure network and voice calls, which are sensitive to delay and jitter.
𝑑𝑒 𝑡ℎ 𝑙𝑜
effectiveness and stability, enhancing QoS. While practical applica- • User3 is focused on video-based applications such as video calls and
tions may require additional QoS factors such as availability, jitter, high-definition streaming, which require both high throughput and
and bandwidth guarantee, the flow persona is an extensible model low latency.
4

H. She et al. Computer Networks 273 (2025) 111784
Fig. 2. Flow persona model.
In a congested network environment-due to burst traffic or limited ing, like email and basic web browsing, has low real-time demands
wireless bandwidth-traditional flow classification mechanisms typically but requires data integrity. The QoS flow rule scheme proposed in this
apply uniform treatment based on static QoS tags or protocol types. This study addresses the specific needs of each media type during network
can lead to inefficient resource allocation: for instance, video streams transmission, ensuring service quality and enhancing the user expe-
of User3 may suffer latency spikes, and audio services for User2 may rience. Specifically, we identified three distinct user types based on
experience jitter, ultimately degrading QoS. analysis of user behavior preferences and historical data. As indicated by
In contrast, FlowPersona models each user’s historical usage behav- Eq. 2, each user’s feedback data is weighted differently. 𝑈𝑠𝑒𝑟 shows
1
ior and service preference using weighted profile functions. The system a preference for browsing the Internet, social media, and other ordi-
then classifies flows using an APSO-optimized CNN, generating adap- nary data streaming services. 𝑈𝑠𝑒𝑟 engages more in activities like lis-
2
tive flow rules aligned with each user’s actual service context. This en- tening to music, making voice calls, and other audio streaming ser-
ables priority-aware flow control-for example, assigning higher prior- vices. On the other hand, 𝑈𝑠𝑒𝑟 is inclined towards video streaming
3
ity to User3’s interactive video traffic-while maintaining fairness and services such as video calls and watching videos. We quantify user pref-
stability across the network. As a result, FlowPersona improves overall erence for each service using 𝑢𝑏𝑠
𝑝
𝑒
𝑟
𝑟
𝑒
𝑣𝑖𝑐𝑒= The number
T
o
o
f
t a
c
l
l i
c
c
l
k
ic
s
k
o
s
f the service. His-
QoS assurance and system responsiveness in dynamic SDN-IoT environ- torical data ℎ𝑠𝑒𝑟𝑣𝑖𝑐𝑒 reflects the number of hours users have spent on dif-
𝑑𝑎𝑡𝑎
ments. ferent services in the past 10 days. Additionally, we use 𝑠𝑟 =0.6∗
𝑑𝑎𝑡𝑎
Flow persona is a QoS flow rule scheme that incorporates user at- Service response time(ms)+0.4∗Throughput(Mbps) as the value of the
tributes and business requirements. It involves collecting and analyzing service requirement data.
network flow data 𝐹 to create a persona for QoS flows. Based on this per-
sona, QoS flow rules are formulated to ensure an optimal user network 𝑈𝑠𝑒𝑟 1 =0.3∗(𝑢𝑏𝑣 𝑝𝑟 𝑖𝑑 𝑒 𝑒𝑜+ℎ𝑣 𝑑 𝑖 𝑎 𝑑 𝑡𝑎 𝑒𝑜)
experience and enable fine-grained service quality management of QoS +0.1∗(𝑢𝑏𝑎𝑢𝑑𝑖𝑜+ℎ𝑎𝑢𝑑𝑖𝑜)
𝑝𝑟𝑒 𝑑𝑎𝑡𝑎
flows. Specifically, as depicted in Fig. 2, the model comprises four main
components: user information collection, service category classification,
+0.6∗(𝑢𝑏𝑜
𝑝
𝑟
𝑟
𝑑
𝑒
𝑖𝑛𝑎𝑟𝑦+ℎ𝑜
𝑑
𝑟
𝑎
𝑑
𝑡𝑎
𝑖𝑛𝑎𝑟𝑦)+𝑠𝑟
𝑑𝑎𝑡𝑎
(2a)
QoS flow classification, and algorithm processing.
The persona gathers basic user information and stores it on the 𝑈𝑠𝑒𝑟 2 =0.3∗(𝑢𝑏𝑣 𝑝𝑟 𝑖𝑑 𝑒 𝑒𝑜+ℎ𝑣 𝑑 𝑖 𝑎 𝑑 𝑡𝑎 𝑒𝑜)
server. Its purpose is to classify QoS flow in real- time by analyzing +0.6∗(𝑢𝑏𝑎𝑢𝑑𝑖𝑜+ℎ𝑎𝑢𝑑𝑖𝑜)
user behavior preferences and historical data for various services. 𝑝𝑟𝑒 𝑑𝑎𝑡𝑎
This paper examines three service categories: video streaming, au-
+0.1∗(𝑢𝑏𝑜
𝑝
𝑟
𝑟
𝑑
𝑒
𝑖𝑛𝑎𝑟𝑦+ℎ𝑜
𝑑
𝑟
𝑎
𝑑
𝑡𝑎
𝑖𝑛𝑎𝑟𝑦)+𝑠𝑟
𝑑𝑎𝑡𝑎
(2b)
dio streaming, and ordinary data streaming. Each category has distinct
network quality requirements. For instance, video streaming is highly 𝑈𝑠𝑒𝑟
3
=0.6∗(𝑢𝑏𝑣
𝑝𝑟
𝑖𝑑
𝑒
𝑒𝑜+ℎ𝑣
𝑑
𝑖
𝑎
𝑑
𝑡𝑎
𝑒𝑜)
sensitive to bandwidth and delay due to its demand for high-quality +0.3∗(𝑢𝑏𝑎𝑢𝑑𝑖𝑜+ℎ𝑎𝑢𝑑𝑖𝑜)
images, while audio streaming, despite lower bandwidth needs, is very 𝑝𝑟𝑒 𝑑𝑎𝑡𝑎
delay-sensitive and jitter-sensitive. In contrast, ordinary data stream- +0.1∗(𝑢𝑏𝑜 𝑝 𝑟 𝑟 𝑑 𝑒 𝑖𝑛𝑎𝑟𝑦+ℎ𝑜 𝑑 𝑟 𝑎 𝑑 𝑡𝑎 𝑖𝑛𝑎𝑟𝑦)+𝑠𝑟 𝑑𝑎𝑡𝑎 (2c)
5

H. She et al.
Computer Networks 273 (2025) 111784
The algorithm processing involves two aspects: real-time QoS flow
problem, and QoS flow classification. For real-time processing, the Net-
Flow protocol is used to gather QoS-related data in real- time, and the
ARIMA model enhances prediction accuracy through deep analysis. To
ensure responsiveness in dynamic environments, the ARIMA model is
periodically executed at fixed time intervals (every 5 seconds) over ag-
gregated traffic statistics rather than individual flows. It forecasts key
QoS metrics such as bandwidth demand and latency variation. These
predictions are not used directly for path selection, but are instead
used to update the QoS attribute weights in the 𝑄′ matrix, guiding
pre-classification before CNN inference.To reduce runtime complexity,
the ARIMA model is implemented using a fixed sliding window and
precomputed coefficients. The Levinson-Durbin algorithm is employed
to ensure numerical stability and efficient parameter estimation. This
lightweight design ensures that the prediction process operates in real
time at the SDN controller without adding delay to the flow rule gen-
eration process. This control enables integration of heterogeneous IoT
services under a unified QoS-aware framework.In QoS flow classifica-
tion, a QoS attribute matrix is constructed to reflect QoS demands, and
the decision model is optimized to maximize QoS attribute values. The
classification model utilizes the APSO algorithm to adjust the hyperpa-
rameters of a one-dimensional CNN. By training and optimizing these
hyperparameters, the model finds the optimal configuration, reducing
Fig. 3. Flowchart of algorithm.
the labor cost of manual adjustments, improving classification accuracy,
and enhancing the speed and performance of the neural network.
As shown in Fig 3, the computed user personas are incorporated into
the system workflow through the weighting of QoS attributes, forming  Where 𝑝(𝑡)= 𝜇(𝑡)−𝜆(𝑡) represents the probability that the SR node can-
the 𝑄′ matrix. This matrix, after normalization, is fed into the APSO- 𝜇(𝑡)
not process or transmit the data packet in time at moment 𝑡. The average
optimized CNN model to perform flow classification. The classification
|                                                                          |     |     |     | queuing time 𝑄 | (𝑡) at time 𝑡 can be used to determine the queuing delay  |     |
| ------------------------------------------------------------------------ | --- | --- | --- | -------------- | --------------------------------------------------------- | --- |
| result is then used by the SDN controller to assign flow priorities and  |     |     |     |                | 𝑢                                                         |     |
𝑇 (𝑡) at the same moment, with the formula as follows:
| generate appropriate QoS flow rules. Since persona vectors are updated  |     |     |     | 𝑞   |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
continuously based on user behavior, the overall process supports adap- 𝑇 (𝑡)=𝑄 (𝑡)∕𝜆(𝑡) (5)
|     |     |     |     | 𝑞𝑢𝑒𝑢𝑒 | 𝑢   |     |
| --- | --- | --- | --- | ----- | --- | --- |
tive flow rule adjustment in real time.
In summary, we can model 𝑞  by combining queuing theory and the
𝑑𝑒
Poisson process. By utilizing the above formula, we define and calculate
3.3.  Problem Formulation of QoS Attributes the end-to-end delay between SR nodes.
Definition 2: Throughput
Definition 1: End-to-end delay
Throughput refers to the quantity of data transmitted over a spe-
In this paper, we replace delay with end-to-end delay between SR
cific path or connection within a time unit. It is a crucial metric for as-
nodes, where SR nodes play a pivotal role as relays in wireless Ad hoc
sessing the efficiency of network transmission, as it evaluates the speed
networks. It measures the total delay encountered by packet transmis-
and capacity of data transmission within the network. The magnitude
sion from the source node to the destination node. Specifically, we de-
of throughput directly impacts user experience and the extent to which
fine end-to-end delay 𝑞  as the time elapsed from when the packet en- business needs are satisfied. A higher throughput signifies a network’s
𝑑𝑒
ters the queue buffer of the source node to when it reaches the end of the  ability to transfer data at a faster rate, providing enhanced data transfer
queue buffer of the target node. This delay encompasses various com- rates and efficiency [28].
ponents, including transmission delay, queuing delay, and propagating  Hence, we require a specific formula to define throughput 𝑞 :
𝑡ℎ
delay.
∑
To model the end-to-end delay between SR nodes, we utilize the  𝑞 (𝑡)= 𝑇ℎ (𝑡) (6)
|                                                                   |     |     |     | 𝑡ℎ  | 𝑙   |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| M/M/1 queue model [27]. This model assumes that the arrival time  |     |     |     |     | 𝑙∈ |     |
follows a Poisson distribution, the service time follows an exponential  Definition 3: Packet loss rate
distribution, and there is only a single service desk. Based on this model,  The packet loss rate signifies the percentage or decimal represen-
 can be calculated using the following formula: tation of packets that fail to reach the receiver during transmission. It
𝑞 𝑑𝑒
serves as a measure of the proportion of lost packets in data transmis-
| 𝑞 (𝑡)=𝑇                                                   | (𝑡)+𝑇                                                 | (𝑡)+𝑇       | (𝑡) | (3) sion.  |        |     |
| --------------------------------------------------------- | ----------------------------------------------------- | ----------- | --- | ---------- | ------ | --- |
| 𝑑𝑒 𝑞𝑢𝑒𝑢𝑒                                                  | 𝑡𝑟𝑎𝑛𝑠𝑚𝑖𝑠𝑠𝑖𝑜𝑛                                          | 𝑝𝑟𝑜𝑝𝑎𝑔𝑎𝑡𝑖𝑜𝑛 |     |            |        |     |
| Among them, 𝑇                                             | (𝑡) represents the queuing delay at time 𝑡, which is  |             |     |            | 𝑁 (𝑡)  |     |
|                                                           | 𝑞𝑢𝑒𝑢𝑒                                                 |             |     | 𝑞          | (𝑡)= 𝑖 | (7) |
| the time a packet waits in the queue before processing. 𝑇 |                                                       |             |     | (𝑡) de- 𝑙𝑜 |        |     |
𝑡𝑟𝑎𝑛𝑠𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑁 𝑠 (𝑡)
notes the transmission delay at time 𝑡, the time needed to send the packet
Where 𝑁 represents the number of lost packets, referring to the
| from the source to the destination. 𝑇 |     |     | (𝑡) indicates the propaga- |     | 𝑖   |     |
| ------------------------------------- | --- | --- | -------------------------- | --- | --- | --- |
𝑝𝑟𝑜𝑝𝑎𝑔𝑎𝑡𝑖𝑜𝑛 packets that did not successfully reach their destination during trans-
tion delay at time 𝑡, which is the time required for the packet to travel
|                      |     |     |     | mission. 𝑁 |  represents the total number of packets sent within the same  |     |
| -------------------- | --- | --- | --- | ---------- | ------------------------------------------------------------- | --- |
| through the channel. |     |     |     |            | 𝑠                                                             |     |
time period.
| The queuing delay 𝑇 |     | (𝑡) can be modeled using the M/M/1 queue  |     |     |     |     |
| ------------------- | --- | ----------------------------------------- | --- | --- | --- | --- |
𝑞𝑢𝑒𝑢𝑒
| model. In this model, the average queue time 𝑄        |     |     | (𝑡) at time 𝑡 and the  |               |     |     |
| ----------------------------------------------------- | --- | --- | ---------------------- | ------------- | --- | --- |
|                                                       |     |     | 𝑢                      | 4.  Algorithm |     |     |
| packet arrival rate 𝜆(𝑡) to the network are related t |     |     | o the packet process-  |               |     |     |
ing and transmission rate 𝜇(𝑡). This relationship can be expressed as:
In this section, we will provide a comprehensive overview of the key
𝜆(𝑡)∗𝑝(𝑡) algorithms discussed in this article. The overall algorithm flow chart is
| 𝑄 (𝑡)=      |     |     |     | (4)                    |     |     |
| ----------- | --- | --- | --- | ---------------------- | --- | --- |
| 𝑢 𝜇(𝑡)−𝜆(𝑡) |     |     |     | illustrated in Fig. 3. |     |     |
6

H. She et al.
Computer Networks 273 (2025) 111784
It is important to note that the machine learning component of  apply the Integral (I) component for differencing non-stationary time se-
Flow Persona operates in an offline training mode, where NS-3 is em- ries to transform them into stationary series, and correct the prediction
ployed to simulate the SDN-IoT topology and generate flow-level data  result using the MA of historical prediction errors [30]. This approach,
for model training and validation. Once the CNN model optimized by  with its ability to capture short-term changes, is well-suited for model-
APSO is trained, the learned classification and prediction functions are  ing QoS attribute variations over time, enabling real-time analysis and
| integrated with the SDN controller for real-time QoS flow rule enforce- |     |     | prediction [31]. |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | ---------------- | --- | --- | --- |
ment. In this way, NS-3 provides a realistic emulation environment for
data generation and performance validation, while the Flow Persona 4.1.1.  Data collection and preprocessing
framework remains modular, allowing future integration of the ML  Enable NetFlow on network routers and configure SolarWinds to col-
model directly into NS-3 or other online platforms if required. lect and analyze data flow, calculating real-time time series of QoS flow.
Use linear interpolation to fill in missing data points and apply moving
average to smooth outliers. Finally, normalize and scale the data to the
4.1.  Real-time QoS Flow Problem
range [0,1] to ensure consistency.
Real-time QoS flow is a critical issue in the flow persona model. Due
4.1.2.  Determine the stationarity of time series
to data processing delays and the dynamic nature of QoS attributes in SR
Use the Augmented Dickey-Fuller (ADF) test to compute ADF statis-
nodes, the QoS flow rule scheme must rapidly converge to support real-
tics with the formula (8): transmission. It serves as a measure of the
time network flow monitoring and control. To address this, as shown
in Algorithm 1, we employ the ARIMA statistical algorithm to handle  proportion of lost packets in data transmission.
real-time QoS flow, ensuring effective real-time monitoring and control
∑ 𝑘
| of network flow. |     |     | 𝜉 =𝛼+𝛽𝑡+𝛾𝑦 | +   | 𝜂𝜉 +𝜀    | (8) |
| ---------------- | --- | --- | ---------- | --- | -------- | --- |
|                  |     |     | 𝑦𝑡         | 𝑡−1 | 𝑖 𝑦𝑡−𝑖 𝑡 |     |
𝑖=1
where 𝜉  is the differenced time series, 𝛼 is the constant term, 𝛽𝑡 is the
| Algorithm 1 Real-time QoS Flow Optimization. |     |     | 𝑦𝑡  |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- |
1: Input: NetFlow data, QoS attribute time series time trend term (if applicable), 𝛾𝑦  is the lag term, 𝜂  are the coef-
|     |     |     |     |     | 𝑡−1 𝑖 |     |
| --- | --- | --- | --- | --- | ----- | --- |
2: Output: Optimized real-time QoS flow rules ficients of the differenced terms, and 𝜀  is the error term. The signif-
𝑡
3: Step 1: Data Collection and Preprocessing icance level from the ADF test determines the stationarity of the QoS
4: Activate NetFlow protocol, configure SolarWinds for real-time data collec- flow time series. If the significance level is below 0.05, the time series is
tion stationary; otherwise, differencing is required. For differencing, calcu-
5: Perform linear interpolation for missing data and apply moving average for  late 𝑦′=𝑦 −𝑦 , where 𝑦′ is the differenced series value at time 𝑡, and
| outlier smoothing                |     |     | 𝑡            | 𝑡 𝑡 − 1              | 𝑡                                             |     |
| -------------------------------- | --- | --- | ------------ | -------------------- | --------------------------------------------- | --- |
|                                  |     |     | 𝑦 is t he or | igin a l  series val | ue at time 𝑡. Differencing removes the trend  |     |
| 6: Normalize data to [0,1] range |     |     | 𝑡            |                      |                                               |     |
co mponent, making the series more stationary.
7: Step 2: Stationarity Check
| 8: Apply ADF test: 𝜉 | =𝛼+𝛽𝑡+𝛾𝑦 | +∑𝑘 𝜂𝜉 +𝜀 |     |     |     |     |
| -------------------- | -------- | --------- | --- | --- | --- | --- |
𝑦 𝑡−1 𝑖=1 𝑖 𝑦𝑡−𝑖 𝑡 4.1.3.  Determine the parameters of the ARIMA model
| 9: if significance lev | e𝑡l > 0.05 then |     |     |     |     |     |
| ---------------------- | --------------- | --- | --- | --- | --- | --- |
Plot the Autocorrelation Function (ACF) and Partial Autocorrelation
| 10:   Apply differencing: 𝑦′=𝑦 |     | −𝑦  |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- |
𝑡 𝑡 𝑡−1 Function (PACF) graphs to preliminarily determine the ranges for the
11: end if
12: Step 3: ARIMA Parameter Identification autoregressive order 𝑝 and moving average order 𝑞 based on the trun-
13: Plot ACF and PACF to estimate 𝑝 and 𝑞 values cation and trailing of the autocorrelation coefficients. Construct ARIMA
14: Use AIC criteria to select the best ARIMA model: 𝐴𝐼𝐶=2𝑘−2ln(𝐿) models for various 𝑝 and 𝑞 values, and calculate the Akaike Information
| 15: Step 4: Initial Model Fitting |     |     | Criterion (AIC) using (9): |     |     |     |
| --------------------------------- | --- | --- | -------------------------- | --- | --- | --- |
16: Fit ARIMA model to the time series:
|     |     |     | 𝐴𝐼𝐶=2𝑘−2ln(𝐿) |     |     | (9) |
| --- | --- | --- | ------------- | --- | --- | --- |
𝑝 𝑞
| 𝑦 =𝑐+ ∑ | 𝜙 𝑦 ∑ 𝜃 𝜀 | +𝜀  |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
𝑡 𝑖 𝑡−𝑖 + 𝑗 𝑡−𝑗 𝑡 where 𝑘 is the number of model parameters and 𝐿 is the model’s like-
𝑖=1 𝑗=1
lihood function. Select the model with the lowest AIC value as the best
17: Step 5: Iterative Model Update
ARIMA model.
18: while new data is collected or error threshold is exceeded do
19:   Collect additional QoS flow data in real- time
4.1.4.  Model fitting and iteration
20:   Preprocess the newly collected data
Use the Levinson-Durbin algorithm to accurately calculate the au-
21:   Recheck stationarity and apply differencing if needed
tocorrelation and partial autocorrelation coefficients, with the formula
22:   Reidentify ARIMA parameters (𝑝, 𝑑, 𝑞) using ACF, PACF, and AIC
23:   Refit the ARIMA model with updated parameters and new data: (10). The algorithm is a recursive method for solving linear predictive
coding problems using Yule-Walker equations, represented by a Toeplitz
∑ 𝑝 ∑ 𝑞
𝑦 =𝑐+ 𝜙𝑦 + 𝜃𝜀 +𝜀 matrix with rows as shifted autocorrelation functions. It begins with a
| 𝑡   | 𝑖 𝑡−𝑖 | 𝑗 𝑡−𝑗 𝑡 |     |     |     |     |
| --- | ----- | ------- | --- | --- | --- | --- |
𝑖=1 𝑗=1 first-order AR model and progressively increases the order until the de-
24:   Forecast QoS time series values using the updated model sired model order is achieved.
| 25:   Evaluate forecast accuracy and update QoS flow rules dynamically |     |     |     | ∑𝑖−1𝑎     |     |      |
| ---------------------------------------------------------------------- | --- | --- | --- | --------- | --- | ---- |
|                                                                        |     |     | 𝑟 − | 𝑟         |     |      |
| 26: end while                                                          |     |     | 𝑖   | 𝑗=1 𝑗 𝑖−𝑗 |     | (10) |
𝑎 𝑖 =
| 27: Step 6: Forecasting and Evaluation |     |     |     | 𝑒 𝑖−1 |     |     |
| -------------------------------------- | --- | --- | --- | ----- | --- | --- |
28: Forecast future QoS time series values using the latest model: where 𝑎 is the regression coefficient at step 𝑖, 𝑟 is the autocorrelation
𝑖 𝑖
|     |     |     | coefficient, and 𝑒 |  is the prediction error. We then use the optimal 𝑝 |     |     |
| --- | --- | --- | ------------------ | --------------------------------------------------- | --- | --- |
| ∑ 𝑝 | ∑ 𝑞 |     |                    | 𝑖 − 1                                               |     |     |
𝑦̂ =𝑐+ 𝜙̂ 𝑦̂ + 𝜃̂ 𝜀̂ and 𝑞 parameters  t o  fit the QoS flow time series data. The fitted ARIMA
| 𝑡+ℎ | 𝑖 𝑡+ℎ−𝑖 | 𝑗 𝑡+ℎ−𝑗 |           |     |     |     |
| --- | ------- | ------- | --------- | --- | --- | --- |
| 𝑖=1 | 𝑗=1     |         | model is: |     |     |     |
29: Evaluate final forecast accuracy using MSE and MAE
|                                                   |     |     |         | 𝑝 𝑞          |              |      |
| ------------------------------------------------- | --- | --- | ------- | ------------ | ------------ | ---- |
| 30: Adjust network resources based on predictions |     |     | ∑       | ∑            |              | (11) |
|                                                   |     |     | 𝑦 𝑡 =𝑐+ | 𝜙𝑦 𝑖 𝑡−𝑖 + 𝜃 | 𝑗 𝜀 𝑡−𝑗 +𝜀 𝑡 |      |
31: End
|     |     |     | 𝑖=1 | 𝑗=1 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
where 𝑐 is a constant, 𝜙 are the autoregressive coefficients representing
𝑖
The ARIMA(𝑝,𝑑,𝑞) model combines Autoregressive model (AR) and  the influence of past values, 𝜃  are the moving average coefficients rep-
𝑗
Moving Average (MA) models to predict time series [29]. We can use his- resenting the influence of past prediction errors, and 𝜀  are the error
𝑡−𝑗
torical time series data to predict the current value using the AR model,  term of the past 𝑗 moment.
7

H. She et al.
Computer Networks 273 (2025) 111784
To adapt to changing QoS requirements, the model is re-fitted when  the service portfolio into a comprehensive QoS metric value. Further-
new data arrives. Periodic error checks and performance evaluations  more, in [36], the author introduces the MQRP method, which optimizes
trigger automatic updates, allowing the ARIMA model to adjust to  decisions to maximize the values of QoS attributes within the network.
network flow changes continuously [32],[33]. Each new data batch  Taking into account the unique requirements and limitations of satel-
prompts a model update based on the latest information, with the QoS  lite networks, this method determines routing paths and resource allo-
flow data collected via the NetFlow protocol and pre-processed accord- cation strategies by considering trade-offs and optimizing various QoS
ingly. Updates occur either based on a set frequency or when an error  attributes. Drawing inspiration from the concepts presented in these two
threshold is exceeded. When triggered, the ARIMA model is refitted and  papers, we have devised a QoS attribute matrix to be utilized in the flow
| its parameters are optimized to align with current QoS needs. The up- | persona model. |     |     |     |
| --------------------------------------------------------------------- | -------------- | --- | --- | --- |
dated model then forecasts future QoS flow, enabling dynamic adjust- We define the matrix (13) as the QoS matrix.
ments to QoS flow rules and resource allocation strategies to maintain
|                                                | 𝑄(1,1) | 𝑄(1,2) | 𝑄(1,3) |      |
| ---------------------------------------------- | ------ | ------ | ------ | ---- |
| real-time performance and prediction accuracy. | ⎡      |        | ⎤      |      |
|                                                | 𝑄(2,1) | 𝑄(2,2) | 𝑄(2,3) |      |
|                                                | ⎢      |        | ⎥      |      |
|                                                | ⎢      |        | ⎥      |      |
| 4.1.5.  Prediction and real-time evaluation    | ⋮      | ⋮      | ⋮      | (13) |
|                                                | 𝑄=⎢    |        | ⎥      |      |
Use the ARIMA model to predict future QoS flow values with the  ⎢ 𝑄(𝑡,1) 𝑄(𝑡,2) 𝑄(𝑡,3) ⎥
| formula (12): | ⎢ ⋮        | ⋮         | ⋮ ⎥        |     |
| ------------- | ---------- | --------- | ---------- | --- |
|               | ⎢          |           | ⎥          |     |
|               | ⎣𝑄(1000,1) | 𝑄(1000,2) | 𝑄(1000,3)⎦ |     |
𝑝 𝑞
∑ ∑
𝑦̂ =𝑐+ 𝜙̂𝑦̂ + 𝜃̂ 𝜀̂ (12) Where 𝑄(𝑡,𝑠) represents the value of the 𝑠-th QoS attribute at the
𝑡+ℎ 𝑖 𝑡+ℎ−𝑖 𝑗 𝑡+ℎ−𝑗
𝑖=1 𝑗=1 𝑡-th moment.𝑄(𝑡,1)=𝑞 (𝑡), 𝑄(𝑡,2)=𝑞 (𝑡), 𝑄(𝑡,3)=𝑞 (𝑡). As a result,
|     |     | 𝑑𝑒  | 𝑡ℎ  | 𝑙𝑜  |
| --- | --- | --- | --- | --- |
where 𝑦̂  is the predicted value of step 𝑡+ℎ, and 𝜀̂  represents  the first column of the matrix represents the QoS attribute value of End-
𝑡 + ℎ 𝑡+ ℎ − 𝑗
the pred i c tion error. To ensure consistently high predi ct i o n accuracy,  to-end delay at time 𝑡, the second column represents the QoS attribute
the model’s performance is re-evaluated after each data update. The  value of throughput at time 𝑡, and the third column represents the QoS
accuracy of the predictions is evaluated by comparing them with actual  attribute value of packet loss rate at time 𝑡. By organizing the collected
flow data into this matrix format, we can conveniently analyze and pro-
data and calculating the mean squared error and mean absolute error.
cess the data, while capturing and analyzing the temporal characteris-
Based on the prediction results, the network resource allocation strategy
tics of QoS attributes. Taking into account the complexity of subsequent
is dynamically adjusted to optimize real-time QoS flow.
CNN model training, we gathered 1000 instances of flow data to allevi-
The ARIMA statistical algorithm effectively addresses real-time QoS
ate the challenges associated with data storage and computation. This
flow issues by enabling timely network flow monitoring and control.
Its advantage lies in learning time patterns and trends from historical  approach helps to strike a balance between capturing sufficient data and
data, allowing accurate prediction of future QoS values. This capability  avoiding an excessive collection of flow data, thus meeting the real-time
facilitates rapid convergence of the QoS flow rule scheme and precise  requirements of QoS flow. Moreover, capturing 1000 instances of data
real-time monitoring and control in the network environment. allows us to sample at a moderate frequency during the actual classifi-
cation process, providing a more accurate reflection of flow character-
istics. At the same time, we define the user’s weight matrix 𝑊 as:
4.2.  QoS Flow Classification
|     | ⎡𝑤𝑈𝑠𝑒𝑟1 | 𝑤𝑈𝑠𝑒𝑟1 𝑤𝑈𝑠𝑒𝑟1⎤ |     |     |
| --- | ------- | -------------- | --- | --- |
QoS flow classification is an important part of the flow persona  ⎢ 𝑑𝑒 𝑡ℎ 𝑙𝑜 ⎥
|     | 𝑊 = 𝑤𝑈 𝑠𝑒𝑟2 | 𝑤𝑈 𝑠𝑒𝑟2 𝑤𝑈 𝑠𝑒𝑟2 |     | (14) |
| --- | ----------- | --------------- | --- | ---- |
model, which is used to classify and identify network flow data so as  ⎢ 𝑑𝑒 𝑡ℎ 𝑙𝑜 ⎥
|     | ⎢ 𝑤𝑈 𝑠𝑒𝑟3 | 𝑤𝑈 𝑠𝑒𝑟3 𝑤𝑈 𝑠𝑒𝑟3⎥ |     |     |
| --- | --------- | ---------------- | --- | --- |
to formulate appropriate rules and strategies for QoS flow. In this part,  ⎣ 𝑑𝑒 𝑡ℎ 𝑙𝑜 ⎦
in order to realize QoS flow classification, we adopt a fine-grained QoS
Where 𝑤𝑈𝑠𝑒𝑟𝑖 indicates the delay weight of user 𝑖, 𝑤𝑈𝑠𝑒𝑟𝑖 indicates
flow classification method [34] to form a QoS flow rule scheme. 𝑑𝑒 𝑡ℎ
the throughput weight of user 𝑖, and 𝑤𝑈𝑠𝑒𝑟𝑖 indicates the packet loss
𝑙𝑜
| 4.2.1.  Data Pre-processing | rate weight of user 𝑖. |     |     |     |
| --------------------------- | ---------------------- | --- | --- | --- |
In the data pre-processing stage, we process and prepare the original  We obtain the 𝑄′ matrix by multiplying 𝑄 with 𝑊. To normalize the
network flow data to facilitate subsequent service classification based  value range of different features, each 𝑄′ matrix is normalized before
| on QoS attribute values. | constructing the training sample. |     |     |     |
| ------------------------ | --------------------------------- | --- | --- | --- |
First, a significant volume of flow data is collected from the net-
|                                                                            |          | 𝑄′(𝑡,𝑠)−𝑄′ (𝑡,𝑠) |     |      |
| -------------------------------------------------------------------------- | -------- | ---------------- | --- | ---- |
|                                                                            | 𝑄′(𝑡,𝑠)= | min              |     | (15) |
| work, with a collection interval of 𝑡 seconds. The data is then subjected  | 𝑛        |                  |     |      |
|                                                                            | 𝑄′       | (𝑡,𝑠)−𝑄′ (𝑡,𝑠)   |     |      |
to cleaning procedures, eliminating outliers, noise, and invalid data to  max min
ensure data quality and accuracy. Subsequently, the QoS attribute value  Among them, 𝑄′(𝑡,𝑠) denotes the normalized values, 𝑄′ (𝑡,𝑠)repre-
|     |     | 𝑛   |     | min |
| --- | --- | --- | --- | --- |
corresponding to each flow data is calculated using the formula intro- sents the minimum of the 𝑠-th 𝑄′ matrix values, and 𝑄′ (𝑡,𝑠) denotes
max
duced in Section 3.3. This generates the QoS Attribute Matrix, which  the maximum of the 𝑠-th 𝑄′ matrix values.
captures the values of the QoS attributes (as described in Section 4.2.2).  By organizing this data in the form of a 𝑄′ matrix, it can be arranged
Next, the data is standardized, unifying the value range of different fea- based on time and attribute, facilitating analysis and processing. This ar-
tures. This standardization is essential for achieving high-fine-grained  rangement is particularly useful when dealing with real-time QoS flow
classification and facilitates training and classification tasks for the CNN  problem, as it enables the capture and analysis of temporal characteris-
model. Lastly, the dataset is divided into training and validation sets. No- tics of QoS attributes. It allows for a better observation of patterns and
tably, during CNN model training, it is necessary to label the type of flow  trends in QoS attribute changes over time, and facilitates the extraction
of valuable time series features, which is convenient to solve the QoS
data to which each sample belongs: video streaming, audio streaming,
or ordinary data streaming. After the data cleaning process, the network  real-time problem.
flow relevant to the target task is filtered, aiming to provide comprehen- Scalability within the FlowPersona framework is addressed in two
sive network state information that facilitates the training of the CNN  complementary dimensions. First, at the network level, the SDN-IoT
model. mesh topology enables seamless horizontal expansion by incorporating
additional Segment Routing nodes, ensuring stable performance even
4.2.2.  QoS Attribute Matrix under increasing device density. Second, at the ML model level, the
In [35], the author presents an effective approach to meeting users’  APSO-optimized CNN is trained using flow data from multiple network
QoS requirements by aggregating the QoS attributes of each service in  scales, making the classifier robust to traffic heterogeneity. For model
8

H. She et al. Computer Networks 273 (2025) 111784
Fig. 4. Optimized CNN classification model based on APSO algorithm.
validation, the collected dataset is partitioned into training, validation, Algorithm 2 The algorithm for finding the optimal hyperparameters of
and testing sets, with k-fold cross-validation applied to mitigate over- CNN model.
fitting. This design ensures that Flow Persona can generalize well to 1: Input: 𝑄′ matrix
unseen data and maintain accuracy as the IoT platform scales. Further- 2: Output: The optimal hyperparameters
more, its modular structure allows incremental retraining when new 3: Initialize: Vectorize the parameters and use binary encoding as the
flow patterns appear, thereby sustaining long-term scalability. position of particles; Randomly select a set of particles as the ini-
tial positions and velocities of the particle swarm, with the initial
4.2.3. Framework velocities generated using random numbers;
This paper adopts a classification model that optimizes the hyperpa- 4: while 𝑖≤𝐺 do
rameter structure of a one-dimensional CNN using an adaptive particle 5: Calculate the fitness value 𝐹 for each particle, choose 𝐹 , 𝐹 ,
𝑚𝑖𝑛 𝑎𝑣𝑔
swarm. By training the model and optimizing the hyperparameters of the and 𝐹cur ;
neural network, suitable hyperparameters can be found. This approach 6: Categorize the state by 𝑓’s value, and adaptive control strategies
avoids the high labor cost of manually adjusting hyperparameters to find are chosen accordingly.
a model suitable for the QoS flow classification task. Consequently, it im- 7: Update the inertia weight 𝜔;
proves the accuracy of classification, as well as the training speed and 8: Update the 𝑝𝑏𝑒𝑠𝑡𝑖 and 𝑔𝑏𝑒𝑠𝑡𝑖 according to the fitness value 𝐹;
effectiveness of the neural network. The specific classification model of 9: Update the veloc 𝑖 i 𝑘 ty 𝑣𝑖+1 and 𝑘 position 𝑥𝑖+1 of the particles accord-
the CNN, optimized based on the APSO algorithm, is illustrated in Fig. 4. ing to (24) and (25); 𝑖𝑘 𝑖𝑘
One-dimensional CNN model construction: CNN is a multi-layer 10: 𝑖=𝑖+1;
neural network where each layer consists of multiple two-dimensional
11: end while
planes [37]. Neurons in each layer compute their output by weighting
and summing the elements from the previous layer and applying an acti-
vation function. In this study, we use a one-dimensional CNN to classify
QoS attribute flows Algorithm 2. data. Furthermore, the feature planes are flattened before connecting
As we consider 𝑄′ as the model’s input and treat the flow data to the subsequent layer through the second pooling layer. To miti-
as a time series where each observation represents different types of gate potential overfitting during training, dropout is implemented to
flow data at each time point, the input data is transformed into a two- improve the network’s generalization ability in each training session
dimensional array. The dimensions of the input layer are (1000, 3), [38]. As a result, certain neurons cease to function with a specific
where each sample represents an instance of network flow. The one- probability, leading to different active neuronal nodes in each train-
dimensional convolution process is depicted in Fig. 5. ing batch and cycle. The dimensions of the output layer are also (1000,
The hidden layer comprises 6 layers, each serving unique functions 3), with 3 representing the classification result, i.e., the three service
and producing distinct effects. The convolution layer extracts deeper categories (also the number of output nodes). Moreover, we assign dif-
and higher-level features by performing convolutions on pre-processed ferent weights according to the importance of each QoS attribute value
9

H. She et al.
Computer Networks 273 (2025) 111784
Step 2: Iterative updating of the particle swarm. Based on the busi-
ness scenario and network environment, we employ the cross-entropy
loss function to evaluate model performance. Predictions are made us-
ing a feedforward neural network, and the loss function for the current
weights is computed. The weights and biases are then updated using
the error backpropagation algorithm based on the gradient of the loss
function to minimize the loss value. During the first training cycle, we
set the cross-entropy value of the CNN as the fitness function value of
the particle [42]. We evaluate the fitness of all particles, selecting the
one with the smallest fitness value as the global optimal particle. This
method speeds up model training and minimizes the gap between actual
and predicted classifications, as a lower cross-entropy loss reflects bet-
ter prediction accuracy. Next, we compute the distance 𝑑 between the
𝑙
global optimal particle and its nearest neighbor. We then compare the
|     |     |     |     |     |     | maximum 𝑑 |  and minimum distances 𝑑 |     |     |  among all particles, and  |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------ | --- | --- | -------------------------- | --- | --- |
|     |     |     |     |     |     |           | 𝑚𝑎𝑥                      |     |     | 𝑚𝑖𝑛                        |     |     |
calculate the average distance of particle 𝑖 to all other particles using
Fig. 5. One-dimensional convolution process.
the Euclidean metric as shown in Eq. 16. This allows us to determine
the evolution factor 𝑓.
√
𝑁 √ 𝐷
to each of the three service categories to ensure that the classification  1 ∑ √ ∑
|     |     |     |     |     |     | 𝑑 = | √   | (𝑥𝑘 | −𝑥𝑘 )2 |     |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---- |
results align as closely as possible with the actual outcomes. For hy- 𝑖 𝑁−1 𝑖𝑑 𝑗𝑑
𝑗=1,𝑗≠𝑖 𝑑=1
perparameters such as weight, bias, and learning rate that require op-
|     |     |     |     |     |     | 𝑑   | 𝑙 −𝑑 min |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
timization in the model, we define them as unknown variables to be 𝑓 = (17)
𝑑 −𝑑
| determined. |     |     |     |     |     | max | min |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Where 𝑁 denotes the particle population size and the evolution fac-
Training the hyperparameters of the CNN model base on the  tor 𝑓 ∈[0,1]. Based on the value of 𝑓, fuzzy classification divides into
APSO algorithm: Adaptive Particle Swarm Optimization is a heuris-
|     |     |     |     |     |     | four states: exploration state 𝑆 |     |     | , development state 𝑆 |     | , convergence  |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --------------------- | --- | -------------- | --- |
tic optimization algorithm proposed by Zhan 𝑒𝑡 𝑎𝑙. [39]. As a deriva- 1 2
|     |     |     |     |     |     | state 𝑆 | , and jump state 𝑆 |     | . The formula for determining the classifi- |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | ------------------------------------------- | --- | --- | --- |
tive optimization model of the Particle Swarm Optimization (PSO) algo- 3 4
cation value is as follows:
rithm, the APSO algorithm offers enhanced optimization performance.
The evolution factor (f) is used to assess the state of the particle swarm  1. Exploration state 𝑆 :
1
and dynamically adjust the weight based on this state, improving global
search capability. In the training process of the standard PSO algorithm,  ⎧0 if 0≤𝑓 ≤0.4
if the inertia weight 𝜔 is set to a large value, particles can easily escape  ⎪ if 0.4<𝑓 ≤0.6
⎪5𝑓−2
| l o c  | a l   op t i m a ,  b u | t  i t  m a y  |   h i n d e r   i te ra | t i v e  c on v e r g e n c e  | in  l a t e r  s t a g e s  o f  |        | ⎪       |          |      |     |     |      |
| ------ | ----------------------- | -------------- | ----------------------- | ------------------------------ | -------------------------------- | ------ | ------- | -------- | ---- | --- | --- | ---- |
|        |                         |                |                         |                                |                                  | 𝜇 (𝑓)= | 1       | if 0.6<𝑓 | ≤0.7 |     |     | (18) |
| t ra i | n i n g. C o n v e rs   | e l y , i f  t | h e in e r t i a  w     | e i g h t  i s  s e t  t o  a  |  s m a l l  v a l u e ,  p a r - | 𝑆1     | ⎨       |          |      |     |     |      |
|        |                         |                |                         |  𝜔                             |                                  |        | ⎪−10𝑓+8 | if 0.7<𝑓 | ≤0.8 |     |     |      |
ticles tend to get trapped in locally optimal solutions [40]. The APSO
⎪
|                                                                         |     |     |     |     |     |     | ⎪0  | if 0.8<𝑓 | ≤1  |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
| algorithm addresses the negative impact of random initialization speed  |     |     |     |     |     |     | ⎩   |          |     |     |     |     |
on particle optimization by dynamically adjusting the inertia weight,  2. Development state 𝑆 :
2
simplifying the algorithm and accelerating convergence. By using APSO
to optimize the hyperparameters of a CNN and integrating QoS flow  ⎧0 if 0≤𝑓 ≤0.2
classification requirements during training, both training time and labor  ⎪ if 0.2<𝑓 ≤0.3
⎪10𝑓−2
| c o s  | t s  a re   s ig n i fi c | a n t ly   re    | d u c ed   c o m p  | a re d   to   tr a d i t io n a | l  m a n u a l  pa r a m e - |        |     |          |      |     |     |      |
| ------ | ------------------------- | ---------------- | ------------------- | ------------------------------- | ---------------------------- | ------ | --- | -------- | ---- | --- | --- | ---- |
|        |                           |                  |                     |                                 |                              | 𝜇 (𝑓)= | ⎪ 1 | if 0.3<𝑓 | ≤0.4 |     |     | (19) |
| te r   | a d ju s t m e n t  o     | r   st a ti c  o | p t im i z a t io n |  m e t h o d s .  F u r th e    | r m o r e ,  co m b i n in g |   𝑆2   | ⎨   |          |      |     |     |      |
|        |                           |                  |                     |                                 |                              |        | ⎪   | if 0.4<𝑓 | ≤0.6 |     |     |      |
the ARIMA model with the APSO algorithm allows for the design of a  −5𝑓+3
⎪
real-time optimization strategy based on the dynamic characteristics of  ⎪0 if 0.6<𝑓 ≤1
⎩
QoS flow, thereby enhancing the real-time classification capability of
|               |     |     |     |     |     | 3. Convergence state 𝑆 |     | :   |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
| network flow. |     |     |     |     |     |                        |     | 3   |     |     |     |     |
We need to collect network flow data and apply principal component  ⎧1 for 0≤𝑓 ≤0.1
a n a l y s is   ( P C A )  t o  r ed u c e   it s  d i m e n s io n al i t y ,  t h e n   r ep r es e n t  i t  a s  a   te ns o r .  𝜇 (𝑓)= ⎪ −5𝑓+1.5 for 0.1<𝑓 ≤0.3 (20)
|                                                                          |                           |               |                        |                               |                               | 𝑆3  | ⎨   |           |     |     |     |     |
| ------------------------------------------------------------------------ | ------------------------- | ------------- | ---------------------- | ----------------------------- | ----------------------------- | --- | --- | --------- | --- | --- | --- | --- |
| W e                                                                      |   t h e n   s p l it  t h | e  d at a s e | t   in t o  t w o   eq | u a l   p a r t s:   o n e  w | i th   b o t h   n e tw o r k |     |     |           |     |     |     |     |
|                                                                          |                           |               |                        |                               |                               |     | ⎪0  | for 0.3<𝑓 | ≤1  |     |     |     |
| flow data and classification labels, and another with only network flow  |                           |               |                        |                               |                               |     | ⎩   |           |     |     |     |     |
data. The first part is used to train an untrained CNN model to obtain  4. Jump state 𝑆 :
4
an optimal model for network flow classification.
|     |     |     |     |     |     |     | ⎧0  | for 0≤𝑓 | ≤0.7 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | --- | --- |
The specific process of training the hyperparameters of the CNN
|     |     |     |     |     |     |     | ⎪   | for 0.7<𝑓 | ≤0.9 |     |     | (21) |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --- | --- | ---- |
model base on the APSO algorithm, as described in this paper, is out- 𝜇 𝑆4 (𝑓)= ⎨ 5𝑓−3.5
| lined below: |     |     |     |     |     |     | ⎪ 1 | for 0.9<𝑓 | ≤1  |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
⎩
Step 1: Coding and initialization of model hyperparameters. The
Step 3: Hyperparameter optimization and weight updating. Firstly,
adaptive particle swarm’s global search capability is utilized to vector-
|     |     |     |     |     |     | the boundary for 𝑐 |     |  and 𝑐 |  is defined as follows: | | 𝑐   | (𝑔+1)−𝑐 | (𝑔)| ≤𝛿,  |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------------------------- | --- | ------- | --------- |
ize the hyperparameters of the CNN model that needs to be solved, with  1 2 | 𝑖 𝑖 |
where 𝑐(𝑔) represents the value of 𝑐 at the 𝑔-th iteration and 𝛿∈
binary coding used for the particle position [41]. A group of particles  𝑖 𝑖
|     |     |     |     |     |     | [0.05,0.1] represents acceleration. Since 𝑐 |     |     |     | +𝑐 ≤4.0, if the sum of 𝑐 |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | ------------------------ | --- | --- |
is randomly selected to define the initial positions and velocities of the  1 2 1
and 𝑐  exceeds 4.0, normalization is applied:
| particle swarm, with their positions serving as the historical optimal po- |     |     |     |     |     | 2   |     |     |     |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑐
sitions. The initial velocities are set using random numbers. The accel- 𝑖 (22)
|                        |     |        |                                               |     |     | 𝑐 𝑖 = | ×4.0, | 𝑖=1,2 |     |     |     |     |
| ---------------------- | --- | ------ | --------------------------------------------- | --- | --- | ----- | ----- | ----- | --- | --- | --- | --- |
| eration coefficients 𝑐 |     |  and 𝑐 |  for the cognitive and social parameters are  |     |     | 𝑐 1   | +𝑐 2  |       |     |     |     |     |
1 2
initialized to 𝑐 =𝑐 =2.0. The maximum and minimum inertia weights  Then, based on the classification results from Step 2, the acceleration
1 2
are set to 𝜔max=0.9 and 𝜔max=0.9, respectively. coefficients 𝑐  and 𝑐  are adjusted adaptively: in the exploration state, 𝑐
|     |     |     |     |     |     |     | 1   | 2   |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10

H. She et al.
Computer Networks 273 (2025) 111784
increases by 0.05 and 𝑐  decreases by 0.05; in the development state, 𝑐 5.  Experimental Results and Performance Evaluation
|                          |     | 2                                               |     |     |     | 1   |     |     |     |     |     |
| ------------------------ | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| increases by 0.005 and 𝑐 |     |  decreases by 0.005; in the convergence state,  |     |     |     |     |     |     |     |     |     |
2
| both 𝑐       |  and 𝑐  increase by 0.005; and in the jump state, 𝑐         |     |     |     |  decreases by  |     |             |     |     |     |     |
| ------------ | ----------------------------------------------------------- | --- | --- | --- | -------------- | --- | ----------- | --- | --- | --- | --- |
|              | 1 2                                                         |     |     |     | 1              |     | 5.1.  Setup |     |     |     |     |
| 0.05 while 𝑐 |  increases by 0.05. Finally, the inertia weight is updated  |     |     |     |                |     |             |     |     |     |     |
2
using the formula as follows. To simulate and evaluate the performance of the proposed flow per-
sona model, we utilize an NS-3-based network simulator. The network
module is implemented on the NS-3 platform to capture flowing data in
| ⎧   |     |     | 𝐹 c u r− 𝐹 if 𝐹cur | ≤𝐹avg |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
⎪ 𝜔 min −(𝜔 max −𝜔 min ) m i n , three different service scenarios, creating datasets and calculating the
| 𝜔=  |     | 𝐹   | a v g − 𝐹 m i n |     |     | (23) |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
⎨ if 𝐹cur>𝐹avg c o r r e s p o n d i n g  Q o S   a tt r i b u t e   v a l u es .  E a c h   s e r v i c e   sc e n a r i o  c o r r es p o n d s
⎪ 𝜔 max ,
⎩ to   a   s p e c ifi c   tr a ffi c  t y p e - s u c h   a s   v id e o ,  a u d i o ,  o r   o r d in a r y   d a ta - a n d  i s  a s -
signed distinct QoS attributes including delay sensitivity and bandwidth
Here, 𝐹  represents the fitness function value of the current particle,  demand. Since we employ software simulation, real-time collection of
𝑐𝑢𝑟
𝐹  denotes the average fitness function value of the current population,  packet loss rate is not feasible. Therefore, we randomly set the packet
𝑎𝑣𝑔
and 𝐹  signifies the fitness function value of the globally optimal par- loss rate within the range of [0.0001-0.1] [43]. Furthermore, the CNN
𝑚𝑖𝑛
ticle. This process ensures that each parameter gradually adjusts within  model trained using the APSO algorithm is built on the TensorFlow deep
the search space, moving toward a direction that allows for accurate
learning framework.
classification based on QoS attribute values. For the labeled flow dataset consisting of 1000 instances, we divide
Step 4: Update particle position and velocity. The position and ve- it into two parts: 80% serves as the training set, and the remaining 20%
locity of each particle are updated following the rules of the APSO al- is allocated as the validation set. Performance tests are conducted on
gorithm. The velocity update formula is: an Intel Core i7 machine with 32 GB of RAM and an NVIDIA GeForce
RTX 4060 GPU card. Additionally, in order to accommodate the flow
𝑣𝑘+1=𝜔𝑣𝑘 (𝑝𝑏𝑒𝑠𝑡𝑘 (𝑔𝑏𝑒𝑠𝑡𝑘 −𝑥𝑘 (24) persona model we constructed, we deploy 500 SR nodes in the network.
|     | +𝑐  | 𝑟𝑎𝑛𝑑 | )+𝑐 𝑟𝑎𝑛𝑑 |        | )   |     |     |     |     |     |     |
| --- | --- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| 𝑖𝑚  | 𝑖𝑚  | 1 1  | 𝑖𝑚 2     | 2 𝑚 𝑖𝑚 |     |     |     |     |     |     |     |
The position update formula is: 5.2.  Discussion of Algorithm
Based on experimental data analysis, we assign different weights to
| 𝑥𝑘+1=𝑥𝑘 | +𝑣𝑘+1 |     |     |     |     | (25) |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
𝑖𝑚 𝑖𝑚 𝑖𝑚 each QoS attribute according to the importance for each service category
|     |     |     |     |     |     |     | [44],[45],[46]. For instance, 𝑈𝑠𝑒𝑟 |     | , which primarily uses video stream- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | ------------------------------------ | --- | --- |
Where 𝑣𝑘 =[𝑣𝑘 ,𝑣𝑘 ,𝑣𝑘 ,…,𝑣𝑘 ] denotes the velocity parameters, and  1 -to-end delay weight 𝑤𝑈𝑠𝑒𝑟1 = 0.29,
|     | 𝑖   | 𝑖1 𝑖2 𝑖3 | 𝑖𝐷  |     |     |     | ing, has the following weights: end |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
𝑥 𝑘 = [ 𝑥 𝑘 , 𝑥𝑘 , 𝑥 𝑘 , … , 𝑥 𝑘 ]  d e n o t e s   th e   p o s it i o n   p a r a m e t e r s .   𝑣 𝑘 + 1   r ep re - 𝑑 𝑒
𝑖 𝑖1 𝑖 2 𝑖 3 𝑖𝐷 𝑖𝑚 throughput weight 𝑤𝑈 𝑠𝑒𝑟1 = 0.57, and packet loss rate w e ight 𝑤𝑈 𝑠𝑒𝑟1
se n ts  t h e  𝑚 - t h   c o m p o n en t  o f  t h e   v e lo c i t y  o f   p a r ti c l e  𝑖  a t  i t e r a t i o n   𝑘 + 1 ,  𝑡ℎ 𝑙𝑜
|                                                                      |     |     |     |     |     |     | = 0.14. 𝑈𝑠𝑒𝑟 | , which tends to use audio streaming media, has weights:  |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --------------------------------------------------------- | --- | --- | --- |
| and 𝑥𝑘+1 represents the 𝑚-th component of the position of particle 𝑖 |     |     |     |     |     |     |              | 2                                                         |     |     |     |
𝑖 𝑚 𝑤𝑈 𝑠𝑒𝑟2 = 0.45 , 𝑤𝑈 𝑠𝑒𝑟2 = 0.25, and 𝑤𝑈 𝑠𝑒𝑟2 = 0.30. Lastly, 𝑈𝑠𝑒𝑟 , which
at iter a tion 𝑘+1. 𝐷 is the dimension of the particle swarm, 𝑟𝑎𝑛𝑑  and  3
|     |     |     |     |     |     | 1   | 𝑑𝑒  | 𝑡ℎ  | 𝑙𝑜  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 are two random numbers uniformly distributed in the int erval  uses ordinary data streaming media, has weights: 𝑤𝑈 𝑠𝑒𝑟3 = 0.32, 𝑤𝑈 𝑠𝑒𝑟3
| 𝑟𝑎𝑛𝑑 2 |     |     |     |     |     |     |     |     |     | 𝑑𝑒  | 𝑡ℎ  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[0,1]. 𝑝𝑏𝑒𝑠𝑡𝑘  denotes the best position found by the current particle,  = 0.43, and 𝑤𝑈𝑠𝑒𝑟3 = 0.25.
| and 𝑔𝑏𝑒𝑠𝑡𝑘 denotes the best position found by the entire particle swarm. | 𝑖𝑚  |     |     |     |     |     | Regarding the CNN model trained using the APSO algorithm, the pa- | 𝑙𝑜  |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
𝑚
Step 5: Convergence Judgement and Termination. Repeat steps 2- rameters are configured as follows: The maximum number of iterations
4 until the convergence condition is met. Convergence is determined  for the particle swarm is set to 200, the population size is 30, the acceler-
when the maximum number of iterations is reached, and the training  ation coefficient 𝑐 =𝑐 =2, the minimum inertia weight is 𝑤 =0.4,
|     |     |     |     |     |     |     |     | 1 2 |     |     | 𝑚𝑖𝑛 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
process is terminated. and the maximum inertia weight is 𝑤 =0.9. Considering precision
𝑚𝑎𝑥
Step 6: Selecting the Optimal Solution. During the particle swarm’s  and real-time requirements, the data collection interval during the train-
iterative process, the global optimal fitness function value and its cor- ing process is set to 0.25 seconds (𝑡=0s, 0.25s, 0.50s, 0.75s...). Setting
responding model hyperparameters are tracked. The hyperparameters  the data acquisition time to 0.25 seconds significantly improves real-
associated with the particle having the smallest fitness function value  time performance while reducing network bandwidth usage. Given the
are selected as the global optimal solution and are used as the optimal  dynamic nature of the network, this collection interval exhibits strong
hyperparameters for the APSO-CNN model. This model represents the  adaptability to network jitter, thereby enhancing the network’s robust-
optimal CNN model. The latter part of the dataset is then fed into this  ness [47]. In the actual classification process using the optimized model
optimal CNN model, and the output matrix is processed through the soft- parameters, all flow data is collected every minute, resulting in a data
max function to obtain the probability distribution of the network flow  collection interval of 𝑡=60/1000=0.06s. This balance between data
data’s category. The category with the highest probability is determined  precision and real-time requirements helps reduce data processing com-
| to be the classification of the network flow data, thereby achieving net- |     |     |     |     |     |     | plexity. |     |     |     |     |
| ------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
work flow classification. Based on the results from [48] and [49], a comparative experiment of
While the simulation setup in this work utilizes a mid-scale IoT- optimizers was conducted using the VGG + BN + Dropout network and
oriented topology, the FlowPersona architecture is designed to be  the DenseNet architecture on the dataset. The experimental results in-
topology-independent and scalable. The user persona construction and  dicate that SGD (stochastic gradient descent) performs the best in terms
QoS classification rely on global traffic features and user behavior pat- of test accuracy and convergence speed. Given that this paper involves a
terns, which do not grow proportionally with the number of nodes.  multi-classification task, we choose SGD as the optimization method for
Therefore, the computational cost remains stable under larger topolo- the model training process. To address the frequent oscillation issue of
gies such as GEANT or Internet2. In terms of flow diversity, the CNN  SGD at local optima, we introduce a first-order momentum setting of 0.9
classifier is trained using mixed service types (video, audio, ordinary)  and dynamic learning rate decay to improve the training effectiveness
| to ensure robust prioritization across concurrent heterogeneous flows.  |     |     |     |     |     |     | [42]. |     |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Moreover, although this paper does not focus on link or node failure re- As depicted in Fig. 6, after 200 iterations of optimization, the par-
covery, FlowPersona’s modular design allows seamless integration with  ticle achieved a minimum fitness value of 𝑓 = 𝑓 =0.1398. This
|     |     |     |     |     |     |     |     |     |     | 𝑚𝑖𝑛 𝑏𝑒𝑠𝑡 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
fault-tolerant SDN control frameworks or routing resilience modules.  value also represents the minimum loss function value achieved on the
These aspects are considered future work directions to enhance deploy- validation set after the initial training. By identifying the parameters
ment robustness in real-world environments. corresponding to the minimum fitness function value, we can determine
11

H. She et al. Computer Networks 273 (2025) 111784
Fig. 6. Iterative results of particle. Fig. 8. Accuracy in training set.
Fig. 9. Accuracy in validation set.
Fig. 7. Accuracy of flow persona in training set and validation set.
Precision(𝑃): Calculated as the ratio of true positives 𝑇 to the sum
𝑝
the optimal hyperparameters for the CNN model. Specifically, 62 con- of true positives and false positives 𝐹 for each service class:
𝑝
volution kernels in the first layer, 48 convolution kernels in the second
𝑃 =𝑇 ∕(𝑇 +𝐹 ) (26)
layer, relu activation functions for both convolution layers, filters with a 𝑝 𝑝 𝑝
length of 2 in the first and second convolutional layers, a dropout rate of Recall rate (𝑅): For each category, it is defined as the ratio of true
0.25, 53 neurons in the first fully connected layer with relu activation, positives 𝑇 𝑝 to the sum of true positives and false negatives 𝐹 𝑛 :
35 neurons in the second fully connected layer with tanh activation, a 𝑅=𝑇 ∕(𝑇 +𝐹 ) (27)
𝑝 𝑝 𝑛
batch size of 154, and a learning rate of 0.08.
These optimal hyperparameters are then incorporated into the CNN F-score: It is defined as the harmonic mean of accuracy 𝑃 and recall
model, as illustrated in Fig. 4. The values of the cross-entropy loss
𝑅, taking into account the performance of both:
function and accuracy for the training set, as well as the cross-entropy 𝐹 =((1∕𝑃+1∕𝑅)∕2)−1=2𝑅𝑃∕(𝑅+𝑃) (28)
loss function and accuracy for the validation set, are obtained for
each training cycle. Fig. 7 presents the accuracy of the training set
5.4. Performance Comparison
and the validation set of the flow persona model using the optimal
hyperparameters.
In this paper, we compare the flow persona model with the APSO-
based RNN model, as well as the RNN, CNN, and SVM models, where the
latter three directly classify the QoS flow without undergoing training
5.3. Performance Metrics through the APSO algorithm. The comparison results on the training set
and the validation set are presented in Fig. 8 and Fig. 9.
We assess the performance of the model on validation sets using pre- It is evident that starting from epoch 91, the accuracy of the flow
viously unseen QoS flow data. To evaluate the accuracy of QoS flow persona model showed a significant increase, surpassing the other four
classification results, we compare the predictions of the flow persona models. Moreover, a similar trend in accuracy was observed in the
model with the actual labels. The following indexes are calculated for validation set. After 200 epochs of training, the flow persona model
assessment: accuracy, precision, recall rate, and F-score. achieved an accuracy of approximately 94.6% on the validation set,
Accuracy: It is defined as the ratio of the number of correctly classi- while the other four models achieved around 90% accuracy. This in-
fied QoS flows to the total number of QoS flows currently input dicates that the flow persona model has higher classification accuracy
12

H. She et al. Computer Networks 273 (2025) 111784
Table 3
Performance comparison of five models.
Model Precision Recall F-score
APSO-RNN 0.911 0.911 0.911
RNN 0.899 0.901 0.900
CNN 0.908 0.909 0.908
SVM 0.888 0.889 0.889
FlowPersona 0.936 0.936 0.936
Fig. 11. Throughput of the network under different algorithms.
Fig. 10. Delay of the network under different algorithms.
and better overall classification performance. It demonstrates that the
algorithm processing of the flow persona model is well-designed and
has a positive impact on QoS flow classification, resulting in a well-
performing QoS flow rule scheme. It also demonstrates that the APSO
algorithm effectively promotes hyperparameter optimization of the CNN
model and attains the global optimal solution.
Next, we evaluated these models in terms of precision 𝑃, recall rate
𝑅, and F-score to measure classification accuracy. As shown in Table 3,
the flow persona model achieved a precision, recall rate, and F-score of
Fig. 12. Average routing computation time of all algorithms.
0.936. This indicates that the flow persona model can accurately classify
positive and negative cases, better capturing the true positive cases and
achieving a good balance between precision and recall rate. In compar- However, it should be noted that the convergence speed of the flow
ison to the other four models, particularly the slightly superior APSO- persona model for QoS flow classification is comparatively slower than
RNN model. The flow persona model demonstrates a 2.7% improvement that of the RNN and CNN models. According to the ‘No Free Lunch the-
in precision, recall rate, and F-score. These results clearly indicate that orem’ [50], no algorithm can excel in all aspects or classes of problems.
the flow persona model achieves higher accuracy and overall perfor- Therefore, enhancing the convergence speed of the flow persona model
mance in QoS flow classification. for QoS flow classification and developing an intelligent routing algo-
We are not merely satisfied with the results of QoS flow classifica- rithm are key challenges that we aim to address in our future research.
tion. Additionally, we applied the traditional OSPF routing algorithm
to route the data post-QoS classification, as shown in Fig. 10, Fig. 11 6. Conclusion
and Fig. 12. From Fig. 10, it is evident that the average delay after
routing with the flow persona model is significantly better than that of In this paper, we propose a flow persona model to address the chal-
the OSPF, RIP, and RIP-persona routing algorithms. This improvement lenges of managing diverse data flow in SDN-IoT scenarios and meeting
is attributed to the QoS flow classification prior to routing. However, specific requirements. This model accurately classifies QoS flows and
the DDQN-persona algorithm achieves an average delay of 139.2ms, effectively targets them to different services.
outperforming the Flow Persona’s 158.2ms. As shown in Fig. 11, the In Section 3, a large number of SR nodes are deployed across the
throughput value of the flow persona is moderate, and it can well pro- network. The flow persona model is divided into four main compo-
vide different specific flows according to different service categories. nents: user information collection, service category classification, QoS
This avoids the extremes of high or low throughput, which could other- flow classification, and algorithm processing. In the algorithm process-
wise lead to performance bottlenecks, degraded user experience, or net- ing part, we address the real-time QoS flow issue using the ARIMA sta-
work performance issues. In terms of average route computation time, tistical algorithm. When training the CNN model with the APSO algo-
the flow persona model is also slightly less efficient than DDQN-persona. rithm, the cross-entropy loss function value during the initial training
Nonetheless, we believe that with the design of an effective AI routing period of the CNN is used as the fitness value for APSO. During the par-
algorithm specifically for flow persona, it can leverage real-time user ticle swarm iteration and optimization process, by updating the swarm’s
and service requirements from persona for dynamic routing, potentially velocity and position, we identify the smaller fitness values, ultimately
surpassing the performance of modern AI-based routing algorithms like leading to the discovery of the optimal CNN model. Simulation results
DDQN-persona. demonstrate that the flow persona model performs well in QoS flow
13

H. She et al. Computer Networks 273 (2025) 111784
classification. Compared to traditional routing algorithms, the flow per- [12] W. Shuai, D. Yuning, L. Tao, Network Traffic Classification Based on LSTM and
sona model offers significant advantages, highlighting its effectiveness. Feature Generation, Journal of Applied Sciences 40 (05) (2022) 758–769.
[13] J. Prados-Garzon, T. Taleb, M. Bagaa, Optimization of Flow Allocation in Asyn-
In summary, the flow persona model possesses remarkable applica-
chronous Deterministic 5G Transport Networks by Leveraging Data Analytics 22
bility and flexibility. This model can deliver effective QoS policies for (2021) 1–1.
various services in large-scale IoT deployments, leveraging diverse net- [14] G. Hu, X. Xiao, M. Shen, B. Zhang, X. Yan, Y. Liu, TCGNN: Packet-grained network
work resources for precise QoS flow scheduling. It is also capable of traffic classification via Graph Neural Networks 123 (2023) 106531.
[15] J. Zhang, F. Li, F. Ye, Sustaining the High Performance of AI-Based Network Traffic
handling the future growth in network devices, ensuring optimal user Classification Models 31 (2023) 816–827.
experience and satisfaction. Additionally, the model has significant po- [16] M. Ibrar, L. Wang, N. Shah, O. Rottenstreich, G.-M. Muntean, A. Akbar, Reliability-
tential for real-world applications. For example, in smart cities, it can Aware Flow Distribution Algorithm in SDN-Enabled Fog Computing for Smart Cities
72 (2023) 573–588.
be integrated into IoT networks to optimize the operation of traffic
[17] L. Xingtong, Z. Hong, H. Jianhua, An Improved Proximal Optimization Multi-
lights, energy management systems, and emergency response mecha- objective Flow QoS Scheduling Strategy, Journal of Applied Sciences 42 (03) (2024)
nisms through accurate classification and efficient scheduling of critical 499–512.
[18] N. Saha, S. Misra, S. Bera, Q-flag: QoS-aware flow-rule aggregation in software-
traffic. This would enhance urban resource utilization and improve res-
defined IoT networks, IEEE Internet of Things Journal 9 (7) (2021) 4899–4906.
idents’ quality of life. However, some limitations should be noted. In [19] S. Paramasivam, R. Leela Velusamy, J.V. Nishaanth, Categorical learning for auto-
practical deployment, factors like device mobility and priority conflicts mated network traffic categorization for future generation networks in SDN, Com-
puting 106 (5) (2024) 1451–1473. https://doi.org/10.1007/s00607-024-01277-y
in large-scale networks need to be carefully addressed.
[20] S. Xie, G. Hu, C. Xing, Y. Liu, Online Elephant Flow Prediction for Load Balancing in
In the future, we will focus on efficiently managing flow rules, con- Programmable Switch-Based DCN, IEEE Transactions on Network and Service Man-
sidering factors such as mobility, rule priority, overhead, and network agement 21 (1) (2024) 745–758. https://doi.org/10.1109/TNSM.2023.3318752
[21] J. Zhang, F. Li, F. Ye, Sustaining the High Performance of AI-Based Network Traf-
capacity constraints. It will also involve further collection and analysis
fic Classification Models, IEEE/ACM Transactions on Networking 31 (2) (2023)
of flow statistics, exploring the applicability of algorithms across differ- 816–827. https://doi.org/10.1109/TNET.2022.3203227
ent network structures and scales, and investigating multi-agent cooper- [22] J. Zhao, Q. Li, Y. Hong, M. Shen, MetaRockETC: Adaptive Encrypted Traffic Clas-
ative training and planning methods based on reinforcement learning. sification in Complex Network Environments via Time Series Analysis and Meta-
Learning, IEEE Transactions on Network and Service Management (2024).
Additionally, integrating heuristic algorithms will enhance the adapt- [23] X. Wang, W. Wei, X. Yu, D. Zheng, N. Kuma, L. Liu, Ensemble Learning-based Traffic
ability of the scheme and expand its potential for larger-scale and more Classification with Small-Scale Datasets for Wireless Networks, in: IEEE INFOCOM
complex application scenarios. 2024-IEEE Conference on Computer Communications Workshops (INFOCOM WK-
SHPS), IEEE, 2024, pp. 1–6.
[24] X. Wang, W. Wei, C. Liu, X. Zhang, W. Lu, Y. Zhong, Network Traffic Classification
CRediT authorship contribution statement with Small-Scale Datasets Using Ensemble Learning, in: ICC 2024-IEEE International
Conference on Communications, IEEE, 2024, pp. 1–6.
Hao She: Writing – review & editing; Lixing Yan: Writing – original [25] Y
fo
.
r
S .
I
K
n
.
t e
M
rn
a
e
n
t
j u
o
n
f
a
T
t
h
h
i
,
n
S
g
.
s
Z
N
h
e
a
t
o
w
,
o
X
r
.
k
-P
T
.
r
Z
a
h
ffi
an
c
g
C
,
l
L
a
.
s
Z
si
h
fi
a
c
o
a
,
t i
T
o
i
n
m
,
e
IE
-D
E
i
E
s t
T
ri
r
b
a
u
n
t
s
e
a
d
c t
F
io
ea
n
t
s
u
o
r
n
e L
N
e
e
a
t
r
w
n
o
in
rk
g
draft; Xin An: Writing – review & editing; Chuanfeng Mao: Writing – and Service Management (2024).
review & editing; Yongan Guo: Funding acquisition. [26] M. Farhan, N. Shah, L. Wang, G.-M. Muntean, H.H. Song, RDG-TE: Link reliability-
aware DRL-GNN-based traffic engineering in SDN, Expert Systems with Applications
265 (2025) 125963.
Data availability [27] T.-N. Tran, T.-V. Nguyen, K. Shim, D.B. da Costa, B. An, A Deep Reinforcement
Learning-Based QoS Routing Protocol Exploiting Cross-Layer Design in Cognitive
The authors are unable or have chosen not to specify which data has Radio Mobile Ad Hoc Networks, IEEE Transactions on Vehicular Technology 71
been used. (12) (2022) 13165–13181.
[28] D.A. Menasce, QoS issues in web services, IEEE internet computing 6 (6) (2002)
72–75.
Declaration of competing interest [29] Y. Xie, M. Jin, Z. Zou, G. Xu, D. Feng, W. Liu, D. Long, Real-Time Prediction of
Docker Container Resource Load Based on a Hybrid Model of ARIMA and Triple
Exponential Smoothing 10 (2022) 1386–1401.
No potential conflict of interest was reported by the authors.
[30] Y. Qiao, C. Li, S. Hao, J. Wu, L. Zhang, Deep or statistical: an empirical study of traffic
predictions on multiple time scales, in: Proceedings of the SIGCOMM’22 Poster and
References Demo Sessions, 2022, pp. 10–12.
[31] Y.-C. Jin, Q. Cao, Q. Sun, Y. Lin, D.-M. Liu, C.-X. Wang, X.-L. Wang, X.-Y. Wang, et al.,
[1] X. Huang, M. Zeng, K. Xie, Intelligent Traffic Control For Qos Optimization In Hybrid Models for COVID-19 data prediction based on improved LSTM-ARIMA algorithms,
Sdns 189 (2021) 107877. IEEE Access (2023).
[2] W. Sun, Z. Wang, G. Zhang, A QoS-guaranteed intelligent routing mechanism in [32] Y. Miao, X. Bai, Y. Cao, Y. Liu, F. Dai, F. Wang, L. Qi, W. Dou, A novel
software-defined networks, Computer Networks 185 (2021) 107709. https://doi. short-term traffic prediction model based on SVD and ARIMA with blockchain
org/10.1016/j.comnet.2020.107709 in industrial internet of Things, IEEE Internet of Things Journal 10 (24) (2023)
[3] Z. Guo, Y. Shen, S. Wan, W.-L. Shang, K. Yu, Hybrid Intelligence-Driven Medical 21217–21226.
Image Recognition for Remote Patient Diagnosis in Internet of Medical Things, IEEE [33] M.Y. Hassan, Applications of Bigdata Technologies in the Comparison of BMTD
Journal of Biomedical and Health Informatics 26 (12) (2022) 5817–5828. https: and ARIMA Models for the Prediction of Internet Congestion, IEEE Access
//doi.org/10.1109/JBHI.2021.3139541 (2024).
[4] A. Cooper, The inmates are running the asylum, Springer, 1999. [34] P. Tang, Y. Dong, J. Jin, S. Mao, Fine-grained classification of internet video traffic
[5] J. An, H. Kwak, S. Jung, J. Salminen, M. Admad, B. Jansen, Imaginary People Rep- from QoS perspective using fractal spectrum, IEEE Transactions on Multimedia 22
resenting Real Numbers: Generating Personas from Online Social Media Data, ACM (10) (2019) 2579–2596.
Trans. Web 12 (4) (2018). https://doi.org/10.1145/3265986 [35] S. Haytamy, F. Omara, Enhanced qos-based service composition approach in multi-
[6] M.U. Farrukh, R. Wainwright, K. Crockett, D. McLean, N. Dagnall, Building Action- cloud environment, in: 2020 International Conference on Innovative Trends in Com-
able Personas Using Machine Learning Techniques, in: 2022 IEEE Symposium Series munication and Computer Engineering (ITCE), IEEE, 2020, pp. 33–38.
on Computational Intelligence (SSCI), IEEE, 2022, pp. 463–472. [36] L. Yang, J. Liu, C. Pan, Q. Zou, D. Wei, MQRP: QoS attribute decision optimization
[7] Y. Luo, P. Liu, E.K. Choe, Co-Designing Food Trackers with Dietitians - Identifying for satellite network routing, in: 2018 IEEE International Conference on Networking,
Design Opportunities for Food Tracker Customization (2019) 592–13. Architecture and Storage (NAS), IEEE, 2018, pp. 1–8.
[8] L. Wang, L. Li, H. Cai, L. Xu, B. Xu, L. Jiang, Analysis of regional group health persona [37] F. Hu, M. Zhou, P. Yan, D. Li, W. Lai, K. Bian, R. Dai, Identification of
based on image recognition, in: 2018 Sixth International Conference on Enterprise mine water inrush using laser-induced fluorescence spectroscopy combined with
Systems (ES), IEEE, 2018, pp. 166–171. one-dimensional convolutional neural network, RSC advances 9 (14) (2019)
[9] J. Salminen, S.-G. Jung, S. Chowdhury, D.R. Robillos, B. Jansen, The ability of per- 7673–7679.
sonas: An empirical evaluation of altering incorrect preconceptions about users 153 [38] G.E. Hinton, N. Srivastava, A. Krizhevsky, I. Sutskever, R.R. Salakhutdinov, Improv-
(2021) 102645. ing neural networks by preventing co-adaptation of feature detectors,(2012). arXiv
[10] P. Ngantcha, M.T. Amith, K. Roberts, J.A. Valenza, M. Walji, C. Tao, Dental EHR- preprint arXiv:1207.0580.
infused Persona Ontologies to Enrich Dental Dialogue Interaction of Agents 2021 [39] Z.-H. Zhan, J. Zhang, Y. Li, H.S.-H. Chung, Adaptive particle swarm optimization,
(2021) 1818–1825. IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics) 39 (6)
[11] Y. Cao, W. Bi, M. Fang, S. Shi, D. Tao, A Model-Agnostic Data Manipulation Method (2009) 1362–1381.
for Persona-based Dialogue Generation Proceedings of the 60th Annual Meeting [40] Y.-Y. Zhang, J. Luo, Y. He, S. Ma, K. Liang, Z. Liu, Smart Meter Intrusion Detection
of the Association for Computational Linguistics (Volume 1: Long Papers) (2022) Based on APSO-DBN Model, in: 2021 Smart City Challenges & Outcomes for Urban
7984–8002. Transformation (SCOUT), IEEE, 2021, pp. 214–217.
14

H. She et al. Computer Networks 273 (2025) 111784
[41] A. Lu, L. Yu, L. Tan, Apso-based optimization algorithm of lstm neural network [46] H. Hajizadeh, M. Nabi, K. Goossens, Decentralized configuration of TSCH-based IoT
model, in: 2021 IEEE 5th Advanced Information Technology, Electronic and Au- networks for distinctive QoS: A deep reinforcement learning approach, IEEE Internet
tomation Control Conference (IAEAC), 5, IEEE, 2021, pp. 2194–2200. of Things Journal 10 (19) (2023) 16869–16880.
[42] X. Kan, Y. Fan, Z. Fang, L. Cao, N.N. Xiong, D. Yang, X. Li, A novel IoT network [47] F. Li, Q. Yuan, T. Pan, X. Wang, J. Cao, MTU-Adaptive In-Band Network-Wide
intrusion detection approach based on adaptive particle swarm optimization convo- Telemetry, IEEE/ACM Transactions on Networking (2024).
lutional neural network, Information Sciences 568 (2021) 147–162. [48] A.C. Wilson, R. Roelofs, M. Stern, N. Srebro, B. Recht, The marginal value of adaptive
[43] S. Liu, C. Guo, Retracted: The Simulation Research on Random Disturbance in Multi- gradient methods in machine learning, Advances in neural information processing
Hop Wireless Network, in: 2018 3rd International Conference on Smart City and systems 30 (2017).
Systems Engineering (ICSCSE), IEEE, 2018, pp. 655–659. [49] N.S. Keskar, R. Socher, Improving generalization performance by switching from
[44] Y. Fu, X. Wang, F. Fang, Multi-Objective Multi-Dimensional Resource Allocation for adam to sgd,(2017). arXiv preprint arXiv:1712.07628.
Categorized QoS Provisioning in Beyond 5G and 6G Radio Access Networks, IEEE [50] D.H. Wolpert, W.G. Macready, No free lunch theorems for optimization, IEEE trans-
Transactions on Communications (2023). actions on evolutionary computation 1 (1) (1997) 67–82.
[45] Y. Gao, C. Lu, Y. Lian, X. Li, G. Chen, D.B. da Costa, A. Nallanathan, QoS-Aware
Resource Allocation of RIS-Aided Multi-User MISO Wireless Communications, IEEE
Transactions on Vehicular Technology (2023).
15