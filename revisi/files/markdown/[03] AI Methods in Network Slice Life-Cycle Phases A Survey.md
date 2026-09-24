# [03] AI Methods in Network Slice Life-Cycle Phases A Survey

> Source file: `[03] AI Methods in Network Slice Life-Cycle Phases A Survey.pdf`

---

Review
AI Methods in Network Slice Life-Cycle Phases: A Survey
EvangelosThomatos1 ,AggelikiSgora1,∗ ,AthanasiosTsipis1 andPeriklisChatzimisios2,3
1 DepartmentofDigitalMediaandCommunication,IonianUniversity,28100Argostoli,Greece;
atsipis@ionio.gr(A.T.)
2 DepartmentofInformationandElectronicEngineering,InternationalHellenicUniversity,
57400Thessaloniki,Greece
3 DepartmentofElectricalandComputerEngineering,UniversityofNewMexico,
Albuquerque,NM87131-0001,USA
* Correspondence:asgora@ionio.gr
Abstract
Networkslicing(NS)playsavitalroleinenablingflexibleandefficientresourceallocation,
tailoredtodiverseusecasesandnetworkdomains. Thissurveypaperexploresthesynergy
between NS and Artificial Intelligence (AI), emphasizing how Machine Learning (ML)
techniques can address challenges across the slice life-cycle. A key contribution of this
workisanin-depthanalysisofAIandprimarilyMLapplicationsineachphaseoftheslice
life-cycle,delvingintotheirspecifictasksanddiscussingthetechniquesappliedtothese
tasks. Furthermore,wepresentataxonomybasedondifferentslicingcriteria,offeringa
structuredperspectivetoenhanceunderstandingandimplementation.
Keywords: 5G; B5G; 6G; artificial intelligence; network slicing; machine learning; slice
life-cycle
1. Introduction
The 5G and Beyond 5G (B5G) networks are designed to serve different types of
users,i.e.,verticals,withaplethoraofdifferentservices,achievinghigherperformancein
termsoflatency,throughput,andreliability,fosteringthedigitaltransformationofvertical
AcademicEditors: LeiMoand
GuiyunLiu industries[1].TheInternationalTelecommunicationUnion(ITU)categorized5Gservices[2]
into(a)EnhancedMobileBroadband(eMBB),forcapacityenhancement,(b)Ultra-Reliable
Received:9September2025
Revised:7October2025 andLow-LatencyCommunications(URLLCs),forprovidingrobustconnectivitywithvery
Accepted:10October2025 lowlatency,and(c)MassiveMachineTypeCommunications(mMTCs),tosupportlow-rate
Published:15October2025 burst-ratecommunicationamongahugenumberofdevices.
Citation: Thomatos,E.;Sgora,A.; The diverse nature and different performance requirements of these services have
Tsipis,A.;Chatzimisios,P.AI drivenbothresearchersandindustryprofessionalstoseekatechnologycapableofenabling
MethodsinNetworkSliceLife-Cycle
aunifiednetworkinfrastructure,capableofmeetingthesevariedrequirementseffectively.
Phases:ASurvey.Electronics2025,14,
NetworkSlicing(NS)hasemergedasasolutiontothischallenge,widelyrecognizedby
4053. https://doi.org/10.3390/
academiaandindustryasakeyenablerforthedeliveryofcustomizedandon-demand
electronics14204053
networkservices[3]. NetworkFunctionVirtualization(NFV)andSoftware-DefinedNet-
Copyright:©2025bytheauthors.
working (SDN) are the main technologies that NS exploits to create end-to-end logical
LicenseeMDPI,Basel,Switzerland.
network-orientedon-demandservices,callednetworkslices,capableofsupportingthedif-
Thisarticleisanopenaccessarticle
distributedunderthetermsand ferentdemandsofeachtypeofservice. Eachslicespansoverallnetworkdomains,i.e.,the
conditionsoftheCreativeCommons RadioAccessNetwork(RAN),theTransportNetwork(TN),andtheCoreNetwork(CN),
Attribution(CCBY)license andiscreatedtoprovideaspecificservice,whichhasdifferentperformancerequirements
(https://creativecommons.org/
thantheservicesprovidedbyotherslices.
licenses/by/4.0/).
Electronics2025,14,4053 https://doi.org/10.3390/electronics14204053

Electronics2025,14,4053 2of38
Eachnetworksliceprogressesthroughmultiplephases, fromitsinitialrequestfor
creation to its eventual decommissioning when it is no longer required. These phases
compose the slice life-cycle and have been defined by the 3rd Generation Partnership
Project(3GPP)[4].
TheapplicationofNSinvolvestaskssuchasthenetworkslicedesign,construction,
deployment,operation,control,andmanagement. Thesetasksrequirereal-timeanalysisof
alargevolumeofcomplexdata,alongwithdynamicdecisionmaking,toensurethatthe
deployednetworksliceeffectivelymeetsthetargetedQualityofService(QoS)requirements.
Giventhevolumeofdatatobeprocessedandthetimeconstraints,tasksrelatedtoslice
creationandoperationarenotalwaysfeasibletoperformmanually,andhencemustbe
automated[5].
In order to address the challenges arising from the application of NS, Artificial In-
telligence(AI)andespeciallyMachineLearning(ML)havebeenwidelyproposedaskey
enablerstomakeitsimplementationmorefeasibleandefficient. Theuseofsuchtechniques
canautomatemanytasksrelatedtothecreation,deployment,andoperationofnetwork
slices,aswellasenabletheoptimizedreal-timereconfigurationofparameters. Buildingon
suchresearchefforts,theadoptionofAI/MLmethodsforNShasalsobeenstandardizedby
leadingglobalStandardsDevelopmentOrganizations(SDOs),whichhavedefinedspecific
usecasesforthesemethodsandtherequirementstheymustmeetinthiscontext[5].
Intheliterature,therearemanyresearchworksproposingAI,andmainlyMLmethods,
thatdealwithdifferentproblemsarisingfromtheapplicationofNSin5GandB5Gnetworks.
Thoseproblemsarerelatedtodifferenttasksthatneedtobeperformedineachphaseof
theslicelife-cycle. Thus,theproposedapplicationsofAIandMLareassociatedwithslice
life-cyclephases.
Theprimarymotivationforthisworkistofillthegapintheliteraturebyproviding
acomprehensivesurveyontheapplicationofMLmethodstovarioustasksacrosseach
phaseofthenetworkslicelife-cycle,asoutlinedinref.[4]. Ourgoalistosummarizethe
tasksassociatedwitheachphaseandthecorrespondingMLmethodsproposedtoaddress
the challenges related to these tasks. Additionally, we aim to contribute to the broader
discourseonintelligentnetworks,andofferreadersavaluableresourcethatcoversthe
fundamentalconceptsofbothNSandML.
Themaincontributionsofthisworkcanbesummarizedasfollows:
• Wepresentthestate-of-the-artrelatedsurveysfocusingontheapplicationofMLto
NS,anddiscusstheirrespectivecontributions.
• WeprovideinsightsaboutthebasicfunctionalitiesofNS,aswellasexistingarchi-
tecturalapproaches, andslicingtypes. Moreover, wepresentthemaintechnology
enablersofNSandthedifferentphasesthatcomposetheslicelife-cycle.
• WeintroducethefoundationalconceptsofMLtechniquesandtheirrespectivecategories.
• WepresentthefindingsofourextensiveliteraturereviewontheapplicationsofML
methodstoNS.Specifically,foreachphaseofthelife-cycleandeachtaskassociated
withaphase,weoutlinetheMLapplicationsproposedintheliterature,thechallenges
theyaddress,andthemethodsemployed.
• Whenever feasible, we also associate each proposed application with the different
typesofslicing,consideringtheresourceallocationapproach,usecaseapplication,
andnetworkdomaininwhichNSisapplied.
Theremainderofthissurveyisorganizedasfollows:Section2presentsthestate-of-the-
artrelatedsurveysandtheircontributions. Section3introducesthebasicsofNS,including
thedifferentarchitectures,slicingtypes,thetechnologyenablersofNS,thephasesofthe
slicelife-cycle,andhowAI/MLempowersNS.Section4provideskeyinformationabout
ML,includingdifferenttrainingapproachesandtheresultingMLcategories. Section5

Electronics2025,14,4053 3of38
highlightsthemaincontributionsofthissurvey,focusingonMLapplicationsproposed
toaddresschallengesarisingfromthedeploymentofNSforeachslicelife-cyclephase.
Section6discussesissuesrelatedtospecificMLmethodsidentifiedduringthissurvey,and
finally,Section7concludesourwork. ThestructureofoursurveyisillustratedinFigure1.
Figure1.Structureofthesurvey.
2. RelatedSurveys
Sincetheappearanceoftheterm“networkslicing”,severalsurveysandreviewshave
been published, exploring various aspects of this term. Initially, researchers primarily
focusedonthefundamentalprinciplesofNS,itsarchitectures,andthedynamicsassociated
withtheiropenchallenges.
Moreprecisely,Foukasetal.[6]presentedthe5Garchitectureanditschallenges. Afo-
labietal.[7]focusedontheNSprincipalconcepts,itsenabledtechnologiesandsolutions,as
wellasthecurrentstandardizationefforts. Kaloxylos[8]summarizedexistingNSsolutions,
whileZhang[3]outlinedslicingapproaches,keytechnologies,andopenissues. Chahbar
etal.[9]presentedend-to-end5GNSmodels. Moreover,themajorityofpapersreviewed
5GNSarchitecturesprimarilyleveragingSDNandNFV.Theauthorsinref.[10]focused
ontheEuropeanTelecommunicationsStandardsInstitute(ETSI)andOpenNetworking
Foundation(ONF)architecturesandtheirSDNandNFVcapabilities,whileBarakabitze
etal.[11]highlighted5GNSusingSDNandNFVsolutions.
SeveralothersurveysfocusonthemathematicalmodelsthatcanbeappliedtoNS.
Debbabietal.[12]investigatedtheNSarchitecturesfromtheiralgorithmicperspective. Su
etal.[13]categorizedthemathematicalmodelsofresourceallocationofNSintogeneral,
economic, game, prediction, androbustness, andfailurerecoverymodels. Theauthors
alsomentionedthatpredictionmodelscanuseMLalgorithms. However,theirdiscussion
ofthistopicislimited. Wijethilakaetal.[14]focusedontheroleofNSfortheInternetof
Things(IoT)realizationin5Gnetworks. Theauthorsalsohighlightedtheneedtointegrate
MLalgorithmswithNStoachieveautomatedfunctionalities;however,theirdiscussionof
thistopicwaslimited.

Electronics2025,14,4053
4of38
From the beginning of 2020, several surveys have investigated the use of AI/ML
algorithms in NS. Shen et al. [15] surveyed AI-assisted RAN slicing and its challenges.
SpecialattentionwasgiventotheimplementationofNSintheIoTenvironment. Khan
etal.[16]highlightedrecentadvances,providedataxonomy,anddiscussedtherequire-
mentsandchallengesinNSforIoTapplications. Theauthorsalsosuggestedtheuseof
federatinglearning(FL)forfutureNS;however,nofurtherdetailsweregiven.Wuetal.[17]
focusedontheapplicationofNSinsmartapplications,mainlyforsmarttransportation,
smart energy, and smart factory applications. The authors also mentioned the benefits
ofintelligentNS.Nevertheless,theydidnotdelveintotheAI/ML-basedNS.Ssengonzi
etal.[18]emphasizedtheapplicationofDeepReinforcementLearning(DRL)forNSin5G
andbeyondnetworks. Dangietal.[19]highlightedsecurityaspectsregardingML-based
NS in 5G networks during the network slice life-cycle. Donatti et al. [20] surveyed the
differentMLtechniquesthatcanbeappliedinthedifferentphasesoftheslicelife-cycle.
Still, the authors focused only on the specific tasks of the phases of the slice life-cycle.
Phyuetal.[21]alsotalkedabouttheapplicationofMLapproachesforthespecifictasks
ofNS,i.e.,trafficforecasting,admissioncontrol,andresourceallocation. Azimietal.[22]
surveyedworksthatemployedMLtechniquesforresourcemanagementinRANslicing.
Hamdi et al. [23] focused on ML techniques and NS for the Internet of Vehicles (IoV).
Ebrahimietal.[24]studiedNSresourcemanagementincross-domainandEnd-to-End
(E2E)contexts,whileNovananaetal.[25]focusedonE2E5Gslicinganddiversitystrategies
toincreasethenetworkperformance.Finally,Sunetal.[26]reviewedthecurrentandfuture
roleofExplainableAI(XAI)in6Gcommunications,focusingonitsapplicationinnetwork
slicing. TheirworkcategorizesXAImethodsandhighlightstheirimpactontransparency
andreliabilityincriticalscenarios,likevehicularnetworks.
Table1summarizestheaforementionedworksbyyearofpublicationinascending
order. In this survey, we alsofocus on the application of the AL/ML techniquesin the
differentphasesoftheslicelife-cycle. However,wegoonestepfurther,delvingdeeper
intothespecifictasksofeachphaseofthelife-cyclebypresentinganddiscussingtheML
techniquesappliedinthesetasks,asoutlinedin[4],andproposingataxonomybasedon
differentslicingcriteria.
Table1.Summaryofrelatedsurveys.
| Year Ref. | Title |     | Objectives/Contributions |                     | TopicsCovered |
| --------- | ----- | --- | ------------------------ | ------------------- | ------------- |
|           |       |     | Provide                  | a holistic overview | of            |
Network Slicing in 5G: Survey 5GNSarchitecture,functionallayers,enablingtech-
| 2017 [6] |               |     | 5Gnetworkslicingarchitectures |     |                              |
| -------- | ------------- | --- | ----------------------------- | --- | ---------------------------- |
|          | andChallenges |     |                               |     | nologies,openresearchissues. |
andidentifykeychallenges.
|           |          |                     | Analyze | ETSI and ONF | frame-                                          |
| --------- | -------- | ------------------- | ------- | ------------ | ----------------------------------------------- |
|           | Network  | slicing for 5G with |         |              |                                                 |
|           |          |                     | works,  | focusing on  | their ETSINFVandONFSDNarchitectures,integration |
| 2017 [10] | SDN/NFV: | Concepts, architec- |         |              |                                                 |
|           |          |                     | SDN/NFV | capabilities | for paradigms,usecases.                         |
tures,andchallenges
enablingslicing.
|     | Network | Slicing and Soft- |           |                |     |
| --- | ------- | ----------------- | --------- | -------------- | --- |
|     |         |                   | Summarize | NS principles, | re- |
warization: A Survey on Prin- Usecasesandrequirements, enablingtechnologies,
| 2018 [7] |     |     | viewenablingtechnologies,and |     |     |
| -------- | --- | --- | ---------------------------- | --- | --- |
ciples, Enabling Technologies, RAN/coreslicingsolutions,openchallenges.
discusspracticalsolutions.
andSolutions
|     |     |     | Assess | proposed solutions |     |
| --- | --- | --- | ------ | ------------------ | --- |
Asurveyandananalysisofnet-
2018 [8] for 5G NS and analyze Access,transport,andcoredomainslicing.
workslicingin5Gnetworks
architecturalperspectives.
Anoverviewofnetworkslicing Summarize slicing approaches Slicingmethods,standardizationactivities,enabling
2019 [3]
for5G andkeyenablingtechnologies. technologies,securityconsiderations.
|     | ResourceAllocationforNetwork |     | Review | principles and | math- |
| --- | ---------------------------- | --- | ------ | -------------- | ----- |
Slicingin5GTelecommunication SDN/NFVconcepts,NSarchitecture,resourcealloca-
| 2019 [13] |           |                     | ematical | models for | NS                     |
| --------- | --------- | ------------------- | -------- | ---------- | ---------------------- |
|           | Networks: | A Survey of Princi- |          |            | tionmodels,challenges. |
resourceallocation.
plesandModels

Electronics2025,14,4053
5of38
Table1.Cont.
| Year Ref | Title            |        | Objectives/Contributions     |     |     | TopicsCovered |     |     |
| -------- | ---------------- | ------ | ---------------------------- | --- | --- | ------------- | --- | --- |
|          | Network slicing: | Recent | ad- ExamineadvancesofNSinIoT |     |     |               |     |     |
IoTapplicationscenarios,taxonomyparameters,re-
| 2020 [16] | vances,taxonomy,requirements, |     | and propose | a taxonomy |     | of  |     |     |
| --------- | ----------------------------- | --- | ----------- | ---------- | --- | --- | --- | --- |
quirements,challenges.
|     | andopenresearchchallenges |         | NSresearch.                |     |     |                                               |     |     |
| --- | ------------------------- | ------- | -------------------------- | --- | --- | --------------------------------------------- | --- | --- |
|     | 5G network                | slicing | using                      |     |     |                                               |     |     |
|     |                           |         | PresentsolutionsforNSbased |     |     | ComparisonofSDN/NFVarchitectures,standardiza- |     |     |
|     | SDN and                   | NFV: A  | survey of                  |     |     |                                               |     |     |
2020 [11] on SDN/NFV and provide tionactivities,projects,orchestrationinsingle/multi-
|     | taxonomy, | architectures | and        |     |     |                 |     |     |
| --- | --------- | ------------- | ---------- | --- | --- | --------------- | --- | --- |
|     |           |               | ataxonomy. |     |     | domainsettings. |     |     |
futurechallenges
AI-assisted network-slicing Explore AI-assisted meth- NSarchitecture,AI-drivenRANslicing,automated
2020 [15] based next-generation ods for RAN slicing in next- RadioAccessTechnology(RAT)integrationinhetero-
|     | wirelessnetworks |     | generationsystems. |     |     | geneousslicing. |     |     |
| --- | ---------------- | --- | ------------------ | --- | --- | --------------- | --- | --- |
Acomprehensivesurveyonthe Reviewend-to-endslicingmod- ETSI NS architecture, RAN/CN/TN slicing, TN
2020 [9]
|           | E2E5Gnetworkslicingmodel      |         | elsfor5Gnetworks.       |                 |         | datamodels. |                |                        |
| --------- | ----------------------------- | ------- | ----------------------- | --------------- | ------- | ----------- | -------------- | ---------------------- |
|           | Survey on                     | Network | Slicing for Investigate | how             | NS sup- |             |                |                        |
|           |                               |         |                         |                 |         | Role of NS  | in IoT, IoT-NS | use cases, challenges, |
| 2021 [14] | InternetofThingsRealizationin |         | ports                   | IoT realization | and     |             |                |                        |
projects,futuredirections.
|     | 5GNetworks |     | emergingapplications. |     |     |     |     |     |
| --- | ---------- | --- | --------------------- | --- | --- | --- | --- | --- |
AlgorithmicsandModelingAs- Provide an algorithmic per- GenericNSarchitecture,ManagementAndOrchestra-
2022 [12] pectsofNetworkSlicingin5G spective on NS architectures tion(MANO)acrossdomains,taxonomyofalgorith-
andBeyondNetworks:Survey andorchestration. micaspects,openissues.
|     | A survey | of deep | reinforce- |                    |     |     |     |     |
| --- | -------- | ------- | ---------- | ------------------ | --- | --- | --- | --- |
|     |          |         | Analyze    | deep reinforcement |     |     |     |     |
ment learning applications in NSconcepts,orchestration,DRL-basedresourceallo-
| 2022 [18] |     |     | learning | applications | in NS |     |     |     |
| --------- | --- | --- | -------- | ------------ | ----- | --- | --- | --- |
5Gandbeyondnetworkslicing cation,admissioncontrol,trafficprediction.
andvirtualization.
andvirtualization
|           | ML-Based | 5G        | Network                  |     |     |                                            |     |     |
| --------- | -------- | --------- | ------------------------ | --- | --- | ------------------------------------------ | --- | --- |
|           |          |           | ReviewML-basedmethodsfor |     |     | TaxonomyofML-basedNSsecurity,threatmodels, |     |     |
| 2022 [19] | Slicing  | Security: | A                        |     |     |                                            |     |     |
|           |          |           | NSsecurity.              |     |     | prevention,solutions,management.           |     |     |
ComprehensiveSurvey
ASurveyofIntelligentNetwork
Slicing Management for Indus- Survey NS management ap- NS concepts, enabling technologies, orchestration,
| 2022 [17] | trialIoT:IntegratedApproaches |     | proachestailoredforindustrial |     |     |     |     |     |
| --------- | ----------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
standardization,usecases,proof-of-conceptproducts.
|     | forSmartTransportation,Smart |     | IoTapplications. |     |     |     |     |     |
| --- | ---------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |
Energy,andSmartFactory
ApplicationsofMachineLearn-
inginResourceManagementfor ExamineML-basedmethodsfor RANslicingapproaches,MLtechniquesforresource
2022 [22]
RAN-Slicingin5GandBeyond RANresourcemanagement. management,challenges,solutions.
Networks:ASurvey
|           | Survey on               | Machine | Learning-                  |     |     |                  |         |                   |
| --------- | ----------------------- | ------- | -------------------------- | --- | --- | ---------------- | ------- | ----------------- |
|           |                         |         | ReviewMLapplicationsacross |     |     | Slice life-cycle | stages, | ML algorithms for |
| 2023 [20] | EnabledNetworkSlicing:  |         | Cov-                       |     |     |                  |         |                   |
|           | eringtheEntireLifeCycle |         | theNSlifecycle.            |     |     | NSmanagement.    |         |                   |
Machine Learning in Network Provide an overview of ML Concepts,enablingtechnologies,MLalgorithmsfor
2023 [21]
Slicing—ASurvey methodsinNS. forecasting,admissioncontrol,resourceallocation.
NetworkSlicingbasedLearning
|           |                            |     | Survey                  | ML techniques | for IoV- | IoVapplications,benefits/challenges,MLtechniques, |     |     |
| --------- | -------------------------- | --- | ----------------------- | ------------- | -------- | ------------------------------------------------- | --- | --- |
| 2024 [23] | TechniquesforIoVin5GandBe- |     |                         |               |          |                                                   |     |     |
|           |                            |     | orientednetworkslicing. |               |          | datasets,simulators,projects,futuredirections.    |     |     |
yondNetworks
|           | Resource                    | Management | From Address | resource         | manage- |              |          |             |
| --------- | --------------------------- | ---------- | ------------ | ---------------- | ------- | ------------ | -------- | ----------- |
|           |                             |            |              |                  |         | Cross-domain | resource | management, |
| 2024 [24] | Single-Domain5GtoEnd-to-End |            | ment         | in single-domain | and     |              |          |             |
methodologies,functionalities.
|     | 6GNetworkSlicing:ASurvey |     | E2Eslicing. |     |     |     |     |     |
| --- | ------------------------ | --- | ----------- | --- | --- | --- | --- | --- |
Performanceof5GSlicingWith Classify5Gslicingmethodswith Services, access technologies, diversity
| 2024 [25] | AccessTechnologiesandDiver- |     |                      |     |     |                     |     |     |
| --------- | --------------------------- | --- | -------------------- | --- | --- | ------------------- | --- | --- |
|           |                             |     | performanceanalysis. |     |     | aspects,challenges. |     |     |
sity:AReviewandChallenges
|     | Advancing | 6G: Survey | for Ex- Explore | the role | of explain- |     |     |     |
| --- | --------- | ---------- | --------------- | -------- | ----------- | --- | --- | --- |
6G,XAIapplicationsinnetworkslicing,vehicularnet-
| 2025 [26] | plainableAIonCommunications |     | able AI | in 6G communications |     |     |     |     |
| --------- | --------------------------- | --- | ------- | -------------------- | --- | --- | --- | --- |
works,challenges.
|     | andNetworkSlicing |     | andslicing. |     |     |     |     |     |
| --- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- |
3. NetworkSlicingBasics
Theconceptofnetworkslicewasintroducedin2015bytheNextGenerationMobile
Network(NGMN)Alliancetosuccessfullyaccommodatethediverseservicerequirements
of the 5G use cases using a common network infrastructure. According to the 3GPP, a
network slice is defined as “a logical network that provides specific network capabili-
tiesandnetworkcharacteristics,supportingvariousservicepropertiesfornetworkslice

Electronics2025,14,4053 6of38
customers”[4]. Moreover,accordingtoAfolabietal.[7],NSshouldadheretotheseven
followingprinciples:
• Automation: Enableson-demandslicesetupwithoutmanualeffort,specifyingService
LevelAgreements(SLAs)andtimingviasignaling.
• Isolation: Enableson-demandslicesetupwithoutmanualeffort,specifyingSLAsand
timingviasignaling.
• Customization: Tailorsresourcestotenantneedswithprogrammablepoliciesand
value-addedservices.
• Elasticity:AdjustsresourcesdynamicallytomaintainSLAsunderchangingconditions.
• Programmability: OpenApplicationProgrammingInterfaces(APIs)allowthirdpar-
tiestomanagesliceresourcesflexibly.
• End-to-end: Ensuresseamlessservicedeliveryacrossdomainsandtechnologies.
• Hierarchicalabstraction: Allowsrecursiveresourcesharing,enablinglayeredservices.
Thus,thebenefitsofNSarenumerousandcanbesummarizedbelow[15,27]:
• Through virtual networks’ multiplexing, it can support multi-tenancy, leading to
reducedcapitalexpenseinbothnetworkdeploymentandoperation.
• Ithasthecapabilitytoachieveservicedifferentiationandensurethefulfillmentof
SLAsforeachtypeofservice.
• On-demandcreationandadjustmentofslices,alongwiththeirpotentialannulmentas
required,canincreasetheflexibilityandadaptabilityinnetworkmanagement.
3.1. NetworkSlicingArchitectures
SeveralSDOs,suchasthe3GPP,theNGMNalliance,etc.,havefocusedonthedevel-
opmentofNS-orientedarchitectures[14,28]. TheNGMNslicingarchitecture,asdepictedin
Figure2,consistsofthefollowinglayers[14,21]: (1)resource(infrastructure)layer;(2)net-
worksliceinstancelayer;and(3)application(serviceinstance)layer. Theresourcelayer
providesallthevirtualorphysicalresourcestothenetworksliceinstancelayerthatfur-
nishesthenecessarynetworkcharacteristicsforaserviceinstance. Finally,theapplication
layerconsistsofallservices(end-userserviceorbusinessservices). Adetailedoverview
regardingNSarchitecturesofSDOsandrelatedNSprojectscanbefoundinref.[28].
Figure2.TheNGMNarchitecture.

Electronics2025,14,4053 7of38
3.2. TypesofSlicing
NScanbeclassifiedaccordingtodifferentcriteria,assummarizedinTable2. Firstly,
basedontheresourceallocationmethod(sliceelasticity)used,NScanbedistinguished
intothefollowingcategories[23,29]:
• Static Slicing, where each Virtual Network (VN) gets a fixed portion of physical
resourcesforitsentireservicelife.Themainadvantageofthisapproachisitssimplicity,
asnocontinuouscontrolsignalingorcoordinationisrequired. However,sincestatic
slicinglacksflexibilitytoadapttovaryingtrafficloads,itoftenleadingtoinefficient
resource utilization. Moreover, the determination of the optimal fixed allocation
amongslicesisaverychallengingtask.
• DynamicSlicing,whereoperatorsareabletodynamicallydesign,deploy,customize,
and optimize the slices according to the service requirements or conditions in the
network. Thisapproachenhancesflexibility,resourceefficiency,andresponsiveness
sinceitallowsthedynamicdeploymentorexpansionofsliceswheneverisneeded.
Moreover, predictive or adaptive mechanisms can further optimize allocation by
foreseeingdemandvariations. However,dynamicslicingincreasessystemcomplexity
andrequiresaccuratetrafficpredictionandorchestration.
• Semi-StaticorSemi-DynamicSlicing,wherepartoftheresourcesisallocatedstatically
anditcanbeguaranteedwhiletheotherpartisdynamicallyallocated. Thishybrid
model balances between stability and adaptability; however it cannot guarantee
efficientresourceutilizationwhileitrequirespartialdynamiccontrolmechanisms.
In addition, depending on the use case application, NS can be applied as shown
below[14]:
• Vertically, where each slice is customized to meet the specific requirements of dif-
ferent vertical industries or applications. (i.e., automotive, smart grid, healthcare,
etc.) Inthiscontext,verticalindustriescollaboratewiththecorenetworktoaddress
diverseQoSandQoEdemandsacrossdifferentusecases[30]. Thus,thisapproach
ensures strong performance isolation; however it comes at the cost of increased
orchestrationcomplexity.
• Horizontally,inwhichtheresourcesaredistributedevenlyacrossdifferentslicesto
meetthediverseneedsofvarioususersorserviceswithinthenetwork. Thus,this
approachpromotesfairresourcesharingandscalability;however,itcannotguarantee
QoSdifferentiationandlatencyassurance.
Basedontheownership,NScanalsobeclassifiedintothefollowingcategories[31]:
• Local 5G Operator (L5GO) Slicing, which allows the local 5G operator to create
andmanagenetworkslicesthatmeetthespecificrequirementsofvarioususecases,
suchashospitals,universities,andindustrialenvironments. Thisapproachsupports
localizedcontrolandenhancesperformanceisolation,butinmanycountries,itmay
facelimitationsduetospectrumavailabilityandregulatoryconstraints.
• MobileNetworkOperators(MNO)Slicing,whichinvolvestheMNOmanagingthe
entireslicelife-cycle. ThisallowstheMNOtoachievecentralizedcontrol,efficient
resource allocation; however, it comes at the cost of increased capital and opera-
tional expenditures and greater complexity in orchestration, tenant isolation, and
SLAassurance.
Finally,accordingtothenetworkdomainwhereinslicingisapplied,NScanbeclassi-
fiedintothefollowingcategories:
• Radio Access Network (RAN) Slicing, that focuses on virtualizing radio resources
suchasspectrum,scheduling,andotherRANcomponentsincludingbasestations
and antennas. It enables flexible the sharing of radio resources among slices but

Electronics2025,14,4053
8of38
it faces challenges in allocating resources in real time, managing interference, and
coordinatingbetweenbasestations.
• Core Slicing, which involves partitioning the CN elements and functions, such as
routers, gateways, andservers, tocreatevirtualizednetworkslices. Itenablescus-
tomizedservicepathsandtheindependentoperationofeachslice,butitfacesissues
regardingscaling,security,andkeepingslicesproperlyisolated.
• Transportslicing,whichencompassespartitioningthenetworktransportinfrastruc-
ture, including optical fibers, switches, and routers, into separate virtual slices. It
enablesdifferentiatedandpersonalized5Gservicestailoredtospecificapplications
anduserneeds. However,integrationwithlegacynetworksandcoordinationacross
multipletransportlayersremainsignificantchallenges.
• E2ESlicing,whichreferstotheorchestrationandcoordinationofnetworkslicesacross
theentirenetwork,fromthecoretotheedge,toprovideseamlessconnectivityand
service delivery to end-users. It enables seamless connectivity and stable service
quality but is hard to implement because it requires coordination across domains,
workswithdifferentvendors,andinvolvescomplexservicemanagement.
Table2.Typesofnetworkslicing.
| ClassificationCriterion | Category |     | Definition |     |     |
| ----------------------- | -------- | --- | ---------- | --- | --- |
EachVirtualNetwork(VN)getsafixedportionof
StaticSlicing
physicalresourcesforitsentireservicelife.
Operatorsareabletodynamicallydesign,deploy,
ResourceAllocationType
|     | DynamicSlicing |     | customize,andoptimizetheslicesaccordingtothe |     |     |
| --- | -------------- | --- | -------------------------------------------- | --- | --- |
(SliceElasticity)
servicerequirementsorconditionsinthenetwork.
|     | Semi-Static    | or Semi- | Partoftheresourcesisallocatedstaticallywhile   |               |                  |
| --- | -------------- | -------- | ---------------------------------------------- | ------------- | ---------------- |
|     | DynamicSlicing |          | theotherpartisdynamicallyallocated.            |               |                  |
|     |                |          | Each slice                                     | is customized | to meet the spe- |
|     | Vertical       |          | cificrequirementsofdifferentverticalindustries |               |                  |
orapplications.
UseCaseType
Theresourcesaredistributedevenlyacrossdiffer-
|     | Horizontal |     | entslicestomeetthediverseneedsofvarioususers |     |     |
| --- | ---------- | --- | -------------------------------------------- | --- | --- |
orserviceswithinthenetwork.
Allowsthelocal5Goperatortocreateandmanage
|     | Local | 5G Operator |     |     |     |
| --- | ----- | ----------- | --- | --- | --- |
networkslicesthatmeetthespecificrequirements
(L5GO)Slicing
| OwnershipType |                       |     | ofvarioususecases. |                  |                  |
| ------------- | --------------------- | --- | ------------------ | ---------------- | ---------------- |
|               | MobileNetworkOperator |     | Involves           | the MNO managing | the entire slice |
|               | (MNO)Slicing          |     | life-cycle.        |                  |                  |
FocusesonvirtualizingtheRAN,whichinturnin-
|     | Radio | Access |     |     |     |
| --- | ----- | ------ | --- | --- | --- |
cludesthebasestations,antennas,andotherradio
Network(RAN)
networkcomponents.
InvolvespartitioningtheCNelementsandfunc-
|     | CoreSlicing |     | tions,suchasrouters,gateways,andservers,to |     |     |
| --- | ----------- | --- | ------------------------------------------ | --- | --- |
createvirtualizednetworkslices.
NetworkDomainType
Encompassespartitioningthenetworktransport
|     | TransportSlicing |     | infrastructure,includingopticalfibers,switches, |     |     |
| --- | ---------------- | --- | ----------------------------------------------- | --- | --- |
androuters,intoseparatevirtualslices.
Referstotheorchestrationandcoordinationofnet-
workslicesacrosstheentirenetwork,fromthecore
E2ESlicing
totheedge,toprovideseamlessconnectivityand
servicedeliverytoend-users.
3.3. NetworkSlicingTechnologyEnablers
ThefeasibilityofimplementingandapplyingtheNSconceptderivesfromtheelab-
oration of several technologies that allow the softwarization and virtualization of the
network. ThissubsectionoverviewsthekeyenablertechnologiesofNS,namelySDN,NFV,
Multi-accessEdgeComputing(MEC),andCloudComputing[11].

Electronics2025,14,4053 9of38
3.3.1. Software-DefinedNetworking(SDN)
TheSDNapproachmakesnetworkscapableoforchestratingandcontrollingapplica-
tions/servicesinamoregranularandE2Emannerthatbringsintelligence,flexibility,and
centralizedcontrolwithaglobalviewoftheentirenetwork. Moreover,respondingrapidly
tochangingnetworkconditions,aswellasbusiness-marketandend-userneeds,ismade
possibleviaSDN.SDNbridgesthegapbetweenserviceprovisioningandnetworkman-
agementbyintroducingavirtualizedcontrolplanethatenablesintelligentmanagement
decisionsacrossnetworkfunctions. Itusesstandardizedsouth-boundinterfaces(SBIs)to
makenetworkcontroldirectlyprogrammable[11].
3.3.2. NetworkFunctionVirtualization(NFV)
With NFV, certain network functions (NFs) can be virtualized and run on top of
commodityhardwaredevices.TheseNFscanbeeasilydeployedanddynamicallyallocated
independently of the software and hardware that exist in traditional vendor offerings.
ThisenablesnetworkresourcestobeefficientlyallocatedtoVirtualNetworkFunctions
(VNFs)throughdynamicscalingtoachieveServiceFunctionChaining(SFC).Resource
provisioningoptimizationtoend-userswithhighQoSisensuredbyNFVaswellasVNF
operationperformancebyincludingminimumlatencyandfailureratethresholds[11].
3.3.3. Multi-AccessEdgeComputing(MEC)andCloudComputing
ByleveragingMEC,dataisprocessednearthepointofgenerationandconsumption,
closetoend-users. Thisapproachprovidescloudcomputingcapabilitiestoapplicationand
contentproviders,alongwithanITserviceenvironmentatthemobilenetwork’sedge. As
aresult,thenetworkcandeliverultra-lowlatencyservicesessentialforbusiness-critical
applicationswhilealsosupportinginteractiveuserexperiencesinhigh-trafficareas.In2012,
Ciscocoinedthetermfogcomputing[32]especiallyforIoTarchitectures. AccordingtoYi
etal.[33]“FogComputingisageographicallydistributedcomputingarchitecturewitha
resourcepoolwhichconsistsofoneormoreubiquitouslyconnectedheterogeneousdevices
(includingedgedevices)attheedgeofnetworkandnotexclusivelyseamlesslybackedby
Cloudservices,tocollaborativelyprovideelasticcomputation,storageandcommunication
(andmanyothernewservicesandtasks)inisolatedenvironmentstoalargescaleofclients
inproximity”. Dependingontheexactlocationofcomputation,alternativeversions,like
MistComputing[34],havealsobeenproposed.
3.4. NetworkSliceLife-CyclePhases
AccordingtoITU-TTS28.530[4],themanagementaspectsofNScanbedistinguished
infourphases,namelythePreparation,theCommissioning,theOperation,andtheDecom-
missioning. Everytask,whichisrelevanttoslicedesign,instantiation,management,etc.,is
includedinoneoftheaforementionedphases. Table3summarizesthetasksofeachphase.
3.4.1. PreparationPhase
Beforethecreation/instantiationofanetworkslice,thefollowingpreparatorytasks
mustbecarriedout. SliceDesign(SD)involvesthedesignofarequirementstemplatethat
should be fulfilled by the new slice. These requirements are derived from the services
providedtothetenantsortotheusersthatwillbeassociatedwiththenewslice. Capacity
Planning (CP) involves the estimation of the network load that the new slice should
be able to handle, in conjunction with the overall network traffic. Network Function
Evaluation(NFE)involvestheassociationofspecificVNFswiththeslicetobecreatedand
theassessmentoftheperformanceofthesefunctions. NetworkEnvironmentPreparation
(NEP)involvesthenecessarypreparationsanddecisionmakingtobeperformedpriorto

Electronics2025,14,4053
10of38
theinstantiationofthenewslice. Thismayincludethemodificationofnetworkparameters
affectingalreadyrunningslicesandtheacceptanceorrejectionofanewslicerequest,based
onthecurrentnetworkenvironmentstatus, i.e., theadmissioncontrol, oneofthemost
importantdecision-makingtasksinthePreparationphase.
Table3.Tasksrelatedtoeachslicelife-cyclephase.Adaptedfromref.[4].
| Life-CyclePhase | RelatedTasks         | Description                |
| --------------- | -------------------- | -------------------------- |
|                 | Slicedesign(SD)      | Requirementstemplatedesign |
|                 | CapacityPlanning(CP) | Networkloadestimation      |
Preparation
|     | NetworkFunctionEvaluation(NFE)     | VNFsassociation       |
| --- | ---------------------------------- | --------------------- |
|     | NetworkEnvironmentPreparation(NEP) | Necessarypreparations |
|     | SliceInstanceCreation(SIC)         | NSIcreation           |
Commissioning NecessaryResourcesReservation(NRR) Essentialresourcesreservation
|     | ResourcesInitialAllocationandConfiguration(RIAC) | Reservedresourcesallocation |
| --- | ------------------------------------------------ | --------------------------- |
|     | Sliceactivation(SA)                              | NSIinoperation              |
|     | Monitoring(MON)-PerformanceReporting(PREP)       | KPIsupervision              |
Operation ResourcesCapacityPlanning(RCP) Allocatedresourcesassessment
|                 | SliceParametersModification(SPM) | Modificationpoliciesgeneration |
| --------------- | -------------------------------- | ------------------------------ |
|                 | Deactivation                     | NSIinactivation                |
| Decommissioning | ReservedResourcesRelease         | NSItermination                 |
3.4.2. CommissioningPhase
Afterthecompletionoftheprevioustasks,networkslicesshouldbecreatedaccording
totheslicerequeststhathavebeenadmittedinthepreviousphase. Moreover,inthisphase,
thefollowingtaskshavetobeperformed. TheNecessaryResourcesReservation(NRR)
task is performed first in order to ensure that the essential amount of resources for the
newslicewillbeavailableuponitscreation. Then,theSliceInstanceCreation(SIC)taskis
performedinordertocreatetheNetworkSliceInstance(NSI)ofthenewslice. Finally,the
ResourcesInitialAllocationandConfiguration(RIAC)taskisperformed,duringwhichthe
reservedresourcesareallocatedtothenewslice.
3.4.3. OperationPhase
FollowingtheCommissioningphase,thesliceisreadytoprovideserviceenteringthe
operationphase. ThefirsttasktobeperformedinthisphaseistheSliceActivation(SA)of
theNSI,whichisadecision-makingtaskthatbasicallycheckswhetherornottheNSIis
preparedtosupportcommunicationservices. Onceactivated,thereservedresourcesare
allocatedtothenetworkslice,enablingittoscheduletheseresourcesandprovideservices
tothesubscribedend-users.
After the activation, the tasks of Monitoring (MON) and Performance Reporting
(PREP)arecarriedoutinacontinuousmanner,astheyintendtosupervisespecificKey
PerformanceIndicators(KPIs)andQoSfulfillment. Furthermore,inordertomaintainthe
efficiencyoftheallocatedresources,theResourceCapacityPlanning(RCP)taskcalculates
thesliceresourceusageandtheperformancerelativetotheallocatedresources. Thistask
mayalsotakeintoaccounttrafficpredictionsinordertocalculateforthcomingperformance.
Theoutcomeofthistaskmaytriggerthesliceparametermodification(SPM)taskwhich
generatesmodificationpolicesthatmayaffectcertainsliceparameters. TheSPMtaskmay
betriggeredbyreceivingnewnetworkslicerequirementsornewsupervision/reporting
results. For all the aforementioned tasks of this phase, AI/ML has been proposed to
enhancethem.
Finally, the operation phase includes the deactivation task that is instantiated by
reportsindicatingthataspecificnetworksliceisnolongerrequired. Thistaskrendersthe
NSIinactiveandstopstheprovisionofcommunicationservicestoend-usersassociated
withthatslice.

Electronics2025,14,4053 11of38
3.4.4. DecommissioningPhase
Inthisphase,allreservedresourcesthatwerededicatedtothespecificslicearereleased.
Meanwhile,resourcesthatweresharedamongthedeactivatedsliceandotherslicesare
modifiedtoremoveanyconfigurationspecifictothedeactivatedslice.
3.5. NetworkSlicingEmpoweredwithAI/ML
Thecomplexityofcreating,operating,andmanagingaslicednetworkisveryhigh
consideringthatmultiplenetworkslicesmustcoexistontopofthesameinfrastructure,
sharingcommonavailablephysicalresources,whilebeinglogicallyisolated,independent
andoperatedbydifferenttenants. Thisrenderstraditionalhuman-drivennetworkman-
agementapproachesinadequateandturnsmachine-drivenmanagementapproachesinto
theonlyoption[35]. ThisisthereasonwhyAIandmorespecificallyMLapproacheshave
beenwidelyproposedintheliteraturetoempowerNS.
Furthermore, the 5G System (5GS) has been fully specified by 3GPP TS 23.501 in
ref.[36]andconsistsofvariousNetworkFunctions(NFs)forboththeuserandthecontrol
plane, each one of which is responsible for implementing specific functionalities. For
instance,oneofthemostpopularNFisAccessandMobilityManagementFunction(AMF),
acontrolplanekeyfunctionofthe5GCN,whichisresponsibleofregisteringtheUEsto
thenetwork,authenticatingthemandauthorizingtheiraccesstoservices. EachNFhas
appropriateserviceinterfacesforexchangingthenecessaryinformationwithotherNFsor
othersources. Forinstance,AMFutilizestheNamfandN1interfacesinordertoexchange
informationwithotherNFsandtheUE,respectively.
AnNS-relatedNFinthe5GSistheNetworkSliceSelectionFunction(NSSF),whichis
responsibleforselectingtheappropriatesliceforaUE.AMFexchangesUE-relateddata
withtheNSSFthroughtheN22interfaceandafterprocessingthem,NSSFinformsAMF
about the slice that fits most the UE. This is, in brief, the slice selection process, one of
theprocessesperformedduringtheOperationphaseoftheslicelife-cycle. Everyprocess
thatneedstobecarriedoutduringtheslicelife-cycleispartofacorrespondingNF,which
exchangesthenecessaryinputandoutputdatathroughthecorrespondinginterfaces.
The elaboration of ML methods has been widely proposed in order to tackle the
challenges and solve the problems arising during the application of the different NFs
relatedtoalmostallthetasksofthethreefirstphasesofthenetworkslicelife-cycle,which
were described in the previous subsection. Briefly, in the Preparation phase, ML has
been proposed to perform slice feature selection and extraction, traffic and congestion
prediction, embedding or placing VNFs and admission control. In the Commissioning
phase,MLhasbeenproposedforadaptiveresourcereservationandbothSICandRIAC.
Finally,intheOperationphase,MLhasbeenproposedforsolvingdecisionmakingand
optimizationproblems,forvariouspredictionsandforallocatingresources. InSection5,
theseapplicationsarepresentedindetail.
4. MLMethods
ML is a subset of AI that focuses on teaching machines to process data efficiently.
Depending on the nature of the data used for training, ML techniques can be broadly
categorized into four main groups: Supervised Learning (SL), Unsupervised Learning
(UL),Semi-SupervisedLearning(SSL),andReinforcementLearning(RL)[37,38]. However,
besidesthesebroadknowncategoriesthatarebasedonthenatureoffeedbackprovidedto
thealgorithmduringthelearningprocess,intheliterature,therearemanyotherclassifi-
cationsfollowingdifferentcriteria,suchasthepurposeforwhichtheMLisusedfor,the
mannerinwhichthemodelevolvesinresponsetofeedback[38],ortheprocesseddataset
exchangingapproach[39]. Inthissurvey,wewilladopttheclassificationthatisbasedon

Electronics2025,14,4053 12of38
thenatureofthedatausedfortraining. Furthermore,NeuralNetworks(NNs)cannotbe
confinedtoasinglecategory,astheyserveasfundamentaltoolsapplicableacrossthefour
aforementionedcategories. Forthisreason,NNsarepositionedherewithinbothSLandRL,
withspecificvariants,suchasFeed-ForwardNNs(FFNNs),includedinbothcategories.
ItisimportanttonotethatthisworkfocusessolelyonpresentingtheMLmethods
proposedintheliteraturetoaddressproblemsrelatedtoNSapplicationsin5GandBeyond
5GNetworks. Adetaileddescriptionofthefunctionalityofthesemethodsisbeyondthe
scopeofthisstudy. Readersareencouragedtoconsulttherespectivereferencedarticles
for more comprehensive information on the functionality of these methods and their
variousintricacies.
4.1. SupervisedLearning
In SL techniques, labeled training datasets are used to build models. This process
involvesprovidingthealgorithmwithsampledatapairsofinputsanddesiredoutputsas
trainingdata. Theprimaryobjectiveofthesetechniquesistoconstructafunctionthatmaps
theinputstotheoutputs. Consequently,givennewinputs,thisfunctionwillbecapableof
estimatingthecorrespondingunknownoutputs. Theoutputofthefunctioncanbeeither
continuousnumericvalues(inthecaseofregression)orclasslabelsfortheinputvalues(in
thecaseofclassification)[40].
Indicative methods of this category include Support Vector Machine (SVM), Least
Absolute Shrinkage and Selection Operator (LASSO), Random Forest (RF), k-Nearest
Neighbor(KNN),GradientBoostingDecisionTree(GBDT),andseveraldifferentArtificial
NeuralNetworks(ANNs)liketheMulti-LayerPerceptron(MLP),ConvolutionalNeural
Networks(CNNs),RecurrentNeuralNetworks(RNNs),etc.
4.2. UnsupervisedLearning
InULtechniques,unstructureddataordatawithoutlabelsareprovidedtothelearning
algorithmasinput. Thealgorithmistaskedwithidentifyingpatternsorstructureswithin
theinputdata,eventhoughnoexplicitfeedbackisprovided. Suchtechniquesaremainly
usedfordataclustering,dimensionalityreduction,anddensityestimation[40,41].
AlgorithmsinthiscategoryincludeK-means,SpectralClustering,PrincipalCompo-
nentAnalysis(PCA),SparseAutoencoder(SAE),andExpectationMaximization(EM).
4.3. Semi-SupervisedLearning
SSLtechniquescombinebothlabeledandunlabeleddataforthetraining. Anenor-
mous amount of unlabeled data and sparse labeled data are used to mainly create an
appropriatemodelofdataclassification[42].
AnalgorithminthiscategorythatisrelatedtoNSistheVariationalAutoencoders
(VAEs)forSemi-SupervisedLearning.
4.4. ReinforcementLearning
InRLtechniques,theentitiesoftheagent(i.e.,thelearningalgorithm)andtheenvi-
ronmentareintroduced. Thelearningprocessisbasedonaseriesofinteractionsbetween
these entities. Specifically, the agent first receives percepts containing the state of the
environment(orsystem). Theagentthenperformsanactionthatresultsinachangeinthe
environment’sstate. Basedonthisnewstate,theagentreceivesfeedbackintheformofa
rewardorapenalty. Thisactionandfeedbackprocessisiterateduntiltheagentlearnsto
navigatetheenvironmenteffectively. ThetwokeyfactorsthatcharacterizeRLtechniques
arethetransitionmodel(whichdefineshowtheenvironmenttransitionsfromonestateto
thenext)andthepolicy(whichdeterminestheactiontakeninagivenstate)[40].

Electronics2025,14,4053 13of38
Algorithms included in this category are the Markov Decision Process (MDP), the
State–Action–Reward–State–Action(SARSA),Q-Learning(QL),theLinearFunctionAp-
proximation(LFA),theMulti-ArmedBandit(MAB),etc.
5. Phase-RelatedMLApplications
TheexploitationofMLmethodsisakeyenableroftheNSconceptin5G.Consequently,
themajorityofresearchworksinthefieldofNSrefertoAI/MLapplicationsasacornerstone
formakingtheNSconceptfeasible. SomekeyapplicationsofMLtechniquesinthecontext
ofNSincludeclassification,prediction,clustering,andpatternrecognition.
Inthissection,wewillsummarize,foreachsliceofthelife-cyclephase,theapplications
ofAI/MLthathavebeenproposedintheliterature,inordertoaddresspotentialchallenges
thatariseduringNSimplementation.
5.1. MLinPreparationPhase
Various ML techniques can be applied in different tasks of the Preparation phase.
Singhetal.[43]usedSVMandK-Meansforslicedesign(SD).Morespecifically,theauthors,
intheirNetworkSub-SlicingFramework,appliedSVMforfeatureselectionandK-Means
for grouping similar services, for use cases such as IoT. Experimental results showed
improvedperformanceintermsoflatencyandenergyefficiency.
In addition to slice design, ML methods can be incorporated during the Network
EnvironmentPreparation(NEP)task.Tothisend,Begaetal.[44]analyzed5Ginfrastructure
marketsfromtheperspectiveofamobilenetworkoperator,focusingonhowtheoperator
shouldmanagenetworkslicerequeststomaximizerevenuewhileensuringthatexisting
slice guarantees are upheld. They modeled this challenge as a Semi-Markov Decision
Process(SMDP)andproposedaQLalgorithmforsliceadmissioncontrol. Theirevaluation
demonstratesthattheQLalgorithmperformsnearlyaswellastheoptimalValueIteration
policyintermsofrevenueandgain,anditsignificantlyoutperformstheoptimalpolicyin
perturbedscenariosduetoitsadaptivenature.Moreover,inref.[45],todealwithscalability
issues,theauthorsextendedtheirpreviousworkbyintroducingtheNetwork-slicingNeural
NetworkAdmissionControl(N3AC)algorithm,aDRLalgorithmthatusestwoFFNNsto
calculaterewardsforacceptingorrejectingrequests. Itsgoalistomaximizethenumber
of accepted slice requests while maintaining QoS for existing slices. Simulation results
demonstratedthatN3ACachievesperformanceclosetotheoptimalpolicy. Bakrietal.[46]
focusedonmaximizingtheInfrastructureProviders’(InPs)revenuewhileminimizingthe
SLAviolationpenalties.Specifically,theauthorsevaluatedtheQL,theDeepQL(DQL),and
theRegretMatching(RM)algorithms’abilitytoidentifyoptimaladmissionpoliciesand
assessedtheirperformanceinbothofflineandonlinescenarios,whichiscrucialforpractical
deployment. TheresultsindicatedthatQLandDQLperformbetterwhentrainedoffline
beforeonlinedeployment,whereasRMoutperformsbothQLandDQLinreal-timeonline
usage. Razaetal.[47]proposedasliceadmissionstrategythatincreasesInPs’revenue
byacceptingasmanyslicerequestsaspossiblewhileminimizingSLAviolationpenalties
byrejectingrequeststhatcoulddegradeotherservices. Toachievethisgoal,theyuseRL
(i.e.,anANN).Performanceevaluationagainstnon-MLapproaches,includingstaticand
threshold-based heuristics, showed that their RL-driven admission policy outperforms
theotherapproachesintermsofoverallloss,whichincludespotentialrevenuelossfrom
rejectedservicesandlossesfromservicedegradationwhenresourceslicescannotbescaled
upasneeded. Businessprofitisalsothefocusinref.[48]. Specifically,theauthorsfocused
ontheAdmissionControlforServiceFederation(ACSF)problem,wheretheadmission
controllerselectsthedomainforservicedeploymentorrejectsittomaximizelong-term
profitwhileaccountingforfederationcosts.Todealwiththisproblem,theauthorsapplieda

Electronics2025,14,4053 14of38
specifictypeofRL,calledaveragerewardlearning,alongwithQL.Theresultsshowedthat
theproposedmethodoutperformsQL,whichstrugglesduetoitsrelianceonthereward
discountfactor. Sciancaleporeetal.[49]introducedOnlineNetworkSlicing(ONETS),an
onlineslicebrokerthatapprovesordeniesslicerequestsbyanalyzingpastdataandusing
resourceoverbookingtomaximizerevenueandminimizeSLAviolations. Theymodeled
theproblemasaBudgetedLock-upMulti-ArmedBandit(BLMAB)andenhancedtheUpper
ConfidenceBound(UCB)approachtoreducecomplexity. EvaluationshowedthatONETS
outperformsnon-ML-basedsolutionsinsystemutilization,multiplexinggain,andSLA
violationreduction. Rezazadehetal.[50,51],workedonthejointsliceadmissioncontrol
and resource allocation problem, which lays in both Preparation and Commissioning
phases;thus,theirworkwillbepresentedinSection5.2.
Ontopofthesestudies,intheliterature,therehavebeenworksthatapplyMLforboth
NEPandNetworkFunctionEvaluation(NFE)tasks. Guanetal.[52]presentedahierarchi-
calresourcemanagementframeworkforcustomizedslicingwheremultipleInPsmanage
multi-tenantE2Eslices. Theauthorsintroducedaglobalresourcemanagerthat,withinits
functionalplane,deploysaServiceBrokerresponsiblefortheadmissioncontrolofreal-time
slicerequestsfrommultipletenantsusingtheDQLalgorithm. Theframeworkaimstoopti-
mizeadmissioncontroldecisionsandmaximizetheaveragerewardbyreservingresources
forrequeststhatgeneratehigherrevenuefortheInP.Evaluationresultsdemonstratedthat
theproposedintelligentframeworkachievesbetterservicequalitysatisfactioncompared
tonon-intelligentapproaches. Sulaimanetal.[53]proposedamulti-agentDRLsolutionto
addressNSandadmissioncontrolin5GCloud-RAN(CRAN),aimingtoimprovelong-term
InPrevenue. Theirmulti-agentDRLapproachusesseparaterewardfunctionsforeach
agentbasedonadmissioncontrolandslicingpolicies,whichallowsbothagentstowork
synergistically without interference. The evaluation results showed that the proposed
solutionoutperformsgreedyandsingle-agentDRLapproachesintermsofInPrevenueand
averageavailablebandwidth. Yanetal.[54]tackledtheautomaticVirtualNetworkEm-
bedding(VNE)problem,whereVirtualNetworkRequests(VNRs)mustbemappedonto
substratenetworkresources. EachVNRrequiresspecificresourcesand,ifavailable,these
resourcesareallocated;otherwise,theVNEalgorithmmayrejectorpostponetherequest.
TheauthorsproposedaDRL-basedVNEschemethatusesaGraphConvolutionalNetwork
(GCN)forfeatureextractionandusesAsynchronousAdvantageActor–Critic(A3C)for
parallelpolicygradienttraining,optimizingtheVNEpolicywithconsiderationsintermsof
requestacceptance,long-termrevenue,loadbalance,andpolicyexploration. Simulations
showedthattheproposedA3C-GCNschemesignificantlyimprovestheacceptanceratio
andaveragerevenuecomparedtootherstate-of-the-artmethods. Rkhamietal.[55]also
addressedtheVNEproblemincoreslicesusingDRL.Theyproposedatwo-stepapproach:
first,applyingaheuristictofindasub-optimalsolution,thenoptimizingwithDRL.Intheir
model,calledImprovingtheQualityofVNEHeuristics(IQH),thesystemstatesarerepre-
sentedasheterogeneousgraphsusingaRelationalGCN(RGCN),andactionprobabilities
arecalculatedwithanMLP.Thegoalistoimprovetherevenue-to-costmetric. Simulations
showedsignificantimprovementswhileusingtheFirst-FitandBest-Fitheuristics. Esteves
etal.[56]proposedaHeuristicallyAssistedDRL(HA-DRL)approachfortheNetwork
SlicePlacement(NSP)problem,usingaGCNforfeatureextractionandA3Cforsolving
theNSP.HA-DRLaimstominimizeresourceconsumption,maximizesliceacceptance,and
balancenodeload. ItincorporatesamodifiedActorNetworkwithaheuristiclayerbased
onthePowerofTwoChoices(P2C)algorithm. HA-DRLwascomparedagainstpureDRL
and P2C, showing faster convergence, near-real-time placement, and better acceptance
ratios. Kibalya et al. [57] tackled the slice deployment challenge across multi-provider
infrastructures,focusingonthecandidatesearchproblem. Inresponse,theyproposedthe

Electronics2025,14,4053
15of38
CandidateSearchAlgorithm(CaSA),whichfiltersfeasibleInPsbasedonnetworktopology
and slice constraints. A DRL neural network is then used to select the optimal InP set,
maximizingtherevenue-to-costratioforslicedeployment.
AnothertaskinwhichMLcanbeincorporatedinthePreparationphaseisCapacity
Planning(CP).Aboeleneenetal.[58]proposedtheError-aware,Cost-effectiveandProac-
tiveNSFramework(ECP)forCP,predictingtrafficlevelsandproactivelycreatingslicesfor
increaseddemand. ECPoperatesintwophases: thefirstusespredictionmodelslikethe
RF,theAutoRegressiveIntegratedMovingAverage(ARIMA),andtheLongShortTerm
Memory(LSTM)toforecastfutureload,whilethesecondusesaDRLmethodwithProximal
PolicyOptimization(PPO)tocreatecost-effectiveslices. SimulationsshowedthatLSTM
providesthehighestaccuracy,andECPallocateslower-costslicesefficiently. ECP’sfirst
phasealignswiththePreparationphase,andthesecondphasealignswiththeCommission-
ingphase. Dandachietal.[59]proposedaCross-sliceAdmissionandCongestionControl
algorithm,dealingwithbothNEPandCPtasks. Theirsolutioncombinesadmissionand
congestioncontrollersusingtheSARSAalgorithmwithLFAinordertooptimizeresource
utilizationandsystemperformancebyreducingtherejectionofbest-effortslicerequests
andincreasingtheacceptancerateofguaranteedQoSslices.
Finally, in the Preparation phase, according to ref. [27], another task in which ML
canbeappliedisthepredictionofservicedemand. TechniqueslikeRNNscananalyze
historicaldatatomakeaccuratepredictionsofservicedemandforaslice,whichcanthen
informdecisionmakingduringtheCommissioningphase.
Table4summarizestherelatedtasks,theallocation,theusecaseandnetworkdomain
types,theMLcategory,aswellasthemethodproposed,andwhetherthatmethodwas
testedforeachofthereferredworksofthepreparationphase.
Table4.SummaryofML-basedNSinthePreparationphase(SD:slicedesign,NFE:NetworkFunction
Evaluation,NEP:NetworkEnvironmentPreparation,CP:CapacityPlanning).
|     | Allocation | UseCase NetworkDo- | MLCat- | Simulations- |
| --- | ---------- | ------------------ | ------ | ------------ |
Ref. Task MLMethod
|          | Type    | Type mainType | egory        | Testbed |
| -------- | ------- | ------------- | ------------ | ------- |
| SD       |         |               | SL SVM       |         |
| [43]     | Static  | Vertical E2E  |              | Yes     |
| NFE      |         |               | UL K-means   |         |
| [44] NEP | Dynamic | Vertical RAN  | RL QL(SMDP)  | Yes     |
| [45] NEP | Dynamic | Vertical RAN  | RL DRL(FFNN) | Yes     |
| [46] NEP | Dynamic | Vertical RAN  | RL QL,DQL    | Yes     |
| [47] NEP | Dynamic | Vertical RAN  | RL ANN       | Yes     |
Average Re-
| [48] NEP | Dynamic | Vertical RAN | RL  | Yes |
| -------- | ------- | ------------ | --- | --- |
ward,QL
| [49] NEP     | Dynamic | Vertical E2E    | RL BLMAB          | Yes |
| ------------ | ------- | --------------- | ----------------- | --- |
| [50] NEP     | Dynamic | Vertical RAN    | RL DDPG,TD3       | Yes |
| [51] NEP     | Dynamic | Vertical RAN    | RL D-TD3          | Yes |
| [52] NFE,NEP | Dynamic | Vertical E2E    | RL DQL            | Yes |
| [53] NFE,NEP | Dynamic | Vertical RAN    | RL Multi-agentDRL | Yes |
| [54] NFE,NEP | Dynamic | Vertical RAN    | RL GCN,A3C        | Yes |
| [55] NFE,NEP | Dynamic | Horizontal Core | RL RGCN,MLP       | Yes |
| [56] NFE,NEP | Dynamic | Vertical Core   | RL A3C,GCN        | Yes |
| [57] NFE,NEP | Dynamic | Horizontal E2E  | RL DRL            | Yes |
| [58] CP      | Dynamic | Vertical E2E    | RL LSTM           | Yes |
SF7SARSA,
| [59] NEP,CP | Dynamic | Horizontal E2E | RL  | Yes |
| ----------- | ------- | -------------- | --- | --- |
LFA

Electronics2025,14,4053 16of38
5.2. MLinCommissioningPhase
The main tasks to be carried out during the Commissioning phase involve slice
creation,includingresourcereservationandorchestration,servicegrouping,andresource
allocation. Once a slice request is accepted and preparation for its creation begins, the
necessaryresourcesmustfirstbereservedtoensurethattheyareavailableforallocationto
thenewslicelater.
According to the network services that each slice should provide, the appropriate
VNFsshouldbeassignedtoit. Forthisplacement,AI/MLmethods,likeDeepLearning
(DL),canbeapplied[27]toensureadynamicapproachthatadaptstotime-varyingservice
demandswhilemeetingservicedelayrequirements.Additionally,theappropriateresources
mustbereservedforeachslice,priortoitscreation,basedontheservicedemandsthat
eachsliceisexpectedtohandle. Sincethesedemandsareinfluencedbytime-varyingdata
trafficloads,resourcereservationshouldbeadaptivetothesevariations. Toaddressthis,
RLmethods,suchasDeepDeterministicPolicyGradient(DDPG),canbeemployedfor
efficientresourcemanagement.
ExtendingtheaforementionedVNFplacementtask,theauthorsofref.[60]statethat
theplacementoftheVNFsontheslicesneedstobecarriedoutautonomously,asthisisa
keyaspectoftheZero-touchnetworkandServiceManagement(ZSM)in5Gandbeyond
networks. Withthatsaid, theyproposeamechanismcalledSCHEMA,whichisaZSM
schemethatemphasizesthescalabilityofmulti-domainnetworksandtheminimizationof
servicelatency. Thecomplexmulti-domainsliceserviceplacementproblemismodeled
asaDistributedMDP,andaDistributedRLapproachisemployedtosolveitbyplacing
RLagentsineachdomain,orchestratinginthiswaytheVNFsindependentlyofotherRL
agentsindifferentdomains. Theproposedschemewasevaluatedandproventobeable
tosignificantlyreducetheaverageservicelatencywhencomparedagainstacentralized
RLsolution.
The last task of the Commissioning phase, denoting the creation of the network
slice, is the initial allocation of network resources to the new slice. The resources to be
allocated vary and include communication (radio), caching, and computing resources.
In this resource allocation process, AI/ML methods can be applied [15,61]. The initial
allocationofresourcestakesplaceinthisphasetoenabletheslice,eventhoughtheamount
ofallocatedresourcesmayalteraccordingtotheneedsofthesliceinthenextphase.
Inref.[62],Zhangetal. addressedtheproblemofvehicularmulti-sliceoptimization,
focusing on slice allocation strategies. Specifically, their proposal aims to calculate the
priorityqueueofslicerequestswaitingtobedeployedontheRAN,takingintoaccountthe
systemstatus,availablespectrumresources,andthedeploymentdelayconstraintsofeach
request. Theoptimizationobjectiveistoselectapriorityqueuethatminimizesaverage
latencywhilemaximizingoverallserviceutility. Tosolvethisoptimizationproblem,the
authorsemployedQLanddevelopedanalgorithmcalledtheIntelligentVehicularMulti-
sliceOptimization(IVMO)algorithm. Todemonstratetheeffectivenessoftheirapproach,
they conducted simulations and compared IVMO’s performance—measured in terms
of the number of requests in the queue and service utility—against two other non-ML-
basedmethods(fairallocationandgreedyalgorithm). Accordingtothesimulationresults
presented,theproposedIVMOalgorithmachievesbetterperformanceonbothmetrics.
Inref.[63],Quangetal. workedontheVNF-ForwardingGraph(VNF-FG)embedding
problem,whichinvolvesdeployingservicerequestsontheCNbyallocatingresourcesto
meettheservicerequirementsintermsofQoS,whileadheringtotheconstraintsofthe
underlyinginfrastructure. EachVNF-FGrequestconsistsofVNFsconnectedbyVirtual
Links(VLs). VNFsrequirespecificcomputingresources,suchasCPU,RAM,andstorage,
whileVLsarecharacterizedbynetwork-orientedmetrics,e.g.,bandwidth,latency,and

Electronics2025,14,4053 17of38
packet loss rate. The authors formulated the VNF-FG allocation problem as an MDP
with appropriate states and actions, aiming to maximize the number of accepted VNF-
FGs. AVNF-FGisconsideredacceptedonlyifallitsVNFsandVLsareallocatedandthe
QoSrequirementsaresatisfied. Toaddressthiscomplexproblem,theauthorsproposed
anenhancedDDPGalgorithmcalledEnhancedExplorationDDPG(E2D2PG).E2D2PG
incorporatestheconceptsof“replaymemory”andtheHeuristicFittingAlgorithm(HFA)
to determine the embedding strategy. To evaluate the performance of their proposed
algorithm,theauthorsconductedsimulationscomparingE2D2PGwiththestandardDDPG.
TheresultsdemonstratedthatE2D2PGoutperformsDDPGintermsofacceptanceratio
andthepercentageofdeployedVLs.
Inref.[64],ZhaoandLiproposedanRL-basedapproachforthecooperativemapping
ofslicerequeststophysicalnodesandlinks. Theirproposedalgorithm,namedRLCO,aims
todeploynetworkslicerequeststotheCNbydeterminingtheoptimalslicingpolicy. This
policycooperativelymapsrequeststophysicalnodesandlinks,consideringthereal-time
resourcestatusofthesubstratenetworkwhilemaximizingtherequestacceptancerateand
theearning-to-costratio. Intheproposedmappingscheme,RLCOhandlesnodemapping,
Dijkstra’salgorithmisusedforlinkmapping,andanRL-basediterativeprocessisapplied
toidentifythemappingstrategythatmaximizesarewardfunction. Thisrewardfunction
accountsforthecross-impactamongbenefits,costs,nodes,andlinks.
TherealsoexistapproachesthattackleproblemslyinginboththePreparationand
Commissioningphases. Forinstance,theECPNSframeworkproposedinref.[58],which
was already presented in Section 5.1, has two phases, the first of which belongs to the
Preparation phase, while the second belongs to the Commissioning phase. During the
secondphase,aPPOmethodisusedtocreatecost-effectiveslices,basedontheforecast
loadderivedinthefirstphase. Anotherexampleispresentedinref.[50],wheretheauthors
focusedonaCRANjointsliceadmissioncontrolandresourceallocationproblem.Theyfirst
formulatedthisproblemasanMDPandthenappliedanadvancedcontinuousDRLmethod,
calledTwinDelayedDDPG(TD3),tosolveit. TheTD3algorithm,basedonthestate–actor–
criticmodel,aimstooptimizepoliciesovertime,enablingtheCentralUnittoautonomously
reconfigurecomputingresourceallocationsacrossslices. Thisapproachminimizeslatency,
energyconsumption,andtheinstantiationoverheadofVNFsforeachslice.
In their later work [51], the authors tackled the same joint problem in a B5G RAN
environment. In particular, they proposed an NS resource allocation algorithm based
on a lifelong zero-touch framework. This algorithm, termed prioritized twin delayed
distributionalDDPG(D-TD3),differsfromTD3inthatitemploysdistributionalreturn
learninginsteadofdirectlyestimatingtheQ-value. Here,theQ-valueisrepresentedasa
distributionfunctionofstate–actionreturns.Additionally,theauthorsincorporatedareplay
buffer,allowingD-TD3agentstomemorizeandreusepastexperiences. Forevaluation
purposes, the proposed algorithm’s performance was assessed in terms of admission
rate,latency,CPUutilization,andenergyconsumptionagainstotherstate-of-the-artDRL
approaches,suchasTD3,DDPG,andSoft–Actor–Critic(SAC).Theresultsdemonstrated
thatD-TD3outperformsthesemethods,achievingsuperiorresultsinallevaluatedmetrics.
Table5summarizestherelatedtasks,theallocation,theusecaseandnetworkdomain
types,theMLcategory,themethodproposed,andwhetherthatmethodwastestedfor
eachofthereferredworksintheCommissioningphase.

Electronics2025,14,4053
18of38
Table5.SummaryofML-basedNSintheCommissioningPhase(SIC:SliceInstanceCreation,RIAC:
Resources’InitialAllocationandconfiguration,NRR:NecessaryResourcesReservation).
|               | Allocation | UseCase NetworkDo- | MLCat-         | Simulations- |
| ------------- | ---------- | ------------------ | -------------- | ------------ |
| Ref. Task     | Type       | Type mainType      | egory MLMethod | Testbed      |
| SIC,RIAC      |            |                    | SL DL          | No           |
| [27]          | Dynamic    | Vertical RAN       |                |              |
| NRR           |            |                    | RL DDPG        | Yes          |
| [50] SIC,RIAC | Dynamic    | Vertical RAN       | RL DDPG,TD3    | Yes          |
| [51] SIC,RIAC | Dynamic    | Vertical RAN       | RL D-TD3       | Yes          |
| [58] RIAC     | Dynamic    | Vertical E2E       | RL PPO         | Yes          |
DistributedRL+
| [60] SIC,RAIC | Dynamic | Vertical E2E |     | Yes |
| ------------- | ------- | ------------ | --- | --- |
RL MDP
| [62] RIAC | Dynamic | Vertical RAN    | RL QL     | Yes |
| --------- | ------- | --------------- | --------- | --- |
| [63] RIAC | Dynamic | Horizontal Core | RL E2D2PG | Yes |
| [64] NRR  | Dynamic | Vertical Core   | RL N/A    | Yes |
5.3. MLinOperationPhase
Theoperationphasehasattractedthemostattentionfromtheresearchcommunityfor
applyingMLmethodstoitsrelatedtasks. Thisisbecausethetasksinthisphasehavethe
greatestimpactontheperformanceandeffectivenessofNS,requiringcomplexreal-time
computations. Forinstance,ultra-lowlatency(equalorlessthan1msforURLLCapplica-
tionssuchasautonomousdrivingorindustrialautomation),highreliability(≥of99.999%
availabilityformission-criticalservices),massiveconnectivity(supportforupto1million
devicespersquarekilometerinmMTCscenariossuchassmartcitiesorsensornetworks),
andguaranteedhighthroughput(multi-GbpsratesforeMBBservices,likeAR/VRand
UHDvideostreaming)havetobeachieved. Theserequirementsarehighlydynamicand
context-dependent,makingreal-timeadaptationessential.
Thevolumeofpastresearchworksinthisphaseissignificantenoughtonecessitate
grouping the works by broader task categories rather than the ones explicitly listed in
Table3. Assuch,eachgroupencompassesthemultipletasksmentionedinTable3. The
resultinggroupsareasfollows:
• DecisionMaking–Optimization–Classification
• Monitoring–Prediction
• ResourceAllocation
5.3.1. DecisionMaking–Optimization–Classification
Thisgroupinvolvesworksthatdealwithproblemsrelatedtothetasksofsliceactiva-
tion(SA),sliceparametermodification(SPM),PerformanceReporting(PREP)andResource
CapacityPlanning(RCP).
Morespecifically,inSA,thedecisiononwhetherasliceinstanceshouldbeactivatedis
taken.Forexample,Phyuetal.[65]proposedaMAB-basedsliceactivation/deactivationap-
proachthatconsiderstheuserQoSandthenetworkenergyconsumption. Morespecifically,
theauthorsformulatedthesliceactivation/deactivationproblemusingMDP,andthen
usedtheMABapproachtoidentifythenear-optimalsliceactivation/deactivationdecision
whileensuringtheQoSrequirementsforindividualusersaremaintained. Furthermore,
theauthorsextendedtheirpreviousworkinref.[66]byconsideringthejointsliceactiva-
tion/deactivationandtheuserassociationproblem.Theproposedmulti-agentfullycooper-
ativedecentralizedframework(ICE-CREAM)usestheDecentralizedPartiallyObservable
MDP(Dec-POMDP)toformulatetheproblemandthemulti-agentpartiallyobservable
state-awareMAB(POMAB)tofindthenear-optimalsolutiontotheaboveproblem.

Electronics2025,14,4053 19of38
Sliceselectionisanothertypeofdecision-makingtaskperformedinthisphase. In
ref. [67], the authors proposed an ML model based on a CNN to determine the most
suitablenetworksliceforadevicetoassociatewith. Theirmodel,DeepSlice,firstpredicts
the traffic load for each slice (as discussed in the next subsection). Then, based on the
service requested parameters, it employs a DLNN to make the slice selection decision.
Inref.[68],Xietal. consideredtheresourceslicingconcepttomaximizeMobileVirtual
NetworkOperators’(MVNOs)benefitsfromthesharedRANinfrastructure.Theyproposed
a mechanism for assigning users to slices, aiming to optimize the MVNO’s long-term
benefitswhileconsideringresourceavailability. TheymodeledtheproblemasanSMDP
andemployedaDRL-basedalgorithmtoaddressthecurseofdimensionalityandenable
onlineoptimization. Specifically, theyusedDeepQ-Network(DQN)andcomparedits
performancewithconventionalQLandRandomResourceAllocation(RRA).Theirresults
showedthatDQNconvergessignificantlyfasterthanQL.Moreover,inhigh-userscenarios,
DQNachieveshighernetworkthroughputandtotalMVNOutilitycomparedtobothQL
and RRA. Shome et al. [69] consider the 3GPP Rel. 16, which enables User Equipment
(UE)toconnecttoupto8networkslices—anaspectoverlookedinrelatedworks. They
proposedaDRL-basedsliceselectionandbandwidthallocationapproachthatconsiders
QualityofExperience(QoE),pricesatisfaction,andspectralefficiency. Inthisapproach,
eachvirtualbasestationisassignedaDQNagent,whichdeterminestheslice(s)towhicha
userwillconnect,basedontheservicerequirementsandavailableresources. Compared
toanotherDQNapproach,theproposedmethodachievesbetterperformanceintermsof
usersatisfaction,convergencetime,andbandwidthsavingsperuser. Inref.[70],Tangetal.
focusedonthecontextofintelligentvehicularnetworks,wherethevehiclesneedtooffload
theirintelligenttaskstotheappropriateslices. Theseslices,calledresourceslices,must
providesufficientresourcestomeetthedemandsoftheconnectedvehicletasks.Theauthors
proposedaSliceSelection-basedOnlineOffloading(SSOO)algorithm(usingaDeepNeural
Network(DNN))thatleveragesdistributedintelligencetoperformresourcesliceselection
andvehicleassignment,andtakesintoaccountthecurrentsystemenvironment,aiming
tominimizethesystem’senergycost. Toevaluatetheirproposedscheme’sperformance,
theycompareditwiththreebaselineschemes: ETCORA,DRL-CORA,andGA-NSS.The
selectedperformancemetricsincludedaveragedeviceenergyconsumption,totalenergy
consumption, task completion rate, and the number of tasks processed by slices. The
experimental results demonstrate that the proposed SSOO algorithm outperforms the
otheralgorithms.
Anotherdecision-makingtaskrelatedtothisphaseistheallocationofuserservice
requests to slices. In ref. [71], Zhang et al. proposed a slicing model and a resource
allocationschemefortheCN.Themainchallengetheyaimedtoaddressrevolvedaround
determining the slice in which a service request should be deployed to ensure a high
transmission success rate. To achieve this, they proposed a Multi-output Classification
Edge-basedGraphConvolutionalNetwork(MCEGCN)whichessentiallyisanSL-based
resourceallocationmodelthatpredictsthesliceonwhicharequestshouldbedeployedto
maximizethenumberofsuccessfullytransmittedrequests.ThemodelconsistsoftwoEdge-
basedGraphCNNs(EGCNs)thatcanextractthespatialcorrelationsofthenetwork’sedge
features. TheauthorschosethisapproachoveraDNNbecause,astheystate,DNNsmay
failinpredictionsincetheycannotexploitthegraphstructureofthenetwork’slinks. For
evaluation,theycomparedtheperformanceoftheirproposedmodelwithotherapproaches,
including a Multi-Layer Perceptron (MLP), another neural network-based model. The
performance metrics included a deployment success rate and total transmission across
differentutilizationrates,andtheresultsshowedthatMCEGCNoutperformstheothers. In
ref.[72],Tsourdinisetal. presentedaframeworkforsliceallocationbasedontheservices

Electronics2025,14,4053 20of38
runningontopofacloud-nativenetwork,enablingthecreationofafullyservice-aware
networkforB5Gapplications. Morespecifically,thisframeworkmakesaccuratedecisions
regarding slice allocation by classifying, in real-time, the traffic exchanged by different
usersandbypredictingthefutureconnectivityneedsofapplications. Theauthorsexplored
theadoptionofseveralMLmodelsforthistask(FFNN,RNN,LSTM,BidirectionalLSTM
(BiLSTM))andconcludedthatahybridCNN-LSTMdistributedlearningschemeprovides
thebestperformance. Specifically,theCNNisappliedtouser-generatedtrafficforfeature
extraction, noise reduction, and dimensionality reduction. The processed information
is then passed to the LSTM, which captures data patterns using memory components,
enablingtheforecastingoffuturedatatrends.
IntheOperationphase,therearetasksrelatedtooptimizingsliceparameters,policies,
orevenprofit-relatedvalues. Tothisend,theauthorsinref.[73]proposedacomputing
resourceallocationoptimizationapproachforafog-RANscenario,whichincludesacluster
offognodescoordinatedwithanedgecontroller(EC).TheproposedDQN-basedapproach
can learn the network’s dynamics and adapt to them by optimizing the computing re-
sourceallocationpolicyoftheedgecontrollers. Meietal.[74]introducedanintelligent
networkslicingarchitectureforVehicle-to-Everything(V2X)services, whichincludesa
SliceDeploymentController(SDCon)thatadjuststhenetworkslicingconfigurationscheme
toensuretheQoSrequirementsofV2Xservicesandreducethenetworkcostformobile
networkoperators. AuthorshaveproposedaDQNthatincorporatesLSTMtomakethe
adaptationdecisions,whichimprovestheQoScomparedtoanon-ML-basedapproach.
Zhangetal.[75]proposedaDDPG-basedpricingandresourceallocationschemeinoptical
datacenters,whichencouragestenants,i.e.,theserviceproviders(SPs),torequestresources
inaload-balancedmannerthatreducesthecumulativeblockingprobability. Similarly,in
ref.[76],Luetal.proposedaDLR-basedschemeforaninter-datacenteropticalnetwork(ID-
CON).Simulationresultsconfirmedthat,comparedtoatraditionalcentralizedapproach,
theproposedschemeincreasestheInPs’profitandreducescomputationalcomplexity. In
ref.[77],Khodapanahetal. proposedaslice-awareradioresourcemanagementframework
thatensuresthesliceKPIs’fulfillmentbyfine-tuningtheslice-relatedcontrolparametersof
thepacketschedulerandtheadmissioncontroller. Forthispurpose,authorsemployedan
SL-basedANNwhoseobjectiveistoprovidetheappropriatesetofcontrolparametersthat
maximizetheKPIs.
Severalworksaddressslicereconfigurationanddecisionmakingunderuncertainty.
Weietal.[78]investigatedtheNetworkSliceReconfigurationProblem(NSRP)causedby
trafficvariability. Specifically,theauthorsreformulatedtheproblemasanMDPandthen
employedaDuelingDouble-DQN(DDQN)tosolveit,formingtheproposedIntelligentNS
ReconfigurationAlgorithm(INSRA).NumericalresultsillustratethatINSRAcanminimize
long-termresourceconsumptionandavoidunnecessaryreconfigurations. Yangetal.[79]
presentedanintent-drivenopticalnetworkarchitecturecombiningDRL-basedslicingpolicy
generationandreconfiguration. ThearchitectureusesaDDPGalgorithmforfine-grained
slicing strategies, including spectrum slicing, computing resource slicing, and storage
resource slicing, which impact network components such as blocking probability, load
balancing,anddelay. Intheevaluation,theauthorscomparetheirapproachtoDQNand
showthattheproposedmethodoutperformsDQNinlearningtime,blockingprobability,
andresourceutilization.
Thereconfigurationofthesliceparametersinsomeworksisbasedontheexchangeof
thenetworkstateinformationbetweentheInPsandthetenants. Ragoetal.[80]proposed
atenant-drivenRANsliceenforcementscheme,wherethesliceenforcementismadeby
theInPbasedontheoutcomeofaDDPGalgorithmthateachtenantisutilizingtocalculate
adaptivebandwidthrequestsforitsslices. Eachtenantisawareoftheoverallnetwork

Electronics2025,14,4053
21of38
statusasInPutilizesaDLscheme,whichisaconvolutionalautoencoder,tothecompress
networkstatusandshareitwithtenants. Similarly,inref.[81],theauthorsleveragedan
SAEthatencodesnetworkcontextualinformation,suchasSNRanddataloadpattern,in
ordertoexchangethisinformationbetweentheBaseBandUnits(BBUs)andtheRemote
RadioUnits(RRUs)inanopenRANscenario.
Besidesworksfocusedsolelyondecisionmakingoroptimizationtasks,someworks
jointlyaddressboth. Inref.[82],theauthorsexploredFog-RANslicinginascenariowitha
hotspotandVehicle-to-Infrastructure(V2I)sliceinstancesonaRANsegmentcomposedof
FogAccessPoints(F-APs)andRRUs. Specifically,theyproposedaDRL-basedapproachto
addresstheinterdependenceofcachingdecisionsandUEassociationsunderdynamiccon-
ditions. ExperimentalresultsshowedthattheproposedDRL-basedsolutionoutperforms
non-MLapproachesintermsofcachehitratioandcumulativereward.
Finally, the last task in this task group is classification, wherein ML methods are
applied to classify slices, use case scenarios, and traffic. Endes and Yuksekkaya [83]
proposeda5-layerNNtoclassifyusersbasedontheirservicerequirementsandassign
themtothemostsuitablenetworkslicetofulfilltheirneeds. Abbasetal.[84]employeda
K-meansclusteringalgorithmtoefficientlyplacethebasestationsingroups. Wuetal.[85]
proposedanAI-basedtrafficclassificationalgorithmthatclassifiesandallocatestrafficto
theappropriateslicebasedonthecurrentserviceandnetworkstate. Theauthorsused
severalMLmethodsintheirclassifierandshowedthatRFandGBDToutperformXGBoost
andKNNintermsofaccuracy.
Table6summarizestherelatedtasks,theallocation,theusecaseandnetworkdomain
types, the ML category, as well as the ML method proposed and whether or not that
methodwastestedforeachofthereferredworksintheDecisionMaking–Optimization–
Classificationgroup.
Table 6. Summary of works related to Decision Making–Optimization–Classification (SA: slice
activation, SPM: slice parameter modification, PREP: Performance Reporting, RCP: Resource
CapacityPlanning).
|     | Allocation UseCase | NetworkDo- | MLCat- | Simulations- |
| --- | ------------------ | ---------- | ------ | ------------ |
Ref. Task MLMethod
|     | Type Type | mainType | egory | Testbed |
| --- | --------- | -------- | ----- | ------- |
DCMAB,
| [65] SA | Dynamic Vertical | RAN | RL Thompson- | Yes |
| ------- | ---------------- | --- | ------------ | --- |
C
| [66] SA       | Dynamic Horizontal | RAN  | RL POMAB       | Yes |
| ------------- | ------------------ | ---- | -------------- | --- |
| [67] RCP      | Dynamic Vertical   | RAN  | SL CNN         | Yes |
| [68] RCP      | Dynamic Vertical   | RAN  | RL DQN         | Yes |
| [69] RCP      | Dynamic Vertical   | RAN  | RL DQN         | Yes |
| [70] RCP      | Dynamic Vertical   | RAN  | RL DNN         | Yes |
| [71] PREP,RCP | Static Vertical    | Core | SL MCEGCN      | Yes |
| [72] SPM,RCP  | Dynamic Vertical   | E2E  | RL CNN,LSTM    | Yes |
| [73] RCP      | Dynamic Vertical   | RAN  | RL DQN         | Yes |
| [74] SPM,PREP | Dynamic Vertical   | RAN  | RL LSTM        | Yes |
| [75] PREP,RCP | Dynamic Horizontal | Core | RL DDPG        | Yes |
| [76] RCP      | Dynamic Horizontal | Core | RL DRL         | Yes |
| [77] SPM,PREP | Dynamic Vertical   | RAN  | SL ANN         | Yes |
| [78] SPM      | Dynamic Vertical   | Core | RL DuelingDDQN | Yes |
| [79] RCP      | Dynamic Vertical   | Core | RL DDPG,DNEN   | Yes |
| PREP          |                    |      | SL DL          | Yes |
| [80]          | Dynamic Vertical   | RAN  |                |     |
| PREP,RCP      |                    |      | RL DDPG        | Yes |

Electronics2025,14,4053 22of38
Table6.Cont.
Allocation UseCase NetworkDo- MLCat- Simulations-
Ref. Task MLMethod
Type Type mainType egory Testbed
[81] PREP Dynamic Horizontal RAN UL SAE Yes
[82] SPM Dynamic Vertical RAN RL DQN Yes
[83] PREP Dynamic Vertical RAN SL ANN Yes
[84] PREP Dynamic Vertical Core UL k-Means Yes
[85] PREP Dynamic Vertical RAN SL RF+GBDT Yes
5.3.2. Monitoring-Prediction
ThisgroupinvolvesworksthatdealwithproblemsrelatedtothetasksofMonitoring
(MON)-Performance Reporting (PREP), and Resource Capacity Planning (RCP). All of
thefollowingworksproposetheapplicationofMLmethodsforpredictingdifferentslice-
relatedvalues.
Severalworksfocusontrafficpredictionandsliceselection. Thantharateetal.[67]
proposed an ML-based model that first leverages RF to predict the traffic load of each
slice,andbasedonthepredictionoutcome,aDLNNisappliedfortheassignmentdecision.
Songetal.[86]introducedtheML-basedtraffic-awaredynamicslicingframework. This
frameworkleveragesMLfortrafficpredictionandallocatesnetworkresourcesaccordingly
toreducedelayandblockingprobability,basedonathree-layerFFNN.
EnsuringtheSLAinsliceservicesisthefocalpointoftheworkinref.[87]. Specifically,
theauthorsproposedamethodforforecastingSLAviolationsinsliceservices. SLAbreach
predictionreliesonVNFbandwidthprediction,whichisperformedbyahybridmodel
combiningLSTMandARIMA,anon-ML-basedmodel.
Manystudiesfocusonpredictingfutureworkloadsandresourceneeds,helpingnet-
workoperatorsprepareinadvanceandavoidallocatingmoreresourcesthannecessary.
Camargo et al. [88] proposed two ML models, LSTM and RF, to forecast the expected
throughput of network slices. The results showed that RF outperformed LSTM, which
lackedgeneralization. Kafleetal.[89]adoptedtheLASSOregressionmodeltoperform
server workload predictions in a CN scenario. Bega et al. proposed two schemes: the
DeepCog[90],anML-basedslicecapacityforecastingscheme,designedtoenableantici-
patoryresourceallocation;andtheAZTEC[91],acapacityallocationframeworkwhich
effectivelyallocatescapacitytoindividualslices,usingamulti-timescaleforecastingmodel.
Specifically, DeepCog forecasts future capacity needs, minimizing resource overprovi-
sioning and SLA violations, using a 3D CNN for encoding and MLPs for decoding. In
contrast,theAZTECisimplementedbyDNNs,andmorespecificallywith3-Dimension
CNNs(3D-CNNs),whichallowdifferentslicestobeexaminedforpredictioninparallel,
astheyareveryefficientinextractingspatio-temporalfeatures. Theforecastingabilityof
thedifferentDNNs,whicharepartoftheAZTEC,wasinvestigated,andshowedthatthe
predictionsmadefollowthefluctuationsoftheslicetraffic.
SeveralworksexplorehowMLcanbeappliedtodeterminewhethernewflowscanbe
acceptedwithoutcompromisingQoS.Garridoetal.[60]presentedaContext-AwareTraffic
Predictor (CATP), and a Prediction-Based Admission Control (Pre-BAC), an admission
controlmechanismthatexploitsadvancedtime-seriesforecasting. Bothapproachesintend
tomakepredictions,andbothleverageMLmethodstodoso. Morespecifically,inPre-BAC,
RLwasused,whileinCATP,differentDNNversionswereused(LSTMs,3D-CNN,Spatio-
TemporalNN,andConvolutionalLSTM(ConvLSTM)).Buyakaretal.[92]employedthe
LSTMalgorithmtopredictfuturebandwidthrequirementsandMondrianRandomForests
(MRF)topredictE2Edelay. Thesepredictionsareintegratedintotheiradmissioncontrol
algorithmtodeterminewhetheraflowwithspecificQoSrequirementscanbeadmitted

Electronics2025,14,4053 23of38
withoutviolatingtheQoSofalreadyadmittedflows. Yanetal.[93]proposedanintelligent
ResourceSchedulingStrategy(iRSS)combiningDLandRLtomanagenetworkandtraffic
dynamics. TheiRSSperformsperiodictrafficpredictionsinalargetime-scaleusingLSTM
andthepredicteddataareusedtoperformresourceallocations. Intheirevaluation,the
authorsdemonstratedthatLSTMachievesaccuratetrafficpredictions. Tayyabaetal.[94]
proposedapolicyframeworkforoptimizedresourceallocationinSDN-based5Gcellular
networks that consists of several modules, including an adaptive policy generator, a
resourcemanager,atrafficscheduler,andatrafficclassifier. Inthetrafficclassifiermodule,
theauthorsemployLSTM,CNN,andDNNmethodsfortrafficpredictionandevaluate
theirdetectionaccuracy. LSTMachievedthehighestaccuracy,followednextbyCNN,with
DNNshowingthelowestaccuracy. Monteiletal.[95]presentedasolutionfordetermining
theoptimalresourcereservationforaserviceproviderbasedonDNNandLSTMmethods.
TheauthorscomparedtheirframeworkwiththebaselineARIMApredictionmodeland
found that DNN and LSTM performed better, as they captured the daily and seasonal
trendsofthedata.
Specialattentionhasbeengiventovehicularandmobilenetworksduetodynamic
trafficpatterns. Cuietal.[96]aimedtooptimizesliceweightsandreducedelay. Fortraffic
prediction, they used ConvLSTM, combining CNN and LSTM, to model the temporal-
spatialdependenciesofsliceservicetraffic. Performanceevaluationsshowedthattheir
predictiveapproachsignificantlyreducessliceresourceallocationdelaycomparedtoanon-
predictiveapproach.Cuietal.,inlaterstudies[97,98],proposedLSTM-DDPG,analgorithm
thatusesLSTMtopredictlong-termtrafficdemandbyextractingtemporalcorrelationsin
datasequences,andDDPGforfine-grainedresourcescheduling,outperformingtraditional
ARIMAmodels. Khanetal.[99]focusedonjointresourceallocationforURLLCandeMMB
slicesinvehicularnetworks,andusedDNNtoestimateChannelStateInformation(CSI),
achievingbetterresourceallocationwithoutexcessivesignaling.
Other works also present specialized prediction models to reduce complexity or
overhead. Sapavath et al. [100] proposed a Sparse Bayesian Linear Regression (SBLR)
algorithm for predicting CSI in large-scale multi-input–multi output (MIMO) wireless
networks,achievingbetterpredictionaccuracywhileavoidingtheoverfittingandhigh
complexityassociatedwithneuralnetworks. Matoussietal.[101]introducedareal-time
user-centricRANslicingschemeforCRAN-basedapplications,whichaimstomaximize
userthroughputandminimizedeploymentcostbyoptimizingresourceallocation,and
usingaBiLSTM-basedDNN.Finally,Jiangetal.[102]presentedaframeworkintegrating
AIforintelligenttasksinNS.Twousecaseswereexamined: MIMOchannelpredictionand
securityanomalydetection. Inthefirstusecase,athree-layerRNNwasusedtopredict
fadingchannels,improvingthetransmissionantennaselection. Inthesecond,RFandSVM
wereutilizedtodetectsecuritythreatsinindustrialnetworks,withhighdetectionaccuracy
ratesachieved.
Researchersarealsofrequentlyinterestedinslicebrokeringandorchestration. Gutter-
manetal.[103]proposedashort-time-scalepredictionmodelforRANslicebrokers,called
X-LSTM.ThemodelisamodificationofLSTMinspiredbyARIMAandtheX-11statistical
method. TheirsimulationsshowedthatX-LSTMoutperformsARIMAandstandardLSTM
in terms of prediction accuracy, resulting in lower slice costs. Sciancalepore et al. [104]
introducedaReinforcementLearning-based5GNetworkSliceBroker(RL-NSB)framework,
forassistingNSBsinassociatingSLArequirementswithphysicalresourcesthatincludesa
trafficforecastingmodule,anadmissioncontrolalgorithm,andaslicescheduler. Similarly,
Abbasetal.[84]proposedaframeworkformulti-domainsliceresourceorchestrationthat
usesLSTMtopredictresourceutilization(CPU,RAM,storage)andthroughputforVNF

Electronics2025,14,4053
24of38
runningonCNslices. ItalsoemploysK-meansclusteringtoprocessthepredicteddataset
anddeterminewhetherreconfigurationisneeded.
Moreover,inter-slicebalanceandfairnessareanotherresearchdirection.Silvaetal.[105]
evaluatedSVM,ANN,andkNNforpredictingQoSdegradation,withSVMachievingthe
bestperformance. Bouzidietal.[106]integratedLSTMandLogisticRegression(LR)to
predictcongestionandsupportproactivesliceadaptationsinanSDN-basedarchitecture.
Finally,Thantharateetal.[107]presentedADAPTIVE6G,anadaptivelearningframework
forresourcemanagementandloadpredictioninNSapplicationsforB5Gand6Gsystems.
ADAPTIVE6G aims to improve network load estimation, promoting fairer and more
uniform resource management. The authors combined DL and TL for load prediction
across different slices and demonstrated that their framework outperforms traditional
DNNapproachesintheirexperimentalresults.
Table7summarizestherelatedtasks,theallocation,theusecaseandnetworkdomain
types, the ML category, as well as the ML method proposed, and whether or not that
methodwastestedforeachofthereferredworksinthemonitoring–predictiontaskgroup.
Table7. Summaryofworksrelatedtomonitoring–prediction(MON:Monitoring,RCP:Resource
CapacityPlanning,SPC:SliceParameterClassification).
|     | Allocation | UseCase NetworkDo- | MLCat- | Simulations- |
| --- | ---------- | ------------------ | ------ | ------------ |
Ref. Task MLMethod
|              | Type    | Type mainType  | egory   | Testbed |
| ------------ | ------- | -------------- | ------- | ------- |
| [60] RCP,SPC | Dynamic | Vertical RAN   | SL DNN  | No      |
| [67] MON,RCP | Dynamic | Vertical RAN   | SL DLNN | Yes     |
| [84] MON,RCP | Dynamic | Vertical Core  | RL LSTM | Yes     |
| [86] MON,RCP | Dynamic | Vertical Core  | SL FFNN | Yes     |
| [87] MON,RCP | Dynamic | Horizontal RAN | RL LSTM | Yes     |
SL RF
| [88] MON,RCP | Dynamic | Vertical RAN |     | Yes |
| ------------ | ------- | ------------ | --- | --- |
RL LSTM
| [89] MON,RCP | Dynamic | Horizontal Core | SL Lasso | Yes |
| ------------ | ------- | --------------- | -------- | --- |
3D-CNN,
| [90] MON,RCP | Dynamic | Horizontal E2E | SL  |     |
| ------------ | ------- | -------------- | --- | --- |
MLP
| [91] MON,RCP | Dynamic | Vertical E2E | SL DNN | Yes |
| ------------ | ------- | ------------ | ------ | --- |
SL MRF
| [92] MON,RCP | Dynamic | Vertical Core |     | Yes |
| ------------ | ------- | ------------- | --- | --- |
RL LSTM
| [93] MON,RCP | Dynamic | Vertical RAN | RL LSTM | Yes |
| ------------ | ------- | ------------ | ------- | --- |
LSTM, CNN,
| [94] MON,RCP | Dynamic | Vertical RAN | RL  | Yes |
| ------------ | ------- | ------------ | --- | --- |
DNN
| [95] RCP,SPC  | Dynamic | Vertical RAN   | RL LSTM,DNN | Yes |
| ------------- | ------- | -------------- | ----------- | --- |
| [96] MON,RCP  | Dynamic | Horizontal RAN | RL ConvLSTM | Yes |
| [97] MON,RCP  | Dynamic | Horizontal RAN | RL LSTM     | Yes |
| [98] MON,RCP  | Dynamic | Horizontal RAN | RL LSTM     | Yes |
| [99] MON,RCP  | Dynamic | Horizontal RAN | RL DNN      | Yes |
| [100] MON,RCP | Dynamic | Vertical RAN   | SL SBLR,SVM | Yes |
| [101] RCP,SPC | Dynamic | Verical RAN    | RL BiLSTM   | Yes |
| MON,RCP       |         | RAN            | RL RNN      | Yes |
| [102]         | Static  | Vertical       |             |     |
| MON           |         | Core           | SL RF,SVM   | No  |
| [103] MON,RCP | Dynamic | Vertical RAN   | RL X-LSTM   | Yes |
| [104] MON,RCP | Dynamic | Vertical RAN   | UL EM       | Yes |

Electronics2025,14,4053 25of38
Table7.Cont.
Allocation UseCase NetworkDo- MLCat- Simulations-
Ref. Task MLMethod
Type Type mainType egory Testbed
ANN, kNN,
[105] MON,RCP Dynamic Horizontal RAN SL Yes
SVM
[106] MON,RCP Static Vertical Core RL LSTM Yes
Transfer
[107] MON,RCP Dynamic Vertical RAN SL Learning Yes
DNN
5.3.3. ResourceAllocation
Thisgroupincludesworksfocusedonresourceallocation,specificallyaddressingthe
tasksofPerformanceReporting(PREP),whichreliesonsliceperformanceobservations,
andsliceparametermodification(SPM),aimedatreconfiguringspecificresourceallocation
parameterstoenhancesliceperformance.
Someworkslookatdistributedandcollaborativeresourcemanagement,wheredifferent
networkstakeholders—likeMVNOs,infrastructureproviders,andcloudproviders—work
together.Forexample,Huetal.[108]proposedafederatedslicingapproachusingblockchain
andRL,helpingallpartiesmakefairandefficientallocationdecisions.Lietal.[109]tooka
morecentralizedapproach,applyingDQLtobettermatchresourcesupplywithuserdemand
inboththeRANandthecorenetwork.Cuietal.[97,98]extendedthisbyfocusingonvehicular
networks,combiningLSTMandDDPGtopredictlong-termtrafficandadjustresourcesin
realtime;anapproachthatshowedastrongperformanceinmaintainingQoS.
Otherresearchershaveturnedtomulti-agentorhybridlearningmethodstohandle
morecomplexscenarios. Wangetal.[110]combinedamulti-agentRLalgorithmwithan
RFclassifiertoallocatebothradioandcorenetworkresourcesinnetworksthatinclude
public and private slices. Moon et al. [111] presented a smart ensemble method that
blendsfast-learningwithhigh-performancealgorithmstoimproveRANslicing. Similarly,
Huaetal.[112]introducedGenerativeAdversarialNetwork-poweredDeepDistributional
Q Network (GAN-DDQN) for better spectrum sharing and SLA satisfaction, whereas
Chenetal.[113]addresseddualconnectivityscenariosusinganLSTM-enhancedDQNto
balanceQoE,throughput,andenergyuse. Shomeetal.[69]proposedaDRL-basedslice
selectionandbandwidthallocationapproach,whichconsidersmulti-slice-connectedUEs
andmultipleDQNagentsthatdecidethebandwidthallocationtotheUEs.
Anumberofstudiesfocusondemand-awareorspectrum-sensitiveresourcetuning.
Mengetal.[114]usedDRLtooptimizebandwidthallocationinsmartgridnetworks,while
Shi et al. [115] accounted for radar systems coexisting with 5G users in their spectrum
allocationmodel. Albondaetal.[116]lookedathowtobalanceresourcesbetweeneMBB
andV2Xslices,combiningQ-learningwithheuristicrulesforbetterQoS.Nourietal. [117]
workedonthejointallocationofpowerandPhysicalResourceBlocks(PRBs)totheUEs
whileensuringQoSrequirementsandleveragedaSemi-Supervisedlearningapproach,
whichcombinesaVAEwithcontrastiveloss,namedSS-VAE,inorderoptimizetheoverall
networkutility.
Whenitcomestodealingwithinterferenceandslice-specificneeds,researchers,like
Zambiancoetal.[118],haveappliedDQNtohandlemixednumerologyissues,reducing
interference while maintaining slice capacity. Shao et al. [119] designed a multi-agent
systemwithGraphAttentionNetworkstomanageresourcesharingindensenetworks.
Cherguietal.[120]focusedonmakingsurethatRANresourceallocationdecisionsalso
respectoperatorcostconstraintsbyusingneuralnetworkstrainedonKPIdata.
Someworksexploreresourcecontrolunderconstraintsorinreal-timeenvironments.
Xuetal.[121]introducedaconstrainedversionoftheSACalgorithmtodealwithenergy

Electronics2025,14,4053 26of38
anddelayconstraints.Liuetal.[122]usedasimilarideawithaconstrainedMDPmodeland
Interior-PointPolicyOptimization(IPPO)toallocatebandwidthwhileconsideringlatency.
Chenetal.[123]usedmulti-agentDQNstooptimizeresourceallocationacrossslicesand
tenants,showingnoticeableimprovementsinperformancemetrics. Yanetal.[93],intheir
proposediRSS,combinedlargetime-scalepredictionsacquiredbyLSTMandA3Cinorder
toperformshort-termresourcescheduling. Intheirevaluation,theauthorsdemonstrated
thatA3Coutperformsstate-of-the-artmethodssuchasQL,AC,andaheuristicresource
schedulingalgorithmintermsofcumulativerewardandresourceutilization.
There is also a wide range of work focused on vehicular and edge networks. Sun
etal.[124]proposedaDRL-basedresourcecontrollerforD2Dvehiclecommunications,
whileYuetal.[125]presentedatwo-stagebandwidthallocationmodelusingDDPGfor
V2X. Li et al. [126] built an E2E framework that coordinates resource allocation across
theRANandCore,improvinguseraccess. Akyildizetal.[127]introducedahierarchical
multi-agentsystemtomanageresourcesharingbetweenURLLCandeMBBslices. Zhou
etal.[128]followedasimilarapproachusingcooperativeQ-learningtoallocateresources
fairlybetweencompetingslices.
In contrast, several works tackle resource allocation at the link level or in energy-
efficientways. Wangetal.[129]proposedaGCN-basedsolutioncalledLinkSliceforbetter
PRBscheduling.Lietal.[130]showedhowcombiningLSTMwithA2Cleadstobetterband-
widthallocation,especiallyinbalancingspectralefficiencywithSLAcompliance. Alcaraz
et al. [131] focused on resource-constrained environments and proposed a lightweight,
kernel-basedRLmethodthatoffersstrongperformancewithoutexcessivecomputation.
Movingbeyondallocation,someresearchersalsoaddressdevice-to-sliceassignment
andmulti-domainorchestration. Dangietal.[132]usedahybridCNN–BiLSTMmodel
toclassifytrafficfromunknowndevicesandassignittothebest-fitslice. Laietal.[133]
presented a DRL model for optimizing multi-resource allocation across UEs, the edge,
andthecloud. Elmosilhyetal.[134]combinedregretlearningandQ-learningtomanage
userassociationinmulti-RATnetworks,whileBoutibaetal.[135]tackledinterferenceand
performanceissuesin5GnewradiowithmixednumerologyusingaDQN-basedscheduler.
Afewmoreworksfocusonend-to-endoptimizationunderuncertainty. Liuetal.[136]
proposedatwo-levelsystem(TORCHandASSAIL)thatusesDQNtocoordinatebetween
theRANandcore.Gharehgolietal.[137]addresseduncertaintrafficandchannelconditions
usingrecurrentpolicygradientmethods. Meietal.[138]appliedactor–criticLSTMina
partiallyobservablesettingtoimproveVehicle-to-Vehicle(V2V)slicing.
Lastly, several newer approaches bring federated learning, edge intelligence, and
energy-awarenessintothepicture. Cherguietal.[139]usedafederatedlearningmodel
todynamicallyallocateresourcesinB5GCRANs,significantlyreducingSLAviolations.
Raftopoulos et al. [140] developed a DRL-based agent for the O-RAN RAN intelligent
controllerstofine-tuneslicingpolicieswhileminimizingPRBuse. Alkhouryetal.[141]
addressedMECresourceallocationusingDQNtoimproverequestacceptanceindense
urban environments. Ayala et al. [81] designed a contextual bandit-based controller to
managebothcomputingandradioresourcesinvirtual-RAN,showingadaptabilityeven
underconstrainedCPUresources.
Table8summarizestheallocation,theusecaseandnetworkdomaintypes,theML
category,aswellastheMLmethodproposedandwhetherornotthatmethodwastested
foreachofthereferredworksintheResourceAllocationtaskgroup. Therelatedtasksof
allthereferredworksarethePREPandSPM.Thus,forconvenience,thisinformationisnot
includedinthistable.

Electronics2025,14,4053
27of38
Table8.SummaryofworksrelatedtoResourceAllocation.
| Allocation    | Use Case   | Network    | ML Cate- |          | Simulations- |
| ------------- | ---------- | ---------- | -------- | -------- | ------------ |
| Ref.          |            |            |          | MLMethod |              |
| Type          | Type       | DomainType | gory     |          | Testbed      |
| [69] Dynamic  | Vertical   | RAN        | RL       | DQN      | Yes          |
|               |            |            | SL       | ANN      |              |
| [81] Dynamic  | Horizontal | RAN        |          |          | Yes          |
|               |            |            | RL       | DDPG     |              |
| [93] Dynamic  | Vertical   | RAN        | RL       | A3C      | Yes          |
| [97] Dynamic  | Horizontal | RAN        | RL       | DDPG     | Yes          |
| [98] Dynamic  | Horizontal | RAN        | RL       | DDPG     | Yes          |
| [108] Dynamic | Horizontal | RAN        | RL       | RL+MDP   | Yes          |
| [109] Dynamic | Horizontal | E2E        | RL       | DQL      | Yes          |
|               |            |            | SL       | RF       |              |
| [110] Dynamic | Horizontal | RAN        |          |          | Yes          |
|               |            |            | RL       | IPPO     |              |
| [111] Dynamic | Horizontal | RAN        | RL       | DRL      | Yes          |
GAN-DDQN,Duel-
| [112] Dynamic | Horizontal | RAN | RL  | ingGAN-DDQN | Yes |
| ------------- | ---------- | --- | --- | ----------- | --- |
| [113] Dynamic | Vertical   | RAN | RL  | LSTM-D3QN   | Yes |
| [114] Dynamic | Horizontal | RAN | RL  | DQL,DDQL    | Yes |
| [115] Dynamic | Vertical   | RAN | RL  | QL          | Yes |
| [116] Dynamic | Horizontal | RAN | RL  | QL          | Yes |
| [117] Dynamic | Horizontal | RAN | SSL | VAE         | Ye  |
| [118] Dynamic | Horizontal | RAN | RL  | DQN         | Yes |
DDQN, Dueling
| [119] Dynamic | Horizontal | RAN | RL  |     | Yes |
| ------------- | ---------- | --- | --- | --- | --- |
DQN,A2C
| [120] Dynamic | Vertical   | RAN     | RL  | DNN               | Yes |
| ------------- | ---------- | ------- | --- | ----------------- | --- |
| [121] Dynamic | Horizontal | RAN     | RL  | CDC-SAC           | Yes |
| [122] Dynamic | Horizontal | RAN     | RL  | IPO               | Yes |
| [123] Dynamic | Vertical   | RAN     | RL  | DoubleDQN         | Yes |
| [124] Dynamic | Vertical   | RAN     | RL  | DQN               | Yes |
| [125] Dynamic | Horizontal | RAN     | RL  | DDPG              | Yes |
| [126] Dynamic | Horizontal | E2E     | RL  | DQN               | Yes |
| [127] Dynamic | Horizontal | RAN     | RL  | DQN               | Yes |
| [128] Dynamic | Horizontal | RAN     | RL  | CorrelatedQL      | Yes |
| [129] Dynamic | Vertical   | RAN     | RL  | DRL,GCN           | Yes |
| [130] Dynamic | Horizontal | RAN     | RL  | LSTM,A2C          | Yes |
| [131] Dynamic | Horizontal | RAN     | RL  | KBRL              | Yes |
| [132] N/A     | N/A        | Core    | RL  | CNN,BiLSTM        | Yes |
| [133] Dynamic | Vertical   | E2E     | RL  | DRL               | Yes |
| [134] Dynamic | Horizontal | RAN     | RL  | QL                | Yes |
| [135] Dynamic | Horizontal | RAN     | RL  | DQN               | Yes |
| [136] Dynamic | Horizontal | E2E     | RL  | DQN               | Yes |
| [137] Dynamic | Horizontal | E2E     | RL  | RDPG,DDPG,SAC     | Yes |
| [138] Dynamic | Vertical   | RAN     | RL  | AC-LSTM           | Yes |
| [139] Dynamic | Horizontal | RAN     | RL  | FederatedLearning | Yes |
| [140] Dynamic | Horizontal | RAN     | RL  | PPO               | Yes |
| [141] Dynamic | Horizontal | RAN-MEC | RL  | DQN               | Yes |

Electronics2025,14,4053 28of38
6. Discussion
NS is an arrow in the quiver of InPs that allows them to slice their networks into
multipleslicesandleasethoseslicestotenants,sothatthelattercanprovidedifferentiated
services. Naturally,theimplementationofNShas,overtheyears,embracedtheadoption
ofvariousAIandMLtechniquestotackledifferentproblemsthatariseinthedifferent
life-cyclephasesofanetworkslice.
ThemainobjectiveofthissurveypaperwastopresenttheapplicationsofMLmethods
thathavebeenproposedintheliteratureassolutionstovariousproblemsrelatedtoNS.
Theextendedsearchthatwasconductedandpresentedintheprevioussectionsrevealsthat
MLmethodsarewidelyfavoredforperformingtasksthatarecriticaltothedeployment
andoperationofnetworkslices.
Inthissection,wewillsummarizethefindingsthatderivefromthepresentedsearch
regardingthenetworkdomainandslicingtypesadopted,theproposedMLmethodsand
theirefficiency,thecategoriesthesemethodsfallinto,thetasksthesemethodsareproposed
forandthelife-cyclephasesthesetasksarerelatedto.
6.1. NetworkDomainsandSlicingTypes
FollowingthedetailedanalysisofMLapplicationsacrossvariousnetworkslicelife-
cyclephasespresentedinSection5,wenowsynthesizehowthesemethodsalignwiththe
multi-dimensionalnetworkslicetaxonomyarticulatedpreviouslyinSection3.2. Specif-
ically,wefocusonMLimplementationvariabilityacrossthedifferentslicingtypesand
deploymentdomains,asshowninTable9,whichdirectlyconditionstheselection,effec-
tiveness,andchallengesofMLapproachesemployedforslicemanagementandoptimiza-
tion[142]. Inpractice,theapplicabilityofMLineachslicingtypedependsonhowdatais
collected(viamonitoringinterfacesandtelemetry),whichfeaturesareextracted(e.g.,traffic
load,mobility,QoSindicators),andhowAIoutputsareenforced(e.g.,viaorchestrationor
controlplaneNFs).
Staticallocationenvironmentsassignfixedresourcesforextendeddurations. These
scenarioslackreal-timeadaptivitybutdemandrobustofflineprofilingandplanning.Hence,
inthesesettings,SL-andUL-basedtechniquessuchasSVM,RF,andK-meansclustering
arecommonlyappliedtopredicttrafficdistributionsandguideCapacityPlanning.Notably,
suchstaticmodelsoftenfailtoaddresstemporalfluctuationsorsuddendemandbursts. In
contrast,dynamicallocationmandatesongoing,low-latencyslicereconfigurationunder
unpredictable traffic and user behavior, accommodating in this way the need for the
frequentadjustmentofresourcesbasedonfluctuatingservicedemands. RLanditsdeep
variants,includingQ-Learning,DQN,DDPG,andPPO,facilitateandoptimizecontinuous
admissioncontrol,resourcescheduling,andpolicyfulfillmentinsuchvolatilecontexts.
These adaptive algorithms enable continuous learning and decision making to balance
resourceutilizationagainstQoSinnearreal-time,althoughthenon-stationarybehaviorof
networkconditionsposeschallengestoconvergenceandstability.
Within vertical slicing, domain-specific requirements demand sophisticated slice-
specificMLstrategies,tailoredtohandleheterogeneousKPIs(e.g.,latency,reliability,and
security)andmeetstringentSLAsacrossdiverseindustrieslikeindustrialIoT,vehicular
communication,andeMBB.HybridSL-RLmodels,alongsiderecurrentarchitecturesand
neuralnetworkssuchasLSTM,haveprovenadeptataddressingthesecomplexrequire-
mentsandofferingadaptivecontrol. Forhorizontalslicing,ontheotherhand,theprimary
focusisonjudiciallybalancingtheresourcesamongmultipletenantswithvaryingand
often competing demands. To this end, frameworks combining clustering algorithms,
ensemblelearning,andmulti-agentreinforcementlearningfacilitateequitableresource

Electronics2025,14,4053
29of38
distribution, ensuringfairnesswithoutsacrificingresourceefficiency. Suchapproaches
supportmulti-tenantdynamismandpreemptresourcecontention.
Table9.NetworkslicetaxonomyversusMLapproaches.
| SlicingType/Domain | TypicalDeploymentChallenges |     |     | MLMethods |     |
| ------------------ | --------------------------- | --- | --- | --------- | --- |
Resourcerigidityleadstounderutilizationduringvari-
|     | abledemandandlimitsadaptability;requiresrobust |     |     | SL (SVM, | RF), UL (K- |
| --- | ---------------------------------------------- | --- | --- | -------- | ----------- |
StaticAllocation
|     | service profiling, | reliable upfront | segmentation, | and means) |     |
| --- | ------------------ | ---------------- | ------------- | ---------- | --- |
predictiveplanning.
Real-timeadaptationanddecisionmakingundernon-
|     | stationaryenvironmentsandadherencetoalteringtraf- |     |     | RL (Q-Learning, | DQN, |
| --- | ------------------------------------------------- | --- | --- | --------------- | ---- |
DynamicAllocation
|     | ficandSLAdemands;requirespolicystabilityandfast |     |     | DDPG),DRL |     |
| --- | ----------------------------------------------- | --- | --- | --------- | --- |
convergenceinvolatileconditions.
HeterogeneousKPIsacrossindustriesandstrictSLAs
|     | demandtailored, | fine-grained, | andinterpretableML | RL, Hybrid | SL-RL, |
| --- | --------------- | ------------- | ------------------ | ---------- | ------ |
VerticalSlicing
|     | models;needforaccuratepredictionandresourceallo- |     |     | LSTM |     |
| --- | ------------------------------------------------ | --- | --- | ---- | --- |
cationwhilemaintainingQoS.
Maintainingfairnessandefficiencyacrossdiverse,co-
|     | existingtenantswithconflictingrequirements;needfor |     |     | UL (Clustering), | Multi- |
| --- | -------------------------------------------------- | --- | --- | ---------------- | ------ |
HorizontalSlicing
|     | dynamic | and judicial load | balancing while | avoiding agentRL,EnsembleML |     |
| --- | ------- | ----------------- | --------------- | --------------------------- | --- |
resourcestarvation.
Highvariabilityandlatency-criticalconstraints;require-
|           |                                                    |     |     | DRL | (multi-agent), |
| --------- | -------------------------------------------------- | --- | --- | --- | -------------- |
| RANDomain | mentsfordistributed,fast-adaptingmulti-agentlearn- |     |     |     |                |
DQN,LSTM-RL
ingforresourcemanagementandresiliencetovolatility.
Complexfunctionplacementandinter-sliceandVNF
|     | dependenciesinrelativelystablebutinterdependent |     |     | SL/UL,RL(GCN,DNN, |     |
| --- | ----------------------------------------------- | --- | --- | ----------------- | --- |
CoreDomain
|     | workloads;requirementforefficientorchestrationthat |     |     | A3C) |     |
| --- | -------------------------------------------------- | --- | --- | ---- | --- |
utilizesgraphandactor–criticRLframeworks.
|     | Concerns        | on the coordination, | privacy preservation, |                 |            |
| --- | --------------- | -------------------- | --------------------- | --------------- | ---------- |
|     | and scalability | across domains       | and operators;        | re- Distributed | RL, feder- |
E2ESlicing
|     | quirement | for multi-agent | distributed and federated | atedML,multi-agentRL |     |
| --- | --------- | --------------- | ------------------------- | -------------------- | --- |
learningapproaches.
Atthedomainlevel,RANslicingfaceshighlyvariablechannelconditionsandstrin-
gentlatencyrequirements, favoringfast-adapting, multi-agentDRLapproachesfordy-
namicspectrummanagementandcongestioncontrol. Meanwhile,therelativelystablebut
complexinterdependenciesofthecorenetworkbenefitfromgraph-basedreinforcement
learning(e.g.,GNNs),DNNs,andactor–criticmethodsforscheduling,VNFplacement,
andorchestrationoverrelativelystabledemandpatterns. Onthecontrary,theE2Eslicing
paradigm requires collaborative coordination among multiple administrative domains,
necessitatingprivacy-awareandscalablelearningAImodels,suchasdistributedreinforce-
mentlearningandfederatedlearning,toorchestrateresourcesacrossbothadministrative
andtechnologicaldomains.
6.2. MethodCategories
StartingfromtheMLcategories,whichwerepresentedinSection4,itcanbenoted
thattheproposedMLmethodsspanallfourMLcategories,butnotequally. SSListheleast
popularcategory,asonlyoneapproachproposesamethodthatbelongstothiscategory.
Conversely,aconsiderablenumberofapproachesproposeUL-basedmethodsmainlyfor
dataclustering,butthisnumberislessthantherespectiveSL-basedapproaches,whichare
significantlymoreandareproposedmainlyforclusteringandprediction. TheMLcategory
thatcanbecharacterizedasthemostpopularisRL,encapsulatingthehighestnumberof
proposedapproaches,andbeingusedmainlyfordecisionmaking,admissioncontrol,and
resourceallocation. Nevertheless,nosinglecategorycanberegardedasapanacea.

Electronics2025,14,4053 30of38
6.3. MethodEfficiencyandEvaluation
Theefficiencyoftheproposedmethodsisanotherissuethatneedstobenoted. As
mentionedearlier,SL-andRL-basedmethodshavebeenproposedmorethanothers,but
this does not mean that any method belonging to these categories is equally effective
whenappliedtoanygiventask. Infact,allproposedmethodshavebothadvantagesand
disadvantages, as one that is effective in performing a specific task can be, in parallel,
ineffectiveinaccomplishinganotherone.
Moreover, the proposed methods are mostly evaluated through simulations with
synthetic data, which limits their practical reliability. Hence, real-world performance
evaluationiscrucialforensuringcommercialacceptanceandeffectivedeployment.
For instance, in ref. [67], RF, which is an SL-based method, is preferred over other
SL-basedmethods,suchasKNN,NaiveBayes, orDecisionTree, duetothenatureand
amountofdatathatthedatasetoftheoptimizationproblemconsistsof. Anothercaseis
ref.[39],statingthatQL,whichisanRL-basedmethod,hasacomputationalcomplexity
lowenoughtoallowitsexecutioninanonlinelearningfashion. However,sinceQLutilizes
Q-tablesasalearningmechanism,thesetablesmay,inthecaseofsliceadmissioncontrol,
endupbeingtoolarge,hencebecomingmemory-intensiveindenseapplicationscenarios.
Accordingtoref.[15],asQLsuffersfromthecurseofdimensionality,itisonlysuitablefor
RANslicingproblemsinsmall-scalenetworksandnotassuitableforadmissioncontrol.
Furthermore,ref. [35]statesthatDRLapproachescaninteractwiththelargesetofvariables
thatcharacterizesuchasystem,anddeterminethebestadmissiondecisionaccordingtoa
specifictarget. ThisiswhyDRL-basedmethodsrepresentthemajorityoftheproposedML
methodsforNS.
6.4. Life-CyclePhasesandTasks
Regardingthelife-cyclephases,wecandeducethattheapplicationofMLmethods
hasbeenproposedforthreeoutofthefourphasesoftheslicelife-cycle. Morespecifically,
theseincludethePreparation,Commissioning,andOperationphases,butnottheDecom-
missioningphase. Thisistobeexpected,astheonlytaskthatfallsunderthisphase,i.e.,the
releaseofthereservedresources,doesnotrequireanyadvancedcomputationordecision
makingtobeperformed,sotheelaborationofMLtechniquesforthistaskhasnotbeen
consideredyet.
Starting from the Preparation phase, ML methods have been mainly proposed for
performingtheNEPtask,asthisisthetaskrelatedtoadmissioncontrol,oneofthekey
processesofthisphase. Mostoftheproposedapproachesconsideradynamicallocation
type of slicing and a vertical use case type. As for the network domain, most of the
approaches are for RAN applications, followed by E2E, and lastly by Core. The most
popularmethodsofthisphaseareRL-based,suchasDRLandDQL.
Commissioningisthephasethat,ingeneral,hastheleastnumberofproposedML
applications,comparedtotheothers. AlmostalltheproposedMLapplicationsarerelated
totheRIACtask,whichisalsothemaintaskofthisphase. Alltheproposedapproaches
consideradynamicallocationtypeofslicing,andthemajorityofthemconsideravertical
usecasetype. RANisthenetworkdomaininwhichmostoftheapproachesareappliedto,
thencomesE2E,followedbyCore. Themostpopularmethodsofthisphaseareagainthe
RL-based,oneofwhichisDDPG.
Finally,theOperationphaseistheonethathasattractedthemostattentionfromthe
research community for applying ML methods to its related tasks. As a result, a large
number of research approaches propose the application of ML to address problems or
performtasksthatresideintheOperationphase. This,however,isexpectedsincethese

Electronics2025,14,4053 31of38
taskshavethegreatestimpactontheperformanceandeffectivenessofNS,andrequire
complexreal-timecomputations.
Duetothesheervolumeofresearchworksinthisphase,wegroupedandanalyzed
theworksbybroadertaskcategories;therefore,wewilldiscussthefindingsforeachgroup
separately. StartingfromtheDecisionMaking-Optimization–Classificationgroup,theRCP
taskistheonethathasthehighestnumberofproposedapplications,asitisrelatedtoslice
selection,averyimportantprocessthathastobeperformedintheoperationphase. Nearly
alltheproposedworksarebasedondynamicallocation, whiletheusecasetypeinthe
majorityofthemisvertical. MostofthemareappliedfortheRANdomain,thenforthe
Core,andlastlyfortheE2E.RLisagainthefavoriteMLcategory,withDQNbeingthe
mostproposedmethodinthisgroup.
The RCP and MON tasks are the ones that almost all studies in the Monitoring-
Predictiongrouparerelatedto. Thishappensbecausetheinformationofthecurrentslice
status, in terms of capacity and other KPIs, is mandatory for maintaining its efficiency
and performing predictions. In this group, almost all approaches consider dynamic al-
location,mostofwhichareaboutverticalusecasesandRANdomainapplications. The
proposedMLmethodsare,intheirmajority,NNsthatfallintomainlyRL-basedandalso
SL-basedcategories. Inparticular,DNNandLSTMarethemethodsthathavebeenmost
widelyproposed.
Thelastgroup,termedResourceAllocation,istheonewiththehighestnumberof
proposedworks. AlltheworksinthisgrouppresentedMLmethodsforperformingthe
PREP and SPM tasks. Moreover, all of them leverage a dynamic allocation type. This
isbecausethecommonobjectiveoftheseworksistoreconfiguretheresourceallocation
inadynamicmannertomaintainahighsliceperformance. Mostoftheworksconsider
horizontalusecasesandareappliedintheRANdomain. Inthiscase,RL-basedmethods
arebyfarthemostproposedovertheothers,withDQNbeingthefavoriteone.
7. Conclusions
WiththeadoptionofNS,future5GandB5Gnetworksarepoisedtodeliveravarietyof
servicetypes—rangingfromeMBBtoURLLCandmMTC—eachwithdiverseandstringent
performancerequirements. Bycreatingandoperatingmultiplelogicalnetworks,orslices,
overasharedinfrastructure,thesenetworkscanflexiblycatertoheterogeneoususerneeds.
Thiscapabilityisincreasinglybecomingarealitythankstotheadventofsoftwarization
andvirtualizationtechnologiessuchasSDN,NFV,andcloud/edgecomputing. Despite
thesetechnologicaladvancements,themanagementoftasksrelatedtoslicecreationand
operationposessignificantchallengesduetotheneedforthereal-timeanalysisoflarge
volumesofcomplexdataanddecision-makingprocessestomeetthedesiredQoStargets.To
addressthesechallengesandautomateslicelife-cyclemanagement,AIandmorespecifically
MLhaveemergedascriticalenablers.
ThispaperpresentedacomprehensivesurveyofMLapplicationsacrossthevarious
tasks characterizing the different phases of the NS life-cycle within the transformative
B5Glandscape. Foreachexaminedwork,weelaboratedontheproblemaddressed,the
specificslicingapproachemployed—consideringallocationtype,usecase,andnetwork
domain—andtheassociatedAI/MLmethodologies. Furthermore,weintroducedatax-
onomy organizing the diverse tasks across the life-cycle phases and matched them to
relevantMLtechniquesdevisedtoaddresstherespectivechallenges. Thesurveyrevealed
apredominantfocusonUL-,SL-,andRL-basedtechniques,withRLbeingthemostwidely
adoptedduetoitssuitabilityfordynamicdecision-makingproblemsinherentinNSman-
agement. Notably,theefficacyofanMLapproachstronglydependsonthespecifictask
andlife-cyclephasetowhichitisapplied. Amongthephases,Operationreceivesthemost

Electronics2025,14,4053 32of38
attention,withresourceallocationastheprimaryfocus,whilesignificanteffortsalsotarget
admissioncontrolinthePreparationphaseandtheRIACtaskintheCommissioningphase.
Interestingly,theDecommissioningphaseremainsunderexplored,suggestingperhapsan
avenueforfurtherresearch.
Inclosing,thesynergybetweenNSandAI/MLstandsasacornerstoneforthead-
vancement of next-generation networks. This survey consolidated the current state of
AI-drivennetworkslicingresearch,highlightinghowMLtechniquesareintegraltomaking
intelligent,automatedNSfeasible. Byprovidingastructuredoverviewandcriticalinsights
intoexistingapproaches,thepaperaimstoserveasavaluablereferenceforresearchers
andpractitionerspursuingadvancesinintelligentnetworkmanagement. Notwithstanding,
challengessuchasscalability,real-timeprocessing,andtheneedforexplainabilityandstan-
dardizationremaincriticalareasthatwarrantfurtherinvestigation. Futureresearchshould
alsoseektofillexistinggapsbyexploringless-studiedlife-cyclephasetasks,improving
modelinterpretability,addressingscalability,consideringotheremergingAImodelslike
GenerativeAI,andtransitioningfromsimulationtoreal-worlddeploymenttounlockthe
fullpotentialofAI-enablednetworkslicingin5Gandbeyond.
AuthorContributions: Conceptualization,E.T.,A.S.,A.T.,andP.C.;investigation,E.T.,A.S.,and
A.T.;resources,E.T.,A.S.,andA.T.;writing—originaldraftpreparation,E.T.,A.S.,A.T.,andP.C.;
writing—reviewandediting,E.T.,A.S.,A.T.,andP.C.;visualization,E.T.,A.S.,andA.T.Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Dataiscontainedwithinthearticle.Furtherinquiriescanbedirected
totheauthors.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. GSMA. E2ENetworkSlicingArchitecture,Version2.0; TechnicalReportNG.127;GlobalSystemforMobileCommunications
Association(GSMA):London,UK,2021.
2. ITU. IMTVision—FrameworkandOverallObjectivesoftheFutureDevelopmentofIMTfor2020andBeyond; RecommendationM.2083;
InternationalTelecommunicationUnion(ITU):Geneva,Switzerland,2015.
3. Zhang,S. Anoverviewofnetworkslicingfor5G. IEEEWirel.Commun.2019,26,111–117.[CrossRef]
4. 3GPP. ManagementandOrchestration;Concepts,UseCasesandRequirements,Version19.0.0; TechnicalSpecification(TS)28.530;3rd
GenerationPartnershipProject(3GPP):Sophia-Antipolis,France,2025.
5. Thomatos,E.;Sgora,A.;Chatzimisios,P. ASurveyonAIbasedNetworkSlicingStandards. InProceedingsofthe2021IEEE
ConferenceonStandardsforCommunicationsandNetworking(CSCN),Thessaloniki,Greece,15–17December2021;pp.136–141.
[CrossRef]
6. Foukas,X.;Patounas,G.;Elmokashfi,A.;Marina,M.K. Networkslicingin5G:Surveyandchallenges. IEEECommun.Mag.2017,
55,94–100.[CrossRef]
7. Afolabi,I.;Taleb,T.;Samdanis,K.;Ksentini,A.;Flinck,H. Networkslicingandsoftwarization:Asurveyonprinciples,enabling
technologies,andsolutions. IEEECommun.Surv.Tutor.2018,20,2429–2453.[CrossRef]
8. Kaloxylos,A. Asurveyandananalysisofnetworkslicingin5Gnetworks. IEEECommun.Stand.Mag.2018,2,60–65.[CrossRef]
9. Chahbar,M.;Diaz,G.;Dandoush,A.;Cérin,C.;Ghoumid,K. AcomprehensivesurveyontheE2E5Gnetworkslicingmodel.
IEEETrans.Netw.Serv.Manag.2021,18,49–62.[CrossRef]
10. Ordonez-Lucena,J.;Ameigeiras,P.;Lopez,D.;Ramos-Munoz,J.J.;Lorca,J.;Folgueira,J. Networkslicingfor5GwithSDN/NFV:
Concepts,architectures,andchallenges. IEEECommun.Mag.2017,55,80–87.[CrossRef]
11. Barakabitze,A.A.;Ahmad,A.;Mijumbi,R.;Hines,A.5GnetworkslicingusingSDNandNFV:Asurveyoftaxonomy,architectures
andfuturechallenges. Comput.Netw.2020,167,106984.[CrossRef]
12. Debbabi,F.;Jmal,R.;Fourati,L.C.;Aguiar,R.L. Anoverviewofintersliceandintrasliceresourceallocationinb5gtelecommunica-
tionnetworks. IEEETrans.Netw.Serv.Manag.2022,19,5120–5132.[CrossRef]
13. Su,R.;Zhang,D.;Venkatesan,R.;Gong,Z.;Li,C.;Ding,F.;Jiang,F.;Zhu,Z. Resourceallocationfornetworkslicingin5G
telecommunicationnetworks:Asurveyofprinciplesandmodels. IEEENetw.2019,33,172–179.[CrossRef]

Electronics2025,14,4053 33of38
14. Wijethilaka,S.;Liyanage,M. SurveyonnetworkslicingforInternetofThingsrealizationin5Gnetworks. IEEECommun.Surv.
Tutor.2021,23,957–994.[CrossRef]
15. Shen,X.;Gao,J.;Wu,W.;Lyu,K.;Li,M.;Zhuang,W.;Li,X.;Rao,J. AI-assistednetwork-slicingbasednext-generationwireless
networks. IEEEOpenJ.Veh.Technol.2020,1,45–66.[CrossRef]
16. Khan,L.U.;Yaqoob,I.;Tran,N.H.;Han,Z.;Hong,C.S. Networkslicing:Recentadvances,taxonomy,requirements,andopen
researchchallenges. IEEEAccess2020,8,36009–36028.[CrossRef]
17. Wu,Y.;Dai,H.N.;Wang,H.;Xiong,Z.;Guo,S. AsurveyofintelligentnetworkslicingmanagementforindustrialIoT:Integrated
approachesforsmarttransportation,smartenergy,andsmartfactory. IEEECommun.Surv.Tutor.2022,24,1175–1211.[CrossRef]
18. Ssengonzi,C.;Kogeda,O.P.;Olwal,T.O. Asurveyofdeepreinforcementlearningapplicationin5Gandbeyondnetworkslicing
andvirtualization. Array2022,14,100142.[CrossRef]
19. Dangi, R.; Jadhav, A.; Choudhary, G.; Dragoni, N.; Mishra, M.K.; Lalwani, P. Ml-based 5G network slicing security: A
comprehensivesurvey. FutureInternet2022,14,116.[CrossRef]
20. Donatti,A.;Correa,S.L.;Martins,J.S.;Abelem,A.;Both,C.B.;Silva,F.;Suruagy,J.A.;Pasquini,R.;Moreira,R.;Cardoso,K.V.;etal.
Surveyonmachinelearning-enablednetworkslicing:Coveringtheentirelifecycle. IEEETrans. Netw. Serv. Manag. 2023,21,
994–1011. [CrossRef]
21. Phyu, H.P.; Naboulsi, D.; Stanica, R. Machine learning in network slicing—A survey. IEEE Access 2023, 11, 39123–39153.
[CrossRef]
22. Azimi,Y.;Yousefi,S.;Kalbkhani,H.;Kunz,T. ApplicationsofmachinelearninginresourcemanagementforRAN-slicingin5G
andbeyondnetworks:Asurvey. IEEEAccess2022,10,106581–106612.[CrossRef]
23. Hamdi,W.;Ksouri,C.;Bulut,H.;Mosbah,M. NetworkSlicingBasedLearningTechniquesforIoVin5GandBeyondNetworks.
IEEECommun.Surv.Tutor.2024,26,1989–2047.[CrossRef]
24. Ebrahimi,S.;Bouali,F.;Haas,O.C.L. ResourceManagementFromSingle-Domain5GtoEnd-to-End6GNetworkSlicing: A
Survey. IEEECommun.Surv.Tutor.2024,26,2836–2866.[CrossRef]
25. Novanana,S.;Kliks,A.;Arifin,A.S.;Wibisono,G. Performanceof5GSlicingwithAccessTechnologies,andDiversity:AReview
andChallenges. IEEEAccess2024,12,170780–170802.[CrossRef]
26. Sun,H.;Liu,Y.;Al-Tahmeesschi,A.;Nag,A.;Soleimanpour,M.;Canberk,B.;Arslan,H.;Ahmadi,H. Advancing6G:Surveyfor
ExplainableAIonCommunicationsandNetworkSlicing. IEEEOpenJ.Commun.Soc.2025,6,1372–1412.[CrossRef]
27. Wu,W.;Zhou,C.;Li,M.;Wu,H.;Zhou,H.;Zhang,N.;Shen,X.S.;Zhuang,W. AI-nativenetworkslicingfor6Gnetworks. IEEE
Wirel.Commun.2022,29,96–103.[CrossRef]
28. Martins,J.S.;Carvalho,T.C.;Moreira,R.;Both,C.;Donatti,A.;Corrêa,J.H.;Suruagy,J.A.;Corrêa,S.L.;Abelem,A.J.;Ribeiro,M.R.;
etal. EnhancingNetworkSlicingArchitectureswithMachineLearning,Security,SustainabilityandExperimentalNetworks
Integration. IEEEAccess2023,11,69144–69163.[CrossRef]
29. Li,W.;Liu,R.;Dai,Y.;Wang,D.;Cai,H.;Fan,J.;Li,Y. Researchonnetworkslicingforsmartgrid. InProceedingsofthe2020
IEEE10thInternationalConferenceonElectronicsInformationandEmergencyCommunication(ICEIEC),Beijing,China,17–19
July2020;pp.107–110.[CrossRef]
30. Dubey,M.;Singh,A.K.;Mishra,R. AIbasedResourceManagementfor5GNetworkSlicing:History,UseCases,andResearch
Directions. Concurr.Comput.Pract.Exp.2025,37,e8327.[CrossRef]
31. Umagiliya,T.;Wijethilaka,S.;DeAlwis,C.;Porambage,P.;Liyanage,M.Networkslicingstrategiesforsmartindustryapplications.
InProceedingsofthe2021IEEEConferenceonStandardsforCommunicationsandNetworking(CSCN),Thessaloniki,Greece,
15–17December2021;pp.30–35.[CrossRef]
32. Liu,B.;Luo,Z.;Chen,H.;Li,C. Asurveyofstate-of-the-artonedgecomputing:Theoreticalmodels,technologies,directions,and
developmentpaths. IEEEAccess2022,10,54038–54063.[CrossRef]
33. Yi,S.;Hao,Z.;Qin,Z.;Li,Q. Fogcomputing:Platformandapplications. InProceedingsofthe2015ThirdIEEEWorkshoponHot
TopicsinWebSystemsandTechnologies(HotWeb),Washington,DC,USA,12–13November2015;pp.73–78.[CrossRef]
34. LopezEscobar,J.J.;DíazRedondo,R.P.;Gil-Castineira,F. In-depthanalysisandopenchallengesofMistComputing. J.Cloud
Comput.2022,11,81.[CrossRef]
35. Bega,D.;Gramaglia,M.;Garcia-Saavedra,A.;Fiore,M.;Banchs,A.;Costa-Perez,X. NetworkSlicingMeetsArtificialIntelligence:
AnAI-BasedFrameworkforSliceManagement. IEEECommun.Mag.2020,58,32–38.[CrossRef]
36. 3GPP. SystemArchitectureforthe5GSystem(5GS),Version19.5.0; TechnicalSpecification(TS)23.501;3rdGenerationPartnership
Project(3GPP):Sophia-Antipolis,Valbonne,France,2025.
37. Bithas, P.S.; Michailidis, E.T.; Nomikos, N.; Vouyioukas, D.; Kanatas, A.G. A survey on machine-learning techniques for
UAV-basedcommunications. Sensors2019,19,5170.[CrossRef]
38. Verbraeken,J.;Wolting,M.;Katzy,J.;Kloppenburg,J.;Verbelen,T.;Rellermeyer,J.S. Asurveyondistributedmachinelearning.
ACMComput.Surv. 2020,53,1–33.[CrossRef]

Electronics2025,14,4053 34of38
39. Han,B.;Schotten,H.D. MachineLearningforNetworkSlicingResourceManagement:AComprehensiveSurvey. ZTECommun.
2019,19, 27–32. Availableonline:https://www.zte.com.cn/content/dam/zte-site/res-www-zte-com-cn/mediares/magazine/
publication/com_en/pdf/en201904.pdf(accessedon8September2025).
40. Kafle,V.P.;Fukushima,Y.;Martinez-Julia,P.;Miyazawa,T. Considerationonautomationof5Gnetworkslicingwithmachine
learning. InProceedingsofthe10thITUAcademicConferenceKaleidoscope:MachineLearningfora5GFuture(ITUK),SantaFe,
Argentina,26–28November2018.[CrossRef]
41. You,X.;Zhang,C.;Tan,X.;Jin,S.;Wu,H. AIfor5G:Researchdirectionsandparadigms. Sci. ChinaInf. Sci. 2019,62,21301.
[CrossRef]
42. ThomasRincy,N.;Gupta,R. ASurveyonMachineLearningApproachesandItsTechniques. InProceedingsofthe2020IEEE
InternationalStudents’ConferenceonElectrical,ElectronicsandComputerScience,SCEECS2020,Bhopal,India,22–23February
2020.[CrossRef]
43. Singh,S.K.;Salim,M.M.;Cha,J.;Pan,Y.;Park,J.H. Machinelearning-basednetworksub-slicingframeworkinasustainable5G
environment. Sustainability2020,12,6250.[CrossRef]
44. Bega,D.;Gramaglia,M.;Banchs,A.;Sciancalepore,V.;Samdanis,K.;Costa-Perez,X. Optimising5Ginfrastructuremarkets:The
businessofnetworkslicing. InProceedingsoftheProceedings-IEEEINFOCOM,Atlanta,GA,USA,1–4May2017.[CrossRef]
45. Bega,D.;Gramaglia,M.;Banchs,A.;Sciancalepore,V.;Costa-Perez,X. AMachineLearningApproachto5GInfrastructure
MarketOptimization. IEEETrans.Mob.Comput.2020,19,498–512.[CrossRef]
46. Bakri,S.;Brik,B.;Ksentini,A. Onusingreinforcementlearningfornetworksliceadmissioncontrolin5G:Offlinevs.online. Int.
J.Commun.Syst.2021,34,e4757.[CrossRef]
47. Raza,M.R.;Natalino,C.;Ohlen,P.;Wosinska,L.;Monti,P. ReinforcementLearningforSlicingina5GFlexibleRAN. J.Light.
Technol.2019,37,5161–5169.[CrossRef]
48. Bakhshi,B.;Mangues-Bafalluy,J.;Baranda,J. R-Learning-BasedAdmissionControlforServiceFederationinMulti-domain5G
Networks. InProceedingsoftheProceedings-IEEEGlobalCommunicationsConference,GLOBECOM,Madrid,Spain,7–11
December2021;pp.1–6.[CrossRef]
49. Sciancalepore,V.;Zanzi,L.;Costa-Perez,X.;Capone,A. ONETS:OnlineNetworkSliceBrokerfromTheorytoPractice. IEEE
Trans.Wirel.Commun.2022,21,121–134.[CrossRef]
50. Rezazadeh,F.;Chergui,H.;Alonso,L.;Verikoukis,C. ContinuousMulti-objectiveZero-touchNetworkSlicingviaTwinDelayed
DDPGandOpenAIGym. InProceedingsofthe2020IEEEGlobalCommunicationsConference,GLOBECOM2020-Proceedings,
Taipei,Taiwan,7–11December2020;pp.1–5.[CrossRef]
51. Rezazadeh,F.;Chergui,H.;Verikoukis,C. Zero-touchcontinuousnetworkslicingcontrolviascalableactor-criticlearning. arXiv
2021,arXiv:2101.06654.
52. Guan,W.;Zhang,H.;Leung,V.C. Customizedslicingfor6G:Enforcingartificialintelligenceonresourcemanagement. IEEE
Netw.2021,35,264–271.[CrossRef]
53. Sulaiman,M.;Moayyedi,A.;Salahuddin,M.A.;Boutaba,R.;Saleh,A. Multi-agentdeepreinforcementlearningforslicingand
admissioncontrolin5GC-RAN. InProceedingsoftheNOMS2022-2022IEEE/IFIPNetworkOperationsandManagement
Symposium,Budapest,Hungary,25–29April2022;pp.1–9.[CrossRef]
54. Yan,Z.;Ge,J.;Wu,Y.;Li,L.;Li,T. Automaticvirtualnetworkembedding:Adeepreinforcementlearningapproachwithgraph
convolutionalnetworks. IEEEJ.Sel.AreasCommun.2020,38,1040–1057.[CrossRef]
55. Rkhami,A.;Hadjadj-Aoul,Y.;Outtagarts,A. Learntoimprove:Anoveldeepreinforcementlearningapproachforbeyond5G
networkslicing. InProceedingsofthe2021IEEE18thAnnualConsumerCommunicationsandNetworkingConference,CCNC
2021,LasVegas,NV,USA,9–12January 2021.[CrossRef]
56. AlvesEsteves,J.J.;Boubendir,A.;Guillemin,F.;Sens,P. AHeuristicallyAssistedDeepReinforcementLearningApproachfor
NetworkSlicePlacement. IEEETrans.Netw.Serv.Manag.2022,19,4794–4806.[CrossRef]
57. Kibalya,G.;Serrat,J.;Gorricho,J.L.;Pasquini,R.;Yao,H.;Zhang,P. Areinforcementlearningbasedapproachfor5Gnetwork
slicingacrossmultipledomains. InProceedingsofthe201915thInternationalConferenceonNetworkandServiceManagement
(CNSM),Halifax,NS,Canada,21–25October2019;pp.1–5.[CrossRef]
58. Aboeleneen,A.E.;Abdellatif,A.A.;Erbad,A.M.;Salem,A.M. ECP:Error-Aware,Cost-EffectiveandProactiveNetworkSlicing
Framework. IEEEOpenJ.Commun.Soc.2024,5,2567–2584.[CrossRef]
59. Dandachi, G.; De Domenico, A.; Hoang, D.T.; Niyato, D. An Artificial Intelligence Framework for Slice Deployment and
Orchestrationin5GNetworks. IEEETrans.Cogn.Commun.Netw.2020,6,858–871.[CrossRef]
60. Garrido,L.A.;Dalgkitsis,A.;Ramantas,K.;Verikoukis,C. MachineLearningforNetworkSlicinginFutureMobileNetworks:
DesignandImplementation. InProceedingsofthe2021IEEEInternationalMediterraneanConferenceonCommunicationsand
Networking,MeditCom2021,Athens,Greece,7–10September2021;pp.23–28.[CrossRef]

Electronics2025,14,4053 35of38
61. Rahmanian,G.;Shahhoseini,H.S.;Pozveh,A.H.J. AReviewofNetworkSlicingin5GandBeyond: IntelligentApproaches
andChallenges. InProceedingsofthe2021ITUKaleidoscope:ConnectingPhysicalandVirtualWorlds,ITUK2021,Geneva,
Switzerland,6–10December2021.[CrossRef]
62. Zhang,C.;Dongy,M.;Otay,K. Vehicularmulti-sliceoptimizationin5G:Dynamicpreferencepolicyusingreinforcementlearning.
InProceedingsoftheProceedings-IEEEGlobalCommunicationsConference,GLOBECOM,Taipei,Taiwan,7–11December 2020;
pp.1–6.[CrossRef]
63. Quang, P.T.A.; Hadjadj-Aoul, Y.; Outtagarts, A. A Deep Reinforcement Learning Approach for VNF Forwarding Graph
Embedding. IEEETrans.Netw.Serv.Manag.2019,16,1318–1331.[CrossRef]
64. Zhao,L.;Li,L. Reinforcementlearningforresourcemappingin5Gnetworkslicing. InProceedingsofthe20205thInternational
ConferenceonComputerandCommunicationSystems,ICCCS2020,Shanghai,China,15–18May 2020;pp.869–873.[CrossRef]
65. Phyu,H.P.;Naboulsi,D.;Stanica,R.;Poitau,G. TowardsenergyefficiencyinRANnetworkslicing. InProceedingsofthe2023
IEEE48thConferenceonLocalComputerNetworks(LCN),DaytonaBeach,FL,USA,2–5October2023;pp.1–9.[CrossRef]
66. Phyu,H.P.;Naboulsi,D.;Stanica,R.ICE-CREAM:MultI-agentfullyCooperativEdeCentRalizEdfrAMeworkforEnergyEfficiency
inRANSlicing. IEEETrans.Netw.Serv.Manag.2025,22,1859–1873.[CrossRef]
67. Thantharate,A.;Paropkari,R.;Walunj,V.;Beard,C. DeepSlice: Adeeplearningapproachtowardsanefficientandreliable
networkslicingin5Gnetworks. InProceedingsofthe2019IEEE10thAnnualUbiquitousComputing,Electronics&Mobile
CommunicationConference(UEMCON),NewYork,NY,USA,10–12October2019;pp.0762–0767.[CrossRef]
68. Xi,R.;Chen,X.;Chen,Y.;Li,Z. Real-Timeresourceslicingfor5GRANviadeepreinforcementlearning. InProceedingsof
theInternationalConferenceonParallelandDistributedSystems-ICPADS,Tianjin,China,4–6December2019;pp.625–632.
[CrossRef]
69. Shome,D.;Kudeshia,A. DeepQ-learningfor5Gnetworkslicingwithdiverseresourcestipulationsanddynamicdatatraffic.
InProceedingsofthe3rdInternationalConferenceonArtificialIntelligenceinInformationandCommunication,ICAIIC2021,
JejuIsland,RepublicofKorea,13–16April 2021;pp.134–139.[CrossRef]
70. Tang,J.;Duan,Y.;Zhou,Y.;Jin,J. Distributedsliceselection-basedcomputationoffloadingforintelligentvehicularnetworks.
IEEEOpenJ.Veh.Technol.2021,2,261–271.[CrossRef]
71. Zhang,T.;Bian,Y.;Lu,Q.;Qi,J.;Zhang,K.;Ji,H.;Wang,W.;Wu,W. SupervisedLearningBasedResourceAllocationwith
NetworkSlicing. InProceedingsofthe2020EighthInternationalConferenceonAdvancedCloudandBigData(CBD),Taiyuan,
China,5–6December2020;pp.25–30.[CrossRef]
72. Tsourdinis,T.;Chatzistefanidis,I.;Makris,N.;Korakis,T.;Nikaein,N.;Fdida,S. Service-awarereal-timeslicingforvirtualized
beyond5Gnetworks. Comput.Netw.2024,247,110445.[CrossRef]
73. Nassar,A.;Yilmaz,Y. DeepReinforcementLearningforAdaptiveNetworkSlicingin5GforIntelligentVehicularSystemsand
SmartCities. IEEEInternetThingsJ.2021,9,222–235.[CrossRef]
74. Mei,J.;Wang,X.;Zheng,K. IntelligentnetworkslicingforV2Xservicestoward5G. IEEENetw.2019,33,196–204.[CrossRef]
75. Zhang,X.;Lu,W.;Li,B.;Zhu,Z. DRL-basednetworkorchestrationtorealizecooperative,distributedandtenant-drivenvirtual
networkslicing. InProceedingsoftheOpticsInfoBaseConferencePapers,Chengdu,China,2–5November2019; PartF138-ACPC
2019,pp.17–19.
76. Lu,W.; Fang,H.; Zhu,Z. AI-assistedresourceadvertisingandpricingtorealizedistributedtenant-drivenvirtualnetwork
slicingininter-DCopticalnetworks. InProceedingsofthe22ndConferenceonOpticalNetworkDesignandModelling,ONDM
2018-Proceedings,Dublin,Ireland,14–17May2018;pp.130–135.[CrossRef]
77. Khodapanah, B.; Awada, A.; Viering, I.; Barreto, A.N.; Simsek, M.; Fettweis, G. Frameworkforslice-awareradioresource
managementutilizingartificialneuralnetworks. IEEEAccess2020,8,174972–174987.[CrossRef]
78. Wei,F.;Feng,G.;Sun,Y.;Wang,Y.;Qin,S.;Liang,Y.C.NetworkSliceReconfigurationbyExploitingDeepReinforcementLearning
withLargeActionSpace. IEEETrans.Netw.Serv.Manag.2020,17,2197–2211.[CrossRef]
79. Yang,H.;Zhan,K.;Bao,B.;Yao,Q.;Zhang,J.;Cheriet,M. Automaticguaranteeschemeforintent-drivennetworkslicingand
reconfiguration. J.Netw.Comput.Appl.2021,190,103163.[CrossRef]
80. Rago,A.;Martiradonna,S.;Piro,G.;Abrardo,A.;Boggia,G. Atenant-drivenslicingenforcementschemebasedonPervasive
IntelligenceintheRadioAccessNetwork. Comput.Netw.2022,217,109285.[CrossRef]
81. Ayala-Romero, J.A.; Garcia-Saavedra, A.; Gramaglia, M.; Costa-Perez, X.; Banchs, A.; Alcaraz, J.J. vrAIn: Adeeplearning
approach tailoring computing and radio resources in virtualized RANs. In Proceedings of the 25th Annual International
ConferenceonMobileComputingandNetworking,LosCabos,Mexico,21–25October2019;pp.1–16.[CrossRef]
82. Xiang,H.;Yan,S.;Peng,M. ARealizationofFog-RANSlicingviaDeepReinforcementLearning. IEEETrans.Wirel.Commun.
2020,19,2515–2527.[CrossRef]
83. Endes,A.;Yuksekkaya,B.5GNetworkSlicingwithMulti-PurposeAImodels. InProceedingsofthe2022IEEEInternationalBlack
SeaConferenceonCommunicationsandNetworking,BlackSeaCom2022, Sofia,Bulgaria,6–9June2022;pp.20–25.[CrossRef]

Electronics2025,14,4053 36of38
84. Abbas,K.;Khan,T.A.;Afaq,M.;Song,W.C. NetworkSliceLifecycleManagementfor5GMobileNetworks:AnIntent-Based
NetworkingApproach. IEEEAccess2021,9,80128–80146.[CrossRef]
85. Wu,Z.X.;You,Y.Z.;Liu,C.C.;Chou,L.D. MachineLearningBased5GNetworkSlicingManagementandClassification. In
Proceedingsofthe6thInternationalConferenceonArtificialIntelligenceinInformationandCommunication,ICAIIC2024,Osaka,
Japan,19–22February 2024;pp.371–375.[CrossRef]
86. Song,C.;Zhang,M.;Huang,X.;Zhan,Y.;Wang,D.;Liu,M.;Rong,Y. Machinelearningenablingtraffic-awaredynamicslicingfor
5Gopticaltransportnetworks. InProceedingsoftheCLEO:ScienceandInnovations,SanJose,CA,USA,13–18May2018;Optica
PublishingGroup:Washington,DC,USA,2018;p.JTu2A–44.[CrossRef]
87. Theodorou, V.; Lekidis, A.; Bozios, T.; Meth, K.; Fernandez-Fernandez, A.; Tavlor, J.; Diogo, P.; Martins, P.; Behravesh, R.
Blockchain-basedzerotouchserviceassuranceincross-domainnetworkslicing. InProceedingsofthe2021JointEuropean
ConferenceonNetworksandCommunicationsand6GSummit,EuCNC/6GSummit2021,Porto,Portugal,8–11June2021;
pp.395–400.[CrossRef]
88. Camargo,J.S.;Coronado,E.;Gomez,B.;Rincon,D.;Siddiqui,S. DesignofAI-basedResourceForecastingMethodsforNetwork
Slicing. InProceedingsofthe2022InternationalWirelessCommunicationsandMobileComputing,IWCMC2022,Dubrovnik,
Croatia,30May–3June2022;pp.1064–1069.[CrossRef]
89. Kafle,V.P.;Martinez-Julia,P.;Miyazawa,T. Automationof5GNetworkSliceControlFunctionswithMachineLearning. IEEE
Commun.Stand.Mag.2019,3,54–62.[CrossRef]
90. Bega,D.;Gramaglia,M.;Fiore,M.;Banchs,A.;Costa-Perez,X. DeepCog:Optimizingresourceprovisioninginnetworkslicing
withAI-basedcapacityforecasting. IEEEJ.Sel.AreasCommun.2019,38,361–376.[CrossRef]
91. Bega,D.;Gramaglia,M.;Fiore,M.;Banchs,A.;Costa-Perez,X. AZTEC:Anticipatorycapacityallocationforzero-touchnetwork
slicing. InProceedingsoftheIEEEINFOCOM2020-IEEEConferenceonComputerCommunications,Toronto,ON,Canada,6–9
July2020;pp.794–803.[CrossRef]
92. Buyakar,T.V.K.;Agarwal,H.;Tamma,B.R.;Franklin,A.A. ResourceallocationwithadmissioncontrolforGBRanddelayQoSin
5Gnetworkslices. InProceedingsofthe2020InternationalConferenceonCOMmunicationSystems&NETworkS(COMSNETS),
Bengaluru,India,7–11January2020;pp.213–220.[CrossRef]
93. Yan,M.;Feng,G.;Zhou,J.;Sun,Y.;Liang,Y.C. Intelligentresourceschedulingfor5Gradioaccessnetworkslicing. IEEETrans.
Veh.Technol.2019,68,7691–7703.[CrossRef]
94. Tayyaba,S.K.;Khattak,H.A.;Almogren,A.;Shah,M.A.;UdDin,I.;Alkhalifa,I.;Guizani,M. 5Gvehicularnetworkresource
managementforimprovingradioaccessthroughmachinelearning. IEEEAccess2020,8,6792–6800.[CrossRef]
95. Monteil,J.B.; Hribar,J.; Barnard,P.; Li,Y.; DaSilva,L.A. Resourcereservationwithinsliced5Gnetworks: Acost-reduction
strategyforserviceproviders. InProceedingsofthe2020IEEEInternationalConferenceonCommunicationsWorkshops(ICC
Workshops),Dublin,Ireland,7–11June2020;pp.1–6.[CrossRef]
96. Cui,Y.;Huang,X.;Wu,D.;Zheng,H. MachineLearningbasedResourceAllocationStrategyforNetworkSlicinginVehicular
Networks. InProceedingsoftheCICInternationalConferenceonCommunicationsinChina,ICCC2020,Chongqing,China,9–11
August2020;Volume292,pp.454–459.[CrossRef]
97. Cui,Y.;Huang,X.;He,P.;Wu,D.;Wang,R. ATwo-TimescaleResourceAllocationSchemeinVehicularNetworkSlicing. In
ProceedingsoftheIEEEVehicularTechnologyConference,Helsinki,Finland,25–28April 2021.[CrossRef]
98. Cui,Y.;Huang,X.;He,P.;Wu,D.;Wang,R. QoSGuaranteedNetworkSlicingOrchestrationforInternetofVehicles. IEEEInternet
ThingsJ.2022,9,15215–15227.[CrossRef]
99. Khan,H.;MajidButt,M.;Samarakoon,S.;Sehier,P.;Bennis,M. DeeplearningassistedCSIestimationforjointURLLCandeMBB
resourceallocation. InProceedingsofthe2020IEEEInternationalConferenceonCommunicationsWorkshops,ICCWorkshops
2020-Proceedings,Dublin,Ireland,7–11June 2020.[CrossRef]
100. Sapavath,N.N.;Rawat,D.B.;Song,M. MachineLearningforRFSlicingUsingCSIPredictioninSoftwareDefinedLarge-Scale
MIMOWirelessNetworks. IEEETrans.Netw.Sci.Eng.2020,7,2137–2144.[CrossRef]
101. Matoussi,S.;Fajjari,I.;Aitsaadi,N.;Langar,R. DeepLearningbasedUserSliceAllocationin5GRadioAccessNetworks. In
ProceedingsoftheProceedings-ConferenceonLocalComputerNetworks,LCN,Sydney,NSW,Australia,16–19November2020;
pp.286–296.[CrossRef]
102. Jiang,W.;Anton,S.D.;Schotten,H.D. IntelligenceSlicing: AUnifiedFrameworktoIntegrateArtificialIntelligenceinto5G
Networks. InProceedingsofthe12thIFIPWirelessandMobileNetworkingConference,WMNC2019,Paris,France,11–13
September2019;pp.227–232.[CrossRef]
103. Gutterman,C.;Grinshpun,E.;Sharma,S.;Zussman,G.RANresourceusagepredictionfora5Gslicebroker. InProceedingsofthe
InternationalSymposiumonMobileAdHocNetworkingandComputing(MobiHoc),Catania,Italy,2–5July 2019;pp.231–240.
[CrossRef]
104. Sciancalepore,V.;Costa-Perez,X.;Banchs,A. RL-NSB:Reinforcementlearning-based5Gnetworkslicebroker. IEEE/ACMTrans.
Netw.2019,27,1543–1557.[CrossRef]

Electronics2025,14,4053 37of38
105. Silva,F.S.;Silva,S.N.;daSilva,L.M.;Bessa,A.;Ferino,S.;Paiva,P.;Medeiros,M.;Silva,L.;Neto,J.;Costa,K.;etal. ML-based
inter-sliceloadbalancingcontrolforproactiveoffloadingofvirtualservices. Comput.Netw.2024,246,110422.[CrossRef]
106. Bouzidi,E.H.;Outtagarts,A.;Hebbar,A.;Langar,R.;Boutaba,R. Onlinebasedlearningforpredictiveend-to-endnetworkslicing
in5Gnetworks. InProceedingsoftheICC2020-2020IEEEInternationalConferenceonCommunications(ICC),Dublin,Ireland,
7–11June2020;pp.1–7.[CrossRef]
107. Thantharate,A.;Beard,C. ADAPTIVE6G:Adaptiveresourcemanagementfornetworkslicingarchitecturesincurrent5Gand
future6Gsystems. J.Netw.Syst.Manag.2023,31,9.[CrossRef]
108. Hu, Q.; Wang, W.; Bai, X.; Jin, S.; Jiang, T. Blockchain Enabled Federated Slicing for 5G Networks with AI Accelerated
Optimization. IEEENetw.2020,34,46–52.[CrossRef]
109. Li,R.; Zhao,Z.; Sun,Q.; Chih-Lin,I.; Yang,C.; Chen,X.; Zhao,M.; Zhang,H. DeepReinforcementLearningforResource
ManagementinNetworkSlicing. IEEEAccess2018,6,74429–74441.[CrossRef]
110. Wang,Y.;Liu,N.;Pan,Z.;You,X. AI-BasedResourceAllocationinE2ENetworkSlicingwithBothPublicandNon-PublicSlices.
Appl.Sci.2023,13,12505.[CrossRef]
111. Moon,S.;Hirayama,H.;Tsukamoto,Y.;Nanba,S.;Shinbo,H. EnsembleLearningMethod-BasedSliceAdmissionControlfor
AdaptiveRAN. InProceedingsofthe2020IEEEGlobecomWorkshops,GCWkshps2020-Proceedings,Taipei,Taiwan,7–11
December2020;pp.1–6.[CrossRef]
112. Hua, Y.; Li, R.; Zhao, Z.; Chen, X.; Zhang, H. GAN-Powered Deep Distributional Reinforcement Learning for Resource
ManagementinNetworkSlicing. IEEEJ.Sel.AreasCommun.2020,38,334–349.[CrossRef]
113. Chen,G.;Mu,X.;Shen,F.;Zeng,Q. NetworkSlicingResourceAllocationBasedonLSTM-D3QNwithDualConnectivityin
HeterogeneousCellularNetworks. Appl.Sci.2022,12,9315.[CrossRef]
114. Meng,S.;Wang,Z.;Ding,H.;Wu,S.;Li,X.;Zhao,P.;Zhu,C.;Wang,X. RANSliceStrategyBasedonDeepReinforcement
LearningforSmartGrid. InProceedingsofthe2019Computing,CommunicationsandIoTApplications,ComComAp2019,
Shenzhen,China,26–28October 2019;pp.106–111.[CrossRef]
115. Shi,Y.;Sagduyu,Y.E.;Erpek,T.ReinforcementLearningforDynamicResourceOptimizationin5GRadioAccessNetworkSlicing.
InProceedingsoftheIEEEInternationalWorkshoponComputerAidedModelingandDesignofCommunicationLinksand
Networks,CAMAD, Pisa,Italy,14–16September2020.[CrossRef]
116. Albonda,H.D.;Perez-Romero,J. AnEfficientRANSlicingStrategyforaHeterogeneousNetworkwitheMBBandV2XServices.
IEEEAccess2019,7,44771–44782.[CrossRef]
117. Nouri,S.;Motalleb,M.K.;Shah-Mansouri,V.;Shariatpanahi,S.P. Semi-SupervisedLearningApproachforEfficientResource
AllocationwithNetworkSlicinginO-RAN. arXiv2024,arXiv:2401.08861.[CrossRef]
118. Zambianco,M.;Verticale,G. Spectrumallocationfornetworksliceswithinter-numerologyinterferenceusingdeepreinforcement
learning. InProceedingsoftheIEEEInternationalSymposiumonPersonal,IndoorandMobileRadioCommunications,PIMRC,
London,UK,31August–3September 2020.[CrossRef]
119. Shao,Y.;Li,R.;Hu,B.;Wu,Y.;Zhao,Z.;Zhang,H. GraphAttentionNetwork-BasedMulti-AgentReinforcementLearningfor
SlicingResourceManagementinDenseCellularNetwork. IEEETrans.Veh.Technol.2021,70,10792–10803.[CrossRef]
120. Chergui, H.; Verikoukis, C. OPEX-Limited 5G RAN Slicing: An Over-Dataset Constrained Deep Learning Approach. In
ProceedingsoftheIEEEInternationalConferenceonCommunications,Dublin,Ireland,7–11June2020.[CrossRef]
121. Xu,Y.;Zhao,Z.;Cheng,P.;Chen,Z.;Ding,M.;Vucetic,B.;Li,Y. ConstrainedReinforcementLearningforResourceAllocationin
NetworkSlicing. IEEECommun.Lett.2021,25,1554–1558.[CrossRef]
122. Liu,Y.;Ding,J.;Liu,X. AConstrainedReinforcementLearningBasedApproachforNetworkSlicing. InProceedingsofthe
Proceedings-InternationalConferenceonNetworkProtocols,ICNP,Madrid,Spain,13–16October 2020.[CrossRef]
123. Chen,X.; Zhao,Z.; Wu,C.; Bennis,M.; Liu,H.; Ji,Y.; Zhang,H. Multi-TenantCross-SliceResourceOrchestration: ADeep
ReinforcementLearningApproach. IEEEJ.Sel.AreasCommun.2019,37,2377–2392.[CrossRef]
124. Sun,G.;Boateng,G.O.;Ayepah-Mensah,D.;Liu,G.;Wei,J. AutonomousResourceSlicingforVirtualizedVehicularNetworks
withD2DCommunicationsBasedonDeepReinforcementLearning. IEEESyst.J.2020,14,4694–4705.[CrossRef]
125. Yu,K.;Zhou,H.;Qian,B.;Tang,Z.;Shen,X. AReinforcementLearningAidedDecoupledRANSlicingFrameworkforCellular
V2X. InProceedingsoftheProceedings-IEEEGlobalCommunicationsConference,GLOBECOM, Taipei,Taiwan,7–11December
2020;pp.13–18.[CrossRef]
126. Li,T.;Zhu,X.;Liu,X. AnEnd-to-EndNetworkSlicingAlgorithmBasedonDeepQ-Learningfor5GNetwork. IEEEAccess2020,
8,122229–122240.[CrossRef]
127. AnilAkyildiz,H.;FarukGemici,O.;Hokelek,I.;AliCirpan,H. HierarchicalReinforcementLearningBasedResourceAllocation
forRANSlicing. IEEEAccess2024,12,75818–75831.[CrossRef]
128. Zhou,H.;Elsayed,M.;Erol-Kantarci,M. RANResourceSlicingin5GUsingMulti-AgentCorrelatedQ-Learning. InProceedings
oftheIEEEInternationalSymposiumonPersonal,IndoorandMobileRadioCommunications,PIMRC,Helsinki,Finland,13–16
September2021;pp.1179–1184.[CrossRef]

Electronics2025,14,4053 38of38
129. Wang,T.;Chen,S.;Zhu,Y.;Tang,A.;Wang,X. LinkSlice:Fine-GrainedNetworkSliceEnforcementBasedonDeepReinforcement
Learning. IEEEJ.Sel.AreasCommun.2022,40,2378–2394.[CrossRef]
130. Li,R.;Wang,C.;Zhao,Z.;Guo,R.;Zhang,H. TheLSTM-BasedAdvantageActor-CriticLearningforResourceManagementin
NetworkSlicingWithUserMobility. IEEECommun.Lett.2020,24,2005–2009.[CrossRef]
131. Alcaraz,J.J.;Losilla,F.;Zanella,A.;Zorzi,M. Model-BasedReinforcementLearningwithKernelsforResourceAllocationinRAN
Slices. IEEETrans.Wirel.Commun.2023,22,486–501.[CrossRef]
132. Dangi,R.;Lalwani,P. Optimizingnetworkslicingin6Gnetworksthroughahybriddeeplearningstrategy. J.Supercomput.2024,
80,20400–20420.[CrossRef]
133. Lai,Y.;Yang,H.;Yang,C. Multi-resourcenetworkslicingwithdeepreinforcementlearningforanoptimalqossatisfactionratio.
InProceedingsofthe202416thInternationalConferenceonAdvancedComputationalIntelligence(ICACI),Zhangjiajie,China,
16–19May2024;pp.140–149.[CrossRef]
134. Elmosilhy,N.A.; Elmesalawy,M.M.; Ibrahim,I.I.; El-Haleem,A.M. JointQ-LearningBasedResourceAllocationandMulti-
NumerologyB5GNetworkSlicingExploitingLWATechnology. IEEEAccess2024,12,22043–22058.[CrossRef]
135. Boutiba,K.;Bagaa,M.;Ksentini,A. Optimalradioresourcemanagementin5GNRfeaturingnetworkslicing. Comput. Netw.
2023,234,109937.[CrossRef]
136. Liu,W.;Hossain,M.A.;Ansari,N.;Kiani,A.;Saboorian,T.ReinforcementLearning-BasedNetworkSlicingSchemeforOptimized
UE-QoSinFutureNetworks. IEEETrans.Netw.Serv.Manag.2024,21,3454–3464.[CrossRef]
137. Gharehgoli,A.;Nouruzi,A.;Mokari,N.;Azmi,P.;Javan,M.R.;Jorswieck,E.A. AI-BasedResourceAllocationinEnd-to-End
NetworkSlicingunderDemandandCSIUncertainties. IEEETrans.Netw.Serv.Manag.2023,20,3630–3651.[CrossRef]
138. Mei,J.;Wang,X.;Zheng,K. Semi-DecentralizedNetworkSlicingforReliableV2VServiceProvisioning: AModel-FreeDeep
ReinforcementLearningApproach. IEEETrans.Intell.Transp.Syst.2022,23,12108–12120.[CrossRef]
139. Chergui,H.;Blanco,L.;Verikoukis,C. CDF-AwareFederatedLearningforLowSLAViolationsinbeyond5GNetworkSlicing.
InProceedingsoftheIEEEInternationalConferenceonCommunications,Montreal,QC,Canada,14–23June 2021;pp. 1–6.
[CrossRef]
140. Raftopoulos,R.;D’Oro,S.;Melodia,T.;Schembra,G. DRL-BasedLatency-AwareNetworkSlicinginO-RANwithTime-Varying
SLAs. InProceedingsofthe2024InternationalConferenceonComputing,NetworkingandCommunications(ICNC),BigIsland,
HI,USA,19–22February2024;pp.737–743.[CrossRef]
141. Alkhoury,G.;Berri,S.;Chorti,A. DeepReinforcementLearning-BasedNetworkSlicingAlgorithmfor5GHeterogenousServices.
In Proceedings of the Proceedings-IEEE Global Communications Conference, GLOBECOM, Kuala Lumpur, Malaysia, 4–8
December 2023;pp.5190–5195.[CrossRef]
142. Gupta,M.;Jha,R.K. Advancednetworkdesignfor6G:Leveraginggraphtheoryandslicingforedgestability. Simul.Model.Pract.
Theory2025,138,103029.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.