# Toward Software-Defined Networking-Based IoT Frameworks A Systematic Literature Review Taxonomy Open Challenges and Pr

> Source file: `Toward Software-Defined Networking-Based IoT Frameworks A Systematic Literature Review Taxonomy Open Challenges and Pr.pdf`

---

Received4June2022,accepted28June2022,dateofpublication4July2022,dateofcurrentversion11July2022.
DigitalObjectIdentifier10.1109/ACCESS.2022.3188311
Toward Software-Defined Networking-Based IoT
Frameworks: A Systematic Literature Review,
Taxonomy, Open Challenges and Prospects
SHAHBAZSIDDIQUI1,SUFIANHAMEED 1,SYEDATTIQUESHAH 2,(Member,IEEE),
IJAZAHMAD 3,(Member,IEEE),ADELANEIBA 2,(Member,IEEE),
DIRKDRAHEIM 4,(Member,IEEE),ANDSCHAHRAMDUSTDAR 5,(Fellow,IEEE)
1DepartmentofComputerScience,NUCES,Karachi75160,Pakistan
2SchoolofComputingandDigitalTechnology,BirminghamCityUniversity,BirminghamB47XG,U.K.
3VTTTechnicalResearchCentreofFinland,02044Espoo,Finland
4InformationSystemsGroup,TallinnUniversityofTechnology,12618Tallinn,Estonia
5DistributedSystemsGroup,ViennaUniversityofTechnology,1040Vienna,Austria
Correspondingauthor:SyedAttiqueShah(syed.shah2@bcu.ac.uk)
ABSTRACT InternetofThings(IoT)ischaracterizedasoneoftheleadingactorsforthenextevolutionary
stageinthecomputingworld.IoT-basedapplicationshavealreadyproducedaplethoraofnovelservicesand
areimprovingthelivingstandardbyenablinginnovativeandsmartsolutions.However,alongwithitsrapid
adoption,IoTtechnologyalsocreatescomplexchallengesregardingthemanagementofIoTnetworksdue
toitsresourcelimitations(computationalpower,energy,andsecurity).Hence,itisurgentlyneededtorefine
theIoT-basedapplication’sarchitecturestorobustlymanagetheoverallIoTinfrastructure.Software-defined
networking (SDN) has emerged as a paradigm that offers software-based controllers to manage hardware
infrastructureandtrafficflowonanetworkeffectively.SDNarchitecturehasthepotentialtoprovideefficient
and reliable IoT network management. This research provides a comprehensive survey investigating the
publishedstudiesonSDN-basedframeworkstoaddressIoTmanagementissuesinthedimensionsoffault
tolerance, energy management, scalability, load balancing, and security service provisioning within the
IoT networks. We conducted a Systematic Literature Review (SLR) on the research studies (published
from 2010 to 2022) focusing on SDN-based IoT management frameworks. We provide an extensive
discussion on various aspects of SDN-based IoT solutions and architectures. We elaborate a taxonomy of
theexistingSDN-basedIoTframeworksandsolutionsbyclassifyingthemintocategoriessuchasnetwork
functionvirtualization,middleware,OpenFlowadaptation,andblockchain-basedmanagement.Wepresent
theresearchgapsbyidentifyingandanalyzingthekeyarchitecturalrequirementsandmanagementissues
inIoTinfrastructures.Finally,wehighlightvariouschallengesandarangeofpromisingopportunitiesfor
future research to provide a roadmap for addressing the weaknesses and identifying the benefits from the
potentialsofferedbySDN-basedIoTsolutions.
INDEXTERMS InternetofThings(IoT),software-definednetworking(SDN),SDN-basedIoTmanagement
frameworks, systematic literature review, network function virtualization, OpenFlow, middleware,
blockchain,securitymanagement,faulttolerance,loadbalancing,scalability,energymanagement.
I. INTRODUCTION communicationtechnology.ThetermIoThasemergedfrom
The Internet of Things (IoT) is one of the most popular connecting embedded objects/things to the Internet. IoT
innovations in the current paradigm of information and infrastructure consists of data, sensing objects, computing,
andcommunicationstoformaglobalanddynamicnetwork
The associate editor coordinating the review of this manuscript and infrastructure[1].AcollectionofsmartdevicessuchasRadio
approvingitforpublicationwasFiroozB.Saghezchi . FrequencyIdentification(RFID)tags,sensors,smartphones,
70850 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
wearabledevices,etc.,areinterconnectedandcanbeusedas
datacollectionanddisseminationpoints.Researchersforesee
afuturewhereIoTdevicesinlargenumberswillbedeployed
| around  | us and    | will generate |             | enormous |     | amounts | of data  |     |     |     |     |     |
| ------- | --------- | ------------- | ----------- | -------- | --- | ------- | -------- | --- | --- | --- | --- | --- |
| without | requiring | the active    | involvement |          | of  | users   | [2]. The |     |     |     |     |     |
generateddatasetswillbecollected,analyzed,andreported
| in an understandable |       |            | form     | for various |         | applications | [3].       |     |     |     |     |     |
| -------------------- | ----- | ---------- | -------- | ----------- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- |
| Yet, the             | field | of IoT is  | about    | to create   | more    | attraction   | to         |     |     |     |     |     |
| researchers          | in    | the coming | years    | due         | to the  | emergence    | of         |     |     |     |     |     |
| new application      |       | areas      | that can | further     | improve |              | our living |     |     |     |     |     |
standards[4].
| The            | application | domains  |                | of IoT   | range       | from   | leisure     |     |     |     |     |     |
| -------------- | ----------- | -------- | -------------- | -------- | ----------- | ------ | ----------- | --- | --- | --- | --- | --- |
| and sports     | such        | as smart |                | activity | monitors,   |        | to critical |     |     |     |     |     |
| infrastructure |             | such as  | manufacturing, |          | healthcare, |        | smart       |     |     |     |     |     |
| grids, and     | smart       | cities.  | The            | driving  | forces      | behind | these       |     |     |     |     |     |
applicationsincludethedevelopmentinsensortechnologies,
mobiledevices,cloudinfrastructures,andaccesstechnology
providers, to name a few. The result is that huge volumes FIGURE1. AgeneralillustrationofSDN-basedIoTarchitecture.
| of IoT | generated | data | containing | real-world |     | sensor-based |     |     |     |     |     |     |
| ------ | --------- | ---- | ---------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
information has dramatically expanded the demand for of the network state enabling it to monitor, prioritize
computing and storage resources for the IoT ecosystems and de-prioritize network traffic through programmable
to provide useful information or services [5]. In the IoT Application Programming Interfaces (APIs) from a central
|     |     |     |     |     |     |     |     | vintage | point. Therefore, | SDN has been adopted |     | as one of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | -------------------- | --- | --------- |
ecosystems,real-timeprocessingistheprimaryrequirement.
In groups of several hundred, thousands, or even millions, themainnetworkmanagementframeworkforIoTnetworks
IoTsystemscantheoreticallyhandleparallelrequests,which [10], [11]. SDN aims to make the network architecture
is required by several types of applications that need quick more agile, flexible, and smart that can dynamically adopt
responses[6]. to run-time changes in the network environment [11], [12].
|            |     |             |     |     |         |         |      | Since an | IoT network is | highly dynamic | mainly | due to its |
| ---------- | --- | ----------- | --- | --- | ------- | ------- | ---- | -------- | -------------- | -------------- | ------ | ---------- |
| Successful |     | deployments | of  | IoT | require | merging | het- |          |                |                |        |            |
erogeneous communication infrastructures, which involves resource constraints such as battery and processing power,
integrating smart gateways to link IoT devices with the and storage capability, the network has to adopt to its
Internet. Lately, research efforts are leading towards inter- unique requirements. Such agility can be achieved through
connecting the IoT infrastructure with technologies such as programmable network APIs in SDN, which makes SDN
themostfavorablenetworkingarchitecture[13]–[18].Fig.1
| cloud computing, |     | edge/ | fog computing, |     | big | data | analytics, |     |     |     |     |     |
| ---------------- | --- | ----- | -------------- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
machine learning, etc., that complement the potential of showsatypicalSDN-basedIoTarchitecture.
IoT.Furthermore,theever-evolvingIoTtechnologyrequires Since the SDN framework greatly facilitates the man-
|     |     |     |     |     |     |     |     | agement | of IoT networks, | substantial research |     | efforts are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | -------------------- | --- | ----------- |
ubiquitousconnectivitytobillionsofheterogeneousdevices
such assensors, cameras,RFID devices, etc.[7]. Theresult dedicatedinthisdirection.Severalstudieshavebeencarried
outtoinvestigatedifferentIoTreferencearchitecturemodels
| is that IoT | networks | are | growing | enormously |     | in  | size, and |     |     |     |     |     |
| ----------- | -------- | --- | ------- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- |
highly complicated due to the heterogeneity of device, based on SDN for current and potential IoT deployments.
access networks and protocols. Therefore, the IoT network Therefore, in this article we survey the existing research
efforts,fingerprinttheresearchgaps,andshedlightonhow
managementhasbecomeanextremelydifficultchallenge[8],
and the challenge will be further exacerbated in networks toovercometheexistingchallengesinthisdirection.Wehave
beyond 5G, i.e., 6G, due to the humongous growth of systematically reviewed various SDN frameworks proposed
connecteddevices.Thesechallengeshaveledresearchersto for the IoT ecosystem. Moreover, we have included the
propose novel IoT management solutions, for instance, for publishedframeworksandhaveevaluatedtheseframeworks
|     |     |     |     |     |     |     |     | to assess | how they stack | up in solving critical | IoT | manage- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ---------------------- | --- | ------- |
loadbalancing,energymanagement,security,scalability,and
faulttolerance[9]. ment challenges in terms of provision of security services,
Software-defined networking (SDN), considered as a fault tolerance, management of energy, load balancing,
breakthrough in communication networks, offers solutions and scalability. In the following subsections, we present
to the management challenges of IoT. SDN simplifies the motivation behind this study, the related surveys published
|     |     |     |     |     |     |     |     | in the existing | literature | and the main contributions |     | of this |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | -------------------------- | --- | ------- |
networkmanagementbyseparatingthenetworkcontrolfrom
the data forwarding elements, and logically centralizing it survey.Table1describestheacronymsusedinthisresearch.
| to high-end | servers. | Thus, | the | SDN | framework | proposes | a   |     |     |     |     |     |
| ----------- | -------- | ----- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- |
three tier approach having an application plane, a control A. MOTIVATION
plane, and a data forwarding plane. The control plane, This survey is motivated by the realization that SDN tends
also called the SDN controller, maintains a global visibility to be a feasible alternative for IoT network architectures
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     | 70851 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE1. Listofacronyms. ThecombinationofIoTandSDN(SDIoT)aimstoconnect
objectsovertheinternetbydecouplingthecontrolplaneand
|     |     |     |     | the data     | plane. In the     | future, we         | envision        | that number    | of     |
| --- | --- | --- | --- | ------------ | ----------------- | ------------------ | --------------- | -------------- | ------ |
|     |     |     |     | connected    | devices in        | IoT networks       | is in billions, | and            | their  |
|     |     |     |     | management   | and control       | is a dynamic       | task            | that is        | a huge |
|     |     |     |     | challenge    | for IoT networks. | Without            | disturbing      | the            | basic  |
|     |     |     |     | architecture | of existing       | implementations,   |                 | SDN can        | render |
|     |     |     |     | the IoT      | network scalable  | and                | programmable    | and provide    |        |
|     |     |     |     | potential    | solutions         | for the emphasized |                 | IoT management |        |
issues.
|     |     |     |     | Recently, | management | for IoT | networks | has received |     |
| --- | --- | --- | --- | --------- | ---------- | ------- | -------- | ------------ | --- |
attentionastheyaredifferentfromthetraditionalnetworks,
|     |     |     |     | which makes | the conventional |     | techniques | and architecture |     |
| --- | --- | --- | --- | ----------- | ---------------- | --- | ---------- | ---------------- | --- |
inapplicableinthedomainofIoT.TheIoTnetworkprotocols
|     |     |     |     | and their | legacy architecture | have     | not been  | built to accom-  |     |
| --- | --- | --- | --- | --------- | ------------------- | -------- | --------- | ---------------- | --- |
|     |     |     |     | modate    | a large amount      | of data, | mobility, | and scalability. |     |
Therearesomedrawbackstotheoperationandmanagement
|     |     |     |     | of these      | heterogeneous   | linked          | devices,       | which produce | a   |
| --- | --- | --- | --- | ------------- | --------------- | --------------- | -------------- | ------------- | --- |
|     |     |     |     | massive       | amount of data. | This rise       | in SDN         | adaptability  | has |
|     |     |     |     | lead the      | initiative to   | use the         | same technique | to manage     |     |
|     |     |     |     | IoT networks. | Most            | recently, there | are numerous   | efforts       | to  |
|     |     |     |     | utilize the   | potentials      | of the SDN      | paradigm       | to manage     | IoT |
networks.Severalstudieshavebeencarriedouttoidentifythe
IoTreferencearchitecturemodelsbasedonSDNforcurrent
|     |     |     |     | and potential  | IoT deployments. |             | The motivation | behind       | our |
| --- | --- | --- | --- | -------------- | ---------------- | ----------- | -------------- | ------------ | --- |
|     |     |     |     | effort is      | to extensively   | review      | these existing | SDN-based    |     |
|     |     |     |     | IoT management | frameworks       |             | for exploring  | the unreaped |     |
|     |     |     |     | opportunities  | and possible     | challenges. | This           | survey aims  | to  |
contributetotheknowledgeofthedesignandimplementation
ofSDN-basedIoTmanagementframeworksandsolutionfor
variousapplications.
B. EXISTINGSURVEYS
|     |     |     |     | A number      | of surveys     | have been     | conducted    | during the   | last   |
| --- | --- | --- | --- | ------------- | -------------- | ------------- | ------------ | ------------ | ------ |
|     |     |     |     | few years     | that broadly   | focus         | on various   | aspects      | of the |
|     |     |     |     | IoT ecosystem | using          | SDN. Table-2  | shows        | a comparison |        |
|     |     |     |     | between       | the existing   | research      | surveys on   | SDN based    | IoT    |
|     |     |     |     | management    | issues         | of IoT. Apart | from these,  | a handful    | of     |
|     |     |     |     | research      | surveys have   | addressed     | the combined | perspective  |        |
|     |     |     |     | of SDN-based  | IoT frameworks |               | along with   | a few of     | their  |
managementissues[62]–[64],moreover,somesurveysfocus
|     |     |     |     | on only | individual aspects | of  | SDN-based | IoT [65], | [66]. |
| --- | --- | --- | --- | ------- | ------------------ | --- | --------- | --------- | ----- |
Giventhatmostoftheseexistingsurveysomitcriticalaspects
|     |     |     |     | and challenges | of SDN-based | IoT, | hence, | to the best | of our |
| --- | --- | --- | --- | -------------- | ------------ | ---- | ------ | ----------- | ------ |
knowledge,nosurveyhasyetfocusedpurelyonSDN-based
|     |     |     |     | IoT frameworks | keeping    | in view            | their management |                 | issues, |
| --- | --- | --- | --- | -------------- | ---------- | ------------------ | ---------------- | --------------- | ------- |
|     |     |     |     | i.e., fault    | tolerance, | energy management, |                  | load balancing, |         |
that enables optimization of the network and opens the security management, and scalability, provided that the
possibility of developing new networks with more practical integrationofSDNanditsevolvingmanagementchallenges
applications towards network management requirements. is a novel paradigm requiring high importance. In the
Although the notion of IoT-focused applications paints a followingsubsections,weillustratetheexistingworkineach
beautiful picture of connected things with various applica- oftheidentifiedSDN-basedIoTmanagementissues.
| tions, however, | it does not come | without a series | of unique |     |     |     |     |     |     |
| --------------- | ---------------- | ---------------- | --------- | --- | --- | --- | --- | --- | --- |
challenges. For IoT to become ubiquitous in industry and 1) FAULTTOLERANCE
our everyday lives, these crucial challenges need to be In IoT networks, particularly in large-scale networks, it is
tackled. theoretically impossible to operate when facing networking
| 70852 |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE2. AcomparisonofexistingsurveysonIoTframeworksusingSDN.
and other failures. Due to the SDN programmability, the 2) ENERGYMANAGEMENT
network mechanism could be configured efficiently to SDN offers a better solution for green networking, which
| attain fault | tolerance and | maintain | the IoT | networks on a |     |     |     |     |
| ------------ | ------------- | -------- | ------- | ------------- | --- | --- | --- | --- |
hasbecomeessentialinnetworkdesignandimplementation
large scale during failure [67]. In [68], Yu et al. present for economic and environmental benefits [70]. It should
a detailed and systematic understanding and review of be noted that, when introduced, security implementations
SDN reliability issues. It began with an introduction of in IoT increase energy consumption since security systems
SDN functionality, taking into account its current state enactcomputationsandcommunicationsthatconsumemore
| of growth | and offering | an overview | of SDN | fault man- |          |                   |               |               |
| --------- | ------------ | ----------- | ------ | ---------- | -------- | ----------------- | ------------- | ------------- |
|           |              |             |        |            | power in | the network [49], | [71]. In [25] | and [39], the |
agement solutions’ two-dimensional taxonomy. In [63], authors address SDN/NFV-based security approaches. They
Salman et al. in their survey critically analyze the solutions alsohighlightedseveraladvantagesinscalability,on-demand
focused on SDN and fog computing to address IoT’s network programmability, energy efficiency, and mobility.
key challenges in terms of fault-tolerant and scalability They also describes existing open SDN and NFV-related
| by highlighting | the benefits | and | limitations | of selected |     |     |     |     |
| --------------- | ------------ | --- | ----------- | ----------- | --- | --- | --- | --- |
challengesforIoTsecurity.
frameworks.In[69],Wangetal.discussthetechniquesthat
accommodate benign faults and identify blockchain-based 3) LOADBALANCING
| systems in | which a fault-tolerant |     | service replicates | servers |         |                      |         |                    |
| ---------- | ---------------------- | --- | ------------------ | ------- | ------- | -------------------- | ------- | ------------------ |
|            |                        |     |                    |         | In SDN, | the controller views | network | resources globally |
andcoordinatesclientinteractionswiththeaidofSDNflow combined with load optimization and applications’ knowl-
tables.
|               |     |     |     |     | edge requirements. | This | approach makes | SDN ideal to |
| ------------- | --- | --- | --- | --- | ------------------ | ---- | -------------- | ------------ |
| VOLUME10,2022 |     |     |     |     |                    |      |                | 70853        |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
perform load balancing activities effectively and provides analyze all relevant evidence on a focused topic or research
newpossibilitiesinIoTnetworksforloadbalancingtoboost questions [80]. With the help of a predefined protocol, the
the technology balance [72]. Also, to boost IoT network SLRmethodselectsandeliminatesreferencesandtests,and,
performanceinmultipleconsciousroutingapproaches,load ultimately, findings are synthesized by assessing specific
balancing technology is critical for the SDN networks. It is studies and a clear proof of test questions. The main
also used to systematically distribute the network’s load contributionsofthissurveyarefourfoldasfollowing:
to improve network capacity and quality of service (QoS). 1) AnSLRisconductedthatprovidesanextensivereview
Therefore,withloadbalancingtechnology,theIoTnetwork’s ofexistingSDN-basedIoT(SDIoT)managementframe-
overallefficiencycanbesignificantlyimproved[71],[73]. workspublishedinreputablejournalsandconferences.
2) Atailoredtaxonomyisdevisedtocategorizetherelated
4) SECURITYMANAGEMENT SDIoT solutions and a detailed discussion of each
SDN was initially implemented to simplify the network architecture is provided for better understanding of the
configuration efforts in order to boost overall network currentchallenges.
performance,however,laterSDNwasfoundtobeapplicable 3) The existing state-of-the-art SDN-based IoT manage-
tonetworksecurity[74]–[76].IoTnetworksarevulnerableto mentframeworksandsolutionsareclassifiedandfurther
numerous security threats, some of which can not easily be investigatedaccordingtothefollowingcategories:
identified. SDN is an evolving technology that can provide i) Network Function Virtualization-based manage-
security protection solutions, because it is able to detect ment
threats and respond faster than conventional networks, and ii) Middleware-basedmanagement
allofthisinanadaptivemanner[74],[77]. iii) OpenFlow adaptation based management frame-
work
5) SCALABILITY iv) Blockchain-basedmanagement
Due to the continuous changes in IoT networks, the focus 4) Every IoT management framework discussed in this
needs to be renewed on security and privacy regarding data paper has been analyzed with respect to its support of
andusers.Blockchaintechnologyhasemergedasacandidate fault tolerance, security management, energy manage-
for computerized transaction-based communications. The ment,loadbalancingandscalabiltiy.
integration of IoT and blockchain technology offers various 5) A set of critical research gaps that needs further
potential solutions in regards to scalability issues of IoT. investigation and research attention are identified to
Biwasetal.[78] highlighted various scalability issues and manageIoTnetworksmoreeffectively.
proposedtheLpeernetworkframeworkbasedonblockchain. 6) Rising challenges and potential opportunities are high-
Theresultsobtainedfromtheirimplementationprovethata lighted to provide a road-map for future research
scalable solution for IoT is applicable. In [37], the authors directionstoaddresstheweaknessesofSDIoTsolutions.
conducted a systematic review on blockchain’s operations To the best of our knowledge, this is the first extensive
and classified their work into layers approach to highlight survey of its kind to review all the current publications
the blockchain-based solutions to the scalability issues in for SDN-based IoT solutions in terms of the full range of
IoT. IoTimplementationframework’smanagementissues.Fig.2
shows the derived taxonomy of existing studies categorized
C. SCOPEOFTHISSURVEYANDCONTRIBUTIONS inaccordancewithvariousSDIoTmanagementframeworks.
Inthissurveypaper,wehavesystematicallyreviewedvarious
SDN frameworks proposed for the IoT ecosystems with D. ORGANIZATIONOFTHEPAPER
respecttovariousmanagementissues.Wehaveincludedpub- TheoverallstructureofthissurveypaperisshowninFig.3.
lished frameworks and have evaluated these frameworks to Section II presents background knowledge of SDN and
assesshowtheystackupinsolvingcriticalIoTmanagement its working principles. Section III outlines the details for
problems in terms of provision of security services, fault the SLR carried out for this study. Section IV covers a
tolerance,managementofenergy,loadbalancing,andscala- thoroughdiscussiononthemainIoTmanagementchallenges.
bility.Ourgoalistocreateataxonomyandcategorizeexisting InSectionV,VI,VII,VIII,theNFV,Middleware,OpenFlow
SDN-basedIoTframeworks.Wehaveincludedframeworks and Blockchain-based SDN management frameworks and
that have been designed since 2010 and have evaluated theirexistingsolutionsarepresentedrespectivelyalongwith
these frameworks to assess how they stack up in solving their assessments regarding the defined research questions.
critical IoT management problems in terms of provision of In Sections IX, we summarized the outcomes of the survey
security services, fault tolerance, management of energy, withregardstotheexistingsolutionsandmergerofdifferent
load balancing, and scalability. We performed a Systematic approaches that aid in addressing the IoT framework’s
Literature Review (SLR) based on Kitchenham’s [79] well- management challenges. In Section X, we discuss the
known methodological framework to gather and analysis researchchallengesandfuturedirectionsfortheSDN-based
the existing research work. SLR is an evidence-based IoTmanagementframeworksinlightofoursurvey.Finally,
method to repetitively and impartially define, evaluate, and theconclusionofthepaperisprovidedinSectionXI.
70854 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
FIGURE2. TaxonomyofrelatedSDN-basedsolutionsforIoTmanagementframeworks.
FIGURE3. Overallorganizationofthesurveypaper.
II. BACKGROUND planesi.e.,theDP,CP,andApplicationPlane(AP),asshown
This section provides the required background knowledge in Fig. 4. SDN architecture uses southbound and NBI API
of SDN and its architectural design by comparing it with for communication with the DP and application plane with
traditionalnetworkingarchitecture. a protocol. OF is the most widely used protocol for this
purpose[81].
A. SDNARCHITECTURE
SDN is an evolving networking design architecture, con- 1) DATAPLANE(DP)
struction architecture, and management architecture of the The DP consists of network elements such as switches,
IoT ecosystem. SDN architecture consists of three layer of routers, sensors nodes, etc. The DP is at the bottom of
VOLUME10,2022 70855

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
FIGURE5. OpenFlowswitcharchitecture.
|     |     |     |     | consumers | or business applications | live,       | to benefit  | from the |
| --- | --- | --- | --- | --------- | ------------------------ | ----------- | ----------- | -------- |
|     |     |     |     | resources | available. It shares     | the control | information | with     |
theSDNControllerviatheNorthboundinterface(NBI)[69],
[92],[93].
4) OpenFlow(OF)
FIGURE4. SDN-Basednetwork. OF is a programmable network interface protocol designed
|     |     |     |     | for controlling | and monitoring | all network   | devices.   | OF is      |
| --- | --- | --- | --- | --------------- | -------------- | ------------- | ---------- | ---------- |
|     |     |     |     | considered      | to be one of   | the first SDN | standards. | Initially, |
the SDN architecture and is responsible for managing data itdefinedthecommunicationprotocolinSDNarchitectures
path and packets based on CP policies. According to the thatenabledtheSDNcontrollertointeractdirectlywiththe
| policies implemented | by the CP, | the DP forwards, | drops |     |     |     |     |     |
| -------------------- | ---------- | ---------------- | ----- | --- | --- | --- | --- | --- |
forwardingplane[94].UsingtheOFprotocol,aswitchmay
andmodifiespackets[82].Physicalorvirtualtrafficrouting beprogrammedtorunidenticallytoalegacyswitchwithout
andprocessingofnetworkelements(NE)ssuchasswitches, re-configuringtheswitchmanuallyifthenetworkshifts[95].
routers, and middleboxes are included in the DP [83]. A typical OF switch as shown in Fig. 5 contains a secure
Although data and CPs are implemented in the firmware channel,flowtable,andagroupoftables.Thegrouptables
of Network Equipment (NE) in traditional networking, organizeintomultipleflowentries,whichforwardtoasingle
the control functionalities are decoupled from the NE in identifier,identifyinganodeonthenetwork.Suchabstraction
| SDN[84]. |     |     |     | allowscommonoutputactionstobeappliedtoflowentries, |     |     |     |     |
| -------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
whichcanbechangedefficiently.IncomingpacketstotheOF
2) CONTROLPLANE(CP) switch are compared with multiple flow table entries until
|                    |                   |           |          | a match | is found, and a | set of actions | applicable | for that |
| ------------------ | ----------------- | --------- | -------- | ------- | --------------- | -------------- | ---------- | -------- |
| The software-based | CP allows network | resources | and for- |         |                 |                |            |          |
warding policies to be programmed and makes network particularflowentryisthenperformed[96].
managementagileandversatile[85].Alogicallycentralized
NOSorSDNcontrollerisusedtocomposetheCP[86].Here, 5) SOUTHBOUNDINTERFACE
NOX,Python-basedopensource(POX),Floodlight,beacon TheSouthboundInterface(SBI)consistsoftheOF[97]and
controllersarethemostcommonlyusedcontroller[87].The Forwarding and Control Element Separation (ForCES) [98]
CPisresponsibleforconfiguringnetworkelementswithrules specifications that allows connectivity between controllers
defined by the network applications designed on the top of and switches and other network nodes with lower-level
controller [88]–[90]. Communication between applications components or a DP layer. Southbound API enables the
(business logic and intelligence) and network devices is end-usertoobtainbetternetworkcontrolandencourageSDN
managed by the ‘‘brain’’ or the controller. The controller controller performance levels to evolve based on real-time
providescriticalfeaturessuchasstorageofnetworktopology, demands and needs. Moreover, the interface is an industry
state data, alerts and system management, protection, and normthatisjustifiedbytheperfectwaytheSDNcontroller
routingoftheshortestpaths[91].Thesearethebasicbuilding can connect with the forwarding plane. To build a more
blocksrequiredbymostnetworkapplications.Thecontroller flexible network layer for real-time traffic requirements,
alsoabstractsthelow-levelspecificsoftheforwardingplane
|     |     |     |     | administrators | may add | or delete network | switches | and |
| --- | --- | --- | --- | -------------- | ------- | ----------------- | -------- | --- |
andofferstheapplicationplaneanAPIcalledNBI[69]. routers’internalflowtables.
| 3) APPLICATIONPLANE(AP) |     |     |     | 6) NORTHBOUNDINTERFACE |     |     |     |     |
| ----------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
The AP is the top layer, which contains numerous applica- The NBI’s API provides communication between the SDN
tions.Itoffersanend-to-endviewoftheentirenetworkfrom controller and the network applications with the help of
awiderangeofapplicationdomainssuchasmilitarysurveil- automation stacks such as puppets, open packs, or open-
lance,healthcareorthesmarttransportationsystemsinwhich source cloud pad [99]. SDN NBI’s API integrates the
| 70856 |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE3. OpenFLowAPIswithSDNcontrollers.
|     |     |     |     | FIGURE7. | SDNorchestration. |     |     |     |
| --- | --- | --- | --- | -------- | ----------------- | --- | --- | --- |
FIGURE6. Legacynetworkarchitecture.
andprogrammingtheirnetworkandintacklingtheirlegacy
|                |     |             |                       | network’s | shortcomings.  | SDN simplifies | network   | manage-  |
| -------------- | --- | ----------- | --------------------- | --------- | -------------- | -------------- | --------- | -------- |
| SDN controller | and | the NBI API | itself to incorporate |           |                |                |           |          |
|                |     |             |                       | ment by   | separating the | Control Plane  | (CP) from | the Data |
more complicated frameworks such as firewalls, load bal- Plane(DP)andmakingthenetworktobeflexiblydeployed
ancers, and so on; and the controller will be respon- and automatically configured by dynamically programming
sible for ensuring that they communicate appropriately. and reorganizing the network environment from the central
NBI’s API uses network computing paths, especially paths SDNcontroller[105],[106].
| that comply | with intended | policies | and computing | paths |     |     |     |     |
| ----------- | ------------- | -------- | ------------- | ----- | --- | --- | --- | --- |
SDNaimsatmakingnetworkingagile,flexible,andsmart
that avoid loops, routing, and recovery from failures, with the help of enhanced configuration, improved perfor-
and implementing protection policies. Table-3 shows the mance in network architecture and operations [25], [64],
| list of | OF protocols | for Southbound | and NBI API | for        |          |                    |     |               |
| ------- | ------------ | -------------- | ----------- | ---------- | -------- | ------------------ | --- | ------------- |
|         |              |                |             | [107]. SDN | provides | network management |     | orchestration |
SDNcontrollers. as shown in Fig. 7. In [94], an OpenFlow (OF) switch
conceptwasintroducedevenbeforetheformaldefinitionof
B. NETWORKPROGRAMMABILITY SDN.Tofacilitateon-campusinnovationnetworks,OFwas
Legacy network architectures rely on purpose-based and developed by allowing researchers to test their ideas in an
vendor-specific systems consisting of highly integrated and isolated ‘slice’ of the actual network [94]. By separating
specialized forwarding chips [104], proprietary operating its CP and DP, this approach breaks the constraints of an
systems, and pre-defined features. An operator must con- ‘‘Ossified’’ network structure. Gudeetal.[108] proposed
figure each device using vendor-specific tools to enforce a network operating system named OpenFlow controller
new network policies. Often, an operator needs to wait for (NOX). NOX provides unified programming interfaces
alongtimeforincludinganewfunctionbeforethedevice’s for the network (called NorthboundInterface (NBI)). The
manufacturer releases a software update that supports the applications will take advantage of the network’s logically
intended component. Fig. 6 shows the main components of centralized view using the NBIs provided by the Network
thelegacynetworkarchitecture. OperatingSystem(NOS).OFandNOXprovideaneffective
On the other hand, as a revolutionary paradigm, SDN solutionfortheSDNarchitectureprinciple(initiallyreferred
allows network operators to be more flexible in managing toastheNOX-basednetwork).
| VOLUME10,2022 |     |     |     |     |     |     |     | 70857 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
III. SYSTEMATICLITERATUREREVIEWPLANNING IoTnetworksandidentifythechallengesandthetechniques
ThissectionoutlinestheoverallplanforconductingtheSLR appliedtoguaranteetheQualityofService(QoS).
for the study at hand. We will explain how the SLR was RQ4: What scalable solutions can be offered by
performed, including the research questions formalization, SDN-basedframeworkstomanageIoTnetworks?
bibliographic source selection, and inclusion and exclusion IoTinfrastructurelinkstogethermanysensorsanddevices
criteria. The conducted SLR aims to provide the grounds for gathering information and sharing it with other applica-
for qualitative synthesis and information extraction leading tions through the Internet. It challenges the system’s design
towardsfindingthepotentialsolutionstosolvingcriticalIoT and implementation to meet scalability and adaptability to
management issues such as security service provisioning, the changing world and people’s needs. Scalability means
fault tolerance, energy management, load balancing, and versatility that helps us to adequately address and satisfy
scalability through the available SDIoT frameworks. In this the unique requirements when they arise. The main aim of
study, we primarily review the existing literature intending makingthesystemflexibleistomeetevolvingneeds[111].
tosystematicallyidentifythecurrentchallengesandresearch RQ5:HowcanSDN-basedframeworksenableefficient
opportunities for contributing to the knowledge-base of the powerconsumptioninIoTnetworks?
SDN-basedIoTframework. IoTnetworkscanachieveenergyefficiencybyincreasing
ordecreasingdatarates.DifferentsectionsofSDN-managed
A. RESEARCHQUESTIONS networkdynamicallyconfigurableSDNframeworktoreduce
This study aims to address the following primary research powerconsumption.Onewayistosettheflowtothenetwork
questions(RQ), trafficandbringunuseddevicesintosleepmode.Whentraffic
RQ1: How can SDN-based frameworks provide effi- is poor, specific ports can be placed in sleep mode instead
cient security solutions to manage IoT network-related of the whole system. Another approach is to optimize or
securityissues? reducethememorysizeusedbyforwardingswitchesasflow
IoT-based applications gather environment data and send tables are stored in costly, power-hungry Ternary Content
it to central servers for review and processing. Maintaining AddressableMemory(TCAM)[112].
privacyisessentialintheapplicationlayer.Besidesprivacy,
therearemanyothersecurityissues,suchasnetworkrouting B. SOURCESELECTION
attacks that can interrupt IoT services. Additionally, many The selection of appropriate online bibliographic databases
IoTapplicationsrequiretrustmanagement[109].Therefore, is essential to search primary studies and find proper
IoT security monitoring is a crucial problem to be tackled. evidence to address the research questions. In the fol-
This question is about how SDN architecture provides IoT lowing subsection, we will define the parameters used to
networkswithprotectionefficiently. select specific bibliographic sources and search strings. For
RQ2: How can SDN-based frameworks provide effec- bibliographic source selection criteria, we considered web
tive fault tolerance management solutions to large-scale articles’ availability and the existence of advanced search
IoTnetworks? mechanisms using keywords and content-based filtering
Fault tolerance or reliability is the primary criteria for (conference papers, journals, and magazines, etc.) and year
an IoT-based solution. SDN provides substantial reliability of publication. We choose the following multidisciplinary
advantages.Forexample,duetoglobalnetworkvisibilityin electronic bibliographic databases: IEEE Xplore, Science
SDNarchitecture,theCPcaneasilycomposevariousnetwork Direct,Scopus,ACMDigitalLibrary,andSpringerLinks.
policiesontheDPwithoutconflicts.Severalnewfeaturesin Due to the integrative nature of the research questions,
SDNarchitecturestillraiseconcernsaboutreliability.These a variety of fitting search strings were required to be
featuresincludethecontrolDPseparationarchitecture,which incorporated. To compose our search string, we considered
can increase network processing latency in the IoT network keywords listed in Table-4, where each group is a keyword
leadingtonetworkfailures[68].Thisquestionseekstoclarify that either concatenates or not with another group string.
the role of the SDIoT-based framework to provide efficient Wecreatedsearchstringsfortwocategories,asshownbelow
faulttolerancemanagementinIoTnetworksandidentifythe in Equation (1) and (2), i.e., one for the survey findings
challenges. and the other is to find the frameworks that are related to
RQ3: What are the potential solutions regarding load theresearchquestions.Here,∧representsthelogicalAND,
balancing in SDN-based frameworks to manage IoT (cid:107) represents the logical OR, and G represent the groups as
networks? showninTable4.
IoT network has limited network capacity to meet the For finding related surveys that answers the research
quality of service requirements. One of the critical goals to questions, we used the following equation for search string
maintainqualityofservicerequirementistheloadbalancing formation.
problem, which helps spread data traffic among multiple
resources to optimize network resources’ efficiency and G1 (cid:8) 1(cid:107)2(cid:107)3(cid:107)4(cid:107)5 (cid:9)∧G2∧G3∧G4 (cid:8) i (cid:9)∧G5
Survey
reliability [110]. This question seeks to clarify the role of (cid:110)
the SDIoT-based framework to manage load balancing in i= NFV||Blockchain||Middleware||OpenFlow (1)
70858 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE4. Listofsearchingstrings.
For discovering the SDN-based IoT frameworks that
answerstheresearchquestions,wehavethefollowingsearch
stringformationequation.
G1 (cid:8) 1(cid:107)2(cid:107)3(cid:107)4(cid:107)5 (cid:9)∧G2∧G3∧G4 (cid:8) i (cid:9)∧G5
Framework
(cid:110)
i= NFV||Blockchain||Middleware||OpenFlow (2)
C. PROCEDUREFORSELECTIONOFSTUDIES
Thefollowinginclusionandexclusioncriteriaweredefined
forthelegitimacyoftheprimarygatheredarticles,
1. The primary study is an English-written article pub-
lished in a scientific journal, conference proceeding,
magazine,orbook.
2. Publications in the shape of dissertations, in-progress
researchpapers,guesteditorials,posters,andblogsare
excluded.
3. Theprimarystudyispublishedonoraftertheyear2010.
4. Theprimarystudyshouldclearthefollowingthree-phase
selectionandassessmentprocess,
FIGURE8. Searchandselectionprocess.
Phasei: Anarticlewillonlybeincludedinthefollowing
phase if it comes in the IoT and SDN domain
papers with the help of the defined search strings. We then
and describing any of the following issues, i.e.,
began executing selection procedures, as defined in the
energy management solution or design, fault
primary study selection procedure, based on three stages
tolerance, load balancing, and scalability and
of selection as defined in SectionIII. C. Having studied
security.Thisstagefocusesonthetitle,abstract,
all abstracts and conclusions in phase 1 (screening phase),
andtheconclusionsection.
we select only those papers that provide SDN-based IoT
Phaseii: An article will be included if it explains the
solutions. We choose 328 research papers in this case and
proposedarchitecturedesignorevaluationofthe
discarded 340. In phase 2, we selected articles explaining
proposed solution in detail. This stage evaluates
theSDN-basedIoTmanagementsolutionarchitecturebased
fullarticlecontent.
on inclusion and exclusion criteria and the relevance of the
Phaseiii: Selected paper screening is finalized and an
titles and keywords to the topic. After reviewing all the
articleisremovedunlessitfollowsthefollowing
selectedpapercontents,wepicked224studiesanddiscarded
contentrequirements.
104researchpapers.Inphase3,wediscarded68morestudies
– C1: Does the selected paper fulfill any of the
that didnot meetthe defined qualityrequirements basedon
researchquestionsornot?
thejudgmentcriterion.Inthelastphase,thefull-textscreen-
– C2: Is the proposed architecture in the selected
ingoftheselectedpaperswasperformed,andthepaperswere
paperdescribedindetail,andisitwell-designed?
thoroughlyanalyzedbytheauthors.Moreover,withthehelp
Eachcriterion(C1andC2)hasthreepossibleresponses,i.e.,
offorwardandbackwardsnowballingthenumberofinclusive
yes, partly, or no. ‘‘Yes’’ counts as 1 (one) point, ‘‘partly’’
studies increased from 156 to 188 resultant papers. Hence,
counts as 0.5 points, and ‘‘no’’ counts as 0 (zero) point.
after the final phase, the size of the selected paper database
Anarticlemustobtainascoreequalto2(two)forselection,
was 188 papers for the exploration of potential answers to
asdefinedinEquation(3):
the research questions. The detailed paper selection process
C1+C2<=2 (3) during different phases are summarized in Table-5. The
completeprocedurefrominitialselectiontofull-textselection
D. SYSTEMATICREVIEWEXECUTION issummarizedinFig.8.
Thesearchfortherequiredarticleswascarriedouttilltheend To classify the selected articles’ information, metadata
ofMarch2022.Initially,wegatheredatotalof668research forms were created to organize the details and considered
VOLUME10,2022 70859

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE5. Paperselectionprocessduringdifferentphases.
annotations. The obtained metadata, containing information A. SECURITYMANAGEMENT
| such as publication |     | year, | keywords, | authors’ | names | and |             |     |              |         |      |          |      |
| ------------------- | --- | ----- | --------- | -------- | ----- | --- | ----------- | --- | ------------ | ------- | ---- | -------- | ---- |
|                     |     |       |           |          |       |     | IoT network |     | applications | collect | data | from the | sen- |
affiliations, journal/conference name, research type, SDN sors/devices and send it for analysis and processing to
andIoTarchitecturedetails,managementissuedetails,etc., central servers. This data can vary from health specifics
were coded for analysis to answer the research questions. to purchasing habits and sales at a retailer. For companies,
Themajorityoftheresultingpaperswerepublishedbetween this data has monetary value. One critical issue during the
| 2018 and | 2021, | indicating | an  | increasing interest |     | in how |               |     |                |         |        |             |     |
| -------- | ----- | ---------- | --- | ------------------- | --- | ------ | ------------- | --- | -------------- | ------- | ------ | ----------- | --- |
|          |       |            |     |                     |     |        | whole process |     | is maintaining | privacy | [121]. | In addition | to  |
SDN can solve management problems in the IoT domain. privacy, security concerns, such as network-based routing
In accordance with the research question, an initial classi- attacks and botnet attacks, can disrupt the IoT services
fication was performed to show the number of survey and [122], [123]. Furthermore, several IoT applications require
framework-basedpaperswithrespecttodifferentchallenges trust management for reliable data fusion and enhanced
| in various | approaches, | as  | shown | in Fig. 9. | Fig. 10 | depicts |             |          |        |         |     |                 |     |
| ---------- | ----------- | --- | ----- | ---------- | ------- | ------- | ----------- | -------- | ------ | ------- | --- | --------------- | --- |
|            |             |     |       |            |         |         | information | security | [124]. | Because | of  | these mentioned |     |
the total number of survey and framework-based papers reasons, IoT security management is critical to ensure the
focusing on various IoT management challenges. With safetyofnetworksandefficientdatatransmission.However,
the available information on different IoT management in IoT networks, the security functionality becomes even
challengesinvariousareas,inFig.11wehavealsoextracted more difficult due to the heterogeneous nature of these net-
| the distribution | of  | the identified |     | papers in accordance |     | with |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | -------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
worksequippedwithresourceconstraintsIoTdevices[125].
theirresearchmethods. Therefore,traditionalIoTsecuritysystemsareinefficientand
|     |     |     |     |     |     |     | require | extensive | adaptation, | including | overall | IoT | network |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----------- | --------- | ------- | --- | ------- |
IV. MANAGEMENTCHALLENGESINIoTSOLUTIONS framework redesigns. The new IoT network management
frameworksrequireinnovativemechanismstodealwiththese
| Conventionally      | managing |           | a network, | involves        | the | use of  |        |            |             |             |     |          |     |
| ------------------- | -------- | --------- | ---------- | --------------- | --- | ------- | ------ | ---------- | ----------- | ----------- | --- | -------- | --- |
|                     |          |           |            |                 |     |         | unique | challenges | on security | management. |     | The need | for |
| a set of management |          | protocols |            | that facilitate | the | sharing |        |            |             |             |     |          |     |
of data between users and networks of all kinds [113]. more robust solutions is piling due to user unawareness,
untimelydeviceupdates,lackofadequatesecurityprotocols
| Due to the | wide | range of | networked | systems | found | on the |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | --------- | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
Internettoday,controllednetworkmodulescanhavediverse forIoTauthenticationandIoTencryption.
characteristicsintermsofstorage,processingcapacities,and
energyusage[114].IoTnetworkmanagementshouldbeable B. FAULTTOLERANCE
| to provide | functionalities, |     | among | other capabilities, |     | such as |     |     |     |     |     |     |     |
| ---------- | ---------------- | --- | ----- | ------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
FaulttolerancemechanismsinIoTnetworksaddressdevice
tomonitornetworkstatus,detectfaults,configureoperating failuresandensurethatthenetworkwillcontinuetooperate
parameters, collect network performance information, and smoothly and reliably [126]. There are numerous reasons
manageitsoperation[115].Moreover,duetothewide-spread
|     |     |     |     |     |     |     | for failures | to  | occur in | the IoT networks. |     | Device | battery |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ----------------- | --- | ------ | ------- |
Internet connectivity the management challenges faced depletionisthemostcommonreasonforfailures[127].Also,
| by traditional | Wireless |     | Sensor | Network (WSN) |     | are now |            |          |        |            |               |     |     |
| -------------- | -------- | --- | ------ | ------------- | --- | ------- | ---------- | -------- | ------ | ---------- | ------------- | --- | --- |
|                |          |     |        |               |     |         | inaccurate | readings | caused | by various | environmental |     | and |
inherited to IoT domain as well [116]. These management technical factors may propagate the devices. The multi-hop
challengeshavebeencharacterizedby[117]–[120]as, communication nature of IoT networks exacerbates a lot of
1: Securitymanagement failures[128].Moreover,thefollowingfailurescanoccurat
| 2: Faulttolerance |     |     |     |     |     |     | allarchitecturallevelsofIoTapplications, |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| 3: Loadbalancing  |     |     |     |     |     |     | • Sensorandactuatornodesmaybeabsent.     |     |     |     |     |     |     |
| 4: Scalability    |     |     |     |     |     |     | • Networkconnectionsmaybedown.           |     |     |     |     |     |     |
5: Energymanagement
• Processingandstoragecomponentsmayfailtooperate
| The IoT | network | management |     | solutions | should | be  | correctly. |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | --------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
designed in a manner that provides a range of management Therefore, IoT infrastructures must support state-of-the-art
functionsthatcatertotheabove-mentionedIoTmanagement faulttolerancemechanismstobeabletorecoverfromthese
issues.
malfunctions.
| 70860 |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| FIGURE9. | Numberofsurveyandframework-basedpapersintheconsideredareas.         |     |     |     |     |     |     |
| -------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          | FIGURE10. NumberofpapersidentifiedintermsofIoTmanagementchallenges. |     |     |     |     |     |     |
C. LOADBALANCING consumption [130]. The clustering in the network is one
Load balancing is one of the essential strategies in IoT way to achieve load balancing in an IoT infrastructure.
environments that aims to assign proper utilization of IoT The IoT network is organized into clusters where the
infrastructure for optimizing the use of sensors or other cluster’s head coordinates and communicates within the
|     |     |     |     | nodes [131]. | Network clustering | reduces | the routing table |
| --- | --- | --- | --- | ------------ | ------------------ | ------- | ----------------- |
connecteddevices.TheroleofloadbalancinginIoTnetworks
iscorrelatedwiththenumberofconnectedobjectsemployed size, conserves network bandwidth, increases network life-
forsharingdata.Theimbalanceinthenetworktrafficwithin time, reduces redundant data packets, and decreases energy
consumption[132],[133].
| the IoT  | network, which      | is hampered  | by resources, results |     |     |     |     |
| -------- | ------------------- | ------------ | --------------------- | --- | --- | --- | --- |
| in waste | of resources [129]. | As a result, | load balancing        |     |     |     |     |
| within   | IoT networks leads  | to efficient | use of resources      |     |     |     |     |
D. SCALABILITY
within IoT networks. IoT networks can expand their life Scalability means versatility that allows one to adapt to the
spanthroughloadbalancing,whichreducesthegrid’senergy changesandgrowwiththemandachievespecificneedswhen
| VOLUME10,2022 |     |     |     |     |     |     | 70861 |
| ------------- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| FIGURE11. | Distributionofpapersaccordingtotheirresearchmethods. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theyarise.Themainadvantageofscalabilityisthatitenables TABLE6. Listofvirtualnetworkfunctionsofnetworklayer.
thesystemtooperategracefullywithoutanyunduedelayand
| unproductive   | resources |            | and makes |                 | fair use    | of the      | available |     |     |     |     |     |     |     |     |
| -------------- | --------- | ---------- | --------- | --------------- | ----------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| resources.     | Any       | scheme     | that      | can manage      |             | the network | with      |     |     |     |     |     |     |     |     |
| the rising     | amount    | of growth  |           | is a beneficial |             | function.   | With      |     |     |     |     |     |     |     |     |
| the increasing |           | definition | of IoT    | in              | the future, | scalability | is        |     |     |     |     |     |     |     |     |
abigchallengeinIoT[134].AnIoTsystemconnectsseveral
| sensors, | actuators, | and | other | devices | to enable | information |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ----- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
avirtualizedsolution.Theconceptofswitchingfunctionality,
| sharing       | and a | large number | of  | applications |     | via the  | Internet. |          |              |               |                  |            |               |      |        |
| ------------- | ----- | ------------ | --- | ------------ | --- | -------- | --------- | -------- | ------------ | ------------- | ---------------- | ---------- | ------------- | ---- | ------ |
|               |       |              |     |              |     |          |           | routing  | assistance,  | and           | other components |            | are           | now  | run in |
| It challenges |       | the design   | and | the system’s |     | growth   | to meet   |          |              |               |                  |            |               |      |        |
|               |       |              |     |              |     |          |           | software | applications | such          | as               | virtual    | applications. |      | These  |
| scalability   | and   | adaptability | to  | the people’s |     | evolving | digital   |          |              |               |                  |            |               |      |        |
|               |       |              |     |              |     |          |           | network  | functions    | are available |                  | in a group | format        | from | the    |
needs.
|     |     |     |     |     |     |     |     | remote    | location. | Table-6 | shows   | some      | renowned | network |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | ------- | --------- | -------- | ------- | --- |
|     |     |     |     |     |     |     |     | functions | of a      | network | device, | switching | device,  | gateway |     |
E. ENERGYMANAGEMENT device, and security devices. The key benefit of using
| Inherently, | IoT   | devices’ | energy | is       | constrained |      | because of |          |                |          |             |              |               |      |     |
| ----------- | ----- | -------- | ------ | -------- | ----------- | ---- | ---------- | -------- | -------------- | -------- | ----------- | ------------ | ------------- | ---- | --- |
|             |       |          |        |          |             |      |            | NFV is   | that it        | enables  | eliminating | middlelayers |               | that | are |
| the sensor  | nodes | deployed | in     | a remote | area        | with | no access  |          |                |          |             |              |               |      |     |
|             |       |          |        |          |             |      |            | deployed | in traditional | networks |             | for cost     | effectiveness |      | and |
to a permanent power source [135]. IoT network energy flexibility. Network and infrastructure features allow the
| management | is  | concerned | with | energy | conservation |     | within |          |        |          |          |     |           |            |     |
| ---------- | --- | --------- | ---- | ------ | ------------ | --- | ------ | -------- | ------ | -------- | -------- | --- | --------- | ---------- | --- |
|            |     |           |      |        |              |     |        | use of a | single | physical | platform | by  | different | providers, |     |
the network for the connected nodes. Over time the power applications, and tenants [47]. On the other hand, NFV
of the existing battery shrinks, and the power depletion can technology facilitates the coexistence of multi-tenancy as
| not be | readily | replaced | as the | sensor | nodes | are | remotely |     |     |     |     |     |     |     |     |
| ------ | ------- | -------- | ------ | ------ | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
well.
deployed. Duty cycling is one of the techniques used to NFV infrastructure consists of two layers, i.e., the hard-
| preserve | energy | on IoT | equipment. |     | The devices |     | will wake |                |     |            |                  |     |        |     |       |
| -------- | ------ | ------ | ---------- | --- | ----------- | --- | --------- | -------------- | --- | ---------- | ---------------- | --- | ------ | --- | ----- |
|          |        |        |            |     |             |     |           | ware resources |     | layer, and | a virtualization |     | layer, | as  | shown |
upduringanintermittenttimeifnecessaryandsleepduring in Fig. 12. The hardware resources layer is responsible
this technique [136]. From this discussion, it is clear that for dealing with the storage and network services that
| a management |     | solution | for those | networks |     | should | have an |         |               |      |       |     |              |     |      |
| ------------ | --- | -------- | --------- | -------- | --- | ------ | ------- | ------- | ------------- | ---- | ----- | --- | ------------ | --- | ---- |
|              |     |          |           |          |     |        |         | include | data centers, | edge | nodes | for | IoT domains, |     | etc. |
elaborate component of energy management in order to be The virtualization layer is accountable for providing virtual
abletoworksmoothlyinanIoTnetwork.
functionstothelowerlayerorhardwareresourcelayer.
|     |     |     |     |     |     |     |     | The SDN | NFV | based | architecture | generally |     | consists | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | ------------ | --------- | --- | -------- | --- |
threemodules,i.e.,controlmodule,forwardingdevices,and
V. NETWORKFUNCTIONVIRTUALIZATIONBASEDSDN
MANAGEMENTFRAMEWORKS NFV platform, as shown in Fig. 13. In the control module,
NetworkFunctionVirtualization(NFV)offersanadvantage the SDN controller communicates with NFV orchestration
fortheICTindustrybyseparatingthenetworkhardwareinto with the help of the NBI-API interface to derive essential
| 70862 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
FIGURE13. SDN-basedNFVarchitectureprovidingthevirtualized
network’sfunctionality.
FIGURE12. Virtualnetworkfunctionsinfrastructure.
2) PROPOSEDFRAMEWORK
In a proposed architecture [143], authors have been influ-
networkfunctionsfromtheNFVplatformlayer.Forwarding enced by SDN and virtualization network function capa-
devices are responsible for forwarding the packets to the bilities for IoT infrastructure resources. The NFV and
controller through an interface for decision-making. The SDN make it easy to program network services. The NFV
NFV orchestration device is responsible for providing portion of Virtual Network Functions (VNF) shifts network
the virtualized network’s functionality and is managed by functions from dedicated hardware to software. In NFV,
standard interfaces by the SDN controller. It translates SDNenablesthecomplexestablishmentofrelationsbetween
the requirements of the logic policy into optimized rout- VNFs.Theproposedarchitecture[143],asshowninFig.14,
ing routes. The NFV orchestration system enforces task is composed of four different layers, i.e., (1) service layer,
assignments[140]. (2) global OS layer, (3) virtualization, and physical layer.
Function Virtualization is implemented in a series of The service layer incorporates all service-level functions.
building blocks to define connectivity and to construct The global OS layer integrates cloud orchestration tools
communication services between them through an NFV and SDN controllers. SDN controller layer is responsible
architecture, which uses various techniques to virtualize for end-to-end network and IT resources management.
full network node functions [141]. The architecture of the It handles all network elements’ dynamic configuration
NFV consists of three key (a) VNF: These are the software and re-configuration parameters. The virtualization layer
features responsible for carrying out basic network opera- organizes hardware resources on virtual machines made
tions;(b)NFVInfrastructure(NFVI):Thisplatformhandles accessible to the layers above. Finally, the perception layer
multipleVNFs,virtualstorage,andprocessing;and(c)NFV consists of IoT sensors responsible for extracting data and
Management and Orchestration (NFV-MANO): Offers an providedtotheupperlayer.Theauthors’aimintheproposed
architecturalframeworkforinterfacesandreferrals[142]. frameworkistodecouplehardwarefromnetworkoperations,
This section aims at answering the research questions minimizing resource management costs with the NFV and
basedonNFVtaxonomywithacombinationofSDNframe- SDN’s help. VNF services are transferred from dedicated
works to address the IoT management challenges. We will applicationsthroughtheuseofSDNcontrollers.
discussthedifferentSDN/NFVframeworksproposedinthe
existingliteraturetoaddresstheIoTmanagementchallenges 3) CRITICALANALYSIS
andtoidentifyfuturedirections. The proposed architecture is very general and does not
provide specific information regarding the various compo-
A. INFRASTRUCTURESERVICESNFV/SDNARCHITECTURE nents’operationsandrelationshipsindifferentlayers.Service
1) MOTIVATION level function and infrastructure resources definition is not
An IoT network faces many challenges in cooperating with presented. Furthermore, no specifics are given about how
various network resources and providing services such as SDNandNFVcollaboratetohandleIoT.
security, computing, power management, etc. IoT networks
need to be tailored to the situation and provide the required B. SDN-BASEDIoTFRAMEWORKUSINGNFV
services. SDN can provide network operations that provide 1) MOTIVATION
controllayeroperationswiththehelpofNetworkFunctions IoT nodes can have a high computing capacity with
Virtualization (NFV). SDN offers a resource management cloud computing support, but deploying cloud computing
mechanism for IoT networks, thus helping infrastructure approaches to IoT poses challenges for the SDN research
resourcestobedeployedeffectively. paradigm and the network virtualization integration feature.
VOLUME10,2022 70863

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     |     | FIGURE15. | AtypicalSDN-basedIoTframeworkwithNFV. |                  |             |
| --- | --- | --- | --- | --------- | ------------------------------------- | ---------------- | ----------- |
|     |     |     |     | tunneling | among IoT gateways,                   | and prioritizing | traffic for |
QoSinacentralized,programmablecontroller.Resourcefully
|     |     |     |     | distributed      | OS assists NFV-based | SDN frameworks | for IoT            |
| --- | --- | --- | --- | ---------------- | -------------------- | -------------- | ------------------ |
|     |     |     |     | infrastructures. | Distributed          | OS approach    | offers centralized |
controlandviewofheterogeneousIoTservices.
3) CRITICALANALYSIS
FIGURE14. InfrastructureservicesNFV/SDNarchitecture. As illustrated in Fig. 15, the proposed architecture is quite
|     |     |     |     | generic,          | and various layers | are not detailed   | appropriately, |
| --- | --- | --- | --- | ----------------- | ------------------ | ------------------ | -------------- |
|     |     |     |     | as implementation | and                | assessment details | are lacking.   |
To create communication services, NFV virtualizes entire Evaluations are necessary to understand the performance
networkfunctionsthataretheninterlinked.Insteadofmaking improvements made by the delivery of OS for IoT network
customhardwareequipmentfornetworkoperations,network management. Moreover, studies must be carried out to
functionsarevirtualizedbyoneormorevirtualmachinesthat measure the overall cost resulting from the virtualization of
execute heterogeneous processes. Li et al. [144] suggested thearchitecturenetworkfunctions.
| that networking | features such | as routing, secure | tunneling |     |     |     |     |
| --------------- | ------------- | ------------------ | --------- | --- | --- | --- | --- |
between IoT gateways, and prioritization of traffic for QoS C. ADISTRIBUTEDSECURESDNIoTARCHITECTURE
inanIoTnetworkcanbeimplementedwithOpenFlow-based
1) MOTIVATION
SDNandNFVimplementation. ThebigconcernintheIoTdomainisconfidentiality,safety,
|     |     |     |     | reliability, | and network | performance. With | the support of |
| --- | --- | --- | --- | ------------ | ----------- | ----------------- | -------------- |
2) PROPOSEDFRAMEWORK centralizednetworks incollaboration withcontrollers,SDN
As shown in Fig. 15, the authors in [144] proposed an canhandletheIoTnetworkassetswiththehelpofintegration
| IoT architecture | based on | SDN with NFV implementation. |     | withNFV. |     |     |     |
| ---------------- | -------- | ---------------------------- | --- | -------- | --- | --- | --- |
Theproposedframeworkconsistsoftheapplication,control,
and infrastructure layer. The application layer includes IoT 2) PROPOSEDFRAMEWORK
servers for various applications and services via API. The Network Virtualization Feature incorporates the theme of
controllayercomprisesSDNcontrollersthatarerunningon using virtual machines that handle routing, switching, and
adistributedOS.ThedistributedOSprovideslogicallycen- other network operations instead of using specialized hard-
tralized IoT control and viewing in a physically distributed ware.However,NFVneedstobemonitoredandcoordinated.
network data forwarding environment. The infrastructure The SDN, therefore, comes with a solution to handle all
layerconsistsofIoTgatewaysandSDNswitchesforaccess virtual machines and networks by decoupling the CP and
tovariousIoTdevicessuchasRFIDsandsensorsviacontrol the DP. The IoT device is distributed in nature, and the
Interface DP. Authors suggest that with OpenFlow-based sensornodeskeepsendingdatatothecontrollerapplications
SDN and NFV implementation, it will be possible to accompanied by environmental perception. This is why
implementIoTnetworkingfunctionssuchasrouting,secure the SDNIoT environment’s deployment has become more
| 70864 |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     |     |     |     |     |     | FIGURE17.     | NETRA:EnhancingIoTsecurityusingNFV. |     |                  |     |              |             |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------------------------- | --- | ---------------- | --- | ------------ | ----------- | --- |
|     |     |     |     |     |     |     |     | availability, | integrity,                          |     | confidentiality, |     | etc., in     | IoT network |     |
|     |     |     |     |     |     |     |     | data. The     | authors                             | do  | not present      |     | any detailed | work        | on  |
securitymodulesinNFVorexploreanyalgorithmicsecurity
|     |     |     |     |     |     |     |     | approach. | Implementation |     | and | analysis | are also | missing | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --- | -------- | -------- | ------- | --- |
thearchitecture.
| FIGURE16. | AdistributedSDN-IoTarchitecture. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D. ENHANCINGIoTSECURITYUSINGNFV-BASED
ANALYSIS
effectiveinlowpowerconsumption,efficiencyenhancement,
1) MOTIVATION
andsecurityissuesreduction.Theauthorsin[145],presented With the evolution of IoT gadgets and their applications,
Black SDN-IoT with NFV implementation for smart cities we are moving toward the era of smart computing. The
| using NFV | integration |     | with | the SDN | controller, |     | as shown |          |          |       |         |     |         |          |     |
| --------- | ----------- | --- | ---- | ------- | ----------- | --- | -------- | -------- | -------- | ----- | ------- | --- | ------- | -------- | --- |
|           |             |     |      |         |             |     |          | security | of these | smart | gadgets | is  | at high | risk due | to  |
in Fig. 16. The proposed architecture is based on the cyber-attacks.Conventionalsecuritymechanismstomanage
| layered | approach: | the | application | layer, | the | CP, | DP, and the |             |          |     |        |                  |     |          |     |
| ------- | --------- | --- | ----------- | ------ | --- | --- | ----------- | ----------- | -------- | --- | ------ | ---------------- | --- | -------- | --- |
|         |           |     |             |        |     |     |             | IoT network | security |     | issues | have limitations |     | in terms | of  |
perception layer. The application layer consists of multiple scalabilityandcost.
| smart services |     | of a | smart | city. In | the | CP, the | virtualize |     |     |     |     |     |     |     |     |
| -------------- | --- | ---- | ----- | -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
functionprovideservicestodistributedSDNcontrollersuch
2) PROPOSEDFRAMEWORK
asrouting,security,resourcemanagement,etc.withthehelp
|         |     |       |             |     |                |     |          | Authors  | in [146] | proposed | a        | Docker-based | framework |              | that |
| ------- | --- | ----- | ----------- | --- | -------------- | --- | -------- | -------- | -------- | -------- | -------- | ------------ | --------- | ------------ | ---- |
| of VNF. | The | DP is | responsible |     | for forwarding |     | the data |          |          |          |          |              |           |              |      |
|         |     |       |             |     |                |     |          | deployed | virtual  | network  | security | functions    | at        | IoT gateway, |      |
packet from the perception to the CP. SDN in the proposed as shown in Fig. 17. These virtual functions are stored in a
| architecture | is  | distributed | in  | nature | according | to  | its security |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ------ | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
cloudstructure.IoTgatewayisresponsibleforfetchingthese
| roles. One | of  | the | distributed | SDN | controller’s |     | critical |                 |     |          |           |      |           |           |     |
| ---------- | --- | --- | ----------- | --- | ------------ | --- | -------- | --------------- | --- | -------- | --------- | ---- | --------- | --------- | --- |
|            |     |     |             |     |              |     |          | virtual network |     | security | functions | from | the cloud | according |     |
roles in preventing the dissipation of the data among the to the requirements. These VNFs play an important role in
| nodes by | making | them | directed | to  | themselves, |     | thus saving |           |     |          |        |               |     |              |     |
| -------- | ------ | ---- | -------- | --- | ----------- | --- | ----------- | --------- | --- | -------- | ------ | ------------- | --- | ------------ | --- |
|          |        |      |          |     |             |     |             | improving | the | security | of IoT | environments. |     | The proposed |     |
energy by the process. The security controller controls the architecture based on docker technology consists of three
| cluster | domain | and protects |     | each | cluster | of SDN | security |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | --- | ---- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
layers,i.e.,corenetwork,IoTgateway,andIoTenvironment.
| controller | against | attacks | produced |     | within | and | outside the |          |         |          |     |        |            |          |     |
| ---------- | ------- | ------- | -------- | --- | ------ | --- | ----------- | -------- | ------- | -------- | --- | ------ | ---------- | -------- | --- |
|            |         |         |          |     |        |     |             | The core | network | contains | the | Docker | hub, which | includes |     |
IoTnetwork. therepositoryforalldockerimages.TheDockerimagescan
bedeployedfromthislayerwithadockerpullcommand.IoT
3) CRITICALANALYSIS gateway layer represents an edge that hosts various dockers
SDN-IoT has numerous unique challenges, and only a few VNFs modules such as firewall, intrusion detection, SDN
researchers have tackled these challenges. The proposed switches.TheIoTenvironmentcontainstheIoTnodessuchas
centralized Black SDN-IoT architecture [145] with NFV cameras,sensors,etc.TheauthorsusedanOpenPlatformas
is considered for smart cities for energy savings, load NFV,andOPNFVconsistsofdifferentIoTnodesthatutilize
balancing, and network scalability purposes. The authors differentnetworkfunctionsdeployedfromtheupperlayerof
introduced several hierarchical SDN controllers to enhance theOPNFVmaster.
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 70865 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
3) CRITICALANALYSIS
| The authors | compare                | the two          | architectures  | VM-based         |     |     |     |     |     |
| ----------- | ---------------------- | ---------------- | -------------- | ---------------- | --- | --- | --- | --- | --- |
| (OPNFV)     | without SDN            | and Docker-based |                | (NETRA) based    |     |     |     |     |     |
| on SDN      | with performance       | indicators       |                | such as storage, |     |     |     |     |     |
| memory,     | latency, network,      | and scalability. |                | The result sug-  |     |     |     |     |     |
| gested that | NFV as container-based |                  | virtualization | with an          |     |     |     |     |     |
SDN-basedapproachworksbetterthantheexistingsolution
| based on | a VM-based framework. |         | The         | proposed solution |     |     |     |     |     |
| -------- | --------------------- | ------- | ----------- | ----------------- | --- | --- | --- | --- | --- |
| improved | the security of       | the IoT | environment | containing        |     |     |     |     |     |
nodessuchassmartcameras,smartsocketsusingappropriate
VNFS.Theauthorsonlyfocusonsecurityfeaturesandhave
| not discussed | the workflow | of  | these NFV | based security |     |     |     |     |     |
| ------------- | ------------ | --- | --------- | -------------- | --- | --- | --- | --- | --- |
functions.
E. ENERGYAWARESDN/NFVARCHITECTURE
1) MOTIVATION
| The IoT | defines a new    | state of | life where | billions of IoT |           |                                  |     |     |     |
| ------- | ---------------- | -------- | ---------- | --------------- | --------- | -------------------------------- | --- | --- | --- |
| sensors | link to colossal | network  | traffic.   | A programmable  |           |                                  |     |     |     |
|         |                  |          |            |                 | FIGURE18. | Energy-awareSDN/NFVarchitecture. |     |     |     |
networksuchasSDNcancopewithsuchdataexplosionand
resourceconstraintswiththehelpofNFV,whichalsoallows
on-demand network deployment. SDN and NFV support architectureisimplementedwithonly40IoTnodeswithgrid
| each other | for an IoT | architecture | where | many network |          |                      |            |         |           |
| ---------- | ---------- | ------------ | ----- | ------------ | -------- | -------------------- | ---------- | ------- | --------- |
|            |            |              |       |              | topology | in Cooja simulation. | Similarly, | battery | existence |
management challenges can be solved. The authors in [51], is identical across all IoT nodes: a coin-type lithium-ion
proposed an architecture that describes an Integer Linear batterywith3Vand150mA-hpowerrating.Thesuggested
Programming(ILP)problemtomaximizeIoTnodes’energy
architecturefocusesmainlyonIoTnodes’energyusage,not
usagebyenablinganappropriatenumberofNFVnodesand on other features such as fault tolerance, security resource
assigningoptimalnodestothosestartingNFVnodes.
features.
| 2) PROPOSEDFRAMEWORK |     |     |     |     | F. NFV-BASEDIoTSECURITYFORHOMENETWORKS |     |     |     |     |
| -------------------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
As shown in Fig. 18, the authors’ proposed SDN-based 1) MOTIVATION
NFV solution for IoT network includes two modules: NFV IoT networks are not powerful enough to detect malicious
Management Module (NMM) and RoutingManagement codeandprotectthemselvesagainstit.BillionsofIoTdevices
Module (RMM) [51]. NMM consists of a VNF container (estimates vary from 10 to 50 billion by 2020) are fertile
andVNFmanagertopreservetheavailablenetworkfunction ground for various attacks such as DDoS, botnet attacks,
definitions and provide an API to an enabled NFV node. etc., leading to terrorism, data theft, and other security
| RMM node | module maintains | its | neighbors’ | energy-state |     |     |     |     |     |
| -------- | ---------------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- |
concerns[147],[148].Theauthorsin[149]proposedanew
information and shares it with the controller. The controller method to defend multiple IoT devices through a single
usesenergy-stateinformationtoenableanoptimumnumber VNF through the ISP network. The approach is based
ofNFVnodesandcreatescorrespondingenergy-awareroutes on the manufacturer’s use definition (MUD), a Whitelist
maintainedatRMM.Theauthorsuse(ILP)problemandmap management(WLM)IoTprotectionscheme.
itintobroadIoTnetworkstosolvetheenergyconsumptionin
IoTnodes.Theyproposedanalgorithminwhicheachsource 2) PROPOSEDFRAMEWORK
| node has | two shortest routes | to  | the accessible | NFV nodes. |                |          |              |          |             |
| -------- | ------------------- | --- | -------------- | ---------- | -------------- | -------- | ------------ | -------- | ----------- |
|          |                     |     |                |            | Afeketal.[149] | proposed | architecture | as shown | in Fig. 19. |
Everyroutehasarelatedenergycost(totalcontactenergy). The author aims to ensure that all IoT application packets
Thealgorithmsassignthesourcenodetooneoftheavailable complywiththeMUDfileguidelines.Thatmeansthateach
NFVnodesbasedonenergyandactivationcosts.
|     |     |     |     |     | packet passes | to a MUD | file for blocking | or  | not blocking |
| --- | --- | --- | --- | --- | ------------- | -------- | ----------------- | --- | ------------ |
purposes.Thus,theMUDcompliancepresentintheformof
3) CRITICALANALYSIS virtualnetworkserviceisevaluatedbyWLM.WLMdecides
The authors implemented a proposed IoT network energy- whetherornotapacketpassesawhitelist.Thepacketiseither
droppedorenabledinwhitelist/MUDcompliance.
sensitiveSDN-basedNFVarchitecture.Theyusedaheuris-
| tic approach | (EA-SDN/NFV) |     | as the | ILP problem is |     |     |     |     |     |
| ------------ | ------------ | --- | ------ | -------------- | --- | --- | --- | --- | --- |
NP-complete to implement the proposed architecture. The 3) CRITICALANALYSIS
results indicate that the proposed SDN-based NFV solution TheproposedframeworkisimplementedonanISPnetwork
shows better results in terms of IoT node’s energy con- environment as a proof of concept. The data-plane is
sumption.However,ithassomelimitations,forexample,the implementedusingOpenvSwitch(OVS)version2.8.1with
| 70866 |     |     |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     |     |     | FIGURE20. | Context-awareSDNNFVbasedIoTarchitecture. |               |                |          |      |
| --- | --- | --- | --- | --- | --------- | ---------------------------------------- | ------------- | -------------- | -------- | ---- |
|     |     |     |     |     | networks. | Data is collected                        | by            | sensors (e.g., | wearable |      |
|     |     |     |     |     | devices)  | and then distributed                     | via           | IoT gateways   | to MVNO  |      |
|     |     |     |     |     | networks. | After managing                           | the MVNO      | switches,      | the      | data |
|     |     |     |     |     | collected | will eventually                          | be aggregated | and            | analyzed | by a |
centralservicecontroller.Theauthorstoguaranteeprotection
|     |     |     |     |     | and privacy, | data collection, | and processing |             | they segregated |     |
| --- | --- | --- | --- | --- | ------------ | ---------------- | -------------- | ----------- | --------------- | --- |
|     |     |     |     |     | from the     | Internet they    | simultaneously | run several | different       |     |
MVNOnetworksforvariousapplications
| FIGURE19. | IoTsecurityforhomenetworksusingNFV. |     |     |     |     |     |     |     |     |     |
| --------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3) CRITICALANALYSIS
OF 1.3. The CP runs as an application (in Python) over The proposed solution supports IoT heterogeneity through
Ryu(Open-sourceOFcontroller)[149].Theimplementation VNF, which is dynamically generated, modified, moni-
leveragesOVS’scachingcapability,supportingthepipelined tored, and removed according to the network situation’s
OVS and OF architectures, where packets cross several requirements.Thefocusistoprovidefunctionalitiessuchas
|              |                 |              |       |             | discovery | and connectivity | of IoT | devices, | data collection |     |
| ------------ | --------------- | ------------ | ----- | ----------- | --------- | ---------------- | ------ | -------- | --------------- | --- |
| tables, each | having numerous | rules before | being | listed. The |           |                  |        |          |                 |     |
authorsdonotdiscusstheresultoftheproposedarchitecture andencapsulation,andforwarding/processingcontext-aware
indetail.Moreover,thearchitecturelacksmodulesforenergy, packets. The proposed framework runs on a very small
security,andresourcemanagement. testbed, and the viability of the proposed framework for
handlinglargeIoTnetworksisaquestionmark.
G. CONTEXT-AWARESDN-NFV-BASEDIoTARCHITECTURE
| 1) MOTIVATION |     |     |     |     | H. SECURITYINLIGHTWEIGHTNETWORKFUNCTION |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
In supporting data-oriented Internet-of-Things (IoT) appli- 1) MOTIVATION
cations, the current host-centered Internet infrastructure is Smart IoT applications enable many IoT devices and
inefficient, where contextual data packet information is networks to be connected to various applications operating
desirable for in-network forwarding and processing. The onfogandcloudcomputingplatforms.Creatingafederated
authors in [150] proposed a context-aware IoT architecture virtual network is one solution to linking IoT devices with
thatcanforwardandprocessIoTtrafficintheDPtofillthe cloudandfogservices.Thisstrategy’sprimaryadvantageis
gapbetweenIoTandIP,basedoncontextualinformation that the IoT uses an application-specific federated network
wherenotrafficfromotherapplicationspasses,anddevices
2) PROPOSEDFRAMEWORK may communicate with several remote services. Multiple
Du et al. [150] focuses on the prototyping of an IoT traffic cloud providers and IoT networks cover this federated
|            |               |                       |     |        | network, | but it can be | operated | as a single | organization. |     |
| ---------- | ------------- | --------------------- | --- | ------ | -------- | ------------- | -------- | ----------- | ------------- | --- |
| management | context-aware | forwarding/processing |     | mecha- |          |               |          |             |               |     |
nism.Thecontextualinformationistransmittedfrombotha Federated virtual networks can be managed centrally and
sensorlayerandanapplicationlayertomitigateIoTnetwork protected from a security point of view, with a consistent
challenges related to scalability, discoverability, stability, globalsecuritystrategyforIoTnetworks.
| reliability, | computational, | and battery | limitations. | The aim |     |     |     |     |     |     |
| ------------ | -------------- | ----------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
is to allow multiple Mobile Virtual Network Operators 2) PROPOSEDFRAMEWORK
(MVNOS) over shared wireless infrastructures. Therefore, As shown in Fig. 21, the proposed architecture by [151]
to enable SDN services for MVNOs, the architecture uses comprises 3 VNFs within the ETSI NFV architecture: a
programmable switches. On FLARE platform, the IoT deep packet inspection engine (DPI), a firewall (FW), and
gatewayprogramensurestrailerslicing.AsshowninFig.20, an intrusion detection system (IDS). The VNF Manager
theauthorssuggestedasystemdesignedwithslicedMVNO is responsible for developing, upgrading the VNFs, and
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     | 70867 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| FIGURE21. | Securityinlightweightnetworkfunction. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
controllingtheservicefeaturechainingoftheVNFOrches-
trator,puttingNFVwithincontainerstoreducethehardware
requirements on the edge router. To transport data from the FIGURE22. ApplicationofIoTbasedonfogcomputing.
| IoT network     | controller   | to the cloud, | the             | authors | suggested    |     |     |     |     |     |     |     |
| --------------- | ------------ | ------------- | --------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| in the proposed | architecture | that          | it is essential |         | to translate |     |     |     |     |     |     |     |
the IoT data into a protocol that the cloud network can connectedtobasestationsorroutingdevicesbyhigh-capacity
understand.First,theIoTgatewayperformsthistranslation, fibers in this architecture, reducing end-to-end transmission
| and then | the information | is sent | by the | IoT | gateway into |     |     |     |     |     |     |     |
| -------- | --------------- | ------- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
delay.Fognodescanalsobeinstalledontheedgeofthecell
a cloud that gathers the data and performs higher-level network so that the same fog node can be used by various
| processing | and analysis | by providing |     | advanced | network |     |     |     |     |     |     |     |
| ---------- | ------------ | ------------ | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
basestationsorroutingdevicestoprocessdata.Thefognodes
servicessuchasFWandDPI. in the network can be linked to the cloud, allowing full use
oftheprocessingresourcesofthecloudtoincreasenetwork
3) CRITICALANALYSIS deploymentflexibility.Thefognodewilluploadthedatato
IoT-related security is the key objective of the proposed thecloudforprocessingwhenthereisalargeamountofdata
architecture.Theconceptistousevirtualnetworkstoaccess to be processed on the network, and the fog node does not
cloud resources and federate various virtual networks to havesufficientcomputingpower.
controlandprotectthefederatednetworkasasingle,isolated
entity. To implement the proposed security architecture, the 3) CRITICALANALYSIS
| NFV and | SFC are focused | on  | numerous | IoT | and cloud |             |      |      |              |     |           |           |
| ------- | --------------- | --- | -------- | --- | --------- | ----------- | ---- | ---- | ------------ | --- | --------- | --------- |
|         |                 |     |          |     |           | The results | show | that | the proposed |     | framework | decreases |
networks, a global network safety strategy. The authors the delay of task processing and task violation rate, and
presumedthateachIoTandcloudplatformhasanNFV/SFC the resource allocation process’s running time also retains
| infrastructure | used in | each IoT | and | cloud | platform in |                   |     |     |      |           |        |             |
| -------------- | ------- | -------- | --- | ----- | ----------- | ----------------- | --- | --- | ---- | --------- | ------ | ----------- |
|                |         |          |     |       |             | some consistency. |     | The | most | important | factor | influencing |
the federated network to deploy, configure and chain the the completion of user tasks is the computational capacity
protectionVNF.Theauthorsdidnotimplementtheproposed
|     |     |     |     |     |     | of the fog | node. | However, | the | competitiveness |     | of multiple |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | --- | --------------- | --- | ----------- |
architectureforanapplicationandmainlyfocusonsecurity resources can affect the efficient distribution of resources
managementratherthancoverothermanagementissues. in the fog environment due to the fog network’s restricted
|                                         |     |     |     |     |     | hierarchy, | network | communication |     |     | resources, | and storage |
| --------------------------------------- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | --- | --- | ---------- | ----------- |
| I. APPLICATIONOFINTERNETOFTHINGSSERVICE |     |     |     |     |     | resources. |         |               |     |     |            |             |
PLATFORM
| 1) MOTIVATION |     |     |     |     |     | J. GENERALIZEDMOBILENETWORKARCHITECTURE |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
Fog computing and IoT technologies play a prominent 1) MOTIVATION
role in smart city deployment, facilitating the sharing and Serving the future obstacles and setting high capacity
| management | of urban | knowledge. | The | authors | in [152] |         |         |             |     |     |          |             |
| ---------- | -------- | ---------- | --- | ------- | -------- | ------- | ------- | ----------- | --- | --- | -------- | ----------- |
|            |          |            |     |         |          | and low | latency | 5G networks |     | are | the main | factors for |
suggest that fog computing-based SDIoT architecture can transforming the mobile core network. In the existing
havethepotentialtoeffectivelyaddressesbigdataprocessing
|     |     |     |     |     |     | literature, | different | technologies |     | such | as NFV | and SDN are |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------ | --- | ---- | ------ | ----------- |
andnetworkscalabilityissues. being discussed to meet the future needs of 5G networks.
|     |     |     |     |     |     | However, | potential | technologies |     | such | as  | the IoT, video |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ------------ | --- | ---- | --- | -------------- |
2) PROPOSEDFRAMEWORK networks, and others may have numerous requirements that
The authors suggested a fog-based computing and NFV emphasize the need for complex network features to be
| platform | for the IoT | as shown | in Fig. | 22. Fog | nodes are | scalable. |     |     |     |     |     |               |
| -------- | ----------- | -------- | ------- | ------- | --------- | --------- | --- | --- | --- | --- | --- | ------------- |
| 70868    |             |          |         |         |           |           |     |     |     |     |     | VOLUME10,2022 |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
2) PROPOSEDFRAMEWORK maintaintheusablenetworkservice.TheRMMnodemodule
|             |     |                   |     |     |            |     |          | securely | stores | and shares | the | energy-state | information |     |
| ----------- | --- | ----------------- | --- | --- | ---------- | --- | -------- | -------- | ------ | ---------- | --- | ------------ | ----------- | --- |
| The authors | in  | [153] incorporate |     | the | principles |     | of cloud |          |        |            |     |              |             |     |
computing, SDN, and NFV with mobile networks in the of its neighbours with the controller. The controller uses
proposed architecture. The mobile network cloud includes energy-state information to make the maximum number
mapping the network functions needed to integrate mobile of NFV nodes possible and creates energy-aware routes
networkswithSDNtechnologyintheproposedarchitecture. at RMM. The authors in [146] propose a Docker-based
|                 |     |          |            |           |     |         |        | framework | for | deploying | virtual network | security |     | functions |
| --------------- | --- | -------- | ---------- | --------- | --- | ------- | ------ | --------- | --- | --------- | --------------- | -------- | --- | --------- |
| These functions |     | are just | controlled | functions |     | for the | mobile |           |     |           |                 |          |     |           |
network, i.e., MME, HSS, PCRF, and S/P-GW CPs. Trans- atIoTgateways.Thesevirtualfunctionsarestoredinacloud-
port,loadbalancing,defense,policy,charging,tracking,QoE, basedsystem.TheIoTgatewayisinchargeofretrievingthese
or resource optimization are additional functions. With this cloud-based virtual network security functions according
method,onlystrategicallypositionedSDN-capableswitches to their requirements. Authors in [152] proposed an AAA
|     |     |     |     |     |     |     |     | module in | fog | computing-based |     | SDIoT | architecture | that |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | ----- | ------------ | ---- |
andregularswitchescomposetheuserplane.SDNswitches
may either partially or fully replace the existing mobile provides an efficient security mechanism by intelligently
transportnetwork. controlling access to IoT devices through strict access and
auditingpolicies.ThemajorityofproposedSDN-basedNFV
|     |     |     |     |     |     |     |     | solutions, | according | to data | synthesis | driven | Table-7, | lack |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | --------- | ------ | -------- | ---- |
3) CRITICALANALYSIS
|              |     |             |         |     |             |      |      | security modules. |     | Moreover, | most | of the proposed |     | security |
| ------------ | --- | ----------- | ------- | --- | ----------- | ---- | ---- | ----------------- | --- | --------- | ---- | --------------- | --- | -------- |
| The proposed |     | framework’s | testbed |     | illustrates | that | some |                   |     |           |      |                 |     |          |
modulesarecorrelatedtoenergymanagementsolutions,and
| of the | needs of | 5G mobile |     | networks | are | met | by the |     |     |     |     |     |     |     |
| ------ | -------- | --------- | --- | -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
onlyafewofthemareimplementedinreal-worldscenarios.
| planned        | architecture | with       | SDN                | and NFV      | integration. |             | The     |                 |               |             |                  |           |                 |         |
| -------------- | ------------ | ---------- | ------------------ | ------------ | ------------ | ----------- | ------- | --------------- | ------------- | ----------- | ---------------- | --------- | --------------- | ------- |
|                |              |            |                    |              |              |             |         | RQ2:            | How can       | SDN-based   | frameworks       |           | provide         | effec-  |
| findings       | also show    | the        | advantages         | of           | SDN          | that        | enhance |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | tive fault      | tolerance     | management  |                  | solutions | to large-scale  |         |
| the successful | and          | efficient  | use                | of resources |              | with        | reduced |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | IoT networks?   |               | In [140],   | the authors      | explore   | fault           | toler-  |
| overhead       | when         | used in    | the backhaul.      |              | The          | testbed     | results |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | ance techniques |               | using NFV   | Management       | and       | Orchestration   |         |
| show high      | latency      | when       | transferring       |              | VMs          | with        | network |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | (NFV-MANO).     |               | The SDN     | controller       | manages   |                 | the NFV |
| components     | (e.g.,       | MME        | or S/P-GW)         |              | due          | to HW       | failure |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | orchestration   | unit          | responsible | for              | providing | the virtualized |         |
| or when        | additional   | processing |                    | resources    | are          | needed.     | The     |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | network’s       | functionality |             | through standard |           | interfaces.     | After   |
| work lacks     | the          | discussion | on virtualization, |              |              | efficiency, | and     |                 |               |             |                  |           |                 |         |
|                |              |            |                    |              |              |             |         | receiving       | the network   | topology    | and              | policy    | demands,        | the     |
robustnessoftheproposedframework.
|     |     |     |     |     |     |     |     | control module |         | decides   | the optimal | function | assignments |          |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --------- | ----------- | -------- | ----------- | -------- |
|     |     |     |     |     |     |     |     | (assigning     | network | functions | to specific | VMs).    | It          | converts |
K. DISCUSSIONOFRESULTS thelogicpolicy’sspecificationsintooptimizedroutingpaths.
NFV has been described as the most promising choice for TheauthorsofferedVIM(virtualinfrastructuremanager)in
the versatile programmability of network control functions the proposed architecture to govern and manage Network
andprotocolsforthedynamicuseofnetworkresources.SDN Function Virtualized Infrastructure resources in its domain
abstractsnetworkresourcesintowell-definedAPIs,allowing with fault management of hardware, software, and virtual
IoT networks to be topology-independent. We thoroughly resources in IoT networks in their paper [137]. The author
examined each of the primary studies chosen during the [139] discusses the reference multi gateway architecture
SLR and classified them into SDN-based NFV taxonomy in which network elements such as the Network Control
based on the management challenges of IoT. With the Centre(NCC)andtheNetworkManagementCentre(NMC)
support of SDN-based NFV solutions, we have addressed are responsible for managing fault tolerance performance
various techniques identified in the existing literature to by managing network function virtualization according to
solve IoT management challenges. Table-8 summarizes the their needs. Authors in [142] discuss NFV-RA (network
merits and demerits of the SDN-based IoT-NFV solu- function virtualization-resource allocation )strategies with
tions under consideration. Based on the above discussion, reference to QoS to manage fault tolerance. Table-7 shows
we summarize the answers to the research questions as that the majority of proposed SDN-based NFV solutions
follows: are proposed with a fault tolerance approach to manage
| RQ1: | How can | SDN-based |     | frameworks |     | provide | effi- | IoTnetworks. |     |     |     |     |     |     |
| ---- | ------- | --------- | --- | ---------- | --- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
cient security solutions to manage IoT network-related RQ3: What are the potential solutions regarding
securityissues?ToprovideefficientsecuritysolutionstoIoT load balancing in SDN-based frameworks to manage
networkswithNFVbasedSDNintegration,Alametal.[47] IoT networks? Authors in [138] discusses the suitable
explored how to incorporate the virtual security feature approachesofloadbalancinginSDN-basedNFVframework
into the SDN-based NFV architecture. They are focusing incontrollerwiththehelpofaccessrules,suchasBroadband
more on network-layer security protocols such as routing RemoteAccessServe(BRAS),etc.Accordingtotheauthors
algorithms,context-awareforwardingofIoTtrafficetc.The in [152], a fog computing-based SDIoT architecture will
authors introduced the NFV Management Module (NMM) effectivelysolvebigdataprocessingandnetworkscalability
and the safe Routing Management Module in [51]. The issues in terms of load-balancing to manage IoT networks
NMM includes a VNF container and a VNF manager to withthehelpofSDNbasedNFVframework.Table-7shows
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     | 70869 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE7. SummaryofSDN-basedIoT-NFVsolutionsthataddressesIoTmanagementchallenges.
TABLE8. MeritsanddemeritsofproposedSDN-basedIoT-NFVsolutions.
thatthemajorityofproposedSDN-basedNFVsolutionsare securityfunctionsfromthecloud.Afeketal.[149]proposed
proposed with a load-balancing approach to managing IoT a scalable SDN-based NFV architecture for the various
networks,butalimitedofthemareimplemented. distributed scalable forms of attacks, such as DDoS, etc.
RQ4: What scalable solutions can be offered by According to Table-7, most proposed SDN-based NFV
SDN-based frameworks to manage IoT networks? With solutionsarescalable,andhencethischallengeistackledon
the support of a distributed SDN controller, Li et al. [155] differentlevelswithvarioussolutions.
proposed an SDN-based NFV architecture to manage IoT RQ5:HowcanSDN-basedframeworksenableefficient
networksthroughvirtualnetworkingfeaturessuchasrouting, powerconsumptioninIoTnetworks?In[145],theauthors
safe tunneling between IoT gateways, and traffic prioriti- presentedadistributed,secureBlackSDNIoTarchitecturefor
zation for QoS in a scalable manner. The authors in [146] smart cities that included NFV implementation. For energy
suggested a Dockers-based architecture for deploying vir- conservation, load balancing, and network scalability, the
tual network security functions at IoT gateways. These proposed unified Black SDN-IoT architecture with NFV is
virtual functions are stored in the scalable cloud. The IoT being considered for smart cities. The authors implemented
gateway is in charge of retrieving these virtual network severalhierarchicalSDNcontrollersintheproposedsystem
70870 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| to improve  | availability, |     |           | credibility, | and         | confidentiality, |              |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | --------- | ------------ | ----------- | ---------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| among other | things.       |     | Li et al. | [155]        | in proposed |                  | architecture |     |     |     |     |     |     |     |
haveenergyefficientsecurenetworkingfeaturesatnetwork
layersuchasrouting,safetunnelingbetweenIoTgateways.
| According     | to Table-7, |             | the majority |        | of proposed |     | SDN-based  |     |     |     |     |     |     |     |
| ------------- | ----------- | ----------- | ------------ | ------ | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| NFV solutions |             | are missing |              | energy | management  |     | solutions. |     |     |     |     |     |     |     |
Mostoftheproposedefficientenergymanagementmodules
| are related | to  | security | management |     | solutions, | and | very few |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ---------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
areimplemented.
|     |     |     |     |     |     |     |     | FIGURE23. | Middleware-BasedSDNcontroller. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------------ | --- | --- | --- | --- | --- |
VI. MIDDLEWARE-BASEDSDNMANAGEMENT
FRAMEWORKS
| A middleware  |     | layer         | for the | IoT        | environment |      | is required |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | ------- | ---------- | ----------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| for different |     | applications. |         | The common |             | goal | of all the  |     |     |     |     |     |     |     |
middlewarelayerdevelopmentinIoTistodevelopaframe-
| work that         | can        | allow      | a plug-n-play |                 | adaptation  |                  | layer [156]. |           |                                                 |     |     |     |     |     |
| ----------------- | ---------- | ---------- | ------------- | --------------- | ----------- | ---------------- | ------------ | --------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Among             | all the    | various    | devices       | belonging       |             | to               | diverse IoT  |           |                                                 |     |     |     |     |     |
| domains,          | it is      | difficult  | to            | define          | and enforce |                  | a common     |           |                                                 |     |     |     |     |     |
| standard.         | Middleware |            | acts          | as a bond       | that        | joins            | together     |           |                                                 |     |     |     |     |     |
| the heterogeneous |            | components |               | [157].          | IoT         | has              | a software   |           |                                                 |     |     |     |     |     |
| framework         | known      | as         | middleware    | that            | basically   |                  | provides an  |           |                                                 |     |     |     |     |     |
|                   |            |            |               |                 |             |                  |              | FIGURE24. | Cloud-basedpublishandsubscribemiddlewareforIoT. |     |     |     |     |     |
| abstraction       | from       | items      | to            | applications    | and         | offers           | multiple     |           |                                                 |     |     |     |     |     |
| services.         | The        | middleware |               | layer addresses |             | interoperability |              |           |                                                 |     |     |     |     |     |
acrossheterogeneousdevicesthatserveinvariousapplication
2) PROPOSEDFRAMEWORK
| domains,   | adaptations, |          | context      | awareness, |          | discovery | and         |                   |     |          |            |         |       |     |
| ---------- | ------------ | -------- | ------------ | ---------- | -------- | --------- | ----------- | ----------------- | --- | -------- | ---------- | ------- | ----- | --- |
|            |              |          |              |            |          |           |             | Antonicetal.[161] |     | proposed | a solution | (CUPUS) | based | on  |
| management | of           | devices, | scalability, |            | privacy, | and       | security in |                   |     |          |            |         |       |     |
content-basedpublish-subscribewithdistributedcloudhelp,
theIoTenvironment[158].
asshowninFig.24.Thecentercloudnodesareresponsible
SDN-based middleware is now becoming quite popular for collecting information from the subscriber nodes for
| as a way         | to manage |     | and control | networks. |        | A typical          | SDN- |            |     |      |            |              |           |     |
| ---------------- | --------- | --- | ----------- | --------- | ------ | ------------------ | ---- | ---------- | --- | ---- | ---------- | ------------ | --------- | --- |
|                  |           |     |             |           |        |                    |      | processing | and | data | analytics. | The proposed | framework |     |
| based middleware |           | is  | shown       | in Fig.   | 23. In | this architecture, |      |            |     |      |            |              |           |     |
consistsoftwoessentialcomponents,themobilebrokerand
| middleware | logic | connected |     | with the | software |     | components |           |         |     |               |        |                |     |
| ---------- | ----- | --------- | --- | -------- | -------- | --- | ---------- | --------- | ------- | --- | ------------- | ------ | -------------- | --- |
|            |       |           |     |          |          |     |            | the cloud | broker. | The | mobile broker | module | is responsible |     |
residesattheSDN-basedCP.SwitchessendtheOFmessages
fordatafilteringanddataacquisitionofconnectedsensors.,
to the middleware, which is processed by the middleware while the cloud broker module in the proposed framework
| components | [159].      | These | components |     | perform |          | the task of |                |     |            |       |      |                   |     |
| ---------- | ----------- | ----- | ---------- | --- | ------- | -------- | ----------- | -------------- | --- | ---------- | ----- | ---- | ----------------- | --- |
|            |             |       |            |     |         |          |             | is responsible | for | processing | a big | data | stream to perform |     |
| adapting   | the network |       | behavior   | and | sending | messages | back        |                |     |            |       |      |                   |     |
dataanalyticsfortheIoTgadgets.Theauthorshaveevaluated
tothenetworkdevices.Sucharchitectureenablesadaptation
theirproposedframeworkintermsofpropagationdelayfrom
| of the network |     | based | on  | the prevailing |     | network | situation |           |            |       |        |             |        |        |
| -------------- | --- | ----- | --- | -------------- | --- | ------- | --------- | --------- | ---------- | ----- | ------ | ----------- | ------ | ------ |
|                |     |       |     |                |     |         |           | IoT nodes | to central | cloud | nodes. | The authors | used a | Citrix |
controller for classifying the legitimate user that has been XenServer virtualization software and 20,000 subscription
| involved | in the | network | [160]. | This | section | will | discuss all |     |     |     |     |     |     |     |
| -------- | ------ | ------- | ------ | ---- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
nodesinasimulatedenvironmenttoimplementtheproposed
theeffortsthathaveadoptedamiddleware-basedapproachto
framework.
manageIoTnetworks.
3) CRITICALANALYSIS
|     |     |     |     |     |     |     |     | CUPUS | middleware | is  | designed | for handling | the resource- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | -------- | ------------ | ------------- | --- |
A. CLOUD-BASEDPUBLISH/SUBSCRIBEMECHANISM
| FORIoT |     |     |     |     |     |     |     | constrainedrequirementsofIoTgadgets.Theresultsuggests |          |           |     |          |          |         |
| ------ | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | -------- | --------- | --- | -------- | -------- | ------- |
|        |     |     |     |     |     |     |     | that the                                              | proposed | framework |     | controls | the data | density |
1) MOTIVATION
Mobilecrowdsensing(MCS)isanewtrendofdevelopment by filtering closer to the production place. Authors never
in IoT applications. Mobile nodes are scattered in large discuss cloud brokers’ and mobile brokers’ details in the
implementation,whichmeansthattheresultcanbedeflected
networkformscapableofsensingandcomputingcollectively
share data with the help of distributed cloud structure. Due indifferentscenarios.
| to mobility | nature | architecture, |     | MCS | has | to face | dynamic |     |     |     |     |     |     |     |
| ----------- | ------ | ------------- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
environments comprising sensors, heterogeneous mobile B. PUBLISH/SUBSCRIBESYSTEMFORLOADBALANCED
devicesthatmakeitnecessarytohaveenergyefficiencyand TOPIC-BASEDSDN
context-aware for community sense. That means both the 1) MOTIVATION
sensinganddatatransmissionprocessesfrommobiledevices IoT in the future has severe challenges due to the massive
andthecloudneedtobemanagedeffectively. stream of data movement in multi-source sensors. The
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     | 70871 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
traditional techniques in IoT infrastructure to address these forsuchaframeworkthatovercometheseissuesandprovide
challenges are insufficient because of the absence of a improvedserviceintheIoTnetwork.SDNhasthepotential
global traffic information center. The topic-based publish- toprovidesuchanovelIoTframeworkwiththehelpofdata
subscribe system is a special kind of publish-subscribe distributionservicemiddleware.
| mechanism | in  | which | events | are published |     | with | specific |                      |     |     |     |     |     |
| --------- | --- | ----- | ------ | ------------- | --- | ---- | -------- | -------------------- | --- | --- | --- | --- | --- |
|           |     |       |        |               |     |      |          | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |
identifierscalledtopics.Publisherbroadcastthistopictothe
Hakirietal.[163]identifiesfivemainbarrierstonetworking.
| concerned | subscribers. |     | This | publish-subscribe |     | mechanism |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ---- | ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Currentstandardizationattemptsatvariouslevelsofthepro-
| tends to | manage | the | IoT network | more | efficiently |     | with the |     |     |     |     |     |     |
| -------- | ------ | --- | ----------- | ---- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
tocolstacksforIoTareisolated.Theauthorshaveproposed
helpofSDN.
6LowPANprotocolsonthenetworklayerbetweenMediaAc-
cessControl(MAC)andIPv6.TheprotocolrequiresIPv6to
2) PROPOSEDFRAMEWORK runonresource-limitedcomputers.ROLL(RoutingforLow
Wangetal.[162] have proposed an SDN topic-based PowerandLossNetworks)oftenaddressesroutingproblems
| publish-subscribe |     | system | known | as  | SDNPS. | The | pro- |         |                     |     |                  |     |             |
| ----------------- | --- | ------ | ----- | --- | ------ | --- | ---- | ------- | ------------------- | --- | ---------------- | --- | ----------- |
|                   |     |        |       |     |        |     |      | for low | power applications. |     | CoAP (Constraint |     | Application |
posed architecture is partitioned into multiple clusters. Protocol) is on the application layer, a specially developed
| These clusters |     | are belonging |     | according | to  | their | regional |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | --------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
applicationprotocolforresource-limiteddevicesthatcomply
characteristics. The different logically autonomous areas withthe6LowPANprotocoltoprovideapplicationservices.
represent each cluster in the topology. The clusters are M2Mmovementshavearisentopromotetheimplementation
communicatingwitheachotherthroughthebordergateway.
|     |     |     |     |     |     |     |     | of the end-to-end | IoT | architecture. | These | standards | need to |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------- | ----- | --------- | ------- |
Atthetopoftheproposedarchitecture,globalserversmanage be combined and interoperated to make them the possible
the whole topology and compute routing efficiently. The endoftheIoTendarchitecture.SinceIoTdevicesarehighly
authors proposed a framework to implement an efficient mobile, the need to handle the versatility of IoT devices
routing protocol based on topic connected overlay called has earned a high degree of interest from them effectively.
| the minimal | cost | topic-connected |     | overlay |     | (MCTCO) | that |     |     |     |     |     |     |
| ----------- | ---- | --------------- | --- | ------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
SDNcanhelpmanageversatilityasitmaintainsafullview
operates by creating an improved routing plan. The global of the network but offers an increasingly mobile network
view of the topology is acquired by collecting a link-state. whichwillbeachallenge.InIoTenvironments,middleware
Publish/subscribe paradigm then guarantees that distributed is required to propagate activities to destinations of interest
everyneweventtotheconnectedsubscriberswhoseinterest in an asynchronous position. TCP is not sufficient for IoT
| in the topic | similar. |     | The proposed | framework |     | consists | of a |     |     |     |     |     |     |
| ------------ | -------- | --- | ------------ | --------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
scenarios,andareliabletransportprotocolisexpectedtobe
three-layer, switch hardware layer, cluster controller layer, studied for IoT situations. Finally, there is no infrastructure
and the global management layer. The switch layer is to provide defense in IoT as traditional defense systems
responsible for taking information from the IoT nodes or are dynamic and complex. Hakiri et al. [163] added Data
agents with the OF protocol’s help or Southbound API and DistributionService(DDS)middlewarebetweenIoTappand
passontotheSDNcontroller.Theglobalmanagementlayer
|     |     |     |     |     |     |     |     | SDN (Open | daylight) | controller | with the | help | of the NBI |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | -------- | ---- | ---------- |
consists of two types of servers for single-point failure, interface.Theproposedframeworkaddressesthehighlighted
i.e., a major server and a standby server. These servers issue as follows. DDS middleware allows cross-domain or
containinformationonoveralltopologyandroutingpolicies.
cross-platforminteroperability,allowsreconfigurationofIoT
Moreover, the proposed framework maintains two kinds of devicesaccordingtotheirenvironmentrequirement,supports
| topology, | i.e., | subscription | topology |     | and physical | topology. |     |          |               |          |            |             |     |
| --------- | ----- | ------------ | -------- | --- | ------------ | --------- | --- | -------- | ------------- | -------- | ---------- | ----------- | --- |
|           |       |              |          |     |              |           |     | multiple | communication | patterns | in a large | distributed | IoT |
IBM server with 16 GB memory is used to implement the system, and provides security mechanism with the help of
| scenariointhree-hoptopology. |     |     |     |     |     |     |     | imposingsecuritypolicies. |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
|                              |     |     |     |     |     |     |     | 3) CRITICALANALYSIS       |     |     |     |     |     |
3) CRITICALANALYSIS The proposed architecture is merely a conceptual represen-
One of the shortcomings of the proposed framework is that tation, and the authors have provided no implementation of
| SDNPS | has to | compute | the topic | tree | and maintain |     | clusters |                 |       |       |           |                |       |
| ----- | ------ | ------- | --------- | ---- | ------------ | --- | -------- | --------------- | ----- | ----- | --------- | -------------- | ----- |
|       |        |         |           |      |              |     |          | their approach. | Thus, | there | have been | no reliability | tests |
in the network. The creation of a topic tree would require andevaluationsofthearchitectureunderdifferentproduction
extracomputation.Theauthorsneverdiscusshowtomanage
|             |        |             |     |         |         |            |     | conditions.     | This middleware |            | approach, | together     | with the |
| ----------- | ------ | ----------- | --- | ------- | ------- | ---------- | --- | --------------- | --------------- | ---------- | --------- | ------------ | -------- |
| the cluster | of SDN | controllers |     | because | cluster | management |     |                 |                 |            |           |              |          |
|             |        |             |     |         |         |            |     | SDN controller, | often           | adds extra | strain    | or overheats | to the   |
wouldrequireadditionalcomputationandstoragetopreserve provisionofIoTapplications.
theclusterstate.
|                                      |     |     |     |     |     |     |     | D. PUBLISHED/SUBSCRIBEENABLEDCOMMUNICATION |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| C. PUBLISH/SUBSCRIBEENABLEDSDNFORIoT |     |     |     |     |     |     |     | PLATFORMFORIoTUSINGSDN                     |     |     |     |     |     |
| 1) MOTIVATION                        |     |     |     |     |     |     |     | 1) MOTIVATION                              |     |     |     |     |     |
IoT infrastructure in the future will face many challenges The exponential growth of IoT gadgets and services/
relatedtomobilitymanagement,integrationwithtraditional applications opens new challenges for researchers in man-
communication protocol, security, etc. There is a high need aging IoT services/applications efficiently. IoT applications
| 70872 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     |     | services | to meet | the event | constraints |     | such | as  | end-to-end |
| --- | --- | --- | --- | -------- | ------- | --------- | ----------- | --- | ---- | --- | ---------- |
latency,lossrate,etc.
3) CRITICALANALYSIS
|     |     |     |     | The proposed |     | architecture | facilitates    |     | the       | access | of various |
| --- | --- | --- | --- | ------------ | --- | ------------ | -------------- | --- | --------- | ------ | ---------- |
|     |     |     |     | IoT services | to  | a single     | middleware     |     | approach. |        | The author |
|     |     |     |     | implemented  | a   | prototype    | by considering |     | thesame   |        | deployed   |
topologyinDistrictHeatingControlandInformationService
|     |     |     |     | System | (DHCISS) | in  | Beijing | and | evaluating | the | proposed |
| --- | --- | --- | --- | ------ | -------- | --- | ------- | --- | ---------- | --- | -------- |
architecture’scorrectnessandfeasibility.Theauthordoesnot
|     |     |     |     | discuss  | the detail | of the   | performance    |     | evaluation |             | parameter |
| --- | --- | --- | --- | -------- | ---------- | -------- | -------------- | --- | ---------- | ----------- | --------- |
|     |     |     |     | involved | in the     | proposed | architecture’s |     |            | throughput. | The       |
presentedevaluationgraphdoesnotcontainsufficientinfor-
|     |     |     |     | mation; | no security | scenarios |     | are discussed |     | in the | proposed |
| --- | --- | --- | --- | ------- | ----------- | --------- | --- | ------------- | --- | ------ | -------- |
system.
E. SDN-INTEGRATEDFRAMEWORKFORIoTTRAFFIC
MANAGEMENT
1) MOTIVATION
|     |     |     |     | The increasing        |          | usage    | of IoT   | raises         | challenges  |             | in manag-  |
| --- | --- | --- | --- | --------------------- | -------- | -------- | -------- | -------------- | ----------- | ----------- | ---------- |
|     |     |     |     | ing heavy             | network  | traffic  | and      | maintaining    |             | the         | quality of |
|     |     |     |     | service requirements. |          | Most     | IoT      | devices        | have        | differences | in         |
|     |     |     |     | processing,           | storage, | power,   | and      | functionality, |             | which       | cause      |
|     |     |     |     | complex               | issues   | for QoS, | resource |                | allocation, | and         | network    |
|     |     |     |     | configuration         | in       | the IoT  | network. |                | There       | is a high   | need to    |
FIGURE25. SDN-basedpublish/subscribeserviceframework. build middleware-based QoS strategies to better serve IoT
applicationsbyknowinghowIoTdevicestransmitdataand
howapplicationsconsumethatdata.
| need QoS      | requirements, | such as no latency | and high data   |     |     |     |     |     |     |     |     |
| ------------- | ------------- | ------------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| rate required | in real-time  | data analytics     | and processing. |     |     |     |     |     |     |     |     |
2) PROPOSEDFRAMEWORK
DifferentiatedQoSisanothercriticalissuethatplaysavital
|     |     |     |     | The authors | in  | [165] proposed |     | an SDN | QoS | control-based |     |
| --- | --- | --- | --- | ----------- | --- | -------------- | --- | ------ | --- | ------------- | --- |
roleincreatingseriousdelaysintheIoTnetwork.
|     |     |     |     | publish-subscribe |     | model     | to manage |             | the IoT | networks. | The |
| --- | --- | --- | --- | ----------------- | --- | --------- | --------- | ----------- | ------- | --------- | --- |
|     |     |     |     | PS-IoT            | SDN | framework | is        | a QoS-aware |         | framework | for |
2) PROPOSEDFRAMEWORK managingIoTtrafficaggregatedintoFog-likeIoTgateways
The authors in [164] proposed an SDN-based pub- alongthenetworkedge.Theauthorfirstdiscussestheexisting
lish/subscribecommunicationplatformresponsibleforcoun- architecture PSIoT-Orch framework created to manage IoT
teringtypicalIoTnetworks’issues.Theauthorimplementsa networks during massive traffic situations generated by
topic-basedpublish/subscribeparadigmunderSDNasadata growingIoTdevices.ThearchitectureusesPublish/Subscribe
distributionservice,whichcommunicateseventsbetweenIoT to allow IoT data transfer among producers and consumers
connectednodes.Theproposedarchitectureconsistsofthree nodes and efficiently handle network resources at the edge
layers: the infrastructure layer, the network layer, and the level based on the QoS requirement. A traffic orchestrator
application layer, as shown in Fig. 25. The infrastructure moduleintheproposedarchitectureresponsibleformanag-
layerconsistsofsensors/actuatorsresponsibleforgenerating ing traffic policies in IoT networks, IoT gateway, or data
data and then delivering it to the connected nodes. The aggregators (IoT gateway) acts as Pub/Sub. The Pub/Sub
network layer consists of many SDN-configurable switches componentisaccountableformanagingdata-prepossessing,
responsible for providing network service. SDN controller backup, or caching and cloud processing center. Here
is responsible for managing sub-modules such as topology the centralized orchestrator must play an essential role in
management, routing service, flow-table management, the communication of clients and producers nodes. The
packet scheduler, etc. The application layer interacts with centralized orchestrator is responsible for the flowing of
the message bus called local processing brokers, which IoT data according to the IoT data characteristics. The
implementthetopic-orientedpublish/subscribeservice.The orchestratorknowseachIoTgatewayaccordingtothetopic
messagebusreceivesdatafromsensors/actuators,combines subscription.Theobjectiveistoaccomplishbothedgelevel
them in a predefined format, and puts them on SDN and system level QoS in the IoT network by utilizing
infrastructure to transmit. The network layer is responsible the QoS management capabilities coupled with SDN-based
forforwardingeventsefficientlyandprovidingdifferentiated networklinkbandwidthallocation.ThePS-IoTorchestrator
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     | 70873 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
communicates to the SDN controller by requesting the G. STATEFULSDNSOLUTIONFORWIRELESSSENSOR
| communication | path | set | up with the | interface | provided |     |     |     |     |     |     |     |     |
| ------------- | ---- | --- | ----------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
NETWORKS
in the SDN controller sub-block. The MAM module is 1) MOTIVATION
| responsible | for bandwidth |     | sharing through |     | the bandwidth |     |          |        |          |      |         |            |          |
| ----------- | ------------- | --- | --------------- | --- | ------------- | --- | -------- | ------ | -------- | ---- | ------- | ---------- | -------- |
|             |               |     |                 |     |               |     | Wireless | sensor | networks | have | similar | challenges | that IoT |
allocation model strategy. This module keeps track of the networksface,withlimitedenergy,processing,andmemory
used bandwidth for all links over the path between IoT availability.Thereisaneedformiddlewaresolutionsthatcan
| producer | and IoT | consumer | calculated | using | the | routing |     |     |     |     |     |     |     |
| -------- | ------- | -------- | ---------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
managethewirelessnetworkmoreefficientlyandovercome
algorithm. The SDN controller creates entries on the Open theexistingproblemsintheWSNdomain.Withthehelpof
Flowswitchesinvolvedinthepath.
theSDN-WISEsolution,wirelessnetworkscanbeefficiently
managedandbecameadaptablewithprogrammability.
3) CRITICALANALYSIS
Theproposedarchitecturefocusesonhowdataistransferred, 2) PROPOSEDFRAMEWORK
| discovered, | shared, | and consumed | to  | manage | IoT networks |     |         |          |          |     |           |       |         |
| ----------- | ------- | ------------ | --- | ------ | ------------ | --- | ------- | -------- | -------- | --- | --------- | ----- | ------- |
|             |         |              |     |        |              |     | Authors | in [167] | proposed | a   | framework | based | on SDN. |
better to adopt the SDN paradigm. The proposed architec- SDN-WISE network maintains three data structures, state
ture’s evaluation results generate more massive throughput array,IDsarray,andWISEflowtable.IDarrayisresponsible
| when bandwidth |     | is distributed | among | the | framework’s |     |             |        |     |      |         |           |             |
| -------------- | --- | -------------- | ----- | --- | ----------- | --- | ----------- | ------ | --- | ---- | ------- | --------- | ----------- |
|                |     |                |       |     |             |     | for keeping | sensor | IDs | in a | current | scenario. | State array |
IoT QoS levels. With these positive results, the proposed maintainsthetableofphysicalstatesandstatisticalreportsof
framework is validated for its usefulness in managing QoS existingIoTnodes,whiletheWiseflowtableisaccountable
| for IoT traffic. | The | authors | only focus | on  | QoS | in the |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
fortakinginformationfromthecontrollerandbuildtheflow
implementation,andthesecurityandscalabilityissuesarenot tableaspertherequirement.Thecontrollerisresponsiblefor
discussedintheimplementedscenarios.
|     |     |     |     |     |     |     | defining   | the network | management |       | policies   | to  | the connected |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | ----- | ---------- | --- | ------------- |
|     |     |     |     |     |     |     | IoT nodes. | The         | sensor     | nodes | work under | the | DP protocol   |
F. MIDDLEWARESSD-IoTFRAMEWORK stack to communicate with other sensing nodes. The sink
1) MOTIVATION node provides a bridge between sensors and controllers
Conventional storage and security mechanisms cannot be through WISE-Visor. This middleware is responsible for
implementedtomanagetheIoTdevicesandnetworksdueto generating local topology information with the help of
theirlimitedresources,sothereisaneedforsuchaplatform the topology discover protocol. The sensor nodes at the
|             |      |         |                  |     |      |     | forwarding | layer | are accountable |     | for | handling | the sensor |
| ----------- | ---- | ------- | ---------------- | --- | ---- | --- | ---------- | ----- | --------------- | --- | --- | -------- | ---------- |
| to overcome | this | problem | in IoT networks. |     | With | NFV |            |       |                 |     |     |          |            |
middleware,multipleSDN-basedfunctionsareimplemented traffic according to the flow table. At the INPP layer, data
tomanagetheIoTnetworks. aggregationisperformed.TheTD(Topologydiscoverylayer)
isresponsibleforencapsulatingtheinformationoftopology
intheheader.
2) PROPOSEDFRAMEWORK
| Authors in | [166] | proposed | an architecture |     | that has | three |     |     |     |     |     |     |     |
| ---------- | ----- | -------- | --------------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
components,i.e.,physicallayer,control(middleware)layer, 3) CRITICALANALYSIS
and application layer. IoT sensors are responsible for The proposed framework is implemented with the help of
collecting data at the physical layer and providing this data wireless module EMB-Z2530P, which acts as sensor nodes.
to the successive layer. The physical layer maintains the The testbed is created with the help of five sensor nodes
database pool for different reasons, such as keeping the and one sink node. SDN-WISE Controller using Dijkstra’s
configuration of each IoT connected node. Physical Layer algorithmforroutingthepacketsinwhich5000datapackets
|     |     |     |     |     |     |     | of connected | sensor | nodes | are | sent every | 15  | seconds. The |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----- | --- | ---------- | --- | ------------ |
communicateswithmiddlewarewiththehelpofSouth-bound
API in the SDN controller. The middleware comprises evaluation results show that the proposed framework is
differentnetworkfunctionsbasedontheSDNcontroller,and efficient under a particular testbed and allows adaptability
the lower layer calls the IoT controller according to their according to the requirement. The authors of the proposed
requirement. frameworkneverdiscusstheoverheadoftopologydiscovery
protocolpresentinWISE-VISORmiddleware.
3) CRITICALANALYSIS
Theauthor’sproposedframeworkisverygeneric.Integration H. SOFTWARE-DEFINEDNETWORKINGPRINCIPLESIN
| of various | SDN-based | network | functions | such | as Software |     | WSN |     |     |     |     |     |     |
| ---------- | --------- | ------- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
defined storage (SDStore) and Software defined security 1) MOTIVATION
(SDSec) should be evaluated because such functions will SDN is an essential building block for the structured
produceoverheadintheIoTtraffic.Noimplementationand low-costapplicationhardwareoff-the-shelfandstillachieves
evaluationresultsoftheproposedarchitecturearepresented; customization necessary for individual deployments. SDN
hencethereisnowayofknowingwhethersuchmiddleware can be used for various purposes, including networking,
isfeasibletoimplement. networkprocessing,andWSNadministrationtasks.
| 70874 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Jacobssonetal.[168] proposed an SDN-based WSN archi- Jacquenetetal.[169]proposedanarchitectureforSDN-based
tecture to manage WSN with SDN layers. The proposed IoT networks. In addition to the proposal, the authors
architecture counters the issue of scalability and reconfigu- also introduced two IoT services: eHealth and energy
ration of WSN networking. The WSN node is attached to management.eHealthrequiresnetworkinfrastructurewhich
a local controller that accepts and executes directions from is highly reliable in preserving data integrity. In addition
the central controller. At the top of the controller, one or to this, some eHealth scenarios require quick reaction time
moreapplicationscanbeplaced.Localcontrollersarepresent and would probably need dynamic route computation for
withinthesensornodesthatwillchangeboththeMACand sending data. The authors’ second use case is large-scale
theroutingbehaviorofthesensingnodesthemselves.These IoT dynamic energy distribution management. With an
controllers take commands from the central controller. The SDN-based IoT network for energy distribution, it will be
localcontrollerthatresidesinthesensornodesisresponsible possibletoeffectivelyimplementtrafficforwardingpolicyin
formodifyingandcontrollingthecode.Modificationcanbe the IoT network. Through the help of data analytics on the
achievedeitherbyalteringtheparameters(e.g.,adjustingthe datacollectedfromtheIoTnetworkevents,theperformance
central frequency of the antenna, MAC layer repropagation of the IoT infrastructure is evaluated. The research has
cap, modifying the outputs in the forwarding table, etc.) effectively used SDN to manage the IoT services. They
or by installing new features (e.g., virtual machines, native havedistinguishedpoliciesfortrafficforwardingtoprioritize
software, and dynamically connected libraries) that would trafficintheIoTnetwork.
| change | the behavior | of  | the network. |     | Forwarding | and | many |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------------ | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
routing decisions are made at individual nodes. However, 3) CRITICALANALYSIS
| long-term | decisions, | such | as  | the protocols |     | and parameters |     |     |     |     |     |     |     |     |
| --------- | ---------- | ---- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Theauthorsdonotdiscusstheprototypeimplementationof
| to be used, | are            | taken by    | the | central     | controller.   | The     | central |              |                |              |         |             |            |                |
| ----------- | -------------- | ----------- | --- | ----------- | ------------- | ------- | ------- | ------------ | -------------- | ------------ | ------- | ----------- | ---------- | -------------- |
|             |                |             |     |             |               |         |         | the proposed | framework.     |              | Details | of the      | algorithms | used for       |
| controller  | is responsible |             | for | discovering | the           | current | topol-  |              |                |              |         |             |            |                |
|             |                |             |     |             |               |         |         | architecture | implementation |              | were    | also found  | to         | be missing.    |
| ogy and     | connection     | performance |     | of          | the connected |         | nodes.  |              |                |              |         |             |            |                |
|             |                |             |     |             |               |         |         | The work     | is simply      | a conceptual |         | undertaking |            | in its current |
To determine the quality of the connections, the controller state. Details of the functions of the proposed architecture
| used Link   | Quality | Estimation(LQE). |     |     | The    | controller | is  |         |          |           |             |            |      |              |
| ----------- | ------- | ---------------- | --- | --- | ------ | ---------- | --- | ------- | -------- | --------- | ----------- | ---------- | ---- | ------------ |
|             |         |                  |     |     |        |            |     | are not | provided | even      | within the  | conceptual |      | model. The   |
| responsible | for     | predicting       | the | WSN | node’s | behavior   | and |         |          |           |             |            |      |              |
|             |         |                  |     |     |        |            |     | authors | claim    | that most | IoT gateway | and        | node | features are |
networklifetimeandperformance. relocated to the IoT system and virtualized as the VNF,
coordinatedbytheIoTnetworkbytheSDN/NFVcontroller
3) CRITICALANALYSIS
|     |     |     |     |     |     |     |     | or orchestrate. |     | This proposed | virtualization |     | over | IoT nodes |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | -------------- | --- | ---- | --------- |
Theauthorshavediscussedtheworkasaconceptualexercise
|          |               |     |     |           |                |     |     | is not feasible |     | due to the | IoT device’s |     | resource | constraint |
| -------- | ------------- | --- | --- | --------- | -------------- | --- | --- | --------------- | --- | ---------- | ------------ | --- | -------- | ---------- |
| and have | not presented |     | any | prototype | implementation |     | and |                 |     |            |              |     |          |            |
nature.
evaluationsofdifferentscenarios.Evenwithintheconceptual
framework,itisunclearhowthecentralandlocalcontrollers
|                   |     |     |            |      |      |       |        | J. MOBILITYMANAGEMENTINURBAN-SCALE |     |     |     |     |     |     |
| ----------------- | --- | --- | ---------- | ---- | ---- | ----- | ------ | ---------------------------------- | --- | --- | --- | --- | --- | --- |
| would synchronize |     | and | coordinate | with | each | other | or how |                                    |     |     |     |     |     |     |
SDN-BASEDIoT
themanagementfunctionsaredistributedbetweenthesetwo
|     |     |     |     |     |     |     |     | 1) MOTIVATION |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
typesofcontrollers.
IoTflowsaredistributedinnatureandneedtoberegulated.
|     |     |     |     |     |     |     |     | The IoT | controls | and | commands | are | grouped | into the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | --- | ------- | -------- |
I. SDNAPPROACHTOIoTNETWORKING
1) MOTIVATION geographicalregionswithintheIoTnetworks.Aninteractive
viewcanbeusedinmulti-networkflowtoselectbetteraccess
| The IoT | is projected |     | to contain |     | billions | of connected |     |         |           |         |              |     |          |           |
| ------- | ------------ | --- | ---------- | --- | -------- | ------------ | --- | ------- | --------- | ------- | ------------ | --- | -------- | --------- |
|         |              |     |            |     |          |              |     | points. | A special | overlay | architecture |     | that can | primarily |
devices,renderingtheprovisionandoperationofcertainIoT
networkingservicesmoredifficult.Indeed,IoTservicesare contribute to stability mitigation and fault tolerance in
SDNIoTwillbehighlysuitable.Inasingleshare,IoTgadgets
| somewhat | different | from | legacy | Internet | services |     | because |     |     |     |     |     |     |     |
| -------- | --------- | ---- | ------ | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
of their dimensioning statistics and because IoT services may connect various types of local switch-related access
points.
| vary drastically |      | in design | and | constraints. |              | For example, |        |     |     |     |     |     |     |     |
| ---------------- | ---- | --------- | --- | ------------ | ------------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| IoT services     | also | rely      | on  | energy       | and CPU-like |              | sensor |     |     |     |     |     |     |     |
technologies, regardless of whether the use is for home 2) PROPOSEDFRAMEWORK
automation, smart building, e-related health, or regional or Wu et al. [170] have proposed Ubiflow, an SDNIoT
national power or water metering. Some IoT services, such architecture, as shown in Fig. 26. Ubiflow has multi-
as dynamic monitoring of biometric data, exploitation of ple controllers. The geographical regions within the IoT
confidentialinformation,andprivacy,needtobesafeguarded networks are split between these controllers, resulting in
wheneverthisinformationistransmittedovertheIoTnetwork distributedcontrolofIoTflows.Ubiflowcontrollersschedule
infrastructure. Authors in [169] explores how SDN can the flows according to device requirements and offer a
enablethedeploymentandoperationofcertainadvancedIoT uniqueoverlaystructureachievingmobilitymanagementand
services,regardlessoftheirexistenceorscope. fault tolerance in SDNIoT. The core components of the
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     | 70875 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
variousspecialWSNrequirements.Theproposedframework
consistsoftwoplanes,CPandtheDP.Theinteractionofthe
CPandtheDPtakesplacewiththehelpoftheOFprotocol.
|     |     |     |     |     |     |     |     | The CP        | comprises | multiple | functions  |           | and | is responsible |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | -------- | ---------- | --------- | --- | -------------- | --- |
|     |     |     |     |     |     |     |     | for providing | topology  |          | discovery, | mobility, |     | and managing   |     |
networkpoliciestotheDP.TheDP,whichisalsocalledthe
|     |     |     |     |     |     |     |     | sink, is | accountable | for | performing | packet |     | engineering | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ---------- | ------ | --- | ----------- | --- |
packetaggregation.TDMAlayerisresponsibleforproviding
|     |     |     |     |     |     |     |     | dynamic | and flexible |     | data | forwarding |     | to the | physical |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---- | ---------- | --- | ------ | -------- |
layer.
|     |     |     |     |     |     |     |     | 3) CRITICALANALYSIS |       |             |     |        |             |     |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ----- | ----------- | --- | ------ | ----------- | --- | ------ |
|     |     |     |     |     |     |     |     | The work            | lacks | evaluations |     | of the | performance |     | of the |
architectureunderdifferentscenarios.Duetothisreason,itis
|     |     |     |     |     |     |     |     | not possible      | to know | the              | overhead     | of       | provisioning |           | services |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ---------------- | ------------ | -------- | ------------ | --------- | -------- |
|     |     |     |     |     |     |     |     | by the controller |         | and              | the proposed |          | TDMA         | protocol. | It is    |
|     |     |     |     |     |     |     |     | also unclear      | the     | sequence         | of           | messages | exchanged    |           | by the   |
|     |     |     |     |     |     |     |     | CP and            | the DP  | for provisioning |              | topology |              | discovery | and      |
virtualizationserviceoverthenetwork.Detailedevaluations
| FIGURE26. | UbiFlowsystemarchitecture. |     |     |     |     |     |     |        |         |      |           |     |         |       |       |
| --------- | -------------------------- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---- | --------- | --- | ------- | ----- | ----- |
|           |                            |     |     |     |     |     |     | should | also be | done | to figure | out | the use | cases | under |
whichtheWSNtrafficloadandtheproposedprogrammable
system architecture of Ubiflow are switches, access points, layer would be cost-efficient in resource consumption and
otherwise.
| data servers, | controllers, |     | and     | Internet       | devices. |             | The data |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------- | -------------- | -------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| collection    | component    |     | gathers | network/device |          | information |          |     |     |     |     |     |     |     |     |
from IoT multi-network neighborhoods and caches it in L. SDNFORINDUSTRIALIoT
a database. Layered components use gathered data in the 1) MOTIVATION
| controller. | The | component | responsible |     | for | task | resource |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ----------- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
IndustrialInternetofThings(IIoT)isanewsubfieldofIoT
matching matches task requests with existing resources in that deals with deploying a wide range of sensors to track
multi-network. supply chain, manufacturing, and other industries in real-
|     |     |     |     |     |     |     |     | time. IIoT | deployments |     | need to | address | information-based |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------- | ------- | ----------------- | --- | --- |
3) CRITICALANALYSIS interactions whereby the system’s experiences change over
time,dependingonthegivenknowledge.
TheframeworkofUbiflowsolvesIoTcontrolproblems,such
| as error         | sensitivity | and    | load balancing. |     | Several  | controllers |        |                      |     |     |     |     |     |     |     |
| ---------------- | ----------- | ------ | --------------- | --- | -------- | ----------- | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| were implemented |             | in the | architecture    |     | that can | create      | issues |                      |     |     |     |     |     |     |     |
|                  |             |        |                 |     |          |             |        | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     |
related to synchronization, but the authors never addressed InIndustrialIoT,applicationneedsvaryfromnearreal-time
| these issues. | The | proposed | framework |     | is implemented |     | with |             |     |              |     |             |     |           |      |
| ------------- | --- | -------- | --------- | --- | -------------- | --- | ---- | ----------- | --- | ------------ | --- | ----------- | --- | --------- | ---- |
|               |     |          |           |     |                |     |      | data access | to  | asynchronous |     | data access |     | depending | upon |
Omnet++.
the help of ORBIT is used as a wireless certaintriggeredevents.Furthermore,thelackoftechnology
testbedforexperimentstoevaluatetheproposedarchitecture standardization is a significant impediment to the adoption
| where performance |     | and | time | are observed. |     | It consists | of  |               |     |            |     |     |          |               |     |
| ----------------- | --- | --- | ---- | ------------- | --- | ----------- | --- | ------------- | --- | ---------- | --- | --- | -------- | ------------- | --- |
|                   |     |     |      |               |     |             |     | of Industrial | IoT | solutions. | Due | to  | the lack | of standards, |     |
400 radio nodes. ORBIT has an open-light controller for interoperability between different systems and technologies
WiFiandWiMAX.Theframework’sschedulingalgorithms
|     |     |     |     |     |     |     |     | has become | a   | real pain | point. | This | issue | can be | solved |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------ | ---- | ----- | ------ | ------ |
are compared with the conventional famous scheduling by standardization of interface intercommunication among
algorithmsofDevoflowandHedera. varying components developed by various vendors. The
proposedarchitectureofWanetal.[172]asshowninFig.27,
K. DESIGNOFLR-WPANIoTSYSTEMSWITHSDN provides information collection, data transmission, and
|     |     |     |     |     |     |     |     | processing | services. | The | data | transmission |     | system | passes |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ---- | ------------ | --- | ------ | ------ |
1) MOTIVATION
Despite the current developments in WSN and IoT, the detecteddatatothecommercialcloudfromthenetwork.
| existing | Internet | architecture | can | not | meet | the high | volume |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | --- | --- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
of new traffic trends from smart sensing systems. SDN 3) CRITICALANALYSIS
| has emerged |     | as a smart | solution |     | to improve |     | network |             |           |     |         |            |     |     |         |
| ----------- | --- | ---------- | -------- | --- | ---------- | --- | ------- | ----------- | --------- | --- | ------- | ---------- | --- | --- | ------- |
|             |     |            |          |     |            |     |         | The authors | developed |     | a model | consisting |     | of  | a cloud |
programmability,agility,versatility. data center, an industrial machine with AVG, IWN, RFID
scanner,conveyor,etc.,toanalyzetheirsystem.Theproposed
2) PROPOSEDFRAMEWORK framework is contrasted with the SDNIIoT architecture.
Hakirietal.[171] proposed the SDN-based framework for For the planned structure and traditional systems, energy
sensors,whichrepresentsanewSDNframeworkthatmeets efficiencyandusageareanalyzed.Resultsindicatedthatthe
| 70876 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     | engine. | Due to | this reason, | SDN-based |     | CP  | can make |
| --- | --- | --- | ------- | ------ | ------------ | --------- | --- | --- | -------- |
decisionswithregardstocommandsfromdevicesinamore
efficientandrobustmanner.
|     |     |     | 3) CRITICALANALYSIS |     |           |     |                 |     |          |
| --- | --- | --- | ------------------- | --- | --------- | --- | --------------- | --- | -------- |
|     |     |     | Zhouetal.[173]      |     | framework | is  | quite effective | in  | managing |
mobilityandensuringenergyconservationwithintheWSAN.
|     |     |     | However,     | there       | is no discussion |              | on how       | security   | and fault |
| --- | --- | --- | ------------ | ----------- | ---------------- | ------------ | ------------ | ---------- | --------- |
|     |     |     | tolerance    | would       | be handled.      |              | Furthermore, | the        | proposal  |
|     |     |     | necessitates | significant |                  | changes      | to the       | protocol   | stack of  |
|     |     |     | WSAN         | to adopt    | SDN into         | the WSN      | stack.       | Further    | studies   |
|     |     |     | regarding    | load        | management       | and          | balancing    | should     | also be   |
|     |     |     | done to      | find out    | how              | effectively  | the          | controller | manages   |
|     |     |     | data load    | from        | the DP           | and responds | to           | requests   | from the  |
applicationsplane.
| FIGURE27. | SDNforindustrialIoT. |     |                                        |          |                  |               |              |              |              |
| --------- | -------------------- | --- | -------------------------------------- | -------- | ---------------- | ------------- | ------------ | ------------ | ------------ |
|           |                      |     | N. SDN-BASEDREFACTOREDMIDDLEWAREFORIoT |          |                  |               |              |              |              |
|           |                      |     | 1) MOTIVATION                          |          |                  |               |              |              |              |
|           |                      |     | SDN allows                             | for      | a redesign       | of the        | middleware   |              | architecture |
|           |                      |     | to improve                             | service  | interconnection, |               | management,  |              | and the      |
|           |                      |     | deployment                             | of       | new monitoring   |               | scenarios.   | The          | middle-      |
|           |                      |     | ware can                               | also     | be refactored    | to            | accommodate  |              | a variety    |
|           |                      |     | of services.                           | The      | motivation       | behind        | the          | author’s     | proposed     |
|           |                      |     | framework                              | [174]    | is to            | solve common  |              | difficulties | in IoT       |
|           |                      |     | contexts,                              | focusing | on               | connectivity, | security     | and          | privacy,     |
|           |                      |     | management,                            | and      | data             | structure,    | particularly |              | in health    |
monitoringscenarios.
|     |     |     | 2) PROPOSEDFRAMEWORK |     |          |             |     |         |           |
| --- | --- | --- | -------------------- | --- | -------- | ----------- | --- | ------- | --------- |
|     |     |     | Arizaetal.[174]      |     | expanded | its support |     | towards | SDN tech- |
nologiesandproposedtheREMOAmiddlewareframework.
FIGURE28. AWSANframeworkbasedonSDNapplication. Complex networks across access points (AP), which are
spreadacrossmoremachine-drivendatabases,areintroduced
|     |     |     | in the architecture. |     | The | AP’S | and network | servers | fulfill |
| --- | --- | --- | -------------------- | --- | --- | ---- | ----------- | ------- | ------- |
IIoT SDN-based design requires less power, is stable, and the function of the actual proxy unit. Flow-based APs is
facilitatesautonomousindustrialdecision-making.
|     |     |     | transmitting | the     | packet. | Things  | collected    | data | is sent to |
| --- | --- | --- | ------------ | ------- | ------- | ------- | ------------ | ---- | ---------- |
|     |     |     | services     | via the | IPSec   | tunnel. | The handling |      | of objects |
M. SDN-BASEDFRAMEWORKFORWIRELESSSENSOR formerlyfocusedonSNMPisnowcenteredonOFcounters.
NETWORKS The ThingsFlow application is available through APs and
1) MOTIVATION provides a timestamp that shows when the counter is being
The motivation is to have effective control of the commu- found. Counters are saved in ThingsFlow and retrieved
nication infrastructure, reduce the processing load of the through services that implement control mechanisms. The
forwarding nodes, increase the network’s reliability, and gateway passes access points packets (AP) in compliance
reducetheenergyconsumptionwithintheWSNandIoT. with OF rules. With the addition of SDN, middleware
|     |     |     | capabilities | have | been | expanded, | and | every AP | can now |
| --- | --- | --- | ------------ | ---- | ---- | --------- | --- | -------- | ------- |
provideseveralservices.
2) PROPOSEDFRAMEWORK
| Zhou et | al. [173] have proposed | an SDN framework | for |     |     |     |     |     |     |
| ------- | ----------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
WirelessSensorandActuatorNetworks(WSAN).Asshown 3) CRITICALANALYSIS
in Fig. 28, the WSAN structure consists of three different The authors have not presented any evaluations, so it is
layers: Application, CP, and DP. The conventional WSAN unclear how much additional overhead would be caused by
protocolstackhasasharedplanethatcommunicateswithfive message passing between the different modules after the
levels of protocols (application, storage, network, medium, refactoring of REMOA gateway. Studies are also needed
and physical access) to decide. Rather than SDN-based, to find out the degree of complexity that has been added
WSAN operators will make routing decisions. The CP as a result of incorporating new modules in the REMOA
| moduleiscomposedofwithSDNcontrollerandascheduling |     |     | architecture. |     |     |     |     |     |       |
| ------------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME10,2022                                     |     |     |               |     |     |     |     |     | 70877 |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
O. ENHANCINGMIDDLEWARE-BASEDIoTAPPLICATIONS etc. The proposed architecture [176] has two ODL SDN
|     |     |     |     |     |     |     |     | controllers | for managing |     | the | industrial | process. | The | frame- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | ---------- | -------- | --- | ------ |
1) MOTIVATION
With the arrival of the new paradigm such as NFV, it is work is for multiple purposes such as backup, maintaining
|              |     |           |     |             |     |          |         | fault tolerance, |     | managing | security |     | risk, etc. | The | authors |
| ------------ | --- | --------- | --- | ----------- | --- | -------- | ------- | ---------------- | --- | -------- | -------- | --- | ---------- | --- | ------- |
| now possible |     | to deploy |     | any network |     | function | such as |                  |     |          |          |     |            |     |         |
switching,trafficmonitoring,loadbalancer,etc.,offeringthe mentioned that the number of controllers in the proposed
required functional capabilities in a virtual form rather than architecture could vary according to the IIoT domain’s
|     |     |     |     |     |     |     |     | situation. | ODL uses | a   | software | functionality |     | called | Virtual |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | -------- | ------------- | --- | ------ | ------- |
implementedondedicatedequipment.
|     |     |     |     |     |     |     |     | Tenant Network |     | (VTN) | to control | controllers’ |     | cluster. | The |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ---------- | ------------ | --- | -------- | --- |
authorsdefinetwotypesofSDNcontrollersintheproposed
2) PROPOSEDFRAMEWORK
Authors in [175] proposed a middleware framework based framework.ThefirstcontrollerisfortheITnetwork’scontrol,
andanothercontrollerisfortheIoTnetwork.Theindustrial
onaself-adaptationofQoSorientedmechanism,consisting
|              |               |           |     |          |         |             |           | machinery     | networks | consist   | of   | devices    | running | on  | different |
| ------------ | ------------- | --------- | --- | -------- | ------- | ----------- | --------- | ------------- | -------- | --------- | ---- | ---------- | ------- | --- | --------- |
| of autonomic |               | computing |     | (AC)     | model   | to interact | with      |               |          |           |      |            |         |     |           |
|              |               |           |     |          |         |             |           | communication |          | protocols | such | as Modbus, |         | CAN | Bus, and  |
| sensors      | and effectors |           | in  | the IoT. | Sensors | are         | basically |               |          |           |      |            |         |     |           |
Ethercat.Theseprotocolscannotcommunicatedirectlywith
| monitoring | the | service | requirement, |     | and | the | effector is |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
implemented the required QoS to the connecting nodes theIoTdomainduetotheirdataformatandcommunication
|                 |        |            |            |           |                  |           |         | protocol’s | incompatibility. |     | To           | communicate |              | with | the IoT  |
| --------------- | ------ | ---------- | ---------- | --------- | ---------------- | --------- | ------- | ---------- | ---------------- | --- | ------------ | ----------- | ------------ | ---- | -------- |
| with the        | help   | of the     | middleware | MW        | entity           | (Public   | cloud). |            |                  |     |              |             |              |      |          |
|                 |        |            |            |           |                  |           |         | domain,    | these devices    | use | a middleware |             | approach     |      | based on |
| This MW         | entity | implements |            | a         | QoS microservice |           | as a    |            |                  |     |              |             |              |      |          |
|                 |        |            |            |           |                  |           |         | OPC UA     | client-server    |     | architecture | that        | communicates |      | with     |
| virtual network |        | function.  | The        | autonomic |                  | computing | model   |            |                  |     |              |             |              |      |          |
thecontroller.
| is responsible |     | for monitoring |     | the | system | with      | the help |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | --- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of sensors     | and | reconfiguring  |     | the | system | according | to the   |     |     |     |     |     |     |     |     |
3) CRITICALANALYSIS
| requirement, | and | finally | executing |     | the plan | with | effectors’ |              |              |     |     |              |     |           |     |
| ------------ | --- | ------- | --------- | --- | -------- | ---- | ---------- | ------------ | ------------ | --- | --- | ------------ | --- | --------- | --- |
|              |     |         |           |     |          |      |            | The proposed | architecture |     | is  | a conceptual |     | solution. | The |
help.
authorsdidnotimplementtheirapproachbecausetherewere
|     |     |     |     |     |     |     |     | no performance |     | studies | and evaluations |     | of  | the architecture |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --------------- | --- | --- | ---------------- | --- |
3) CRITICALANALYSIS
|                |           |          |           |             |            |             |            | under various | production |     | scenarios. |     | This | proposed   | SDN |
| -------------- | --------- | -------- | --------- | ----------- | ---------- | ----------- | ---------- | ------------- | ---------- | --- | ---------- | --- | ---- | ---------- | --- |
| The authors    | implement |          | different |             | algorithms | at          | the appli- |               |            |     |            |     |      |            |     |
|                |           |          |           |             |            |             |            | controller    | deployment |     | solution   | has | some | advantages | and |
| cation network |           | function | named     | redirector, |            | compressor, | and        |               |            |     |            |     |      |            |     |
disadvantages.Thebenefitsaremodularityisthatitprovides
de-compressorinatransportationusecase.Theresultclearly
|                |            |          |          |                |               |          |           | more efficient   | management |             | of   | applications.    |           | The        | disadvan- |
| -------------- | ---------- | -------- | -------- | -------------- | ------------- | -------- | --------- | ---------------- | ---------- | ----------- | ---- | ---------------- | --------- | ---------- | --------- |
| shows          | the better | response |          | time           | at adaptation |          | QoS with  |                  |            |             |      |                  |           |            |           |
|                |            |          |          |                |               |          |           | tage is hardware |            | needs,      | such | as high-powerful |           | computers, |           |
| no adaptation. |            | The      | proposed | framework      |               | has only | focused   |                  |            |             |      |                  |           |            |           |
|                |            |          |          |                |               |          |           | allocating       | for each   | controller, |      | and              | assigning | backup     | for       |
| on a specific  |            | use      | case of  | transportation |               | of       | QoS self- |                  |            |             |      |                  |           |            |           |
controllers.
| adaptation. | The          | authors | never  | discussed |          | the detailed | imple-       |     |     |     |     |     |     |     |     |
| ----------- | ------------ | ------- | ------ | --------- | -------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| mentation   | of connected |         | actors | in the    | proposed |              | architecture |     |     |     |     |     |     |     |     |
Q. DISCUSSIONOFRESULTS
| and nor    | mentioned | how     | to      | handle    | the security |                 | risk of the |                  |       |          |           |     |          |              |           |
| ---------- | --------- | ------- | ------- | --------- | ------------ | --------------- | ----------- | ---------------- | ----- | -------- | --------- | --- | -------- | ------------ | --------- |
|            |           |         |         |           |              |                 |             | IoT applications |       | involve  | a variety | of  | layers   | having       | different |
| middleware | data      | center  | that    | provides  | the          | QoS             | service in  |                  |       |          |           |     |          |              |           |
|            |           |         |         |           |              |                 |             | processes,       | hence | managing | such      | IoT | networks | necessitated |           |
| the form   | of a      | virtual | network | function. |              | The implemented |             |                  |       |          |           |     |          |              |           |
theuseofanabstraction/adaptationlayer.Middlewarehides
| algorithm’s | performance |        | is   | a question |          | mark because | the     |          |                      |     |           |     |                |     |          |
| ----------- | ----------- | ------ | ---- | ---------- | -------- | ------------ | ------- | -------- | -------------------- | --- | --------- | --- | -------------- | --- | -------- |
|             |             |        |      |            |          |              |         | all the  | complexities         | of  | diversity |     | by providing   |     | API for  |
| algorithm   | was         | tested | only | on the     | specific | use          | case of |          |                      |     |           |     |                |     |          |
|             |             |        |      |            |          |              |         | physical | layer communications |     |           | and | other required |     | services |
transportation.
toapplications.ToovercomethemanagementissuesofIoT
|     |     |     |     |     |     |     |     | networks, | SDN-based | Middleware |     | acts | as a | link connecting |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | ---- | ---- | --------------- | --- |
P. SDNFRAMEWORKFORINDUSTRIALIoT
heterogeneouscomponents.Basedonthemanagementissues
1) MOTIVATION of IoT, we thoroughly investigated each of the major
The IoT-based smart industry aims to manage the industrial studies chosen during the SLR and classified them into
| process | to achieve |     | better | performance |     | in the | industrial |           |            |     |           |     |             |     |         |
| ------- | ---------- | --- | ------ | ----------- | --- | ------ | ---------- | --------- | ---------- | --- | --------- | --- | ----------- | --- | ------- |
|         |            |     |        |             |     |        |            | SDN-based | middleware |     | taxonomy. |     | We examined |     | several |
revolution;however,challengesareraisedduetothemassive strategies described in the existing literature to overcome
| IoT gadget | deployment |     | in  | smart | industries. | The | authors |                |     |              |     |                 |     |            |     |
| ---------- | ---------- | --- | --- | ----- | ----------- | --- | ------- | -------------- | --- | ------------ | --- | --------------- | --- | ---------- | --- |
|            |            |     |     |       |             |     |         | IoT management |     | difficulties |     | using SDN-based |     | middleware |     |
in [176] tries to meet these challenges by presenting an solutions. Table-10 summarizes the merits and demerits of
SDN-based solution on OpenDaylight (ODL) controller to the SDN-based Middleware solutions for IoTs that were
managetheindustrialIoTscenario.
selectedthroughtheSLR.Basedontheforegoingdiscussion,
|                      |     |     |     |     |     |     |     | the answers | to  | the research |     | questions | are | presented | as  |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | --------- | --- | --------- | --- |
| 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     | follows.    |     |              |     |           |     |           |     |
The IIoT domain consists of IoT devices from different RQ1: How can SDN-based frameworks provide effi-
communicationstandardssuchassensormotes,RFID,BLE cient security solutions to manage IoT network-related
working under ProfNet, Ethercat, CAN Bus, and Modbus. security issues? As mentioned before, conventional secu-
TheIIoTnetworkalsocontainstheconventionalITenterprise rity mechanisms cannot be implemented to manage IoT
network, composed of routers, switches, PCs, printers, devices due to their limited resources. Authors in [162]
| 70878 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE9. SummaryofSDN-basedmiddlewaresolutionsthataddressesIoTmanagementchallenges.
highlighted the need for such a middleware-based approach tolerance scheme. They also highlighted the importance of
to address IoT management challenges; therefore, they faulttolerancesolutionsinIoTnetworks.
proposed a middleware-based SDN solution to manage the RQ3: What are the potential solutions regarding load
IoTnetworks.Theyproposedvariousvirtualnetworksecurity balancing in SDN-based frameworks to manage IoT
functions at the controller layer, such as Software-defined networks? The increasing usage of IoT raises challenges
storage (SDStore) and Software-defined security (SDS). in managing heavy network traffic and maintaining ser-
Authorsin[157],[159]discussthegeneralwaytoimplement vice requirements. Most IoT devices have differences in
the middleware SDN-based solution in order to maintain processing, storage, power, and functionality, which cause
efficient security in IoT networks discuss the security in complex issues for QoS, resource allocation, and network
terms of application layer protocol, network layer protocols configurationintheIoTnetworkintermsofloadbalancing.
such as CoAp, MQTT, HTTPS, IPSEC etc.Table-9 clearly Theauthorsin[165]proposedanIoTnetworkmanagement
shows significantly fewer efforts are made to address the paradigmbasedonSDNQoScontrolandpublish-subscribe.
security challenges in IoT networks with the help of a The proposed framework is a QoS-aware framework for
middleware-basedSDNframework. managingIoTtrafficaggregatedintoFog-likeIoTgateways
RQ2: How can SDN-based frameworks provide effec- along the network edge with the help of an efficient load
tive fault tolerance management solutions to large-scale balancingmechanism.Theauthorshighlightedsomecritical
IoT networks? Authors in [168] proposed a framework parameters to address IoT networks in load balancing, such
basedonSDNwithscalabilityandreconfigurationfeaturesto as QoS, network configuration, etc. The massive stream of
addressfaulttoleranceinWSN.TheIoTnodesareconnected data transfer in IoT networks poses severe issues in the
toalocalcontroller,whichreceivesandprocessescommands future. Wangetal.[162] proposed SDNPS, a topic-based
from the central controller. One or more applications can publish-subscribesystembasedonSDN.Thearchitectureis
be placed at the top of the controller with the help of divided into numerous clusters. These clusters are grouped
an efficient load balancing approach. Local controllers are basedontheirregionalcharacteristics.Severalconceptually
located within sensor nodes, and they can affect the MAC autonomous areas represent each cluster in the topology.
and routing behaviour of the sensing nodes. The central Throughthebordergateway,theclusterscommunicatewith
controller issues command to these controllers. The code oneanother.Theyproposedtheminimalcosttopic-connected
is modified and controlled by the local controller, which overlay (MCTCO), an efficient routing protocol based on
is located in the sensor nodes. The Industrial Internet of topic connected overlay that operates by generating an
Things (IIoT) is a new area of the Internet of Things that optimumroutingschemabasedonloadbalancingtechniques.
usesvarioussensorstofollowsupplychains,manufacturing, Authors in [160] discuss the concept of adaptive load
and other industries in real-time. IIoT installations must balancing technique with the help of detecting overload
addressinformation-basedinteractions,inwhichthesystem’s conditionssuchastheheavynumberofrequestssenttothe
experiences change over time as a result of the knowledge SDNcontroller.
available.Theauthors’in[172]proposedframeworkresults RQ4: What scalable solutions can be offered by
indicated that the IIoT SDN-based proposed framework SDN-basedframeworkstomanageIoTnetworks?Author
requires less power, is stable, and facilitates autonomous in [158] discusses the scalable middleware solution for
industrial decision-making with the help efficient fault interoperability across heterogeneous devices that serve in
VOLUME10,2022 70879

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE10. MeritsanddemeritsofSDNmiddlewarebasedsolutionsforIoTnetworks.
various application domains such as discovery protocols to SDNframeworksolutionsaddressIoTnetwork’sscalability
manage IoT devices and context-aware IoT applications. challenges;however,mostoftheproposedsolutionsarenot
Hakirietal.developedapublishedsubscriber-basedscalable implemented.
middlewarestrategyin[163].onthenetworklayerprotocols, RQ5:HowcanSDN-basedframeworksenableefficient
the authors suggested that 6LowPAN protocols between powerconsumptioninIoTnetworks?Thecomputationand
MediaAccessControl(MAC)andIPv6workonsystemswith securityparameterscreateenergychallengesforIoTdevices.
restricted resources and proposed scalable routing protocol In[169]adynamicenergydistributionframeworkisproposed
ROLL (Routing for Low Power and Loss Networks) for for large-scale IoT in eHealth applications. The proposed
low-power devices. However, the proposed framework is framework focuses on energy challenges of IoT networks
not implemented to handle IoT management challenges concerning dynamic security and forwarding policies to
using SDN layers. Authors in [170] discuss the efficient, manage the IoT network. The authors in [172] implement
scalable solutions in terms of the controller to schedule an energy-efficient framework that included a cloud data
flows rules according to device requirements. Table-9 center,anindustrialmachinewithAVG,IWN,RFIDscanner,
clearly shows that the majority of the middleware-based conveyor, and so on. According to the findings, the IIoT
70880 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
|     |     |     |     |     |     |     | ForCES uses | logical | function | blocks | (LFB) | to  | provide | net- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------- | ------ | ----- | --- | ------- | ---- |
workingfunctionality,suchasIProuting,todataforwarding
|     |     |     |     |     |     |     | devices. In | OpenFlow-SDN, |        | the            | controller | has        | visibility | of     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------ | -------------- | ---------- | ---------- | ---------- | ------ |
|     |     |     |     |     |     |     | the global  | network       | state  | over the       | network.   | The        | forwarding |        |
|     |     |     |     |     |     |     | rules (flow | entries)      | can    | be proactively |            | configured | on         | each   |
|     |     |     |     |     |     |     | linked data | forwarding    | unit’s | flow           | tables.    | However,   |            | it has |
beenusedtoimplementflowtablesduetothehighwildcard
|     |     |     |     |     |     |     | lookup efficiency |              | of Ternary | Content-Addressable |     |     | Memory      |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | ---------- | ------------------- | --- | --- | ----------- | --- |
|     |     |     |     |     |     |     | (TCAMs)           | [38].        | OpenFlow   | protocol            | for | SDN | is designed |     |
|     |     |     |     |     |     |     | fortraditional    | networks.The |            | protocolmaintains   |     |     | flowtables  |     |
acrossthenetworkandpopulatesthetableswiththedecision
|     |     |     |     |     |     |     | from the        | central | SDN controller. |       | This design | is  | not suitable |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | --------------- | ----- | ----------- | --- | ------------ | --- |
|     |     |     |     |     |     |     | for constrained |         | IoT networks    | which | usually     |     | run over     | the |
6LowPanprotocolstack.Therefore,intheexistingliterature,
thereareanumberofeffortstoadapttheOpenFlowoperation
|           |                  |     |     |     |     |     | and table              | and message | structure | better | to  | accommodate |     | IoT |
| --------- | ---------------- | --- | --- | --- | --- | --- | ---------------------- | ----------- | --------- | ------ | --- | ----------- | --- | --- |
| FIGURE29. | Sensor-OpenFlow. |     |     |     |     |     | networks’requirements. |             |           |        |     |             |     |     |
SDN-based design uses less energy, is more stable, and A. SENSOROpenFlow
|            |            |     |                             |     |         |     | 1) MOTIVATION |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --------------------------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| allows for | autonomous |     | industrial decision-making. |     | Table-9 |     |               |     |     |     |     |     |     |     |
clearlyshowssignificantlyfewereffortsaremadetoaddress WSN are application-specific and, due to network topology
|                      |     |                  |     |     |           |     | changes, | they are | challenging | to  | handle. | By  | adopting | the |
| -------------------- | --- | ---------------- | --- | --- | --------- | --- | -------- | -------- | ----------- | --- | ------- | --- | -------- | --- |
| the energy-efficient |     | middleware-based |     | SDN | framework | to  |          |          |             |     |         |     |          |     |
manageIoTnetworks. Open FLow protocol, the authors in [183] suggested an
SDN-basedarchitectureforIoTtoaddressthesechallenges.
VII. OPENOWADAPTATIONBASEDMANAGEMENT
| FRAMEWORKS |     |     |     |     |     |     | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
The control plane (CP), southbound interface (SBI), and The SDN-WSN, as shown in Fig. 29, was introduced by
data plane (DP) are the essential elements of an SDN Louetal.[183],withasimplesplitbetweenthecontrolplane
architecture[178].Theapplicationplanecomprisesnetwork and a data plane using OpenFlow as an agreed protocol
applicationsthatspecifytherulesandinstructionsthatgovern for interaction between the two planes. The data plane has
the network logic using the exposed northbound APIs. nodes that perform the flow table-based packet forwarding.
These instructions are translated to the control plane by the The WSN is very versatile, flexible, and easy to manage
northboundAPIinterface,whichoffersfine-grainedcontrol by incorporating SDN into WSN. Since OpenFlow has
over the forwarding nodes and provides many network nevertheless been designed as a wired network protocol,
services, such as routing, monitoring, load balancers, and it needs some tweaking to make it suitable for wireless
firewalls [179]. These applications are either embedded in networks.ThishasbeenthetaskofLouetal.[183]withtheir
thecontrolplane(e.g.,optimizationofrouting,management proposed OpenFlow Sensor system. The Sensor OpenFlow
and monitoring of networks, security, traffic engineering, control channel is similar to the OpenFlow control channel.
and control of QoS) or located on a proxy server (e.g., In SDN OpenFlow, the channel is out of band, which is
firewall and firewall control). The control plane consists not realistic for WSN, and the Sensor OpenFlow channel is
of one or more controllers that, through the Southbound hostedinaband,whichmeansWSNhastocarryadditional
| APIs interface, |     | forward | the instruction | sets | and policies |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --------------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
controltraffic.Thisbecomesquiteanoverheadsincecontrol
specified by network applications to the data plane [180]. traffic in WSN is already significant due to high network
OpenFlow [181] is the first and most prevalent SDN flow dynamics and results in the WSN getting overloaded rather
controlprotocol,whichisnowthedefactostandardforSDN quickly. WSN typically does not process data as it arrives
switchcontrol.Inordertoallowthecontrollertohavedirect butinsteadaggregatesdataandthenprocessesittoconserve
| access and | control | of the | data forwarding |     | network devices, |     |                   |     |                |     |     |                |     |         |
| ---------- | ------- | ------ | --------------- | --- | ---------------- | --- | ----------------- | --- | -------------- | --- | --- | -------------- | --- | ------- |
|            |         |        |                 |     |                  |     | network resources |     | and bandwidth. |     | The | first solution |     | in this |
it plays the function of the southbound interface. The Open regard is to rewrite flow tables. The second option would
Networking Framework (ONF) standardizes OpenFlow to be to augment WSN to handle IP traffic so that the control
cope with the varied life and high latency of applications channelcanworkbothwithIPandnon-IP-basedtraffic.For
anddecreasemanagementcomplexity.Flowcontrolsystems IP traffic, the Sensor OpenFlow channel is equipped with a
suchasforwardingandcontrolelementseparation(ForCES) superimposedtransportprotocolovertheWSN.Ifanoperator
and protocol-oblivious forwardings (POF) are examples of chooses WSN with IP, then sensor OpenFlow channels are
| southbound    | [182]. | Similar | to the | OpenFlow | flow | tables, | self-supplied. |     |     |     |     |     |     |       |
| ------------- | ------ | ------- | ------ | -------- | ---- | ------- | -------------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME10,2022 |        |         |        |          |      |         |                |     |     |     |     |     |     | 70881 |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
3) CRITICALANALYSIS
| The authors | have | not provided |     | any details |     | on how | they are |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
addressingthemajorchallengesofIoTmanagement,suchas
| load balancing, |                | energy   | management,    |             | and so      | on. In       | addition |     |     |     |     |     |     |     |
| --------------- | -------------- | -------- | -------------- | ----------- | ----------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| to this,        | implementation |          | and            | evaluations | of          | the          | proposed |     |     |     |     |     |     |     |
| architecture    | have           | not been | performed.     |             | Without     | formal       | and      |     |     |     |     |     |     |     |
| detailed        | studies        | on the   | architecture’s |             | performance |              | under    |     |     |     |     |     |     |     |
| different       | scenarios,     | and      | working        | conditions, |             | the proposal | is       |     |     |     |     |     |     |     |
merelyaconceptualexercise.
B. FRAMEWORKFORIoTVIRTUALIZATIONVIAOPENOW
1) MOTIVATION
| Establishing | an      | IoT             | ecosystem | through |         | networking | and      |     |     |     |     |     |     |     |
| ------------ | ------- | --------------- | --------- | ------- | ------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| resource     | sharing | in configurable |           | and     | dynamic |            | networks |     |     |     |     |     |     |     |
amongmanyphysicalentitieswillleadtoambientcomputing
| and pervasiveintelligence. |           |        | Thevision |         | of achievingtechnol- |               |     |     |     |     |     |     |     |     |
| -------------------------- | --------- | ------ | --------- | ------- | -------------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ogy as                     | a service | can be | fulfilled | through | the                  | collaboration |     |     |     |     |     |     |     |     |
betweentheIoTandOpenFlow. FIGURE30. CENSOR:Cloud-enabledsecureIoTarchitectureoverSDN
paradigm.
2) PROPOSEDFRAMEWORK in[185]proposedCENSOR,anewcloud-enabledsecureIoT
| The proposed       | framework    |         | by              | [184],     | consists    | of four | layers,    |                      |     |       |        |               |     |        |
| ------------------ | ------------ | ------- | --------------- | ---------- | ----------- | ------- | ---------- | -------------------- | --- | ----- | ------ | ------------- | --- | ------ |
|                    |              |         |                 |            |             |         |            | network architecture |     | based | on the | SDN paradigm, | to  | tackle |
| i.e., connectivity |              | layer,  | access          | layer,     | abstraction |         | layer, and | theseissues.         |     |       |        |               |     |        |
| service            | layer. These | layers  | form            | interfaces |             | among   | services   |                      |     |       |        |               |     |        |
| and units          | through      | network | virtualization. |            |             | This    | layer also |                      |     |       |        |               |     |        |
2) PROPOSEDFRAMEWORK
verifies the availability of physical resources and network The proposed architecture of [185] is shown in Fig. 30.
| infrastructure. |     | The access | layer | consists |     | of the | topology |                  |     |            |           |         |                   |     |
| --------------- | --- | ---------- | ----- | -------- | --- | ------ | -------- | ---------------- | --- | ---------- | --------- | ------- | ----------------- | --- |
|                 |     |            |       |          |     |        |          | The architecture |     | is divided | into four | layers, | i.e., application |     |
specification, activation of the network, and domain forma- layer, control plane, and data plane. The data plane is
tion. It also manages link setup, intra-inter domain com- responsibleforcontrolledsensors,andactuatorsuseaTrusted
| munication, | scheduling, |     | and | packet | transmissions |     | between |          |        |       |             |     |            |     |
| ----------- | ----------- | --- | --- | ------ | ------------- | --- | ------- | -------- | ------ | ----- | ----------- | --- | ---------- | --- |
|             |             |     |     |        |               |     |         | Platform | Module | (TPM) | responsible | for | the safety | and |
flow sensors and IoT gateways. One of OpenFlow’s core essential services related directive from the IoT controller.
featuresisaddingvirtuallayerstoanarchitecture,leavingthe
ThecontrolplanehasseveralcentralizedSDNcontrollersthat
actualinfrastructureunchanged.Thus,forvariousnetworks,
managevariousIoTenvironmentsinseveralsituations,such
a virtual connection can be generated, and a common as security management, topology management, resource
| platform | can be | built for | different | communication |     |     | systems. |             |     |         |             |          |     |        |
| -------- | ------ | --------- | --------- | ------------- | --- | --- | -------- | ----------- | --- | ------- | ----------- | -------- | --- | ------ |
|          |        |           |           |               |     |     |          | management, | IoT | service | management, | traffic, | and | device |
The storage and maintenance layer includes data storage management. The modules of multiple controllers also
| and supervision, |     | and the | service | layer | provides | information |     |             |      |       |              |             |          |     |
| ---------------- | --- | ------- | ------- | ----- | -------- | ----------- | --- | ----------- | ---- | ----- | ------------ | ----------- | -------- | --- |
|                  |     |         |         |       |          |             |     | communicate | with | Cloud | data centers | for various | purposes |     |
resourcesandbusinessmanagementandoperations.
|     |     |     |     |     |     |     |     | such as data | analytics, | NFV | based | integration | of  | security |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ----- | ----------- | --- | -------- |
services,etc.TheapplicationplaneconsistsofdifferentIoT
3) CRITICALANALYSIS servicesresponsibleforimplementingthebusinesslogicand
The framework performance assessment is conducted for datastorageapplication-levelpolicies.
| three different |     | scenarios: | internet |     | communication, |     | intra- |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
domain communication, and cross-domain communication. 3) CRITICALANALYSIS
Inallofthesescenarios,asignificantincreaseinperformance
Theproposedarchitectureisbasedonacloud-enabledsecure
canbeseen. IoT SDN paradigm. The analysis report of the proposed
|     |     |     |     |     |     |     |     | framework | shows | that the | framework | is resistant | to  | various |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------- | --------- | ------------ | --- | ------- |
C. CLOUD-ENABLEDSECUREIoTARCHITECTURE security threats. The authors never discuss the attestation
THROUGHSDN processbetweenthecontrolplaneanddataplaneandthedeep
packetinspectionalgorithm.
1) MOTIVATION
| The expected |     | deployment | of  | IoT technologies |     |     | in several |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
D. SDNFORWIRELESSMOBILENETWORKS
| real-world | applications, |     | such | as surveillance, |     | transport, | and |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ---- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
environmentalmanufacturing,couldbeseriouslyundermined 1) MOTIVATION
by cybersecurity threats to low-cost end-user devices. Also, SDNiswidelyusedinmostcomputernetworkingapplication
theenormousquantityofdatathesedevicesgeneratecreates architectures such as data centers, private clouds, public
new problems with efficient collection and analysis of clouds,etc.However,someofthelegacynetworkarchitecture
data, decision-making, and behavior execution. The authors is now in the removal stages, such as cellular networks 2G,
| 70882 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
LTE,etc.Theselegacysystemscanberevivedwiththeadop- while at the same time suggesting higher differentiated
tion of SDN-based solutions. The legacy cellular network performancestandardsforthecommunicationsystem.Power
consistsof GatewayGPRSSupport Node(GGSN),Serving internet of things has introduced challenges of performance
GPRSSupportNode(SGSN),BaseStationController(BSC). requirements due to power ecosystem complexity, limited
These elements are responsible for mobility and session capacities of connected devices in power systems, threats,
managementofthemobilestations,andthestationcontroller attacks, etc. There is a need for SDN-based manage-
also provides functions such as encryption, decryption, and ment in the power internet of things to overcome these
| authentication. |     |     |     |     |     |     |     | challenges. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2) PROPOSEDFRAMEWORK
|            |       |          |       |              |     |     |        | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     |
| ---------- | ----- | -------- | ----- | ------------ | --- | --- | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| Authors in | [186] | proposed | a new | architecture |     | for | the 2G |                      |     |     |     |     |     |     |     |
Authorsin[187]proposedarchitecturethatconsistsofthree
| legacy network | architecture |     | with | the | SDN-based | approach |     |         |         |       |        |            |          |          |     |
| -------------- | ------------ | --- | ---- | --- | --------- | -------- | --- | ------- | ------- | ----- | ------ | ---------- | -------- | -------- | --- |
|                |              |     |      |     |           |          |     | layers. | The top | layer | is the | controller | cluster, | composed |     |
thatadoptednoncellularaccesstechnologyordomainsuchas
|     |     |     |     |     |     |     |     | of three | cluster | management |     | layers | responsible | for | main- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | ------ | ----------- | --- | ----- |
IoTnetworks.TheproposedarchitecturebasedonOpenFlow
|                |     |          |          |     |      |               |     | taining    | the overall | network |          | stability  | and | completing      | the |
| -------------- | --- | -------- | -------- | --- | ---- | ------------- | --- | ---------- | ----------- | ------- | -------- | ---------- | --- | --------------- | --- |
| protocol takes | the | existing | standard |     | GPRS | as a baseline |     |            |             |         |          |            |     |                 |     |
|                |     |          |          |     |      |               |     | functional | task        | with    | the Root | controller |     | and information |     |
removing the GGSN and SGSN nodes from the legacy synchronization.Thelocalrootlayermanagescomplexlocal
cellularnetworkswithnewnodesinthearchitecture.Thenew
services.Inthelastlayer,thelocalcontrollercommunicates
nodesconsistofsubnodes:ePCU(enhancedPacketControl
|     |     |     |     |     |     |     |     | with the | switch | using | the | OpenFlow | protocol. | The | next |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | --- | -------- | --------- | --- | ---- |
Unit),SDNcontroller,vGSN(virtualGPRSSupportNode),
|                    |     |            |     |       |              |     |      | layer is    | the FLowvisor |           | network |               | virtualization |           | platform, |
| ------------------ | --- | ---------- | --- | ----- | ------------ | --- | ---- | ----------- | ------------- | --------- | ------- | ------------- | -------------- | --------- | --------- |
| and OpenFlow-based |     | forwarding |     | core. | The sub-node |     | ePCU |             |               |           |         |               |                |           |           |
|                    |     |            |     |       |              |     |      | responsible | for           | providing |         | proxy between |                | the lower | and       |
of the new node is responsible for understanding the GPRS SDNclustercontrollerFlowVisorgeneratesrich‘‘slices’’of
protocolpacketandseparatingthesignalingfromuserplane
|            |         |         |     |           |      |             |     | network | resources. | To  | reduce | the single | point | failure | in the |
| ---------- | ------- | ------- | --- | --------- | ---- | ----------- | --- | ------- | ---------- | --- | ------ | ---------- | ----- | ------- | ------ |
| data. This | node is | working | as  | a special | kind | of OpenFlow |     |         |            |     |        |            |       |         |        |
controller,centralizedclustermanagementisimplementedin
| forwarder. | The other     | sub-node |           | vGSN   | is responsible |     | for  |           |      |            |       |             |     |      |           |
| ---------- | ------------- | -------- | --------- | ------ | -------------- | --- | ---- | --------- | ---- | ---------- | ----- | ----------- | --- | ---- | --------- |
|            |               |          |           |        |                |     |      | which the | root | controller | takes | information |     | from | the local |
| processing | the signaling |          | messages, | mobile | station        | or  | BSC, |           |      |            |       |             |     |      |           |
controller.
| and assisting | during | authentication |     | procedures |     | or  | session |     |     |     |     |     |     |     |     |
| ------------- | ------ | -------------- | --- | ---------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
managementprocedures.vGSNcommunicateswiththeSDN
|             |       |       |                |     |            |     |         | 3) CRITICALANALYSIS |     |              |     |         |          |     |       |
| ----------- | ----- | ----- | -------------- | --- | ---------- | --- | ------- | ------------------- | --- | ------------ | --- | ------- | -------- | --- | ----- |
| controller, | which | works | as an OpenFlow |     | controller |     | through |                     |     |              |     |         |          |     |       |
|             |       |       |                |     |            |     |         | The proposed        |     | architecture |     | is very | abstract | and | needs |
theGbinterface.
|     |     |     |     |     |     |     |     | a detailed | explanation |               | of  | the algorithms     |     | involved. | The    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------------- | --- | ------------------ | --- | --------- | ------ |
|     |     |     |     |     |     |     |     | authors    | have        | not discussed |     | the implementation |     |           | and no |
3) CRITICALANALYSIS
formalevaluationshavebeenconductedtotestthedifferent
Theauthorsimplementtheproposedarchitecture.Thesetup
scenarios.
| was composed | of                 | Sysmocom | SysmoBTS, |      | a relatively |               | inex- |     |     |     |     |     |     |     |     |
| ------------ | ------------------ | -------- | --------- | ---- | ------------ | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| pensive 2G   | (850/900/1800/1900 |          |           | MHz) | BTS.         | The transport |       |     |     |     |     |     |     |     |     |
corecontrolledbytheSDN-basedOpenFlowcontroller.The F. OpenFlowENABLEDPOLICY-BASEDIoTNETWORK
| transport          | core itself | is based      | on  | OpenFlow |           | compliant | for- | SECURITY      |     |     |     |     |     |     |     |
| ------------------ | ----------- | ------------- | --- | -------- | --------- | --------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| warder responsible |             | for executing |     | MAC      | tunneling | according |      |               |     |     |     |     |     |     |     |
|                    |             |               |     |          |           |           |      | 1) MOTIVATION |     |     |     |     |     |     |     |
toOpenFlowrulessetbythecontroller.However,theaccess The implementation of the SDN paradigm in networking
edge forwarders (ePCU) examine the IP header and the improves the traditional architecture of computer networks.
access-specific header (e.g., GPRS-specific protocols). The The adoption of the SDN paradigm in IoT has increased
external network edge (e.g., Internet uplink) also examines rapidly in the recent past, but this adaptation often presents
| the IP header | to  | select | the correct | tunnel | for | a particular |     |            |     |         |        |     |         |        |     |
| ------------- | --- | ------ | ----------- | ------ | --- | ------------ | --- | ---------- | --- | ------- | ------ | --- | ------- | ------ | --- |
|               |     |        |             |        |     |              |     | challenges | in  | the IoT | domain | due | to high | volume | and |
mobilestation.ThenewarchitectureisjustremovingSGSN, network traffic rates, variations in the characteristics of IoT
GGSN nodes from the legacy cellular network. In the new systemsandcomputernetworks,andlimitedresourcesinthe
architecture, the SDN OpenFlow controller is in charge of underlyingnetworkframework.
| transport | core and | connectivity |     | orchestration. |     | The proposed |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ------------ | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
architectureishypotheticalbecausetheauthorsneverdiscuss
|     |     |     |     |     |     |     |     | 2) PROPOSEDFRAMEWORK |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
implementation details and never discuss the OpenFlow In[188],authorsproposedanIoT-NETSECframeworkbased
protocoldetails.Nojustificationisprovidedthattheproposed
|     |     |     |     |     |     |     |     | on SDN | technology |     | consisting | of  | the following |     | building |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ---------- | --- | ------------- | --- | -------- |
solutionplayanyvitalroleinanyreal-timeproblem blocks: device policy repository, IoT device registration,
|     |     |     |     |     |     |     |     | security | flow role | installer, |     | statistic | collector. | The | proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | --------- | ---------- | --- | -------- |
E. CENTRALIZEDARCHITECTUREFORCOMMUNICATION framework monitors the traffic of IoT devices across the
NETWORKBASEDONSDN network to ensure three basic rules: only approved commu-
1) MOTIVATION nicationsareallowedandeverythingelseisdenied,monitor
The rapid growth of the IoT has encouraged the vigor- the network traffic, and protect the IoT device against three
ous development of new services in distributed networks attacks such as port scanning DOS, DDOS. The proposed
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 70883 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
frameworkcanbeusedasasecurityasaserviceapplication
inanIoTdomain.Thedevicepolicyrepositoryisresponsible
| for containing | dynamic |     | policy | documents. |     | This means | that |     |     |     |     |     |     |     |     |
| -------------- | ------- | --- | ------ | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
thepolicydocumentinthismoduleischangeableaccording
| to the situation |            | or reconfigure. |       | The | parameter | to   | making    |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | --------------- | ----- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| policy is        | the device | name,           | type, | and | set of    | flow | rules for |     |     |     |     |     |     |     |     |
IoTnodescommunicatewiththeSDNcontrollerIoTdevice
| registry | responsible | for | registering |     | the IoT | device | with a |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ----------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
propermechanismtocommunicatewiththeSDNcontroller
throughIPaddressPortnumber.Thedevicepolicyisofthe
| particular | node | is implemented |     | with | the help | of  | the device |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------------- | --- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
policyrepository.SecurityFlow-ruleInstallerisresponsible
| for providing | routing |              | and non-routing |      | flow | entries. | This      |           |                                              |     |     |     |     |     |     |
| ------------- | ------- | ------------ | --------------- | ---- | ---- | -------- | --------- | --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|               |         |              |                 |      |      |          |           | FIGURE31. | SDN-BasedSecurityFrameworkinDistributedGrid. |     |     |     |     |     |     |
| module parses |         | the security | ruleset         | from | the  | IoT      | nodes and |           |                                              |     |     |     |     |     |     |
thencreatesrelatedsecurityflowrulesfortrafficmonitoring
| purposes         | and installs | the          | flow | entries | in the   | SDN    | Switch. |                 |     |     |                |     |           |     |        |
| ---------------- | ------------ | ------------ | ---- | ------- | -------- | ------ | ------- | --------------- | --- | --- | -------------- | --- | --------- | --- | ------ |
|                  |              |              |      |         |          |        |         | programmability |     | can | be implemented |     | to create | a   | modern |
| Before deploying |              | the security |      | flow    | entries, | ensure | whether |                 |     |     |                |     |           |     |        |
networkingchannelfortheIoT.
| they are     | already   | relevant   | flow | entries | rule | at the | switch in |     |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | ---- | ------- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the network. | Statistic | collectors |      | collect | the  | packet | from the  |     |     |     |     |     |     |     |     |
IoT nodes associated with monitoring flow entries in the 2) PROPOSEDFRAMEWORK
|     |     |     |     |     |     |     |     | The proposed | architecture |     | shown |     | in Fig. | 31 by | [189] is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ----- | --- | ------- | ----- | -------- |
SDNswitchintheIoTnetworktofine-grainthemonitoring
|                 |     |             |            |     |            |          |     | based on  | an Opendaylight |     | MD-SAL   |     | Akka-based | clustering |      |
| --------------- | --- | ----------- | ---------- | --- | ---------- | -------- | --- | --------- | --------------- | --- | -------- | --- | ---------- | ---------- | ---- |
| ability through |     | statistical | knowledge. |     | Statistics | analyzer | is  |           |                 |     |          |     |            |            |      |
|                 |     |             |            |     |            |          |     | solution. | The authors     |     | proposed | a   | routing    | algorithm  | with |
responsibleforgettinginformationfromthestatisticcollector
distributedclusterSDNroutingprotocol,whichcanbeused
andanalyzingthepacketindeepaboutthetrafficflowboth
statisticcollectorsconnect. tofacilitateSDN-basedinter-domaincollaboration,toselect
|     |     |     |     |     |     |     |     | a suitable | route | between | nodes | connected |     | to the | cluster. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------- | ----- | --------- | --- | ------ | -------- |
Theproposedalgorithmautomatedthedomainclusters.The
3) CRITICALANALYSIS
|     |     |     |     |     |     |     |     | OpenFlow | protocol | specifies |     | control | messages | for | creating |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | --- | ------- | -------- | --- | -------- |
Theproposedarchitecture’simplementationisevaluatedwith thisapplication,allowingtheSDNcontrollertocreateastable
anOpenFlow-enabledswitch.Itrunsonadual-core2.4GHz link to network devices, read their current status and install
| Intel Xeon | processor | connected |     | to the | controller |     | through a |     |     |     |     |     |     |     |     |
| ---------- | --------- | --------- | --- | ------ | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
forwardinginstructions.
1Gbpssharedlinkwithapingdelayof0.5ms.Theproposed
| solution | implementation |     | testbed | is very | limited; | the | dataset |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------- | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
3) CRITICALANALYSIS
for experimentation is not trustworthy; the authors never The proposed framework is tested on a very small testbed.
| discussed   | the details | for  | choosing | the       | test | data and | training |              |            |           |         |      |         |             |          |
| ----------- | ----------- | ---- | -------- | --------- | ---- | -------- | -------- | ------------ | ---------- | --------- | ------- | ---- | ------- | ----------- | -------- |
|             |             |      |          |           |      |          |          | Moreover,    | the        | framework | working |      | details | are missing | in       |
| data for    | analyzing.  | The  | proposed | framework |      | focuses  | only     |              |            |           |         |      |         |             |          |
|             |             |      |          |           |      |          |          | the proposed | algorithm. |           | Authors | only | focus   | on the      | security |
| on security | features    | with | a basic  | Machine   |      | Learning | (ML)     |              |            |           |         |      |         |             |          |
parameterrelatedtotheroutingalgorithm.
| approach | that may | show | a better | result | with | other | methods |     |     |     |     |     |     |     |     |
| -------- | -------- | ---- | -------- | ------ | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
appliedlikedeeplearning.
H. DISCUSSIONOFRESULTS
|     |     |     |     |     |     |     |     | At the moment, |     | OpenFlow | is  | the most | extensively |     | utilized |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | -------- | ----------- | --- | -------- |
G. SDN-BASEDSECURITYFRAMEWORKINDISTRIBUTED SDN approach. In an SDN architecture, OpenFlow is a
| GRID |     |     |     |     |     |     |     | method | that standardizes |     | how | a controller |     | communicates |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | --- | ------------ | --- | ------------ | --- |
1) MOTIVATION with network devices. The OpenFlow protocol maintains
SDN is emerging as a new model for the next decade’s flow tables in the network and populates the tables with
network infrastructure. The separation of the control plane the SDN controllers. This design is not sufficient for IoT
and the data plane inside the SDN brings the versatility networks that usually operate over the 6LowPan protocol.
to use complicated software programs to handle, configure, Therefore,wechoosethosepapersinwhichresearchefforts
protect and maximize network resources. Security point of are directed to adopt the OpenFlow operation for better
view SDN can collect information from network devices accommodatingIoTnetworks’requirementswithaproposed
and allow applications to program forwarding devices, framework or implementation of the proposed solution.
unleashing a powerful proactive and smart security policy Wealsoselectedsomepapersthatcanbeusedasabuilding
technology. Unlike conventional protection solutions based blocktounderstandinghowOpenFlowadaptationaddresses
on a static firewall programmed by an administrator, such IoTmanagementissues.Addressingthemanagementissues
astheIntrusionDetectionandPreventionSystem(IDS/IPS), of IoT OpenFlow taxonomy, according to the literature
these functions enable the incorporation of security tools assessment, is also essential. We summarize the critical
that can be used in distributed scenarios. This network’s rationalesupportingtheOpenFlowtaxonomythataddresses
| 70884 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE11. SummaryofOpenFLowadaptationbasedsolutionaddressesIoTmanagementchallenges.
TABLE12. SummaryofOpenFlowbasedIoTsolution.
the IoT challenge by answering the following research interface,whichallowsfine-grainedcontroloverforwarding
questions. nodes and numerous network services such as routing,
RQ1: How can SDN-based frameworks provide effi- monitoring,loadbalancers,andfirewalls,governsthecontrol
cient security solutions to manage IoT network-related plane. These applications are either built into the control
securityissues? plane (for example, routing optimization, network admin-
Authors in [180], [181] highlight the importance of istration and monitoring, security, traffic engineering, and
security access policies at the controller level. OpenFlow QoScontrol)orhostedonaproxyserver.Table12suggested
can address the security challenges of IoT networks in that to maintain the fault tolerance, other IoT management
terms of network degradations, network throughputs, etc. parameters such as scalability and load-balancing must be
The control plane consists of one or more controllers that takenintoconsideration.
forwardtheinstructionsetsandpoliciesspecifiedbynetwork RQ3: What are the potential solutions regarding load
applications to the data plane through the Southbound balancing in SDN-based frameworks to manage IoT
APIs interface. Table-12 suggested minimal effort has been networks?
made to address the management challenges of IoT, and Ambient computing and pervasive intelligence will be
many of the proposed solutions lack detailed features enabled by establishing an IoT ecosystem by networking,
discussion. Authors in [188] proposed monitor modules and resource sharing among many physical elements is
in the proposed framework to monitor the traffic of IoT configurable and dynamic networks. Through collaboration
devices across the network to ensure three basic rules: only between IoT and OpenFlow, the concept of technology as
approved communications are allowed and everything else a service can be realized. Authors in [184] proposed a
is denied, monitor the network traffic, and protect the IoT frameworkthatfocusesonloadbalancingtechniqueinterms
device against three attacks such as port scanning DOS, of data storage, and the load-balancing algorithm is applied
DDOSattacks in a testbed of multiple virtual storages. Existing literature
RQ2: How can SDN-based frameworks provide effec- suggests that many implemented solutions and research
tive fault tolerance management solutions to large-scale effortshavealreadybeenmadeinthisregardtomanagethe
IoT networks? To address the fault tolerance difficulty of IoTenvironment.
managingIoTnetworks,theauthorsin[178],[179]describe RQ4: What scalable solutions can be offered by
the control plane and data plane roles. The northbound API SDN-basedframeworkstomanageIoTnetworks?
VOLUME10,2022 70885

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
Scalable solution to address the IoT management chal- IoT applications based on blockchain technology. This
lenges with OpenFlow taxonomy is generally correlated to passportisessentiallyusedforauthorization,authentication,
security, fault tolerance, load-balancing parameters [178], andtrust.Throughsmartcontracts,datasecurityandprivacy
[179], [184]. Literature suggests the most of the proposed apply to secure data communication between applications
frameworks are scalable. The majority of the proposed and nodes. The database for the IoT passport is responsible
solution working on controller ends have algorithms for intheformofanidentityregistryforeachIoTnode.TheIoT
security,loadbalancing,andfaulttolerance. repositoryconsistsofanintelligentcontractknownastheIoT
RQ5:HowcanSDN-basedframeworksenableefficient Passport contracts, consisting of identity mapping, identity
power consumption in IoT networks? SDN is widely registration,andrevocation.Theuser-definedpoliciesmod-
used in data centers, private clouds, public clouds, and ule is responsible for ensuring policies that trigger a given
otherfieldsofcomputernetworking.However,certainolder conditionandareresponsibleforfurtheractionduringnode
network design is being phased out, such as 2G, LTE, interaction.Theaccesscontrolpolicymoduleisresponsible
and other cellular networks. With the implementation of an forprovidinganauthorizationmechanismforcross-platform
SDN-based solution, these legacy systems can be brought communication nodes. This access control policy written in
back to life. Authors in [186] highlights the key energy a smart contract called the trust rule contract with identity
parametersinvolvetoaddressthemanagementchallengesof authentication,accesscontrol,andtrustbetweennodes.The
IoTintermsofsecurityalgorithms.Therapidgrowthofthe incentivepoliciesmodulemakespoliciesforminerswhoare
IoT has prompted the rapid development of new services in involvedinthetransactionoperation.Theagreementisalso
distributed networks while also implying higher specialized writtenintheformofthesmartcontract,whichfinallygives
communication system performance demands. Because of somerewordbasedonminers’efforts.
| the power   | requirements  | of the IoT, there | have been     | specific |     |     |     |     |     |     |
| ----------- | ------------- | ----------------- | ------------- | -------- | --- | --- | --- | --- | --- | --- |
| performance | difficulties. | To counter        | this, authors | in [188] |     |     |     |     |     |     |
3) CRITICALANALYSIS
proposedasecuritypolicyrepositoryinordertomanagethe The proposed structure is based on five fundamental prin-
energychallengesofIoTnetworks.
|     |     |     |     |     | ciples associated | with | the intelligent | contract. |     | The authors |
| --- | --- | --- | --- | --- | ----------------- | ---- | --------------- | --------- | --- | ----------- |
providednoanalysisoftheproposedarchitecture.Moreover,
VIII. BLOCKCHAIN-BASEDSDNMANAGEMENT
|     |     |     |     |     | the authors | have not | provided | a profound | discussion | of the |
| --- | --- | --- | --- | --- | ----------- | -------- | -------- | ---------- | ---------- | ------ |
FRAMEWORK
coreblockchaintheory,andnospecificcontext-awaredesign
| Blockchain | is a distributed | ledger | of continuously | grow- |     |     |     |     |     |     |
| ---------- | ---------------- | ------ | --------------- | ----- | --- | --- | --- | --- | --- | --- |
controlalgorithmissubmitted.
| ing data | in chain      | order in which   | each block  | is secured |     |     |     |     |     |     |
| -------- | ------------- | ---------------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
| using a  | cryptographic | algorithm [190]. | It enhances | man-       |     |     |     |     |     |     |
agement by verifying data such as digital content man- B. BLOCKCHAIN-BASEDFRAMEWORKFOREDGEAND
agement [191], [192]. Blockchain can be used to store FOGCOMPUTING
data, verification authentication, currency transaction, etc. 1) MOTIVATION
The concept of blockchain is introduced from the Bitcoin Recently, efforts have been made to integrate Edge, Fog,
crypto-currency system launched in 2008 by Satoshi Naka- and cloud-based services to support IoT applications, but
moto.Blockchainmaytypicallybeusedtoprovidesecurity they come with unique security, resource management, and
services. For example, applications have already emerged multi-application execution limitations. To address these
from blockchain-based identity providers, voting systems, limitations,aframeworkcalledFogBusthatsupportsend-to-
financial services and supply chain management, etc. end IoT-Fog-Cloud integration to ensure data integrity, data
Blockchainseemstobethedrivingtechnologycontributing confidentiality, reliability through blockchain is proposed
| toasignificantpartinIoTtechnology’s[193]–[196]. |     |     |     |     | in[201]. |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
BlockchainisessentiallyaperfectcomplementtoIoTwith
improved interoperability, privacy, security, reliability, and 2) PROPOSEDFRAMEWORK
| scalability | [197]–[199]. | We have focused | on existing | liter- |         |          |          |              |      |           |
| ----------- | ------------ | --------------- | ----------- | ------ | ------- | -------- | -------- | ------------ | ---- | --------- |
|             |              |                 |             |        | Authors | in [201] | proposed | architecture | that | comprises |
ature that directs their focus towards integrating blockchain IoT devices, Fog gateway nodes, Fog infrastructure, cloud
withtheSDIoTframework.
|     |     |     |     |     | infrastructure, | broker | nodes, | general nodes, | and | repository |
| --- | --- | --- | --- | --- | --------------- | ------ | ------ | -------------- | --- | ---------- |
A. ABLOCKCHAIN-BASEDTRUSTFRAMEWORKFORIoTs nodes. Fog gateway nodes are the entry point for IoT
|     |     |     |     |     | devices to | communicate | with | Fog computational |     | nodes via |
| --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ----------------- | --- | --------- |
1) MOTIVATION
IoTsareanticipatedtoopenupchallengesforresearchersand FogBus terminology. FogBus is responsible for supplying
|          |             |                     |         |           | IoT devices | authentication |     | credentials | service, | conveying |
| -------- | ----------- | ------------------- | ------- | --------- | ----------- | -------------- | --- | ----------- | -------- | --------- |
| industry | vendors for | better coordination | between | different |             |                |     |             |          |           |
IoTnetworks.Cross-platformcollaborationsarerequiredfor serviceexpectations,obtainingserviceresults,handlingIoT
|     |     |     |     |     | device requests | effectively. |     | Fog gateway | nodes | are respon- |
| --- | --- | --- | --- | --- | --------------- | ------------ | --- | ----------- | ----- | ----------- |
sharingdatawithotherIoTapplications.
|     |     |     |     |     | sible for | fast and dynamic |     | communication | with | accessible |
| --- | --- | --- | --- | --- | --------- | ---------------- | --- | ------------- | ---- | ---------- |
2) PROPOSEDFRAMEWORK Fog nodes through COAP or SNMP protocol. Fog Bus
Theauthorsin[200]introducedadecentralizedtrustsystem simultaneously communicates several heterogeneous Fog
namedIoTpassportforcross-platformcollaborationbetween computer nodes that communicate nodes with broker nodes
| 70886 |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
and general repository nodes. Fog computational nodes analyzingthetrafficinrawdatafromtheblockchaintotrust
start data processing and find the best available tools for the IoT device. With the help of assessing the report, the
the available repository nodes in the local area of the modulesfindwhethertheneworunknowndevicecanharm
requested IoT system. General computing nodes essentially the network. The front layer is responsible for interaction
supportedvariousnetworkfunctionsinvirtualizationsuchas between the controller and analyzer. Through this middle
firewallservices,networkservicemanagerstocontrolservice layer,thecontrollercanaccessthetrustscoreofeachdevice
quality,etc.Repositorynodesareresponsibleforfacilitating todecidewhetherthedeviceconnectstothenetworksliceor
data exchange, replication, recovery, and secure storage. not.Theinformationonthetrustscorecanbepulledbythe
Repository nodes provide interfaces for instant access and controllerfromthefrontal,middlelayer.
historical data analysis. They maintain the meta-data of
differentapplications,includingapplicationmodels,runtime
3) CRITICALANALYSIS
specifications,anddependencies.Foginfrastructureisover-
Theproposedarchitectureisbasedonblockchaintocompute
whelmedbytrafficordoesnotprovidetherequiredservice.
a trust score and provide this report to the controller.
Fog infrastructure interacts with the cloud data center to
On behalf of this report, the controller dynamically (dis)
conductthenecessaryservicethroughcloudservicesthrough
connects a device (from) to a slice labeled with a certain
cloud data centers. In combination with Fog repository
trustlevel.Theproposedarchitecturemayhavethepotential
nodes,itenablescomprehensivedatastorageanddistribution
to deal with the surface attack. The authors missed the
such that data access and processing become location-
discussion on the details of the algorithms used in the
independent.
proposedarchitecture.
3) CRITICALANALYSIS
D. FORENSICSARCHITECTUREINSDN-IoTUSING
The authors introduce the proposed architecture called the
BLOCKCHAIN
Sleep Apnea prototype. The embedded blockchain function
1) MOTIVATION
in FogBus architecture is very generic. The security feature
The IoT domain faces challenges in digital forensics,
implemented with blockchain aid increases computational
including data integrity, deletion of proofs, or modification
time in resource management, security mitigation steps run
toresolvethosechallenges.Blockchaintechnologies,evenif
timeframeworkmigration.
used,canpresentweakattackdetectionandsluggishprocess-
ing. SDN-IoT provides an efficient forensic architecture to
C. SDNANDBLOCKCHAIN-BASEDTRUSTMANAGEMENT overcomethesechallengesthatcreateaCustodyChain(CoC)
FORIoTDEVICES withblockchaintechnology.
1) MOTIVATION
In the IoT domain, it is challenging to recognize devices
2) PROPOSEDFRAMEWORK
that are vulnerable to the environment due to a lack of
Authors in [203] suggested SDN-based IoT architecture,
required knowledge and available solutions. An SDN and
where controllers are implementing flow-table switch rules
blockchain-based trust system using an SDN controller to
for three different traffics, Voice over Internet Protocol
establishatrustlevelthroughatrustscorebasedontherecord
(VoIP), File Transfer Protocol (FTP), or HyperText Trans-
inablockchainknownasStewARDisproposedin[202].
fer(HTTP)Protocol.ThearchitectureusesaLinearHomor-
phic Signature (LHS). The parsing of the message includes
2) PROPOSEDFRAMEWORK Flow-Mod, Packet-In, Stats-Reply, and other necessary
Authors in [202] proposed an architecture that consists of packet features. The controller feature analyzer module is
a Blockchain layer, analyzer, frontal, and controller. The responsibleforthefeatureextractionoftheentrypacketbased
blockchain layer is responsible for tagging the devices as on the attribute’s value. The authentication module in the
good behavior, bad behavior, malicious behavior, bind, and controllerauthenticatesthedeviceusingtheLHSalgorithm,
leave.Goodbehavioristaggedwhenthechainofthatdevice which considers the authentication of a single IoT device
inblockchainreportsthatthedeviceisbehavingaccordingto with an Elliptical Point. This module contains flow rules
therule.Badbehavioriswhenthedevicechainhistoryshows based on the type of traffic, protocol, or port number. Only
some deviation is detected. Malicious behavior is tagged three types of traffic with the help of flow table rules are
when the chain history shows some abnormal activities of permitted or disclaimed in the proposed architecture. There
traffic according to defined rules. Bind is responsible for areavarietyofflowentriesforeachchangeintheproposed
joining a new device to the controller before connecting to system. Before treatment, each switch verifies all three
aslice.Suchpairingaimstopreventfakeormalicioushome traffics and the corresponding port numbers. The change
controllersfromreportingondevicesthattheydonotmanage. discards invalid traffic with the wrong port number. These
Leave terminate the device’s connection to the controller three traffics checked with port numbers as unauthorized
permanently, the same as the concept of proof of burn in users access the network using an invalid port number. The
theblockchain.Theanalyzerisresponsibleforcontinuously authorsproposedtwoalgorithms.Onealgorithmfocuseson
VOLUME10,2022 70887

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
FIGURE32. Anenergy-efficientSDNcontrollerbasedonblockchain.
theprocessfollowedforswitchesimplementedinthecontrol IoT devices. The proposed architecture’s key objectives
plane.Theotheralgorithmtargetstheprocessfollowedforthe are to enhance the security of IoT communication and
controllerintheSDNcontrollerusingtheNeuroMulti-Fuzzy reduceenergyconsumption.Theypresentedanalgorithmfor
model in the controller for classifying the legitimate user energyefficiencyandsecurity.Privateandpublicblockchains
involvedinthenetwork.Thedevicesareauthenticatedfrom are used in the proposed architecture, optimized for the
the blockchain, and are analyzed on the neuro multi-fuzzy IoT network. The proposed algorithm is based on the
model. configurationoftheclusterandthelimitationsofIoTdevices
|     |     |     | in terms of | energy and | computation. The | algorithm utilizes |
| --- | --- | --- | ----------- | ---------- | ---------------- | ------------------ |
3) CRITICALANALYSIS the blockchain security features to improve security in line
|     |     |     | with the | energy efficiency | criteria and an | SDN controller |
| --- | --- | --- | -------- | ----------------- | --------------- | -------------- |
TheNetworkSimulatorVersion3(NS3)forensicarchitecture
in SDN IoT is developed. In NS3, the blockchain concept for the process of authentication and verification in each
| wasintegratedintoIoTbasedonSDN.Inordertoimplement |     |     | cluster. |     |     |     |
| ------------------------------------------------- | --- | --- | -------- | --- | --- | --- |
theblockchainconceptinSDN,thisarchitecturewascreated
usingaBitcoincodingframeworkinNS3.Theblocksinthe 3) CRITICALANALYSIS
blockchainaregeneratedin10seconaverage,whichcanbe The proposed architecture shows a significant impact on
improvedfordifferentscenarios. reducingenergyconsumptionandincreasingcommunication
|     |     |     | protection | between IoT | devices. The architecture | missed |
| --- | --- | --- | ---------- | ----------- | ------------------------- | ------ |
E. BLOCKCHAINENABLEDENERGY-EFFICIENTSDN addressing the load balancing and resource management
|     |     |     | issues in | IoT networks, | which could have | been accommo- |
| --- | --- | --- | --------- | ------------- | ---------------- | ------------- |
CONTROLLERARCHITECTUREFORIoTNETWORKS
| 1) MOTIVATION           |            |                    | datedforaneffectivesolution. |     |     |     |
| ----------------------- | ---------- | ------------------ | ---------------------------- | --- | --- | --- |
| There are long-standing | challenges | in the IoT market, | such                         |     |     |     |
as security, comparability, energy consumption, and device F. SDN-BASEDDISTRIBUTEDBLOCKCHAIN
heterogeneity.Securityandenergyfactorsplayessentialroles ARCHITECTUREFORIoT
in data transmission across IoT and edge networks. The 1) MOTIVATION
merger of blockchain and SDNing (SDN) can resolve the The recent growth of the IoT and the subsequent prolifer-
energyandsecurityparameterissuesinIoTnetworks.
|     |     |     | ation of data | volumes        | created by intelligent | devices have  |
| --- | --- | --- | ------------- | -------------- | ---------------------- | ------------- |
|     |     |     | contributed   | to outsourcing | data to specified      | data centers. |
2) PROPOSEDFRAMEWORK However,consolidateddatacenters,suchascloudcomputing,
Authorsin[204]proposedarchitecture,asshowninFig.32, cannotcontinuetohandlethesemassivedatastoresdesirably.
distributed network management for IoT devices imple- In conventional networking architecture, there are several
mentedusinganIoT-tailoredblockchainandSDNcontroller problemsduetotheexponentialincreaseindiversityandthe
in a cluster structure. The architecture in which the SDN number of devices not built to link to the Internet. Provide
controllers linked to a single blockchain can communicate high availability, data distribution in real-time, scalability,
| 70888 |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | ------------- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| protection | durability, |     | and low | latency. | A   | blockchain | dis- |     |     |     |     |     |
| ---------- | ----------- | --- | ------- | -------- | --- | ---------- | ---- | --- | --- | --- | --- | --- |
tributedcloudsystemwithanSDNcontrollercansolvethese
problems.
2) PROPOSEDFRAMEWORK
| The proposed |     | architecture |     | in [205] | is  | based | on three |     |     |     |     |     |
| ------------ | --- | ------------ | --- | -------- | --- | ----- | -------- | --- | --- | --- | --- | --- |
phases.ThismodelmonitorsandparsesimportantOpenFlow
| messages   | from          | OpenFlow |              | packets   | to create  |          | an overall |     |     |     |     |     |
| ---------- | ------------- | -------- | ------------ | --------- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- |
| network    | view in       | the      | first phase. | In        | the second |          | phase, the |     |     |     |     |     |
| data set   | was analyzed, |          | and          | the state | of         | routing  | topology   |     |     |     |     |     |
| extracted, | and Metadata  |          | features     | sets      | for        | building | a traffic  |     |     |     |     |     |
flowtopologygrid.Theproposedarchitecturemaintainsthe
Metadata’stopologicalstatus,flowdesignrulesforoutbound
| flows, store | transmission |     | of  | inbound | packet | headers, | etc. |     |     |     |     |     |
| ------------ | ------------ | --- | --- | ------- | ------ | -------- | ---- | --- | --- | --- | --- | --- |
Aparticularmetadataflowvalidatethepermissiblemetadata
| values collected |        | over        | the flow | and       | management |          | strategies  |     |     |     |     |     |
| ---------------- | ------ | ----------- | -------- | --------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- |
| duration         | in the | third       | stage.   | The model | flags      | knew     | attacks     |     |     |     |     |     |
| by the manager   |        | strategies, | despite  |           | being      | the most | specific    |     |     |     |     |     |
| flow activities  |        | conducted   | over     | time      | to         | detect   | potentially |     |     |     |     |     |
maliciousactivity.Whenthemodelfindsnewflowbehavior,
| it does    | not trigger | an    | alarm:     | it   | triggers | alarms      | when it  |           |                                      |     |     |     |
| ---------- | ----------- | ----- | ---------- | ---- | -------- | ----------- | -------- | --------- | ------------------------------------ | --- | --- | --- |
|            |             |       |            |      |          |             |          | FIGURE33. | BlockchainandNFVforsmartcondominium. |     |     |     |
| recognizes | unreliable  |       | entities   | that | change   | an existing | flow     |           |                                      |     |     |     |
| or flow    | behavior,   | which | challenges |      | a        | specific    | security |           |                                      |     |     |     |
policy. or cloud orchestration layer. The IoT device Layer works
|     |     |     |     |     |     |     |     | as a perception | layer | of the IoT environment, |     | such as |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ----------------------- | --- | ------- |
3) CRITICALANALYSIS sensors, responsible for extracting the information passing
The author provides the network with a programmable thisinformationtotheSDNcontroller.TheSDNcontrolleris
controller to ensure scalability and durability with high responsibleforroutingtheparticulardatatothedestination.
availability. The proposed architecture uses cloud and NFV layer provides different network functions such as
| fog nodes | for | data | collection, |     | and blockchain |     | is used |          |                 |                  |     |             |
| --------- | --- | ---- | ----------- | --- | -------------- | --- | ------- | -------- | --------------- | ---------------- | --- | ----------- |
|           |     |      |             |     |                |     |         | routing, | security, etc., | to the framework | in  | the form of |
to protect data transfer transparency. The data processed a distributed package. The cloud orchestration layer is
at the server’s end is secured, enhancing the possibility responsibleforputtingthedataonthepublicblockchain.The
of confidential data leakage. Fog nodes for protecting proposed architecture is implemented with the topology of
data transfer from cloud to IoT nodes. The blockchain 50networknodeswithnineaccesspoints(APs).
| functionality | is  | used for | cost-effective |     | access | management |     |     |     |     |     |     |
| ------------- | --- | -------- | -------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
systems. The proposed architecture will greatly minimize 3) CRITICALANALYSIS
| end-to-end | delays | for | IoT applications, |     | machine |     | resources, |                |                |             |     |            |
| ---------- | ------ | --- | ----------------- | --- | ------- | --- | ---------- | -------------- | -------------- | ----------- | --- | ---------- |
|            |        |     |                   |     |         |     |            | A distributed, | secure SDN-IoT | model based | on  | blockchain |
and core network traffic loads relative to conventional IoT as shown in Fig. 33 was propsed by [206]. The study
architecture.
|     |     |     |     |     |     |     |     | proposed | a CHS (Cluster | Head Selection) | algorithm | that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --------------- | --------- | ---- |
selectsCH(ClusterHead)withthehighestenergyoptimally.
G. BLOCKCHAIN-BASESDNMODELFORIoTs TheSDNcontrollercontinuouslymonitorsandmanagesIoT
1) MOTIVATION device information across the entire IoT network; it also
ThecombinationofSDN,NFV,andblockchainarecapable detects possible attacks on the network system; it enhances
of addressing reliable communication in IoT environments scalabilityandflexibilityissues.NFVthensuppliesavirtual
suchasprotection,privacy,flexibility,performance,andIoT platform to the SDN-IoT-enabled physical environment
environment availability. A safe communication platform and saves money, extending the entire network’s lifetime.
or channel has been highlighted as a key requirement for Distributed blockchain also provides ample security and
efficientcommunicationinIoTsystems. privacy; it efficiently identifies and mitigates cyber attacks
intheproposedscheme.
2) PROPOSEDFRAMEWORK
In[206],theauthorsproposedasmartcondominiumframe- H. BLOCKCHAIN-BASEDSECURITYFRAMEWORKFOR
| workbasedonSDNtechnologyandblockchaintechnology, |     |     |     |     |     |     |     | SDNs |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
toimprovetheprotectionofIoTenvironments.Theproposed 1) MOTIVATION
architecture is based on a layered approach: IoT device Existing literature suggests that in SDNs, the main danger
Layer, SDN controller layer, NFV layer, Middle Layer, is the single point of failure. Any failure of the controller
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     | 70889 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
would affect the network’s overall functionality, as the 3) CRITICALANALYSIS
| primary | objective | of  | the | attackers | was | to  | compromise |              |     |              |     |       |                |     |        |
| ------- | --------- | --- | --- | --------- | --- | --- | ---------- | ------------ | --- | ------------ | --- | ----- | -------------- | --- | ------ |
|         |           |     |     |           |     |     |            | The proposed |     | architecture |     | lacks | the discussion |     | on the |
the controller. In [207], the authors proposed a security algorithmic approach and does not provide implementation
model to ensure compliance with enhanced security based detailsthatcandemonstratetheeffectivenessoftheproposed
| on blockchain |     | technology |     | between | instances |     | of the SDN | framework. |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ------- | --------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
controller.
J. DISCUSSIONOFRESULTS
2) PROPOSEDFRAMEWORK It has been discovered that IoT devices generate a large
|             |          |     |           |     |       |          |           | amount | of data, | which | must | then | be stored | and | evalu- |
| ----------- | -------- | --- | --------- | --- | ----- | -------- | --------- | ------ | -------- | ----- | ---- | ---- | --------- | --- | ------ |
| The authors | proposed |     | a control |     | plane | security | algorithm |        |          |       |      |      |           |     |        |
and choose to deploy security models using the OpenDay- ated for analysis to extract new insights. Blockchain has
|             |             |     |         |             |           |        |          | played      | a significant |            | role in | decentralized |     | IoT networks. |     |
| ----------- | ----------- | --- | ------- | ----------- | --------- | ------ | -------- | ----------- | ------------- | ---------- | ------- | ------------- | --- | ------------- | --- |
| light SDN   | controller. |     | The     | proposed    | framework |        | uses the |             |               |            |         |               |     |               |     |
|             |             |     |         |             |           |        |          | Distributed | Ledger        | Technology |         | (DLT)         | and | decentralized |     |
| open-source | blockchain  |     | project | hyperledger |           | fabric | with an  |             |               |            |         |               |     |               |     |
adaptiveconsensusmoduletobuildtheunderlyingprotection cryptocurrencies(suchasBitcoin[211],Ethereum[212]etc.,
|     |     |     |     |     |     |     |     | and the | technology | beyond |     | them | has become | a trending |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------ | --- | ---- | ---------- | ---------- | --- |
mechanism.Theirmodulararchitectureallowsthecontroller
andblockchainproviders’coreservicestobecombinedwhile research area in recent years. For every IoT operation
maintainingtheperformancescale. (such as create, update, delete, and read) in the blockchain
|     |     |     |     |     |     |     |     | blocks,   | each data | item | can be      | saved | as a transaction. |             | Smart |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---- | ----------- | ----- | ----------------- | ----------- | ----- |
|     |     |     |     |     |     |     |     | contracts | can be    | used | to register | the   | identity          | information |       |
3) CRITICALANALYSIS
|                  |             |          |     |          |             |         |            | of IoT      | devices | in a block  | with | current | status     | and instance |     |
| ---------------- | ----------- | -------- | --- | -------- | ----------- | ------- | ---------- | ----------- | ------- | ----------- | ---- | ------- | ---------- | ------------ | --- |
| The architecture |             | proposed |     | provides | a           | general | overview   |             |         |             |      |         |            |              |     |
|                  |             |          |     |          |             |         |            | information | of      | production, | as   | well    | as control | policies     | for |
| and lacks        | information |          | on  | how      | the various |         | components |             |         |             |      |         |            |              |     |
IoTdevices.Table-13summarizestheeffortsofSDN-based
| function      | and communicate |             |     | with | each      | other. | There is no |            |          |     |            |     |            |       |     |
| ------------- | --------------- | ----------- | --- | ---- | --------- | ------ | ----------- | ---------- | -------- | --- | ---------- | --- | ---------- | ----- | --- |
|               |                 |             |     |      |           |        |             | blockchain | taxonomy |     | to address | the | management | issue | of  |
| comprehensive |                 | algorithmic |     | work | presented |        | because the |            |          |     |            |     |            |       |     |
IoTnetworks.
architectureislaidoutingenerallayers.Theauthorsprovided
|                   |     |     |            |     |        |              |     | RQ1:           | How | can SDN-based |           | frameworks |     | provide         | effi- |
| ----------------- | --- | --- | ---------- | --- | ------ | ------------ | --- | -------------- | --- | ------------- | --------- | ---------- | --- | --------------- | ----- |
| no implementation |     | and | evaluation |     | of the | architecture | as  |                |     |               |           |            |     |                 |       |
|                   |     |     |            |     |        |              |     | cient security |     | solutions     | to manage |            | IoT | network-related |       |
well.
securityissues?Duetoalackofexperienceandevaluationin
theexitingIoTsolution,itischallengingtoidentifydevices
I. DDoSBOTNETPREVENTIONUSINGBLOCKCHAIN
|     |     |     |     |     |     |     |     | that are | vulnerable | to  | the environment |     | in  | the IoT domain. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------------- | --- | --- | --------------- | --- |
1) MOTIVATION
|     |     |     |     |     |     |     |     | The authors | in  | [202] | suggested | StewARD, |     | an SDN | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --------- | -------- | --- | ------ | --- |
Thestudy[208]addressestheincreasinglygrowingnumber blockchain-based trust system that uses an SDN controller
ofIoTdevices,whichatthesametimeleadstonetworking,
|     |     |     |     |     |     |     |     | to determine | a   | trust level | based | on  | a trust | score based | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | ----- | --- | ------- | ----------- | --- |
protection, management problems, and the possibility of a blockchain record. In [203] highlights the IoT domain
| being part          | of a | botnet | to launch | a   | DDoS       | attack. | According |                 |        |               |            |            |      |                    |     |
| ------------------- | ---- | ------ | --------- | --- | ---------- | ------- | --------- | --------------- | ------ | ------------- | ---------- | ---------- | ---- | ------------------ | --- |
|                     |      |        |           |     |            |         |           | confronts       | issues | in digital    | forensics, |            | such | as data integrity, |     |
| to the researchers, |      | the    | Internet  | of  | Everything | (IoE)   | leads to  |                 |        |               |            |            |      |                    |     |
|                     |      |        |           |     |            |         |           | proof deletion, |        | or alteration |            | to resolve |      | those problems.    |     |
more and new problems rather than solving existing ones. Althoughblockchainisbeingusedasasolutionintheexisting
| Therefore, | they | proposed | new | techniques |     | to  | protect IoT |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | --- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
literature,thetechnologyitselfhaspoorattackdetectionand
networksagainstDDoSattacks. processing speed. SDN-IoT presents a forensic architecture
thatefficientlyovercomestheobstaclesofcreatingaCustody
2) PROPOSEDFRAMEWORK Chain(CoC)usingblockchaintechnology.Authorsin[213]
The proposed framework integrates a blockchain SDN discuss the blockchain-based security solutions in terms of
controller to manage the distributed nature of IoT devices privacyleakageandselfishmining.Table-13showsthatsecu-
efficiently. The proposed framework consists of three rityfeaturesareoneofthecorethemesofblockchain-based
modules: Security Policy Module (SecPoliMod), Controller SDN solutions to address the management challenges of
| Module | (ConMod), | and | LogModule |     | (LogMod), |     | in which | IoTnetworks. |     |     |     |     |     |     |     |
| ------ | --------- | --- | --------- | --- | --------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
SecPoliMod and ConMod are primarily programmed to RQ2: How can SDN-based frameworks provide effec-
prevent the use of IoT devices as botnets, while Log- tive fault tolerance management solutions to large-scale
Mod controls network traffic for the devices in order to IoT networks? Few of the existing studies [191] and [192]
ensure their legitimacy. To implement security policy and examine security and resource management in terms
differentiate between legitimate and illegitimate connected of fault tolerance technique using a private and public
devices, SecPoliMod relies on the colored coins concept blockchain method. In [200], the authors explored a use
introducedbyblockchaintechnology.Ifadeviceiscolored, case study in terms of contact aware Access Control for
thisindicatesthatthedevicehasmettheminimumnetwork IoT, in which fault-tolerant routing is one of the critical
linksecuritycriteria.However,networktrafficflowingfrom elements, as well as how fault-tolerance mechanisms relate
that system will be separated and dropped by the switches to other key challenges of IoT. The authors in [201]
before integrating with other network traffic if no label is discusses the fault tolerance in three aspects that is Fog
identifiedonthedevice. computational nodes, Computing Services, and Network
| 70890 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
TABLE13. SummaryofblockchainbasedsolutionaddressesIoTmanagementchallenges.
TABLE14. SummaryofblockchainbasedSDNIoTsolution.
topology aspect. Fog computational Nodes maintain a fog RQ4: What scalable solutions can be offered by
leveltableandarule-basedmechanismtomaintainthefault SDN-based frameworks to manage IoT networks? With
tolerance. exponential development in network management and con-
RQ3: What are the potential solutions regarding load figuration complexity, SDN has emerged as a promising
balancing in SDN-based frameworks to manage IoT network model. SDN aims to improve network function
networks? Edge, fog, and cloud infrastructure all work efficiency by making network design and operations more
independently in an IoT ecosystem. However, efforts have dynamic and efficient. Authors in [209] discuss the way to
recently been made to integrate all of these to serve thescalableapproachofSDNsolution.In[210],theauthors
IoT applications, but security, resource management, and discuss scalability challenges when dynamic solutions are
multi-application execution load balancing remain the key required to manage IoT networks. One of the challenges
challenges to overcome. To address these concerns, the is dynamic networks policies. Table-13 suggests that the
authors in [201] introduced FogBus. This platform enables majorityoftheproposedsolutionsarescalableinnature,but
end-to-end IoT-Fog-Cloud integration using blockchain to frameworkdiscussionshowsthattheproposedsolutionsare
ensure data integrity, secrecy, and reliability in terms implementedinverylimitedtestbeds.
of load balancing. Existing literature suggests that fault RQ5:HowcanSDN-basedframeworksenableefficient
load-balancing is the critical feature to address the IoT power consumption in IoT networks? Energy usage and
managementchallengesduetotheconsensusalgorithminthe device heterogeneity are all long-standing issues in the
blockchain-basedSDNframework. IoT business. In data transmission through IoT and edge
VOLUME10,2022 70891

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
networks,securityandenergyconsiderationsarecritical.The 2) ENERGYMANAGEMENT
combination of blockchain and SDN has the potential to Energy is a precious resource in IoT networks, because
tackle energy and security challenges in IoT networks. The the deployed sensor devices do not have access to the
authorsin[204]presentanarchitecturebasedondistributed uninterrupted power supply. In the SDN paradigm, the
networkmanagementforIoTdevices,whichisimplemented SDN controller can help schedule network flows, resulting
in a cluster structure utilizing an IoT-tailored blockchain in energy savings. Furthermore, centralizing the network’s
andSDNcontroller.ThearchitectureforcommunicatingIoT architecture allows for an aggregation of energy-efficient
devicesusingSDNcontrollerslinkedtoasingleblockchain. knowledge. This is one of the most significant issues
The suggested architecture’s primary goals are to improve that will gain significance with the increasing number of
IoT communication security while also lowering energy IoT devices deployed worldwide. Literature suggests that
usage. To maximize the IoT network, private and public most proposed SDN-based management frameworks for
blockchainsaredeployed. efficient energy management solutions for IoT networks
concerning lightweight cryptographic algorithms, efficient
IX. LESSONSLEARNED routingmechanisms,efficientschedulingalgorithmsetc
Thissectionprovidesthelessonslearnedfromtheproposed
taxonomy to address the IoT management issues with SDN 3) SECURITYMANAGEMENT
integration. Moreover, we present the lessons learned from Providing and ensuring security services over a resource-
SDNtoaddressthedefinedIoTmanagementchallenges. constrainedIoTnetworkischallengingastraditionalsecurity
protocols and mechanisms are not applicable in the IoT
A. LESSONLEARNEDFROMSDNTOADDRESSIoT security domain. Literature suggests that most of the
FRAMEWORK’SMANAGEMENTCHALLENGES proposed works in the area of SDIoT security frameworks
It is known that infrastructures built around SDN-enabled is related to access-list, authentication, authorization, and
IoT units have a tremendous potential [214]. SDN can key management. However, all of the proposed solutions
provide orchestration for network management in the IoT also have another critical issues, i.e., they depreciate the
environment by decoupling the control plane and the data performance energy consumption. Most proposed security
plane, including flexibility and programmability in the IoT solutionsaretestedonparticularusecases.However,attack
network. This is the main reason why the SDN-based IoT mitigation or the prevention module are missing in the
networkshasthepotentialtoaddressIoTmanagementissues majorityoftheproposedframeworks.
suchasfaulttolerance,loadbalancing,etc.Separationofthe
controlanddataplanesisavitalaspectoftheSDNparadigm. 4) LOADBALANCING
Ithasobviousbenefitsintermsofnetworkprogrammability. Load balancing is considerably eased by the deployment
The control plane can be centralized or decentralized, that of SDN in IoT networks. SDN creates a centralized view
helps in developing and implementing dynamic policies at of the network traffic as the data is being transmitted to
the perception layer, control layer, etc., in IoT networks to the controller. This centralized control can thus be used to
addressmanagementchallenges. optimize the traffic load passing through the IoT network.
Furthermore, load estimation techniques and algorithms at
the controller can assess the IoT network load, influencing
1) FAULTTOLERANCE
the flow traffic in the IoT network. A number of efforts
Fault tolerance techniques for IoT networks are classified
are made to tackle load management problems in IoT in
as fault prevention, fault detection, fault isolation, and fault
the application layer and the network layer with the help of
recovery [170]. SDN controllers can enable the design
efficient path selection mechanisms and efficient load shift
and creation of efficient fault detection techniques for IoT
algorithms.
networks due to its centralized view. The IoT nodes send
datatothecentralcontroller,whichcaneasilydetectfaultsat
particularnodes.Onceafaulthasbeenidentified,thecentral 5) SCALABILITY
control can quickly reconfigure the network to circumvent The implementation of SDN in IoT significantly simplifies
the faulty nodes or routes. Extensive research is needed the scalability of IoT networks. To enhance the scalability
to design novel fault detection and mitigation algorithms of SDN-based IoT networks, several studies have been
for SDN-based IoT networks.Literature suggests that, most conductedinthepast.Thecontrolplanewasfirstrestructured
proposed SDN-based management frameworks for efficient byscatteringcontrollershorizontallyorhierarchicallywhile
faulttolerancemanagementsolutionsforIoTnetworksareat maintaining unified control over each distributed controller.
thenetworklayer,withsolutionsforroutingprotocols,fault According to the existing literature, considerable attention
detection,reconfiguration,linkstatus,andcongestioncontrol is given to global visibility, link-state discovery, flow-rule
mechanisms.Applicationandservicelayerprotocolsreceive positioning,andcontrollerloadunbalancingincomplexand
lessattention. large-scalenetworks.
70892 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
| B. LESSONSLEARNEDFROMOTHERAPPROACHES |     |     |     |     |     |     |     | 3) OpenFLow |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
INTEGRATEDWITHSDNTOADDRESSTHEIoT OpenFlow is the first dominant SDN flow control protocol,
FRAMEWORK’SMANAGEMENTCHALLENGES which has already been the defacto standard for SDN
controllers[217].Communicationbetweenthecontrollayer
1) NETWORKFUNCTIONVIRTUALIZATION
SDNs have been widely deployed in the IoT environment, andtheforwardinglayerisachievedthroughthesouthbound
where they have been primarily used for flow optimization interface, and OpenFlow is one of the widely used south-
and related policies to manage IoT networks [215]. Virtual- bound APIs [218]. The existing literature suggested that
izationintermsofnetworks,functions,andapplicationshas researchers put efforts to improve the management issues
|     |     |     |     |     |     |     |     | of IoT with | the | help of | OpenFlow |     | Southbound | API. | Still, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | -------- | --- | ---------- | ---- | ------ |
alsoseenimmensecontributionsintherecentpast.Toaddress
IoT resource management problems, we studied both SDN we noticed that most of the implementation was done to
and virtualization combination frameworks in the literature manage load balancing issues in IoT, and a majority of the
review and classified them into different IoT management proposedframeworkslackedimplementationdetails.
solutions[216].WenoticethattheSDNframeworkislimited
tovirtualizingtheIPstack’snetworklayer,wherethetraffic 4) BLOCKCHAIN
| flow of | the IoT | network | is  | configured. | Therefore, |     | in terms |            |            |     |                 |     |               |     |      |
| ------- | ------- | ------- | --- | ----------- | ---------- | --- | -------- | ---------- | ---------- | --- | --------------- | --- | ------------- | --- | ---- |
|         |         |         |     |             |            |     |          | Blockchain | technology |     | is conceptually |     | fundamentally |     | dif- |
ofimplementation,theproposedsolutionsfocusprimarilyon
|     |     |     |     |     |     |     |     | ferent from | SDN, | as  | with | a blockchain, |     | information | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | ---- | ------------- | --- | ----------- | --- |
security solutions instead of combining other management decentralized in a P2P network and the need for a trusted
issuesinIoTnetworks
|     |     |     |     |     |     |     |     | third party | is  | removed. | In  | regards | of  | accessibility | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | ------- | --- | ------------- | --- |
Accordingtotheexistingliterature,therearetwowaysto
|     |     |     |     |     |     |     |     | transactions, | blockchains |     | are | classified | as  | public, | private, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --- | ---------- | --- | ------- | -------- |
buildanNFV/SDN-basedarchitecturetosolveIoTnetwork or consortium. In a public blockchain, all nodes take part
| management | issues: |     | one from | the | NFV side | and | the other |                  |     |         |     |        |     |             |       |
| ---------- | ------- | --- | -------- | --- | -------- | --- | --------- | ---------------- | --- | ------- | --- | ------ | --- | ----------- | ----- |
|            |         |     |          |     |          |     |           | in the consensus |     | process | and | review | the | transaction | data. |
from the SDN side. The NFV management and network On the contrary, in private and consortium blockchains,
| orchestration |     | (MANO) | framework |     | places | various | VNFs on |             |               |     |              |     |         |     |         |
| ------------- | --- | ------ | --------- | --- | ------ | ------- | ------- | ----------- | ------------- | --- | ------------ | --- | ------- | --- | ------- |
|               |     |        |           |     |        |         |         | transaction | accessibility |     | is typically |     | granted | and | revoked |
theNFVsideusedintheSDNcontrolplane,whichprovides
|     |     |     |     |     |     |     |     | based on | a centralized |     | agency | judgment. |     | Only | a small |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------ | --------- | --- | ---- | ------- |
multiple services to IoT networks such as security, load numberofpre-approvednodesareinvolvedintheconsensus
balancing,faulttolerance,etc.TheSDN-sideSDNcontroller
|     |     |     |     |     |     |     |     | process. | SDN breaks |     | the vertical |     | integration | of  | the data |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------------ | --- | ----------- | --- | -------- |
in the NFV framework has its management strategies to and controls planes and passes the network’s control logic
solvetheIoTmanagementproblem[50].Themajorityofthe
|     |     |     |     |     |     |     |     | to an SDN | controller |     | called | a centralized |     | entity | [219]. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------ | ------------- | --- | ------ | ------ |
proposedsolutionisdistributedinnature,mainlyfocusingon
|     |     |     |     |     |     |     |     | SDN frameworks |     | themselves |     | have itself | has | some | security |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ---- | -------- |
fault tolerance and load balancing constraints with the help limitations such as single point failure, improper network
ofSDN’sflowtables,resourcemanagementaccess-lists,etc.
|     |     |     |     |     |     |     |     | rule insertion, | DDOS, |     | etc., that | may | affect | the performance |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --- | ---------- | --- | ------ | --------------- | --- |
ScalabilityisprovidedwiththehelpoftheNFVmanagement of the IoT network. The combination of blockchain and
| framework. | In        | terms | of the | NFV taxonomy, |         | the  | proposed |            |               |        |           |                |             |         |          |
| ---------- | --------- | ----- | ------ | ------------- | ------- | ---- | -------- | ---------- | ------------- | ------ | --------- | -------------- | ----------- | ------- | -------- |
|            |           |       |        |               |         |      |          | SDN has    | the potential |        | to manage |                | IoT network |         | resource |
| security   | solutions | are   | mainly | from          | the NFV | side | in which |            |               |        |           |                |             |         |          |
|            |           |       |        |               |         |      |          | management | issues        | [220]. | In        | the literature |             | review, | we find  |
different virtual security solutions are provided to the IoT that security, scalability, decentralization, and traceability
networksintheformofVNFs.
|     |     |     |     |     |     |     |     | are the   | main features |     | of blockchain |     | technology |      | that can |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------- | --- | ---------- | ---- | -------- |
|     |     |     |     |     |     |     |     | assist an | SDN-based     |     | framework     | in  | dealing    | with | various  |
2) MIDDLEWARE-BASEDSDNSOLUTION
|                |          |            |              |               |          |                     |          | challenges.         | Moreover,        |         | latency   | remains   | a constant |           | challenge |
| -------------- | -------- | ---------- | ------------ | ------------- | -------- | ------------------- | -------- | ------------------- | ---------------- | ------- | --------- | --------- | ---------- | --------- | --------- |
| The middleware |          | layer      | plays        | a significant |          | role in integration |          |                     |                  |         |           |           |            |           |           |
|                |          |            |              |               |          |                     |          | in blockchain-based |                  | SDN     | solutions |           | in IoT     | networks. | The       |
| with the       | SDN      | controller | to           | manage        | the IoT  | networks.           | This     |                     |                  |         |           |           |            |           |           |
|                |          |            |              |               |          |                     |          | majority            | of the           | related | papers    | suggested |            | that      | load bal- |
| layer reduces  |          | the SDN    | controller’s |               | workload | and                 | provides |                     |                  |         |           |           |            |           |           |
|                |          |            |              |               |          |                     |          | ancing,             | fault tolerance, |         | and       | energy    | management |           | in IoT    |
| additional     | benefits | to         | the control  | plane         | and      | the data            | plane.   |                     |                  |         |           |           |            |           |           |
networkscanbeachievedwiththehelpofblockchain-based
Inthegatheredliterature,mostoftheproposedframeworks’
smart-contracts.
middlewarelayersconsistofaperceptionlayer,accesslayer,
| and edge | layer. | The | majority | of solutions |     | focus | on load- |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | -------- | ------------ | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
X. OPENRESEARCHCHALLENGESANDFUTURE
balancing,fault-tolerance,andscalabilitywheretheproposed
OPPORTUNITIES
| algorithms | in  | the middleware |     | layer | include | SBIs | and NBIs |     |     |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | ----- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
forcontrolanddataplanes.Theauthorsdiscussthescalable ThissectionfocusesontheSDIoTmanagementframework’s
activeresearchareasandopenresearchproblemsconnected
| middleware    | solution  |           | for interoperability |            |             | across      | heteroge- |                |          |            |       |            |            |            |     |
| ------------- | --------- | --------- | -------------------- | ---------- | ----------- | ----------- | --------- | -------------- | -------- | ---------- | ----- | ---------- | ---------- | ---------- | --- |
|               |           |           |                      |            |             |             |           | to the defined | taxonomy |            | i,e., | NFV,       | Middleware | Openflow   |     |
| neous devices |           | that      | serve                | in various | application |             | domains,  |                |          |            |       |            |            |            |     |
|               |           |           |                      |            |             |             |           | adaptation     | and      | Blockchain |       | to address | IoT        | management |     |
| such as       | discovery | protocols |                      | to manage  |             | IoT devices | and       |                |          |            |       |            |            |            |     |
challenges.
| context-aware |     | IoT applications |     | also | focus | on computation |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------- | --- | ---- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andsecurityparametersinordertoprovideefficientsolutions
to address the IoT management challenges,minimal effort A. NETWORKFUNCTIONVIRTUALIZATION
towardefficientmodulesthatmanagesecurity,energyissues InSDN-basedframeworksforIoTnetworks,NFViscritical
inIoTnetworkscanbenoticed. for properly handling data traffic and meeting resource
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 70893 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
management framework requirements. More research subject includes enforcing dynamic open-flow rules and
towards context-aware NFV employing AI to govern IoT procedures for various resource and security management
frameworks is necessary [221]. During the last few years, issues, i.e., user authentication, software reliability, threat
theNFVbasedSD-IoTmanagementsolutionhasdeveloped detection,lackofregularpatchesandupdates,untrustworthy
context-aware learning tools and systems. The most preva- communication, and data privacy concerns [53]. Dedicated
lent solutions are rule-based, logic-based, ontology-based, hardware appliances are replaced by programs running
supervised, unsupervised, and reinforcement algorithms on virtual network functions (VNFs) that need intense
to improve performance [222]. It is possible to utilize a packet processing under the network function virtualization
combination of hybrid machine learning approaches, such paradigm.Inthefuture,thereisaneedforVNF-basedadap-
as rule-based and ensemble-based algorithms, to provide a tive programmable rules-based distributed SDN switches
bettermanagementframeworkandmoreadvancedreasoning managingmechanismsforloadbalancing,energyefficiency,
capabilities to address the management challenges [223]. data plane scalability, and traffic flow QoS requirements
Connecting each IoT device to a power source is not in IoT, in addition to Open Flow heterogeneous switches
always possible. IoT devices must be energy efficient in resources [229] Mobile nodes are the most common IoT
order to smooth the running of IoT network [224]. In the devicesthatrequiremobilitymanagementprotocolstodeliver
future, there is a need for power-hungry IoT devices with transparent services to users without delays or disconnec-
NFV-based architecture based on to save energy while tions. Packet loss, end-to-end delay, increased handover
maintaining QoS standards. Security challenges related latency, increased signalling costs, and power consumption
to container-based virtualization technologies are also a is just a few of the concerns and problems that affect
popular topic. However, we can still ensure the security of communicationbetweenmobilenodesinamobileIPcapable
container-basedarchitecturesbyrunningthemontopofVMs network. In future, there is a need for an AI-based adaptive
byusinganadaptiveapproach[61]. protocol suite that handles the mobility management of IoT
devices[230].
B. MIDDLEWARE-BASEDSOLUTIONS
In combination with edge computing, the emergence of the D. BLOCKCHAIN-BASEDSOLUTIONS
IoThasrecentlyopenedupseveralpossibilitiesfornewappli- Dynamicinteroperabilityandprotocolstandardisationwillbe
cations[225].Acommonchallengeisprovidingapersistent required in the future, posing further hurdles in addressing
infrastructure,i.e.,aservicecapableofcontinuouslysustain- IoT device management issues in the smart city [60].
ingahigh-efficiencylevel,facingpotentialfailures,etc.Inthe To achieve full Interoperability (i.e., from data to policy
future, there is a need for a middleware solution that works interoperability) and integration with heterogeneous IoT
asalightweight,adaptiveengineinSDN-basedframeworks systems, the adoption of Blockchain will be the key that
to manage IoT resource management issues [224]. An in- helps to overcome these challenges in IoT with the help of
depth investigation is needed to understand how centrally federated learning.Blockchain has been viewed as a viable
controlled IoT networks are managed via SDN-based IoT fabricforasecure,decentralizedIoTedgeinrecentyearsdue
frameworks and how they can recover from faults, manage to its inherent qualities of fault tolerance, transparency, and
the sensor nodes’ energy more efficiently, balance traffic enforcementofservicelevelagreementsthroughsmartcon-
within the network, and provide security to the network tracts [59]. Despite their advantages, blockchains confront
and its applications. Making the network status available to severalchallenges.Oneofthehighlightedchallengesisinthe
the SDN controller can help provide security services such on-demanddecentralizedhorizontalscalingofanIoT-based
as attack mitigation, privacy, lightweight key management, smartcitynetworks.Blockchain-baseddecentralizedsecurity
etc., for IoT networks [226]. Combining the proliferation frameworks for IoT networks that works adaptively and
of cloud-based network services as a middleware solution dynamicallytoadoptmultiplesecuritysolutionswillhighly
with SDN for solving IoT network management problems berequiredinthenearfuture[58].
has created new challenges in cloud service selection, and
ranking [227]. Because of the wide range of cloud services XI. CONCLUSION
available,thereisaneedforIoTnetworkstoselectcarefully The IoT paradigm presents a future of computing that is
the one that would suit their needs best and adjust to rapidlygainingtractioninourlivesasameansofimproving
their circumstances accordingly. Because of the intelligent thequalityoflifebyconnectingarangeofintelligentdevices,
capabilities of network slicing and edge computing. Edge technologies, services, and applications. However, there are
applications must have adjustability, dynamism, usability, several challenges within the IoT network management
flexibility, interoperability, and compatibility with other frameworks that require novel solutions. These challenges
technologiesarerequired[60]. revolve around the fragile nature of IoT devices in terms
of faults; failure in the wake of higher traffic load; security
C. OpenFlowADAPTATIONS weaknesses; the lack of energy efficiency; and scalability.
ThecombinationofnetworkprogrammabilityandIoTcomes IoTdevicesareheterogeneousandresource-constrained.The
withnewissuesforIoTnetworks[228].Themostemphasized operation of these diverse IoT devices requires specialized
70894 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
network behavior and services such as security, efficient [4] T. Qiu, N. Chen, K. Li, M. Atiquzzaman, and W. Zhao, ‘‘How can
energy management, load management module, etc., that heterogeneous Internet of Things build our future: A survey,’’ IEEE
Commun.SurveysTuts.,vol.20,no.3,pp.2011–2027,3rdQuart.,2018.
| is also overhead |     | to the  | IoT networks. |     | SDN,  | with | its novel  |               |     |           |               |           |              |            |               |
| ---------------- | --- | ------- | ------------- | --- | ----- | ---- | ---------- | ------------- | --- | --------- | ------------- | --------- | ------------ | ---------- | ------------- |
|                  |     |         |               |     |       |      |            | [5] J. Gubbi, | R.  | Buyya, S. | Marusic,      | and M.    | Palaniswami, | ‘‘Internet | of            |
| approaches       | to  | network | management    |     | along | with | its latest |               |     |           |               |           |              |            |               |
|                  |     |         |               |     |       |      |            | Things(IoT):  |     | A vision, | architectural | elements, | and          | future     | directions,’’ |
developments within the realm of IoT offers promising FutureGenerat.Comput.Syst.,vol.29,no.7,pp.1645–1660,2013.
solutions.SDNprovidesglobalvisibilityofthenetworkstate [6] B.Guo,D.Zhang,Z.Wang,Z.Yu,andX.Zhou,‘‘OpportunisticIoT:
ExploringtheharmoniousinteractionbetweenhumanandtheInternet
| and logically                                         | centralized |     | control | of  | resources, | which | can |              |     |               |        |      |         |                  |     |
| ----------------------------------------------------- | ----------- | --- | ------- | --- | ---------- | ----- | --- | ------------ | --- | ------------- | ------ | ---- | ------- | ---------------- | --- |
|                                                       |             |     |         |     |            |       |     | of Things,’’ | J.  | Netw. Comput. | Appl., | vol. | 36, no. | 6, pp.1531–1539, |     |
| bephysicallydistributedifrequired,throughprogrammable |             |     |         |     |            |       |     | Nov.2013.    |     |               |        |      |         |                  |     |
APIs from a central vintage point. Thus, SDN facilitates [7] T.Park,N.Abuzainab,andW.Saad,‘‘Learninghowtocommunicatein
theInternetofThings:Finiteresourcesandheterogeneity,’’IEEEAccess,
| novel techniques |     | for network |     | management. |     | Therefore, | huge |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | ----------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.4,pp.7063–7073,2016.
researcheffortsarededicatedtodevelopingSDN-basedIoT [8] I.Bedhief,M.Kassar,andT.Aguili,‘‘SDN-basedarchitecturechalleng-
managementframeworks. ingtheIoTheterogeneity,’’inProc.3rdSmartCloudNetw.Syst.(SCNS),
Dec.2016,pp.1–3.
Thisarticlepresentsadetailedoverviewofthestate-of-the-
[9] L.Farhan,S.T.Shukur,A.E.Alissa,M.Alrweg,U.Raza,andR.Kharel,
| art of important |     | SDN-based |     | IoT management |     | frameworks. |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
‘‘AsurveyonthechallengesandopportunitiesoftheInternetofThings
Theseframeworksarediscussedintermsoffourkeytrends: (IoT),’’inProc.11thInt.Conf.Sens.Technol.(ICST),Dec.2017,pp.1–5.
1) NFV-based frameworks, 2) Middleware-based frame- [10] P.Mishra,D.Puthal,M.Tiwary,andS.P.Mohanty,‘‘Softwaredefined
|     |     |     |     |     |     |     |     | IoT systems: |     | Properties, | state of | the art, | and future | research,’’ | IEEE |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | -------- | -------- | ---------- | ----------- | ---- |
works,3)OpenFlow-basedframeworks,and4)Blockchain-
WirelessCommun.,vol.26,no.6,pp.64–71,Dec.2019.
based frameworks. All the proposed architectures discussed [11] H. I. Kobo, A. M. Abu-Mahfouz, and G. P. Hancke, ‘‘A survey
in this article are utilizing the reconfiguration capabilities on software-defined wireless sensor networks: Challenges and design
of SDNs, which is fundamental to existing and future IoT requirements,’’IEEEAccess,vol.5,pp.1872–1899,2017.
[12] M.A.Hassan,Q.-T.Vien,andM.Aiash,‘‘Softwaredefinednetworking
| systems. | The main | theme | in  | these | four | dimensions | is to |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | --- | ----- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
forwirelesssensornetworks:Asurvey,’’Adv.WirelessCommun.Netw.,
improve fault tolerance, energy and security management, vol.3,pp.10–22,May2017.
|     |     |     |     |     |     |     |     | [13] H. Huang, | J.  | Zhu, and | L. Zhang, | ‘‘An | SDN_based | management |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------- | ---- | --------- | ---------- | --- |
loadbalancing,andimprovingscalability.Albeit,SDNlays
frameworkforIoTdevices,’’inProc.25thIETIrishSignalsSyst.Conf.,
| the foundation |     | for robust | management |     | solutions, |     | AI-based |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ---------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
China-IrelandInt.Conf.Inf.Commun.Technol.(ISSC/CIICT).IET,2014.
| approaches | in  | conjunction | with | SDN | are | still lacking | to  |                  |     |           |             |     |        |              |       |
| ---------- | --- | ----------- | ---- | --- | --- | ------------- | --- | ---------------- | --- | --------- | ----------- | --- | ------ | ------------ | ----- |
|            |     |             |      |     |     |               |     | [14] O. Flauzac, | C.  | Gonzalez, | A. Hachani, |     | and F. | Nolot, ‘‘SDN | based |
embed intelligent decision-making during uncertain situa- architectureforIoTandimprovementofthesecurity,’’inProc.IEEE29th
Int.Conf.Adv.Inf.Netw.Appl.Workshops,Mar.2015,pp.688–693.
| tions. Blockchain, |     | IoT, | and | AI are | innovations |     | that can |     |     |     |     |     |     |     |     |
| ------------------ | --- | ---- | --- | ------ | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[15] Y.Yuan,D.Lin,R.Alur,andB.T.Loo,‘‘Scenario-basedprogramming
promise benefits in security, transparency, immutability, forSDNpolicies,’’inProc.11thACMConf.Emerg.Netw.Experiments
privacy, and business process automation in IoT networks. Technol.,Dec.2015,pp.1–13.
However, when blockchain, IoT, and AI are combined into [16] Z. Qin, G. Denker, C. Giannelli, P. Bellavista, and
|        |           |     |        |     |           |     |          | N.Venkatasubramanian, |     |     | ‘‘A software | defined | networking |     | architecture |
| ------ | --------- | --- | ------ | --- | --------- | --- | -------- | --------------------- | --- | --- | ------------ | ------- | ---------- | --- | ------------ |
| an SDN | framework | to  | manage | IoT | networks, | the | benefits |                       |     |     |              |         |            |     |              |
fortheInternet-of-Things,’’inProc.IEEENetw.Oper.Manage.Symp.
of these technologies can even be higher. In the future, (NOMS),May2014,pp.1–9.
|             |      |      |          |     |              |     |          | [17] P. Hu,  | ‘‘A system | architecture | for  | software-defined |     | industrial | Internet  |
| ----------- | ---- | ---- | -------- | --- | ------------ | --- | -------- | ------------ | ---------- | ------------ | ---- | ---------------- | --- | ---------- | --------- |
| we envision | that | with | the help | of  | AI, adaptive |     | resource |              |            |              |      |                  |     |            |           |
|             |      |      |          |     |              |     |          | of Things,’’ | in         | Proc. IEEE   | Int. | Conf. Ubiquitous |     | Wireless   | Broadband |
managementframeworksforIoTnetworkswillbeintroduced
(ICUWB),Oct.2015,pp.1–5.
| that will | also include |     | blockchain-based |     | SDN | frameworks. |     |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ---------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[18] V.R.Tadinada,‘‘Softwaredefinednetworking:Redefiningthefutureof
Moreover, the envisioned deployment of IoT on a wide internetinIoTandcloudera,’’inProc.Int.Conf.FutureInternetThings
scale would reveal further practical challenges since most Cloud,Aug.2014,pp.296–301.
|     |     |     |     |     |     |     |     | [19] S. Scott-Hayward, |     | G. O’Callaghan, |     | and | S. Sezer, | ‘‘SDN | security: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --------------- | --- | --- | --------- | ----- | --------- |
of the existing research is either in constrained and lab A survey,’’ in Proc. IEEE SDN Future Netw. Services (SDN4FNS),
environmentsorbasedontheoreticalevaluations.Thestate- Nov.2013,pp.1–7.
of-the-art research work identified in this article suggests [20] N. Bizanis and F. Kuipers, ‘‘SDN and virtualization solutions for the
InternetofThings:Asurvey,’’IEEEAccess,vol.4,pp.5591–5606,2016.
| that the dynamism |     | provided |     | by SDN | can | help reconfigure |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[21] M.Díaz,C.Martín,andB.Rubio,‘‘State-of-the-art,challenges,andopen
| or update | and upgrade |     | the IoT | network | at  | run-time | to solve |        |                    |     |             |           |     |                    |     |
| --------- | ----------- | --- | ------- | ------- | --- | -------- | -------- | ------ | ------------------ | --- | ----------- | --------- | --- | ------------------ | --- |
|           |             |     |         |         |     |          |          | issues | in the integration |     | of Internet | of Things | and | cloud computing,’’ |     |
emergingchallenges. J.Netw.Comput.Appl.,vol.67,pp.99–117,May2016.
[22] D.Qiang,N.Ansari,andM.Toy,‘‘Software-definednetworkvirtual-
ization:AnarchitecturalframeworkforintegratingSDNandNFVfor
REFERENCES service provisioning in future networks,’’ IEEE Netw., vol. 30, no. 5,
pp.10–16,Sep./Oct.2016.
[1] A.Al-Fuqaha,M.Guizani,M.Mohammadi,M.Aledhari,andM.Ayyash, [23] C. Bouras, A. Kollia, and A. Papazois, ‘‘SDN & NFV in 5G:
| ‘‘Internet | of  | Things: | A survey | on enabling | technologies, |     | protocols, |              |     |                   |     |          |      |              |         |
| ---------- | --- | ------- | -------- | ----------- | ------------- | --- | ---------- | ------------ | --- | ----------------- | --- | -------- | ---- | ------------ | ------- |
|            |     |         |          |             |               |     |            | Advancements |     | and challenges,’’ |     | in Proc. | 20th | Conf. Innov. | Clouds, |
and applications,’’ IEEE Commun. Surveys Tuts., vol. 17, no. 4, InternetNetw.(ICIN),Mar.2017,pp.107–111.
pp.2347–2376,4thQuart.,2015. [24] S.K.Tayyaba,M.A.Shah,O.A.Khan,andA.W.Ahmed,‘‘Software
[2] I.Ahmad,T.Kumar,M.Liyanage,M.Ylianttila,T.Koskela,T.Braysy, definednetwork(SDN)basedInternetofThings(IoT):Aroadahead,’’
A. Anttonen, V. Pentikinen, J.-P. Soininen, and J. Huusko, ‘‘Towards inProc.Int.Conf.FutureNetw.Distrib.Syst.,Jul.2017,pp.1–8.
gadget-freeinternetservices:Aroadmapofthenakedworld,’’Telematics [25] S.Bera,S.Misra,andA.V.Vasilakos,‘‘Software-definednetworking
Inform., vol. 35, no. 1, pp.82–92, Apr. 2018. [Online]. Available: forInternetofThings:Asurvey,’’IEEEInternetThingsJ.,vol.4,no.6,
https://www.sciencedirect.com/science/article/pii/S0736585316305597
pp.1994–2008,Dec.2017.
[3] M. Marjani, F. Nasaruddin, A. Gani, A. Karim, I. A. T. Hashem, [26] X.Huang,S.Cheng,K.Cao,P.Cong,T.Wei,andS.Hu,‘‘Asurvey
A.Siddiqa, and I. Yaqoob, ‘‘Big IoT Data analytics: Architecture, of deployment solutions and optimization strategies for hybrid SDN
opportunities, and open research challenges,’’ IEEE Access, vol. 5, networks,’’IEEECommun.SurveysTuts.,vol.21,no.2,pp.1483–1507,
| pp.5247–5261,2017. |     |     |     |     |     |     |     | 2ndQuart.,2018. |     |     |     |     |     |     |       |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME10,2022      |     |     |     |     |     |     |     |                 |     |     |     |     |     |     | 70895 |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
[27] H.Zhang,Z.Cai,Q.Liu,Q.Xiao,Y.Li,andC.F.Cheang,‘‘Asurveyon [48] C. Jiang, T. Fan, H. Gao, W. Shi, L. Liu, C. Cerin, and J.Wan,
security-awaremeasurementinSDN,’’Secur.Commun.Netw.,vol.2018, ‘‘Energyawareedgecomputing:Asurvey,’’Comput.Commun.,vol.151,
pp.1–14,Apr.2018. pp.556–580,Feb.2020.
[28] M. A. Ferrag, M. Derdour, M. Mukherjee, A. Derhab, L. Maglaras, [49] W. Rafique, L. Qi, I. Yaqoob, M. Imran, R. U. Rasool, and W. Dou,
and H. Janicke, ‘‘Blockchain technologies for the Internet of Things: ‘‘ComplementingIoTservicesthroughsoftwaredefinednetworkingand
Researchissuesandchallenges,’’IEEEInternetThingsJ.,vol.6,no.2, edge computing: A comprehensive survey,’’ IEEE Commun. Surveys
pp.2188–2204,Apr.2019. Tuts.,vol.22,no.3,pp.1761–1804,3rdQuart.,2020.
[29] W.Gao,W.G.Hatcher,andW.Yu,‘‘Asurveyofblockchain:Techniques, [50] A.A.Barakabitze,A.Ahmad,R.Mijumbi,andA.Hines,‘‘5Gnetwork
applications,andchallenges,’’inProc.27thInt.Conf.Comput.Commun. slicingusingSDNandNFV:Asurveyoftaxonomy,architecturesand
Netw.(ICCCN),Jul.2018,pp.1–11. futurechallenges,’’Comput.Netw.,vol.167,Feb.2020,Art.no.106984.
[30] I.Farris,T.Taleb,Y.Khettab,andJ.Song,‘‘AsurveyonemergingSDN [51] D. Saha, M. Shojaee, M. Baddeley, and I. Haque, ‘‘An energy-aware
andNFVsecuritymechanismsforIoTsystems,’’IEEECommun.Surveys SDN/NFVarchitecturefortheInternetofThings,’’inProc.IFIPNetw.
Tuts.,vol.21,no.1,pp.812–837,1stQuart.,2019. Conf.Netw.,Jun.2020,pp.604–608.
[31] H.Zemrane,Y.Baddi,andA.Hasbi,‘‘SDN-basedsolutionstoimprove [52] A.Imteaj,U.Thakker,S.Wang,J.Li,andM.H.Amini,‘‘Asurveyon
IoT: Survey,’’ in Proc. IEEE 5th Int. Congr. Inf. Sci. Technol. (CiSt), federatedlearningforresource-constrainedIoTdevices,’’IEEEInternet
Oct.2018,pp.588–593. ThingsJ.,vol.9,no.1,pp.1–24,Jan.2022.
[32] R.KanagaveluandK.M.M.Aung,‘‘AsurveyonSDNbasedsecurity [53] V.Mothukuri,R.M.Parizi,S.Pouriyeh,Y.Huang,A.Dehghantanha,and
in Internet of Things,’’ in Proc. Future Inf. Commun. Conf. Cham, G.Srivastava,‘‘Asurveyonsecurityandprivacyoffederatedlearning,’’
Switzerland:Springer,2018,pp.563–577. FutureGener.Comput.Syst.,vol.115,pp.619–640,Feb.2021.
[33] M.Burhan,R.Rehman,B.Khan,andB.-S.Kim,‘‘IoTelements,layered [54] P.P.RayandN.Kumar,‘‘SDN/NFVarchitecturesforedge-cloudoriented
architectures and security issues: A comprehensive survey,’’ Sensors, IoT:Asystematicreview,’’Comput.Commun.,vol.169,pp.129–153,
vol.18,no.9,p.2796,Aug.2018. Mar.2021.
[34] M. S. Ali, M. Vecchio, M. Pincheira, K. Dolui, F. Antonelli, and [55] M. A. Uddin, A. Stranieri, I. Gondal, and V. Balasubramanian, ‘‘A
M.H.Rehmani,‘‘ApplicationsofblockchainsintheInternetofThings: surveyontheadoptionofblockchaininIoT:Challengesandsolutions,’’
Acomprehensivesurvey,’’IEEECommun.SurveysTuts.,vol.21,no.2, Blockchain,Res.Appl.,vol.2,no.2,Jun.2021,Art.no.100006.
pp.1676–1717,2ndQuart.,2019. [56] S.AhmadandA.H.Mir,‘‘Scalability,consistency,reliabilityandsecurity
[35] F. H. Pohrmen, R. K. Das, and G. Saha, ‘‘Blockchain-based security inSDNcontrollers:AsurveyofdiverseSDNcontrollers,’’J.Netw.Syst.
aspects in heterogeneous Internet-of-Things networks: A survey,’’ Manage.,vol.29,no.1,pp.1–59,Jan.2021.
Trans. Emerg. Telecommun. Technol., vol. 30, no. 10, Oct. 2019, [57] S. Khorsandroo, A. G. Sánchez, A. S. Tosun, J. Arco, and
Art.no.e3741. R.Doriguzzi-Corin, ‘‘Hybrid SDN evolution: A comprehensive
[36] X.Wang,X.Zha,W.Ni,R.P.Liu,Y.J.Guo,X.Niu,andK.Zheng, survey of the state-of-the-art,’’ Comput. Netw., vol. 192, Jun. 2021,
‘‘Survey on blockchain for Internet of Things,’’ Comput. Commun., Art.no.107981.
vol.136,pp.10–29,Feb.2019. [58] N. Alasbali, S. R. B. Azzuhri, R. B. Salleh, M. L. M. Kiah,
[37] M. Wu, K. Wang, X. Cai, S. Guo, M. Guo, and C. Rong, ‘‘A A.A.A.S.A.Shariffuddin, N. M. I. B. N. M. Kamel, and L. Ismail,
comprehensivesurveyofblockchain:FromtheorytoIoTapplicationsand ‘‘Rulesof smartIoT networkswithin smartcities towardsblockchain
beyond,’’IEEEInternetThingsJ.,vol.6,no.5,pp.8114–8154,Oct.2019. standardization,’’MobileInf.Syst.,vol.2022,pp.1–11,Feb.2022.
[38] M.Alsaeedi,M.M.Mohamad,andA.A.Al-Roubaiey,‘‘Towardadaptive [59] I.Ahmed,Y.Zhang,G.Jeon,W.Lin,M.R.Khosravi,andL.Qi,‘‘A
and scalable OpenFlow-SDN flow control: A survey,’’ IEEE Access, blockchain-andartificialintelligence-enabledsmartIoTframeworkfor
vol.7,pp.107346–107379,2019. sustainablecity,’’Int.J.Intell.Syst.,2022,doi:10.1002/int.22852.
[39] J.Anish,A.G.Singh,andK.Neeraj,‘‘SURVIVOR:Ablockchainbased [60] B.GhimireandD.B.Rawat,‘‘Recentadvancesonfederatedlearning
edge-as-a-serviceframeworkforsecureenergytradinginSDN-enabled for cybersecurity and cybersecurity for federated learning for Internet
vehicle-to-grid environment,’’ Comput. Netw., vol. 153, pp.36–48, of Things,’’ IEEE Internet Things J., vol. 9, no. 11, pp.8229–8249,
Apr.2019. Jun.2022.
[40] N. Tariq, M. Asim, F. Al-Obeidat, M. F. Farooqi, T. Baker, [61] Z.Shah,I.Ullah,H.Li,A.Levula,andK.Khurshid,‘‘Blockchainbased
M.Hammoudeh, and I. Ghafir, ‘‘The security of big data in fog- solutionstomitigatedistributeddenialofservice(DDoS)attacksinthe
enabled IoT applications including blockchain: A survey,’’ Sensors, Internet of Things (IoT): A survey,’’ Sensors, vol. 22, no. 3, p.1094,
vol.19,no.8,p.1788,2019. Jan.2022.
[41] R. Chaudhary, A. Jindal, G. S. Aujla, S. Aggarwal, N. Kumar, and [62] B. A. A. Nunes, M. Mendonca, X.-N. Nguyen, K. Obraczka, and
K.K.R.Choo,‘‘BEST:Blockchain-basedsecureenergytradinginSDN- T. Turletti, ‘‘A survey of software-defined networking: Past, present,
enabled intelligent transportation system,’’ Comput. Secur., vol. 85, andfutureofprogrammablenetworks,’’IEEECommun.SurveysTuts.,
pp.288–299,Aug.2019. vol.16,no.3,pp.1617–1634,3rdQuart.,2014.
[42] A. A. Gebremariam, M. Usman, and M. Qaraqe, ‘‘Applications of [63] O.Salman,I.Elhajj,A.Chehab,andA.Kayssi,‘‘IoTsurvey:AnSDN
artificialintelligenceandmachinelearningintheareaofSDNandNFV: andfogcomputingperspective,’’Comput.Netw.,vol.143,pp.221–246,
Asurvey,’’inProc.16thInt.Multi-Conf.Syst.,SignalsDevices(SSD), Oct.2018.
Mar.2019,pp.545–549. [64] M.Ndiaye,G.P.Hancke,andA.M.Abu-Mahfouz,‘‘Softwaredefined
[43] P. B. Pajila and E. G. Julie, ‘‘Detection of DDoS attack using networking for improved wireless sensor network management: A
SDN in IoT: A survey,’’ in Intelligent Communication Technologies survey,’’Sensors,vol.17,no.5,p.1031,2017.
and Virtual Mobile Networks. Cham, Switzerland: Springer, 2019, [65] W. Iqbal, H. Abbas, M. Daneshmand, B. Rauf, and Y. A. Bangash,
pp.438–452. ‘‘Anin-depthanalysisofIoTsecurityrequirements,challenges,andtheir
[44] A. Dorri, ‘‘LSB: A Lightweight Scalable Blockchain for IoT security countermeasuresviasoftware-definedsecurity,’’IEEEInternetThingsJ.,
and anonymity,’’ J. Parallel Distrib. Comput., vol. 134, pp.180–197, vol.7,no.10,pp.10250–10276,Oct.2020.
Dec.2019. [66] M. B. Yassein, S. Aljawarneh, M. Al-Rousan, W. Mardini, and
[45] B. K. Mohanta, D. Jena, U. Satapathy, and S. Patnaik, ‘‘Survey on W.Al-Rashdan,‘‘Combinedsoftware-definednetwork(SDN)andInter-
IoTsecurity:Challengesandsolutionusingmachinelearning,artificial netofThings(IoT),’’inProc.Int.Conf.Electr.Comput.Technol.Appl.
intelligence and blockchain technology,’’ Internet Things, vol. 11, (ICECTA),Nov.2017,pp.1–6.
Sep.2020,Art.no.100227. [67] J. Chen, J. Chen, F. Xu, M. Yin, and W. Zhang, ‘‘When software
[46] J.Hu,M.Reed,N.Thomos,M.F.AI-Naday,andK.Yang,‘‘Securing defined networks meet fault tolerance: A survey,’’ in Proc. Int. Conf.
SDN-controlledIoTnetworksthroughedgeblockchain,’’IEEEInternet AlgorithmsArchit.ParallelProcess.Cham,Switzerland:Springer,2015,
ThingsJ.,vol.8,no.4,pp.2102–2115,Feb.2021. pp.351–368.
[47] I.Alam,K.Sharif,F.Li,Z.Latif,M.M.Karim,S.Biswas,B.Nour, [68] Y. Yu, X. Li, X. Leng, L. Song, K. Bu, Y. Chen, J. Yang, L.
andY.Wang,‘‘AsurveyofnetworkvirtualizationtechniquesforInternet Zhang,K.Cheng,andX.Xiao,‘‘Faultmanagementinsoftware-defined
ofThingsusingSDNandNFV,’’ACMComput.Surv.,vol.53,no.2, networking: A survey,’’ IEEE Commun. Surveys Tuts., vol. 21, no. 1,
pp.1–40,Mar.2021. pp.349–392,1stQuart.,2018.
70896 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
[69] T.Wang,F.Liu,andH.Xu,‘‘Anefficientonlinealgorithmfordynamic [93] S. Sezer, S. Scott-Hayward, P. K. Chouhan, B. Fraser, D. Lake,
SDNcontrollerassignmentindatacenternetworks,’’IEEE/ACMTrans. J.Finnegan, N. Viljoen, M. Miller, and N. Rao, ‘‘Are we ready for
Netw.,vol.25,no.5,pp.2788–2801,Oct.2017. SDN?Implementationchallengesforsoftware-definednetworks,’’IEEE
[70] S. Moin, A. Karim, K. Safdar, I. Iqbal, Z. Safdar, V. Vijayakumar, Commun.Mag.,vol.51,no.7,pp.36–43,Jul.2013.
K.T.Ahmed,andS.A.Abid,‘‘GREENSDN—Anenhancedparadigmof [94] N.McKeown,T.Anderson,H.Balakrishnan,G.Parulkar,L.Peterson,
SDN:Review,taxonomy,andfuturedirections,’’ConcurrencyComput., J.Rexford,S.Shenker,andJ.Turner,‘‘OpenFlow:Enablinginnovation
Pract.Exper.,vol.32,no.21,Nov.2020,Art.no.e5086. incampusnetworks,’’ACMSIGCOMMComput.Commun.Rev.,vol.38,
[71] I.Hamzaoui,B.Duthil,V.Courboulay,andH.Medromi,‘‘Asurveyon no.2,pp.69–74,Apr.2008.
thecurrentchallengesofenergy-efficientcloudresourcesmanagement,’’ [95] A.Lara,A.Kolasani,andB.Ramamurthy,‘‘Networkinnovationusing
SocialNetw.Comput.Sci.,vol.1,no.2,pp.1–28,Mar.2020. OpenFlow: A survey,’’ IEEE Commun. Surveys Tuts., vol. 16, no. 1,
[72] K.InayatandS.O.Hwang,‘‘Loadbalancingindecentralizedsmartgrid pp.493–512,1stQuart.,2014.
trade system using blockchain,’’ J. Intell. Fuzzy Syst., vol. 35, no. 6, [96] I.F.Akyildiz,A.Lee,P.Wang,M.Luo,andW.Chou,‘‘Aroadmapfor
pp.5901–5911,Dec.2018. trafficengineeringinSDN-OpenFlownetworks,’’Comput.Netw.,vol.71,
[73] Z. Shu, J. Wan, J. Lin, S. Wang, D. Li, S. Rho, and C. Yang, pp.1–30,Oct.2014.
‘‘Trafficengineeringinsoftware-definednetworking:Measurementand [97] B.AgborubereandE.Sanchez-Velazquez,‘‘OpenFlowcommunications
management,’’IEEEAccess,vol.4,pp.3246–3256,2016. andTLSsecurityinsoftware-definednetworks,’’inProc.IEEEInt.Conf.
[74] I.Ahmad,S.Namal,M.Ylianttila,andA.Gurtov,‘‘Securityinsoftware InternetThings(iThings)IEEEGreenComput.Commun.(GreenCom)
definednetworks:Asurvey,’’IEEECommun.SurveysTuts.,vol.17,no.4, IEEE Cyber, Phys. Social Comput. (CPSCom) IEEE Smart Data
pp.2317–2346,4thQuart.,2015. (SmartData),Jun.2017,pp.560–566.
[75] J.Bhayo,S.Hameed,andS.A.Shah,‘‘Anefficientcounter-basedDDoS [98] A. Doria, J. H. Salim, R. Haas, H. M. Khosravi, W. Wang, L.
attackdetectionframeworkleveragingsoftwaredefinedIoT(SD-IoT),’’ Dong,R.Gopal,andJ.M.Halpern,ForwardingandControlElement
IEEEAccess,vol.8,pp.221612–221631,2020. Separation(ForCES)ProtocolSpecification,documentRFC,5810,2010,
[76] N.Z.Bawany,J.A.Shamsi,andK.Salah,‘‘DDoSattackdetectionand pp.1–124.
mitigationusingSDN:Methods,practices,andsolutions,’’ArabianJ.Sci. [99] A.Prajapati,A.Sakadasariya,andJ.Patel,‘‘Softwaredefinednetwork:
Eng.,vol.42,no.2,pp.425–441,2017. Futureofnetworking,’’inProc.2ndInt.Conf.InventiveSyst.Control
[77] M. Monshizadeh, V. Khatri, and R. Kantola, ‘‘An adaptive detection (ICISC),Jan.2018,pp.1351–1354.
and prevention architecture for unsafe traffic in SDN enabled mobile
[100] M.Paliwal,D.Shrimankar,andO.Tembhurne,‘‘ControllersinSDN:A
networks,’’inProc.IFIP/IEEESymp.Integr.Netw.ServiceManage.(IM),
reviewreport,’’IEEEAccess,vol.6,pp.36256–36270,2018.
May2017,pp.883–884.
[101] M.N.A.Sheikh,M.Halder,S.S.Kabir,M.W.Miah,andS.Khatun,
[78] S.Biswas,K.Sharif,F.Li,B.Nour,andY.Wang,‘‘Ascalableblockchain
‘‘SDN-basedapproachtoevaluatethebestcontroller:Internalcontroller
frameworkforsecuretransactionsinIoT,’’IEEEInternetThingsJ.,vol.6,
NOXandexternalcontrollersPOX,ONOS,RYU,’’GlobalJ.Comput.
no.3,pp.4650–4659,Jun.2019.
Sci.Technol.,vol.19,pp.21–32,Feb.2019.
[79] B.Kitchenham,O.P.Brereton,D.Budgen,M.Turner,J.Bailey,and
[102] Z. K. Khattak, M. Awais, and A. Iqbal, ‘‘Performance evaluation of
S.Linkman,‘‘Systematicliteraturereviewsinsoftwareengineering—
OpenDaylightSDNcontroller,’’inProc.20thIEEEInt.Conf.Parallel
Asystematicliteraturereview,’’Inf.Softw.Technol.,vol.51,pp.7–15,
Distrib.Syst.(ICPADS),Dec.2014,pp.671–676.
Jan.2008.
[103] P.Berde,‘‘ONOS:Towardsanopen,distributedSDNOS,’’inProc.3rd
[80] B.Kitchenham,ProceduresforPerformingSystematicReviews,vol.33.
WorkshopHotTopicsSoftw.DefinedNetw.,2014,pp.1–6.
Keele,U.K.,KeeleUniv.,2004,pp.1–26.
[104] S.Hong,L.Xu,H.Wang,andG.Gu,‘‘Poisoningnetworkvisibilityin
[81] M.-K.Shin,K.-H.Nam,andH.-J.Kim,‘‘Software-definednetworking
software-definednetworks:Newattacksandcountermeasures,’’inProc.
(SDN):AreferencearchitectureandopenAPIs,’’inProc.Int.Conf.ICT
NDSS,vol.15,2015,pp.8–11.
Converg.(ICTC),Oct.2012,pp.360–361.
[105] I. Afolabi, T. Taleb, K. Samdanis, A. Ksentini, and H. Flinck,
[82] H. Mekky, F. Hao, S. Mukherjee, Z.-L. Zhang, and T. V. Lakshman,
‘‘Networkslicingandsoftwarization:Asurveyonprinciples,enabling
‘‘Application-aware data plane processing in SDN,’’ in Proc. 3rd
technologies,andsolutions,’’IEEECommun.SurveysTuts.,vol.20,no.3,
WorkshopHotTopicsSoftw.DefinedNetw.,Aug.2014,pp.13–18.
pp.2429–2453,3rdQuart.,2018.
[83] A. Nakao, ‘‘Software-defined data plane enhancing SDN and NFV,’’
IEICETrans.Commun.,vol.E98.B,no.1,pp.12–19,2015. [106] C. Rametta and G. Schembra, ‘‘Designing a softwarized network
deployedonafleetofdronesforruralzonemonitoring,’’FutureInternet,
[84] A. Kumari, R. Gupta, S. Tanwar, and N. Kumar, ‘‘A taxonomy of
vol.9,no.1,p.8,Mar.2017.
blockchain-enabledsoftwarizationforsecureUAVnetwork,’’Comput.
Commun.,vol.161,pp.304–323,Sep.2020. [107] N. Feamster, J. Rexford, and E. Zegura, ‘‘The road to SDN: An
[85] K.Phemius,M.Bouet,andJ.Leguay,‘‘DISCO:Distributedmulti-domain intellectual history of programmable networks,’’ ACM SIGCOMM
SDNcontrollers,’’inProc.IEEENetw.Oper.Manage.Symp.(NOMS), Comput.Commun.Rev.,vol.44,no.2,pp.87–98,Apr.2014.
May2014,pp.1–4. [108] N. Gude, T. Koponen, J. Pettit, B. Pfaff, M. Casado, N. McKeown,
[86] V.Thirupathi,C.Sandeep,N.Kumar,andP.Kumar,‘‘Acomprehensive and S. Shenker, ‘‘NOX: Towards an operating system for networks,’’
reviewonSDNarchitecture,applicationsandmajorbenifitsofSDN,’’ ACMSIGCOMMComput.Commun.Rev.,vol.38,no.3,pp.105–110,
Int.J.Adv.Sci.Technol.,vol.28,no.20,pp.607–614,2019. 2008.
[87] S.-Y. Wang, H.-W. Chiu, and C.-L. Chou, ‘‘Comparisons of SDN [109] S.Scott-Hayward,S.Natarajan,andS.Sezer,‘‘Asurveyofsecurityin
OpenFlowcontrollersoverEstiNet:Ryuvs.NOX,’’inProc.ICN,2015, softwaredefinednetworks,’’IEEECommun.SurveysTuts.,vol.18,no.1,
p.256. pp.623–654,1stQuart.,2016.
[88] M.Canini,D.Venzano,P.Perešíni,D.Kostić,andJ.Rexford,‘‘ANICE [110] A. A. Neghabi, N. J. Navimipour, M. Hosseinzadeh, and A. Rezaee,
waytotestOpenFlowapplications,’’inProc.9thUSENIXSymp.Netw. ‘‘Load balancing mechanisms in the software defined networks: A
Syst.DesignImplement.(NSDI),2012,pp.127–140. systematicandcomprehensivereviewoftheliterature,’’IEEEAccess,
[89] R.Skowyra,A.Lapets,A.Bestavros,andA.Kfoury,‘‘Averification vol.6,pp.14159–14178,2018.
platformforSDN-enabledapplications,’’inProc.IEEEInt.Conf.Cloud [111] I.D.PriyaandS.Silas,‘‘Asurveyonresearchchallengesandapplications
Eng.,Mar.2014,pp.337–342. in empowering the SDN-based Internet of Things,’’ in Advances in
[90] T. Ball, N. Bjørner, A. Gember, S. Itzhaky, A. Karbyshev, M. Sagiv, BigDataandCloudComputing(AdvancesinIntelligentSystemsand
M.Schapira,andA.Valadarsky,‘‘VeriCon:Towardsverifyingcontroller Computing),vol.750,J.Peter,A.Alavi,andB.Javadi,Eds.Singapore:
programsinsoftware-definednetworks,’’inProc.35thACMSIGPLAN Springer,2019,doi:10.1007/978-981-13-1882-5_39.
Conf.Program.Lang.DesignImplement.,2014,pp.282–293. [112] M.F.Tuysuz,Z.K.Ankarali,andD.Gözüpek,‘‘Asurveyonenergy
[91] Y. E. Oktian, S. Lee, H. Lee, and J. Lam, ‘‘Distributed SDN efficiency in software defined networks,’’ Comput. Netw., vol. 113,
controllersystem:Asurveyondesignchoice,’’Comput.Netw.,vol.121, pp.188–204,Feb.2017.
pp.100–111,Jul.2017. [113] Y.B.Zikria,S.W.Kim,O.Hahm,M.K.Afzal,andM.Y.Aalsalem,
[92] S. Singh and R. K. Jha, ‘‘A survey on software defined networking: ‘‘InternetofThings(IoT)operatingsystemsmanagement:Opportunities,
Architecture for next generation network,’’ J. Netw. Syst. Manage., challenges,andsolution,’’Sensors,vol.19,no.8,p.1793,Apr.2019,doi:
vol.25,no.2,pp.321–374,2017. 10.3390/s19081793.
VOLUME10,2022 70897

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
[114] M.A.Abbasi,Z.A.Memon,J.Memon,T.Q.Syed,andR.Alshboul, [137] M.Ojo,D.Adami,andS.Giordano,‘‘ASDN-IoTarchitecturewithNFV
‘‘AddressingthefuturedatamanagementchallengesinIoT:Aproposed implementation,’’ in Proc. IEEE Globecom Workshops (GC Wkshps),
framework,’’Int.J.Adv.Comput.Sci.Appl.,vol.8,no.5,pp.197–207, Dec.2016,pp.1–6.
2017. [138] V.G.Nguyen,A.Brunstrom,K.-J.Grinnemo,andJ.Taheri,‘‘SDN/NFV-
[115] T. Anagnostopoulos, A. Zaslavsky, K. Kolomvatsos, A. Medvedev, based mobile packet core network architectures: A survey,’’ IEEE
P.Amirian, J. Morley, and S. Hadjieftymiades, ‘‘Challenges and Commun.SurveysTuts.,vol.19,no.3,pp.1567–1602,3rdQuart.,2017.
opportunities of waste management in IoT-enabled smart cities: A [139] R. Ferrús, H. Koumaras, O. Sallent, G. Agapiou, T. Rasheed,
survey,’’ IEEE Trans. Sustain. Comput., vol. 2, no. 3, pp.275–289, M.-A.Kourtis, C. Boustie, P. Gélard, and T. Ahmed, ‘‘SDN/NFV-
Jul.2017. enabledsatellitecommunicationsnetworks:Opportunities,scenariosand
[116] K.Tejasvit,‘‘Challengesinintegratingwirelesssensornetworksintothe challenges,’’Phys.Commun.,vol.18,pp.95–112,Mar.2016.
internet,’’Int.J.Eng.Manage.Sci.,vol.5,no.1,pp.7–11,2014. [140] M. Monaco, O. Michel, and E. Keller, ‘‘Applying operating system
[117] R.Amin,M.Reisslein,andN.Shah,‘‘HybridSDNnetworks:Asurvey principlestoSDNcontrollerdesign,’’inProc.12thACMWorkshopHot
ofexistingapproaches,’’IEEECommun.SurveysTuts.,vol.20,no.4, TopicsNetw.,Nov.2013,pp.1–7.
pp.3259–3306,4thQuart.,2018. [141] K.Kaur,V.Mangat,andK.Kumar,‘‘Acomprehensivesurveyofservice
[118] N.Benamar,A.Jara,L.Ladid,andD.E.Ouadghiri,‘‘Challengesofthe functionchainprovisioningapproachesinSDNandNFVarchitecture,’’
InternetofThings:IPv6andnetworkmanagement,’’inProc.8thInt. Comput.Sci.Rev.,vol.38,Nov.2020,Art.no.100298.
Conf. Innov. Mobile Internet Services Ubiquitous Comput., Jul. 2014, [142] J.G.HerreraandJ.F.Botero,‘‘ResourceallocationinNFV:Acom-
pp.328–333. prehensivesurvey,’’IEEETrans.Netw.ServiceManage.,vol.13,no.3,
[119] A.P.AthreyaandP.Tague,‘‘Networkself-organizationintheInternet pp.518–532,Sep.2016.
ofThings,’’inProc.IEEEInt.WorkshopInternetThingsNetw.Control [143] N. Omnes, M. Bouillon, G. Fromentoux, and O. Grand, ‘‘A pro-
(IoT-NC),Jun.2013,pp.25–33. grammable and virtualized network IT infrastructure for the Internet
[120] A.ČolakovićandM.Hadžialić,‘‘InternetofThings(IoT):Areviewof of Things: How can NFV SDN help for facing the upcoming
enablingtechnologies,challenges,andopenresearchissues,’’Comput. challenges,’’ in Proc. 18th Int. Conf. Intell. Next Gener. Netw., 2015,
Netw.,vol.144,pp.17–39,Oct.2018. pp.64–69.
[121] M.AbomharaandG.M.Koien,‘‘SecurityandprivacyintheInternetof [144] J.Li,E.Altman,andC.Touati,‘‘AgeneralSDN-basedIoTframework
Things:Currentstatusandopenissues,’’inProc.Int.Conf.PrivacySecur. withNVFimplementation,’’ZTECommun.,vol.13,no.3,pp.42–45,
MobileSyst.(PRISMS),May2014,pp.1–8. 2015.
[122] I.Ali,A.I.A.Ahmed,A.Almogren,M.A.Raza,S.A.Shah,A.Khan, [145] M. J. Islam, M. Mahin, S. Roy, B. C. Debnath, and A. Khatun,
andA.Gani,‘‘SystematicliteraturereviewonIoT-basedbotnetattack,’’ ‘‘DistBlackNet:AdistributedsecureblackSDN-IoTarchitecturewith
IEEEAccess,vol.8,pp.212220–212232,2020. NFVimplementationforsmartcities,’’inProc.Int.Conf.Electr.,Comput.
Commun.Eng.(ECCE),Feb.2019,pp.1–6.
[123] S.Sicari,A.Rizzardi,L.A.Grieco,andA.Coen-Porisini,‘‘Security,
[146] R.Sairam,S.S.Bhunia,V.Thangavelu,andM.Gurusamy,‘‘NETRA:
privacyandtrustinInternetofThings:Theroadahead,’’Comput.Netw.,
EnhancingIoTsecurityusingNFV-basededgetrafficanalysis,’’IEEE
vol.76,pp.146–164,Jan.2015.
SensorsJ.,vol.19,no.12,pp.4660–4671,Jun.2019.
[124] Z.Yan,P.Zhang,andA.V.Vasilakos,‘‘Asurveyontrustmanagement
[147] T. D. Nguyen, S. Marchal, M. Miettinen, H. Fereidooni, N. Asokan,
forInternetofThings,’’J.Netw.Comput.Appl.,vol.42,pp.120–134,
andA.-R.Sadeghi,‘‘DÏoT:Afederatedself-learninganomalydetection
Jun.2014.
systemforIoT,’’inProc.IEEE39thInt.Conf.Distrib.Comput.Syst.
[125] S.T.Ali,V.Sivaraman,A.Radford,andS.Jha,‘‘Asurveyofsecuring
(ICDCS),Jul.2019,pp.756–767.
networksusingsoftwaredefinednetworking,’’IEEETrans.Rel.,vol.64,
[148] Y. Meidan, M. Bohadana, Y. Mathov, Y. Mirsky, A. Shabtai,
no.3,pp.1086–1097,Sep.2015,doi:10.1109/TR.2015.2421391.
D.Breitenbacher,andY.Elovici,‘‘N-BaIoT—Network-baseddetection
[126] M.T.MoghaddamandH.Muccini,‘‘Fault-tolerantIoT,’’inProc.Int.
ofIoTbotnetattacksusingdeepautoencoders,’’IEEEPervasiveComput.,
WorkshopSoftw.Eng.ResilientSyst.Cham,Switzerland:Springer,2019,
vol.17,no.3,pp.12–22,Jul.2018.
pp.67–84.
[149] Y. Afek, A. Bremler-Barr, D. Hay, R. Goldschmidt, L. Shafir,
[127] A.Javed,K.Heljanko,A.Buda,andK.Framling,‘‘CEFIoT:Afault-
G.Avraham,andA.Shalev,‘‘NFV-basedIoTsecurityforhomenetworks
tolerantIoTarchitectureforedgeandcloud,’’inProc.IEEE4thWorld
usingMUD,’’inProc.NOMSIEEE/IFIPNetw.Oper.Manage.Symp.,
ForumInternetThings(WF-IoT),Feb.2018,pp.813–818.
Apr.2020,pp.1–9.
[128] L. Paradis and Q. Han, ‘‘A survey of fault management in wireless
[150] P. Du, P. Putra, S. Yamamoto, and A. Nakao, ‘‘A context-aware IoT
sensornetworks,’’J.Netw.Syst.Manage.,vol.15,no.2,pp.171–190,
architecturethroughsoftware-defineddataplane,’’inProc.IEEERegion
Jun.2007.
Symp.(TENSYMP),May2016,pp.315–320.
[129] H. Trigui, R. Cuthill, and R. G. Kusyk, ‘‘Dynamic load balancing,’’
[151] P.Massonet,L.Deru,A.Achour,S.Dupont,L.-M.Croisez,A.Levin,
U.S.Patent8,498,207,Jul.30,2013.
andM.Villari,‘‘Securityinlightweightnetworkfunctionvirtualisation
[130] F.M.Al-Turjman,A.E.Al-Fagih,W.M.Alsalih,andH.S.Hassanein, forfederatedcloudandIoT,’’inProc.IEEE5thInt.Conf.FutureInternet
‘‘A delay-tolerant framework for integrated RSNs in IoT,’’ Comput. ThingsCloud(FiCloud),Aug.2017,pp.148–154.
Commun.,vol.36,no.9,pp.998–1010,May2013. [152] C. Zhang, ‘‘Design and application of fog computing and Internet of
[131] S.-Y. Chen, C.-F. Lai, Y.-M. Huang, and Y.-L. Jeng, ‘‘Intelligent Thingsserviceplatformforsmartcity,’’FutureGener.Comput.Syst.,
home-appliance recognition over IoT cloud network,’’ in Proc. 9th vol.112,pp.630–640,Nov.2020.
Int. Wireless Commun. Mobile Comput. Conf. (IWCMC), Jul. 2013, [153] J. Costa-Requena, M. Liyanage, M. Ylianttila, E. M. de Oca,
pp.639–643. J.L.Santos,V.F.Guasch,K.Ahokas,G.Premsankar,S.Luukkainen,
[132] L.Lengyel,P.Ekler,T.Ujj,T.Balogh,andH.Charaf,‘‘SensorHUB:An O.L.Perez,M.U.Itzazelaia,andI.Ahmad,‘‘SDNandNFVintegration
IoTdriverframeworkforsupportingsensornetworksanddataanalysis,’’ ingeneralizedmobilenetworkarchitecture,’’inProc.Eur.Conf.Netw.
Int.J.Distrib.SensorNetw.,vol.11,no.7,Jul.2015,Art.no.454379. Commun.(EuCNC),Jun.2015,pp.154–158.
[133] D.WajgiandN.V.Thakur,‘‘Loadbalancingalgorithmsinwirelesssensor [154] A.Dawoud,S.Shahristani,andC.Raun,‘‘Deeplearningandsoftware-
network:Asurvey,’’Int.J.Comput.Netw.WirelessCommun.(IJCNWC), defined networks: Towards secure IoT architecture,’’ Internet Things,
vol.2,pp.456–460,Aug.2012. vols.3–4,pp.82–89,Oct.2018.
[134] B.Duncan,A.Happe,andA.Bratterud,‘‘EnterpriseIoTsecurityand [155] Y. Li, X. Su, J. Riekki, T. Kanter, and R. Rahmani, ‘‘A SDN-based
scalability:Howunikernelscanimprovethestatusquo,’’inProc.9thInt. architectureforhorizontalInternetofThingsservices,’’inProc.IEEE
Conf.UtilityCloudComput.,Dec.2016,pp.292–297. Int.Conf.Commun.(ICC),May2016,pp.1–7.
[135] K. Georgiou, S. Xavier-de-Souza, and K. Eder, ‘‘The IoT energy [156] T. Alam, ‘‘A middleware framework between mobility and IoT using
challenge:Asoftwareperspective,’’IEEEEmbeddedSyst.Lett.,vol.10, IEEE 802.15.4e sensor networks,’’ Jurnal Online Informatika, vol. 4,
no.3,pp.53–56,Sep.2018. no.2,pp.90–94,2020.
[136] D.B.RawatandS.R.Reddy,‘‘Softwaredefinednetworkingarchitecture, [157] S.BansalandD.Kumar,‘‘IoTecosystem:Asurveyondevices,gateways,
securityandenergyefficiency:Asurvey,’’IEEECommun.SurveysTuts., operatingsystems,middlewareandcommunication,’’Int.J.WirelessInf.
vol.19,no.1,pp.325–346,1stQuart.,2017. Netw.,vol.27,no.3,pp.340–364,2020.
70898 VOLUME10,2022

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
[158] S. Bandyopadhyay, M. Sengupta, S. Maiti, and S. Dutta, ‘‘Role of [181] K.Ichino,‘‘OpenFlowcommunicationsystemandOpenFlowcommuni-
middlewareforInternetofThings:Astudy,’’Int.J.Comput.Sci.Eng. cationmethod,’’U.S.Patent8605734,Dec.10,2013.
Survey,vol.2,no.3,pp.94–105,2011. [182] D. Erickson, ‘‘The beacon openflow controller,’’ in Proc. 2nd ACM
[159] S. D. Castilho, E. P. Godoy, and F. Salmen, ‘‘Implementing security SIGCOMMWorkshopHotTopicsSoftw.DefinedNetw.(HotSDN),2013,
| andtrustinIoT/M2Musingmiddleware,’’inProc.Int.Conf.Inf.Netw. |     |     |     |     |     |     | pp.13–18. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
(ICOIN),Jan.2020,pp.726–731.
|     |     |     |     |     |     |     | [183] T. Luo, | H.-P. Tan, and | T. Q. | S. Quek, ‘‘Sensor | OpenFlow: | Enabling |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | ----- | ----------------- | --------- | -------- |
[160] S. Bhowmik, M. A. Tariq, B. Koldehofe, F. Durr, T. Kohler, and software-defined wireless sensor networks,’’ Commun. Lett., vol. 16,
K. Rothermel, ‘‘High performance publish/subscribe middleware in no.11,pp.1896–1899,Nov.2012.
software-defined networks,’’ IEEE/ACM Trans. Netw., vol. 25, no. 3, [184] T. Kanter, R. Rahmani, and A. Mahmud, ‘‘Conceptual framework
pp.1501–1516,Jun.2017. for Internet of Thing’ virtualization via OpenFlow in context-aware
[161] A.Antonić,M.Marjanović,K.Pripužić,andI.P.Žarko,‘‘Amobilecrowd
networks,’’Int.J.Comput.Sci.Issues,vol.10,no.6,p.16,2013.
sensingecosystemenabledbyCUPUS:Cloud-basedpublish/subscribe
[185] M.Conti,P.Kaliyar,andC.Lal,‘‘CENSOR:Cloud-enabledsecureIoT
middlewarefortheInternetofThings,’’FutureGenerat.Comput.Syst., architectureoverSDNparadigm,’’ConcurrencyComput.,Pract.Exper.,
vol.56,pp.607–622,Mar.2016. vol.31,no.8,Apr.2019,Art.no.e4978.
[162] Y.Wang,Y.Zhang,andJ.Chen,‘‘SDNPS:Aload-balancedtopic-based [186] M.Nagy,‘‘Softwaredefinednetworkinginwirelessmobilenetworks,’’
| publish/subscribe |     | system | in software-defined |     | networking,’’ | Appl. Sci., |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------------------- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
Inf.Sci.Technol.,Bull.ACMSlovakia,vol.11,no.1,pp.12–20,2019.
vol.6,no.4,p.91,Mar.2016.
[187] T.Luo,S.Zhang,andJ.Liu,‘‘Designofcentralizedcontrolarchitecture
[163] A.Hakiri,P.Berthou,A.Gokhale,andS.Abdellatif,‘‘Publish/subscribe-
|     |     |     |     |     |     |     | for distribution | network | communication | network | based | on SDN,’’ in |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ------------- | ------- | ----- | ------------ |
enabled software defined networking for efficient and scalable IoT Proc.Int.Conf.Commun.,Inf.Syst.Comput.Eng.(CISCE),Jul.2019,
| communications,’’ |     | IEEE | Commun. | Mag., | vol. 53, no. | 9, pp.48–54, | pp.59–64. |     |     |     |     |     |
| ----------------- | --- | ---- | ------- | ----- | ------------ | ------------ | --------- | --- | --- | --- | --- | --- |
Sep.2015.
|                |     |        |              |      |                              |     | [188] M. Nobakht, | C. Russell, | W.  | Hu, and A. | Seneviratne, | ‘‘IoT-NetSec: |
| -------------- | --- | ------ | ------------ | ---- | ---------------------------- | --- | ----------------- | ----------- | --- | ---------- | ------------ | ------------- |
| [164] Y. Wang, | Y.  | Zhang, | and J. Chen, | ‘‘An | SDN-based publish/subscribe- |     |                   |             |     |            |              |               |
Policy-basedIoTnetworksecurityusingOpenFlow,’’inProc.IEEEInt.
| enabled                         | communication |     | platform | for IoT | services,’’ China | Commun., |                      |                   |         |           |         |             |
| ------------------------------- | ------------- | --- | -------- | ------- | ----------------- | -------- | -------------------- | ----------------- | ------- | --------- | ------- | ----------- |
|                                 |               |     |          |         |                   |          | Conf.                | Pervasive Comput. | Commun. | Workshops | (PerCom | Workshops), |
| vol.15,no.1,pp.95–106,Jan.2018. |               |     |          |         |                   |          | Mar.2019,pp.955–960. |                   |         |           |         |             |
[165] P.F.MoraesandJ.S.B.Martins,‘‘Apub/subSDN-integratedframework [189] C. Gonzalez, S. M. Charfadine, O. Flauzac, and F. Nolot, ‘‘SDN-
forIoTtrafficorchestration,’’inProc.3rdInt.Conf.FutureNetw.Distrib.
|     |     |     |     |     |     |     | based | security framework | for | the IoT in | distributed | grid,’’ in Proc. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------ | --- | ---------- | ----------- | ---------------- |
Syst.,Jul.2019,pp.1–9.
Int.MultidisciplinaryConf.Comput.EnergySci.(SpliTech),Jul.2016,
| [166] Y. | Jararweh, | A. Mahmoud, | A.  | Darabseh, | E. Benkhelifa, | M. Vouk, |     |     |     |     |     |     |
| -------- | --------- | ----------- | --- | --------- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
pp.1–5.
andA.Rindos,‘‘SDIoT:AsoftwaredefinedbasedInternetofThings
[190] N.RaviandS.M.Shalinie,‘‘Learning-drivendetectionandmitigationof
framework,’’ J. Ambient Intell. Humanized Comput., vol. 6, no. 4, DDoSattackinIoTviaSDN-cloudarchitecture,’’IEEEInternetThings
pp.453–461,Aug.2015.
J.,vol.7,no.4,pp.3559–3570,Apr.2020.
[167] L.Galluccio,S.Milardo,G.Morabito,andS.Palazzo,‘‘SDN-WISE:
[191] J.Sun,J.Yan,andK.Z.K.Zhang,‘‘Blockchain-basedsharingservices:
Design,prototypingandexperimentationofastatefulSDNsolutionfor
Whatblockchaintechnologycancontributetosmartcities,’’Financial
| WIreless | SEnsor | networks,’’ | in  | Proc. IEEE | Conf. Comput. | Commun. |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ---------- | ------------- | ------- | --- | --- | --- | --- | --- | --- |
Innov.,vol.2,no.1,pp.1–9,Dec.2016.
(INFOCOM),Apr.2015,pp.513–521.
[168] M. Jacobsson and C. Orfanidis, ‘‘Using software-defined networking [192] Z. Zheng, S. Xie, H. Dai, X. Chen, and H. Wang, ‘‘An overview
ofblockchaintechnology:Architecture,consensus,andfuturetrends,’’
| principles | for | wireless | sensor | networks,’’ | in Proc. SNCNW. | Karlstad, |          |           |            |               |          |            |
| ---------- | --- | -------- | ------ | ----------- | --------------- | --------- | -------- | --------- | ---------- | ------------- | -------- | ---------- |
|            |     |          |        |             |                 |           | in Proc. | IEEE Int. | Congr. Big | Data (BigData | Congr.), | Jun. 2017, |
Sweden,May2015,pp.28–29.
pp.557–564.
[169] C.JacquenetandM.Boucadair,‘‘Asoftware-definedapproachtoIoT
[193] A.D.Dwivedi,G.Srivastava,S.Dhar,andR.Singh,‘‘Adecentralized
networking,’’ZTECommun.,vol.14,no.1,pp.61–68,2016.
[170] D.Wu,D.I.Arkhipov,E.Asmare,Z.Qin,andJ.A.McCann,‘‘UbiFlow: privacy-preservinghealthcareblockchainforIoT,’’Sensors,vol.19,no.2,
| Mobility | management |     | in urban-scale | software | defined | IoT,’’ in Proc. | p.326,2019. |     |     |     |     |     |
| -------- | ---------- | --- | -------------- | -------- | ------- | --------------- | ----------- | --- | --- | --- | --- | --- |
[194] T.P.Mashamba-ThompsonandE.D.Crayton,‘‘Blockchainandartificial
IEEEConf.Comput.Commun.(INFOCOM),Apr.2015,pp.208–216.
intelligencetechnologyfornovelcoronavirusdisease-19self-testing,’’
[171] H.AkramandA.Gokhale,‘‘RethinkingthedesignofLR-WPANIoT
|     |     |     |     |     |     |     | Diagnostics, | vol. 10, | no. 4, p. | 198, Apr. 2020, | doi: | 10.3390/diagnos- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --------- | --------------- | ---- | ---------------- |
systemswithsoftware-definednetworking,’’inProc.Int.Conf.Distrib.
| Comput.SensorSyst.(DCOSS),May2016,pp.238–243. |     |     |     |     |     |     | tics10040198. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
[172] J.Wan,S.Tang,Z.Shu,D.Li,S.Wang,M.Imran,andA.Vasilakos, [195] M.Kouhizadeh,S.Saberi,andJ.Sarkis,‘‘Blockchaintechnologyandthe
sustainablesupplychain:Theoreticallyexploringadoptionbarriers,’’Int.
‘‘Software-definedindustrialInternetofThingsinthecontextofindustry
J.Prod.Econ.,vol.231,Jan.2021,Art.no.107831.
4.0,’’IEEESensorsJ.,vol.16,no.20,pp.7373–7380,Oct.2016.
|                |     |        |           |        |                 |             | [196] J. Wu, | M. Dong, K. | Ota, J. | Li, and W. | Yang, ‘‘Application-aware |     |
| -------------- | --- | ------ | --------- | ------ | --------------- | ----------- | ------------ | ----------- | ------- | ---------- | ------------------------- | --- |
| [173] J. Zhou, | H.  | Jiang, | J. Wu, L. | Wu, C. | Zhu, and W. Li, | ‘‘SDN-based |              |             |         |            |                           |     |
applicationframeworkforwireless sensor andactornetworks,’’IEEE consensus management for software-defined intelligent blockchain in
Access,vol.4,pp.1583–1594,2016. IoT,’’IEEENetw.,vol.34,no.1,pp.69–75,Jan.2020.
[174] L.M.R.Arbiza,L.M.Bertholdo,C.R.P.dosSantos,L.Z.Granville, [197] H.-N.Dai,Z.Zheng,andY.Zhang,‘‘BlockchainforInternetofThings:
|     |       |             |               |     |                    |            | A survey,’’ | IEEE Internet | Things | J., vol. | 6, no. | 5, pp.8076–8094, |
| --- | ----- | ----------- | ------------- | --- | ------------------ | ---------- | ----------- | ------------- | ------ | -------- | ------ | ---------------- |
| and | L. M. | R. Tarouco, | ‘‘Refactoring |     | Internet of Things | middleware |             |               |        |          |        |                  |
Oct.2019.
| through | software-defined |     | network,’’ | in  | Proc. 30th Annu. | ACM Symp. |     |     |     |     |     |     |
| ------- | ---------------- | --- | ---------- | --- | ---------------- | --------- | --- | --- | --- | --- | --- | --- |
Appl.Comput.,Apr.2015,pp.640–645. [198] J.Sengupta,S.Ruj,andS.D.Bit,‘‘Acomprehensivesurveyonattacks,
[175] C. A. Ouedraogo, S. Medjiah, C. Chassot, and K. Drira, ‘‘Enhancing security issues and blockchain solutions for IoT and IIoT,’’ J. Netw.
middleware-based IoT applications through run-time pluggable QoS Comput.Appl.,vol.149,Jan.2020,Art.no.102481.
management mechanisms. Application to a oneM2M compliant IoT [199] J.Xie,H.Tang,T.Huang,F.R.Yu,R.Xie,J.Liu,andY.Liu,‘‘Asurvey
ofblockchaintechnologyappliedtosmartcities:Researchissuesand
middleware,’’Proc.Comput.Sci.,vol.130,pp.619–627,Jan.2018.
challenges,’’IEEECommun.SurveysTuts.,vol.21,no.3,pp.2794–2830,
[176] J.L.Romero-GázquezandM.V.Bueno-Delgado,‘‘Softwarearchitecture
| solutionbasedonSDNforanindustrialIoTscenario,’’WirelessCommun. |     |     |     |     |     |     | 3rdQuart.,2019. |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
MobileComput.,vol.2018,pp.1–12,Sep.2018. [200] B. Tang, H. Kang, J. Fan, Q. Li, and R. Sandhu, ‘‘IoT passport:
[177] F.I.KhanandS.Hameed,‘‘Softwaredefinedsecurityserviceprovision- A blockchain-based trust framework for collaborative Internet-of-
ingframeworkforInternetofThings,’’2017,arXiv:1711.11133. Things,’’ in Proc. 24th ACM Symp. Access Control Models Technol.,
May2019,pp.83–92.
[178] A.Bianco,R.Birke,L.Giraudo,andM.Palacin,‘‘OpenFlowswitching:
Dataplaneperformance,’’inProc.IEEEInt.Conf.Commun.,May2010, [201] S.Tuli,R.Mahmud,S.Tuli,andR.Buyya,‘‘FogBus:Ablockchain-
pp.1–5. basedlightweightframeworkforedgeandfogcomputing,’’J.Syst.Softw.,
[179] A.Shalimov,D.Zuikov,D.Zimarina,V.Pashkov,andR.Smeliansky, vol.154,pp.22–36,Aug.2019.
‘‘AdvancedstudyofSDN/OpenFlowcontrollers,’’inProc.9thCentral [202] M. Boussard, S. Papillon, P. Peloso, M. Signorini, and E. Waisbard,
EasternEur.Softw.Eng.Conf.Russia(CEE-SECR),2013,pp.1–6. ‘‘STewARD:SDNandblockchain-basedtrustevaluationforautomated
[180] R.Durner,A.Blenk,andW.Kellerer,‘‘Performancestudyofdynamic risk management on IoT devices,’’ in Proc. IEEE INFOCOM Conf.
QoSmanagementforOpenFlow-enabledSDNswitches,’’inProc.IEEE Comput. Commun. Workshops (INFOCOM WKSHPS), Apr. 2019,
| 23rdInt.Symp.QualityService(IWQoS),Jun.2015,pp.177–182. |     |     |     |     |     |     | pp.841–846. |     |     |     |     |       |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ----- |
| VOLUME10,2022                                           |     |     |     |     |     |     |             |     |     |     |     | 70899 |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
[203] M.PourvahabandG.Ekbatanifard,‘‘Anefficientforensicsarchitecture [224] M. A. Abid, N. Afaqui, M. A. Khan, M. W. Akhtar, A. W. Malik,
insoftware-definednetworking-IoTusingblockchaintechnology,’’IEEE A.Munir, J. Ahmad, and B. Shabir, ‘‘Evolution towards smart and
Access,vol.7,pp.99573–99588,2019. software-defined Internet of Things,’’ AI, vol. 3, no. 1, pp.100–123,
| [204] A. | Yazdinejad, | R. M. | Parizi, | A. Dehghantanha, |     | Q. Zhang, and | Feb.2022. |     |     |     |     |     |     |
| -------- | ----------- | ----- | ------- | ---------------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
K.-K.-R.Choo, ‘‘An energy-efficient SDN controller architecture for [225] H.Li,K.Ota,andM.Dong,‘‘LearningIoTinedge:Deeplearningfor
IEEE Trans. Services theInternetofThingswithedgecomputing,’’IEEENetw.,vol.32,no.1,
| IoT | networks | with blockchain-based |     | security,’’ |     |     |     |     |     |     |     |     |     |
| --- | -------- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Comput.,vol.13,no.4,pp.625–638,Jul.2020. pp.96–101,Jan./Feb.2018.
[205] P.K.Sharma,M.-Y.Chen,andJ.H.Park,‘‘Asoftwaredefinedfognode [226] R.Sahay,W.Meng,D.A.S.Estay,C.D.Jensen,andM.B.Barfod,
baseddistributedblockchaincloudarchitectureforIoT,’’IEEEAccess, ‘‘CyberShip-IoT: A dynamic and adaptive SDN-based security policy
vol.6,pp.115–124,2016. enforcementframeworkforships,’’FutureGener.Comput.Syst.,vol.100,
pp.736–750,Nov.2019.
| [206] A.      | Rahman, | M. J. Islam, | Z.        | Rahman, | M. M. Reza, | A. Anwar,      |                  |       |         |        |                     |     |             |
| ------------- | ------- | ------------ | --------- | ------- | ----------- | -------------- | ---------------- | ----- | ------- | ------ | ------------------- | --- | ----------- |
|               |         |              |           |         |             |                | [227] S. Nastic, | H.-L. | Truong, | and S. | Dustdar, ‘‘SDG-pro: | A   | programming |
| M.A.P.Mahmud, |         | M.           | K. Nasir, | and R.  | M. Noor,    | ‘‘DistB-condo: |                  |       |         |        |                     |     |             |
Distributedblockchain-basedIoT-SDNmodelforsmartcondominium,’’ frameworkforsoftware-definedIoTcloudgateways,’’J.InternetServices
IEEEAccess,vol.8,pp.209594–209609,2020. Appl.,vol.6,no.1,pp.1–17,Aug.2015.
[207] B.LokeshandN.Rajagopalan,‘‘Ablockchain-basedsecuritymodelfor [228] B.Yi,X.Wang,S.K.Das,K.Li,andM.Huang,‘‘Acomprehensive
|     |     |     |     |     |     |     | survey | of network | function | virtualization,’’ | Comput. | Netw., | vol. 133, |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | ----------------- | ------- | ------ | --------- |
SDNs,’’inProc.IEEEInt.Conf.Electron.,Comput.Commun.Technol.
pp.212–262,Mar.2018.
(CONECCT),Jul.2020,pp.1–6.
[229] M.Abbasi,S.Maleki,G.Jeon,M.R.Khosravi,andH.Abdoli,‘‘An
| [208] Q. Shafi | and | A. Basit, | ‘‘DDoS | botnet | prevention using | blockchain |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------ | ------ | ---------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
in software defined Internet of Things,’’ in Proc. 16th Int. intelligent method for reducing the overhead of analysing big data
flowsinopenflowswitch,’’IETCommun.,vol.16,no.5,pp.548–559,
| Bhurban | Conf. | Appl. | Sci. | Technol. | (IBCAST), | Jan. 2019, |     |     |     |     |     |     |     |
| ------- | ----- | ----- | ---- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Mar.2022.
pp.624–628.
|                  |     |           |                      |     |           |                | [230] E. Mohamed, |     | ‘‘The relation | of  | artificial intelligence | with | Internet of |
| ---------------- | --- | --------- | -------------------- | --- | --------- | -------------- | ----------------- | --- | -------------- | --- | ----------------------- | ---- | ----------- |
| [209] K. Bhushan |     | and B. B. | Gupta, ‘‘Distributed |     | denial of | service (DDoS) |                   |     |                |     |                         |      |             |
Things:Asurvey,’’J.Cybersecur.Inf.Manage.,vol.1,no.1,pp.24–30,
| attack                                                          | mitigation | in  | software | defined network | (SDN)-based | cloud |       |     |     |     |     |     |     |
| --------------------------------------------------------------- | ---------- | --- | -------- | --------------- | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
| computingenvironment,’’J.AmbientIntell.HumanizedComput.,vol.10, |            |     |          |                 |             |       | 2020. |     |     |     |     |     |     |
no.5,pp.1985–1997,May2019.
[210] M.P.SinghandA.Bhandari,‘‘New-flowbasedDDoSattacksinSDN:
| Taxonomy, | rationales, |     | and research | challenges,’’ | Comput. | Commun., |     |     |         |     |                                |     |     |
| --------- | ----------- | --- | ------------ | ------------- | ------- | -------- | --- | --- | ------- | --- | ------------------------------ | --- | --- |
|           |             |     |              |               |         |          |     |     | SHAHBAZ |     | SIDDIQUI receivedtheM.S.degree |     |     |
vol.154,pp.509–527,Mar.2020.
intelecommunicationfromHamdardUniversity,
[211] S.NadarajahandJ.Chu,‘‘Ontheinefficiencyofbitcoin,’’Econ.Lett., Karachi, Pakistan. He is currently pursuing the
vol.150,pp.6–9,Jan.2017.
|     |     |     |     |     |     |     |     |     | Ph.D. | degree | in computer | sciences | with the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | -------- | -------- |
[212] W.G.Ethereum,‘‘Asecuredecentralisedgeneralisedtransactionledger,’’
|     |     |     |     |     |     |     |     |     | National | University | of Computer | and | Emerging |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | --- | -------- |
EthereumProjectYellowPaper,vol.151,pp.1–32,Apr.2014.
Sciences,Karachi.HealsoworksasanAssistant
| [213] Z. Zheng, | S.  | Xie, H. | Dai, X. | Chen, and | H. Wang, | ‘‘An overview |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------- | --------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
ProfessorattheDepartmentofComputerScience,
ofblockchaintechnology:Architecture,consensus,andfuturetrends,’’
|             |      |             |     |               |          |            |     |     | National                                     | University | of Computer | and | Emerging |
| ----------- | ---- | ----------- | --- | ------------- | -------- | ---------- | --- | --- | -------------------------------------------- | ---------- | ----------- | --- | -------- |
| in Proc.    | IEEE | Int. Congr. | Big | Data (BigData | Congr.), | Jun. 2017, |     |     |                                              |            |             |     |          |
| pp.557–564. |      |             |     |               |          |            |     |     | Sciences,Karachi.Hisresearchinterestsinclude |            |             |     |          |
[214] S.Dustdar,S.Nastić,andO.Šćekić,SmartCities—TheInternetofThings, theInternetofThings,SDN,andblockchain.
PeopleandSystems.Cham,Switzerland:Springer,2017.
| [215] R. M.  | A. Ujjan, | Z. Pervez, | K.        | Dahal, A. | K. Bashir,       | R. Mumtaz, and |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | --------- | --------- | ---------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| J. González, |           | ‘‘Towards  | sFlow and | adaptive  | polling sampling | for deep       |     |     |     |     |     |     |     |
learningbasedDDoSdetectioninSDN,’’FutureGener.Comput.Syst., SUFIAN HAMEED received the Ph.D. degree
vol.111,pp.763–779,Oct.2020.
|                |     |           |               |         |                |            |     |     | in networks |     | and information     | security | from the     |
| -------------- | --- | --------- | ------------- | ------- | -------------- | ---------- | --- | --- | ----------- | --- | ------------------- | -------- | ------------ |
| [216] J. Singh | and | S. Behal, | ‘‘Detection   |         | and mitigation | of DDoS    |     |     |             |     |                     |          |              |
|                |     |           |               |         |                |            |     |     | University  | of  | Göttingen, Germany. |          | He currently |
| attacks        | in  | SDN: A    | comprehensive | review, | research       | challenges |     |     |             |     |                     |          |              |
worksasanAssistantProfessorattheDepartment
and future directions,’’ Comput. Sci. Rev., vol. 37, Aug. 2020, ofComputerScience,NationalUniversityofCom-
| Art.no.100279. |     |     |     |     |     |     |     |     | puterandEmergingSciences(NUCES),Pakistan. |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
[217] T.Ninikrishna,S.Sarkar,R.Tengshe,M.K.Jha,L.Sharma,V.K.Daliya, HealsoleadstheITSecurityLabs,NUCES.The
andS.K.Routray,‘‘SoftwaredefinedIoT:Issuesandchallenges,’’in
|       |            |         |             |         |          |            |     |     | research | laboratory | studies       | and teaches | security |
| ----- | ---------- | ------- | ----------- | ------- | -------- | ---------- | --- | --- | -------- | ---------- | ------------- | ----------- | -------- |
| Proc. | Int. Conf. | Comput. | Methodolog. | Commun. | (ICCMC), | Jul. 2017, |     |     |          |            |               |             |          |
|       |            |         |             |         |          |            |     |     | problems | and        | solutions for | different   | types of |
pp.723–726.
|                  |     |           |          |                 |     |              |     |     | information |     | and communication | paradigms. | His |
| ---------------- | --- | --------- | -------- | --------------- | --- | ------------ | --- | --- | ----------- | --- | ----------------- | ---------- | --- |
| [218] E. Torres, | R.  | Reale, L. | Sampaio, | and J. Martins, | ‘‘A | SDN/OpenFlow |     |     |             |     |                   |            |     |
researchinterestsincludenetworksecurity,websecurity,mobilesecurity,
| framework | for | dynamic | resource | allocation | based on | bandwidth allo- |     |     |     |     |     |     |     |
| --------- | --- | ------- | -------- | ---------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
cationmodel,’’IEEELatinAmer.Trans.,vol.18,no.5,pp.853–860, andsecurearchitecturesandprotocolsforcloudandtheIoT.
May2020.
[219] J.Pan,J.Wang,A.Hester,I.Alqerm,Y.Liu,andY.Zhao,‘‘EdgeChain:
Anedge-IoTframeworkandprototypebasedonblockchainandsmart
contracts,’’ IEEE Internet Things J., vol. 6, no. 3, pp.4719–4732, SYEDATTIQUESHAH(Member,IEEE)received
| Jun.2019. |     |     |     |     |     |     |     |     | thePh.D.degreefromtheInstituteofInformatics, |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
[220] S.Hameed,S.A.Shah,Q.S.Saeed,S.Siddiqui,I.Ali,A.Vedeshin,
|     |     |     |     |     |     |     |     |     | Istanbul | Technical | University, | Istanbul, | Turkey. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----------- | --------- | ------- |
andD.Draheim,‘‘AscalablekeyandtrustmanagementsolutionforIoT
DuringhisPh.D.,hestudiedasaVisitingScholar
sensorsusingSDNandblockchaintechnology,’’IEEESensorsJ.,vol.21, at The University of Tokyo, Japan; the National
no.6,pp.8716–8733,Jan.2021. Chiao Tung University, Taiwan; and the Tallinn
[221] I.H.AbdulqadderandS.Zhou,‘‘SliceBlock:Context-awareauthenti- UniversityofTechnology,Estonia;wherehecom-
cation handover and secure network slicing using DAG-blockchain in pletedthemajorcontentofhisthesis.Heworked
edge-assistedSDN/NFV-6Genvironment,’’IEEEInternetThingsJ.,doi:
asanAssociateProfessorandtheChairpersonat
10.1109/JIOT.2022.3161838.
theDepartmentofComputerScience,BUITEMS,
| [222] T. P. | da Silva, | T. Batista, | F.  | Lopes, A. | R. Neto, | F. C. Delicato, |     |     |     |     |     |     |     |
| ----------- | --------- | ----------- | --- | --------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Quetta,Pakistan.HewasalsoengagedasaLecturerattheDataSystems
P.F.Pires,andA.R.daRocha,‘‘Fogcomputingplatformsforsmartcity
Group,InstituteofComputerScience,UniversityofTartu,Estonia.Heis
applications—Asurvey,’’ACMTrans.InternetTechnol.,tobepublished.
currentlyworkingasaLecturerinsmartcomputersystemsattheSchoolof
| [223] A. | Gaurav, | B. B. Gupta, | and | P. K. Panigrahi, | ‘‘A | comprehensive |     |     |     |     |     |     |     |
| -------- | ------- | ------------ | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
surveyonmachinelearningapproachesformalwaredetectioninIoT- ComputingandDigitalTechnology,BirminghamCityUniversity,U.K.His
basedenterpriseinformationsystem,’’EnterpriseInf.Syst.,2022,doi: researchinterestsincludebigdataanalytics,theInternetofThings,network
10.1080/17517575.2021.2023764. security,andinformationmanagement.
| 70900 |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Siddiquietal.:TowardSDN-BasedIoTFrameworks:ASLR,Taxonomy,OpenChallengesandProspects
IJAZ AHMAD (Member, IEEE) received the DIRK DRAHEIM (Member, IEEE) received the
M.Sc. and Ph.D. degrees in wireless communi- Ph.D. degree from Freie Universität Berlin and
cations from the University of Oulu, Finland, the Habilitation degree from the Universität
in 2012 and 2018, respectively. He has been a Mannheim,Germany.From2006to2008,hewas
Visiting Scientist at Aalto University, Finland, an Area Manager for database systems at the
in2018,andattheTUVienna,Austria,in2019. SoftwareCompetenceCenterHagenberg,Austria.
HeiscurrentlywiththeVTTTechnicalResearch From2008to2016,hewastheHeadoftheData
Centre, Finland. His research interests include Center, University of Innsbruck and, in parallel,
security in 5G and 6G, SDN and its security, anAdjunctReaderattheFacultyofInformation
andtheapplicationsofmachinelearninginfuture Systems,UniversityofMannheim.Heiscurrently
networks.Hehasreceivedseveralawardsforhisresearchwork,including a Full Professor of information systems at the Tallinn University of
theNokiaFoundation,TaunoTönning,theJormaOllilaGrantAwards,and Technology(Taltech),Estonia,andheadingtheTaltechInformationSystems
twoIEEEbestpaperawards. Group.TheTaltechInformationSystemsGroupconductsresearchinlarge-
and ultra-large-scale IT systems, in particular, next generation of digital
government technologies and digital government ecosystems. He is the
coauthoroftheSpringerBookForm-OrientedAnalysisandauthorofthe
SpringerbooksBusinessProcessTechnology,SemanticsoftheProbabilistic
TypedLambdaCalculus,andGeneralizedJeffreyConditionalization.Heis
alsoaninitiatorandaleaderofnumerousdigitaltransformationinitiatives.
SCHAHRAM DUSTDAR (Fellow,IEEE)iscur-
rently a Full Professor of computer science
heading the Research Division of Distributed
Systems,TUWien,Austria.Heholdsseveralhon-
orary positions: University of California (USC)
ADEL ANEIBA (Member, IEEE) received the at Los Angeles; Monash University, Melbourne;
Ph.D.degreeinthefieldofmobilecomputingand ShanghaiUniversity;MacquarieUniversity,Syd-
distributedsystemsfromStaffordshireUniversity, ney;UniversityPompeuFabra,Barcelona,Spain.
in2008.HeworkedasaSeniorICTConsultant From December 2016 to January 2017, he was
for international organizations, for ten years, aVisitingProfessorattheUniversityofSevilla,
including UNESCO and several governmental Spain,andfromJanuarytoJune2017,hewasaVisitingProfessoratUC
organizationsformanyyears,andhasparticipated Berkeley,USA.HehasanH-indexof78withsome36,000citations.Heis
in managing mega ICT projects mainly on data anElectedMemberoftheAcademiaEuropaea:TheAcademyofEurope,
center designing and development, and reengi- whereheistheChairpersonoftheInformaticsSection.HeisanAsia-Pacific
neering business processes. He is currently an ArtificialIntelligenceAssociation(AAIA)Fellow(2021).Hewasarecipient
AssociateProfessorofcomputernetworksandtheInternetofThings(IoT) ofmultipleawards,IEEETCSVCOutstandingLeadershipAward(2018),
with Birmingham City University. He is the Research Lead for Cyber- IEEE TCSC Award for Excellence in Scalable Computing (2019), ACM
physicalSystems(CPS)ResearchGroup.HeissupervisingseveralPh.D. Distinguished Scientist (2009), ACM Distinguished Speaker (2021), and
students on various research topics, such as the IoT, SDN, resources IBMFacultyAward(2012).HeistheFoundingCo-Editor-in-ChiefofACM
allocations,andoptimizationin5Gandblockchainapplicationsinthesmart TransactionsonInternetofThings(ACMTIoT)aswellastheEditor-in-
cities domain. His current research interests include the IoT, computer Chief of Computing (Springer). He is an Associate Editor of the IEEE
networks, evaluation, and optimization, and blockchain. He is a member TRANSACTIONSON SERVICES COMPUTING, the IEEE TRANSACTIONSON CLOUD
of the Association for Computing Machinery (ACM) and the Institute of COMPUTING,ACMComputingSurveys,ACMTransactionsontheWeb,and
EngineeringandTechnology(IET).HeisafellowoftheHigherEducation ACMTransactionsonInternetTechnology,aswellasontheEditorialBoard
Academy(HEA)andamemberofmanytechnicalcommitteesforscientific ofIEEEINTERNETCOMPUTINGandIEEECOMPUTER.
academicconferencesandjournals.
VOLUME10,2022 70901