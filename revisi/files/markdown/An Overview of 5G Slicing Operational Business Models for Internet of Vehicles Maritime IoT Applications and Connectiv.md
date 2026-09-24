# An Overview of 5G Slicing Operational Business Models for Internet of Vehicles Maritime IoT Applications and Connectiv

> Source file: `An Overview of 5G Slicing Operational Business Models for Internet of Vehicles Maritime IoT Applications and Connectiv.pdf`

---

ReceivedOctober29,2021,acceptedNovember11,2021,dateofpublicationNovember16,2021,
dateofcurrentversionDecember2,2021.
DigitalObjectIdentifier10.1109/ACCESS.2021.3128496
An Overview of 5G Slicing Operational Business
Models for Internet of Vehicles, Maritime IoT
Applications and Connectivity Solutions
EUGENBORCOCI1,(Member,IEEE),
ANA-MARIADRĂGULINESCU 1,(GraduateStudentMember,IEEE),
FRANKY.LI 2,(SeniorMember,IEEE),MARIUS-CONSTANTINVOCHIN 1,
ANDKJETILKJELLSTADLI3
1DepartmentofTelecommunications,UniversityPolitehnicaofBucharest(UPB),061071Bucharest,Romania
2DepartmentofInformationandCommunicationTechnology,UniversityofAgder(UiA),4885Grimstad,Norway
3TelenorMaritimeAS,4841Arendal,Norway
Correspondingauthor:Ana-MariaDrăgulinescu(ana.dragulinescu@upb.ro)
TheresearchleadingtotheseresultshasreceivedfundingfromtheNOGrants2014-2021,underProjectcontractno.42/2021,
RO-NO-2019-0499-‘‘AMassiveMIMOEnabledIoTPlatformwithNetworkingSlicingforBeyond5GIoV/V2XandMaritimeServices
(acronym:SOLID-B5G).’’
ABSTRACT Identification of ecosystems and Business Models (BM) is an important starting point for
new complex system development. The definition of actor (or stakeholder) roles and their interactions (at
both business and technical levels), together with target scenarios and use cases, provide essential input
information for further system requirement collection and architecture specification. The powerful and
flexibleFifthGeneration(5G)networkslicingtechnology,whichiscapableofcreatingvirtuallyisolatedand
logically parallel networks, enables a large range of complex services and vertical applications. Although
various terminologies and models have been proposed in recent years for BMs in the 5G domain by
many studies, projects, standards, and technical specifications from dedicated organizations, they are not
always consistent with each other. This study presents an overview and comparison of different BMs
for 5G sliced systems, followed by an example on BM definition for a 5G system in a novel ongoing
European research project. While a general ecosystem and business model could involve a large range
of organizations (including, e.g., regulation and standardization bodies), the scope of this article will be
limitedtoprimarily5GoperationalBMs,withafocusonthoseactorsorstakeholderswhoareactiveand
interactingduringreal-lifesystemoperation.Withintheproject,weperformaselectionamongsometailored
BMconfigurations,adaptedfordedicatedsliceswithdifferentservicerequirements,aimingtoserveVehicle
to Everything (V2X) and Internet of Vehicles (IoV) applications as well as Internet of Things (IoT) for
maritimeverticalapplications.ThefinalpartofthisarticlepresentsourproposedIoTconnectivitysolutions
for various maritime scenarios with and without involving satellite links. Furthermore, we shed light on
futurechallengesanddirectionsfornetworkslicinginbeyond5Gsystems.
INDEX TERMS 5G,networkslicing,businessmodels/operationalbusinessmodel,stakeholder/actorsand
roles,IoT,IoV/V2X,maritimeapplications,multi-domain,multi-operator,multi-tenant.
I. INTRODUCTION popularterminologiesadoptedinmanystudies,projects,and
Complex systems involve multiple stakeholders who have standards,aimingtoidentifytheactor/stakeholderrolesand
differentrolesandcooperatewitheachother[1].Identifying their interactions (atboth business and technical levels)[4].
therolesofstakeholdersandunderstandingtheirinteractions Based on target use cases and their associated scenarios,
are essential for every new system development [2], [3]. the defined BMs form the basis for system requirement
To this end, ecosystems and Business Models (BMs) are identification and functional architectural design. In the lit-
erature,many terminologiesandapproaches havebeenpro-
The associate editor coordinating the review of this manuscript and posedandadopted.However,theyarenotalwaysconsistent
approvingitforpublicationwasChien-MingChen . witheachother,sincevariousstudies,standards,orprojects
156624 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME9,2021

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
focused on objectives with different interests, representing other during real-life system operation. Existing BMs pro-
theperspectivefromaspecificworkinggrouporstakeholder. posed in the standards and literature for 5G and its slicing
Currently, the terminologies ecosystem and BM expose a developments will be briefly presented and compared with
multi-semanticcharacteristicindifferentstudies[5]. respect to several criteria such as flexibility, complexity,
In a general sense, a business ecosystem is a network rolesoftheactors,scalability,multi-domain,multi-operator,
of organizations/stakeholders such as suppliers, technol- and multi-tenant capabilities. Then, mainstream and poten-
ogyandserviceproviders,distributors,customers,competi- tially selectable models will be considered and compared,
tors, government agencies, regulators, etc., involved in the among those proposed by the 3rd Generation Partnership
development and delivery of a specific product or service Project(3GPP),5GInfrastructurePublicPrivatePartnership
throughbothcompetitionandcooperation[6].Traditionally, (5G-PPP),EuropeanTelecommunicationsStandardsInstitute
in the telecommunication world, ecosystem has been a fre- (ETSI), and various 5G-oriented projects. Afterwards, the
quently used terminology in mobile communication indus- BMs (roles, actors, and interactions) will be defined for a
tries, including terminal equipment and network providers, novel5G-basedcomplexsystemdevelopedintheframework
communication service providers and Over-The-Top (OTT) ofanongoingEuropeanEconomicArearesearchproject‘‘A
providers. However, in the Fifth Generation (5G) domain, MassiveMIMOEnabledIoTPlatformwithNetworkingSlic-
the semantic of ecosystem has been expanded to include ingforBeyond5GIoV/V2XandMaritimeServices(SOLID-
also other entities, e.g., the industries which are served [7]. B5G)’’ [11]. The main goal of the SOLID-B5G project is
Inparticular,CommunicationServiceProviders(CSPs),Net- todevelopbreakthroughbeyondstate-of-the-artsolutionsin
workProviders(NPs),anddifferententerprisescollaborateto orchestration management and control of resources, in the
formanecosystem.Theinvolvedstakeholders/actors/entities context of network slicing and edge computing based on
interact with each other in order to achieve together the massiveIoT(mIoT)enabledradioaccessnetwork(RAN)and
system goals (in the rest of this article, the terminologies core network (CN) for beyond 5G IoV/V2X and maritime
stakeholders and actors are interchangeably used, whereas applications. The proposed solutions by the SOLID-B5G
entity is a more general and abstract terminology used on projectforIoTconnectionsformaritimeapplicationsarealso
somemodels).Inmanystudies,ecosystemandBMarecon- presented. Finally, we shed light on challenges and future
sideredasbeingequivalent.Inotherstudies,theterminology researchdirectionswithinthistopicforbeyond5Gnetwork
ecosystembusinessmodelisalsoused[8]. slicedsystems.
In this study, a BM is regarded as a part of a general The remainder of this article is structured as follows.
ecosystem, i.e., the BM is more limited in terms of number Section II discusses general 5G ecosystems and business
ofenvironmententitiesconsideredinthesystemrepresenta- models with a focus on 5G sliced systems. A comparison
tion.Ontheotherhand,asystemcanbetreatedeitherfrom will be made among several models. Section III identifies a
a technical point of view, or from a commercial-business fewimportantaspectsrelatedtomulti-tenant,multi-domain,
point of view. The initial system development phase and and multi-operator systems. Section IV deals with specific
its commercial-business aspects can also be structured in a BMs for V2X, IoV, and IoT applied to maritime communi-
commercial-oriented BM, whereas the major system func- cation systems. Considering the potential BMs discussed in
tionalities can be described in a so-called technical BM. Sections II-IV, Section V defines BMs appropriate for the
Obviously,thetwomodelsareinterdependent. scenariosandusecasesenvisagedintheSOLID-B5Gproject
ThisarticlefocusesmainlyontechnicalBMs,whosedefi- and presents six proposed solutions for IoT connectivity.
nitionaimstoprovideinputinformationinthesystemfunc- ChallengesandfuturedirectionsarepresentedinSectionVI.
tional architecture specification phase. In the framework of Finally,SectionVIIconcludesthearticle.
5G technologies, the capabilities provided by network slic-
ing to create virtually parallel and dedicated networks offer II. 5GECOSYSTEMSANDBUSINESSMODELS
a powerful and unique opportunity for supporting a large Thissectionpresentsasummaryofsomemajorecosystems
range of complex services and applications. Consequently, andbusinessmodelsproposedfor5G.Acomparisonwillbe
appropriate BMs should be identified and selected among performed considering their main characteristics. The focus
multiple solutions. This article provides a critical overview ofourstudywillbeon5Gslicedsystems.
on different 5G slicing BMs, and ends up with a selec-
tion example of a few tailored configurations adapted for A. GENERAL5GECOSYSTEMS
dedicated slices, to serve Internet of Things (IoT), in both Thepurposeofthissubsectionistoillustratethecomplexity
consumer IoT and industrial IoT branches [9], Vehicle to andrichnessofageneralecosysteminthe5Gera.Onlyapart
Everything (V2X), Internet of Vehicles (IoV), and systems ofthisecosystem,i.e.,BMs,willbefurtherinvestigatedinthe
formaritimeapplications[10].Whilegeneralecosystemsand restofthearticle.
BMscouldinvolvealargerangeoforganizations(including Themobilecommunicationand5Gcommunityecosystem
e.g., the regulation and standardization bodies), this study definitions [12], [13] capture the systemic nature of the 5G
focuses on so-called Operational BMs (OBMs), which con- technologies and markets. In brief, industries adopt the ter-
tainonlythoseactorsthatareactiveandinteractwitheach minologyecosystemintwoslightlydifferentways:
VOLUME9,2021 156625

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
• MobileecosystemusedbytheGlobalSystemforMobile As a generic category, connectivity and higher layer
Communications Association (GSMA) and the Inter- service providers perform daily operational activities with
national Telecommunication Union (ITU) is a refined respect to network connectivity and/or service provisioning
terminology to broaden the market beyond mobile viawired/wirelessnetworks.Suchproviderscouldbe:
operators, including device manufacturers, equipment • Network Operators (NOs) that provide access to a
vendors,retailoperators,softwarecompanies,andorga-
telecommunicationsnetwork(e.g.,amobilephonenet-
nizationsinadjacentindustrysectors.
work)ortotheInternet.
• Ecosystem is a terminology adopted for more specific • SmallcelloperatorsthatenableMobileNetworkOper-
| cases | where | a platform | enables | surrounding |     | firms to |     |              |     |           |       |     |           |           |
| ----- | ----- | ---------- | ------- | ----------- | --- | -------- | --- | ------------ | --- | --------- | ----- | --- | --------- | --------- |
|       |       |            |         |             |     |          |     | ators (MNOs) |     | to deploy | sites | in  | strategic | locations |
innovateandcreatevaluesinordertoscaleupthetotal offeringsmallercoveragewithhighercapacities(using
market. Apple’s App Store is often referred to as an licensedorunlicensedspectrum).
exemplarofthisconcept.
|     |     |     |     |     |     |     | •   | Hotspot | providers | that | offer | Internet | access | (typically |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ---- | ----- | -------- | ------ | ---------- |
viaWirelessFidelity(WiFi)).
| Furthermore, |     | two recognized |     | ecosystem | concepts | origi- |     |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
natefromthebusinessmanagementandinnovationdomain, • Service Providers (SPs) that provide Internet services
|         |         |               |     |          |     |              |     | or other | value-added |     | services, | e.g.,     | cloud   | computing, |
| ------- | ------- | ------------- | --- | -------- | --- | ------------ | --- | -------- | ----------- | --- | --------- | --------- | ------- | ---------- |
| namely, | (a) the | value network |     | [14] and | (b) | the platform |     |          |             |     |           |           |         |            |
|         |         |               |     |          |     |              |     | storage, | e-learning, |     | etc. SP   | is a more | general | termi-     |
ecosystem[15].
|       |          |         |             |     |                 |     |     | nology used | to  | refer | to third | party | or outsourced | sup- |
| ----- | -------- | ------- | ----------- | --- | --------------- | --- | --- | ----------- | --- | ----- | -------- | ----- | ------------- | ---- |
| These | concepts | capture | the complex |     | interdependence | of  |     |             |     |       |          |       |               |      |
pliersincludingTelecommunicationsServiceProviders
valuecreation.Whiletheformerismoredetailedandusually
focuses on a single industry such as telecommunications, (TSPs),ApplicationServiceProviders(ASPs),Storage
|     |     |     |     |     |     |     |     | Service | Providers | (SSPs), | Internet |     | Service | Providers |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------- | -------- | --- | ------- | --------- |
utilities,ortransportation,thelatterpaysparticularattention
(ISPs),andcloud/edgeproviders.
tocompositeservicesenabledbyonekeymarketplayerand
• OTTProvidersthatoffermediaservicesdirectlytoend
| supported | by several | supplementary |     | entities | that | may span |     |     |     |     |     |     |     |     |
| --------- | ---------- | ------------- | --- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
usersviatheInternet;usuallytheyarenottheownersof
| across several | industries. |     | These | concepts | could | be instanti- |     |     |     |     |     |     |     |     |
| -------------- | ----------- | --- | ----- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
anetworkinfrastructure.Inparticular:
atedinthe5Gcontext[15]byconsideringthe5Gecosystem
– ASPsprovidecomputer-basedsolutions/servicesto
aseitheracomplexnetworkoraninterconnectedsystem.The
modelsarerecognizedasbeingcomplementary. customersoveranetwork,suchasaccesstoasoft-
|             |       |              |         |        |         |           |     | ware | solution/application |     |       | (e.g.,   | customer  | relation- |
| ----------- | ----- | ------------ | ------- | ------ | ------- | --------- | --- | ---- | -------------------- | --- | ----- | -------- | --------- | --------- |
| • Introvert | view: | 5G value     | network |        | focuses | on how 5G |     |      |                      |     |       |          |           |           |
|             |       |              |         |        |         |           |     | ship | management)          |     | using | standard | protocols | (e.g.,    |
| services    | are   | provisioned. | Such    | models | reveal  | platform  |     |      |                      |     |       |          |           |           |
theHypertextTransferProtocol(HTTP)).
internalcomplexityandhidethecomplexityoftheinter-
|     |     |     |     |     |     |     |     | – Technology |     | providers | and | developers |     | develop and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ---------- | --- | ----------- |
actionwithcustomersandexternalpartners.
|     |     |     |     |     |     |     |     | provide | technology |     | solution(s) |     | which | can be used |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | ----- | ----------- |
• Extrovertview:5Gplatformecosystemfocusesonhow
by5G-PPPprojects,SMEs,start-ups,etc.
| one | 5G platform | interacts |          | with     | the external | world. |     |          |           |     |        |     |               |      |
| --- | ----------- | --------- | -------- | -------- | ------------ | ------ | --- | -------- | --------- | --- | ------ | --- | ------------- | ---- |
|     |             |           |          |          |              |        | •   | Chip and | component |     | makers | buy | raw materials | from |
| The | model       | hides the | platform | internal | complexity   | and    |     |          |           |     |        |     |               |      |
explains in an explicit way the interactions with cus- theirsuppliers,assembletheseintocomponentsandpass
theirproductstoothermanufacturers.
tomersandexternalpartnersbelongingtootherindustry
• Developers(includingbothindividualsandinstitutions)
domains.
buildandcreatesoftwareapplications.Theseengineers
A 5G-PPP vision on a general and complete ecosystem write,debug,andexecutethesourcecodesofasoftware
business model is presented in [16]. The model consists application.
of several categories of stakeholders such as 5G industry • Device or Software, which is an object or machine,
and research, 5G complementary industry, verticals, policy apieceofmechanicalorelectronicequipment,hasbeen
makers,financingbodies,standardsandopensourceorgani-
constructedtofulfillaparticularpurpose.Adevicetyp-
zations, 5G related organizations, and vertical associations. icallyincludesbothhardwareandsoftware.
InthecontextoftheSOLID-B5Gproject,themostimportant SMEsutilizeservicesandinfrastructuresprovidedbya
•
categories are those that include active actors in the OBM. project, making their products available to developers
Examples include 5G industry and research category, 5G or end-users. An SME can be also a developer who
complementaryindustry,andverticals.
|     |     |     |     |     |     |     |     | can perform | its | own | test using | the | services | offered by |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---------- | --- | -------- | ---------- |
5G-PPPprojectsandinfrastructuresinordertodevelop
itsproducts,solutions,orsystems.SMEsincludestart-
1) 5GINDUSTRYANDRESEARCHCATEGORY
ups,spin-offs,nicheplayers,etc.
Thiscategorycontainsanygeneralbusinessorresearchactiv-
| ities, or | commercial | enterprises |     | that apply | 5G  | technologies |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
or have activities related to 5G. It includes connectivity 2) 5GCOMPLEMENTARYINDUSTRY
and higher layer service providers, technology providers 5GComplementaryIndustryrepresentsarichcategory[16]
anddevelopers,SmallandMediumEnterprises(SMEs)and including Information Technology (IT) system and net-
researchinstitutions. work integrators, IT consulting, Digital Services Providers
| 156626 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE1. Stakeholderrolesinthe5Gbusinessmodel:A5G-PPPvision(adaptedfrom[17]).
(DSPs),ITmanagementofnetworkandsoftware,Machine- Examples of verticals include Automotive (car technology
to-Machine (M2M) component providers, and other equip- providers,manufacturers,automotiveservices);Broadcasting
mentproviders. andMedia(studios,broadcasters,contentproviders,satellite
DSPsareenterprisesthatofferdigitalservicestoend-users. and cable providers, media service providers); Consumers
Suchanenterprisemayhavearolepartiallyoverlappingwith (organizations or individuals); Energy (power companies,
SPsandASPsofthe5GIndustryandResearchcategory. utilities, large users, smart grid operators); Public safety
IT Management of Network and Software: During sys- (police, rescue and fire departments, emergency medical
tem operation, network management tools automatically professionals, army, hospitals, ambulance, drone industry);
monitor active nodes, traffic, perform revision manage- Agriculture and farming; Healthcare (hospitals, healthcare
ment, and assure security. Fault detection and isolation as companies, insurance companies, health providers); Smart
well as resolution should be performed to optimize net- cities (transport and traffic management, parking, street
work efficiency and avoid any downtime. A service sup- lighting,tourism,governance,smarteconomy,environment,
plier should install and configure a network management mobility, industry); Transport and logistics (rail, maritime,
system which manages user moves, adds, or changes on aviation,road);Factoriesofthefuture.
the network, as well as network software and hardware The other stakeholders which are included by a 5G-PPP
upgrades. report[16]intheecosystemgeneralmodel,likepolicymak-
M2M component providers are enterprises offering solu- ersandfinancingbodies,standardsandopensourceorganiza-
tionsthatenablenetworkeddevicestoexchangeinformation tions,5Grelatedorganizations,andverticalassociationswill
andperformactionswithoutanymanualinterventionorassis- benotdetailedinthisarticle.Thisisbecausetheseactorsact
tanceofhumanbeings. directlyonlyinthedevelopmentphaseofasystembutnotin
theoperationphase.
3) VERTICALS
These are enterprises that take the advantages of 5G infras- B. 5GGENERALBUSINESSMODELS
tructurestocreateorofferhighlevelservicestotheirusers, This subsection presents an overview on 5G OBMs as they
or they could be themselves consumers of certain services. aredefinedbymajororganizationsinvolvedinthisdomain,
Such enterprises can play active roles in a particular OBM. i.e.,5G-PPPand3GPP.
VOLUME9,2021 156627

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
1) 5G-PPPVISION:STAKEHOLDERROLESINTHE5G
ECOSYSTEM
A5G-PPPdocument[17]presentsageneralOBMconsisting
ofmultiplestakeholders,asillustratedinFigure1.
|     | Service | Customer |     | (SC). | It uses | services | offered | by an |     |     |     |     |     |     |
| --- | ------- | -------- | --- | ----- | ------- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
•
|     | SP. | The vertical |     | industries | are | considered |     | as typical |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ---------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
examplesofSCs.
|     | • Service | Provider.  |           | It designs, | builds,    |            | and operates | high         |     |     |     |     |     |     |
| --- | --------- | ---------- | --------- | ----------- | ---------- | ---------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
|     | level     | services,  | on        | top of      | aggregated |            | network      | services.    |     |     |     |     |     |     |
|     | An        | SP plays   | a         | generic     | role,      | comprising |              | three possi- |     |     |     |     |     |     |
|     | ble       | sub-roles, | depending |             | on the     | service    | offered      | to an        |     |     |     |     |     |     |
SC:
– Acommunicationserviceproviderofferstraditional
telecommunicationservices;
|     | –   | A DSP | offers | digital | services |     | (e.g., | enhanced |     |     |     |     |     |     |
| --- | --- | ----- | ------ | ------- | -------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
mobilebroadbandandIoTtovariousverticals);
|     | –   | A Network |     | Slice as | a Service |     | (NSaaS) | provider |     |     |     |     |     |     |
| --- | --- | --------- | --- | -------- | --------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- |
offersanetworksliceanditsservices.
|     | • Network   |                | Operator.      | An         | NO       | orchestrates |            | resources  |     |     |     |     |     |     |
| --- | ----------- | -------------- | -------------- | ---------- | -------- | ------------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
|     | that        | are            | potentially    |            | offered  | by           | multiple   | virtual-   |     |     |     |     |     |     |
|     | ized        | infrastructure |                | providers. |          | It utilizes  |            | aggregated |     |     |     |     |     |     |
|     | virtualized |                | infrastructure |            | services |              | to design, | build,     |     |     |     |     |     |     |
|     | and         | operate        | network        |            | services | to           | be         | offered to |     |     |     |     |     |     |
FIGURE2. 3GPPbusinessmodel:Ahigh-levelmodelincluding
stakeholdersandtheirroles(adaptedfrom[19]).
SPs.
|     | • Virtualization |     | Infrastructure |     | Service |     | Provider | (VISP). |     |     |     |     |     |     |
| --- | ---------------- | --- | -------------- | --- | ------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
2) 3GPPBUSINESSMODEL
|     | It builds |     | and operates |     | virtualization |     | infrastructure(s) |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------ | --- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
A3GPPdocument,TR28.801[19],definesabusinessmodel
|     | (i.e., | networking |     | and computing |     | resources) |     | and then |     |     |     |     |     |     |
| --- | ------ | ---------- | --- | ------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
includingasetofstakeholdersandtheirroles.Asillustrated
|     | offers | virtualized |     | infrastructure |     | services. |     | Sometimes, |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | -------------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
inFigure2,themodelissimilartothatofthe5G-PPPwith
aVISPoffersaccesstoavarietyofresourcesbyaggre-
thestakeholdersandtheirrolesdescribedbelow.
|     | gating     | multiple | technology |          | domains     |     | and making  | them |                   |     |         |          |       |           |
| --- | ---------- | -------- | ---------- | -------- | ----------- | --- | ----------- | ---- | ----------------- | --- | ------- | -------- | ----- | --------- |
|     |            |          |            |          |             |     |             |      | • A Communication |     | Service | Customer | (CSC) | uses com- |
|     | accessible |          | through    | a single | Application |     | Programming |      |                   |     |         |          |       |           |
municationservices.
Interface(API).
Data Center Service Provider (DCSP). It designs, • Acommunicationserviceproviderdesigns,builds,and
•
operatescommunicationservices.
builds,operates,andoffersdatacenterservices.ADCSP
|     |         |      |     |      |     |           |     |           | A network | operator | designs, | builds, | and | operates its |
| --- | ------- | ---- | --- | ---- | --- | --------- | --- | --------- | --------- | -------- | -------- | ------- | --- | ------------ |
|     | differs | from | a   | VISP | and | it offers | raw | resources | •         |          |          |         |     |              |
network-levelservices.
|     | (i.e., | host   | servers) | in  | rather      | centralized |     | locations |                 |                |     |         |          |          |
| --- | ------ | ------ | -------- | --- | ----------- | ----------- | --- | --------- | --------------- | -------------- | --- | ------- | -------- | -------- |
|     |        |        |          |     |             |             |     |           | • A virtualized | infrastructure |     | service | provider | designs, |
|     | and    | simple | services | for | consumption |             | of  | these raw |                 |                |     |         |          |          |
resources. builds, and operates its virtualization infrastructure(s).
TheVISPsmayalsooffertheirvirtualizedinfrastructure
|           | As shown | in      | Figure | 1, a     | top-down | view    | of  | the layered |             |       |          |            |       |         |
| --------- | -------- | ------- | ------ | -------- | -------- | ------- | --- | ----------- | ----------- | ----- | -------- | ---------- | ----- | ------- |
|           |          |         |        |          |          |         |     |             | services to | other | types of | customers, | maybe | to CSPs |
| hierarchy |          | of this | model  | includes |          | SC, SP, | NO, | VISP, and   |             |       |          |            |       |         |
directly,i.e.,withoutgoingthroughaNO.
| DCSP. | Note | that, | in  | practice, | a   | single | organization | can |     |     |     |     |     |     |
| ----- | ---- | ----- | --- | --------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
• Adatacenterserviceproviderdesigns,builds,andoper-
| play | one | or more | roles | from | the | above | list. Furthermore, |     |     |     |     |     |     |     |
| ---- | --- | ------- | ----- | ---- | --- | ----- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
atesitsdatacenters.
| several | 5G-PPP |     | Phase | I/II | collaborative |     | research | projects |     |     |     |     |     |     |
| ------- | ------ | --- | ----- | ---- | ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
AsshowninFigure2,theNO,VISPandDCSPcouldbe
| have | been | performed |     | (see examples |     | in [18]). | Some | of them |     |     |     |     |     |     |
| ---- | ---- | --------- | --- | ------------- | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
theclientsofthefollowingproviders,respectively:
extendedthelistofroledefinitions,allowingvariouspossible
customer-provider relationships among verticals, operators, • NetworkEquipmentProvider(NEP)whichsuppliesnet-
andotherstakeholders. work equipment. For the sake of simplicity, a Virtual
NetworkFunction(VNF)supplierisconsideredhereas
|     | Note | further | in Figure | 1   | that three | auxiliary |     | actors (i.e., |     |     |     |     |     |     |
| --- | ---- | ------- | --------- | --- | ---------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
NetworkServicesAggregator,InfrastructureAggregator,and atypeofNEP;
|     |     |     |     |     |     |     |     |     | • Network Function |     | Virtualization |     | Infrastructure | (NFVI) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------------- | --- | -------------- | ------ |
DataCenteraggregator)mayexistandtheyplayessentially
aggregationandorchestrationroles.However,theirfunctions supplier.Itoffersvirtualizationinfrastructuretoitscus-
| couldbeembeddedinthemainactorsifthedesignapproach |     |     |     |     |     |     |     |     | tomers; |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Hardwaresupplierthatsupplieshardware.
| selects | this | option. | The | 5G-PPP | BM  | does | not elaborate | the | •   |     |     |     |     |     |
| ------- | ---- | ------- | --- | ------ | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
rolesinsideanOperationSupportProvider(OSP)andhard- Moreover, an organization can play one or multiple roles
ware/softwaresuppliers. defined above. Note that the list of roles above is not
| 156628 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
exhaustive. Furthermore, there exists mapping between the 2) ASLICINGMODELWITHFOURROLES
| 3GPP model | and | the | 5G-PPP | counterpart. | A   | CSC which | is  |     |     |     |     |     |     |     |
| ---------- | --- | --- | ------ | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
In[18],amorerefinedmodelisdefinedincludingfourmain
theupperlayer(e.g.,Industry4.0)utilizesservicesprovided roles,assummarizedbelow.
| by a CSP, | thus | playing    | the               | role of | an end-user. | A   | CSP    |          |      |             |     |              |     |                |
| --------- | ---- | ---------- | ----------------- | ------- | ------------ | --- | ------ | -------- | ---- | ----------- | --- | ------------ | --- | -------------- |
|           |      |            |                   |         |              |     |        | • An InP | owns | and manages |     | the physical |     | infrastructure |
| organizes | and  | structures | its communication |         | services     |     | on top |          |      |             |     |              |     |                |
(network/cloud/datacenter).Itcouldleaseitsinfrastruc-
| of the NO | it relies | on. | To perform | this | task, | the CSP | may |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
request, for instance, a network slice template from the NO ture(asitis)toasliceprovider,oritcanconstructslices
itself(theBMisflexiblewiththisrespect)andthenlease
| portfolio | (e.g., | the Industry | 4.0 | service | may | require | mas- |     |     |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
sive Machine-Type Communications (mMTC) or enhanced theinfrastructureinanetworkslicingfashion.
|        |           |        |     |                   |     |          |     | • A Network | Slice | Provider |     | (NSLP) | can | be a typical |
| ------ | --------- | ------ | --- | ----------------- | --- | -------- | --- | ----------- | ----- | -------- | --- | ------ | --- | ------------ |
| Mobile | Broadband | (eMBB) |     | slice instances). |     | NOs have | a   |             |       |          |     |        |     |              |
telecommunicationserviceprovider(theownerortenant
directconnectionwithNEPswiththeirrolesdescribedabove.
Tobuildnetworksliceinstances,theymaydeployVNFsfrom oftheinfrastructuresfromwhichnetworkslicesarecon-
|     |     |     |     |     |     |     |     | structed). | The | NSLP | can construct |     | multi-tenant, | multi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------------- | --- | ------------- | ------ |
oneormoreNEPs,whicharefinallyexecutedintheunder-
domainslicesontopofinfrastructuresofferedbyoneor
| lying cloud | infrastructure. |     | The | VISPs | provide | virtualized |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | --- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
severalInPs.
connectivitybyusingthehardwarefromoneormoreNFVI
|     |     |     |     |     |     |     |     | • A Slice | Tenant | (SLT) | in this | model | is a | generic user |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ------- | ----- | ---- | ------------ |
supplier(offeringe.g.,transportnetworkfunctionality).The
DCSP finally offers the bare metal resources (acquired ofaspecificsliceincludingnetwork/cloud/datacenters,
whichcanhostcustomizedservices.AnSLTcanrequest
| from a hardware |     | supplier) | to  | run the | service | requested | by  |         |           |     |     |                |     |              |
| --------------- | --- | --------- | --- | ------- | ------- | --------- | --- | ------- | --------- | --- | --- | -------------- | --- | ------------ |
|                 |     |           |     |         |         |           |     | an NSLP | to create | a   | new | slice instance |     | dedicated to |
CSCs.
supportcertainSLTspecificservices.TheSLTcanlease
virtualresourcesfromoneormoreNSLPsinformofa
C. 5GSLICINGBUSINESSMODELS
|        |     |           |        |       |                 |     |      | virtual network, |     | where | the | tenant | can realize, | manage, |
| ------ | --- | --------- | ------ | ----- | --------------- | --- | ---- | ---------------- | --- | ----- | --- | ------ | ------------ | ------- |
| The 5G | BMs | presented | in the | above | two subsections |     | have |                  |     |       |     |        |              |         |
andthenprovidenetworkservicestoitsindividualend
| been generic, |     | in the | sense that | they do | not elaborate |     | in an |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
users.Asingletenantmaydefineandrunoneorseveral
| explicit | way the | roles | that network | slicing | related | entities |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ------------ | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
slicesinitsdomain.
play.Inthissubsection,weexploresuchaspectsthroughtwo
|     |     |     |     |     |     |     |     | • An End-User |     | consumes | (part | of) the | services | supplied |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ----- | ------- | -------- | -------- |
representativemodels.
byatenant,withouttheneedfortheseservicesprovided
byotherbusinessactors.
1) ASLICINGMODELWITHTHREEROLES
A simplified model presented in [20] defines three main Notethatthismodelhasaclearerdistinction(withrespect
stakeholderswiththeirroles,assummarizedbelow. tothethreerolemodel)betweenthesliceproviderandtenant
An Infrastructure Provider (InP) owns and manages a (genericuser).TheaboveBMscanbeviewedfromdifferent
•
perspectives.
| physical | network   |     | as well     | as its | constituent | resources. |     |                                                  |     |     |     |     |     |     |
| -------- | --------- | --- | ----------- | ------ | ----------- | ---------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| Such     | resources |     | (e.g., Wide | Area   | Networks    | (WANs)     |     |                                                  |     |     |     |     |     |     |
|          |           |     |             |        |             |            |     | • Fromabusinesspointofview,asliceinstanceisacom- |     |     |     |     |     |     |
and/ordatacenters)canbevirtualizedandthenoffered bination of all relevant network resources, functions,
throughanAPItoasingleortomultipletenants.
|          |     |        |         |           |      |        |      | and assets                                         | required | to  | fulfill | a specific | business | case |
| -------- | --- | ------ | ------- | --------- | ---- | ------ | ---- | -------------------------------------------------- | -------- | --- | ------- | ---------- | -------- | ---- |
| A Tenant |     | leases | virtual | resources | from | one or | more |                                                    |          |     |         |            |          |      |
| •        |     |        |         |           |      |        |      | orservice,includingoperationsystemsupport,business |          |     |         |            |          |      |
InPsinformofavirtualnetwork,wherethetenantcan
systemsupport,andDevOps(whichisasetofpractices
| realize, | manage, |     | and provide | network | slices | which | in  |     |     |     |     |     |     |     |
| -------- | ------- | --- | ----------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thatcombinesoftwaredevelopment(Dev)withIToper-
| turn    | realize | network  | services | for           | end-users. | A network |       | ations(Ops)). |                  |     |       |            |         |             |
| ------- | ------- | -------- | -------- | ------------- | ---------- | --------- | ----- | ------------- | ---------------- | --- | ----- | ---------- | ------- | ----------- |
| service | is      | provided | through  | a composition |            | of        | VNFs, |               |                  |     |       |            |         |             |
|         |         |          |          |               |            |           |       | • From an     | infrastructure   |     | point | of view,   | a slice | instance    |
| and     | it is   | defined  | in terms | of individual |            | VNFs and  | the   |               |                  |     |       |            |         |             |
|         |         |          |          |               |            |           |       | requires      | the partitioning |     | and   | assignment |         | of a set of |
mechanism used to connect them, i.e., VNF graphs. resources that can be used in an isolated, disjunctive
Inthismodel,atenantisequivalenttoaVirtualNetwork
|     |     |     |     |     |     |     |     | or non-disjunctive |     | manner | with | respect | to  | other slices. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ---- | ------- | --- | ------------- |
ServiceProvider(VNSP). Infrastructureresourcesincludeconnectivity,computa-
| • An | End-User | consumes |     | (part of) | the services | supplied |     |     |     |     |     |     |     |     |
| ---- | -------- | -------- | --- | --------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
tion,andstorageresources.
byatenant,withouttheneedfortheseservicesprovided
|     |     |     |     |     |     |     |     | • From a | tenant | point of | view, | a slice | instance | provides |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ----- | ------- | -------- | -------- |
byotherbusinessactors. differentcapabilities,intermsofdatatransportfeatures
Note that the above model is recursive. That is, one or as well as their management and control capabilities.
several layers of tenants may exist, where a level-n ten- Here it is important to design how much of the man-
+
ant can offer virtual networks (i.e., slices) to a level-(n agementandcontrolcapabilitiestheNSLPallowstothe
1) tenant. However, the tenant role in this model is very slicetenant.
complex, given that it should create slices, maybe exploit Fromamanagementplanepointofview,networkslices
•
them and possibly offer them to other tenants. Therefore, refer to the managed fully functional and dynamically
betterrefinedmodelswouldbemorevaluableforreal-world createdpartitionsofphysical/virtualnetworkresources,
systems. and service functions that can act as an independent
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 156629 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
instance of a connected network and/or as a network MSP,respectively.Lastly,theVNFsupplieroffersvirtualized
| cloud.      |        |                  |            |         |         |            |     | softwarecomponentstotheMSP. |     |     |     |     |     |     |
| ----------- | ------ | ---------------- | ---------- | ------- | ------- | ---------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
| • From      | a data | plane viewpoint, |            | network | slices  | refer      | to  |                             |     |     |     |     |     |     |
| dynamically |        | created          | partitions | of      | network | forwarding |     |                             |     |     |     |     |     |     |
|             |        |                  |            |         |         |            |     | 2) 5GEXCHANGE(5GEx)         |     |     |     |     |     |     |
deviceswithguaranteesforisolationandsecurity. The 5GEx project proposes a more refined model and it
makesdistinctionbetweentwotypesofbusinessroles[22]:
D. COMPARISONOFSLICINGBUSINESSMODELSIN • Externalcustomerrole:A5Gcustomerin5GExvision
RESEARCHPROJECTS
|     |     |     |     |     |     |     |     | could be | an enterprise |     | customer | (a 5G | enterprise | cus- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | -------- | ----- | ---------- | ---- |
Generally,thebasicmodelsoutlinedintheprevioussubsec- tomer), e.g., an SME or a large enterprise, a specific
tion constitute the reference models. However, distinctions industryverticaloraDSPofferingapplicationservices
| exist among | different | approaches, |     | depending |     | on the | main |     |     |     |     |     |     |     |
| ----------- | --------- | ----------- | --- | --------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
totheirownend-users.Users’accesscouldbeobtained
objectives of each particular project. For comparison pur- throughbasicbest-effortInternetaccessservices,Virtual
| poses, this | subsection | presents | a   | few relevant |     | BMs adopted |     |         |         |        |     |         |         |          |
| ----------- | ---------- | -------- | --- | ------------ | --- | ----------- | --- | ------- | ------- | ------ | --- | ------- | ------- | -------- |
|             |            |          |     |              |     |             |     | Private | Network | (VPN), | or  | even an | evolved | Internet |
inseveral5Gresearchprojects.Notehoweverthatthissub- access service. The 5G enterprise customer purchases
sectiondoesnotintendtoprovideanexhaustivesurveyofall the5Genterpriseservicefromaprimaryprovider.
BMsproposedindifferent5Gprojects.
|     |     |     |     |     |     |     |     | • Primary/customer-facing |             |      | provider | role:    | This       | role is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | ----------- | ---- | -------- | -------- | ---------- | ------- |
|     |     |     |     |     |     |     |     | needed                    | to directly | deal | with     | external | customers. | It is   |
1) 5G-NORMA implemented in some of the 5GEx actors. Those who
Similar to the basic models, the BM presented in the implement this role should offer an interface to exter-
5G-NORMAprojectcontainsthreemainstakeholders[21]: nalpartiesfordescribingtheavailableservicesandfor
negotiatingaswellassellingtheseservices.
| • An | infrastructure | provider |     | owns | and manages | parts | of  |     |     |     |     |     |     |     |
| ---- | -------------- | -------- | --- | ---- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Theactorrolesdefinedinthe5GExprojectare:
| or all | of the | network | infrastructure. |     | The | InP offers | an  |     |     |     |     |     |     |     |
| ------ | ------ | ------- | --------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Infrastructure-as-a-Service(IaaS)totheMobileService
|     |     |     |     |     |     |     |     | • A (5G) | Infrastructure |     | Service | Provider | (InSP) | offers |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | -------- | ------ | ------ |
Provider (MSP). The InP role may be further divided 5G-enabled NFV IaaS and can also provide services
into antenna and radio equipment provider; transport directlytoa5Genterprisecustomer.Ifpresent,aCloud
networkprovider;andDCSP. Service Provider (CdSP) also belongs to this category
• An MSP provides mobile Internet connectivity to andoffersIaaS.
end-users either directly, based on a business-to- A (5G) Network Service Provider (NSP) offers
•
customer relationship or via an intermediate tenant, network-levelservices(belongingtoarchitecturelayers
i.e., a business-to-business or business-to-business-to- L2/L3. The network service scope can be assigned
| anyone | relationship. |     | The | MSP | can construct |     | dedi- |     |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
throughprivateaddressingaswellasaccordingtopublic
cated logical mobile networks based on Network Slice addressingsuchastheInternetaddressscheme.
Instances (NSLIs) realizing relevant network function A (5G) communication service provider offers 5G
•
chains to support instantiated services, e.g., inside compatiblecommunicationservices(e.g.,voice,video,
eMBBormMTCslices.Incaseofintermediatetenants, ormoreadvancedservices).Moreservicesbelongtothis
theMSP’sofferingsareNSaaSorPlatformasaService
category,suchasunifiedcommunicationandcollabora-
(PaaS).TheMSPisresponsiblefordesign,building,and tionservices,orliveeventreal-timecontentdelivery.
operationofitsserviceofferings. An Online Applications service Provider (OAP, also
•
• A Tenant buys and leverages a network slice and the known as Over-The-Top Service Provider (OTTSP))
associated services provided by an MSP. A tenant can offers online digital application services which do not
| be, | for instance, | a Mobile |     | Virtual | Network | Operator |     |           |              |     |                  |     |           |     |
| --- | ------------- | -------- | --- | ------- | ------- | -------- | --- | --------- | ------------ | --- | ---------------- | --- | --------- | --- |
|     |               |          |     |         |         |          |     | belong to | the category |     | of communication |     | services. | For |
(MVNO), an enterprise (e.g., from avertical industry), instance,largeOTTSPslikeGoogleorNetflixfallinto
oranotherorganizationthatrequirestelecommunication this category. The 5G solutions that can offer value
servicesfortheirinternalbusinessorforofferingtotheir added connectivity services as well as communication
| customers. |     |     |     |     |     |     |     | serviceswillallowanewrangeofOAPstocreatenovel |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Inthe5G-NORMAvision,therolesofMSPandInPcanbe businessesandvaluestotheirowncustomers.
vertically integrated into a single stakeholder entity namely • AnExchangePointserviceProvider(XPP)operatesan
|     |     |     |     |     |     |     |     | exchange | point | solution. | An  | XPP can | play the | role of |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | --- | ------- | -------- | ------- |
MobileNetworkOperator(MNO).Inpractice,theremayalso
existaso-calledVISPwhichdesigns,builds,andoperatesits an aggregator, supporting consumers and providers in
developinganexchangepointsuchthatautomationand
virtualizationinfrastructure(s)ontopofInPservicesprovided
interactionorchestrationarepossible.
| by one or | more DCSPs. |     | The VISP | offers | its | infrastructure |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | -------- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
service to the MSP. Other roles are: the hardware supplier • A 5G enterprise customer is a general user of system
highlevelservices.
offeringhardware(server,antenna,cable,etc)totheInPs,the
NFVIsupplierprovidingthecorrespondingNFVinfrastruc- The5GExproposalenablessolutionsfor5Genabledand
ture to its customers, i.e., to the VISP and/or directly to the 5GcompatibleSP-to-SPwholesaleservicetradingwherethe
| 156630 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
TABLE1. Mappingofdifferentprojectsbusinessmodelstothe3GPPreferencemodel.
actor roles can meet and interact, either privately at their and network aggregated virtual infrastructure services
agreed private point of interaction or at exchange points andithasagreementswithVISPs.
(wheremultiplesuch5GExactorsmeetandcantrade5GEx • A VISP provides virtualized infrastructure services
servicesaccordingtothe5GExservicespecification). based on the virtualization infrastructure(s) it designs,
|     |     |     |     |     |     |     | builds, and | operates. | A VISP | can | be further | special- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | --- | ---------- | -------- |
izeddependingonthekindofinfrastructureitmanages.
3) 5G-TRANSFORMER(5G-T) WhileaVISPtransportprovideroffersvirtualtransport
| The 5G-T | project | [23] | develops | mobile | transport | net- |     |     |     |     |     |     |
| -------- | ------- | ---- | -------- | ------ | --------- | ---- | --- | --- | --- | --- | --- | --- |
infrastructures,aVISPcomputingprovidersuppliesvir-
workswithflexibleandscalableSoftwareDefinedNetwork tualcomputinginfrastructures.
(SDN)/NFV based transport and communication infrastruc- ADCSPprovidesdatacenterservicesbasedonthedata
•
tures.Itofferscustomizedslicesforverticalindustries.Itcan
|     |     |     |     |     |     |     | centers it | designs, | builds, | and operates. | The | difference |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | ------------- | --- | ---------- |
alsoaggregateandfederatetransportnetworksandcomput- between a DCSP and a VISP computing provider is
| ing fabric | from | the edge | up to | the core | and cloud, | aiming |          |           |        |            |           |       |
| ---------- | ---- | -------- | ----- | -------- | ---------- | ------ | -------- | --------- | ------ | ---------- | --------- | ----- |
|            |      |          |       |          |            |        | that the | former is | closer | to the raw | resources | (host |
tocreateandmanageslicesontopofafederatedvirtualized servers) offering simple services of raw resource con-
infrastructure. sumption. Additionally, these resources are located in
| The stakeholders |     | for | the 5G-T | system | are defined | in a |     |     |     |     |     |     |
| ---------------- | --- | --- | -------- | ------ | ----------- | ---- | --- | --- | --- | --- | --- | --- |
acentralizedlocation(datacenter).AVISPcomputing
top-downapproach[23],assummarizedbelow. provider offers accessto a variety of virtualinfrastruc-
tureresourcescreatedbyaggregatingmultipletechnol-
| • A | Telecommunication |     | Service | Consumer | (TSC) | uses |             |     |           |      |            |         |
| --- | ----------------- | --- | ------- | -------- | ----- | ---- | ----------- | --- | --------- | ---- | ---------- | ------- |
|     |                   |     |         |          |       |      | ogy domains | and | by making | them | accessible | through |
5G-Tservicesthatareofferedbya5G-TSP.Themodel a single API for all of them. For instance, it may offer
isflexibleinasensethata5G-TSPcanalsobeaTSCof
notonlycentralizeddatacenterresources,butalsodis-
| another | SP  | through | federation. | In the | context | of 5G-T, |                    |     |           |           |            |     |
| ------- | --- | ------- | ----------- | ------ | ------- | -------- | ------------------ | --- | --------- | --------- | ---------- | --- |
|         |     |         |             |        |         |          | tributed computing |     | resources | available | throughout | the |
themainroleconsideredasaconsumerofservicesisthe
network.
verticalindustry.
• A telecommunication service provider provides 5G-T 4) 5G-MONARCH
services. A TSP designs, builds, and operates its 5G-T The 5G-MONARCH project [24] proposes an ecosys-
services. tem model for 5G slicing. In this system, the role of a
• A Mobile Transport and Computing Platform Opera- mobile network operator may change from a vertically
tor (MTCPO) is in charge of orchestrating resources, integrated stakeholder which owns the spectrum, antennas,
potentiallyfrommultiplevirtualinfrastructureproviders core network sites and equipment, to a layered stakeholder
offered to the TSP. That is, it acts as an aggregator of where each layer might be managed or implemented by
resources. The virtual infrastructure features transport a different party. A stakeholder is defined in [24] as an
and computing resources, potentially including those individual, entity, or organization that affects how the over-
DCSPswithwhichtheMTCPOhasanagreement.The all system operates. The 5G-MONARCH stakeholder roles
| MTCPO        | designs, |     | builds, | and operates | the | computing | are: |     |     |     |     |        |
| ------------ | -------- | --- | ------- | ------------ | --- | --------- | ---- | --- | --- | --- | --- | ------ |
| VOLUME9,2021 |          |     |         |              |     |           |      |     |     |     |     | 156631 |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
• An End-User is the ultimate entity which uses the ser- A. STAKEHOLDERSANDROLESFORMULTI-TENANT,
vicesprovidedbyatenantoranMSP.
MULTI-DOMAINSLICING
• ATenantpurchasesandutilizesanetworksliceandits Creating multi-tenant, multi-domain, multi-operator E2E
associated services offered by an MSP. Tenant exam- slices has impact on BMs in such environments, given the
ples include MVNO, enterprise, or any entity that need of cooperation between independent (organizational
requires telecommunication services for its business and technical) entities while preserving their independence
operations.
attributesatareasonablelevel.
• AnMSPisthemainentitywhichprovidesmobileInter-
net connectivity and telecommunication services to its 1) MULTI-TENANTSLICING
end-users.Tothisend,anMSPconstructsnetworkslices A5Gslicedsystemshouldbemulti-tenantcapable.Accord-
andtheirfunctionchainstocomposeservices.Examples ingly, several requirements need to be satisfied. A multi-
ofslicescanbeeMBBormMTC.TheMSPsetoftasks tenant 5G system is expected to 1) perform on-demand
comprisesdesign,building,offering,andoperationofits (per-tenant) dedicated slice creation, allocation, modifica-
servicesbasedonslicing. tion, isolation, and deletion of slices for different tenants;
• An InP owns and manages the network infrastructure 2) to allocate slices to different tenants concurrently on top
(antennas, base stations, remote radio heads, data cen- of a common shared infrastructure; 3) to provide suitable
ters,etc.)andoffersittotheMSP,intheformofIaaS. APIs, allowing tenants to perform specific slice monitoring
Inpractice,alargerorganizationalentity,e.g.,anMNO, andmanagement;4)toprovideelasticadaptationwithinmin-
couldoperateandownamobilenetwork,combiningthe imum and maximum limits of the slice capacity for a given
rolesofMSPandInP. tenant;and5)topossiblysupportsliceprioritizationamong
varioustenants.
| The 5G-MONARCH |     |     | model | further | refines | the | roles of |         |      |        |           |            |     |              |
| -------------- | --- | --- | ----- | ------- | ------- | --- | -------- | ------- | ---- | ------ | --------- | ---------- | --- | ------------ |
|                |     |     |       |         |         |     |          | For the | time | being, | no single | definition | of  | a tenant has |
otherentitieswhichmayexist,asdistinctactors:
|          |     |         |             |              |     |              |         | reached         | a general | consensus. | Consequently, |     |             | the definition |
| -------- | --- | ------- | ----------- | ------------ | --- | ------------ | ------- | --------------- | --------- | ---------- | ------------- | --- | ----------- | -------------- |
| • A VISP | may | exist,  | as an       | intermediate |     | actor        | between |                 |           |            |               |     |             |                |
|          |     |         |             |              |     |              |         | of stakeholders |           | and roles  | in a BM       | may | be affected | by this        |
| an InP   | and | an MSP. | It designs, | builds,      |     | and operates | a       |                 |           |            |               |     |             |                |
ambiguity.Ashortcomparisonissummarizedbelow.
| virtualization |     | infrastructure |     | on top | of the | InP | services, |          |          |       |            |     |           |            |
| -------------- | --- | -------------- | --- | ------ | ------ | --- | --------- | -------- | -------- | ----- | ---------- | --- | --------- | ---------- |
|                |     |                |     |        |        |     |           | In [20], | a tenant | actor | is defined | as  | an entity | who leases |
andoffersitsinfrastructureservicestotheMSP.
virtualresourcesfromoneormoreInPsinformofavirtual
| • At      | a lower | logical | level, an      | NFVI | supplier | may        | exist, |              |        |            |         |            |         |          |
| --------- | ------- | ------- | -------------- | ---- | -------- | ---------- | ------ | ------------ | ------ | ---------- | ------- | ---------- | ------- | -------- |
|           |         |         |                |      |          |            |        | network,     | where  | the tenant | can     | construct, | manage, | and pro- |
| providing |         | an NFV  | infrastructure |      | to its   | customers, | i.e.,  |              |        |            |         |            |         |          |
|           |         |         |                |      |          |            |        | vide network | slices | which      | in turn | realize    | network | services |
totheVISPand/ordirectlytotheMSP.
|         |         |     |           |          |     |              |     | for end-users. |        | Therefore, | the tenant  | is  | also the   | builder of |
| ------- | ------- | --- | --------- | -------- | --- | ------------ | --- | -------------- | ------ | ---------- | ----------- | --- | ---------- | ---------- |
| The BMs | adopted | in  | different | projects | can | be generally |     |                |        |            |             |     |            |            |
|         |         |     |           |          |     |              |     | network        | slices | and could  | be regarded |     | as a VNSP. | Corre-     |
mapped (but not always in a one-to-one relationship) onto spondingly, the business model defined therein is flexible
the3GPPmodel,asshowninTable1.Giventhecomplexity
andrecursive,withalayeredhierarchysupportingco-existing
of an overall multi-stakeholder system, its heterogeneity is tenants. A tenant at one layer can play the role of an InP
recognized and is still present among different BM defini- for the upper layer. Furthermore, a tenant can provide net-
tions.Diverseterminologieshavebeenadoptedbydifferent
|              |            |     |          |        |     |           |       | work services |     | not only | to an end-user |     | but also | to another |
| ------------ | ---------- | --- | -------- | ------ | --- | --------- | ----- | ------------- | --- | -------- | -------------- | --- | -------- | ---------- |
| stakeholders | performing |     | the same | tasks. | On  | the other | side, | tenant.       |     |          |                |     |          |            |
itisinherentgiventhatindependentdevelopmentshavebeen
Ontheotherhand,theworkin[18]definesatenantactoras
conducted in the same period of time. A lesson learnt from aslicetenantwhoisagenericuserofaspecificslice,includ-
the above overview is that, for a new system to be defined ing network/cloud/data centers, which can host customized
| and designed, | one | should | consider | as  | a basis | the reference |     |           |          |         |     |            |         |            |
| ------------- | --- | ------ | -------- | --- | ------- | ------------- | --- | --------- | -------- | ------- | --- | ---------- | ------- | ---------- |
|               |     |        |          |     |         |               |     | services. | Therein, | an NSLP | is  | the actual | builder | of slices. |
BMs (for example from 3GPP, 5G-PPP, etc.) but then care- An SLT can request from an NSLP to create a new slice
fully customize them to the target objectives and system instance dedicated to support certain SLT specific services.
| scale. |     |     |     |     |     |     |     | TheSLTcanleasevirtualresourcesfromoneormoreNSLPs |           |          |       |     |        |              |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --------- | -------- | ----- | --- | ------ | ------------ |
|        |     |     |     |     |     |     |     | in form of                                       | a virtual | network, | where | the | tenant | can realize, |
III. E2ESLICINGINMULTI-TENANT,MULTI-DOMAIN, manage,andthenprovidenetworkservicestoitsindividual
ANDMULTI-OPERATORENVIRONMENTS end-users. A single tenant may define, request, and run one
The BM models presented above do not address in-depth orseveralslicesinitsdomain.
aspectsrelatedtomulti-domain,multi-operator,andEnd-to- Moreover, a tenant actor in [25] is defined as a business
End(E2E)slices.Nordotheyelaborateonwhatchangesmay entitythatrentsandleveragesanNSLprovidedbyanetwork
emergewithrespecttostakeholdersandroleswhensuchan operator. The NO is the actual builder of slices. The tenant
environmentisconsidered.Anexceptionisthe5GExproject actorscanbeMVNOs,otherenterprises(e.g.,verticalindus-
which considered some multi-domain problems. Based on tries), or other organizations that require telecommunica-
this observation, we discuss in this section some aspects of tionservices.Thephysicalresourcesandcomputingentities,
E2E network slicing in multi-tenant, multi-domain, multi- whicharevirtualizedintoisolatedandindependentslices,are
| operatorenvironments. |     |     |     |     |     |     |     | sharedamongtheMVNOs. |     |     |     |     |     |              |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ------------ |
| 156632                |     |     |     |     |     |     |     |                      |     |     |     |     |     | VOLUME9,2021 |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
2) MULTI-TENANTANDMULTI-DOMAINSLICING Furthermore,anorchestratoroperator,asliceoperator(or
A3GPPdocument,TR28.804[26],hasproposedaBMand evenend-usersinsomecases)shouldbeabletocreate/request
architecture for multi-tenant and multi-domain 5G slicing aslice.Inthelattercase(whichrequiressliceon-demand),the
systems. In the 3GPP model, three actors or stakeholders slicecharacteristicsshouldbeadvertised,anditsroll-outtime
exist,i.e.,InP(s)(oneorseveral,thelatterinamulti-domain is a critical performance indicator. In addition, there must
environment); tenant(s) (one or several, the latter for multi- be an administrative interface between a slice operator and
tenants);andend-users(many). asliceprovider.
Inthatmodel,eachtenantcanconstructseveraldedicated TocreateanE2Eslice,itisnecessarytogoacrossmultiple
slicesontopoftheinfrastructureprovidedbyanInPorInPs. technologicalor/andadministrativedomains.Creatingslices
Since the model applies also to multi-domain, several InPs insuchcasescanbeperformed,generally,bytwomeans:
may cooperate and actually offer to a tenant not only bare • Direct creation of the E2E capability on a slice.
metalhardwareresourcesbutalsoafullNFVIwhichisman- In this approach, the first step is to integrate all
agedintheNFVstyle.Whatisimportantfromtheviewpoint domainresourcesviamulti-domainresourceorchestra-
of actors and roles is that each tenant has management and tion.AspecialBMactor,whichplaystheroleoforches-
controlcapabilitiesuponitsslices(basedonNFVandSDN tration, is needed. Since a multi-role actor is expected,
technologies). These network slices are operated in parallel this role could be played by one of the regular actors
uponasharedunderlyingNFVI.Theresourcesoftheshared (e.g.,aVMNO).Lateron,theorchestratorthatinitiated
underlying NFVI are owned and managed by different InP the process deploys a network slice similar to a single
actors, each defining a different infrastructure domain. The domaincase.
NFVIresourcesownedandmanagedbytheInPsaredelivered In the single domain case, a single slice template is
to the tenants logically placed on top of them. Each tenant sufficient. When different administrative domains co-
makesuseoftheNFVIresourcessuppliedbytheunderlying exist,however,theapproachofdirectcreationhaslim-
InPtomeettheservicerequirementsoftheslicesinthetenant ited applicability especially when diverse technologies
domain. The resources in this model are represented in the are adopted in different domains. This is because to
NFVIaaStype. exchange information among orchestrators about each
domain’sspecificity(heterogeneoushardwarenodesor
B. STAKEHOLDERSANDROLESFORMULTI-DOMAIN,
wholesubsystems)couldbedifficultortroublesome.
MULTI-OPERATOR,ANDE2ESLICING
• Creation of per-domain sub-slices and stitching them
Multi-domain E2E slicing architectures and especially
together. This solution follows a hierarchical approach
multi-domain orchestration are important topics and they
where per-domain orchestrators are loosely coupled
havebeenaddressedbythestandardizationandresearchcom-
with a special entity known as Business Service Slice
munities as well as 3GPP, 5G Americas, and many 5G-PPP
Orchestrator(BSSO).Inthiscase,eachdomainorches-
projects. To provide E2E services, slices should be cre-
tratorcanuseitsownslicetemplatesorblueprints.
atedacrossmultipletechnologicaloradministrativedomains.
– TheBSSOcanaskadomainorchestratortocreatea
However, not all slices are composed of domains with full
slicethatfulfillsspecificrequirements(forexample
functionality, due to different slice specific requirements or
intermsofQualityofService(QoS)).
limitedownershipcapabilities.AnE2Eslicetemplateshould
– The local orchestrator returns a list of slices that
beawareofcapabilitiesofeachadministrativedomain.
can be deployed. The mechanism of local slice or
Achallengingtasktoenablethismulti-domaincapability
sub-slicecreationissimilartothecreationofaslice
ishowtomakeatrade-offbetweenthebusinessandtechnical
on-demandbyanend-user.
independence for each BM actor and the need for coordi-
– The creation of an E2E slice as a combination of
nating the management and orchestration of the assembly,
sub-slicesisapreferredsolutionwhenslicecreation
in order to offer end-users an E2E slice crossing diverse
is triggered by end-users. Herein, sub-slices are
domains.
createdusingaparallelprocess;henceaccelerating
The BM needs to contain multiple stakeholders and will
theE2Eslicecreationroll-outtime.Thissolutionis
haveimpactontheoverallsystemarchitecture.Morespecifi-
alsoactualifanintermediatedomainoperatordoes
cally, 1) Interfaces should be defined among different own-
notallowtocreateoroperateaslicebyaBSSOin
ers/operators; 2) A business interface, which allows slice
itsdomain.
operators (tenants) to perform slice management especially
– This approach is more flexible and applies to the
to create E2E slices over multiple administrative domains,
case when an existing slice is enlarged. Note that
is needed; 3) A slice operator should have high-level man-
connecting (chaining) slices may affect the QoS
agementcapabilitiesthatincludepolicybasedmanagement,
of an E2E slice. Therefore, a process of how to
configuration, security operations, accounting, and perfor-
orchestrateslicesshouldbetakenintoaccount.
mance monitoring; and 4) A slice orchestrator should
exit, to perform automatic fault detection and performance Figure 3 exhibits a logical infrastructure which may be
management. operated and managed by a single telecom operator or may
VOLUME9,2021 156633

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE3. Anexampleofamulti-domain,multi-operator5Gslicingandorchestrationarchitecture
(adaptedfrom[27]).RO:ResourceOrchestrator;VI:VirtualInfrastructure;Ellipses:possibledifferent
businessactors.
includemultiplesub-domainsoperatedbymultipleoperators identifyroles,actors,andinteractions.Thenspecificaspects
and providers, e.g., telecom operators, MVNOs, and cloud relatedtothesupportof5Gslicingarediscussed.
| providers. | In the         | architecture, | slices              | are | deployed | on top of |     |     |     |     |     |     |
| ---------- | -------------- | ------------- | ------------------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
| various    | configurations | of            | the infrastructure, |     | where    | flexible  |     |     |     |     |     |     |
A. INTERNETOFTHINGS
configurations are possible due to the fact that resources An IoT ecosystem is a network of organizations/actors
| are virtualized | (i.e., | dedicated |     | and isolated) | for | a specific |               |             |     |          |     |               |
| --------------- | ------ | --------- | --- | ------------- | --- | ---------- | ------------- | ----------- | --- | -------- | --- | ------------- |
|                 |        |           |     |               |     |            | which develop | and exploit | IoT | products | and | services. The |
slice.
|                                                  |              |     |          |          |          |      | interacting | actors are in | both   | competition    | and | cooperation  |
| ------------------------------------------------ | ------------ | --- | -------- | -------- | -------- | ---- | ----------- | ------------- | ------ | -------------- | --- | ------------ |
| Furthermore,theworkin[28]givesanexampleofamulti- |              |     |          |          |          |      | status.     |               |        |                |     |              |
| domain                                           | slice, which | is  | composed | of three | segments | each |             |               |        |                |     |              |
|                                                  |              |     |          |          |          |      | To present  | the BM        | for an | IoT ecosystem, |     | a role-based |
coveringadistinctadministrativedomain.Inthatcase,each
|     |     |     |     |     |     |     | model is | the most flexible | approach. |     | To do | so, four major |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --------- | --- | ----- | -------------- |
domain belongs to a different actor of the business model. roles in an IoT ecosystem need to be identified and distin-
ItisproposedtoemployaseparateE2Eslicecoordinatorat
guished[29].Thatis,(a)thedevelopmentroleofatechnical
the system level in order to assure functional inter-domain solutionforanIoTsystem;(b)theoperationalroleinsystem
| coherency. | The cross-domain |        | coordinator |         | aligns | cloud and   |             |                  |     |       |        |                |
| ---------- | ---------------- | ------ | ----------- | ------- | ------ | ----------- | ----------- | ---------------- | --- | ----- | ------ | -------------- |
|            |                  |        |             |         |        |             | functioning | and exploitation | to  | serve | users; | (c) governance |
| networking | resources        | across | federated   | domains |        | and carries |             |                  |     |       |        |                |
andsupport;and(d)thenon-technicalactivitiesofthesystem.
out life-cycle management operations of a multi-domain Among them, the roles defined in (b) and (c) belong to the
| slice. It | also establishes |     | and controls | inter-domain |     | transport |     |     |     |     |     |     |
| --------- | ---------------- | --- | ------------ | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
OBM.
layerconnectivitytoassuretheexpectedperformance. Several other entities that do not belong to the OBM can
alsobeinvolvedintheIoTsystemdevelopment.Theseactors
IV. DEDICATED5GSLICINGBUSINESSMODELSFORIoT include mechanical developer, electronic hardware devel-
|     |     |     |     |     |     |     | oper, electronics | manufacturing |     | service | provider, | software |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------- | --- | ------- | --------- | -------- |
ANDIoV
ThefocusofthissectionwillbeontheOBMsthatconstitute developer, and data processing solution developer. Further-
apartofageneralIoTecosystemandareinparticularrelated more,theseactorsdeveloptheirsolutionsbasedonthesup-
to IoT and IoV/V2X applications. In what follows, we first port offered by component supplier, test provider, support
| 156634 |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
provider for software and data development, and data - Splitroles:Amunicipality(user/utilizer)purchasesnew
| broker. |     |     |     |     |     | IoT-enabled |     | waste | containers | from | a PM | and | allows a |
| ------- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ---------- | ---- | ---- | --- | -------- |
An IoT OBM can include three entities/actors, i.e., end disposal company which offers waste disposal services
users, IoT service provider(s), and (probably) product man- toserveasanSP.
ufacturer(s), with their roles clarified below. The support - Combined roles: A PM offers a service for predictive
resources are assured by a network service provider, com- maintenanceonitsmachinerythroughIoT-enablement.
putingprovider,andsupportserviceprovider.Keepinmind
• Theuseravailsand/oroperatestheIoTenabledproduct
howeverthatinpracticeanactormayplayseveralroles. orservice.Ausermightbe:
| A general     | model  | proposed        | in [28] defines | two    | additional |         |          |          |            |          |         |        |         |
| ------------- | ------ | --------------- | --------------- | ------ | ---------- | ------- | -------- | -------- | ---------- | -------- | ------- | ------ | ------- |
|               |        |                 |                 |        |            | - An    | end-user | who      | directly   | consumes | the     | IoT    | enabled |
| roles, acting | during | the development | phase           | of the | IoT sys-   |         |          |          |            |          |         |        |         |
|               |        |                 |                 |        |            | product | or       | service. | An example |          | of such | a user | can be  |
tem,namely,IoTclientadvisorandIoTcontractor.However,
acitizenwhousesanIoTenabledtrashbin.
toexploretheirrolesisbeyondthescopeofthisarticle.
|     |     |     |     |     |     | - A | utilizer | who facilitates |     | an IoT | enabled | product | or  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------ | ------- | ------- | --- |
serviceintouse.Theutilizercaneitherpurchaseoff-the-
1) ROLESINTHEIoTOPERATIONALBUSINESSMODEL shelfproducts/servicesorrequestnewproducts/services
An IoT OBM assumes the existence of six major actors, fromthePM.Anexamplecanbeamunicipalityordering
i.e., a Computing Provider (CP), NSP, Product Manufac- IoTenabledtrashbins.
turer(PM),SP,supportandserviceprovider,anduser.Their
respectiverolesareexplainedbelow.
2) SUPPORTOF5GSLICINGFORIoTAPPLICATIONS
The CP provides theIT infrastructure(e.g., computing Among the three fundamental service classes for 5G, i.e.,
•
power,datastorage,andbasicsoftware)necessarytorun eMBB, mMTC, and Ultra-Reliable Low Latency Commu-
andoperatetheIoTsolutionanditsparts.Thecomput- nications (URLLC), mMTC is the one which fits best for
|     |           |                  |        |              |      | supporting | IoT | applications | that | are | characterized |     | by low |
| --- | --------- | ---------------- | ------ | ------------ | ---- | ---------- | --- | ------------ | ---- | --- | ------------- | --- | ------ |
| ing | provision | can be performed | either | in a central | or a |            |     |              |      |     |               |     |        |
distributedmanner.Frequently,thisrolecanbetakenby requirementsintermsoflatencyandthroughput.Theseser-
thePMorbyathird-partycomputing(cloud)provider. vice classes are referred to as three major 5G user cases
|     |     |     |     |     |     | by the | 3GPP and | each | of them | has | a different | set | of ser- |
| --- | --- | --- | --- | --- | --- | ------ | -------- | ---- | ------- | --- | ----------- | --- | ------- |
Thecomputingpartssetupcanbeprovidedonpremises
at the PM, on shore, at the IT outsourcing company, vice requirements. 5G can create solutions within an E2E
|       |         |         |                 |          |       | network | slice for | each | service | scenario | (e.g., | autonomous |     |
| ----- | ------- | ------- | --------------- | -------- | ----- | ------- | --------- | ---- | ------- | -------- | ------ | ---------- | --- |
| or as | a cloud | service | (IaaS or PaaS). | The PaaS | solu- |         |           |      |         |          |        |            |     |
tioncanbecombinedwithasoftwareanddatasolution vehicle slice, smart health slice, industrial automation slice,
platform. environment monitoring slice, etc.) In particular, mMTC-
|     |     |     |     |     |     | type slices | could | well | serve | those | IoT applications |     | that |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ----- | ----- | ---------------- | --- | ---- |
• TheNSPassuresconnectivityfortheIoTenabledprod-
ucts.TheNSPservicesareoftenprovidedbyatelecom require a high number of end devices for machine-to-
|     |     |     |     |     |     | machine | communications. |     | For | IoT connectivity |     | especially |     |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | --- | ---------------- | --- | ---------- | --- |
entity(cellular,low-powersmallorlargearea).Forshort
range wireless technologies and internal networks, the in scenarios where large or huge numbers of IoT devices
NSP role is often embedded in the PM organization exist, both licensed band based connections and unlicensed
|     |     |     |     |     |     | band based | connected |     | could be | supported. |     | For certain | cat- |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | ---------- | --- | ----------- | ---- |
ortheutilizer’sorganization.Connectivitytechnologies
are very diverse, depending on the geographic scale, egories of IoT/V2X applications requiring high data rates,
|     |     |     |     |     |     | eMBB-type | slices | may | be preferable, |     | as presented |     | later in |
| --- | --- | --- | --- | --- | --- | --------- | ------ | --- | -------------- | --- | ------------ | --- | -------- |
applicationtype,requiredbandwidthandresponsetime,
| complexity,cost,securityguarantees,etc. |     |     |     |     |     | SubsectionV-B. |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
• The PM of the physical IoT-enabled product is also ConsideringtheactorsandrolesintheIoTOBMpresented
|          |     |                |          |         |          | above, the | creation | of  | network | slices | becomes | essential | for |
| -------- | --- | -------------- | -------- | ------- | -------- | ---------- | -------- | --- | ------- | ------ | ------- | --------- | --- |
| referred | to  | as the Product | Owner or | the IoT | Solution |            |          |     |         |        |         |           |     |
Owner. Its role can be performed by well-established NSPsand/orPMs.AsliceprovidercanofferNSaaStocreate
companies with existing non IoT-enabled products on customizednetworkslicestousers.Thisapproachgenerates
the market, or start-ups trying to enter the market with a new business model for MNOs compared with the BMs
new products being born as IoT-enabled. The PM may without slicing [30]. Network slicing can improve resource
utilizationefficiencyandscalabilitybyadjustingthealloca-
| itself | start | an IoT enablement | as  | part of | the prod- |     |     |     |     |     |     |     |     |
| ------ | ----- | ----------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
uct development process, or based on a user request. tionofnetworkresourcesamongslices.
| The | PM may | have some | of the capabilities |     | needed to |     |     |     |     |     |     |     |     |
| --- | ------ | --------- | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
IoT-enabledproductbutmayneedtosourcetherestof B. INTERNETOFVEHICLES
the capabilities from the IoT ecosystem. The PM may IoV is a network with connected components (vehicles)
take the role to offer itself IoT services and in such a which are intelligent moving objects with sensing, com-
caseitwillbeapartoftheOBM. puting, storage capabilities, and control units. Vehicles can
The SP utilizes the capabilities provided by an connect to other vehicles, to road side units, charging/gas
•
IoT-enabled solution to offer services to users. The SP stations, the Internet, pedestrians, via V2X communica-
may take also the PM role, or SP and PM could be tions. Vehicles can play client or server roles, take big data
separated.Forexample: services, leading to numerous new IoV applications, from
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     |     | 156635 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE4. Themainstakeholdersandrelationshipsinthecontextof5GV2Xdeployment(adaptedfrom[31]).
assisted/autonomousdriving,platooning,secureinformation industry;StandardsDevelopingOrganizations(SDOs);road
sharingandlearning,totrafficcontrolandoptimization.IoV infrastructureoperators;policymakers,andusers.
isanextensionofV2X,aimingtocreateaglobalnetworkof The four actors that belong to the V2X OBM as well as
vehicles - enabled by various wireless access technologies. theirrolesareoutlinedbelow.
| It involves | the | Internet | and includes |     | heterogeneous |     | access |               |          |     |             |          |     |          |
| ----------- | --- | -------- | ------------ | --- | ------------- | --- | ------ | ------------- | -------- | --- | ----------- | -------- | --- | -------- |
|             |     |          |              |     |               |     |        | • 5G industry | includes |     | any general | business |     | activity |
networks.IoVextendstraditionalbasicautomobilefunctions
|     |     |     |     |     |     |     |     | or commercial |     | enterprise | developing |     | or using | 5G, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ---------- | --- | -------- | --- |
likevehicledrivingandsafetytonoveltargetdomainssuchas
|     |     |     |     |     |     |     |     | or providing | 5G-related |     | services, | e.g., | MNOs, | telecom |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --------- | ----- | ----- | ------- |
enhancedtrafficmanagement,automobileproduction,repair
|             |            |      |                |     |              |     |     | vendors, | cloud | providers, | device | providers, |     | software |
| ----------- | ---------- | ---- | -------------- | --- | ------------ | --- | --- | -------- | ----- | ---------- | ------ | ---------- | --- | -------- |
| and vehicle | insurance, | road | infrastructure |     | construction |     | and |          |       |            |        |            |     |          |
developers,etc.
repair,logisticsandtransportation,etc.IoVcanberegarded
|         |             |          |     |              |      |             |     | • Automotive | industry | includes |            | car Original    | Equipment |      |
| ------- | ----------- | -------- | --- | ------------ | ---- | ----------- | --- | ------------ | -------- | -------- | ---------- | --------------- | --------- | ---- |
| also as | a dedicated | use case | of  | IoT, dealing | with | intelligent |     |              |          |          |            |                 |           |      |
|         |             |          |     |              |      |             |     | Manufacturer | (OEMs)   |          | (e.g., car | manufacturers), |           | com- |
terminalsandcomponentssuchasvehicles(andamongthem
|     |     |     |     |     |     |     |     | ponent | manufacturers | and | tier-1 | suppliers, | CAM | ser- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ------ | ---------- | --- | ---- |
someareautonomous).
viceproviders,highdefinitionmapproviders,andother
| The complexity |            | of V2X/IoV |           | applications    |     | demands | for      |                     |                |            |     |            |          |          |
| -------------- | ---------- | ---------- | --------- | --------------- | --- | ------- | -------- | ------------------- | -------------- | ---------- | --- | ---------- | -------- | -------- |
|                |            |            |           |                 |     |         |          | automotive-specific |                | technology |     | providers. | It       | can also |
| strong support |            | from an    | advanced  | infrastructure. |     |         | The 5G   |                     |                |            |     |            |          |          |
|                |            |            |           |                 |     |         |          | include             | other services | such       | as  | vehicle    | logistic | sectors. |
| slicing        | technology | is a       | promising | candidate       |     | for     | enabling |                     |                |            |     |            |          |          |
Thiscategorybringsautomotiveexpertiseandservices
| V2X/IoV | services. | Accordingly, |     | 5G V2X/IoV |     | BMs | deter- |     |     |     |     |     |     |     |
| ------- | --------- | ------------ | --- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
(includingmobilityservices)tocustomers(businessand
minetheroles,responsibilities,andinterfacesoftheentities
consumers).
| andafter         | definingthe | usecases,        |     | allowidentification |            |     | ofsys- |                       |          |                  |     |            |              |         |
| ---------------- | ----------- | ---------------- | --- | ------------------- | ---------- | --- | ------ | --------------------- | -------- | ---------------- | --- | ---------- | ------------ | ------- |
|                  |             |                  |     |                     |            |     |        | • Road Infrastructure |          | Operators        |     | (RIOs)     | are national | or      |
| tem requirements |             | and architecture |     | design.             | Concerning |     | V2X    |                       |          |                  |     |            |              |         |
|                  |             |                  |     |                     |            |     |        | regional              | entities | (public/private) |     | performing |              | deploy- |
BMs,itisrecognizedthattherestilllackssomeinsightsinto
|     |     |     |     |     |     |     |     | ment, operation, |     | and | maintenance | of  | physical | road |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----------- | --- | -------- | ---- |
therequiredroll-outconditions,rolesofdifferentstakehold-
infrastructure.Theymayalsomanageroadtrafficoper-
| ers, investments, |     | business | models, | and | expected | profit | for |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | ------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ations,own,oroperatetollsystems,etc.
| Connected | and         | Automated | Mobility | (CAM) |            | services | (see a |         |        |          |         |         |             |     |
| --------- | ----------- | --------- | -------- | ----- | ---------- | -------- | ------ | ------- | ------ | -------- | ------- | ------- | ----------- | --- |
|           |             |           |          |       |            |          |        | • Users | can be | drivers, | vehicle | owners, | passengers, |     |
| business  | feasibility | study     | for 5G   | V2X   | deployment |          | by the |         |        |          |         |         |             |     |
orpedestrians.
5G-PPP[31]).Ontheotherhand,thegeneralBMsdeveloped
for5Gslicednetworksshouldbeadaptedandrefinedinorder InFigure4,severalinteractionsbetweenstakeholdersare
toserveV2X/IoTsystemrequirements. represented(withtheirdetailsdescribedin[31]).Herein,R1
The5G-PPPAutomotiveWorkingGroup[31]hasdefined
providesuserswiththeauthorizedregulationstobefollowed;
a general 5G V2X BM, capturing both operational features R2collectsfeedbackfromusersinordertodefinetherequire-
and business relationships. It identifies the following key ments and features of the new products, functionalities and
stakeholder categories involved in the deployment of 5G services. R3 represents the regulation framework by policy
V2X technologies (shown in Figure 4), i.e., 5G industry makerstobefollowedbyautomotiveindustryaswellasthe
(networkoperators,networkanddevicevendors);automotive
feedback;R4meansthatusersbuyproductsandservicesfrom
| 156636 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
the 5G Industry and provide feedback; R5 represents inter– A. SOLID-B5GVISION
| cooperation, | allowing | design | a 5G | V2X | technology | which |            |             |            |     |              |            |     |
| ------------ | -------- | ------ | ---- | --- | ---------- | ----- | ---------- | ----------- | ---------- | --- | ------------ | ---------- | --- |
|              |          |        |      |     |            |       | 5G slicing | facilitates | a powerful |     | and flexible | networking |     |
meetsthesystemandcomponentlevelneeds;R6represents platform for a wide range of applications. In particular,
the regulations and feedback between policy makers and massive IoT (mIoT) applications specifically in IoV/V2X
the 5G Industry; R7 indicates that SDOs have to consider and maritime sectors, that are the main targets of the
regulatory conditions in standards development; R8 repre- SOLID-B5G project, can be well served by the 5G slicing
| sents thatSDOs |     | definethe | standards | tobe | implementedfor |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
technology.Amongthethreeusecasesmentionedabove,the
5G deployments; R9 means that RIO may participate in the SOLID-B5G project focuses on mMTC/mIoT and URLLC
deploymentof5GV2Xandprovideorfacilitatelicensesor bydevelopingdecentralizedsolutionsbasedonMulti-access
otherinfrastructurerequirements. EdgeComputing(MEC)combinedwithnetworkslicingand
In the meantime, several research projects that target applyingthemtoIoV/V2Xandmaritimeapplications.Novel
| at 5G based |     | V2X systems | have | proposed |     | BMs similar |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ---- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
massivemultiple-inputandmultiple-output(mMIMO)based
to the one developed by the 5G-PPP. For example, the radio access mechanisms at the network edge will also be
5GCAR [32] project identifies a BM in which the four developedaspartofthisproject.
actorspresentedabovecaninteractaccordingtooperational Figure5illustratesahigh-levelviewoftheproposedsys-
scenarios. Those stakeholders may assume different roles tem architecture which addresses two unique use cases for
| in V2X | applications | with | the support |     | of network | slicing |             |            |     |          |            |     |         |
| ------ | ------------ | ---- | ----------- | --- | ---------- | ------- | ----------- | ---------- | --- | -------- | ---------- | --- | ------- |
|        |              |      |             |     |            |         | mMIMO based | ubiquitous |     | IoT data | collection | and | network |
features. slicing enabled service provisioning for IoV/V2X and mar-
itimeapplications.
- Atenantentityrentsandleverages5Gconnectivity.Note
| that      | RIOs,        | OEMs, or | other | organization | may     | also take |                                      |     |     |     |     |     |     |
| --------- | ------------ | -------- | ----- | ------------ | ------- | --------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| thisrole. |              |          |       |              |         |           | B. SOLID-B5GBUSINESSMODELSFORIoV/V2X |     |     |     |     |     |     |
| - An      | MSP provides | services | to    | different    | tenants | with 5G   | APPLICATIONS                         |     |     |     |     |     |     |
dedicatedslicesforcustomizedservices. The operational business actors involved in SOLID-B5G
- A 5G infrastructure provider can be divided into cloud studiesareselectedbyconsideringthescenariosidentifiedin
andRANproviders,andtheyoffertheelementsneeded
theproject,particularlybasedonservicedescriptionsrelated
fortheMSPtoimplementitsslices. to IoV/V2X applications. That is, vertical services and use
- A non-V2X (supplementary) service provider can offer cases for safety and traffic efficiency of V2X slices as well
passenger-targeted services such as enhanced infotain- as for autonomous driving. More specifically, two types of
ment,mobileoffice,etc. dedicated slices, non-URLLC and URLLC, are considered,
fortwocategoriesofapplications:
| On the | other | hand, although | a   | general | 5G  | slicing OBM |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
may be mapped approximately one-to-one onto the V2X • Non-URLLC slice for traffic efficiency and auxil-
| OBM, the | dynamic | environment |     | caused | by vehicle | mobil- |                |     |            |         |     |                   |     |
| -------- | ------- | ----------- | --- | ------ | ---------- | ------ | -------------- | --- | ---------- | ------- | --- | ----------------- | --- |
|          |         |             |     |        |            |        | iary services. |     | This slice | targets | at  | non-time-critical |     |
ityintroducesadditionalchallengesforserviceprovisioning.
|     |     |     |     |     |     |     | V2X/vehicle-to-pedestrian |     |     | (V2P) |     | applications | for |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ----- | --- | ------------ | --- |
Asaneffortfromthe3GPP,twodocuments,TS22.186and instanceperiodicmessagescontainingalerts,roadcon-
| TR 23.786 | [33], | [34], have | elaborated |     | network | slicing for |     |     |     |     |     |     |     |
| --------- | ----- | ---------- | ---------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ditionupdate,weatherforecast,kinematicsparameters,
V2Xsystems.ItisrecommendedtodevelopdedicatedV2X entertainmentapplications,etc.Forexample,fortrans-
| slices, considering |      | that the | basic | reference | slices | for other |         |            |             |     |          |          |          |
| ------------------- | ---- | -------- | ----- | --------- | ------ | --------- | ------- | ---------- | ----------- | --- | -------- | -------- | -------- |
|                     |      |          |       |           |        |           | ferring | messages   | between     | two | vehicles | directly | or via   |
| traffic types       | such | as eMBB, | mMTC, | and       | URLLC, | in their  |         |            |             |     |          |          |          |
|                     |      |          |       |           |        |           | a road  | side unit, | the maximum |     | latency  | is 100   | ms [35]. |
originalforms,areincapableofsufficingV2Xrequirements High reliability should be supported without requiring
toasatisfactorylevel.
|     |     |     |     |     |     |     | application-layer |     | message | retransmissions, |     | but | no con- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ---------------- | --- | --- | ------- |
Asoftoday,constructingdedicated5GV2Xslicesisstill cretevalueisgivenin3GPPTS22.185[35].
a challenging task since it requires multi-access and edge- mMTC slices can support services where vehicles can
| oriented | 5G network | infrastructures. |     | Appropriate |     | priorities |       |           |               |     |         |      |          |
| -------- | ---------- | ---------------- | --- | ----------- | --- | ---------- | ----- | --------- | ------------- | --- | ------- | ---- | -------- |
|          |            |                  |     |             |     |            | sense | and learn | environmental |     | changes | from | built-in |
shouldbeassignedtodifferentclassesoftraffic(e.g.,inded- sensorsdeployedincarsorwithininfrastructure.mMTC
| icated network |     | slices for | V2X safety | applications, |     | the V2X |         |        |        |         |           |             |     |
| -------------- | --- | ---------- | ---------- | ------------- | --- | ------- | ------- | ------ | ------ | ------- | --------- | ----------- | --- |
|                |     |            |            |               |     |         | is also | useful | within | a dense | connected | environment |     |
traffic type should be prioritized over other network traffic to support non-delay-sensitive V2X applications (e.g.,
types). A slice provider should be able to handle intra- and dynamic ride sharing, software update) or even to pro-
inter-MNOmobilityseamlesslythroughswiftsliceresource
videmoredataforsafety-relatedapplications[36].
reconfigurationandinter-operatorsliceorchestration. • URLLC slice for safety and autonomous driving.
URLLCsliceswillplayavitalroleforintelligenttrans-
V. SOLID-B5GPROJECTSOLUTIONS portationincludingautomateddriving,roadsafety,and
In this section, we present the vision, business models, and trafficefficiencyservices,etc.Theseslicesneedtosat-
solutions proposed in our ongoing project - SOLID-B5G isfytherequirementsthatarefarstricterthanthosefor
which focuses on developing network slicing solutions for non-URLLC applications, for instance collision warn-
IoV/V2XandmaritimeIoTapplications. ing, automatic cruise control, vulnerable road users
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     |     | 156637 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE5. AgeneralviewoftheSOLID-B5GsystemarchitectureincludingRANforIoV/V2Xandmaritimeapplications,5Gcore,and
satelliteconnections.
safetyalert.Insuchcases,vehiclesmaydriveveryclose autonomousdriving,adedicatedsliceisforeachoperatoris
to each other (e.g., platooning) and at higher speeds, preferable.
and surrounding environments may change dynami- In the rest of this subsection, we identify actors for the
cally. For highest degree of automation for platooning, envisagedIoV/V2Xapplicationsandexploretheirroles.
the maximum E2E latency is 10 ms and the reliabil-
ity requirement is 99.99% [33]. For emergency tra- 1) CATEGORIESOFACTORS
jectory alignment between vehicles supporting V2X Considering the general models presented in the previous
application, the maximum E2E latency and reliability subsections and on V2X/IoV supported by 5G technolo-
requirements are 3 ms and 99.999% respectively [33]. gies, the following categories of actors are included in the
Vehicles can benefit from the information they receive SOLID-B5GOBM.
fromroadsideunitsorothervehicles.Typicalusecases
• 5Gindustry.ThesameaspresentedinSubsectionIV-B.
canbeautomatedovertake,cooperativecollisionavoid-
However,theservicesprovidedwillbebasedonconnec-
ance,andhigh-densityplatooning,whichrequireanE2E
latencyof5∼10msandablockerrorrateof∼10−5[37]. tivityoverdedicatedslicessupportingagivensetofhigh
levelV2X/IoVapplications.Usually,suchanactor(e.g.,
On the other hand, eMBB-type slices can also be appli- MNO)willownandmanagethenetworkinfrastructure
cable to V2X applications, e.g., when high data rates are (RAN,backhaul,andCNontopofwhichitcancreate
needed,forextendedsensorgroupsorsharinghigh-precision sliceinstances.WhenMECisadopted,themanagement
video as in the case of remote driving. eMBB slices andcontrolofMECcouldbealsoataskofthisactor.
can serve vehicles on the highway with heterogeneous • AutomotiveIndustry.ThesameaspresentedinSubsec-
traffic requirements, e.g., slices for autonomous driving tionIV-B.
safety messages (URLLC services), infotainment and video • RIOs. In addition to the ones presented in
streaming (non-URLLC services). eMBB can also serve SubsectionIV-B,specialattentionwillbepaidtoRIOs
non-safetyapplicationssuchasinfotainmentandmultimedia whichworkonnewroadconstructionasitismorelikely
services. thatIoTcouldbeanintegralpartofsuchinfrastructures
Inamulti-domainmulti-operationenvironment,itispos- supportingRANandnetworkconnectivity.
sible that multiple operators or tenants share a non-URLLC • Users.Insteadofinvolvingthegeneralusergroupspre-
slicebasedontheresourcesprovidedbyacommon5Ginfras- sentedinSubsectionIV-B,wewillfocusonusergroups
tructureprovider.ForURLLCservicessupportingsafetyand inRomaniaandNorway.
156638 VOLUME9,2021

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
The precise mapping between the above categories of TABLE2. Businessrelationshipmodelsbythe3GPP(adaptedfrom[40]).
actorsandOBMrolesshouldbedefinedaccordingtospecific
V2X/IoVapplicationusecases.
2) 5GSLICINGSTAKEHOLDERROLES
Fromthe5Gslicingtechnologypointofview,asetofroles
| inside the  | OBM         | will be | selected. | We       | foresee | that specific |     |     |     |     |     |     |
| ----------- | ----------- | ------- | --------- | -------- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
| roles which | are similar | to      | those     | proposed | in [38] | will apply    |     |     |     |     |     |     |
inourcase.
| • End-users | receive | the | IoV/V2X | services | provided | by a |     |     |     |     |     |     |
| ----------- | ------- | --- | ------- | -------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
tenantoranMSP.
| • A tenant | purchases |     | and utilizes | a   | network | slice and its |     |     |     |     |     |     |
| ---------- | --------- | --- | ------------ | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
associatedservicesofferedbyanMSP.Tenantexamples
| are an | MVNO, | enterprise |     | or any | entity | that requires |     |     |     |     |     |     |
| ------ | ----- | ---------- | --- | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- |
IoV/V2Xservicesforitsbusinessoperations.
| • An MSP | is  | the main | entity | which | provides | mobile |     |     |     |     |     |     |
| -------- | --- | -------- | ------ | ----- | -------- | ------ | --- | --- | --- | --- | --- | --- |
InternetconnectivityandIoV/V2Xservicestoitsusers.
authorizedtocontrolsomeaspectsofnetworkslicesthatare
| To this | end, | the MSP | constructs |     | dedicated | network |     |     |     |     |     |     |
| ------- | ---- | ------- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
slices, and their function chains to compose IoV/V2X ownedbytheMNOforprovidingIoV/V2Xservices).
Whennetworkslicingisemployed,Model3)needsaddi-
| services. | Examples |     | of dedicated | slices | can | be URLLC |     |     |     |     |     |     |
| --------- | -------- | --- | ------------ | ------ | --- | -------- | --- | --- | --- | --- | --- | --- |
tionalinvestigationrelatedtothetrustrelationshipsbetween
| and non-URLLC |     | defined |     | above, | or mMTC | for IoT |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- |
applications. MNOs and 3rd parties. There are four potential business
relationshipoptions[39]whichimpactthetrustrelationships
| • An InP | owns | and manages |     | the network | or  | road infras- |     |     |     |     |     |     |
| -------- | ---- | ----------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
tructuresandoffersittotheMSP,intheformofIaaS. forstakeholderroleModel3).
AnMNOprovidesthephysical/virtualinfrastructureand
| Similar | to the | general | case, | a larger | organizational | entity | 3a) |     |     |     |     |     |
| ------- | ------ | ------- | ----- | -------- | -------------- | ------ | --- | --- | --- | --- | --- | --- |
VNFs;anda3rdpartyusesthefunctionalityprovidedby
maycombinetherolesofMSPandInP.Additionaloptional
theMNO.
stakeholderrolesmayalsoexist,like:
3b) AnMNOprovidesthephysical/virtualinfrastructureand
• Asanintermediateactor(‘‘layer’’)betweenanInPand
|     |     |     |     |     |     |     | VNFs; | and a 3rd party | manages | some | VNFs via | APIs |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | ------- | ---- | -------- | ---- |
MSP, a VISP designs, builds and operates a virtualiza- exposedbytheMNO.
tioninfrastructureontopoftheInP-offeredservices,and
3c) AnMNOprovidesphysical/virtualinfrastructure;anda
offersitsinfrastructureservicetotheMSP.
3rdpartyprovidessomeoftheVNFs.
• Atalowerlogicallevel,anNFVIsuppliermayprovide
3d) The3rdpartyprovidesandmanagessomeofthephysi-
anNFVinfrastructuretoitscustomers,i.e.,totheVISP
cal/virtualinfrastructureandVNFs.
and/ordirectlytotheMSP.
|     |     |     |     |     |     |     | For IoV/V2X | slicing in | the SOLID-B5G |     | project, | the 3a), |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------- | --- | -------- | -------- |
If an MNO stakeholder entity is defined, then three models 3b),and3c)variantswillbeinvestigatedprimarily,inaccor-
arepossible[39]intermsofnetworkownership:
dancewiththesystemarchitecture.
1) TheMNOownsandmanagesbothRANsandaCN. Table2summarizestheserelationshipmodelsdefinedby
|     |     |     |     |     |     |     | the 3GPP [39]. | Among them, | Models | 3c) | and 3d) | provide |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------ | --- | ------- | ------- |
2) AnMNOownsandmanagestheCN,whereastheRAN
issharedamongmultipleoperators(i.e.,RANsharing). extendedcontrolforthe3rdpartyonthenetworkcapabilities
3) Onlyapartofthenetworkisownedand/ormanagedby that support its services. Accordingly, appropriate levels of
theMNO,whileotherpartsareownedand/ormanaged securityshouldbemaintainedforanycommunications.
bya3rdparty.(AnexampleisgiveninFigure8.) Furthermore, three management role models can be con-
sideredforModels3c)and3d).
Models1)and2)abovecanbefoundinpreviousgenera-
- TheMNOmanagesallphysical/virtualinfrastructureand
tionsofcellularsystems,whereMNOsareoperatingpublic
landmobilenetworks.Froma3GPPperspective,stakeholder allVNFsincluding3rdparty’sones.
role models 1) and 2) are the same, no matter an MNO or - The 3rd party manages its own physical/virtual infras-
|     |     |     |     |     |     |     | tructure | and/or its own | VNFs; | the MNO | manages | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | ----- | ------- | ------- | --- |
vertical3rdpartyisinvolved.
| In earlier | generations, |     | the basic | support | for | the 3rd party | others.   |               |                  |     |                |     |
| ---------- | ------------ | --- | --------- | ------- | --- | ------------- | --------- | ------------- | ---------------- | --- | -------------- | --- |
|            |              |     |           |         |     |               | - The 3rd | party manages | physical/virtual |     | infrastructure |     |
stakeholderrolemodelwasprovidedviaAPIswhichallowed
minimal access to or management of network capabilities. and/or VNFs including its own infrastructure and/or
In 5G, greater control and ownership by the 3rd party are VNFs and some MNO’s physical/virtual infrastructure
and/orVNFs;theMNOmanagestheothers.
| allowed, requiring |     | increased |     | trust between | the | MNO and |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
3rd party. These new trust relationships are more important Fromthe3rdparty’sperspective,thelattertwomanagement
whennetworkslicingisconsidered,(e.g.,ifthe3rdpartyis role models provide stronger support for its management
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     | 156639 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
| FIGURE6. | IllustrationofTelenor’sGEOsatellite,Thor7,anditsKa-bandcoverage[41]. |     |     |     |     |     |     |
| -------- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
function and enable extended management for the MNO to an API between the 3GPP management system and the TN
coordinate with the 3rd party management. The 3rd party wouldbesufficienttoconfiguretheadoptedsatellitenetwork
may use suitable APIs provided by the MNO to directly tohandlethesliceflowsandbackhauldatabetweenRANand
manage the VNFs as well as the infrastructure resources so CN.InitsroleofTNfor5Gbackhauling,thesatellitenetwork
thatitcanproperlyhandlewhentheirbusinessrequirements covers multiple nodes 5G New Radio (NR) nodeB (gNBs)
are updated. The last two role models are considered in the andinterconnectswithvarious5Guserplanefunctions.This
SOLID-B5GdevelopmentforIoV/V2Xdedicatedslices. implies to reserve adequate resources on both ground and
|     |     |     |     | space equipments | (e.g., satellite | gateways | and satellite pay- |
| --- | --- | --- | --- | ---------------- | ---------------- | -------- | ------------------ |
C. MARITIMESYSTEMS5GBUSINESSMODELANDIoT loads).Morethanthereservationandallocationofresources,
CONNECTIVITYSOLUTIONS the equipments need to be configured and orchestrated in
ThissubsectionpresentstheOBMforasystemdedicatedto a simple, automated manner. The 5G network should be
IoT applications in the maritime sector, with the support of abletodynamicallyrequesttheestablishmentofabackhaul
connectivityandtoupdateitdynamicallyaccordingtoservice
| 5G slicing, | which is developed | in the SOLID-B5G | project. |     |     |     |     |
| ----------- | ------------------ | ---------------- | -------- | --- | --- | --- | --- |
The corresponding solutions for IoT connectivity with and requirementsandtrafficconditions.
withoutinvolvingsatellitenetworksarealsooutlined. The above considerations suggest an approach of having
In systems dedicated to maritime applications, there are a separate business role and actor to manage the satellite
specific use cases with salient traffic and connectivity char- networkanditisadoptedintheSOLID-B5Gproject.
|              |                     |                  |             | A typical | BM for satellite | network slicing | would contain |
| ------------ | ------------------- | ---------------- | ----------- | --------- | ---------------- | --------------- | ------------- |
| acteristics. | For IoT application | scenarios, there | are several |           |                  |                 |               |
alternative solutions for data traffic via satellite networks thefollowingrolesandactors[42]:
(see Figure 7). In the meantime, it is also feasible to carry satellite slice customer
|     |     |     |     | • A |     | is the user | and tenant of a |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- |
traffic without involving satellite links, i.e., based on High satelliteslice.Itcouldbea5Gterrestrialoperatorwho
Frequency(HF)radios(seeFigure8). needsbackhaul5Gdata,orabrokerwholeasesmultiple
For maritime users/customers, we consider ships (includ- slicestomultiplesatellitesliceprovidersinordertopro-
ingcruiseships,cargovessels,etc.),offshoreplatforms(e.g., videmultipleconnectivitytoitscustomers,oraservice
oil platforms) and rigs. In such scenarios, the generated providerwhorunsOTTservices.
traffic type will be hybrid, composed of both Human-Type • Satelliteslice:Asaserviceproviderownsasliceman-
Communication(HTC)trafficandIoT/MTCtraffic.Forthe agementsystem,itmustdesign,run,andmanageslices
technicalsolutionspresentedlaterinthissubsection,wepay on the top of the satellite infrastructure. It can pro-
moreattentiontoIoTtraffic. vide slices with different levels of flexibility to a slice
|     |     |     |     | customer. | The types | of slices and | services it could |
| --- | --- | --- | --- | --------- | --------- | ------------- | ----------------- |
1) SATELLITE-RELATED5GSLICINGANDIMPLICATIONON offerdependontheinfrastructurecapabilities.Theslice
| BM  |     |     |     | provider | roles can be | played by a Satellite | Network |
| --- | --- | --- | --- | -------- | ------------ | --------------------- | ------- |
A model of satellite integration into 5G slicing system is Operator (SNO), Satellite Virtual Network Operator
presented in [42]. The satellite network plays the transport (SVNO),oradedicatedsliceoperator.
role between RAN and CN (however, in principle, the 5G AnSNOownsthesatellitespacesegmentandthesatel-
•
TransportNetwork(TN)couldbeofanytype).Integratinga lite VNFs or/and physical network functions provided
satellite network as a TN is the simplest option to integrate by suppliers (e.g., Eutelsat, SES, ViaSat). These func-
a satellite or several satellites into 5G networks. Defining tions can be monolithic components such as satellite
| 156640 |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | ------------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE7. Telenormaritime:IoTconnectivitysolutionsviasatellitenetworks.
gateways (GWs) and satellite terminals, or be disag- i.e., NFVI supplier, cooperates with InSP and provides
gregated components such as digital video broadcast themanagementsystemfortheinfrastructure;anditis
modulator/de-modulator or encapsulator (e.g., iDirect, usuallyasoftwarecompany(e.g.,VMWare,RedHat).
Newtec,Teamcast). • A satellite teleport provider owns the overall infras-
• An InSP builds, manages, and maintains a virtualized tructure. It builds the satellite teleport and configures
infrastructure(e.g.,OVH,Scaleway).Aseparateentity, it according to its clients’ demand. A teleport could
VOLUME9,2021 156641

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
FIGURE8. Telenormaritime:IoTconnectivityviaWaveAccessmeshnetworksupportedbyHFradios.
be used by multiple SNOs or SVNOs, and it is not devicescanbeconnectedtotheglobalInterneteithervia
dedicatedtoaspecifictenant.Theteleportprovideralso thegNBofanon-boardcellularnetwork(toThor7GEO
buildsandmaintainsabackbonebetweenallitsteleports satellite)ordirectlytoLEOsatellites[47].
andensuresthateachoneisconstantlyconnectedtoits (b) EPC on-board. With this solution, some of the core
customernetwork.Acommercialoff-the-shelfhardware network functions can be implemented on-board. With
suppliercanprovidenecessarycomponentstothesatel- the support of on-board EPC, network slicing may be
liteteleportprovider. supportedon-shipandoptimalresourceallocationover
ThemodelintroducesnewactorsrelatedtotheNFVtech- the satellite links can be implemented. The direct con-
nectionoptionisthesameasusedinsolution(a).
| nology. | As usual, | each actor | could | assume | one | or multiple |     |     |     |     |     |     |     |
| ------- | --------- | ---------- | ----- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
(c) BothEPCandMECon-board.Withthissolution,cer-
| roles and | it would | be most | likely | the | case. | For example, |     |     |     |     |     |     |     |
| --------- | -------- | ------- | ------ | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
taintypesofservicesmaybeprovidedlocallyon-board
| Telenor | is both | an SNO | and InSP, | as  | shown | in Figure 6. |         |          |     |                 |     |           |           |
| ------- | ------- | ------ | --------- | --- | ----- | ------------ | ------- | -------- | --- | --------------- | --- | --------- | --------- |
|         |         |        |           |     |       |              | without | the need | to  | use a satellite |     | link. For | instance, |
Inthemeantime,thirdpartyinvolvementfordataanalysisand
|     |     |     |     |     |     |     | some video | services |     | for HTC | may | be stored | locally |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------- | --- | --------- | ------- |
applicationservicesisalsoenabled,asshowninFigure8.
on-shipandbeprovidedtocustomersdirectlyviaMEC.
|     |     |     |     |     |     |     | For certain | types | of IoT | applications, |     | services | can also |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ------------- | --- | -------- | -------- |
2) SATELLITEINFRASTRUCTUREBASEDSOLUTIONSFOR
|     |     |     |     |     |     |     | be provided | solely | based | on the | on-board | facility. | For |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ----- | ------ | -------- | --------- | --- |
SOLID-B5GMARITIMEIoTAPPLICATIONS
othertraffictypes,asatellitelinkisstillnecessary.
Figure 7 presents six alternative solutions that are proposed (d) On-board private mobile network with EPC and
| in the SOLID-B5G |     | project | for | providing | both | HTC and |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
MEC.Withthissolution,bothEPCandMECareplaced
IoT/MTCservicesbasedonsatellitenetworkinfrastructures. on-board and a dedicated private network is deployed
| Herein, | satellite | networks | include | both | Geostationary | Earth |            |      |     |         |           |     |      |
| ------- | --------- | -------- | ------- | ---- | ------------- | ----- | ---------- | ---- | --- | ------- | --------- | --- | ---- |
|         |           |          |         |      |               |       | to provide | both | IoT | and HTC | services. | The | mov- |
Orbit(GEO)andLowEarthOrbit(LEO)satellites.Figure6
|     |     |     |     |     |     |     | ing/offshore | network |     | is still connected |     | to the | on-land |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------------------ | --- | ------ | ------- |
illustrates a GEO satellite, Thor 7, which is owned and network via satellite links, but less satellite traffic is
| operated | by Telenor.Thor |     | 7 is | equipped | with bothKu-band |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ---- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
generated.
and Ka-band transponders, covering Nordic countries, and (e) On-board gateway and edge processing. With this
| Central | and Eastern | Europe | (for | Ka-band), |     | as shown in |           |     |         |               |     |         |           |
| ------- | ----------- | ------ | ---- | --------- | --- | ----------- | --------- | --- | ------- | ------------- | --- | ------- | --------- |
|         |             |        |      |           |     |             | solution, | IoT | devices | are connected |     | to a GW | first and |
Figure6b).
theGWoftendoesedgeprocessingofdatatoreducethe
The E2E connection covers three segments, including amountofdatagoingtothecloud/MEC.Inthiscase,the
on-boardequipment(users,IoTdevices,andlocalnetworks);
GWisconnectedtotheon-boardcellularnetwork,and
backhaulnetwork(GEOorLEOsatellitebased);andon-land
othertypesofradio,e.g.,Bluetooth,LoRaWAN,WiFi,
terrestrialnetworks.Inwhatfollows,wepresentoursolutions
aresupportedbetweenIoTdevicesandtheGW.
whichareillustratedinFigure7.
|     |     |     |     |     |     |     | (f) On-board | gateway |     | and 5G | on satellites. |     | With this |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------ | -------------- | --- | --------- |
solution,5GradioisdirectlyoperatedfromLEOsatel-
(a) MECandEvolvedPacketCore(EPC)on-land.With
this solution, only a RAN lies on-board whereas both lites,sothatIoTdevicescanconnectdirectlytothe5G
MEC and EPC facilities are located on land. The con- radio network on the satellite. However, this solution
|          |         |     |          |     |     |              | only works | for | outdoor | IoT | devices | or GWs | due to |
| -------- | ------- | --- | -------- | --- | --- | ------------ | ---------- | --- | ------- | --- | ------- | ------ | ------ |
| nections | between | the | on-board | RAN | and | the on-shore |            |     |         |     |         |        |        |
CNareconnectedthroughasatellitelink.On-boardIoT limitedradiolinkbudget.ForIoTdeviceslocatedindoor
| 156642 |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
butwithaGWconnection,itisalsofeasibletousethis In what concerns 6G networks, the 6G Vision for
kindofnetworkwhentheGWisplacedoutdoorsothat 2030 [43]–[46] implies that a super-smart society will be
itcanconnecttosatellite5Gradio. data-driven, served by near instant, with unlimited wireless
connectivity.Themaingoalsof6Ginclude:
SummaryofIoTConnectivity:Therearethreeoptionsfor
IoTconnectionsviasatellites.Thatis,(1)IoT/MTCdevices To meet novel network demands (e.g., ultra-high relia-
•
with 4G/5G cellular capability, e.g., Narrow-Band IoT bility, ultra-high capacity and efficiency, and ultra-low
(NB-IoT),areconnecteddirectlytoagNB,andthenthesatel- latency) in a holistic fashion, satisfying the new needs
litebackhaul(theupperpartofsolutions(a)–(d));(2)Direct of economic, social, technological, and environmental
IoTconnectionstoLEOsatellitesfordeviceslocatedoutdoor contextofthe2030era.
(the lower part of solutions (a)–(d)); and (2) Connecting to Integrationofthespace,aerial,terrestrial,andmaritime
•
satellitenetworksviaaGW(solutions(e)–(f)). communicationsintoarobustnetwork.
Note further that in case of IoT connections without a • Support of Augmented Reality (AR)/Virtual Real-
GW, some reduction of data is often performed directly on ity (VR), holographic tele-presence (teleportation),
an IoT device itself. For a solution where IoT devices are eHealth, pervasive connectivity, Industry 5.0 and
connected to 5G radio directly via satellite networks, local robotics, unmanned mobility, new devices replacing
MEC on-board will not be possible. In Figure 7, we denote smartphones.
the core network by EPC and it would also be a 5G Core • Implementationofhighresolutionimagingandsensing,
(5GC)networkwhenavailable.Forallsolutionsexcept(b), wearabledisplays,mobilerobotsanddrones,specialized
EPC/5GCandMECcouldbeco-locatedon-boardoron-land. processors,distributedArtificialIntelligence(AI),hap-
ticcommunication.
|     |     |     |     |     |     |     | • Support | of autonomous |     | connected | vehicles, | massive |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --------- | --------- | ------- |
3) HFRADIOBASEDSOLUTIONSFORMARITIMEIoT
|                |           |          |         |                  |        |          | URLLC         | (mURLLC), | human-centric |     | services, | bio-IoT, |
| -------------- | --------- | -------- | ------- | ---------------- | ------ | -------- | ------------- | --------- | ------------- | --- | --------- | -------- |
| APPLICATIONS   |           |          |         |                  |        |          | andnano-NIoT. |           |               |     |           |          |
| Considering    | a salient | feature  | of      | IoT applications |        | which is |               |           |               |     |           |          |
| characteristic | of        | sporadic | traffic | and small        | packet | sizes,   |               |           |               |     |           |          |
5GnetworkslicingsupportedbySDNandNFVwillcon-
wepresenthereanothermaritimeIoTsolutionthatdoesnot tinuetoplayavitalrolein6G.Othercharacteristicsrelated
relyonasatellite.Figure8illustratesacommercialsolution tonetworkingaspectsof6Gincludeservicebasedarchitec-
developed by Telenor Maritime, branded as WaveAccess, tures;cognitiveservicearchitectures;cell-freeoperation;and
which is based on wireless mesh networking through HF ubiquitouscloud/fog/edgecomputing.
radioswhicharemountedon-board.
Relatedtonetworkslicingfor6G,severalchallengeswill
WaveAccess provides a subscription based IoT solution havetobeaddressed,suchas:
| including | collecting, | processing, |     | and access | of  | vessel data |     |     |     |     |     |     |
| --------- | ----------- | ----------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
• Sliceisolation.Toguaranteetheservicequalityofeach
| with a two-way |     | connection | range | up to | 10000 | kilometers. |     |     |     |     |     |     |
| -------------- | --- | ---------- | ----- | ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
The radios are operated on the frequency of 1.5–30 MHz, slice, different areas of isolation should be realized,
providingdataratesupto236kbps. including traffic, bandwidth, processing, and storage.
|     |     |     |     |     |     |     | The main | challenge | is  | the management | and | control of |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | -------------- | --- | ---------- |
WaveAccesssupportsmultiplestandardsforreal-timedata
collectionon-board,collectionofdatafrommultiplesources resources as such functions require to accommodate
differentisolationmechanismsacrossmultipledomains.
simultaneously,edgeprocessingformanagingandprioritiz-
ingdataalreadyatvessels,andreal-timeaccesstoimportant TheisolationmechanismssignificantlyrelyonSDNand
| dataon-shore. |     |     |     |     |     |     | NFVfunctionalities,whicharenotyetfullymature. |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
• Lackofstandardsfor6Gslicing.Thereisnotyetafinal
|     |     |     |     |     |     |     | standardized | network | slice | architecture. | Integration | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ----- | ------------- | ----------- | --- |
VI. NETWORKSLICINGCHALLENGESFORB5G/6G the space, aerial, terrestrial, and maritime communica-
5G cellular networks significantly improve communication tionsintoarobustnetworkwithslicingwillraiseamajor
| technologies | beyond | 4G  | with respect | to  | a variety | of ser- |     |     |     |     |     |     |
| ------------ | ------ | --- | ------------ | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
challengingtask.
vices/applicationssupported,numberandkindsofterminals • Dynamic slice creation and management. Efficient
connected(forbothHTCandMTC/IoTtraffic),userexperi-
dynamicslicecreationanddeletionarenecessary,while
ence(datarateandlatency),supportofdynamictraffic,pro-
|     |     |     |     |     |     |     | preserving | isolation | (performance, |     | security) | of slices. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------- | --- | --------- | ---------- |
cessingcapabilities,integrationwithcloud/edgecomputing, A network slice should be able to scale dynamically
IoV/V2Xsupport,energyconsumption,etc.
withthevaryingloadandefficientsharingisnecessary.
However, 5G has limitations with respect to the needs Furthermore,lifecyclemanagementofnetworkslicesis
| of the future | super-smart |     | society. | As such, | beyond | 5G or |     |     |     |     |     |     |
| ------------- | ----------- | --- | -------- | -------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
acriticalproblem,especiallyinamulti-domain,multi-
| Sixth Generation |     | (6G) networks |     | will play | a major | role to |     |     |     |     |     |     |
| ---------------- | --- | ------------- | --- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
tenantandmulti-operatorenvironment.
resolvethechallengesbyprovidingnewcommunicationand
computingservices,networkcapacity,andultra-lowlatency The SOLID-B5G project will extend its studies in the
| communications. |     |     |     |     |     |     | beyond5Garea,especiallytowardstwodirections: |     |     |     |     |        |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | ------ |
| VOLUME9,2021    |     |     |     |     |     |     |                                              |     |     |     |     | 156643 |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
TABLE3. Listofabbreviations. TABLE3. (Continued)Listofabbreviations.
• Integrationofspace,terrestrial,andmaritimecommuni-
cationsintoaflexibleandrobustnetwork(inaccordance
withtheprojectobjectives);
• Dynamicslicecreationandmanagementwhicharenec-
essaryinhighmobilityIoV/V2Xapplications.
VII. CONCLUSION
This article revisited the ecosystems and business models
for5GslicingsystemsandthendefinedtheBMforanovel
European research project, SOLID-B5G. The definition of
156644 VOLUME9,2021

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
actor/stakeholderrolesandtheirinteractions(atbothbusiness [13] 5G-PPP.VisionPapers&Roadmaps.Accessed:Apr.22,2021.[Online].
andtechnicallevels)havebeenpresented,whileconsidering Available:https://5g-ppp.eu/roadmaps/
|     |     |     |     |     |     | [14] C. B. | Stabell | and Ø. D. Fjeldstad, | ‘‘Configuring |     | value | for competitive |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | -------------------- | ------------- | --- | ----- | --------------- |
somebasicmodelsproposedbythe3GPPand5G-PPP.Ithas
advantage:Onchains,shops,andnetworks,’’StrategicManage.J.,vol.19,
beenshownthatseveralnon-convergentapproachesexistin
no.5,pp.413–437,May1998.
the literature, related to the definition of an ecosystem and [15] A.GawerandM.A.Cusumano,‘‘Industryplatformsandecosysteminno-
businessmodel.Thisstudyconsideredabusinessmodelasa vation,’’J.ProductInnov.Manage.,vol.31,no.3,pp.417–433,May2014.
partofamoregeneralecosystem.Whilethegeneralecosys- [16] 5G-PPP. (Apr. 2020). The 5G PPP Stakeholders Glossary. [Online].
|            |         |         |       |                            |     | Available: |     | https://5g-ppp.eu/revised-5g-ppp-stakeholders-picture-and- |     |     |     |     |
| ---------- | ------- | ------- | ----- | -------------------------- | --- | ---------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
| tems could | involve | a large | range | of entities/organizations, |     | glossary/  |     |                                                            |     |     |     |     |
thefocusofthisarticlehasbeenon5Goperationalbusiness [17] 5G-PPP Architecture Working Group. (Jun. 2019). View on 5G
|     |     |     |     |     |     | Architecture |     | V3.0. [Online]. | Available: | https://5g-ppp.eu/wp-content/ |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | ---------- | ----------------------------- | --- | --- |
models,limitedtothoseactorswhoareactiveandinteracting
uploads/2019/07/5G-PPP-5G-Architecture-White-Paper_v3.0_
for real-life system deployment and operation. A compara- PublicConsultation.pdf
tive overview of different BMs for 5G sliced systems has [18] A.GalisandK.Makhijani,‘‘Networkslicinglandscape:Aholisticarchi-
|                 |     |       |         |              |             | tectural | approach, | orchestration | and | management | with | applicability in |
| --------------- | --- | ----- | ------- | ------------ | ----------- | -------- | --------- | ------------- | --- | ---------- | ---- | ---------------- |
| been performed. | The | final | part of | this article | developed a |          |           |               |     |            |      |                  |
mobileandfixednetworksandclouds,’’inProc.IEEENetw.Softwariza-
| selection among | some | tailored | BM  | configurations, | adapted |     |     |     |     |     |     |     |
| --------------- | ---- | -------- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tion(NetSoft),Jun.2018,pp.1–121.
fordedicatedslices,aimingtoserveIoT,IoV/V2X,andmar- [19] TelecommunicationManagement;StudyonManagementandOrchestra-
itime vertical applications. Our technical solutions for IoT tionofNetworkSlicingforNextGenerationNetwork,documentTR28.801,
R15,V15.1.0,3GPP,Dec.2017.
connectivityinmaritimeapplicationshavealsobeenoutlined
[20] J.Ordonez-Lucena,P.Ameigeiras,D.Lopez,J.J.Ramos-Munoz,J.Lorca,
and these solutions are currently being implemented within and J. Folgueira, ‘‘Network slicing for 5G with SDN/NFV: Concepts,
ourongoingproject.Finally,someopenresearchissuesfrom architectures, and challenges,’’ IEEE Commun. Mag., vol. 55, no. 5,
the perspective of future 6G have been addressed and new pp.80–87,May2017.
|     |     |     |     |     |     | [21] 5G NORMA |     | Consortium. | 5G NORMA–5G |     | Novel Radio | Multiservice |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ----------- | --- | ----------- | ------------ |
challengesareidentified.
AdaptiveNetworkArchitecture.Accessed:Apr.29,2021.[Online].Avail-
able:http://www.it.uc3m.es/wnl/5gnorma/
APPENDIX
[22] 5GExchangeConsortium.5GExchange.5GExProject.H2020CORDIS
LISTOFABBREVIATIONS European Commission. Accessed: Apr. 29, 2021. [Online]. Available:
| SeeTable3. |     |     |     |     |     | https://cordis.europa.eu/project/id/671636/fr |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
[23] 5G-TRANSFORMERConsortium.5G–TRANSFORMERRefinedArchi-
REFERENCES
tectureProductionProperties.Accessed:Apr.29,2021.[Online].Avail-
able:http://5g-transformer.eu/
[1] B.M.Arnaut,D.B.Ferrari,andM.L.deOliveiraeSouza,‘‘Arequire-
|     |     |     |     |     |     | [24] 5G-MONARCH |     | Consortium. | Deliverables–5G |     | Mobile | Network |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --------------- | --- | ------ | ------- |
mentsengineeringandmanagementprocessinconceptphaseofcomplex
systems,’’inProc.IEEEInt.Symp.Syst.Eng.(ISSE),Oct.2016,pp.1–6. Architecture. Accessed: May 6, 2021. [Online]. Available: https://5g-
[2] I.Ielite,G.Olevsky,andT.Safiulins,‘‘Identificationandprioritization monarch.eu/deliverables/
ofstakeholdersintheplanningprocessofsustainabledevelopmentofthe [25] V.Sciancalepore,C.Mannweiler,F.Z.Yousaf,P.Serrano,M.Gramaglia,
smartcity,’’inProc.IEEE7thInt.Conf.Intell.Comput.Inf.Syst.(ICICIS), J.Bradford,andI.L.Pavon,‘‘Afuture-proofarchitectureformanagement
Dec.2015,pp.251–257. and orchestration of multi-domain NextGen networks,’’ IEEE Access,
[3] C.Suraci,G.Araniti,A.Abrardo,G.Bianchi,andA.Iera,‘‘Astakeholder- vol.7,pp.79216–79232,2019.
orientedsecurityanalysisinvirtualized5Gcellularnetworks,’’Comput. [26] TelecommunicationManagement;StudyonTenancyConceptin5GNet-
Netw.,vol.184,Jan.2021,Art.no.107604. works and Network Slicing Management, document TR 28804, 3GPP,
[4] C.Kalogiros,H.K.Hallingby,andO.B.Erdal,‘‘5Gecosystemdilemmas: V16.0.1,R16,Sep.2019.
Sharingrolesandrevenues,’’inProc.Eur.Conf.Netw.Commun.(EuCNC), [27] Pagoda Consortium. 5G!Pagoda—A Network Slice for Every Service.
Jun.2020,pp.144–148.
Accessed:Apr.22,2021.[Online].Available:https://5g-pagoda.aalto.fi/
[5] P.Camps-Arago,S.Delaere,andP.Ballon,‘‘5Gbusinessmodels:Evolving
[28] T.Taleb,I.Afolabi,K.Samdanis,andF.Z.Yousaf,‘‘Onmulti-domain
mobilenetworkoperatorrolesinnewecosystems,’’inProc.SmartCities
networkslicingorchestrationarchitectureandfederatedresourcecontrol,’’
Inf.Commun.Technol.(CTTE-FITCE),Sep.2019,pp.1–6. IEEENetw.,vol.33,no.5,pp.242–252,Sep./Oct.2019.
[6] A. Nuseibah and C. Wolff, ‘‘Business ecosystem analysis framework,’’ [29] NordicIoTCentre.WhitePaperontheRole-BaseIoTEcosystemModel.
inProc.IEEE8thInt.Conf.Intell.DataAcquisitionAdv.Comput.Syst.,
Accessed:Apr.22,2021.[Online].Available:https://nordiciot.dk/the-role-
Technol.Appl.(IDAACS),vol.2,Sep.2015,pp.501–505.
based-iot-ecosystem-model/
[7] Z.Li,X.Wang,andT.Zhang,‘‘Systemarchitectureandtechnological
[30] S.WijethilakaandM.Liyanage,‘‘SurveyonnetworkslicingforInternetof
basicsof5G,’’in5G+How5GChangetheSociety.Singapore:Springer,
Thingsrealizationin5Gnetworks,’’IEEECommun.SurveysTuts.,vol.23,
| 2021,ch.4.     |            |        |            |             |                | no.2,pp.957–994,2ndQuart.,2021. |          |             |       |     |        |             |
| -------------- | ---------- | ------ | ---------- | ----------- | -------------- | ------------------------------- | -------- | ----------- | ----- | --- | ------ | ----------- |
| [8] N. Bahari, | R. Maniak, | and V. | Fernandez, | ‘‘Ecosystem | business model |                                 |          |             |       |     |        |             |
|                |            |        |            |             |                | [31] 5G-PPP.                    | Business | Feasibility | Study | for | 5G V2X | Deployment. |
design,’’inProc.Int.Conf.StrategicManage.,Jun.2015,pp.1–18.
|     |     |     |     |     |     | Accessed: | Apr. | 22, 2021. | [Online]. | Available: | https://bscw.5g-ppp.eu/ |     |
| --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | --------- | ---------- | ----------------------- | --- |
[9] M.R.Palattella,M.Dohler,A.Grieco,G.Rizzo,J.Torsner,T.Engel,
pub/bscw.cgi/d293672/5G%20PPP%20Automotive%20WG_White%
andL.Ladid,‘‘InternetofThingsinthe5Gera:Enablers,architecture,
20Paper_Feb2019.pdf
| and business | models,’’ | IEEE | J. Sel. Areas | Commun., | vol. 34, no. 3, |     |     |     |     |     |     |     |
| ------------ | --------- | ---- | ------------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
pp.510–527,Mar.2016. [32] P.Lindberg,T.Abbas,Y.Zang,A.Laya,M.Fallgren,A.E.Fernandez,
[10] C.Yu,J.Li,C.Zhang,H.Li,R.He,andB.Lin,‘‘Maritimebroadbandcom- A. Servel, O. Sancier, R. Comte, E. Le Fur, M. Bouillon, M. Gharba,
|     |     |     |     |     |     | Z. Li, | and | G. Vivier. | Deliverable | D2.2 | Intermediate | Report on |
| --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | ----------- | ---- | ------------ | --------- |
munications:Applications,challengesandanoffshore5G-virtualMIMO
|     |     |     |     |     |     | V2X | Business | Models and | Spectrum | Document. | Accessed: | Apr. 22, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | --------- | --------- | -------- |
paradigm,’’inProc.IEEEInt.Conf.ParallelDistrib.Process.Appl.,Big
|     |     |     |     |     |     | 2021. | [Online]. | Available: | https://5gcar.eu/wp-content/uploads/2018/08/ |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --------- | ---------- | -------------------------------------------- | --- | --- | --- |
DataCloudComput.,Sustain.Comput.Commun.,SocialComput.Netw.
(ISPA/BDCloud/SocialCom/SustainCom),Dec.2020,pp.1286–1291. 5GCAR_D2.2_v1.0.pdf
[11] SOLID-B5GProjectHomepage.Accessed:Jul.21,2021.[Online].Avail- [33] ServiceRequirementsforEnhancedV2XScenarios,documentTS22.186,
| able:https://solid-b5g.upb.ro/ |     |     |     |     |     | R16,V16.2.0,3GPP,Jun.2019. |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
[12] G. Darzanos, C. Kalogiros, K. Papakonstantinopoulou, G. Stamoulis, [34] Study on Architecture Enhancements for the Evolved Packet System
|     |     |     |     |     |     | (EPS) | and the | 5G System | (5GS) to | Support | Advanced | V2X Services, |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --------- | -------- | ------- | -------- | ------------- |
G.Zois,P.Muschamp,G.Caruso,A.Gavras,M.B.Weiss,H.K.Hallingby,
H. Lønsethagen, D. Lopez, and J. A. Ordoñez-Lucena. D5.1 Ecosys- documentTR23.786,R16,V16.1.0,3GPP,Jun.2019.
temAnalysisandSpecificationofB&EKPIs.Accessed:Apr.22,2021. [35] ServiceRequirementsforV2XServices;Stage1,documentTS22.185,
[Online].Available:https://zenodo.org/record/3345665#.YIFcDtritPY R16,V16.0.0,3GPP,Jul.2020.
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     | 156645 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

E.Borcocietal.:Overviewof5GSlicingOBMsforIoV,MaritimeIoTApplicationsandConnectivitySolutions
[36] A.Alalewi,I.Dayoub,andS.Cherkaoui,‘‘On5G-V2Xusecasesand FRANK Y. LI (Senior Member, IEEE) received
enabling technologies: A comprehensive survey,’’ IEEE Access, vol. 9, thePh.D.degreefromtheDepartmentofTelem-
pp.107710–107737,2021. atics (now the Department of Information Secu-
[37] 5G-PPP, ‘‘5G automotive vision,’’ White Paper, Oct. 2015. Accessed: rityandCommunicationTechnology),Norwegian
May 6, 2021. [Online]. Available: https://5gppp.eu/wp-content/uploads/ University of Science and Technology (NTNU),
2014/02/5G-PPP-White-Paper-on-Automotive-Vertical-Sectors.pdf
|                 |                      |         |                |              |             |     |     | in 2003.   | He              | was a      | Senior    | Researcher with |
| --------------- | -------------------- | ------- | -------------- | ------------ | ----------- | --- | --- | ---------- | --------------- | ---------- | --------- | --------------- |
| [38] 5G-MONARCH | Consortium.          | 5G      | Mobile Network | Architecture | for         |     |     |            |                 |            |           |                 |
|                 |                      |         |                |              |             |     |     | the        | UniK-University | Graduate   |           | Center (now the |
| Diverse         | Services, Use Cases, | and     | Applications   | in 5G        | and Beyond. |     |     |            |                 |            |           |                 |
|                 |                      |         |                |              |             |     |     | Department | of              | Technology | Systems), | University      |
| Deliverables–5G | Mobile               | Network | Architecture.  | [Online].    | Available:  |     |     |            |                 |            |           |                 |
ofOslo,beforejoiningtheDepartmentofInforma-
https://5g-monarch.eu/deliverables/
[39] StudyonBusinessRoleModelsforNetworkSlicing,documentTR22.830, tionandCommunicationTechnology,University
|     |     |     |     |     |     | of Agder | (UiA), in | August 2007, | as an | Associate | Professor, | and then a |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ------------ | ----- | --------- | ---------- | ---------- |
R16,V16.1.0,3GPP,Dec.2018.
|     |     |     |     |     |     | Full Professor. | From | August | 2017 to July | 2018, | he was | a Visiting Pro- |
| --- | --- | --- | --- | --- | --- | --------------- | ---- | ------ | ------------ | ----- | ------ | --------------- |
[40] Y.Huo,X.Dong,andS.Beatty,‘‘Cellularcommunicationsinoceanwaves
fessorwiththeDepartmentofElectricalandComputerEngineering,Rice
formaritimeInternetofThings,’’IEEEInternetThingsJ.,vol.7,no.10,
University,Houston,TX,USA.Duringthepastfewyears,hehasbeenan
pp.9965–9979,Oct.2020.
[41] Telenor. Satellite Fleet. Accessed: May 6, 2021. [Online]. Available: active participant in multiple Norwegian and European research projects.
https://www.telenorsat.com/satellite-fleet/ HisresearchinterestsincludeMACmechanismsandroutingprotocolsin
[42] Y.Drif,E.Chaput,E.Lavinal,P.Berthou,B.TiomelaJou,O.Grémillet, 5G and beyond mobile systems and wireless networks, the Internet of
andF.Arnal,‘‘Anextensiblenetworkslicingframeworkforsatelliteinte- Things,meshandadhocnetworks,wirelesssensornetworks,D2Dcom-
grationinto5G,’’Int.J.Satell.Commun.Netw.,vol.39,no.4,pp.339–357,
munications,cooperativecommunications,cognitiveradionetworks,green
Jul.2021.
wirelesscommunications,dependabilityandreliabilityinwirelessnetworks,
[43] M.Giordani,M.Polese,M.Mezzavilla,S.Rangan,andM.Zorzi,‘‘Toward
QoS,resourcemanagement,andtrafficengineeringinwiredandwireless
6Gnetworks:Usecasesandtechnologies,’’IEEECommun.Mag.,vol.58,
IP-basednetworks,andtheanalysis,simulation,andperformanceevaluation
no.3,pp.55–61,Dec.2020. ofcommunicationprotocolsandnetworks.HewaslistedasaLeadScientist
[44] V.Ziegler,H.Viswanathan,H.Flinck,M.Hoffmann,V.Raisanen,and
bytheEuropeanCommissionDGRTDUnitA.03—EvaluationandMoni-
K.Hatonen,‘‘6Garchitecturetoconnecttheworlds,’’IEEEAccess,vol.8,
toringofProgrammes,inNovember2007.
pp.173508–173520,2020.
[45] L.U.Khan,I.Yaqoob,M.Imran,Z.Han,andC.S.Hong,‘‘6Gwireless
systems:Avision,architecturalelements,andfuturedirections,’’IEEE
Access,vol.8,pp.147029–147044,2020.
| [46] H. Tataria, | M. Shafi, A.  | F. Molisch, | M. Dohler,            | H.  | Sjöland, and |     |     |     |     |     |     |     |
| ---------------- | ------------- | ----------- | --------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| F.Tufvesson,     | ‘‘6G wireless | systems:    | Vision, requirements, |     | challenges,  |     |     |     |     |     |     |     |
insights,andopportunities,’’Proc.IEEE,vol.109,no.7,pp.1166–1199,
Jul.2021.
| [47] J. A. | Fraire, S. Céspedes, | and | N. Accettura, | ‘‘Direct-to-satellite |     |     |     |     |     |     |     |     |
| ---------- | -------------------- | --- | ------------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
IoT—Asurveyofthestateoftheartandfutureresearchperspectives,’’ MARIUS-CONSTANTIN VOCHIN received the
in Proc. Int. Conf. Ad-Hoc, Mobile, Wireless Netw. (ADHOC-NOW), Ph.D. degree in electronics and telecommunica-
|     |     |     |     |     |     |     |     | tions | from the | Faculty | of Electronics, | Telecom- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------- | --------------- | -------- |
Oct.2019,pp.241–258.
municationsandInformationTechnology(ETTI),
|     |     |     |     |     |     |     |     | University | Politehnica |     | of Bucharest | (UPB), |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------ | ------ |
EUGENBORCOCI(Member,IEEE)iscurrentlya in 2014, with a thesis topic on ‘‘Virtualization
ProfessorwiththeDepartmentofTelecommunica- MethodsforFutureInternet.’’
tion, Faculty of Electronics Telecommunications He is currently an Associate Professor with
and Information Technology (ETTI), University ETTI,UPB.Hehasbeentheprojectleaderora
PolitehnicaofBucharest(UPB).Hehaspublished teammemberinmultiplenationalandEuropean
severalbooksandover190scientificortechnical researchprojects,andhasservedasanevaluatorforseveralinternational
papers and scientific reports. As a team leader, researchprojectopencalls.Hehasbeenascientificreviewerformanyhigh
hehasparticipatedinmanyEuropeanandnational impactjournalsandconferencesinhisareaofresearchexpertise.Hehas
|     |     |     |     |     |     | authored | four books | and over | 65 scientific | papers, | and | teaches several |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ------------- | ------- | --- | --------------- |
researchprojects.Histeachingandresearchinter-
coursesandprovideslaboratoryguides.
|     | ests | and activities | are on | new technologies, | like |     |     |     |     |     |     |     |
| --- | ---- | -------------- | ------ | ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
SDN,NFV,cloud/fog/edgecomputing,4G/5Gnetworking,slicingservices,
andvehicularcommunications.
|     | ANA-MARIA |     | DRĂGULINESCU |     | (GraduateStu- |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
dentMember,IEEE)receivedtheB.Eng.degree
|     | in telecommunication |            | systems   | and        | technologies |     |     |     |     |     |     |     |
| --- | -------------------- | ---------- | --------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|     | and                  | the M.Eng. | degree in | multimedia | technolo-    |     |     |     |     |     |     |     |
gies in content production for audiovisual and KJETIL KJELLSTADLI received the master’s
communication from the Faculty of Electronics, degreeintelecommunicationsfromtheNorwegian
TelecommunicationsandInformationTechnology, University of Science and Technology (NTNU)
|     |            |             |     |           |           |     |     | (earlier | known | as NTH—Norwegian |     | Institute of |
| --- | ---------- | ----------- | --- | --------- | --------- | --- | --- | -------- | ----- | ---------------- | --- | ------------ |
|     | University | Politehnica | of  | Bucharest | (UPB), in |     |     |          |       |                  |     |              |
2014and2016,respectively.Sheiscurrentlypur- Technology).Hehas30yearsofexperienceintest-
suingthePh.D.degreewithathesistopicfocusing ingandoperationoftelecommunicationsystems.
ondevelopingandenhancingsensorsandtheIoTsystemsbasedonLPWAN At Telenor Maritime, he has technical responsi-
| technologies. |     |     |     |     |     |     |     | bilityforshipconnectivity(backhaul)andmobile |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
Since 2017, she has been a Research and Teaching Assistant with the solutions.HeiscurrentlyaTechnologySpecialist
Department of Telecommunications, UPB. Her main research interests atTelenorMaritimeAS.Heisofteninvolvedin
includeautomation,sensorsystemsandnetworks,theIoTandtheInternet writingoffersandtechnicalmattersregardingtheproducts.
ofMedicalThings,andLPWANcommunicationtechnologies.
| 156646 |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |