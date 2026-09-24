# [22] Intelligent Requests Orchestration for Microservice Management Based on Blockchain in SDN A Security Guarantee

> Source file: `[22] Intelligent Requests Orchestration for Microservice Management Based on Blockchain in SDN A Security Guarantee.pdf`

---

WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
Intelligent Requests Orchestration for Microservice
Management Based on Blockchain in Software
Defined Networking: a Security Guarantee
1st Yasheng Zhang 3rd Ning Chen*
2nd Chengcheng Li 4th Peiying Zhang
The 54th Research Institute of CETC College of Computer Science and Technology
Shijiazhuang 050081, China China University of Petroleum (East China)
zys163@163.com, lengcangche@bupt.cn Qingdao 266580, China
nchen@s.upc.edu.cn, zhangpeiying@upc.edu.cn
Abstract—Throughtheprogrammablecontrolofthenetwork,
Data Forwarding Plane
the distributed and discrete service equipment is managed
Entity or Service
uniformly, and the software-defined network (SDN) effectively (Hardware or
improves the overall management and control capabilities of the Software)
centralized management model. Each service node in SDN is M D es a s t a a g e start
connected by the service function chain (SFC) and completes Service Function
Chain (SFC) A service path networkservicesinaspecifiedorder.However,therearestillthe end
following challenges in service request orchestration of SDN: (1)
(2)
The tightly coupled characteristic of SFC bring management
problems, e.g., deployment difficulties, service collisions, and Control Plane
poor scalability, etc., to frequent user service requests. (2) The user Service Service
(1)
complicated technologies in SDN, e.g., interference of wireless Requests Orchestration
communication, cause potential safety hazards between service user Controller (3)
nodes, which may cause devastating effects on the controller.
(4) logical abstraction
Correspondingly, we propose the following solutions: (1) Mean-
Microservice Management
ingfully transform the service request orchestration in SDN into Micro Service (MS)
the Microservice Management problem, and further combine Service Invocation
Artificial Intelligence (AI) technology to provide a flexible,
Chain 1 (SIC1)
SIC2 SIC3
autonomous,andscalableintelligentserviceorchestrationmodel.
SIC4
(2) Combine the Diffie-Hellman algorithm to establish a shared
keyforthecommunicationnode,andcombinethecharacteristics
Fig.1. ServicerequestsorchestrationformicroservicemanagementinSDN.
of the distributed ledger in the consortium blockchain, e.g., The specific flow is: (1) Users send service requests; (2) The controller
immutable,privacy,credibility,andhighsecurity,etc.,foridentity logicallyabstractsentitiesinthedataforwardinglayerplane;(3)Serviceor-
authenticationtofurtherimprovethesecurityofthesharedkey. chestrationthroughmicroservicemanagement;(4)Respondtousersrequests.
Eventually, we have proved through theory and practice that
the proposed algorithm can provide efficient intelligent request
orchestration extremely safely in SDN. management and control capabilities through this centralized
Index Terms—Software Defined Networking (SDN), Service
management pattern [4].
Function Chain (SFC), Microservice Management, Blockchain,
Request Orchestration, Artificial Intelligence (AI) As shown in Fig. 1, the realization of services in SDN
requires data messages to run in the order specified by the
I. INTRODUCTION business logic in the network entities. The communication
link between different network entities is called the Service
In recent years, as emerging network technology, Software
FunctionChain(SFC),whichconstitutestheimportantservice
DefinedNetworking(SDN)hasattractedwidespreadattention
function.Specifically,SFCprovidesthefunctionofdefiningan
in the industry [1], [2]. It separates the control plane from
orderedlistofnetworkservices,whichareorganizedtocreate
the data forwarding plane and improves the programmability
a service path [5]. When a data message enters the service
control of the network [3]. Specifically, it uniformly manages
path, it will flow through each service node (entity) according
distributed and discrete hardware and software devices, e.g.,
to the predetermined order of SFC, and then forward to the
Internet of Things (IoT) devices, Servers, Load Balance (LB),
next node, finally encapsulate and forward at the last node to
IntrusionDetectionSystem(IDS),IntrusionPreventionSystem
complete the specified network service [6]. We can find that
(IPS),etc.Therefore,SDNcaneffectivelyimprovetheoverall
SFC in SDN has the characteristic of tight coupling. When it
*Correspondingauthors:NingChen isexpandedorchanged,itisnecessarytomakecomplexmod-
978-1-6654-2671-8/22/$31.00 ©2022 IEEE 254
6354189.2202.86435SPOHSKROWCCI/9011.01
:IOD
| EEEI
2202©
00.13$/22/8-1762-4566-1-879
|
)spohskroW
CCI(
spohskroW
snoitacinummoC
no
ecnerefnoC
lanoitanretnI
EEEI
2202
Authorized licensed use limited to: Biruni Universitesi. Downloaded on November 10,2022 at 07:47:09 UTC from IEEE Xplore. Restrictions apply.

WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
ifications to the topology, and frequent manual programming thentication, so that the communication process cannot
control is unrealistic. Therefore, in response to user requests, be tampered with and has high reliability and credibility.
howtoorganizeautonomousandextensibleintelligentservice • Through simulation to simulate the real environment for
request orchestration is a meaningful issue. Through logical experiments, satisfactory results have been obtained in
abstraction, microservice management can provide flexible long-term average revenue, acceptance rate, and long-
and intelligent service orchestration [7]. It resolves the prob- term revenue-cost ratio. Eventually, the effectiveness of
lems of poor scalability, deployment difficulties, and bloated the proposed algorithm is proved through theory and
| services | in the        | monolithic |             | system | by decomposing |     | related   | practice. |     |            |              |     |             |     |         |
| -------- | ------------- | ---------- | ----------- | ------ | -------------- | --- | --------- | --------- | --- | ---------- | ------------ | --- | ----------- | --- | ------- |
| entities | into mutually |            | independent |        | microservice   |     | (MS), and |           |     |            |              |     |             |     |         |
|          |               |            |             |        |                |     |           | The rest  | of  | this paper | is organized |     | as follows: | In  | Section |
implementing specified services through logical calls between II, the related work is briefly described; In Section III, the
| MS. It | has a | similar | structure | and | functional | characteristics |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ------- | --------- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
definitionoftheproblemandthedetailsoftheproposedalgo-
as SFC, so inspired by it, to solve the above problems, we rithmareelaborated;InSectionIV,toprovetheeffectiveness,
employ microservice management for SFC intelligent request simulationexperimentsarecarriedout;InSectionV,thework
orchestration.
done is summarized.
| Moreover, | there | are | many | types | of SDN | technologies. | For |     |     |     |     |     |     |     |     |
| --------- | ----- | --- | ---- | ----- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
example, SDN is implemented by different software (e.g. II. RELATEDWORK
Dragonflow,Midonet,etc.),thecontrolplanealsohasdifferent
|            |              |     |       |              |     |              |         | A. Software | Defined | Networking |     |     |     |     |     |
| ---------- | ------------ | --- | ----- | ------------ | --- | ------------ | ------- | ----------- | ------- | ---------- | --- | --- | --- | --- | --- |
| processing | technologies |     | (e.g. | centralized, |     | distributed, | active, |             |         |            |     |     |     |     |     |
hybrid, etc.). To provide reliable links, these technologies Compared with the scattered functions of the traditional IP
network,SDNadoptscentralizedprogrammablemanagement,
commonlyutilizesecurecommunicationprotocolsforsecurity
|     |     |     |     |     |     |     |     | which significantly |     | improves |     | the scalability |     | and flexibility | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | --- | --------------- | --- | --------------- | --- |
control,e.g.OpenFlow.However,thisapproachstillhaspoten-
tialsafetyhazardsduringthecontrolgap.Inaddition,withthe the network. Works [2], [12] have re-examined and defined
|     |     |     |     |     |     |     |     | the SDN | architecture. |     | Due to | it can | realize | network | inter- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------ | ------ | ------- | ------- | ------ |
developmentofwirelesstechnology,communicationsbetween
different devices frequently interfere. Therefore, security in connection under the cooperation of the control layer, and
|        |          |           |       |     |             |     |               | dynamically | configure |         | and optimize |           | network     | resources, | it is     |
| ------ | -------- | --------- | ----- | --- | ----------- | --- | ------------- | ----------- | --------- | ------- | ------------ | --------- | ----------- | ---------- | --------- |
| SDN is | still an | essential | issue | to  | be resolved |     | [8], [9]. The |             |           |         |              |           |             |            |           |
|        |          |           |       |     |             |     |               | widely used | in        | various | fields       | [4], such | as Internet |            | of Things |
emergenceofBitcoinbasedonadistributed,decentralized,and
trustedsystemmarkedthebeginningandsuccessofblockchain (IoT) [13], Vehicle-to-Grid (V2G) [14], Internet of Vehicles
|             |             |     |     |               |        |     |               | (IoV) [3], | etc. |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | ------------- | ------ | --- | ------------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| technology. | Blockchain, |     | as  | a distributed | ledger |     | (system), has |            |      |     |     |     |     |     |     |
thecharacteristicsofdecentralization,autonomy,immutability,
|          |     |              |           |     |     |          |          | B. Microservice |     | Management |     |     |     |     |     |
| -------- | --- | ------------ | --------- | --- | --- | -------- | -------- | --------------- | --- | ---------- | --- | --- | --- | --- | --- |
| accuracy | and | credibility, | anonymity |     | and | privacy, | and high |                 |     |            |     |     |     |     |     |
security, etc, [10] and is widely used in security management Microservice architecture is the mainstream method in the
issues in non-secure environments [1], [8], [11]. In addition, softwareindustry.Itperformsvitalbusinessfunctionsthrough
highlycohesive,lightweight,andsmallservices,whichsignif-
| according | to different |     | consensus | algorithms, |     | blockchains | can |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
also be divided into public chains, consortium chains, and icantly improves the flexibility and scalability of the network
private chains. According to the characteristics of microser- [7]. Hannousse et al. [5] have further reviewed the mapping
vices in SDN, the selected blockchain technology should be mechanism of the microservice system on the basis of Vale
aslightweightaspossible,lowcost,fastprocessingspeed,high et al. [15], and focused on the security issues. Fu et al.
|           |              |     |                |     |       |     |               | [16] have | applied | microservices |     | to  | Cloud-Edge | Continuum |     |
| --------- | ------------ | --- | -------------- | --- | ----- | --- | ------------- | --------- | ------- | ------------- | --- | --- | ---------- | --------- | --- |
| security, | and privacy. |     | The consortium |     | chain | can | suitably meet |           |         |               |     |     |            |           |     |
our expectations, so we employ it for the security deployment to adaptively and efficiently deploy microservices, effectively
of microservice management to improve the security and reducingresourceloss.Inshort,microservicemanagementhas
privacy of user’s request orchestration. been widely used due to its high flexibility.
| Inspired | by            | theabove, | we               | have | proposed   | anovel | intelligent |               |     |     |     |     |     |     |     |
| -------- | ------------- | --------- | ---------------- | ---- | ---------- | ------ | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| requests | orchestration |           | for microservice |      | management |        | based on    | C. Blockchain |     |     |     |     |     |     |     |
blockchain.Inparticular,thecontributionsofthisresearchare Blockchain technology is widely used in various fields due
summarized as: to its privacy and transparency [11]. Singh et al. [8] have
• Aimingatthedeploymentdifficulties,servicecongestion, proposed to use the blockchain to create smart contracts to
and poor scalability in service requests orchestration establish trust between both parties to the transaction and
caused by frequent user requirements, we convert it provideasecurecommunicationframeworkforretailissuesin
intomicroservicemanagementproblemsandcombineAI theCOVID-19scenario.IntheissueofSDNsecurity,Aujlaet
technology to further provide flexible, autonomous, and al. [1] have proposed BlockSDN to deal with insecure factors
scalable intelligent services orchestration. such as man-in-the-middle attacks and applied it to smart
Aiming at the security and privacy issues of communica- cities. However, security issues in SDN are still the focus of
•
|      |         |               |     |     |      |         |          | continuous | attention. |     |     |     |     |     |     |
| ---- | ------- | ------------- | --- | --- | ---- | ------- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| tion | between | microservices |     | in  | SDN, | we have | combined |            |            |     |     |     |     |     |     |
the Diffie-Hellman algorithm to establish a symmetric Aiming at the problems of deployment difficulties, service
shared key for the communication nodes, and combined congestion, and poor service communication security that still
with the consortium blockchain for identity access au- exist in service request orchestration in SDN, we provide
Authorized licensed use limited to: Biruni Universitesi. Downloaded on2 N5ov5ember 10,2022 at 07:47:09 UTC from IEEE Xplore.  Restrictions apply.

WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
TABLEI where |U| represents the number of user requests.
THENOTATIONSOFMICROSERVICEMANAGEMENTANDUSERREQUESTS (2) Available resources of SICM: For sicM, its resources
k
should be sufficient to assign to sicU in all user requests that
Model Notation Definition j
MSM Thesetofmicroservices, can be satisfied, specifically denoted as:
correspondingtonodesinSDN
Microservice SICM Thesetofserviceinvocationchians, |U|
Management correspondingtoSFCinSDN RESM(cid:0) sicM(cid:1)
−
XX RESU(cid:0) sicU(cid:1)
≥0.
(M)inSDN LOCM Thelocationofmicroservices k ∀(sicM→sicU) j
DELM ThedelayofSICM inSDN j=1 k j
REMM TheresourcesofMSM inSDN (2)
RESM TheresourcesofSICM inSDN (3) Delay limits of SICM: For sicM, its delay should be
MSU Thesetofrequiredmicroservices k
SICU Thesetofrequiredserviceinvocationchians greaterthanthedelayofallSICsassignedtosicU j ,specifically
Userrequest LOCU Thelocationofrequiredmicroservices denoted as:
(U) DELU ThedelayofSICU
REMU TheresourcesofMSU DELM(cid:0) sicM(cid:1)
≥max
n DELU(cid:0) sicU(cid:1)o
RESU TheresourcesofSICU k j
(3)
s.t. ∀ (cid:0) sicM →sicU(cid:1) ,1≤j ≤|U|.
k j
flexible and intelligent orchestration strategies based on mi- C. Diffie–Hellman to Establish the Symmetric Key
croservice management, and combine blockchain technology
to improve communication reliability and security between The Diffie–Hellman confidentiality protocol can enable two
microservices. parties in communication to exchange keys securely in an
insecure channel, so it is used to encrypt communication
III. PROBLEMDEFINITIONANDTHEPROPOSED information. For example, for the requested microservices
ALGORITHM ms and ms , the shared key needs to be established for
1 2
A. Notation them to ensure the security of their information transmission.
Specifically, the key exchange steps are:
Table I records the definition notations used in this work.
(1)Randomlygeneratetwoprimenumberspandg,whereg
It should be noted that the resources of MS and SIC can have
is the primitive root of p and satisfies the following equation:
multiple forms, e.g., CPU, bandwidth, etc. In this work, we
use a unified form of representation. In fact, it can be easily
gi mod p=i, s.t. ∀ i∈[1,p−1], (4)
extended to multiple resource problems. Moreover, lowercase
lettersareusedtodenotespecificelements,e.g.sicM indicates
k where mod is the remainder operator.
the k-th chain in M. If msM and msM are the start and end
i j (2)ms randomlygeneratesandsavesitsprivatekeya,and
nodes of sicm, respectively, they can also be expressed as 1
k ms randomly generates and saves its private key b.
msM −msM. 2
i j (3) ms calculates its public key K and sends it to ms .
DifferentMSU andSICU cancoexistonthesameMSM 1 1 2
and SICM respectively, which originates from frequent user
K =ga mod p. (5)
requests. Therefore, the problem we studied can be summa- 1
rized as: how to consume the least resources to meet the user
(4) ms calculates its public key K and sends it to ms .
requests as many as possible under the premise of limited 2 2 1
resourcesinM.ItcanbeknownthatitisanNP-hardproblem K =gb mod p. (6)
2
[17]. Meanwhile, how to ensure information such as service
resources are not attacked and tampered with, i.e., access
(5) ms calculates and obtains the symmetric key K .
1 12
security is also an important dispute.
K =Ka mod p. (7)
B. Orchestration Constraints 12 2
In the request orchestration process, the corresponding re-
(6) ms calculates and obtains the symmetric key K .
2 21
sources are allocated to U. Part of the resources in M is
occupied by different U, and this part of resources is not K =Kb mod p. (8)
21 1
released until the service of U ends. In the orchestration
process, the following constraints should be fulfilled: where K = K . It should be noted that a, b, and p must
12 21
(1) Available resources of MSM: For msM i , its resources be very large, otherwise, the key can easily be exhaustively
should be sufficient to assign to msU j in all user requests that enumerated. g usually takes a small value, and an empirical
can be satisfied, specifically denoted as: value of 5 is set in this work. Take SIC as an example,
3
the shared symmetric key construction process between mi-
|U|
REMM(cid:0) msM(cid:1) − XX REMU(cid:0) msU(cid:1) ≥0, croservicesisshowninFig.2.Duringtherequestorchestration
i ∀(msM→msU) j process, the microservices must have the same symmetric key
j=1 i j
(1) to communicate.
Authorized licensed use limited to: Biruni Universitesi. Downloaded on2 N5ov6ember 10,2022 at 07:47:09 UTC from IEEE Xplore. Restrictions apply.

ms 1 ms 2 ms 3 Consortium Blockchain
SIC 3 Block 1 Block 2 Block 3 ... Block n
g, p, a 5, 97, 36
g, p, b 5, 97, 58 g, p, c
K
1
=ga mod p 536mod97=50
K
1
K 2 =gb mod p 558mod97=44
K K
2 2
K =Ka mod p K =Kb mod p
12 2 21 1 K=gc mod p 3
4436mod97=75 5058mod97=75
K
3
K =Kb mod p K =Kc mod p
23 3 32 2
Symmetric Key Symmetric Key
K12 = K21=75 K23 = K32
Fig. 2. The process of symmetric key construction between microservices,
wherethetextinbluefontisanactualexample
D. Consortium Blockchain for Identity Authentication
However, the lack of identity authentication between the
communicating parties makes it vulnerable to man-in-the-
middleattacks.Therefore,wecombinetheblockchaintechnol-
ogytojointheidentityauthenticationmechanismtostrengthen
the security and privacy of the key exchange technology, and
apply it to the SDN microservice management.
Correspondingly, each ms needs to register and record
information in the consortium blockchain ledger, including
prime number g, primitive root p, and its own public key K .
∗ After registration, key exchanges can be carried out. Mean-
while, both parties need to perform access authentication and
create the symmetric share key. The records of key exchange
will be recorded in the ledger and maintained by each node.
Assuming that ms needs to communicate with ms , the
1 2
key exchange process of introduced access authentication is
illustrated in Fig. 3. The specific description is as follows:
(1) ms generates the session (including the address of the
1
sender,addressofthereceiver,primenumberp,primitiveroot
g, public key K , private key signature a) and broadcasts it
1
through the broadcast mechanism.
(2)ms actsasaminernodetoverifythesender’ssignature 2
in the session is correct and credible, the session will be
packaged into a block and added to the blockchain.
(3) Through the broadcast mechanism, ms obtains the 2
session information of ms that wants to communicate with 1
it. And query the information of ms stored in the ledger at 1
the registration stage. If the verification is inconsistent, the
communication is rejected; after the verification is consistent,
the Diffie-Hellman algorithm can be used to establish the
Symmetric Key according to Section III-C.
(4) ms creates the session, where the receiver is ms , and
2 1
the prime number and primitive root are obtained from the
...
(1)
Generate Session
Broadcast ms1
(1)
tsacdaorB ms2
S
O
e
b
ss
ta
io
in
n
Generate Session
Correct and Verify Session Credible?
Reject Communication (end)
Package
and
Add
y
ddA
dna
egakcaP
Obtain (5) (2)
Session
(4)
(5) (2) (4)
(5) (2)
Verify Session
y n y
(6) (3)
Verify Registration Verify Registration
y(6) n (2) n (3)y
Diffie-Hellman Diffie-Hellman
to Establish (6) (3) to Establish
Symmetric Key Symmetric Key
(6) (3)
End of key exchange through the consortium blockchain
Anothor
Microservice
msn
Fig.3. Theprocessofstrengtheningthesecurityandprivacyofkeyexchange
technology through the consortium blockchain for identity authentication. It
shouldbenotedthattheconsortiumblockchainissharedbyallMSinSDN.
session information in the ms block obtained in (3). Then
1
broadcast the session, the process is similar to (1).
(5)ms actasaminernodeandperformtheprocesssimilar
1
to (2) and (3).
E. Request Orchestration
LLaayyeerr
CCoonnvvoolluuttiioonnaall
LLaayyeerr
PPrroobbaabbiilliittyy FFiilltteerr
LLaayyeerr
MSM
... ...
msn
Sort
by probability
in descending
order
WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
Fig.4. Thestructureoforchestrationnetwork.Threelayers:(1)Convolutional
layer;(2)Probabilitylayer;(3)Filterlayer.
To provide autonomous and scalable smart service request
orchestration, we have designed an orchestration network,
which is mainly composed of a three-layer architecture and
manifested in Fig. 4. Specifically, the convolutional layer is
utilizedtoextractthelocalspatialfeaturesofMSM toobtain
resource vectors. The probability layer employs the softmax
function to calculate the probability of MSM being orches-
trated according to the available resources. The filtering layer
filters out the microservices that do not meet the constraints
describedinSectionIII-Bandsortsthemindescendingorder.
Finally, breadth-first search is used to orchestrate SICM.
In addition, when orchestration the SICs, we first need to
use the proposed consortium blockchain technology to add an
identity authentication mechanism for both parties to enhance
the security and privacy of the key exchange technology.
Second,thesymmetrickeyiscreatedfortheendmicroservices
Authorized licensed use limited to: Biruni Universitesi. Downloaded on2 N5ov7ember 10,2022 at 07:47:09 UTC from IEEE Xplore. Restrictions apply.

WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
oftheSICthroughtheDiffie-Hellmanalgorithm.Ifanyofthe TABLEII
processinformationinthemiddlefailstopasstheverification, THEDETAILEDCONFIGURATIONOFTHESIMULATIONENVIRONMENT
the communication will be rejected, i.e., this service request
Model SimulationEnviroment Configuration
orchestrationwillfail.Althoughitwillreducethesuccessrate DELM 1ms-60ms
of request orchestration to a certain extent, it fully guarantees M REMM 20TFLOPS-100TFLOPS
the security and reliability of the orchestration. RESM 50Mbps-100Mbps
DELU 1ms-50ms
F. Evaluation indicators U REMU 1TFLOPS-20TFLOPS
REMU 1Mbs-20Mbs
Specifically,thefollowingindicatorsareutilizedtoevaluate
the resource consumption:
(1) Cos: the cost of the additional resources consumed TABLEIII
AVERAGEPERFORMANCE
for service orchestration. Therefore, it is not only related
to REMU but also to RESU. In addition, the longer the RevL Acc RevL/CosL
SICU is requested, i.e. the greater the number of hops, the 1ms≤DELU ≤50ms 1720.8301 0.811 0.3392
1ms≤DELU ≤40ms 1586.1305 0.779 0.3288
higher the cost.
1ms≤DELU ≤30ms 1505.3366 0.714 0.3447
Cos(M →U)= X REMU(cid:0) msU(cid:1) 1ms≤DELU ≤20ms 1116.8953 0.579 0.3511
msU∈MSU
(9)
+
X hops(sicU)×RESU(cid:0) sicU(cid:1)
.
sicU∈SICU B. Performance
(2) Rev: the resources that successfully response to user
Through Fig. 5, we can find that the orchestration network
requests, i.e. revenue.
converges quickly with the iterative process. And we observe
Rev(M →U)=
X REMU(cid:0) msU(cid:1) the performance by limiting the upper limit of DELU to
msU∈MSU (10) 20ms,30ms,40ms,and50msinsequence.Astheupperlimitis
+
X RESU(cid:0) sicU(cid:1)
. decreased,thenumberofuserrequeststhatcanbesuccessfully
sicU∈SICU
scheduled is reduced consequently, and the corresponding
Accordingly, the following indicators is employed to eval-
Rev and Acc are gradually reduced. Since Rev /Cos is
L L L
uate the performance of the algorithm we proposed:
also related to Cos , its fluctuation is slight. The results in
L
(1)Long-termAverageRevenue:theintegralofrevenueover
Table III also confirm the correctness of our theoretical anal-
time.
ysis. Moreover, as time goes by, allocable resources decrease,
PT
Rev (M →U)
and the three indicators should show the same trend as above.
Rev = lim t=0 t . (11) The results are manifested in Fig. 6 also excellently prove
L T→+∞ T this process. Therefore, our proposed orchestration network
(2) Acceptance Ratio: the percentage of successfully re- can converge quickly, and its training and testing phases are
sponded requests U acc to all user requests U. alsoeffectiveandcanorchestratemicroservicestouserssafely
and efficiently.
PT
U
Acc= lim t=0 acct. (12)
T→+∞
PT
U
V. CONCLUSION
t=0 t
Inthiswork,weproposeanovelintelligentrequestsorches-
(3) Long-term Revenue-Cost Ratio: The less resource loss,
tration for microservice management based on blockchain in
thebetterthealgorithmperformance,sotheratiooflong-term
SDN. It provides a flexible and scalable intelligent service
revenue to long-term cost is used for evaluation.
orchestration model for SDN through the combination of
PT Rev (M →U) microservice management technology and AI technology. In
Rev /Cos = lim t=0 t . (13)
L L
T→+∞
PT
Cos (M →U)
addition, the Diffie-Hellman algorithm is combined to es-
t=0 t tablish a shared symmetric key between microservices. And
IV. EXPERIMENT combined with the consortium blockchain to perform identity
In this section, we conduct simulation experiments to eval- accessauthenticationforcommunicationmicroservices,sothat
uate the effectiveness of the proposed algorithm. the communication process has reliable security. In the end,
theeffectivenessoftheproposedalgorithmisprovedfromthe
A. Simulation Enviroment
perspective of theory and practice.
100 microservices and 581 SFCs are randomly generated.
Randomlygenerate2000userrequestsU,thefirst1000asthe
VI. ACKNOWLEDGEMENTS
training set, and the remainder as the testing set. In addition, This work is partially supported by the Shandong
computing power is taken as an example to represent REM, Provincial Natural Science Foundation, China under Grant
and bandwidth is taken as an example to represent RES. ZR2020MF006, and partially supported by the Major Sci-
The detailed configuration of the simulation environment is entific and Technological Projects of CNPC under Grant
recorded in Table II. ZD2019-183-006.
Authorized licensed use limited to: Biruni Universitesi. Downloaded on2 N5ov8ember 10,2022 at 07:47:09 UTC from IEEE Xplore. Restrictions apply.

1700
1600
1500
1400 0 50 100 150 200
LveR
0.82
0.80
0.78
0.76
RevL
0.74
0 50 100 150 200
epoch
(a)
ccA
0.425
0.400
0.375
0.350
Acc 0.325
0 50 100 150 200
epoch
(b)
LsoC/LveR
RevL/CosL
epoch
(c)
Fig.5. ThevariationofRevL,AccandRevL/CosL,withtheiterativetrainingprocess.
2500
2000
1500
1000
0 10 20 30
LveR
0.9
1ms <= DV <= 50ms 1ms <= DV <= 40ms 1ms <= DV <= 30ms 1ms <= DV <= 20ms
0.8
0.7
0.6
0.5
0 10 20 30
time(×1000s)
(a)
ccA
0.5
1ms <= DV <= 50ms 1ms <= DV <= 40ms 0.4
1ms <= DV <= 30ms 1ms <= DV <= 20ms
0.3
0 10 20 30
time(×1000s)
(b)
LsoC/LveR
WS21 IEEE ICC 2022 Workshop on Blockchain for Secure Software-defined Networking in Smart Communities
1ms <= DV <= 50ms 1ms <= DV <= 40ms 1ms <= DV <= 30ms 1ms <= DV <= 20ms
time(×1000s)
(c)
Fig.6. ThevariationofRevL,AccandRevL/CosL,withtheiterativetrainingprocess.
REFERENCES [10] W.Sun,L.Wang,P.Wang,andY.Zhang,“Collaborativeblockchainfor
space-air-groundintegratednetworks,”IEEEWirelessCommunications,
vol.27,no.6,pp.82–89,2020.
[1] G. S. Aujla, M. Singh, A. Bose, N. Kumar, G. Han, and R. Buyya, [11] D. Berdik, S. Otoum, N. Schmidt, D. Porter, and Y. Jararweh, “A
“Blocksdn:Blockchain-as-a-serviceforsoftwaredefinednetworkingin surveyonblockchainforinformationsystemsmanagementandsecurity,”
smartcityapplications,”IEEENetwork,vol.34,no.2,pp.83–91,2020. InformationProcessing&Management,vol.58,no.1,p.102397,2021.
[2] D.Kreutz,F.M.Ramos,P.E.Verissimo,C.E.Rothenberg,S.Azodol- [12] W. Xia, Y. Wen, C. H. Foh, D. Niyato, and H. Xie, “A survey
molky, and S. Uhlig, “Software-defined networking: A comprehensive on software-defined networking,” IEEE Communications Surveys &
survey,”ProceedingsoftheIEEE,vol.103,no.1,pp.14–76,2014. Tutorials,vol.17,no.1,pp.27–51,2014.
[3] A.Gulati,G.S.Aujla,N.Kumar,S.Garg,andG.Kaddoum,“Software- [13] X. Ren, G. S. Aujla, A. Jindal, R. S. Batth, and P. Zhang, “Adaptive
definedcontentdisseminationschemeforinternetofhealthcarevehicles recoverymechanismforsdncontrollersinedge-cloudsupportedfintech
incovid-likescenarios,”IEEEInternetofThingsMagazine,vol.4,no.3, applications,”IEEEInternetofThingsJournal,pp.1–1,2021.
pp.34–40,2021. [14] A. Jindal, G. S. Aujla, and N. Kumar, “Survivor: A blockchain based
[4] H.Cao,Y.Hu,S.Wu,J.Du,F.Tian,G.S.Aujla,andL.Yang,“Novisec: edge-as-a-service framework for secure energy trading in sdn-enabled
Novelvirtual networkmapping frameworkfor securesoftware-defined vehicle-to-gridenvironment,”ComputerNetworks,vol.153,pp.36–48,
networking,” in 2020 IEEE Wireless Communications and Networking 2019.
ConferenceWorkshops(WCNCW). IEEE,2020,pp.1–6. [15] A. Pereira-Vale, G. Ma´rquez, H. Astudillo, and E. B. Fernandez, “Se-
curity mechanisms used in microservices-based systems: A systematic
[5] A.HannousseandS.Yahiouche,“Securingmicroservicesandmicroser-
vice architectures: A systematic mapping study,” Computer Science
mapping,”in2019XLVLatinAmericanComputingConference(CLEI).
Review,vol.41,p.100415,2021. IEEE,2019,pp.01–10.
[16] K.Fu,W.Zhang,Q.Chen,D.Zeng,andM.Guo,“Adaptiveresource
[6] K. Kaur, S. Garg, G. S. Aujla, N. Kumar, J. J. Rodrigues, and
efficient microservice deployment in cloud-edge continuum,” IEEE
M.Guizani,“Edgecomputingintheindustrialinternetofthingsenvi-
Transactions on Parallel and Distributed Systems, vol. 33, no. 8, pp.
ronment:Software-defined-networks-basededge-cloudinterplay,”IEEE
1825–1840,2022.
communicationsmagazine,vol.56,no.2,pp.44–51,2018.
[17] L. Gu, D. Zeng, J. Hu, B. Li, and H. Jin, “Layer aware microservice
[7] S.Garg,K.Kaur,G.Kaddoum,P.Garigipati,andG.S.Aujla,“Security
placementandrequestschedulingattheedge,”inIEEEINFOCOM2021
in iot-driven mobile edge computing: new paradigms, challenges, and
-IEEEConferenceonComputerCommunications,2021,pp.1–9.
opportunities,”IEEENetwork,vol.35,no.5,pp.298–305,2021.
[8] M.Singh,G.S.Aujla,R.S.Bali,S.Vashisht,A.Singh,andA.Jindal,
“Blockchain-enabled secure communication for drone delivery: a case
studyincovid-likescenarios,”inProceedingsofthe2ndACMMobiCom
Workshop on Drone Assisted Wireless Communications for 5G and
beyond,2020,pp.25–30.
[9] P.Zhang,F.Liu,N.Kumar,andG.S.Aujla,“Informationclassification
strategyforblockchain-basedsecuresdniniotscenario,”inIEEEINFO-
COM2020-IEEEConferenceonComputerCommunicationsWorkshops
(INFOCOMWKSHPS). IEEE,2020,pp.1081–1086.
Authorized licensed use limited to: Biruni Universitesi. Downloaded on2 N5ov9ember 10,2022 at 07:47:09 UTC from IEEE Xplore. Restrictions apply.