# Landscape of Architecture and Design Patterns for IoT Systems

> Source file: `Landscape of Architecture and Design Patterns for IoT Systems.pdf`

---

IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020 10091
Landscape of Architecture and Design
Patterns for IoT Systems
Hironori Washizaki , Member, IEEE, Shinpei Ogata, Member, IEEE, Atsuo Hazeyama, Member, IEEE,
Takao Okubo, Member, IEEE, Eduardo B. Fernandez, Senior Member, IEEE,
and Nobukazu Yoshioka , Member, IEEE
Abstract—Due to the widespread proliferation of today’s devices, such as sensors and actuators that are tied with the
InternetofThings(IoT),asystemdesignerneedstheIoTsystem physical entities to be monitored and manipulated), together
and software design patterns to assist in designing scalable and
in support of intelligent decision making to empower teams
replicablesolutions.Patternsareencapsulationsofreusablecom-
across the world [1].
mon problems and solutions under specific contexts. Many IoT
patterns have been published, such as IoT design patterns and Thus,IoTaimstobringconnectivitytoalmosteveryelectric
IoTarchitecturepatternstodocumentthesuccesses(andfailures) device in physical space. Although IoT extends connectivity
inIoTsystemsandsoftwaredevelopment.However,becausethese to everyday things, this increase in connectivity creates many
patternsarenotwellclassified,theiradoptiondoesnotliveupto
challenges [2]. Since the application spread in today’s IoT is
their potential. To understand the reasons, we conducted a sys-
wide and is typically structured in market-oriented groups, a
tematicliteraturereview.Fromthe32identifiedpapers,143IoT
architecture and design patterns were extracted. We analyzed system designer needs the IoT system and software design
these patterns according to several characteristics and outlined patternstoassistindesigningforscalableandreplicablesolu-
directions for improvements when publishing and adopting IoT tions [3]. Patterns are encapsulations of reusable common
patterns. Of the extracted patterns, 57% are non-IoT patterns,
problems and solutions under specific contexts. To document
suggesting that IoT systems and software are often designed via
thesuccesses(andfailures)inIoTsystemsandsoftwaredevel-
conventionalarchitectureanddesignpatternsthatarenotspecific
to IoT design. Although most IoT design patterns are applica- opment, IoT patterns, including IoT design patterns and IoT
ble to any domain, IoT architecture patterns tend to be domain architecture patterns, have been published.
specific,implyingthattheuniquenatureofIoTadoptioninspe- Ingeneral,systemsandsoftwaredesignprocesseshavetwo
cificdomainsappearsatthearchitecturelevel.Asmoredomains
major phases [4] with different abstraction levels: 1) archi-
adopt IoT, the number of domain-specific IoT design patterns
tecting (i.e., architectural design) and 2) design (i.e., detailed
shouldincrease.Intermsofqualityattributes,manyIoTpatterns
address compatibility, security, and maintainability. design). These two phases can be classified into two corre-
spondingtypes:1)architecturepatternsand2)designpatterns.
Index Terms—Architecture, design, Internet of Things (IoT),
Moreover, architecture patterns that do not emphasize prob-
patterns, survey, systematic literature review (SLR).
lems and rationales are called architecture styles. Although
some IoT architecture styles have been studied [5], IoT archi-
I. INTRODUCTION
tecture and design patterns at different abstraction levels are
THE INTERNET of Things (IoT) is expected to bridge
notwellclassified orresearched. Consequently, adopting such
diverse Internet collaborative technologies to enable new
patternsmaynotresolveproblemsorhavethedesiredimpact.
services and applications by connecting physical objects (i.e.,
The abstraction level can be important when describing,
examining, and reusing IoT patterns. The same is true for
ManuscriptreceivedNovember16,2019;revisedMay14,2020;accepted
June 3, 2020. Date of publication June 18, 2020; date of current version domain specificity and quality attributes. IoT is basically con-
October9,2020.ThisworkwassupportedinpartbyJSPSKAKENHIunder stituted of the traditional technical fields, such as wireless
Grant16H02804andGrant17K00475,andinpartbySCATandenPiT-Pro
sensor networks, and embedded and control systems. Thus,
SmartSE.(Correspondingauthor:HironoriWashizaki.)
Hironori Washizaki is with the Faculty of Science and Engineering, “IoT patterns” may not be exclusively IoT patterns. Non-IoT
WasedaUniversity,Tokyo1698555,Japan,alsowiththeNationalInstituteof patterns as well as some domain-specific IoT can be utilized
Informatics,Tokyo101-8430,Japan,alsowithSystemInformationCompany
for IoT systems and software design. Moreover, it is impor-
Ltd.,Tokyo104-0054,Japan,andalsowitheXmotionCompanyLtd.,Tokyo
141-0032,Japan(e-mail:washizaki@waseda.jp). tant to identify which quality attributes are addressed by the
Shinpei Ogata is with the Graduate School of Engineering, Faculty of target IoT pattern to be reused. IoT architecture and design
Engineering,ShinshuUniversity,Nagano390-8621,Japan.
patterns should address interoperability since, by definition,
Atsuo Hazeyama is with the Department of Information Science, Tokyo
GakugeiUniversity,Tokyo184-0015,Japan. IoTisaboutensuringinteroperabilityamongobjects.However,
Takao Okubo is with the Institute of Information Security, Kanagawa otherattributesmayalsobeaddressed.Basedonthedefinition
221-0835,Japan.
in ISO/IEC 25010:2011 [6], interoperability for IoT systems
EduardoB.FernandeziswiththeDepartmentofComputerandElectrical
EngineeringandComputerScience,FloridaAtlanticUniversity,BocaRaton, means the degree that two or more IoT devices and systems
FL33431USA. exchange and use information.
NobukazuYoshiokaiswiththeInformationSystemsArchitectureResearch
Thecontributionofthisarticleisanoverviewofthecurrent
Division,NationalInstituteofInformatics,Tokyo101-8430,Japan.
DigitalObjectIdentifier10.1109/JIOT.2020.3003528 landscape of IoT architecture and design patterns to identify
ThisworkislicensedunderaCreativeCommonsAttribution4.0License. Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/

10092 IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020
shortcomings and suggest improvements when publishing and interoperability issues and state-of-practices of IoT technolo-
adopting IoT patterns. Specifically, a complete set of IoT gies in the industry, which highlighted integration challenges
patterns available in the literature is analyzed. The authors related to IoT that have significantly shifted the landscape of
found32paperspublishedfrom2014–2018.Thefourresearch Internet-based collaborative services and applications.
questions below are intended to constructively determine the However, previous studies did not classify IoT architecture
direction for improvement. anddesignpatternsatdifferentabstractionlevels.Thisstudyis
RQ1. How does academic literature address IoT archi- the first comprehensive survey on IoT architecture and design
tecture and design patterns? To answer this question, we patterns.1
conducted a systematic literature review (SLR) of the aca-
demic literature. We analyzed the 32 identified papers and
III. SYSTEMATICLITERATUREREVIEW
extracted 143 patterns.
RQ2. Are all existing IoT architecture and design patterns A. Process and Query
really IoT patterns? To answer this question, we distin- We performed an SLR of the academic literature to collect
guished between architecture and design patterns specific to architectureanddesignpatternsforIoTsystemsandsoftware.
IoT systems and non-IoT patterns that are applicable to any An SLR aims to assess scientific papers and group con-
system or software design. Of the 143 patterns, 61 addressed cepts around a topic. We chose Scopus2 as the search engine
IoT-specific problems and solutions, and the remaining 82 since it is effectively used in SLRs of software engineering
were not IoT-specific patterns. and the search results can be exported. The database cov-
RQ3. Can IoT architecture and design patterns be classi- ers many major publishers, including IEEE, ACM, Springer
fied? To answer this question, we classified these IoT patterns Nature, Wiley Blackwell, Taylor & Francis, and Elsevier.
with respect to three characteristics: 1) abstraction level; Furthermore, the database provides a mechanism to perform
2) domain specificity; and 3) quality attributes. keyword searches.
RQ4. What IoT architecture and design patterns exist? To Fig. 1 overviews the process adopted to identify relevant
answer this question, we showed that IoT patterns not only papers. Our process has four steps as follows.
exist but are related to different abstraction levels, domain 1) InitialSearch:Weexecutedthefollowingqueryontitles,
specificities,andqualityattributes.Wealsoprovidedexamples abstracts,andkeywordsofpapersregardlessoftimeand
of such patterns. subjectarea.Weusednopublicationsperiodrestrictions.
The remainder of this article is organized as follows. We found 63 papers published from 2014 to 2018.
Section II summarizes related work. Section III presents our
"IoT" AND ( "design pattern" OR "
SLRanditsresults.SectionIVdiscussesourresults.SectionV
architecture pattern" )
concludes this article and provides a future direction.
2) Impurity Removal: Due to the nature of the involved
data source, the search results included elements that
are clearly not research papers, such as abstracts and
II. RELATEDWORK
international standards. Removing such results left 56
Surveys have been conducted on general architecture and papers.
designpatterns,e.g.,[7]–[9].Mostfocusontheobject-oriented 3) Inclusion and Exclusion Criteria: For each paper, two
design. Moreover, surveys on architecture and design pat- of the authors vetted whether they should be included
terns exist for specific domains and quality attributes, such in our SLR by applying the following criteria. First, the
as multiagent systems [10], machine learning systems [11], or titles and abstracts followed by the entire paper were
secure systems [12]. read to determine whether the paper pertained to IoT
Ahmadi et al. [13] conducted an SLR of IoT-specific to the architecture and design patterns. Using the definition of
healthcare domain. Asghari et al. [14] conducted an SLR of ourquery,32scholarlypapers[18]–[49]wereidentified.
IoTapplications.Giudice[15]conductedaliteraturereviewon a) Inclusion:PapersaddressingpatternstodesignIoT
the role of IoT on the business process management in terms systems and software that are written in English.
of promotion of knowledge flow, innovation, and competitive- b) Exclusion: Papers focusing on IoT but not explic-
ness.NoneofthesereviewsfocusedonIoTpatterns.Ray[16] itly dealing with architecture and design patterns
surveyed existing IoT cloud platforms. However, Ray’s work or duplicate papers of the same study.
is not formalized and the scope of it is limited to the domain 4) Data Extraction: The following information was col-
concerning IoT clouds. lectedfromeachpapertoanswertheresearchquestions:
For the domain of IoT systems and software design, publication title, publication year, publication venue,
case studies, best practices, and patterns are mostly avail- types of patterns proposed or used, pattern names,
able as independent documents. To grasp the entire picture,
several surveys have been reported [1], [5]. Muccini and 1This article is an extension of a paper presented at the 1st International
Moghaddam[5]conductedasystematicmappingstudyofIoT Workshop on Software Engineering Research & Practices for the IoT
architecture styles. They identified seven architecture styles, (SERP4IoT2019)[17].Inthisarticle,weextendresearchquestionsandpat-
tern analysis as well as corresponding discussions. We also added related
including layered architecture and service-oriented architec-
work.
ture. In addition, Aly et al. conducted an SLR of both IoT 2https://www.scopus.com/

WASHIZAKIetal.:LANDSCAPEOFARCHITECTUREANDDESIGNPATTERNSFORIoTSYSTEMS 10093
Amongthe143patterns,82(57%)wereconsiderednon-IoT
patterns in terms of domain specificity. Table I shows the list
ofextractednon-IoTarchitectureanddesignpatternsandtheir
abstraction levels (i.e., architecture style, architecture pattern,
or design pattern). 11 non-IoT patterns appeared in multiple
Fig. 1. Selection process and the number of papers remaining after each
papers:“publish-subscribe”[21],[22],[39],[48],[49],“client-
activity.
server” [39], [48], [49], “peer-to-peer” [39], [48], “represen-
tational state transfer” (REST) [48], [49], “service-oriented
architecture” (SOA) [39], [49], “role-based access control”
(RBAC)[27],[30],“model-view-controller”(MVC)[35],[43],
“reflection” [23], [42], “blockchain architecture style” [22],
[24],“strategy”[23],[30],and“observer”[30],[40].Theother
71 non-IoT patterns appeared in one paper only.
Fourteen papers [18], [21], [23], [26], [27], [35], [37],
[39], [41]–[43], [46], [48], [49] only used non-IoT patterns.
These results indicate that IoT systems and software are often
designedviaconventionalarchitectureanddesignpatternsthat
are not specific to IoT design. This is not unexpected since
IoT is constituted of traditional technical fields such as wire-
Fig.2. Numbersofdocumentsperyear. lesssensornetworks,embeddedandcontrolsystems,andother
supports. However, an alternative possibility is that practition-
ers are unaware of the existing IoT patterns. The existing IoT
domain names in the case of domain-specific IoT pat- patternssupportpractitionerstoplananddesigntheirownIoT
terns, and quality attributes addressed. systems and software.
There are 61 IoT patterns (i.e., 43%) in 18 papers [19],
B. RQ1. How Does Academic Literature Address IoT [20], [22], [24], [25], [28]–[34], [36], [38], [40], [44], [45],
Architecture and Design Patterns? [47] that address specific problems and solutions in IoT. The
details are discussed in the subsequent section.
Our SLR revealed that IoT architecture and design patterns
RQ2. Are all existing IoT architecture and design pat-
are very popular due to the promotion of IoT systems and
terns really IoT patterns? Of the extracted patterns, 57% are
software in recent years. Fig. 2 shows the annual trend in
non-IoT patterns, suggesting that IoT systems and software
the number of papers related to IoT architecture and design
are often designed via conventional architecture and design
patterns by publication type.
patterns that are not specific to IoT design.
The most common publication types are conference papers
(17), journals (7), workshops (5), symposiums (2), and a ref-
ereed book chapter (1). The most common publication type is
conference papers followed by journals, suggesting that cer- D. RQ3. Can IoT Architecture and Design Patterns Be
tain IoT patterns are maturing. However, the high number of Classified?
conference papers suggests that the entire topic of IoT archi-
Through our SLR and while reading the documents, we
tecture and design patterns is in its early stage. Since 2016,
noted various characteristics that could help classify patterns.
IoT patterns have garnered increased research attention each
We observed that IoT patterns are often presented in a con-
year.
text with an abstraction level, domain specificity, and quality
RQ1. How does academic literature address the IoT archi-
attribute to be addressed.
tecture and design patterns? There are 32 academic papers
1) Abstraction Level: Patterns to design IoT systems and
related to IoT architecture and design patterns. Most are con-
software can be classified into two types: 1) architecture pat-
ference papers followed by journal publications. The high
ternsand2)designpatterns.Inaddition,therearetwodifferent
number of conference papers indicates that the entire topic
terms in the literature with respect to the nature of archi-
of IoT architecture and design patterns is in its early stage,
tecture patterns: 1) “architecture style” and 2) “architecture
but the presence of journal articles suggests that some types
pattern.” Both refer to recurring solutions that solve prob-
of IoT patterns are maturing.
lems at the architecture design level and provide a common
vocabulary to facilitate communication [7]. The key differ-
C. RQ2. Are All Existing IoT Architecture and Design
ence is that architecture patterns address problem–solution
Patterns Really IoT Patterns?
pairs with contexts and rationales behind particular solutions,
Five of the authors plus two researchers indicated in the while architecture styles address the structure with constraints
acknowledgmentreadaseventhofthepapers.Foreachpaper, without explicit attention to the problem [7]. By definition,
patterns were extracted and the specificity of the content to architecture styles are located at a higher abstraction level
IoT was analyzed. All patterns were independently vetted by comparedtoarchitecturepatternssincearchitecturestyleshave
another author. Overall, the 32 papers contained 143 patterns. less information.

10094 IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020
TABLEI
LISTOFEXTRACTEDNON-IOTPATTERNS(AS:ARCHITECTURESTYLE,AP:ARCHITECTUREPATTERN,ANDDP:DESIGNPATTERN)
Thus, IoT design patterns can be classified into the follow- architecture patterns contain more information than
ing three types in terms of abstraction level. architecture styles (i.e., highly abstract design descrip-
1) High Abstraction Level: Architecture styles are patterns tions)whilestilladdressingtheentiresoftwareorsystem
that specify architectural elements and connections at a design rather than specific parts. On the other hand,
veryhighabstractionlevel.Theseareoftenusedinearly design patterns address specific parts of the system
phases, such as analysis and architecture design. For design(i.e.,lowabstractdesigndescriptions).Forexam-
example,“layeredarchitectureforIoTapplications”[44] ple, “entity-component-attribute (ECA) on linked data
addressesagenerallayeredIoTarchitecturewithoutany platform” [32] recommends a specific architecture to
concreteproblemorrationale.Hence,architecturestyles improve the changeability and reusability of IoT soft-
are regarded as highly abstract. ware components over different domains on the linked
2) Medium Abstraction Level: Unlike architecture styles, data platform by establishing the structural mapping
medium recommends concrete architecture designs of from ECA to the platform as semantic Web of Things
IoT systems and software to address recurrent architec- (WoT). Hence, architecture patterns are regarded as
tural problems such as ensuring interoperability among medium abstract.
heterogeneousdevices.Thesearchitecturalelementsand 3) LowAbstractionLevel:Therearerecommendeddetailed
connections are often documented as architecture pat- designs to address recurrent detailed design problems
terns that encapsulate contexts, recurring problems, such as enabling proper communications among soft-
and corresponding solutions. The abstraction level of ware modules while keeping high extensibility. Since
architecture patterns is between high and low since these patterns target specific modules or limited parts

WASHIZAKIetal.:LANDSCAPEOFARCHITECTUREANDDESIGNPATTERNSFORIoTSYSTEMS 10095
TABLEII
| and | not | the entire | software |     | or system, | the | abstrac- |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | -------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
PATTERNSBYABSTRACTIONLEVELANDDOMAINSPECIFICITY(AS:
tion level of the design patterns is regarded as low. ARCHITECTURESTYLE,AP:ARCHITECTUREPATTERN,AND
These are often used in the detailed design and con- DP:DESIGNPATTERN)
| struction          |                   | phases.   | For example, |             | “pull information” |               | [38]     |     |          |     |            |          |           |     |              |
| ------------------ | ----------------- | --------- | ------------ | ----------- | ------------------ | ------------- | -------- | --- | -------- | --- | ---------- | -------- | --------- | --- | ------------ |
| recommends         |                   | a         | detailed     | design      | of the             | communication |          |     |          |     |            |          |           |     |              |
| structure          |                   | between   | IoT          | devices     | and gateways.      |               | Hence,   |     |          |     |            |          |           |     |              |
| design             | patterns          |           | are regarded | as          | low abstract.      |               |          |     |          |     |            |          |           |     |              |
| 2) Domain          | Specificity:      |           | Domain       | specificity |                    | is important  |          | to  |          |     |            |          |           |     |              |
| examine            | the applicability |           | and          | reusability | of each            | IoT           | pattern. |     |          |     |            |          |           |     |              |
| It is divided      | into              | three     | types:       | 1) non      | IoT; 2)            | general       | IoT; and |     |          |     |            |          |           |     |              |
| 3) domain-specific |                   | IoT.      |              |             |                    |               |          |     |          |     |            |          |           |     |              |
|                    |                   |           |              |             |                    |               |          | For | example, | the | IoT design | patterns | described |     | in [38] such |
| 1) Non-IoT         |                   | Patterns: | General      | systems     | and                | software      | archi-   |     |          |     |            |          |           |     |              |
tecture patterns as well as design patterns that can as “application launch” are dedicated to usability only, while
“edgeorchestration”[34]addressesmanyattributes,including
| be       | adopted | to design    | IoT | systems | and           | software | if the   |             |     |                      |     |     |     |     |     |
| -------- | ------- | ------------ | --- | ------- | ------------- | -------- | -------- | ----------- | --- | -------------------- | --- | --- | --- | --- | --- |
|          |         |              |     |         |               |          |          | reliability |     | and maintainability. |     |     |     |     |     |
| contexts |         | and problems |     | match   | the patterns’ |          | contexts |             |     |                      |     |     |     |     |     |
and problems. There are 82 non-IoT patterns, such RQ3. Can IoT architecture and design patterns be clas-
|     |     |       |          |      |       |       |           | sified? | Patterns |     | for IoT | systems | and | software | can be |
| --- | --- | ----- | -------- | ---- | ----- | ----- | --------- | ------- | -------- | --- | ------- | ------- | --- | -------- | ------ |
| as  | MVC | [35], | [43] and | RBAC | [27], | [30], | which are |         |          |     |         |         |     |          |        |
well-accepted general architecture and design patterns. divided along three main characteristics: 1) abstraction level;
|            |       |               |            |                  |         |            |       | 2)  | domain    | specificity; | and          | 3) quality | attributes. |          |        |
| ---------- | ----- | ------------- | ---------- | ---------------- | ------- | ---------- | ----- | --- | --------- | ------------ | ------------ | ---------- | ----------- | -------- | ------ |
| 2) General |       | IoT Patterns: |            | IoT architecture |         | and design | pat-  |     |           |              |              |            |             |          |        |
| terns,     | which | are           | applicable |                  | to any  | IoT system | or    |     |           |              |              |            |             |          |        |
| software.  |       | Examples      | include    | “IoT             | gateway | event      | sub-  |     |           |              |              |            |             |          |        |
|            |       |               |            |                  |         |            |       | E.  | RQ4. What | IoT          | Architecture | and        | Design      | Patterns | Exist? |
| scription” |       | [29]          | and “pull  | information”     |         | [38] since | these |     |           |              |              |            |             |          |        |
are originally described in the context of IoT systems Table II shows the distribution of IoT and non-IoT pat-
and software, and not specific to a certain problem or terns by abstraction level and domain specificity. Table III
technical domain. lists the 61 IoT architecture and design patterns. Table III can
3) Domain-specific IoT Patterns: IoT architecture and be a guide for practitioners to identify available IoT patterns
design patterns that address specific problem domains in terms of abstraction level, domain specificity, and quality
| (such | as  | healthcare) | and | technical | domains |     | (such as | attributes. |     |     |     |     |     |     |     |
| ----- | --- | ----------- | --- | --------- | ------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
brain–computer interactions). For example, “operator- Surprisingly,onlytwopatterns“OCM”[19],[47]and“com-
controller-module (OCM)” [19], [47] is a problem- putation offloading” [22], [33] are mentioned in multiple
domain-specific pattern since it addresses a specific papers. The rest appear in one paper, demonstrating that IoT
problem and solution in the cyber–physical control patterns are not shared or recognized by different research
domain such as operating organic Rankine cycle tur- groups. This may be due to their short history. To avoid con-
bines. fusion, potential pattern authors should check the existing IoT
3) Quality Attribute: All systems and software design pat- patterns carefully before publishing their own “new” patterns.
terns are expected to address one or more quality attributes. Intermsofabstractionlevel,manyIoTdesignpatterns(i.e.,
|     |     |     |     |     |     |     |     | 42/61 | =   |     |     |     |     |     | (16/61 = |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | -------- |
For example, IoT design patterns should mostly address 69%) and some IoT architecture patterns
interoperability, which is defined as a subattribute of com- 26%) exist, but only a few represent IoT architecture styles
| patibility | in ISO/IEC |     | 25010:2011 | [6] | since, | by  | definition, | (3/61=5%). |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ---------- | --- | ------ | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
IoT is about ensuring interoperability among objects. To In terms of domain specificity, 41 patterns (i.e., 67%) are
classify IoT patterns, we use all quality attributes except generalIoT,whiletheremaining20patterns(33%)arespecific
for functional suitability defined in ISO/IEC 25010:2011, to a problem or technical domain (Table II).
which is a well-accepted quality model system, and select Reviewingthecombinationsofabstractionlevelanddomain
terms from software engineering: performance, compatibility, specificity, most of the IoT design patterns are applicable
usability, reliability, security, maintainability, and portability. to any domain. In contrast, many IoT architecture pat-
We excluded functional suitability because certain functional terns exist for specific domains, implying that the unique
requirements are often satisfied by concrete system and soft- nature of IoT adoption in specific domains often appears
ware design decisions, including reuse of IoT platforms and at the architecture level. Design details seem to be com-
software libraries, instead of reuse of abstract architecture monly addressed by general IoT design patterns or non-IoT
or design patterns. Without concrete functional requirements, design patterns. This is not surprising since IoT is constituted
it is difficult to determine whether a pattern contributes to of traditional technical fields. In the future, the number of
functional suitability. specific IoT design patterns may increase as more domains
| Additionally, |     | there | are emerging | quality | attributes |     | that are | adopt | IoT. |     |     |     |     |     |     |
| ------------- | --- | ----- | ------------ | ------- | ---------- | --- | -------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
not defined in ISO/IEC 25010:2011 but are common in IoT In terms of quality attributes, more than 80% of IoT pat-
developmentandoperation.Possiblecandidatesarescalability terns address compatibility (including interoperability as a
and privacy. subattribute),security,andmaintainability.Thisfindingisrea-
We observed that some IoT patterns are dedicated to one sonable since major concerns in IoT adoption revolve around
orfewqualityattributes,whileothersaddressmanyattributes. theseattributes.Asexpected,mostIoTarchitectureanddesign

10096 IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020
TABLEIII
LISTOFIOTPATTERNS(AS:ARCHITECTURESTYLE,AP:ARCHITECTUREPATTERN,DP:DESIGNPATTERN,PE:PERFORMANCE,C:COMPATIBILITY,
U:USABILITY,R:RELIABILITY,SE:SECURITY,M:MAINTAINABILITY,PO:PORTABILITY,SC:SCALABILITY,ANDPR:PRIVACY)
patterns address interoperability. On the other hand, connec- IoTsecuritypatternshavebeenrequiredandpublishedtomit-
tivity is at the core of IoT, and every communication channel igate vulnerabilities. Maintainability is well addressed in IoT
needstobesecuredagainstattacks.Moreover,thenumberand patterns since IoT systems and software often address various
heterogeneityofobjectscanincreasetheattacksurface.Hence, devices and their different lifecycles.

WASHIZAKIetal.:LANDSCAPEOFARCHITECTUREANDDESIGNPATTERNSFORIoTSYSTEMS 10097
TABLEIV
OVERVIEWOFPAPERSMENTIONINGIOTPATTERNS(REFERENCES
INDICATINGPAPERSOFDOMAIN-SPECIFICIOTPATTERNS)
Fig.3. LayeredarchitecturestyleforIoTapplications(adaptedfrom[44]).
Inaddition,someIoTpatternsaddressperformance,usabil-
event subscription” [29] as an example of IoT design pattern.
ity,reliability,andscalability.Weobservedthattheseattributes
For brevity, participants, collaborations, implementation, and
are also important to address in IoT systems and software.
knownusesareomitted.Theintentsectionofeachpatterncan
Consequently, other quality attributes are less researched.
beaguideforpractitionerstounderstandandconsiderreusing
For example, only a few IoT patterns address portability and
the corresponding content.
privacy. In the future, IoT patterns addressing these attributes
1) Example of IoT Architecture Style:
are anticipated by accumulating more design cases focusing
a) Pattern name: Layered architecture for IoT
on these attributes since they are also important.
applications [44].
Asanadditionalguideforpractitionerstofindpapersabout
b) Intent: Support the construction of hierarchical, pro-
IoTpatterns,TableIVshowsthedistributionofpaperscontain-
grammable, and autonomic IoT applications.
ing IoT patterns by abstraction level, domain specificity, and
c) Solution: TheIoTplatformprovidingresourcevirtual-
influence of the quality attributes addressed by the patterns.
ization using lightweight virtualization (i.e., containerization)
According to ISO/IEC 25010:2011 [6], performance, usabil-
for multilayer applications (Fig. 3).
ity,reliability,andsecuritysignificantlyinfluencethequalityin
d) Consequences: By implementing the respective
useforprimaryusers,whilecompatibility,maintainability,and
requirements of an IoT application to the appropriate layer of
portability greatly impact quality in use for secondary users
thethreelayersshowninFig.3,nonfunctionalproperties,such
who maintain the system. We classify these additional quality
asperformance,securityandprivacy,reliability,elasticity,and
attributes as privacy and scalability. The former is an impor-
scalability can be treated flexibly with service orchestration
tantconcern ofprimaryusers,whilethelatterisabouteaseof
through the layers.
extending a system by maintainers in terms of performance.
2) Example of IoT Architecture Pattern:
InTableIV,mostpapersuseIoTpatternstoaddressquality
a) Pattern name: ECA2LD [32].
attributes that influence the quality in use for primary users
as well as those that influence the quality in use for main- b) Intent: Support the design of changeable and main-
tenance tasks. Because this implies that IoT systems should tainablesoftwarecomponentsforlarge-scaleIoTapplications.
be designed with good quality for both primary users and c) Context: The Web is considered as an IoT con-
maintainers, the identified IoT patterns should help support vergence platform to realize WoT. Software built for IoT
architecting and design. environments must be adaptable to changes and interoperable
RQ4. What IoT architecture and design patterns exist? IoT with others on the platform.
architecture patterns and design patterns exist. Many IoT pat- d) Problem: ECA-based software design (Fig. 4) is par-
terns address compatibility (including interoperability as a ticularlywellsuitedtoimprovethechangeabilityandreusabil-
subattribute), security, and maintainability. Most IoT design ity of IoT software components. However, seamless cross-
patternsareapplicabletoanydomain.Ontheotherhand,many domain interoperability between independently developed IoT
IoTarchitecturepatternsaredomainspecific,implyingthatthe applications and platforms is not directly addressed.
unique nature of IoT adoption in specific domains appears at e) Solution: It establishes a structural mapping from
the architecture level. ECA to the Linked Data Platform so that the interoperability
of independently developed IoT applications can be seamless
over different domains on the platform.
IV. DISCUSSION
f) Consequences: This data-oriented approach should
We describe extracted IoT patterns, possible use cases, and
significantly improve the changeability of entities and reuse
threats to validate our results.
of IoT software components. Mapping the entire architecture
makes it easy to implement large-scale IoT applications to
A. Examples of IoT Pattern Semantic WoT.
Here, we describe three extracted IoT patterns having dif- 3) Example of IoT Design Pattern:
ferent abstraction levels: 1) “layered architecture for IoT a) Pattern name: IoT gateway event subscription [29].
applications” [44] as an example of IoT architecture style; b) Intent: Provide interoperability between two hetero-
2) “ECA on linked data platform (ECA2LD)” [32] as an geneous IoT devices, while simultaneously ensuring that the
example of IoT architecture pattern; and 3) “IoT gateway IoT gateway has flexibility.

10098 IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020
can also support writing new patterns to consider appropri-
ateabstractionlevels,domainspecificity,andqualityattributes
to be addressed. In addition, the practitioners and researchers
eventually extend the existing IoT architecture and design
patterns.
UC2(ToResolveIoTDesignProblems):Whenpractitioners
and researchers want to resolve problems in the IoT design,
ourclassificationresultsandthecharacteristicsofIoTpatterns
helpthemtocomparetheexistingIoTpatterns,andthenselect
and reuse the appropriate one according to their objectives.
Developers can utilize our classification scheme and results in
different development phases.
1) Toconsidertheappropriatehigh-levelIoTsystemarchi-
tecture in the analysis phase as well as the early
Fig.4. ECA(adaptedfrom[32]).
architecting phase in IoT system development projects,
c) Context: Thispatternisusedwithinevent-basedcom- developers can first review non-IoT or IoT architecture
munication when the data are pushed (pulled) to (from) the styles of the given projects by examining the relevance
IoTgatewayasynchronously.TheIoTgatewayallowsfordata between the contexts, architectural elements, and their
forwarding. connections.
d) Problem: Interoperabilitybetweentwoheterogeneous 2) To design concrete architectures of the target IoT
IoT devices requires bidirectional, asynchronous communica- systems and software in the architecting phase, devel-
tion with the ability to publish, filter, and consume data. opers can also consider reusing (non-) IoT architecture
e) Solution: Employ a subscription mechanism into the patterns by examining the relevance between projects’
IoT gateway, which allows asynchronous and mutual trans- specific requirements, contexts, and problems of the
missions of data obtained by sensors at the destination and architecture patterns.
the message between artifacts. Transmitters of messages (i.e., 3) To design limited parts of the target IoT systems and
publishers) can publish messages using defined classes with- software in the design phase, developers can consider
out knowledge of subscribers. Meanwhile, subscribers can reusing (non-) IoT design patterns by examining rel-
express interest in one or more classes, and receive messages evance between specific detailed design problems and
of interest without knowledge of publishers. The IoT gate- contexts of the design patterns.
way works flexibly in two parts. The physical part deals with UC3 (To communicate and Research IoT Patterns): Our
networkaccessandcommunicationprotocols,whilethevirtual classificationresultsandthecharacteristicsofIoTpatternscan
partdealswiththeremaininggatewayoperationsandservices. serve as a reference for the IoT pattern engineering commu-
The former is platform specific. It depends on the network nity,includingpractitionersandresearchers.Ourresultscanbe
communication protocols and devices deployed in physical extended by peers, providing the community with an impor-
space. In contrast, the latter is platform-independent. tant body of knowledge to guide future communications and
f) Consequences: Encouraging asynchronous messaging research on IoT patterns.
improves the compatibility of IoT applications using hetero-
geneous IoT devices. Enhancing the loose coupling between C. Threats to Validity
publishersandsubscribersimprovesthemaintainabilityofIoT
As an empirical study, the results of SLRs are vulnerable
applications.Inaddition,decouplingtheIoTgatewayintotwo
to internal validity and reliability [50]. Internal validity arises
parts realizes flexibility in the device-to-device layer.
fromthecause–effectconclusiondrawnfromtheSLRprocess
g) Related patterns: “D2D REST request/re-
and its results. To alleviate this, we used the data to answer
sponse” pattern [29], and “publish-subscribe” pattern
each research question.
[21], [22], [39], [48], [49].3
Reliability concerns arise from the quality and rigor that
the SLR was conducted. To demonstrate a sound process,
B. Use Cases SectionIIIexplainsthestepsinourSLRandreportsthenum-
The results of our SLR are expected to guide practitioners ber of papers in each step. In addition, all of our data are
andresearchersinthefollowingpossibleusecasesUC1–UC3. available online.4
UC1 (To Publish New IoT Patterns): When practitioners Another threat to reliability is that an independent third
(and researchers) want to write and publish their new IoT party has yet to vet all the identified patterns. The Pattern
architecture and design patterns, they can be aware of the Languages of Programs (PLoP) conference series,5 such as
existing IoT patterns by referring to our classification results. PLoP6 and AsianPLoP,7 which is sponsored by the Hillside
The characteristics of IoT patterns identified in our SLR
4http://www.washi.cs.waseda.ac.jp/iot-patterns/
3“IoT gateway event subscription” can be regarded as a general IoT 5https://hillside.net/conferences/
design pattern since it is originally described as a slight extension of 6https://www.hillside.net/plop/
“publish-subscribe”inthecontextofIoT[29]. 7http://asianplop.org

WASHIZAKIetal.:LANDSCAPEOFARCHITECTUREANDDESIGNPATTERNSFORIoTSYSTEMS 10099
Group, focuses on pattern writing groups to improve patterns andmaintainability.Consequently,otherqualityattributeshave
throughgroupexposure.Weintendtoparticipateintheconfer- yet to be investigated.
ence series to receive community feedback about each pattern Our future work includes further analysis of IoT pat-
prior to publication. terns using additional characteristics, such as the relationships
Most authors extracted and classified patterns. All patterns among patterns and writing quality of patterns (as discussed
were independently vetted by another author. Although our in [55] for security patterns). We also plan to increase our
rigorous SLR noted the characteristics of IoT patterns, other survey scope to include gray literature.
characteristics to be used for the classification of IoT patterns We plan to share the revised survey and analysis results to
maybeomitted.Itispossiblethatourclassificationresultsare obtainreviewsfromthepublic.Weexpectthattheresearchcom-
not completely correct. To analyze the extent of this threat to munitywillfurthervalidatetheSLRresultsfromtheviewpoints
reliability in terms of pattern extraction and classification, we ofpractitionersandresearchers.Publicinputshouldextendthe
asked two uninvolved researchers (R 1 and R 2 ) to extract and classification to include new characteristics and data sets.
| classify | patterns | from | [32] and | [44] | studied | in our | SLR. We |     |     |     |     |     |     |     |     |
| -------- | -------- | ---- | -------- | ---- | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
selectedthesepapers[32],[44]sincetheydonotdescribepat-
ACKNOWLEDGMENT
ternsinanyexplicitstructuredpatternformat.Thus,therewas
apossibilitythatdifferentexaminersmayextractdifferentpat- The authors would like to thank Dr. Takehisa Kato and
|          |          |      |              |      |       |     |               | Prof. Haruhiko |     | Kaiya | for their | initial | pattern | analysis, | and |
| -------- | -------- | ---- | ------------ | ---- | ----- | --- | ------------- | -------------- | --- | ----- | --------- | ------- | ------- | --------- | --- |
| terns or | classify | them | differently. | From | [44], | R 1 | extracted the |                |     |       |           |         |         |           |     |
Dr.TakafumiTanakaandHideyukiKanukafortheiradditional
| same architecture |     | style | as our | result | (i.e., layered |     | architecture |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | ------ | ------ | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
patternanalysis.Theyalsowouldliketothanktheanonymous
| for IoT  | applications) |          | while | R 2 extracted |            | a similar   | but more |           |           |            |     |          |     |              |     |
| -------- | ------------- | -------- | ----- | ------------- | ---------- | ----------- | -------- | --------- | --------- | ---------- | --- | -------- | --- | ------------ | --- |
|          |               |          |       |               |            |             |          | reviewers | for their | insightful |     | comments | and | suggestions. |     |
| concrete | architecture  | pattern. |       | Interms       | of quality | attributes, | R        |           |           |            |     |          |     |              |     |
2
| commonly | identified |     | performance, | reliability, |     | security, | scala- |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------------ | ------------ | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
bility,andprivacy,whicharealsoidentifiedbyusinTableIII. REFERENCES
| In contrast, | R   | identified | compatibility, |     | maintainability, |     | porta- |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | -------------- | --- | ---------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1
bility, and scalability; these attributes except for scalability [1] M. Aly, F. Khomh, Y. Guéhéneuc, H. Washizaki, and S. Yacout, “Is
fragmentationathreattothesuccessoftheInternetofThings?”IEEE
are different from our result. From [32], R and R extracted Internet Things J., vol. 6, no. 1, pp.472–487, Feb. 2019. [Online].
|     |     |     |     |     |     | 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the same or similar patterns as our result (i.e., ECA2LD), but Available:https://doi.org/10.1109/JIOT.2018.2863180
[2] M.Aly,F.Khomh,M.Haoues,A.Quintero,andS.Yacout,“Enforcing
| classified | them    | as design   | patterns | unlike     | our            | classification. | In    |          |             |     |           |             |     |            |            |
| ---------- | ------- | ----------- | -------- | ---------- | -------------- | --------------- | ----- | -------- | ----------- | --- | --------- | ----------- | --- | ---------- | ---------- |
|            |         |             |          |            |                |                 |       | security | in Internet |     | of Things | frameworks: | A   | systematic | literature |
| terms of   | quality | attributes, | R        | identified | compatibility, |                 | main- |          |             |     |           |             |     |            |            |
2 review,” Internet Things, vol. 6, Jun. 2019, Art. no. 100050. [Online].
tainability, and portability, which are also identified by us in Available:https://doi.org/10.1016/j.iot.2019.100050
|                         |          |            |       |               |             |                 |          | [3] J. Höller, | V.       | Tsiatsis,   | and C.       | Mulligan, | “Toward | a machine | intel-       |
| ----------------------- | -------- | ---------- | ----- | ------------- | ----------- | --------------- | -------- | -------------- | -------- | ----------- | ------------ | --------- | ------- | --------- | ------------ |
| Table III.              | R 1 also | identified |       | compatibility |             | and portability | but      |                |          |             |              |           |         |           |              |
|                         |          |            |       |               |             |                 |          | ligence        | layer    | for diverse | industrial   |           | IoT use | cases,”   | IEEE Intell. |
| missed maintainability. |          |            | Based | on these      | independent |                 | analysis |                |          |             |              |           |         |           |              |
|                         |          |            |       |               |             |                 |          | Syst.,         | vol. 32, | no.         | 4, pp.64–71, | Aug.      | 2017.   | [Online]. | Available:   |
results, we believe that our pattern extraction results can be https://doi.org/10.1109/MIS.2017.3121543
generally consistent. However, our classification process can [4] “Software engineering—Guide to the software engineering body of
|     |     |     |     |     |     |     |     | knowledge | (SWEBOK),” |     | ISO/IEC, |     | Geneva, | Switzerland, | Rep. TR |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | --- | ------- | ------------ | ------- |
besomewhatinconsistentresultinginpartiallydifferentclassi-
19759:2015,2015.
fication results by different examiners. To mitigate this threat, [5] H. Muccini and M. T. Moghaddam, “IoT architectural styles—A
wehavesharedourclassificationresultswiththepublictocall systematic mapping study,” in Proc. 12th Eur. Conf. Softw. Archit.
|              |     |     |         |        |         |     |     | (ECSA), | Madrid, | Spain, | Sep. | 2018, | pp.68–85. | [Online]. | Available: |
| ------------ | --- | --- | ------- | ------ | ------- | --- | --- | ------- | ------- | ------ | ---- | ----- | --------- | --------- | ---------- |
| for comments | on  | our | website | in the | future. |     |     |         |         |        |      |       |           |           |            |
https://doi.org/10.1007/978-3-030-00761-4_5
| We used | Scopus | as  | the initial | document |     | base | of the SLR. |              |     |          |                     |     |     |              |         |
| ------- | ------ | --- | ----------- | -------- | --- | ---- | ----------- | ------------ | --- | -------- | ------------------- | --- | --- | ------------ | ------- |
|         |        |     |             |          |     |      |             | [6] “Systems | and | software | engineering—Systems |     |     | and software | quality |
Although many other SLRs, such as [11] and [51]–[53] have requirements and evaluation (SQuaRE)—System and software quality
models,”ISO/IEC,Geneva,Switzerland,Rep.25010:2011,2011.
| adopted | it, relevant |     | papers | (such | as IoT | security | pattern |                 |     |          |                |     |          |             |         |
| ------- | ------------ | --- | ------ | ----- | ------ | -------- | ------- | --------------- | --- | -------- | -------------- | --- | -------- | ----------- | ------- |
|         |              |     |        |       |        |          |         | [7] P. Avgeriou | and | U. Zdun, | “Architectural |     | patterns | revisited—A | pattern |
papers[54])mayhavebeenmissed.Tomitigatethisthreat,we
language,”inProc.10thEur.Conf.PatternLang.Programs(EuroPLoP),
plan to use other databases, extend our SLR, and elicit public Irsee,Germany,Jul.2005,pp.431–470.
review of the results. [8] A. Ampatzoglou, S. Charalampidou, and I. Stamelos, “Research state
|     |     |     |               |     |     |     |     | of the  | art on | GoF     | design           | patterns: | A mapping | study,”   | J. Syst.   |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ------- | ------ | ------- | ---------------- | --------- | --------- | --------- | ---------- |
|     |     |     |               |     |     |     |     | Softw., | vol.   | 86, no. | 7, pp.1945–1964, |           | 2013.     | [Online]. | Available: |
|     |     |     | V. CONCLUSION |     |     |     |     |         |        |         |                  |           |           |           |            |
https://doi.org/10.1016/j.jss.2013.03.063
To overview the current landscape of IoT architecture and [9] B. B. Mayvan, A. Rasoolzadegan, and Z. G. Yazdi, “The state of
design patterns, we conducted an SLR of the academic litera- the art on design patterns: A systematic mapping of the literature,”
|     |     |     |     |     |     |     |     | J. Syst. | Softw., | vol.125, | pp.93–118, |     | Mar. 2017. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ---------- | --- | ---------- | --------- | ---------- |
tureandidentifiedthe143patternsmentionedin32papers.Of https://doi.org/10.1016/j.jss.2016.11.030
the extracted patterns, 57% are non-IoT patterns, suggesting [10] J. Juziuk, D. Weyns, and T. Holvoet, “Design patterns for multi-agent
|                     |         |     |          |           |          |         |             | systems:                | A systematic |             | literature        | review,” | in Agent-Oriented |       | Software   |
| ------------------- | ------- | --- | -------- | --------- | -------- | ------- | ----------- | ----------------------- | ------------ | ----------- | ----------------- | -------- | ----------------- | ----- | ---------- |
| that IoT            | systems | and | software | are often | designed |         | via conven- |                         |              |             |                   |          |                   |       |            |
|                     |         |     |          |           |          |         |             | Engineering—Reflections |              |             | on Architectures, |          | Methodologies,    |       | Languages, |
| tional architecture |         | and | design   | patterns  | that     | are not | specific    | to                      |              |             |                   |          |                   |       |            |
|                     |         |     |          |           |          |         |             | and                     | Frameworks.  | Heidelberg, |                   | Germany: | Springer,         | 2014, | pp.79–99.  |
the IoT design. Although most IoT design patterns are appli- [Online].Available:https://doi.org/10.1007/978-3-642-54432-3_5
[11] H.Washizaki,H.Uchida,F.Khomh,andY.-G.Gueheneuc,“Studying
| cable to | any domain, |     | IoT architecture |     | patterns | tend | to be for |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ---------------- | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
softwareengineeringpatternsfordesigningmachinelearningsystems,”
specificdomains,implyingthattheuniquenatureofIoTadop-
|     |     |     |     |     |     |     |     | in Proc. | 10th | Int. Workshop |     | Empirical | Softw. | Eng. Pract. | (IWESEP), |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------- | --- | --------- | ------ | ----------- | --------- |
tion in specific domains appears at the architecture level. In Tokyo,Japan,2019,pp.1–6.
the future, the number of domain-specific IoT design patterns [12] P. Ponde and S. Shirwaikar, “An exploratory study of the secu-
|              |     |      |         |       |      |          |            | rity design | pattern | landscape |        | and their | classification,” |           | Int. J. Syst. |
| ------------ | --- | ---- | ------- | ----- | ---- | -------- | ---------- | ----------- | ------- | --------- | ------ | --------- | ---------------- | --------- | ------------- |
| may increase | as  | more | domains | adopt | IoT. | In terms | of quality |             |         |           |        |           |                  |           |               |
|              |     |      |         |       |      |          |            | Syst.       | Eng.,   | vol. 7,   | no. 3, | pp.26–43, | 2016.            | [Online]. | Available:    |
attributes, many IoT patterns address compatibility, security, https://doi.org/10.4018/IJSSE.2016070102

| 10100 |     |     |     |     |     |     |     | IEEEINTERNETOFTHINGSJOURNAL,VOL.7,NO.10,OCTOBER2020 |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[13] H. Ahmadi, G. Arji, L. Shahmoradi, R. Safdari, M. Nilashi, and [32] T.Spieldenner,R.Schubotz,andM.Guldner,“ECA2LD:Fromentity-
M. Alizadeh, “The application of Internet of Things in healthcare: A component-attribute runtimes to linked data applications,” in Proc.
systematic literature review and classification,” Univ. Access Inf. Soc., Int. Workshop Semantic Web Things Ind. Extend. Semantic Web Conf.
| vol.18,pp.1–33,May2018. |     |     |     |     |     |     |     | (ESWC),Jun.2018,pp.1–12. |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
[14] P. Asghari, A. M. Rahmani, and H. H. S. Javadi, “Internet of [33] S. Chen, B. Liu, X. Chen, Y. Zhang, and G. Huang, “Framework for
Things applications: A systematic review,” Comput. Netw., vol.148, adaptivecomputationoffloadinginIoTapplications,”inProc.9thAsia–
pp.241–261,Jan.2019. Pac.Symp.Internetware,Shanghai,China,Sep.2017,pp.1–6.[Online].
Available:https://doi.org/10.1145/3131704.3131717
| [15] M. D. | Giudice, | “Discovering |     | the Internet | of  | Things | (IoT) within the |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------------ | --- | ------------ | --- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
business process management: A literature review on technological [34] S. Qanbari et al., “IoT design patterns: Computational con-
revitalization,”Bus.ProcessManag.J.,vol.22,no.2,pp.1–9,2016. structs to design, build and engineer edge applications,” in Proc.
[16] P. P. Ray, “A survey of IoT cloud platforms,” Future Comput. 1st IEEE Int. Conf. Internet Things Design Implement. (IoTDI),
Informat. J., vol. 1, no. 1, pp.35–46, 2016. [Online]. Available: Berlin, Germany, Apr. 2016, pp.277–282. [Online]. Available:
https://doi.org/10.1109/IoTDI.2015.18
http://www.sciencedirect.com/science/article/pii/S2314728816300149
[17] H. Washizaki et al., “Landscape of IoT patterns,” in Proc. 1st Int. [35] M. P. Shopov, “IoT gateway for smart metering in electri-
WorkshopSoftw.Eng.Res.Pract.InternetThings,(SERP4IoT@ICSE), cal power systems–software architecture,” in Proc. 40th Int.
Montreal, QC, Canada, May 2019, pp.57–60. [Online]. Available: Convention Inf. Commun. Technol. Electron. Microelectron.
|     |     |     |     |     |     |     |     | (MIPRO), | May | 2017, | pp.974–978. |     | [Online]. |     | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | ----------- | --- | --------- | --- | ---------- |
https://dl.acm.org/citation.cfm?id=3354013
https://doi.org/10.23919/MIPRO.2017.7973565
[18] W.LeeandP.Law,“Acasestudyinapplyingsecuritydesignpatterns
[36] A.Q.Gill,N.Phennel,D.Lane,andV.L.Phung,“IoT-enabledemer-
forIoTsoftwaresystem,”inProc.Int.Conf.Appl.Syst.Innov.(ICASI),
May2017,pp.1162–1165. gency information supply chain architecture for elderly people: The
[19] C. Wolff, M. Knirr, K. Priebe, P. Schulz, and J. Strumberg, “A australian context,” Inf. Syst., vol. 58, pp.75–86, Jun. 2016. [Online].
Available:https://doi.org/10.1016/j.is.2016.02.004
| layered | software | architecture |     | for a | flexible | and smart | organic rank- |     |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --- | ----- | -------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[37] S.Vorapojpisut,“Model-baseddesignofIoT/WSNnodes:Devicedriver
| ine      | cycle (ORC) | turbine–solutions |                |     | and case | study,”   | Inf. Technol. |                  |     |          |            |          |     |               |          |
| -------- | ----------- | ----------------- | -------------- | --- | -------- | --------- | ------------- | ---------------- | --- | -------- | ---------- | -------- | --- | ------------- | -------- |
|          |             |                   |                |     |          |           |               | implementation,” |     | in Proc. | Int. Conf. | Embedded |     | Syst. Intell. | Technol. |
| Control, | vol.        | 47, no.           | 2, pp.349–362, |     | 2018.    | [Online]. | Available:    |                  |     |          |            |          |     |               |          |
https://doi.org/10.5755/j01.itc.47.2.19681 Int. Conf. Inf. Commun. Technol. Embedded Syst. (ICESIT-ICICTES),
[20] M.H.Syed,E.B.FernÁndez,andM.Ilyas,“Apatternforfogcomput- May2018,pp.1–5.
|     |     |     |     |     |     |     |     | [38] M. Brambilla, | E.  | Umuhoza, | and | R. Acerbis, | “Model-driven |     | develop- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | ----------- | ------------- | --- | -------- |
ing,”inProc.10thTravellingConf.PatternLang.ProgramsVikingPLoP,
mentofuserinterfacesforIoTsystemsviadomain-specificcomponents
| Leerdam, | The | Netherlands, | Apr. | 2016, | pp.1–10. | [Online]. | Available: |     |     |     |     |     |     |     |     |
| -------- | --- | ------------ | ---- | ----- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
andpatterns,”J.InternetServicesAppl.,vol.8,no.1,pp.1–21,2017.
https://doi.org/10.1145/3022636.3022649
[Online].Available:https://doi.org/10.1186/s13174-017-0064-1
| [21] L. | Roffia | et al., | “A  | semantic | publish-subscribe |     | architec- |     |     |     |     |     |     |     |     |
| ------- | ------ | ------- | --- | -------- | ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ture for the Internet of Things,” IEEE Internet Things J., [39] B. Tekinerdogan and Ö. Köksal, “Pattern based integration of Internet
|      |        |                  |     |      |       |           |            | of Things | systems,” | in  | Proc. 3rd | Int. Conf. | Internet | Things | (ICIOT) |
| ---- | ------ | ---------------- | --- | ---- | ----- | --------- | ---------- | --------- | --------- | --- | --------- | ---------- | -------- | ------ | ------- |
| vol. | 3, no. | 6, pp.1274–1296, |     | Dec. | 2016. | [Online]. | Available: |           |           |     |           |            |          |        |         |
ServicesConf.Federat.(SCF),Seattle,WA,USA,Jun.2018,pp.19–33.
https://doi.org/10.1109/JIOT.2016.2587380
[Online].Available:https://doi.org/10.1007/978-3-319-94370-1_2
| [22] N. Ntuli | and | A. M. | Abu-Mahfouz, |     | “A simple | security | architecture |     |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------------ | --- | --------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[40] M.A.Walker,A.Dubey,A.Laszka,andD.C.Schmidt,“PlaTIBART:
| for smart | water | management |     | system,” | in Proc. | 7th Int. | Conf. Ambient |     |     |     |     |     |     |     |     |
| --------- | ----- | ---------- | --- | -------- | -------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Syst.Netw.Technol.(ANT)6thInt.Conf.Sustain.EnergyInf.Technol. A platform for transactive IoT blockchain applications with repeat-
abletesting,”inProc.4thWorkshopMiddlewareAppl.InternetThings
(SEIT)AffiliatedWorkshops,Madrid,Spain,May2016,pp.1164–1169.
|     |     |     |     |     |     |     |     | (M4IoT@Middleware), |     |     | Las Vegas, | NV, | USA, Dec. | 2017, | pp.17–22. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------- | --- | --------- | ----- | --------- |
[Online].Available:https://doi.org/10.1016/j.procs.2016.04.239
[Online].Available:https://doi.org/10.1145/3152141.3152392
| [23] E. Jung, | I.  | Cho, and | S. M. | Kang, | “An agent | modeling | for over- |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ----- | ----- | --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[41] V.Cardellini,T.G.Grbac,M.Nardelli,N.Tankovic,andH.L.Truong,
| coming | the | heterogeneity | in  | the IoT | with design | patterns,” | in Proc. |     |     |     |     |     |     |     |     |
| ------ | --- | ------------- | --- | ------- | ----------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
“QoS-basedelasticityforservicechainsindistributededgecloudenvi-
Mobile Ubiquitous Intell. Comput. (MUSIC) FTRA 4th Int. Conf. ronments,”inAutonomousControlforaReliableInternetofServices—
| Mobile | Ubiquitous |     | Intell. | Comput., | Gwangju, | South | Korea, Sep. |          |         |             |     |             |             |     |            |
| ------ | ---------- | --- | ------- | -------- | -------- | ----- | ----------- | -------- | ------- | ----------- | --- | ----------- | ----------- | --- | ---------- |
|        |            |     |         |          |          |       |             | Methods, | Models, | Approaches, |     | Techniques, | Algorithms, |     | and Tools. |
2013,pp.69–74.[Online].Available:https://doi.org/10.1007/978-3-642-
|     |     |     |     |     |     |     |     | Cham, Switzerland: |     | Springer, | 2018, | pp.182–211. |     | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | ----- | ----------- | --- | --------- | ---------- |
40675-1_11
https://doi.org/10.1007/978-3-319-90415-3_8
[24] C.Pahl,N.E.Ioini,S.Helmer,andB.Lee,“Anarchitecturepatternfor [42] M. Mongiello, G. Boggia, and E. D. Sciascio, “ReIOS: Reflective
trusted orchestration in IoT edge clouds,” in Proc. 3rd Int. Conf. Fog architecting in the Internet of objects,” in Proc. 4rd Int.
MobileEdgeComput.(FMEC),Barcelona,Spain,Apr.2018,pp.63–70.
|     |     |     |     |     |     |     |     | Conf. | Model | Driven | Eng. | Softw. | Develop. | (MODELSWARD), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ---- | ------ | -------- | ------------- | --- |
[Online].Available:https://doi.org/10.1109/FMEC.2018.8364046
|     |     |     |     |     |     |     |     | Rome, | Italy, | Feb. | 2016, | pp.384–389. | [Online]. |     | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---- | ----- | ----------- | --------- | --- | ---------- |
[25] V.Charpenay,S.Käbisch,D.Anicic,andH.Kosch,“Anontologydesign
https://doi.org/10.5220/0005800603840389
patternforIoTdevicetaggingsystems,”inProc.5thInt.Conf.Internet [43] M.A.Al-Taee,W.Al-Nuaimy,Z.J.Muhsin,andA.Al-Ataby,“Robot
Things (IoT), Seoul, South Korea, Oct. 2015, pp.138–145. [Online]. assistantinmanagementofdiabetesinchildrenbasedontheInternetof
Available:https://doi.org/10.1109/IOT.2015.7356558
Things,”IEEEInternetThingsJ.,vol.4,no.2,pp.437–445,Apr.2017.
[26] S.PapeandK.Rannenberg,“ApplyingprivacypatternstotheInternet
[Online].Available:https://doi.org/10.1109/JIOT.2016.2623767
| of Things’ |     | (IoT) architecture,” |     | Mobile | Netw. | Appl., | vol. 24, no. | 3,               |     |             |     |        |              |     |            |
| ---------- | --- | -------------------- | --- | ------ | ----- | ------ | ------------ | ---------------- | --- | ----------- | --- | ------ | ------------ | --- | ---------- |
|            |     |                      |     |        |       |        |              | [44] H. Khazaei, | H.  | Bannazadeh, |     | and A. | Leon-Garcia, |     | “SAVI-IoT: |
pp.925–933,2019.[Online].Available:https://doi.org/10.1007/s11036- A self-managing containerized IoT platform,” in Proc. 5th IEEE
018-1148-2 Int. Conf. Future Internet Things Cloud (FiCloud), Prague,
[27] I.AliandM.Asif,“Applyingsecuritypatternsforauthorizationofusers Czech Republic, Aug. 2017, pp.227–234. [Online]. Available:
| in IoT | based | applications,” |     | in Proc. | Int. Conf. | Eng. | Emerg. Technol. |     |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | --- | -------- | ---------- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1109/FiCloud.2017.27
(ICEET),Feb.2018,pp.1–5.
|     |     |     |     |     |     |     |     | [45] A. Mazayev, |     | J. A. | Martins, | and | N.  | Correia, | “Semantic |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | -------- | --- | --- | -------- | --------- |
[28] S.J.R.MéndezandJ.K.Zao,“BCIontology:Acontext-basedsense Web thing architecture,” in Proc. 4th Exp. Int. Conf.,
and actuation model for brain-computer interactions,” in Proc. 9th Int. Faro, Portugal, Jun. 2017, pp.43–46. [Online]. Available:
Semantic Sensor Netw. (SSN) Workshop Colocated 17th Int. Semantic https://doi.org/10.1109/EXPAT.2017.7984368
WebConf.(ISWC),Monterey,CA,USA,Oct.2018,pp.32–47.[Online].
|     |     |     |     |     |     |     |     | [46] A. Auger, | E.  | Exposito, | and | E. Lochin, |     | “Sensor | observation |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ---------- | --- | ------- | ----------- |
Available:http://ceur-ws.org/Vol-2213/paper3.pdf
|     |     |     |     |     |     |     |     | streams | within | cloud-based | IoT | platforms: | Challenges |     | and direc- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | --- | ---------- | ---------- | --- | ---------- |
[29] R. Tkaczyk et al., “Cataloging design patterns for Internet of Things tions,” in Proc. 20th Conf. Innov. Clouds Internet Netw. (ICIN),
artifact integration,” in Proc. IEEE Int. Conf. Commun. Workshops Paris, France, Mar. 2017, pp.177–184. [Online]. Available:
(ICC),KansasCity,MO,USA,May2018,pp.1–6.[Online].Available: https://doi.org/10.1109/ICIN.2017.7899407
https://doi.org/10.1109/ICCW.2018.8403758 [47] C. Wolff et al., “Software architecture for an ORC turbine—Case
| [30] K. | Periyasamy, | V.  | S. Alagar, | and | K. Wan, | “Dependable | design |           |                |     |           |        |        |        |              |
| ------- | ----------- | --- | ---------- | --- | ------- | ----------- | ------ | --------- | -------------- | --- | --------- | ------ | ------ | ------ | ------------ |
|         |             |     |            |     |         |             |        | study for | an intelligent |     | technical | system | in the | era of | the Internet |
for elderly health care,” in Proc. Federated Conf. Comput. Sci. of Things,” in Proc. 23rd Int. Conf. Inf. Softw. Technol. , (ICIST),
Inf. Syst. (FedCSIS), Sep. 2017, pp.803–806. [Online]. Available: Druskininkai, Lithuania, Oct. 2017, pp.226–237. [Online]. Available:
https://doi.org/10.15439/2017F261 https://doi.org/10.1007/978-3-319-67642-5_19
[31] G. Bloom, B. Alsulami, E. Nwafor, and I. C. Bertolotti, “Design [48] P.M.JacobandP.Mani,“Softwarearchitecturepatternselectionmodel
patterns for the industrial Internet of Things,” in Proc. 14th IEEE for Internet of Things based systems,” IET Softw., vol. 12, no. 5,
Int. Workshop Factory Commun. Syst. (WFCS), Jun. 2018, pp.1–10. pp.390–396, 2018. [Online]. Available: https://doi.org/10.1049/iet-
| [Online].Available:https://doi.org/10.1109/WFCS.2018.8402353 |     |     |     |     |     |     |     | sen.2017.0206 |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |

WASHIZAKIetal.:LANDSCAPEOFARCHITECTUREANDDESIGNPATTERNSFORIoTSYSTEMS 10101
[49] V. Taratukhin, Y. Yadgarova, and J. Becker, “The Internet of Things Atsuo Hazeyama (Member, IEEE) received the
prototypingplatformunderthedesignthinkingmethodology,”inProc. Doctoral degree in information engineering from
125thASEEAnnu.Conf.Expo.Amer.Soc.Eng.Educ.,2018,pp.1–9. ShinshuUniversity,Nagano,Japan,in1999.
[50] X. Zhou, Y. Jin, H. Zhang, S. Li, and X. Huang, “A map of threats He is a Professor with the Department of
tovalidityofsystematicliteraturereviewsinsoftwareengineering,”in Information Science, Tokyo Gakugei University,
Proc.23rdAsia–Pac.Softw.Eng.Conf.,Dec.2016,pp.153–160. Tokyo, Japan. His research interests are support of
[51] H.Washizakietal.,“Taxonomyandliteraturesurveyofsecuritypattern securesoftwaredevelopment,collaborativesoftware
research,” in Proc. IEEE Conf. Appl. Inf. Netw. Security (AINS), Nov. development, and project-based learning for soft-
| 2018,pp.87–92. |     |     |     |     |     |     |     |     | waredevelopment. |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
[52] A. Dadwal, H. Washizaki, Y. Fukazawa, T. Iida, M. Mizoguchi, and Dr.HazeyamahasservedasaProgramCommittee
K.Yoshimura,“Prioritizationinautomotivesoftwaretesting:Systematic Memberforsomeinternationalconferences,includ-
literature review,” in Proc. 6th Int. Workshop Quantitative Approaches ing the International Conference on Software Engineering Education and
Softw. Quality Colocated 25th Asia–Pac. Softw. Eng. Conf. (APSEC), Training, Asia–Pacific Software Engineering Conference, and Knowledge
Nara, Japan, Dec. 2018, pp.52–58. [Online]. Available: http://ceur- BasedandIntelligentInformationandEngineeringSystems.
ws.org/Vol-2273/QuASoQ-07.pdf
| [53] A. B. | Marques, | R.  | Rodrigues, | and T. | Conte, | “Systematic | literature |     |     |     |     |     |     |
| ---------- | -------- | --- | ---------- | ------ | ------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
reviewsindistributedsoftwaredevelopment:Atertiarystudy,”inProc.
IEEE7thInt.Conf.GlobalSoftw.Eng.,Aug.2012,pp.134–143.
| [54] E. B. | FernÁndez, | N.  | Yoshioka, | and H. | Washizaki, | “Abstract |     | and IoT |             |          |       |          |          |
| ---------- | ---------- | --- | --------- | ------ | ---------- | --------- | --- | ------- | ----------- | -------- | ----- | -------- | -------- |
|            |            |     |           |        |            |           |     |         | Takao Okubo | (Member, | IEEE) | received | the M.S. |
securitysegmentationpatterns,”inProc.8thAsianConf.PatternLang.
|     |     |     |     |     |     |     |     |     | degree in | engineering | from | the Tokyo | Institute |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | --------- | --------- |
Programs(AsianPLoP),2019,pp.1–9.
[55] T.Heyman,K.Yskout,R.Scandariato,andW.Joosen,“Ananalysisof of Technology, Tokyo, Japan, in 1991, and the
thesecuritypatternslandscape,”inProc.3rdInt.WorkshopSoftw.Eng. Ph.D. degree in informatics from the Institute of
InformationSecurity,Kanagawa,Japan,in2009.
SecureSyst.(SESS),Minneapolis,MN,USA,May2007,p.3.[Online].
HeisaProfessorwiththeInstituteofInformation
Available:https://doi.org/10.1109/SESS.2007.4
|     |     |     |     |     |     |     |     |     | Security.  | From 1991    | to            | 2013, he | worked as a  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------------- | -------- | ------------ |
|     |     |     |     |     |     |     |     |     | Researcher | in software  | engineering   |          | and software |
|     |     |     |     |     |     |     |     |     | security   | with Fujitsu | Laboratories. |          | In 2013, he  |
movedtotheInstituteofInformationSecurityasan
AssociateProfessor.Hiscurrentinterestsaresecure
|     |     | Hironori |     | Washizaki | (Member, | IEEE) | received | the developmentandthreatanalysis. |     |     |     |     |     |
| --- | --- | -------- | --- | --------- | -------- | ----- | -------- | --------------------------------- | --- | --- | --- | --- | --- |
Doctoraldegreeininformationandcomputerscience
Dr.OkuboisamemberofIEICE,IPSJ,ACM,andIEEECS.
fromWasedaUniversity,Tokyo,Japan,in2003.
|     |     |          | He is a    | Professor | and the   | Associate    | Dean        | of the    |     |     |     |     |     |
| --- | --- | -------- | ---------- | --------- | --------- | ------------ | ----------- | --------- | --- | --- | --- | --- | --- |
|     |     | Research |            | Promotion | Division, | Waseda       | University, |           |     |     |     |     |     |
|     |     | and      | a Visiting | Professor | with      | the National |             | Institute |     |     |     |     |     |
ofInformatics.HealsoworksinindustryasOutside
Director of System Information and eXmotion. He Eduardo B. Fernandez (Eduardo Fernandez
has led many academia–industry joint research and Buglioni)(SeniorMember,IEEE)receivedtheB.S.
large-fundedprojectsinsoftwareanalysisandqual- degree in electrical engineering from Universidad
|     |     |     |            |       |          |          |     |         | Técnica Federico |     | Santa Maria, | Valparaíso, | Chile, |
| --- | --- | --- | ---------- | ----- | -------- | -------- | --- | ------- | ---------------- | --- | ------------ | ----------- | ------ |
|     |     | ity | assurance. | Since | 2017, he | has been | the | lead on |                  |     |              |             |        |
alarge-scalegrantatMEXT,calledenPiT-ProSmartSE,whichencompasses the M.S. degree in electrical engineering from
professionaleducationinIoT,AI,softwareengineering,andbusiness.Since Purdue University, Lafayette, IN, USA, in 1963,
2015,hehasbeentheConvenerofISO/IEC/JTC1SC7/WG20tostandardize andthePh.D.degreeincomputersciencefromthe
UniversityofCaliforniaLosAngeles(UCLA),Los
| bodies of | knowledge | and professional |     | certifications. |     | He has | published | more |     |     |     |     |     |
| --------- | --------- | ---------------- | --- | --------------- | --- | ------ | --------- | ---- | --- | --- | --- | --- | --- |
than 120 research papers in refereed international journals and conferences, Angeles,CA,USA,in1972.
includingIoT-J,TETC,EMSE,SCICO,ICSE,andASE.Hisresearchinterests He is a Professor with the Department of
includesystemsandsoftwareengineering. ComputerScienceandEngineering,FloridaAtlantic
Dr. Washizaki has received various awards and honors, including the University, Boca Raton, FL, USA. He is an active consultant for industry,
includingassignmentswithIBM,AlliedSignal,Panasonic,Motorola,Lucent,
| IWESEP | Best Paper | Award | and | the IJSEKE | Most | Read | Article. | He has |     |     |     |     |     |
| ------ | ---------- | ----- | --- | ---------- | ---- | ---- | -------- | ------ | --- | --- | --- | --- | --- |
servedastheProgramChairofmultipleIEEEconferences,includingICST, andHuawei.Hehaspublishednumerouspapersaswellasseveralbookson
CSEE&T,andSIoT/SISAofCOMPSAC.HeistheProgramChairofICPC computersecurityandsoftwarearchitecture,andnumerouspapersonautho-
ProgrammingEducationTrackandSCAMEngineeringTrack,theWorkshop rization models, object-oriented analysis and design, cloud computing, and
ChairandthePublicityChairofASE,aLocalChairofCOMPSAC,andthe securitypatterns.Hehaswrittenfourbooksonthesesubjects,themostrecent
beingabookonsecuritypatterns.
ChairofIEEECSJapanChapter.HeservesastheChairoftheIEEEComputer
SocietyProfessionalandEducationalActivitiesBoardEngineeringDiscipline
Committee.HeisspearheadingtheGuidetotheSoftwareEngineeringBody
ofKnowledge(SWEBOK)evolution.HeservesasanAssociateEditorforthe
| IEEE TRANSACTIONS |        | ON     | EMERGING | TOPICS     | IN COMPUTING, |          | a           | Steering |     |     |     |     |     |
| ----------------- | ------ | ------ | -------- | ---------- | ------------- | -------- | ----------- | -------- | --- | --- | --- | --- | --- |
| Committee         | Member | of the | IEEE     | Conference | on            | Software | Engineering |          |     |     |     |     |     |
Education and Training, and an Advisory Committee Member of the IEEE Nobukazu Yoshioka (Member, IEEE)received the
|             |            |          |        |         |              |           |        |       | B.E. degree  | in electronic |             | and information | engi-      |
| ----------- | ---------- | -------- | ------ | ------- | ------------ | --------- | ------ | ----- | ------------ | ------------- | ----------- | --------------- | ---------- |
| CS flagship | conference | COMPSAC. |        | He is a | Professional | Member    | of     | IEEE- |              |               |             |                 |            |
|             |            |          |        |         |              |           |        |       | neering from | Toyama        | University, | Toyama,         | Japan,     |
| Eta Kappa   | Nu. Since  | 2019,    | he has | been a  | Steering     | Committee | Member | of    |              |               |             |                 |            |
|             |            |          |        |         |              |           |        |       | in 1993,     | and the       | M.E.        | and Ph.D.       | degrees in |
APSEC.
informationsciencefromtheSchoolofInformation
|     |     |     |     |     |     |     |     |     | Science, | Japan Advanced | Institute | of  | Science and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --------- | --- | ----------- |
Technology,Nomi,Japan,in1995and1998,respec-
|     |     | Shinpei | Ogata | (Member, | IEEE) | received | the | M.E. | tively. |     |     |     |     |
| --- | --- | ------- | ----- | -------- | ----- | -------- | --- | ---- | ------- | --- | --- | --- | --- |
degree in electrical engineering and computer sci- HeisaResearcherwiththeNationalInstituteof
ence and the Ph.D. degree in functional control Informatics, Tokyo, Japan. From 1998 to 2002, he
systems from the Shibaura Institute of Technology, waswithToshibaCorporation,Tokyo.From2002to
Tokyo,Japan,in2009and2012,respectively. 2004,hewasaResearcher,andsinceAugust2004,hehasbeenanAssociate
He is an Associate Professor with Shinshu Professor with the National Institute of Informatics. His research interests
University, Nagano, Japan. His current research include Security and privacy software engineering and software engineering
|     |     | interests |     | include | model-driven | engineering |     | for formachinelearning-basedsystems. |     |     |     |     |     |
| --- | --- | --------- | --- | ------- | ------------ | ----------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
informationsystemdevelopment. Dr.YoshiokawasaBoardMemberofJSSSTfrom2011to2015,andhas
Dr.OgataisamemberofACM,IEICE,IPSJ,and beentheAuditorsince2018.HewastheChairoftheIEEECSJapanChapter
|     |     | JSSST. |     |     |     |     |     | from2015to2017. |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |