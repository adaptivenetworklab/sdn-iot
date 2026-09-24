# Cross-Network-Slice Authentication Scheme for the 5th Generation Mobile Communication System

> Source file: `Cross-Network-Slice Authentication Scheme for the 5th Generation Mobile Communication System.pdf`

---

IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021 701
Cross-Network-Slice Authentication Scheme for the
th
5 Generation Mobile Communication System
Chun-I Fan , Yu-Tse Shih, Jheng-Jia Huang , and Wan-Ru Chiu
Abstract—Thefifth-generationmobilenetwork(5G)integrates I. INTRODUCTION
various application services in a heterogeneous network envi- THE FIFTH-GENERATION mobile network (5G) inher-
ronment. Compared to the traditional networks, 5G is not just
its the functionalities of network function virtualiza-
an extension of the 4th generation, which contains three impor-
tant properties, enhanced mobile broadband (eMBB), massive tion (NFV) and software-defined networking (SDN), and
machine type communications (mMTC), and ultra-reliable and it enables multiple services through the network slicing
low latency communications (URLLC). 5G applies the function- with distinctive characteristics. However, providing a guar-
alities of Network Function Virtualization and Software-Defined
antee of connecting to a correct network slice is one of
Networkingtosupportmultipleservicesandproposesanewcon-
the prime concerns. This research aims to present a novel
cept called Network Slicing. Users can access different services
quickly in the 5G network supported by network slicing. In a authenticationtechniquetailoredfor5Gthatsatisfiesthethird-
traditional network like 4G, if a user wants to access different generation partnership project (3GPP). According to the IMT-
services, it will be necessary to perform different authentication 2020projectproposedbytheInternationalTelecommunication
procedures that cause additional burden and operation cost in
Union Radiocommunication Sector (ITU-R) [1], the 5G stan-
theuser’sdevice.However,the5Gnetworkinheritstheprevious
dard was published in 2020, and the new system of 5G is
network architecture. Hence, the user’s device still needs to be
authenticated by the core network. Besides, providing a guaran- commercialized to demonstrate diversified services such as
tee of connecting to a correct network slice is one of the prime enhanced mobile broadband, ultra-high reliability, and low
concerns. The paper presents an authentication scheme tailored latency applications, massive Internet of Things (IoT), etc.
forthe5Gnetwork.Intheproposedscheme,theauthenticationis Fig. 1 depicts the scopes and requirements of the 5G network
decentralizedtotheedgecloudstoachievelowlatency.Moreover,
asdefinedbyITU-R[1].Inthe5Gnetwork,EnhancedMobile
the authentication flow is no longer attached to the operator all
Broadband provides high speed while Ultra-Reliable Low-
the time to reduce time latency. The proposed scheme is secure
against the attackers who aim to impersonate users, network Latency Communication guarantees extremely-low latency,
operators,orevennetworkslices,anditalsoprovidessecureses- and Massive Machine Type Communication assists lots of
sion key exchange. Empirical performance assessment in terms devices to connect each other.
of its functionalities gains better acceptability of the proposed
Based on the 5G Concept white paper published by IMT-
scheme than other existing ones.
2020 (5G) Promotion Group in Feb, 2015 [2], the 5G
Index Terms—Authentication, 5G, network slicing, edge com- technology development was broadly divided into four parts:
puting, low latency.
1) Seamless Wide-Area Coverage: It provides a better user
experience with a data rate of over 100Mbps. Users
can also experience high coverage of the 5G network
ManuscriptreceivedMay13,2020;revisedOctober25,2020andDecember
20,2020;acceptedDecember29,2020.DateofpublicationJanuary18,2021; in high-speed mobile environments and border areas.
date of current version March 11, 2021. This work was partially supported 2) High-Capacity Hot Spots: It supports high-capacity hot
by Taiwan Information Security Center at National Sun Yat-sen University
spotsandhigh-trafficservices.Thechallengeofthissce-
(TWISC@NSYSU) and the Ministry of Science and Technology of Taiwan
undergrantsMOST109-2221-E-110-044-MY2,MOST110-2923-E-110-001- nario is to give users 1 Gbps user experienced data rate,
MY3,MOST109-2222-E-011-007-MY2,andMOST109-2218-E-492-009.It tensofGbpspeakdatarate,andtensofTbps/km 2 traffic
also was financially supported by the Information Security Research Center
volume density.
at National Sun Yat-sen University in Taiwan and the Intelligent Electronic
Commerce Research Center from The Featured Areas Research Center 3) Low-Power Massive-Connections: The main applica-
Program within the framework of the Higher Education Sprout Project by tions of the 5G are smart cities, smart health care
theMinistryofEducation(MOE)inTaiwan.Theassociateeditorcoordinat-
systems, environmental monitoring, and even preven-
ingthereviewofthisarticleandapprovingitforpublicationwasB.Martini.
(Correspondingauthor:Jheng-JiaHuang.) tion of forest fires. These application scenarios have
Chun-IFaniswiththeDepartmentofComputerScienceandEngineering some common characteristics, such as large numbers
and the Information Security Research Center, National Sun Yat-sen
of packets transmission, numerous devices, and a wide
University, Kaohsiung 804, Taiwan, and also with the Intelligent Electronic
CommerceResearchCenter,NationalSunYat-senUniversity,Kaohsiung804, range of areas. To support these applications, 5G must
6 2
Taiwan(e-mail:cifan@mail.cse.nsysu.edu.tw). achievethe10 /km connectiondensitywithlowpower
Yu-Tse Shih and Wan-Ru Chiu are with the Department of Computer
consumption and low cost.
Science and Engineering, National Sun Yat-sen University, Kaohsiung 804,
Taiwan(e-mail:d073040005@student.nsysu.edu.tw;sdspscindy@gmail.com). 4) Low-Latency With High-Reliability: Driverless and
Jheng-Jia Huang is with the Department of Information Management, industrial control are two of the most critical appli-
National Taiwan University of Science and Technology, Taipei 106335,
cations in this scenario. It must guarantee that the
Taiwan(e-mail:jhengjia.huang@gmail.com).
minimumlatencycansupportdatatransferdelaysbelow
DigitalObjectIdentifier10.1109/TNSM.2021.3052208
ThisworkislicensedunderaCreativeCommonsAttribution4.0License. Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/

702 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
Fig.1. 5GScenarios.
Fig.2. SliceCrossinginthe5GNetwork.
one-thousandthofasecondandmaintainhighreliability
to ensure application security.
With the aforementioned four properties, the 5G network Fig. 2 shows the 5G network environment, where different
environment requires high-speed data rates while providing network slices and infrastructures provide different services.
various services to different devices and users. It is not Therefore, a user’s device will be required to be authenticated
just the pursuit of high speed as it used to be. Given the bythecorenetworkeachtimetheuserwantstoaccessanother
diversity of services and the balance of network speeds, the network slice. In the proposed scheme, we aim to reduce the
traditional network architectures cannot meet the 5G require- authenticationcostwhenadevicecrossesnetworkslices.Ifthe
ments. Therefore, 5G has proposed a new type of network user wants to access a different slice, he needs to be authen-
architecture called network slicing. In the traditional network ticated by the slice rather than the core network to achieve
environment, no matter the core network (CN) or the radio fast handover. Thus, we can reduce the time latency and com-
access network (RAN) has a dedicated hardware device to munication cost between the slice base station and the core
provide services, a set of devices only corresponds to a network.
single service. It would easily cause that any minor adjust- Besides, for security concerns, the framework of security
ments may lead to an overall service suspension, inefficiency, authentication must be innovated. In the past generations, the
and huge hardware cost. Since 5G communication requires authentication framework only certified one service at a time.
a lot of network access, the concept of network slicing is Foranewtypeofnetworkcontainingalargenumberofaccess
introduced to divide a physical network into multiple virtual networks and supporting large numbers of services, the tra-
networks, where each virtual network can flexibly correspond ditional network authentication framework is inefficient and
to different services. Therefore, it is no longer necessary to costly. According to the security white paper “Security chal-
map each service to a dedicated network environment when lengesandopportunitiesfor5Gmobilenetworks”[3]released
deploying, which significantly reduces network hardware byNOKIAin2017,and“5GSECURITY:SCENARIOSAND
costs. SOLUTIONS” [4] released by Ericsson in 2015, the 5G secu-
According to the consumers’ demands, network slicing can rity authentication framework needs to consider the following
be adjusted without suspending the overall service’s opera- aspects:
tion. Specifically, 5G adopts NFV and SDN to implement the 1) Multiple access networks (heterogeneous networks)
functionalities of network slicing. Specifically, it virtualizes 2) Fast service switching (network slicing)
the network functions through the NFV technology, and then 3) Fast authentication
utilizes the SDN technology to control the flow of packets 4) Reduction of the computation cost of the operator
uniformly. Thus, a single network function no longer requires Since the appearance of heterogeneous networks and network
support from a single hardware device, which can reduce the slicing, the network society becomes more complicated than
cost of telecommunication operators. Since the SDN technol- before, so we need a mechanism for rapid authentication and
ogyisusedasapacketflowcontrolsystem,allservicenetwork computation to support a diverse network society. In addition
packets can be managed in a unified manner and integrated to the support of rapid authentication, reducing the compu-
into a complete 5G network. With the cooperation of NFV, tation cost is also an essential topic in these white papers.
SDN, and cloud computing, the 5G communication provides The security white paper also mentions the attacks that 5G
a highly flexible network. The traditional vertical network systems may suffer from. For example, hackers may launch
can be divided into many pieces, each of which is indepen- DDOS attacks on a large number of IoT devices. Compared
dent and does not interfere with each other. The operator can with traditional single-user devices, 5G networks face this
impose virtual network services that satisfy the customers’ threat more seriously than before. Not only are the technical
requirements. attacks increasing, but also there are more social engineering

TH
FANetal.:CROSS-NETWORK-SLICEAUTHENTICATIONSCHEMEFOR5 GENERATIONMOBILECOMMUNICATIONSYSTEM 703
attacks. Therefore, we must design the 5G systems very care- development of developed and developing countries. Mobile
fullyandautomatethemasmuchaspossibletoreducemanual communication has been closely integrated into the daily life
management and build a secure network environment. of the entire society. It is expected that social technology
In addition to the white papers, 3GPP explicitly defined the trends and the evolution of mobile communication systems
network slice architecture in the TS 23.501 [5] standard. For will remain tightly coupled and become the foundation of the
example, in Network Slice Selection Assistance Information society.However,itisexpectedthatinthefuturenewrequire-
(NSSAI), each slice Single-Network Slice Selection ments,suchasmoretraffic,moredevices,anddifferentservice
Assistance Information (S-NSSAI) has its Slice/Service requirements,abetterqualityoftheuserexperience(QoE)and
Type (SST) and the Slice Differentiator (SD). The NSSAI better affordability to further reduce costs will require more
is a collection of max eight S-NSSAIs (that is, each user and more innovative solutions. The goal of this recommenda-
can access at most eight services) and so on. Through the tion [1] is to define IMT’s vision, describe potential users and
above white papers or standards, we can learn that switching applicationtrends,trafficgrowth,technologytrends,andspec-
betweenslicesinasecurewayisurgentlyrequired.Therefore, trum impact, and provide guidelines for the IMT framework
designing a fast and light-weight authentication for the 5G and capabilities in the future.
network environment is a crucial goal for 3GPP and the
operators.
B. 5G Network Environments
A. Contribution The 5G network has stretched much of flexibility due to
the concept of network slicing comparing with traditional
Devices are able to support diverse wireless communi-
networks. The 5G networks not only enhance broadband but
cation systems now, which are also known as heteroge-
also connect the whole smart devices to construct the mMTC
neousnetworks,butthecurrentauthenticationmechanismsdo
property.Moreover,itprovidesultra-lowlatencyandhighreli-
not address adequate strategies for heterogeneous networks.
abilitynetworktransmissioninthisenvironment.Furthermore,
In tradition, there is a corresponding authentication frame-
theoriginalaccessnetworkandcorenetworkmustbeadjusted
work for an access network. However, there is no complete
according to the target: the connection of many Internet of
cross-network-sliceauthenticationframeworkinthetraditional
Thingsdevices,low-latency,high-reliabilitynetworktransmis-
architecture,alsointhe5Gstudy.Onlytheneedofintegrating
sion,andtherealizationofspeedinahigh-speedtransmission
heterogeneous network authentication was proposed, but no
environment. Therefore, whether it is base station deployment
correspondingsolutionhasbeenputforward.Itisstillanopen
ornetworkdatapackettransmission,5Gnetworksareentirely
problem to provide a cross-slice authentication. Therefore,
different from traditional networks.
in this article, we will design a fast authentication mecha-
In a traditional mobile network, all user devices attached
nism tailored for the 5G network environment. Through this
with an access network are further connected to the core
mechanism, we integrate the access authentication of hetero-
network. The data computation units are unified in the core
geneousnetworks.Duetotheintegrationoftheheterogeneous
network. However, this method may increase latency unnec-
networks, it is unnecessary to spend a lot of time repeat-
essarily. In order to address the aforementioned aspect and
edly running the authentication process, and we can achieve
to satisfy the diversified services of 5G, the core network and
low-latency with high-reliability mechanism in 5G.
theaccessnetworkpartiallyutilizetheconceptofcentercloud
and edge cloud. The edge cloud is the collective name for the
B. Organiazation
access network and a small part of the core network. In order
In Section II, we review some backgrounds of knowl- toeasilyconnecttothebasestation,theedgecloudisbeingset
edge, including the 5G environment and the 3GPP standard upneartothebasestation.Therefore,thefunctionalitiesofthe
TS 33.501. In Section III, we briefly review an authenti- original core network are moved with low latency to the edge
cation scheme and give some comments on the scheme. In cloud. Hence, the consumer needs to connect its nearby base
Section IV, we describe the proposed authentication scheme station to avail the permissible network computing and stor-
inthe5Genvironment.Weprovidethesecurityanalysisofthe age features. Center cloud is a small part of the core network.
proposedschemeinSectionV.Thecomparisonsarepresented If the number of service requests are high enough, such as
inSectionVIandaconcludingremarkisgiveninSectionVII. the mMTC scenario, the data are still processed in the center
cloud just as a traditional network.
II. PRELIMINARIES As a result, the latency of the package switching can be
greatly reduced. Fig. 3 shows the different service slices with
In this section, we will briefly introduce some 3GPP
differentfunctionalitiesdeployedbetweenthecentercloudand
standards and technologies related to our work.
the edge cloud. The eMBB service has a great demand for
bandwidth, so the user plane of the core network and the
A. IMT Vision–Framework and Overall Objectives of the
cache memory can be placed in an edge cloud which is closer
Future Development of IMT for 2020 and Beyond [1]
to the user. Thus, it can increase the user’s favorability to
The social and economic evolution of the past few decades the service. URLLC service is designed for automatic driv-
is an essential driving factor for the evolution of mobile com- ing and remote management. It is more demanding for the
munications, which has promoted the economic and social latency related to the package switching. To achieve the goal,

704 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
Fig.4. ATS33.501Flow.
Fig.3. 5GNetworkEnvironments.
as “core network.” A mobile device initiates a transmission
flow by sending a request to the base station gNB for access-
the core network and the corresponding server (such as V2X ing the network and transmitting SUCI (i.e., encrypted SUPI)
Server) are moved to the edge cloud to reduce the data trans- or Globally Unique Temporary UE Identity (GUTI). After
missiontime.Throughthecollocationbetweentheedgecloud receiving the information, the base station gNB forwards the
and the center cloud, the edge cloud can separate and dis- informationtothecorenetwork.Thecorenetworkreceivesthe
tribute the complexity of the calculation to the center cloud. message and judges if it is a GUTI or SUCI. If the message
Duetothepowerofpartialcalculationsisdecentralizedtothe is a GUTI, it matches the corresponding SUPI and then the
edge cloud, the demand for low-latency service can be easily network service information (SN-Name) corresponding to the
achieved. carried process in the core network will be analyzed to deter-
mine whether the mobile phone is within the service range of
the network or not. After confirming the above information,
C. Technical Specification 33.501
the core network will decrypt SUCI to obtain SUPI and con-
A unique International Mobile Subscription Identity
figure the corresponding authentication procedure for mobile
(IMSI) [6] shall be allocated to each mobile subscriber in
phones through SUPI.
the GSM/UMTS/EPS system. In the traditional 2G, 3G, and
We know that encrypting SUPI and decrypting SUCI are
even 4G network environments, the problem of leaking pri-
a major issue for mobile phone identity verification during
vate locations of mobile phones, the so-called IMSI Catcher,
the authentication and transmission process. Based on elliptic
has not been properly solved. Due to the considerations of
curvecryptography(ECC),therearetwopairsofkeys.Oneis
network functionality, cost, and security, this issue is a signif-
the pair of the terminal side ephemeral (Eph.) public key and
icant concern whenever a new generation of communication
private key, where both of the keys are generated by Eph.key
network standards is formulated. According to TS 33.501 [7]
pairgeneration.Theotherpaircomesfromthehomenetwork.
publishedby3GPPin2018,the5GIMSIsecuritystandardhas
Theuserhasthepublickeyofthehomenetworkstoredinthe
beenclearlydefined.In5G,thetrueidentityofamobilephone
SIM card.
is called SUbscription Permanent Identifier (SUPI), which is
similartoIMSI,andtheciphertextencryptedbythepublickey
D. Slice Specific Authentication and Access Control for
iscalledSUbscriptionConcealedIdentifier(SUCI).In4G,the
5G [8]
IMSIissentincleartextfromtheUEtothenetwork.Tosolve
this problem, 5G conceals the SUPI by encrypting it. In 2020, Behrad [8] pointed out that each network slice
AccordingtoTS33.501,5Gintroducesapublic/privatekey can be dedicated to a third party. Moreover, they proposed a
system. The operator stores its public key in the secure ele- 5Gslice-specificauthenticationandaccesscontrolmechanism.
ment of a UE and keeps the private key by itself. Besides, On the other hand, the Mobile Network Operator (MNO) is
the UE will encrypt the SUPI with the operator’s public key, not responsible for Authentication and Access Control (AAC)
and it does not send its identity in a cleartext. In this way, of all devices in the network, which decreases the signalling
only the carrier can decrypt the real identity information of load on the operator’s network. The architecture of the AAC
the mobile phone. Attackers can only obtain the encrypted mechanisms consists of an AC server and AC clients. When
informationandcannotcatchtheIMSIwithouttheprivatekey. anACclientwantstoaccessthenetwork,theACclientneeds
AftertheSUCIistransmittedtothebasestation,thebasesta- to send queries to the AC server to process the authentication
tion directly forwards it to the core network. Fig. 4 shows the protocol.
transmission flow of the device identity from the user side to When a device needs to be authenticated by the network
the core network in TS 33.501. sliceservice,thedevicewillperformtheauthenticationproto-
In the 5G core network, NFV virtualizes the original col based on the AAC information provided fromthe network
core network into many functions with different features one slice service. This information includes the slice ID of the
another. However, in the paper, we will not go into details third party and the device identifier. These identifiers may
about the functions and the operating mode between func- be distinct from the globally unique identifiers used in the
tions. We refer to the core network functions in TS 33.501 current cellular systems and the 3GPP specifications (IMSI

TH
FANetal.:CROSS-NETWORK-SLICEAUTHENTICATIONSCHEMEFOR5 GENERATIONMOBILECOMMUNICATIONSYSTEM 705
and SUPI). According to the AAC mechanism selected by the systematic, and security assessment of the 5G security target
third party, the information provided to the devices may con- model. This work [13] gave a formal analysis of 5G authen-
tain some security credentials. It determines the format of the tication and the first formal model of the 5G AKA protocol.
subscription identifiers, and they do not need to be specific Moreover,itidentifiedtheassumptionsrequiredforeachsecu-
to 5G. rity goal and pointed out some critical security goals missing
from the 3GPP standards.
E. Some Related Authentication Schemes in LTE-A
G. An Overview of the 3GPP 5G Security Standard
In 2019, Panda and Chattopadhyay proposed an improved
In2019,thiswork[14]waspostedonthewebsite.Itshows
authentication and security scheme for LTE/LTE-A
an overview of the 3GPP 5G security standard, including the
networks [9]. It adopted elliptic curve encryption (ECC),
authentication framework, subscriber privacy, service-based
elliptic curve Diffie-Hellman (ECDH) and Salsa20 algorithms
architecture and interconnection security, and user plane pro-
to improve end-to-end security and provide faster data
tection.LTE/4Gand5Ghavemanysimilarfunctions.Inthese
transmission for 4G environments. The scheme [9] used
two systems, security mechanisms can be divided into two
a variety of robust encryption techniques while providing
groups. The first group contains all of the network access
proper mutual authentication between the user equipment
security mechanisms. These are security functions which pro-
(UE) and the message management entity (MME).
vide users with secure access to services via devices (usually
In 2019, Ma et al. proposed a privacy-preserving secure
phones), and can prevent attacks on the air interface between
handoverauthenticationscheme[10]inLTE-Anetworks.They
the device of a user and the radio node (eNB in LTE or gNB
proposedasecurehandoveridentityverificationschemebased
in 5G). This includes functions that enable nodes to exchange
on a certificateless symbol encryption technology. Their solu-
signaling data and user data safely, such as between radio
tion can realize a secure and unified handover procedure
nodes and core network nodes.
without sacrificing efficiency. Security and performance mea-
surement show that their scheme can satisfy various security III. RELATEDWORKS
properties, including perfect forward/backward confidential- The 3GPP did not specify how to perform authentica-
ity and privacy protection. At the same time, their solution tion when a device needs to access another network slice.
achieves the desired efficiency. The straightforward method is to authenticate the device by
In 2019, Zhou et al. proposed a hybrid authentication the core network again. Our proposed scheme can speed up
protocol for LTE/LTE-A network [11]. They discussed the theauthenticationbyauthenticatingthedeviceinthesliceside.
main weaknesses of the Long Term Evolution (LTE) authen- Comparing to 5G-AKA and EAP-AKA, the device does not
tication process and proposed a new method, the Hybrid need to be authenticated by the core network in the proposed
EvolutionaryPacketSystem(HEPS)protocoltosolvethevul- scheme in the above situation. After we surveyed the 5G
nerability.Theirprotocolhasbeenlogicallyverified,usingthe networksliceauthenticationschemes,theconceptofNietal.’s
Burbu-Abadi-Needum(BAN)logic.TheHEPSagreementwill scheme [15] is more suitable for our scheme.
optimizetheperformanceoftheLTEauthenticationprocessand Based on the framework of the 3GPP TS 23.501 System
fundamentallycopewiththesecurityproblemsoftheprocess. Architecture[5]forthe5GSystem,Nietal.proposedaneffi-
In 2019, Parne et al. proposed a Performance and cient service-oriented authentication protocol, but we found
Security Enhancement (PSE-AKA) protocol for LTE/LTE-A a disadvantage. The scheme performs the same identity ver-
networks[12].ItsupportsInternetofThingsandtheproposed ification process for each slice base station, but the scheme
protocol follows the cocktail therapy, generates an authentica- doesnotconsiderthesituationwheredifferentslicesmayhave
tion carrier, and improves performance in terms of computing different infrastructures and specifications. The operator can
andcommunication overhead. Theagreement protects thepri- find the slices which a user can access without knowing the
vacy of the object, protects KSI, and avoids identification slice/servicetype(SST)andSDofeachslice,andtheusercan
attacks on the communication network. It used the BAN logic anonymouslyaccessthesliceservices.Hence,theschemecan
and the AVISPA tools to perform verification and security protect the information included in each slice. Nevertheless,
analysis on the proposed protocol, respectively. Security anal- the scheme ignores the different services which are provided
ysis demonstrates that the protocol meets the security goals by each slice. For the service with less latency, the computing
and can resist various known attacks. unit should be decentralized to the edge cloud. Therefore, we
do not recommend that a service should be authenticated in
F. A Formal Analysis of 5G Authentication the center cloud since it will increase the latency.
There have been several schemes proposed in recent years;
The mobile communication network connects most of the
henceweanalyzetheseworksthataresimilartoourproposed
world’s population. For the 5G network, the 3GPP group has
scheme. In the following subsections, we briefly introduce
standardized the 5G AKA protocol for the purpose. The pro-
some related works.
tocol provides the first comprehensive official model from the
AKA series of agreements: 5G AKA. It also extracts precise
A. Authentication and Access Control for 5G [16]
requirements from the 3GPP standards that define 5G and
identify missing security goals. Using Tamarin, a security In2020,Behradetal.proposedaworkcalled“Authentication
protocol verification tool, they conducted a comprehensive, and Access Control for 5G” [16]. They showed some surveys

706 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
authenticationandkeyagreementthatmeetstheAACrequire-
|     |     |     |     |     | ments in      | 5G. The       | authentication |            | mechanism   |              | in the  | 5G          | system |
| --- | --- | --- | --- | --- | ------------- | ------------- | -------------- | ---------- | ----------- | ------------ | ------- | ----------- | ------ |
|     |     |     |     |     | will follow   | the           | same           | principles | with        | some         | subtle  | differences |        |
|     |     |     |     |     | in the 4G     | system.       | These          |            | differences | in           | the AKA | mecha-      |        |
|     |     |     |     |     | nism will     | only          | be from        | the        | network     | perspective, |         | not         | from   |
|     |     |     |     |     | the UE        | perspective.  | The            | AKA        | mechanism   |              | in the  | 5G          | system |
|     |     |     |     |     | (such as      | the mechanism |                | in         | the 4G      | system)      | takes   | the         | “ser-  |
|     |     |     |     |     | vice network  | name”         |                | (such      | as the SNid | in           | 4G)     | to derive   | the    |
|     |     |     |     |     | anchor key    | (KSEAF);      |                | therefore, | the         | anchor       | key     | will        | belong |
|     |     |     |     |     | to a specific | service       |                | network,   | and         | this service |         | network     | can-   |
|     |     |     |     |     | not pretend   | to            | be another     | service    | network.    |              | Unlike  | EPS+AKA,    |        |
Fig.5. FunctionsofanAACSystemfrom[17]. there are four participants in 5G-AKA, and this section will
|     |     |     |     |     | further explain    |              | these           | participants. |            | Another        | difference |            | in the  |
| --- | --- | --- | --- | --- | ------------------ | ------------ | --------------- | ------------- | ---------- | -------------- | ---------- | ---------- | ------- |
|     |     |     |     |     | AKA mechanism      |              | of              | the 5G        | system     | is that        | the        | anchor     | key     |
|     |     |     |     |     | (KSEAF)            | derived      | in              | 3GPP          | access     | also           | is able    | to be      | used    |
|     |     |     |     |     | for non-3GPP       |              | access          | without       | a new      | authentication |            | process.   |         |
|     |     |     |     |     | The authentication |              | process         | will          | involve    | the            | UE         | in the     | service |
|     |     |     |     |     | network,           | the security |                 | anchor        | function,  | the            | AUSF       | in HN,     | and     |
|     |     |     |     |     | the UDM/ARPF       |              | (Authentication |               | Repository |                | and        | Processing |         |
|     |     |     |     |     | Function)          | in HN        | [18].           | SEAF          | will       | be included    |            | in AMF     | and     |
interactwithAUSFinordertoobtainauthenticationdatafrom
|     |     |     |     |     | UDM. It | completes | the | UE  | authentication |     | of different |     | access |
| --- | --- | --- | --- | --- | ------- | --------- | --- | --- | -------------- | --- | ------------ | --- | ------ |
networks.ARPFstoressubscriberprofilesandsecurity-related
|     |     |     |     |     | information. | It  | also selects | the | authentication |     | method | (such | as  |
| --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | -------------- | --- | ------ | ----- | --- |
Fig.6. AnAACModelintheCellularNetworks.
|     |     |     |     |     |         |     | +    |     | +    |           |     |        |       |
| --- | --- | --- | --- | --- | ------- | --- | ---- | --- | ---- | --------- | --- | ------ | ----- |
|     |     |     |     |     | 5G-AKA, | EAP | AKA, | EAP | TLS) | according |     | to the | iden- |
tityofthesubscriber,andcalculatesthekeymaterialofAUSF.
| on the network | architecture, | AKA | protocol, | access control, |          |         |        |     |            |       |     |     |     |
| -------------- | ------------- | --- | --------- | --------------- | -------- | ------- | ------ | --- | ---------- | ----- | --- | --- | --- |
|                |               |     |           |                 | The call | flow of | 5G-AKA | is  | as follows | [19]. |     |     |     |
specific use cases, and requirements of 5G. (1) Initially, the UE transmits its SUCI to SEAF.
1) Basics of Authentication and Access Control: The main (2) After receiving the signaling message from the UE,
purposes of Authentication and Access Control (AAC) are to SEAF will send a 5G-AIR (Authentication Initiation
protect user privacy and network security. Fig. 5 shows the Request) message to AUSF. 5G-AIR includes the UE’s
| flow of an AAC | system. |     |     |     |      |     |      |         |      |        |         |          |     |
| -------------- | ------- | --- | --- | --- | ---- | --- | ---- | ------- | ---- | ------ | ------- | -------- | --- |
|                |         |     |     |     | SUCI | or  | SUPI | and the | name | of the | service | network. |     |
2) Overall Architecture of the AAC in 3G, 4G, and This message also shows that the UE is using a 3GPP
5G: From the perspective of AAC, cellular networks (such access or non-3GPP access.
as 3G, 4G, and 5G) are composed of three main parts: ES (3) After verifying the authorization of the service network
(userequipment)orequipment,SN(servicenetwork),andHN requesting the authentication service, AUSF will send
| (home network). | HN is the | network | to which | UEs subscribe. |     |     |         |              |     |     |      |       |      |
| --------------- | --------- | ------- | -------- | -------------- | --- | --- | ------- | ------------ | --- | --- | ---- | ----- | ---- |
|                 |           |         |          |                | an  | AIR | message | to UDM/ARPF. |     | If  | AUSF | sends | SUCI |
The service network is the ES service network changing the in this message, the SIDF (Subscription ID De-hiding
network in the roaming plan. SN is an AC client and HN is Function) parallel to UDM/ARPF will decrypt SUCI to
the AC server. Fig. 6 illustrates the AAC model in a cellular obtainSUPI.Afterreceivingarequestforauthentication
| network.          |     |        |         |               | informationfromAUSF,UDM/ARPFwillgenerateAVs |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------- | ------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3) Authentication | and | Access | Control | in 5G: The 5G |                                             |     |     |     |     |     |     |     |     |
(asin4G),andthenconvertthemintonewAVsspecific
architecture provides some new design options for authenti- to5Gsystems.Dependingontheselectedauthentication
cationandaccesscontrol,butitalsobringsmanycontinuities. method, this conversion will vary.
The most essential continuity involves symmetric key-based (4) UDM/ARPF sends the AV containing AUTN, XRES*,
authentication through security elements. In TS 33.501 of the KASUF, and SUPI to AUSF in the authentication
5G specification, secure elements in UEs or devices (such as informationresponsemessage.Whenreceivingthismes-
UICCin4Gand3G,andSIMcardin2G)werekepttohandle sage,AUSFcalculatesHXRES*,whichisthehashvalue
subscription authentication and process subscription creden- of XRES*, and stores KAUSF.
tials[7].ThiscredentialcanalsobeanESIM(EmbeddedUser (5) AUSF sends 5G-AIA (Identity Verification Information
Identity Module) provided by the device makers. The opera- Acceptance) (including HXRES*) to SEAF. This mes-
tor can provide its profile through the air when subscribing. sage does not include SUPI. AUSF (in the home
The authentication methods introduced in the 5G specifica- network) only sends SUPI to SEAF (in the service
tionare5G-AKA,EAP+AKAandEAP+TLS(TransportLayer network) after successful UE authentication.
| Security). |     |     |     |     | (6) After | storing | HXRES*, |     | SEAF | transmits |     | the | AUTN |
| ---------- | --- | --- | --- | --- | --------- | ------- | ------- | --- | ---- | --------- | --- | --- | ---- |
4) 5G-AKA Protocol: Without losing versatility, the proto- token in the authentication request message to the UE.
col focused on the 5G-AKA agreement (and its differences The UE verifies the validity of AUTN (by using the
+
with the EPS AKA agreement) because it is the main key shared with HN). If AUTN is valid, the network

TH
FANetal.:CROSS-NETWORK-SLICEAUTHENTICATIONSCHEMEFOR5 GENERATIONMOBILECOMMUNICATIONSYSTEM 707
| identity        | verification |                | in            | the UE        | is successful. |              | If AUTN        |     |     |     |     |     |     |     |     |
| --------------- | ------------ | -------------- | ------------- | ------------- | -------------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| is              | invalid,     | the UE         | will          | send          | a MAC          | failure      | message        |     |     |     |     |     |     |     |     |
| (message        |              | authentication |               | code)         | to SEAF.       | Next,        | as in the      |     |     |     |     |     |     |     |     |
| ESP+AKA         |              | process,       | the           | UE verifies   |                | the sequence | num-           |     |     |     |     |     |     |     |     |
| ber             | (SQN)        | derived        | from          | AUTN          | to control     |              | the freshness  |     |     |     |     |     |     |     |     |
| of              | AUTN.        | If this        | verification  |               | fails,         | the UE       | will send      | a   |     |     |     |     |     |     |     |
| synchronization |              |                | failure       | message       | to             | SEAF.        | The UE also    |     |     |     |     |     |     |     |     |
| calculates      |              | RES*.          |               |               |                |              |                |     |     |     |     |     |     |     |     |
| (7) The         | UE transmits |                | RES*          | to SEAF       | in             | the          | authentication |     |     |     |     |     |     |     |     |
| response        |              | message.       | SEAF          | verifies      | the            | validity     | of RES*        |     |     |     |     |     |     |     |     |
| by              | calculating  | HRES*          |               | and comparing |                | it with      | HXRES*.        |     |     |     |     |     |     |     |     |
| (8) In          | order        | to make        | the final     | decision      |                | about        | UE authenti-   |     |     |     |     |     |     |     |     |
| cation          | through      | the            | home          | network,      | SEAF           |              | sends 5G-AC    |     |     |     |     |     |     |     |     |
| (identity       |              | verification   | confirmation) |               | messages       |              | (including     |     |     |     |     |     |     |     |     |
| RES*)           | to           | AUSF.          | AUSF          | verifies      | the            | validity     | of RES* by     |     |     |     |     |     |     |     |     |
| comparing       |              | it with        | XRES*.        |               | Sending        | 5G-AC        | messages       |     |     |     |     |     |     |     |     |
from SN to HN is to prevent possible billing cheating Fig.7. TheProposedSystemModel.
| proposed            |     | by SN | [20].                          |     |     |     |     |           |        |      |             |      |     |         |           |
| ------------------- | --- | ----- | ------------------------------ | --- | --- | --- | --- | --------- | ------ | ---- | ----------- | ---- | --- | ------- | --------- |
| 5) NewConceptsin5G: |     |       | Thesedifferentgoalsandusecases |     |     |     |     |           |        |      |             |      |     |         |           |
|                     |     |       |                                |     |     |     |     | server to | ensure | that | the service | data | in  | the fog | cache and |
haveanimportantimpactonthesecurityofthesystem.When
designingappropriateauthenticationandaccesscontrolmech- the remote server are safely accessed with low latency. They
evaluatedtheperformanceoftheproposedframeworkthrough
anismsfor5Gnetworks(suchasfastcommunicationrequiring
|          |             |     |                  |     |          |     |              | simulations | to  | demonstrate | its | efficiency | and | feasibility | under |
| -------- | ----------- | --- | ---------------- | --- | -------- | --- | ------------ | ----------- | --- | ----------- | --- | ---------- | --- | ----------- | ----- |
| fast AAC | processes), |     | service-specific |     | security |     | requirements |             |     |             |     |            |     |             |       |
should be considered [21]. Another example is that in IoT, the 5G infrastructure.
|     |     |     |     |     |     |     |     | Since, | in Ni | et al.’s | scheme, | the core | network |     | needs to re- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | ------- | -------- | ------- | --- | ------------ |
manydevicesmayaccessthenetworkatthesametime,sothe
network should be able to control the large amount of signal- authenticate a device when it accesses a different slice, it will
|             |              |           |              |             |             |          |              | be time-consuming. |                  | In  | our proposed |       | scheme, | the          | devices only |
| ----------- | ------------ | --------- | ------------ | ----------- | ----------- | -------- | ------------ | ------------------ | ---------------- | --- | ------------ | ----- | ------- | ------------ | ------------ |
| ing traffic | and          | correctly | authenticate |             | the devices |          | to withstand |                    |                  |     |              |       |         |              |              |
|             |              |           |              |             |             |          |              | need to            | be authenticated |     | by slices    | after | the     | registration | phase.       |
| the DDoS    | (distributed |           | denial       | of service) |             | attacks. | IoT devices  |                    |                  |     |              |       |         |              |              |
have low power consumption and cannot support the strong As compared to Ni et al.’s scheme, our scheme can reduce
|                |     |          |              |     |      |             |      | the latency | time | of the | authentication. |     | A detailed |     | comparison |
| -------------- | --- | -------- | ------------ | --- | ---- | ----------- | ---- | ----------- | ---- | ------ | --------------- | --- | ---------- | --- | ---------- |
| authentication |     | process. | In addition, |     | they | are usually | able | to          |      |        |                 |     |            |     |            |
connect to the network through the authentication and access will give in Section VI.
| control of | the | 5G non-3GPP |     | access | options | (some | of these |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ------ | ------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
IV. THEPROPOSEDSCHEME
| options | will not | have | 5G radio | accesses |     | and will | use Wi-Fi |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | -------- | -------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
or Bluetooth) [22]. In view of these limitations, some IoT We present an efficient and lightweight authentication
|         |           |       |     |             |     |                |      | scheme    | for the | 5G network. |        | In the | proposed  | scheme, | there    |
| ------- | --------- | ----- | --- | ----------- | --- | -------------- | ---- | --------- | ------- | ----------- | ------ | ------ | --------- | ------- | -------- |
| gateway | solutions | based | on  | group-based |     | authentication | were |           |         |             |        |        |           |         |          |
|         |           |       |     |             |     |                |      | are three | roles:  | User,       | Slice, | and    | Operator. | The     | proposed |
proposedtoreducethenumberofcompleteAKAprocessexe-
|               |       |             |       |             |          |         |                | scheme                | consists | of four | phases:       | Setup, | Registration,  |     | Three-     |
| ------------- | ----- | ----------- | ----- | ----------- | -------- | ------- | -------------- | --------------------- | -------- | ------- | ------------- | ------ | -------------- | --- | ---------- |
| cutions [23], | [24]. | But         | these | group-based |          | AKA     | solutions also |                       |          |         |               |        |                |     |            |
|               |       |             |       |             |          |         |                | Party Authentication, |          |         | and Handover, |        | as illustrated |     | in Fig. 7. |
| have their    | own   | weaknesses. |       | Some        | of these | include | the tra-       |                       |          |         |               |        |                |     |            |
ditional AKA weaknesses mentioned in the previous section, The Setup algorithm publishes security parameters that will
|          |         |     |             |     |          |          |          | be used | to provide | authentic | communication. |     |     | Next, | users will |
| -------- | ------- | --- | ----------- | --- | -------- | -------- | -------- | ------- | ---------- | --------- | -------------- | --- | --- | ----- | ---------- |
| and some | attacks | are | group-based |     | specific | to these | methods. |         |            |           |                |     |     |       |            |
registerwiththeoperatorintheRegistrationphase.Ausercan
| For example, | attackers |       | can | impersonate | group |     | members and |             |                |            |        |          |       |         |               |
| ------------ | --------- | ----- | --- | ----------- | ----- | --- | ----------- | ----------- | -------------- | ---------- | ------ | -------- | ----- | ------- | ------------- |
|              |           |       |     |             |       |     |             | send a      | request        | to a slice | that   | the user | wants | to      | access in the |
| access the   | Internet  | [25]. |     |             |       |     |             |             |                |            |        |          |       |         |               |
|              |           |       |     |             |       |     |             | three-phase | authentication |            | phase. | The      | 5G    | setting | allows one    |
devicetohaveatmosteightslicesatatime.Aftertheoperator
| B. Ni et | al.’s Scheme |        |          |     |           |                  |     |               |     |            |         |        |      |       |             |
| -------- | ------------ | ------ | -------- | --- | --------- | ---------------- | --- | ------------- | --- | ---------- | ------- | ------ | ---- | ----- | ----------- |
|          |              |        |          |     |           |                  |     | authenticates | a   | slice with | a user, | if the | user | wants | to access a |
| In 2018, | Ni           | et al. | proposed | an  | efficient | service-oriented |     |               |     |            |         |        |      |       |             |
differentslice,hewillbeauthenticatedbythenewslicerather
| authentication | scheme |     | [15], | which | is the compliance |     | with the |     |     |     |     |     |     |     |     |
| -------------- | ------ | --- | ----- | ----- | ----------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
3GPP standard for the 5G architecture. We will briefly intro- than the core network to achieve fast handover.
| duce Ni                                                    | et al.’s | scheme | and | give a | summary. | They | proposed |          |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | -------- | ------ | --- | ------ | -------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| anefficient,secure,andservice-orientedauthenticationframe- |          |        |     |        |          |      |          | A. Setup |     |     |     |     |     |     |     |
worktosupportnetworkslicingandfogcomputingfor5GIoT Each slice is deployed by the operator, and the operator
services.Specifically,userscaneffectivelyestablishaconnec- shares a long-term secret key slki with each slice SIDi at the
tion with the 5G core network and anonymously access the time of deployment. Let n be the number of slices. We define
|     |     |     |     |     |     |     |     |     | = {slk1 | ,slk2 | ,...,slkn | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | --- | --- | --- | --- |
IoT service assigned by the fog node according to the correct • slk as the set of the long-term
5G infrastructure network slice selected by the slice/service secret keys of the n different slices.
|     |     |     |     |     |     |     |     |     | ={SID1 | ,SID2 | ,...,SIDn |     | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------- | --- | --- | --- | --- |
type of the access service. A privacy-preserving slice selec- • SID as the set of the identi-
tion mechanism is introduced to retain the configured slice ties of the n slices.
type and users who access the service type. In addition, a ses- • sSecret = {κ ,κ ,...,κ } as the set of the identity
|     |     |     |     |     |     |     |     |     |     | 1   | 2   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sion key is negotiated among the user, the fog, and the IoT secrets of the n slices.

708 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
We define a Single-NSSAI (S-NSSAI) as an identity secret decryption is identical to its κ i. If not, SIDi will
κ i, which consists of a slice/service type (SST) and some abort the query.
optimal information called a slice differentiator (SD). Every 2) SIDi computes c2 = Eslk (c1 ||κ i ||ts1 )||SIDi and
i
slice has its unique feature. It is easier to find slices that pro- sendsc2 totheoperatorwherets1 isthetimestamp.
vide services through these features by users or the operator. • Step 3: The operator authenticates the slice and verifies
When the demand for various services increases or decreases, the user
the set slk, SID, and sSecret will be added or deleted by the 1) The operator authenticates the slice: The operator
operator. first parses c2 = c 2 (cid:2)||SIDi. According to SIDi, the
According to 3GPP TS 33.501, the encryption and decryp- operator retrieves (slki, κ i) from its database and
tion between the operator and the users are under the Elliptic decrypts c 2 (cid:2) . Let c1 ||κ(cid:2) i ||ts1 =Dslk i (c 2 (cid:2)). The oper-
Curve Integrated Encryption Scheme (ECIES) [26]. Based on ator checks if both κ(cid:2) i =κ i and ts1 is fresh.If true,
the ECIES scheme: the operator will authenticate SIDi; otherwise, it
• The operator generates a pair of keys (pk, sk) where pk will abort the request.
is its public key and sk is the secret key corresponding 2) The operator verifies the user: The operator takes
to pk. upk in c1 and its private key sk to create the shared
• pk is stored in every SIM card where pk is legally key x = H(sk · upk). It performs the following
published and sk is kept secret by the operator. tasks.
• A key generator keygen is stored in every SIM card, - Decrypt SUCI in c1 with x to get
which can generate a different pair of keys for a user Eulk (SUPI||ID||α)||ID.
in each different session. - Decrypt Eulk (SUPI||ID||α) with ulk of user ID
• (Ekey ,Dkey ) is a pair of symmetric encryption and and then parse the result as SUPI||ID (cid:2)||α.
decryption functions. If ID (cid:2) (cid:4)=ID, the operator aborts the request.
• H is a one-way hash function defined in ECIES, which • Step4:Theoperatorsetstheparametersforhandoverand
maps an arbitrary-length byte string to a byte string of a sends the parameters to the slice
predefined output length. Since the operator knows the services the user can
access,itcanretrievethelong-termsecretkeysandiden-
B. Registration
tity secrets of those slices and perform the following
A user is able to register with the operator as follows. tasks.
1) The user must provide his identity ID and the identities 1) Compute slice (cid:2) = {Eslk (κ j ||uslkj )||uslkj |j ∈
j
of the slices which he wants to access to the operator. Γ ID } where uslkj is randomly chosen and will
2) Let Γ ID ⊆[1,n] be the index set of the slices the user act as the common secret key shared by user ID
wants to access. The operator gives a SIM card SIM and slice SIDj for each j after the three-party
to the user where SIM contains {pk,keygen,slice = authentication is successfully completed.
{Eslk j (κ j )||SIDj |j ∈Γ ID },ulk}. 2) Computec3 =Eslk i (Eulk (slice (cid:2)||α||β)||κ i ||α||β||ts2 )
where ulk is the long-term secret key shared by the operator where β is a randomly-chosen string and ts2 is the
andtheuseronly.Theoperatorshouldmaintainalisttorecord timestamp.
the information. The operator transfers c3 to SIDi.
• Step5:Thesliceauthenticatestheoperatorandsendsthe
C. Three-Party Authentication
parameters to the user
• Step 1: A user ID sends a request for accessing a service Afterreceivingc3,SIDi decryptsc3 andextractsthesec-
to a slice SIDi ond component κ˜ i from the output of the decryption.
1) Theuserrandomlychoosesastringαasthesession If both κ˜ i is identical to its κ i and ts2 is fresh, SIDi
number. will authenticate the operator; otherwise, it will abort the
2) The user executes keygen to generate a public- session. It sends c4 =Eulk (slice (cid:2)||α||β) to the user.
private key pair (upk, usk) for this session. • Step 6: The user authenticates the system and stores the
3) The user takes the operator’s public key pk which parameters for handover
hadbeenstoredinSIM andusktogenerateashared After receiving c4, the user decrypts it and extracts the
key x = H(usk ·pk) (According to ECIES [26], second component α(cid:2) from the output of the decryption.
H(usk ·pk)=H(sk ·upk)=x). If α(cid:2) = α, the user will authenticate the system; other-
4) The user forms SUCI = wise, he will abort the session. He keeps slice (cid:2) for later
Ex (Eulk (SUPI||ID||α)||ID) where SUPI is handover and sends H(β) to SIDi. Finally, the user sets
the user device identification code (similar to IMSI H(α||β) to be the session key with SIDi.
in 4G). • Step 7: The slice authenticates the user
5) Let c1 =Eslk (κ i )||SUCI||upk. The user sends c1 SIDi verifies if H(β) is correct by applying H to
i
to SIDi, where Eslk (κ i ) had been stored in SIM. the β it received from the operator. If true, it will
i
• Step 2: SIDi verifies the correctness of Eslk (κ i ) authenticate user ID; otherwise, it will abort the request.
i
1) After receiving c1, SIDi takes slki to decrypt Finally, SIDi sets the session key with the user to
Eslk (κ i ) and then verifies if the output of the be H(α||β).
i

TH
FANetal.:CROSS-NETWORK-SLICEAUTHENTICATIONSCHEMEFOR5 GENERATIONMOBILECOMMUNICATIONSYSTEM 709
D. Handover B. Mutual Authentication and Session Key Agreement
+
In the 5G environment, it is allowed that one device has Between User ID and the System (Slice Operator)
at most eight network slices at a time. In certain situations, a The long-term secret key ulk had been shared by user
devicemayneedtoswitchbetweentheslicesquickly.Suppose ID and the operator in the Registration phase. In Step 1 of
α
thatsliceSIDt istheonewhichuserIDwantstohandoverto. Three-Party Authentication, is randomly chosen by user
Thesliceandtheusercanauthenticateeachotherandestablish ID as a challenge material to the system and then SUCI
a session key as follows. = Ex (Eulk (SUPI||ID||α)||ID) is sent to the system. In
|     |     |     |     | (κ ||uslkt | )   |     |     |     |     |     |     |     | =Eulk | (slice | (cid:2)||α||β) |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | -------------- |
1) User ID retrieves Eslkt t and uslkt from his Step 5, the user receives the response c4
(cid:2)
stored slice , and then he randomly chooses a string α from the system. In Step 6, after decrypting c4, if the α in
|     |     |     | (α). |     |     | (κ ||uslkt | )   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and computes Euslkt He sends Eslkt t and the decryption result is identical to the one the user chosen in
Euslkt (α) to slice SIDt. Step 1, then he will authenticate the system since only the
2) SIDt decrypts Eslkt (κ ||uslkt ) to obtain κ and uslkt. operatorandheknowulk andboththeoperatorandSIDi had
|     |     |     |     | t   |     | t   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
κ
If the t is identical to its own one, SIDt will set uslkt authenticated each other.
tobethecommonsecretkeysharedwithuserID;other- Thestringβ israndomlychosenbytheoperatorinStep4to
|     |     |     |     |     |     |     | (α) |     |     |     |     |     | =Eulk | (slice | (cid:2)||α||β) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | -------------- |
wise, it will abort the request. SIDt decrypts Euslkt beachallengematerialtotheuserandc4
by using uslkt and gets α. It randomly chooses a string is sent to the user in Step 5. In Step 6, after decrypting
β and then computes and sends Euslkt (H(α)||β) to the c4 and getting β, the user computes and sends the response
H(β)
|     | user. |     |     |     |     |     |     |     | to  | the system. | If  | the response | is correct, | the | system |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ----------- | --- | ------ |
3) User ID decrypts Euslkt (H(α)||β) to obtain H(α) and will authenticate the user since β is randomly chosen by the
|     | β.  |     |     | H(α) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
He verifies if the is correct by applying H to operator and ulk is only known to the user and the operator.
α
the he chosen in step 1). If true, he will authenticate Therefore, mutually authentication between the user and the
SIDt and set the session key to be H(α||β); otherwise, system can be achieved.
hewillabortthesession.Finally,hecomputesandsends Consider the session key agreement. After the mutual
H(β) to SIDt. authentication, user ID and slice SIDi have shared α and β
4) SIDt verifies if H(β) is correct by applying H to the secretly,eachofwhichhasbeenprotectedbyeitherencryption
|     | β   |     |     |     |     |     |     |     |     |     |     | H(α||β) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
it chosen in step 2). If true, it will authenticate user or one-way hashing. Hence, can form as a session
ID and set the session key to be H(α||β); otherwise, it key between user ID and slice SIDi for the following secure
|     | will abort | the | request. |     |     |     |     | communication |     | in  | this session. |     |     |     |     |
| --- | ---------- | --- | -------- | --- | --- | --- | --- | ------------- | --- | --- | ------------- | --- | --- | --- | --- |
V. SECURITYANALYSIS C. Mutual Authentication and Session Key Establishment
|               |                |     |               |                |              |              |      | Between |       | User ID          | and Slice   | SIDt | in the Handover  | Phase |           |
| ------------- | -------------- | --- | ------------- | -------------- | ------------ | ------------ | ---- | ------- | ----- | ---------------- | ----------- | ---- | ---------------- | ----- | --------- |
| The           | security       | of  | mutual        | authentication |              | and session  | key  |         |       |                  |             |      |                  |       |           |
|               |                |     |               |                |              |              |      |         | After | performing       | Three-Party |      | Authentication   |       | success-  |
| establishment |                | can | be guaranteed | based          | on           | the security | of   |         |       |                  |             |      |                  |       |           |
|               |                |     |               |                |              |              |      | fully,  | user  | ID has           | obtained    |      | an authenticated | slice | (cid:2) = |
| public-key    | cryptosystems, |     |               | symmetric      | encryptions, | and          | one- |         |       |                  |             |      |                  |       |           |
|               |                |     |               |                |              |              |      | {Eslk   | (κ    | ||uslkj )||uslkj | |j          | ∈ Γ  | }                |       |           |
way hash functions. The challenge-response mechanism and j ID from the system. In the
j
|                                                      |     |     |     |     |     |     |     | Handover |     | phase, the | user | retrieves  | Eslkt (κ ||uslkt | ) and | uslkt |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ---- | ---------- | ---------------- | ----- | ----- |
| thetimestampapproachhavebeenappliedtowithstandreplay |     |     |     |     |     |     |     |          |     |            |      |            | t                |       |       |
|                                                      |     |     |     |     |     |     |     |          |     | (cid:2)    |      | (κ ||uslkt | )                |       |       |
attacks. We show how to achieve the security as follows. from slice and sends Eslkt t to SIDt. After decryp-
|           |                |             |                |       |      |         |     | tion,     | SIDt     | can obtain    | the     | common       | secret key | uslkt  | shared    |
| --------- | -------------- | ----------- | -------------- | ----- | ---- | ------- | --- | --------- | -------- | ------------- | ------- | ------------ | ---------- | ------ | --------- |
|           |                |             |                |       |      |         |     | with      | the      | user.         |         |              |            |        |           |
| A. Mutual | Authentication |             | Between        | Slice | SIDi | and the |     |           |          |               |         |              | α          |        | (α)       |
|           |                |             |                |       |      |         |     |           | The user | randomly      | chooses |              | and sends  | Euslkt | as a      |
| Operator  | in             | Three-Party | Authentication |       |      |         |     |           |          |               |         |              |            |        |           |
|           |                |             |                |       |      |         |     | challenge |          | to the slice. | If      | the response | H(α)       | from   | the slice |
slki
The slice long-term secret key had only been shared is correct, the user will authenticate the slice since none can
by slice SIDi and the operator in the Setup phase. In decrypt Euslkt (α) to obtain α and then compute H(α) with-
Step 2 of Three-Party Authentication, slice SIDi sends c2 = out uslkt. On the other hand, the slice randomly chooses β
| (c  | ||κ ||ts1 | )||SIDi | =   | (cid:2)||SIDi |     |     |     |     |     | (H(α)||β) |     |     |     |     | H(β) |
| --- | --------- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | ---- |
Eslk 1 i c 2 to the operator. A cor- and sends Euslkt to the user. If the response
i (cid:2)
rect c can be constructed by using slki only and a fresh from the user is correct, the slice will authenticate the user
2
c (cid:2) c an o n l y be g e n e r at e d in th e c u r re n t s e ss io n ( i. e ., c (cid:2) is (H(α)||β) β
2 2 s i n ce n o n e c an d e c ry p t E u s lk to obtain and then
|     |     |     |     |     |     |     |     | (cid:2) |     |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
n o t a rep l a y ed on e ) . T h e r efo re, in S t e p 3 , a f te r d ecr y p t in g c 2 , c o m pu t e H (β ) w i th o u t u sl k t .
oncetheκ extractedfromthedecryptionresultistheidentity After performing the mutual authentication successfully,
i
|     |     |     |     |     |     |     |     | (cid:2) |     |     |     |     |     | α   | β,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
secret of SIDi and ts1 is fresh, the operator will learn that c 2 user ID and slice SIDt have secretly shared and each
is correct and fresh and thus it will authenticate SIDi. of which has been protected by either encryption or one-
In Step 4 of Three-Party Authentication, the operator way hashing. Therefore, H(α||β) can form as a session key
|     | =   | (Eulk | (slice | (cid:2)||α||β)||κ | ||α||β||ts2 | )   |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ------ | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sends c3 Eslk i to SIDi. between user ID and slice SIDt in this session.
i
| In Step | 5, SIDi | decrypts |     | c3. Similarly, | SIDi | will | authen- |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --- | -------------- | ---- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
κ
| ticate | the operator |          | if the | i extracted | from      | the decryption |        |     |     |     |     |             |     |     |     |
| ------ | ------------ | -------- | ------ | ----------- | --------- | -------------- | ------ | --- | --- | --- | --- | ----------- | --- | --- | --- |
|        |              |          |        |             |           |                |        |     |     |     | VI. | COMPARISONS |     |     |     |
| result | is its       | identity | secret | and ts2     | is fresh. | From the       | above, |     |     |     |     |             |     |     |     |
mutual authentication between SIDi and the operator can be In this section, we show the comparison between the
guaranteed. proposed scheme and Ni et al.’s scheme [15]. Ni et al.’s

710 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
TABLEI
COMPUTATIONCOSTS
TABLEII
| scheme | satisfies | the | 3GPP | standard, | but | it does | not sat- |     |     |     |     |     |
| ------ | --------- | --- | ---- | --------- | --- | ------- | -------- | --- | --- | --- | --- | --- |
NOTATIONS
| isfy some  | 5G       | network     | environment |          | characteristics. |           | The 5G        |     |     |     |     |     |
| ---------- | -------- | ----------- | ----------- | -------- | ---------------- | --------- | ------------- | --- | --- | --- | --- | --- |
| network    | allows   | one device  | to          | have     | at most          | eight     | slices simul- |     |     |     |     |     |
| taneously. | It means | that        | each        | device   | may              | have more | than one      |     |     |     |     |     |
| slice at   | the same | time.       | In Ni       | et al.’s | scheme,          | whenever  | a user        |     |     |     |     |     |
| wants to   | access   | a different | slice,      | it       | will be          | necessary | for the       |     |     |     |     |     |
corenetworktoauthenticatetheuser.Itistime-consumingand
| will be     | getting | worse    | when the        | user | crosses | slices  | frequently. |     |     |     |     |     |
| ----------- | ------- | -------- | --------------- | ---- | ------- | ------- | ----------- | --- | --- | --- | --- | --- |
| We will     | provide | the same | scenario        |      | in both | of the  | schemes for |     |     |     |     |     |
| comparisons | where   | a        | user equipment, |      | network | slices, | and the     |     |     |     |     |     |
operator are included. Since Ni et al.’s scheme is based on TABLEIII
PROPERTYCOMPARISON
| a credential    | system,    | the         | authentication     |         | performance |            | may not      |             |            |         |            |             |
| --------------- | ---------- | ----------- | ------------------ | ------- | ----------- | ---------- | ------------ | ----------- | ---------- | ------- | ---------- | ----------- |
| be as good      | as         | that of     | our scheme         | while   |             | it has the | advantage    |             |            |         |            |             |
| of the storage  |            | of the      | slice information. |         | However,    |            | Ni et al.’s  |             |            |         |            |             |
| scheme          | needs more | computation |                    | cost    | and         | more       | time latency |             |            |         |            |             |
| whenever        | switching  | among       | the                | slices. |             |            |              |             |            |         |            |             |
| A. Performance  |            | Comparison  |                    |         |             |            |              |             |            |         |            |             |
|                 |            |             |                    |         |             |            |              | CPU @3.2GHz | and 8.00GB | memory. | Hence, the | clock cycle |
| The performance |            | comparison  |                    | between |             | Ni et      | al.’s scheme |             |            |         |            |             |
isapproximately0.3125ns.Accordingto[28],[29],[30],[31],
| and our     | scheme | is shown |           | in Table | I and           | some | notations |               |             |                    |           |             |
| ----------- | ------ | -------- | --------- | -------- | --------------- | ---- | --------- | ------------- | ----------- | ------------------ | --------- | ----------- |
|             |        |          |           |          |                 |      |           | wehavethatTe1 | andTe2      | are240timesofTm.Tp |           | is5times    |
| are defined | in     | Table    | II. We    | count    | the computation |      | costs of  |               |             |                    |           |             |
|             |        |          |           |          |                 |      |           | of Te1.       | Th and TAES | are 0.4 times      | of Tm. Ts | is 29 times |
| Ni et al.’s | scheme | by       | measuring |          | the computation |      | cost of   |               |             |                    |           |             |
of Tm.
| each cryptographic |      | primitive |        | used in         | Ni et    | al.’s scheme,  | such  |               |            |     |     |     |
| ------------------ | ---- | --------- | ------ | --------------- | -------- | -------------- | ----- | ------------- | ---------- | --- | --- | --- |
| as Hash,           | ECC, | and AES.  | In     | the Three-Party |          | Authentication |       |               |            |     |     |     |
|                    |      |           |        |                 |          |                |       | B. Properties | Comparison |     |     |     |
| phase and          | the  | Handover  | phase, | Ni              | et al.’s | scheme         | needs | 8             |            |     |     |     |
multiplications,17exponentiations,5pairings,2AESencryp- Based on the discussions in Section III, we compare the
tions, and 8 one-way hash computations in the user side. It proposed scheme with Ni et al.’s in three-party authentication
requires 5 exponentiations, 6 pairings, and 4 one-way hash and handover. Regarding the satisfaction of the TS 33.501
computations in the slice side. And it needs 7 multiplications, standard, both of the proposed scheme and Ni et al.’s scheme
25exponentiations,12pairings,5AESencryptions,and8one- achieveit.Furthermore,ourschemeisbasedonellipticcurves
way hash computations in the operator side. Our three-party andwecancompletetheentireauthenticationwithoutpairing.
authentication needs 1 multiplication, 3 AES encryptions, and It turns out that the time latency of the proposed scheme is
3 one-way hash computations in the user side. And it requires much lower than that of Ni et al.’s. The property comparison
3 AES encryptions and 2 one-way hash computations in the between Ni et al.’s and the proposed scheme is summarized
| sliceside,anditneeds |     |     | 1multiplication,(5+ns)AESencryp- |     |     |     |     | in Table | III. |     |     |     |
| -------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- |
tions, and 1 one-way hash computation in the operator side. Here, we show a practical example to demonstrate the effi-
Theproposedhandoverrequires2AESencryptionsand3one- ciencyoftheproposedscheme.Aswementionedinaprevious
way hash computations in the user side and it needs 3 AES section, the 5G network allows one device to have at most
encryptionsand3one-wayhashcomputationsinthesliceside. eight slices simultaneously. Assume that a user called Bob
According to [27], we have Tm ≈ 66 clock cycles. We exe- has a 5G device such as a smart phone. And this device has
cute the computations on a computer with Intel Core i7-8700 eightsliceslikeSmartHomeusinganeMBBslice,SmartCity

TH
FANetal.:CROSS-NETWORK-SLICEAUTHENTICATIONSCHEMEFOR5 GENERATIONMOBILECOMMUNICATIONSYSTEM 711
latency for 5G communication. Further, it showed an effi-
cient handover mechanism where IoT devices need to switch
network slices based on the requirement. The security of the
proposed scheme is based on the security of public-key cryp-
tosystems, symmetric encryptions, and one-way hashing. It
is immune to replay attacks under the protection from the
challenge-response mechanism and the timestamp approach.
Theperformanceoftheproposedschemeismeasuredbasedon
theoverheadsofdifferentcryptographicoperations.Moreover,
it is found that the proposed scheme is better than Ni et al.’s
scheme in terms of the computation cost and the latency.
We will look for relevant open-source software and plan to
implement the proposed scheme in our future work.
Fig.8. TimeLatencyintheUserSide. ACKNOWLEDGMENT
The authors would like to thank Prof. Arijit Karati for his
valuable comments on the paper.
REFERENCES
[1] “IMTvision—Frameworkandoverallobjectivesofthefuturedevelop-
mentofIMTfor2020andbeyond,”Int.Telecommun.Union,Geneva,
Switzerland,ITU-RecommendationM.2083,Sep.2015.
[2] I.-G. P. Group, “5G concept,” IMT-2020(5G) Promotion
Group, Beijing, China, Rep., Feb. 2015. [Online]. Available:
http://www.imt2020.org.cn/en/documents/3
[3] “Security challenges and opportunities for 5G mobile networks,”
NOKIA, Espoo, Finland, Rep., 2017. [Online]. Available: https://
onestore.nokia.com/asset/201049?_ga=2.41812066.1968491423.161172
2503-172889078.1611722503
[4] “5Gsecurity:Scenariosandsolutions,”Erricsson,Stockholm,Sweden,
Rep., 2017. [Online]. Available: https://www.ericsson.com/en/reports-
and-papers/white-papers/5g-security—enabling-a-trustworthy-5g-system
[5] SystemArchitectureforthe5GSystem,3GPPStandardTS23.501,2017.
Fig.9. TimeLatencyintheSlicesSide. [6] Numbering, Addressing and Identification, 3GPP Standard TS 23.003,
2020.
[7] SecurityArchitectureandProceduresfor5GSystem,3GPPStandardTS
33.501,2018.
using an MMTC slice, and Self-Driving Car using a uRLLC [8] S. Behrad, “Slice specific authentication and access control for 5G,”
slice. When Bob works at home or plays a game, he will Ph.D. dissertation, Dept. Comput. Sci. Netw., Inst. Polytechnique de
Paris,Palaiseau,France,2020.
need one slice in this situation. When Bob wants to control
[9] P. K. Panda and S. Chattopadhyay, “An improved authentication and
some IoT devices like lights or air conditioners in his Smart securityschemeforLTE/LTE-Anetworks,”J.AmbientIntell.Humanized
Home, he will need another slice to control them. After Bob Comput.,vol.11,no.5,pp.2163–2185,2020.
[10] R.Ma,J.Cao,D.Feng,H.Li,Y.Zhang,andX.Lv,“PPSHA:Privacy
finishes his work and he wants to watch an AR/VR video, he
preserving secure handover authentication scheme for all application
requires another eMBB slice again. At last, he wants to go scenarios in LTE-A networks,” Ad Hoc Netw., vol. 87, pp.49–60,
outside and takes a Self-Driving Car. He will need a uRLLC May2019.
[11] J. Zhou, M. Ma, and S. Sun, “A hybrid authentication protocol for
slice to achieve ultra-low latency. In the above example, Bob
LTE/LTE-Anetwork,”IEEEAccess,vol.7,pp.28319–28333,2019.
are accessing several slices and switching among his slices [12] B.L.Parne,S.Gupta,andN.S.Chaudhari,“PSE-AKA:Performance
frequently. We illustrate the comparisons on the latency time and security enhanced authentication key agreement protocol for IoT
enabledLTE/LTE-Anetworks,”Peer-to-PeerNetw.Appl.,vol.12,no.5,
regarding the user side in Fig. 8 and the slices side in Fig. 9
pp.1156–1177,2019.
to demonstrate how fast the proposed scheme will be as com- [13] D.Basin,J.Dreier,L.Hirschi,S.Radomirovic,R.Sasse,andV.Stettler,
pared with Ni et al.’s scheme in a sequence of handovers. “Aformalanalysisof5Gauthentication,”inProc.ACMSIGSACConf.
Comput.Commun.Security,2018,pp.1383–1396.
Sinceinthe5Genvironment,three-partyauthenticationisexe-
[14] (Jul. 17, 2019). An Overview of the 3GPP 5G Security Standard.
cuted one time; however, handover will be executed lots of [Online]. Available: https://www.ericsson.com/en/blog/2019/7/3gpp-5g-
times when a device wants to switch among the slices. security-overview
[15] J. Ni, X. Lin, and X. S. Shen, “Efficient and secure service-oriented
authenticationsupportingnetworkslicingfor5G-enabledIoT,”IEEEJ.
Sel.AreasCommun.,vol.36,no.3,pp.644–657,Mar.2018.
VII. CONCLUSION [16] S.Behrad,E.Bertin,andN.Crespi,AuthenticationandAccessControl
for5G.Hoboken,NJ,USA:Wiley,May2020,pp.1–19.
This article demonstrated a new authentication technique
[17] S.Behrad,S.Tuffin,E.Bertin,andN.Crespi,“Networkaccesscontrol
suitable for effective communication in the 5G network. for the IoT: A comparison between cellular, Wi-Fi and LoRaWAN,”
The scheme is based on the concept of the elliptic curve inProc.22ndConf.Innovat.CloudsInternetNetw.Workshops(ICIN),
2019,pp.195–200.
integrated encryption strategy. It leverages the functionali-
[18] “Studyofsecurityaspectsofthenextgenerationsystem,”3GPP,Sophia
ties of the edge cloud and the center cloud to reduce the Antipolis,France,Rep.33.899,2017.

712 IEEETRANSACTIONSONNETWORKANDSERVICEMANAGEMENT,VOL.18,NO.1,MARCH2021
[19] H. Khan and K. M. Martin, “On the efficacy of new privacy attacks Yu-Tse Shih was born in Taichung. He is cur-
against5GAKA,”inProc.ICETE,2019,pp.431–438. rently pursuing the Doctorate degree in com-
[20] R. P. Jover, “The current state of affairs in 5G security and puter science and engineering with National
the main remaining security challenges,” 2019. [Online]. Available: Sun Yet-sen University, Kaohsiung, Taiwan. His
arXiv:1904.08394. research interests include communication security,
[21] P. Schneider and G. Horn, “Towards 5G security,” in Proc. IEEE informationsecurity,appliedcryptography,andbio-
Trustcom/BigDataSE/ISPA,vol.1,2015,pp.1165–1170. metricauthentication.
| [22] C. S. | Näslund,                                                     | P.           | Ståhl, | I. Innov, | G. Correndo, |              | V. Krivcovs, |           |     |     |     |     |     |     |     |
| ---------- | ------------------------------------------------------------ | ------------ | ------ | --------- | ------------ | ------------ | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| and        | S. Philips,                                                  | “Deliverable |        | D2.7      | security     | architecture |              | (final),” |     |     |     |     |     |     |     |
| [Online].  | Available:https://5gensure.eu/sites/default/files/5G-ENSURE_ |              |        |           |              |              |              |           |     |     |     |     |     |     |     |
D2.7_SecurityArchitectureFinal.pdf
[23] C.Lai,H.Li,R.Lu,andX.S.Shen,“SE-AKA:Asecureandefficient
| group | authentication |     | and key | agreement | protocol | for | LTE networks,” |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ------- | --------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Comput.Netw.,vol.57,no.17,pp.3492–3510,2013.
| [24] W.-T. | Su, W.-M. | Wong, | and | W.-C. Chen, | “A  | survey | of performance |     |     |     |     |     |     |     |     |
| ---------- | --------- | ----- | --- | ----------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
improvementbygroup-basedauthenticationinIoT,”inProc.Int.Conf.
Appl.Syst.Innovat.(ICASI),2016,pp.1–4.
[25] R.GiustolisiandC.Gerhmann,“Threatsto5Ggroup-basedauthentica-
tion,”inProc.13thInt.Conf.SecurityCryptogr.(SECRYPT),Jul.2016,
pp.360–367.
| [26] V. Shoup, | “A  | proposal | for an | ISO standard | for | public | key encryption |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------ | ------------ | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(version2.1),”IACRe-PrintArchive,vol.112,pp.1–56.Dec.2001. Jheng-Jia Huang wasborninKaohsiung,Taiwan.
[27] R. L. A. Mrabet and N. El-Mrabet, “A systolic hardware He received the M.S. degree in information man-
architectures of montgomery modular multiplication for public agement from National Kaohsiung First University
key cryptosystems,” Cryptol. ePrint Archive, Int. Assoc. Cryptol. of Science and Technology, Kaohsiung, in 2012,
andthePh.D.degreeincomputerscienceandengi-
| Res., | Lyon, | France, | Rep. | 2016/487, | 2016, | [Online]. | Available: |     |     |     |     |     |     |     |     |
| ----- | ----- | ------- | ---- | --------- | ----- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://eprint.iacr.org/2016/487 neering from the National Sun Yat-sen University,
[28] N. Koblitz, A. Menezes, and S. Vanstone, “The state of elliptic Kaohsiung, in 2019. From 2019 to 2020, he has
curve cryptography,” Designs Codes Cryptogr., vol. 19, pp.173–193, beenaDirectoroftheInfoComSecurityDivision,a
| Mar.2000.  |          |       |           |     |          |           |          |     |     | Quality | Control/Quality |          | Assurance          | Supervisor, | and |
| ---------- | -------- | ----- | --------- | --- | -------- | --------- | -------- | --- | --- | ------- | --------------- | -------- | ------------------ | ----------- | --- |
|            |          |       |           |     |          |           |          |     |     | the     | Chief           | Security | Officer of Telecom | Technology  |     |
| [29] A. J. | Menezes, | S. A. | Vanstone, | and | P. C. V. | Oorschot, | Handbook | of  |     |         |                 |          |                    |             |     |
AppliedCryptography.BocaRaton,FL,USA:CRCPress,2001. Center, Kaohsiung. In 2020, he joined the faculty
[30] M.Scott,“Implementingcryptographicpairings,”inProc.Pairing-Based withtheDepartmentofInformationManagement,NationalTaiwanUniversity
Cryptogr.,2007,pp.177–196. ofScienceandTechnology,Taipei,Taiwan.HealsoistheDeputySecretary
[31] Y. Zhang, W. Liu, W. Lou, and Y. Fang, “Securing mobile ad hoc General of the Chinese Cryptology and Information Security Association.
|          |      |                 |     |        |             |        |            | His current | research | interests | include | cloud | computing and | security, | social |
| -------- | ---- | --------------- | --- | ------ | ----------- | ------ | ---------- | ----------- | -------- | --------- | ------- | ----- | ------------- | --------- | ------ |
| networks | with | certificateless |     | public | keys,” IEEE | Trans. | Dependable |             |          |           |         |       |               |           |        |
SecureComput.,vol.3,no.4,pp.386–399,Oct./Dec.2006. network security and authentication, network and communication security,
|     |     |     |     |     |     |     |     | information | security, | and applied |        | cryptography. | He won            | the Phi | Tau Phi |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----------- | ------ | ------------- | ----------------- | ------- | ------- |
|     |     |     |     |     |     |     |     | Award and   | the Best  | Ph.D.       | Thesis | Award         | from the National | Sun     | Yat-sen |
Universityin2019,theBestPh.D.ThesisAwardfromtheTaiwanAssociation
|     |     |        |     |          |     |      |           | for Web Intelligence |             | Consortium |          | and the | Taiwan Institute | of     | Electrical |
| --- | --- | ------ | --- | -------- | --- | ---- | --------- | -------------------- | ----------- | ---------- | -------- | ------- | ---------------- | ------ | ---------- |
|     |     |        |     |          |     |      |           | and Electronic       | Engineering |            | in 2019, | and     | the Best Ph.D.   | Thesis | Award      |
|     |     | Chun-I | Fan | received | the | M.S. | degree in | com-                 |             |            |          |         |                  |        |            |
puter science and information engineering from from the Taiwan Association of Cloud Computing, the Chinese Cryptology
National Chiao Tung University, Hsinchu, Taiwan, and Information Security Association, and the Institute of Information &
ComputingMachineryin2020.
|     |     | in      | 1993, and         | the        | Ph.D. degree  | in          | electrical | engi-   |     |     |     |     |     |     |     |
| --- | --- | ------- | ----------------- | ---------- | ------------- | ----------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | neering | from              | National   | Taiwan        | University, |            | Taipei, |     |     |     |     |     |     |     |
|     |     | Taiwan, | in                | 1998.      | From 1999     | to          | 2003,      | he was  |     |     |     |     |     |     |     |
|     |     | an      | Associate         | Researcher |               | and a       | Project    | Leader  |     |     |     |     |     |     |     |
|     |     | with    | Telecommunication |            | Laboratories, |             | Chunghwa   |         |     |     |     |     |     |     |     |
TelecomCompany,Ltd.,Taoyuan,Taiwan.In2003,
|                    |            | he       | joined        | as a faculty | with             | the         | Department | of      |     |     |     |     |     |     |     |
| ------------------ | ---------- | -------- | ------------- | ------------ | ---------------- | ----------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|                    |            | Computer |               | Science      | and Engineering, |             | National   | Sun     |     |     |     |     |     |     |     |
| Yat-sen University |            | (NSYSU), | Kaohsiung,    |              | Taiwan.          | He has      | been       | a Full  |     |     |     |     |     |     |     |
| Professor          | since 2010 | and a    | Distinguished | Professor    |                  | since 2019. | He         | also is |     |     |     |     |     |     |     |
theDeanofCollegeofEngineeringandtheDirectorofInformationSecurity
| Research   | Center at     | NSYSU, | and | he was | the CEO      | of “Aim | for the     | Top  |     |     |     |     |     |     |     |
| ---------- | ------------- | ------ | --- | ------ | ------------ | ------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| University | Plan” Office, | NSYSU. | And | he     | is currently | an      | outstanding | fac- |     |     |     |     |     |     |     |
ultyinAcademicResearchinNSYSU.Hiscurrentresearchinterestsinclude
| applied cryptology, |     | information | security, | and | communication |     | security. | He  |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --------- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Wan-RuChiuwasborninChanghuaCity,Taiwan.
| received the | Best     | Student  | Paper Awards | from       | the          | National  | Conference     | on   |     |         |          |             |                  |     |          |
| ------------ | -------- | -------- | ------------ | ---------- | ------------ | --------- | -------------- | ---- | --- | ------- | -------- | ----------- | ---------------- | --- | -------- |
|              |          |          |              |            |              |           |                |      |     | She     | received | the         | master’s degrees | in  | computer |
| Information  | Security | in 1998, | the          | Dragon     | Ph.D. Thesis | Award     | from           | Acer |     |         |          |             |                  |     |          |
|              |          |          |              |            |              |           |                |      |     | science | and      | engineering | from National    |     | Sun Yat- |
| Foundation,  | the Best | Ph.D.    | Thesis       | Award from | the          | Institute | of Information |      |     |         |          |             |                  |     |          |
and Computing Machinery in 1999, and the Y. Z. Hsu Science Paper sen University, Kaohsiung, Taiwan, in 2018. Her
|                                           |     |     |     |     |                        |     |     |     |     | research | interests |     | include communication |     | security, |
| ----------------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | -------- | --------- | --- | --------------------- | --- | --------- |
| Award (InformationandCommunicationScience |     |     |     |     | andTechnologyCategory) |     |     |     |     |          |           |     |                       |     |           |
cloudcomputing,networksecurity,andinformation
| in 2020. He | won | the Engineering | Professors |     | Award | from Chinese | Institute |     |     |     |     |     |     |     |     |
| ----------- | --- | --------------- | ---------- | --- | ----- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
security.
| of Engineers—Kaohsiung |     | Chapter |     | in 2016, | and the | Outstanding | Technical |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ------- | --- | -------- | ------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
AchievementAwardfromIEEETainanSectionin2020.HeistheChairman
| of Chinese | Cryptology | and | Information | Security | Association, |     | and was | the |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ----------- | -------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ChiefExecutiveOfficerofTelecomTechnologyCenterinTaiwan.