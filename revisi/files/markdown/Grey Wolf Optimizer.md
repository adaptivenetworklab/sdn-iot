# Grey Wolf Optimizer

> Source file: `Grey Wolf Optimizer.pdf`

---

AdvancesinEngineeringSoftware69(2014)46–61
ContentslistsavailableatScienceDirect
Advances in Engineering Software
journal homepage: www.elsevier.com/locate/advengsoft
Grey Wolf Optimizer
Seyedali Mirjalilia,⇑ , Seyed Mohammad Mirjalilib, Andrew Lewisa
aSchoolofInformationandCommunicationTechnology,GriffithUniversity,NathanCampus,BrisbaneQLD4111,Australia
bDepartmentofElectricalEngineering,FacultyofElectricalandComputerEngineering,ShahidBeheshtiUniversity,G.C.1983963113,Tehran,Iran
a r t i c l e i n f o a b s t r a c t
Articlehistory: Thisworkproposesanewmeta-heuristiccalledGreyWolfOptimizer(GWO)inspiredbygreywolves
Received27June2013 (Canis lupus). The GWO algorithm mimics the leadership hierarchy and hunting mechanism of grey
Receivedinrevisedform18October2013 wolvesinnature.Fourtypesofgreywolvessuchasalpha,beta,delta,andomegaareemployedforsim-
Accepted11December2013
ulatingtheleadershiphierarchy.Inaddition,thethreemainstepsofhunting,searchingforprey,encir-
Availableonline21January2014
clingprey,andattackingprey,areimplemented.Thealgorithmisthenbenchmarkedon29well-known
test functions, and the results are verified by a comparative study with Particle Swarm Optimization
Keywords:
(PSO), Gravitational Search Algorithm (GSA), Differential Evolution (DE), Evolutionary Programming
Optimization
(EP),andEvolutionStrategy(ES).TheresultsshowthattheGWOalgorithmisabletoprovideverycom-
Optimizationtechniques
petitiveresultscomparedtothesewell-knownmeta-heuristics.Thepaperalsoconsiderssolvingthree
Heuristicalgorithm
Metaheuristics classicalengineeringdesignproblems(tension/compressionspring,weldedbeam,andpressurevessel
Constrainedoptimization designs)andpresentsarealapplicationoftheproposedmethodinthefieldofopticalengineering.The
GWO resultsoftheclassicalengineeringdesignproblemsandrealapplicationprovethattheproposedalgo-
rithmisapplicabletochallengingproblemswithunknownsearchspaces.
(cid:2)2013ElsevierLtd.Allrightsreserved.
1.Introduction problems since they mostly assume problems as black boxes. In
otherwords,onlytheinput(s)andoutput(s)ofasystemareimpor-
Meta-heuristicoptimizationtechniqueshavebecomeverypop- tantforameta-heuristic.So,alladesignerneedsistoknowhowto
ularoverthelasttwodecades.Surprisingly,someofthemsuchas representhis/herproblemformeta-heuristics.
Genetic Algorithm (GA) [1], Ant Colony Optimization (ACO) [2], Third, the majority of meta-heuristics have derivation-free
and ParticleSwarmOptimization (PSO)[3]are fairly well-known mechanisms. In contrast to gradient-based optimization ap-
amongnotonlycomputerscientistsbutalsoscientistsfromdiffer- proaches, meta-heuristics optimize problems stochastically. The
ent fields. In addition to the huge number of theoretical works, optimization processstarts withrandomsolution(s),and thereis
such optimizationtechniques have been applied in various fields noneedtocalculatethederivativeofsearchspacestofindtheopti-
ofstudy.Thereisaquestionhereastowhymeta-heuristicshave mum.Thismakesmeta-heuristicshighlysuitableforrealproblems
becomeremarkablycommon.Theanswertothisquestioncanbe withexpensiveorunknownderivativeinformation.
summarizedintofourmainreasons:simplicity,flexibility,deriva- Finally,meta-heuristicshavesuperiorabilitiestoavoidlocalop-
tion-freemechanism,andlocaloptimaavoidance. tima compared to conventional optimization techniques. This is
First,meta-heuristicsarefairlysimple.Theyhavebeenmostly duetothestochasticnatureofmeta-heuristicswhichallowthem
inspiredbyverysimpleconcepts.Theinspirationsaretypicallyre- toavoidstagnationinlocalsolutionsandsearchtheentiresearch
lated tophysical phenomena, animals’ behaviors, or evolutionary spaceextensively.Thesearchspaceofrealproblemsisusuallyun-
concepts.Thesimplicityallowscomputerscientiststosimulatedif- knownandverycomplexwithamassivenumberoflocaloptima,
ferent natural concepts, propose new meta-heuristics, hybridize someta-heuristicsaregoodoptionsforoptimizingthesechalleng-
twoormoremeta-heuristics,orimprovethecurrentmeta-heuris- ingrealproblems.
tics.Moreover,thesimplicityassistsotherscientiststolearnmeta- TheNoFreeLunch(NFL)theorem[4]isworthmentioninghere.
heuristicsquicklyandapplythemtotheirproblems. Thistheoremhaslogicallyprovedthatthereisnometa-heuristic
Second,flexibilityreferstotheapplicabilityofmeta-heuristics bestsuitedforsolvingalloptimizationproblems.Inotherwords,
todifferentproblemswithoutanyspecialchangesinthestructure aparticularmeta-heuristicmayshowverypromisingresultsona
ofthealgorithm.Meta-heuristicsarereadilyapplicabletodifferent set of problems, but the same algorithm may show poor perfor-
mance on a different set of problems. Obviously, NFL makes this
⇑ fieldofstudyhighlyactivewhichresultsinenhancingcurrentap-
Correspondingauthor.Tel.:+61434555738.
proachesandproposingnewmeta-heuristicseveryyear.Thisalso
E-mail addresses: seyedali.mirjalili@griffithuni.edu.au (S. Mirjalili),
mohammad.smm@gmail.com(S.M.Mirjalili),a.lewis@griffith.edu.au(A.Lewis).
0965-9978/$-seefrontmatter(cid:2)2013ElsevierLtd.Allrightsreserved.
http://dx.doi.org/10.1016/j.advengsoft.2013.12.007

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 47
motivates our attempts to develop a new meta-heuristic with inspiredbytheconceptsofevolutioninnature.Themostpopular
inspirationfromgreywolves. algorithm in this branch is GA. This algorithm was proposed by
Generally speaking, meta-heuristics can be divided into two Hollandin1992[13]andsimulatesDarwnianevolutionconcepts.
main classes: single-solution-based and population-based. In the TheengineeringapplicationsofGAwereextensivelyinvestigated
formerclass(SimulatedAnnealing[5]forinstance)thesearchpro- by Goldberg [14]. Generally speaking, the optimization is done
cessstartswithonecandidatesolution.Thissinglecandidatesolu- byevolvinganinitialrandomsolutioninEAs.Eachnewpopulation
tion is then improved over the course of iterations. Population- iscreated by thecombinationand mutationof theindividualsin
based meta-heuristics, however, perform the optimization using the previous generation. Since the best individuals have higher
asetofsolutions(population).Inthiscasethesearchprocessstarts probabilityofparticipatingingeneratingthenewpopulation,the
with a random initial population (multiple solutions), and this new population is likely to be better than the previous genera-
population is enhanced over the course of iterations. Population- tion(s). This can guarantee that the initial random population is
based meta-heuristics have some advantages compared to single optimizedoverthecourseofgenerations.SomeoftheEAsareDif-
solution-basedalgorithms: ferentialEvolution(DE)[15],EvolutionaryPrograming(EP)[16,17],
and Evolution Strategy (ES) [18,19], Genetic Programming (GP)
(cid:2) Multiple candidate solutions share information about the [20],andBiogeography-BasedOptimizer(BBO)[21].
searchspacewhichresultsinsuddenjumpstowardtheprom- Asanexample,theBBOalgorithmwasfirstproposedbySimon
isingpartofsearchspace. in2008[21].Thebasicideaofthisalgorithmhasbeeninspiredby
(cid:2) Multiple candidate solutions assist each other to avoid locally biogeographywhichreferstothestudyofbiologicalorganismsin
optimalsolutions. termsofgeographicaldistribution(overtimeandspace).Thecase
(cid:2) Population-basedmeta-heuristicsgenerallyhavegreaterexplo- studies might include different islands, lands, or even continents
rationcomparedtosinglesolution-basedalgorithms. overdecades,centuries,ormillennia.Inthisfieldofstudydifferent
ecosystems(habitatsorterritories)areinvestigatedforfindingthe
Oneoftheinterestingbranchesofthepopulation-basedmeta- relations betweendifferent species (habitants) in termsof immi-
heuristics is Swarm Intelligence (SI). The concepts of SI was first gration, emigration, and mutation. The evolution of ecosystems
proposedin 1993 [6]. AccordingtoBonabeauet al.[1], SI is‘‘The (consideringdifferentkindsofspeciessuchaspredatorandprey)
emergentcollectiveintelligenceofgroupsofsimpleagents’’.Theinspi- over migration and mutation to reach a stable situation was the
rations of SI techniques originate mostly from natural colonies, maininspirationoftheBBOalgorithm.
flock,herds,andschools.SomeofthemostpopularSItechniques The second main branch of meta-heuristics is physics-based
areACO[2],PSO[3],andArtificialBeeColony(ABC)[7].Acompre- techniques.Suchoptimizationalgorithmstypicallymimicphysical
hensive literature review of the SI algorithms is provided in the rules.SomeofthemostpopularalgorithmsareGravitationalLocal
nextsection.SomeoftheadvantagesofSIalgorithmsare: Search(GLSA)[22],Big-BangBig-Crunch(BBBC)[23],Gravitational
Search Algorithm (GSA) [24], Charged System Search (CSS) [25],
(cid:2) SIalgorithmspreserveinformationaboutthesearchspaceover CentralForceOptimization(CFO)[26],ArtificialChemicalReaction
the course of iteration, whereas Evolutionary Algorithms (EA) OptimizationAlgorithm(ACROA)[27], BlackHole(BH)[28]algo-
discardtheinformationofthepreviousgenerations. rithm,RayOptimization(RO)[29]algorithm,Small-WorldOptimi-
(cid:2) SI algorithms often utilize memory to save the best solution zation Algorithm (SWOA) [30], Galaxy-based Search Algorithm
obtainedsofar. (GbSA)[31],andCurvedSpaceOptimization(CSO)[32].Themech-
(cid:2) SIalgorithmsusuallyhavefewerparameterstoadjust. anismofthesealgorithmsisdifferentfromEAs,inthatarandom
(cid:2) SI algorithms have less operators compared to evolutionary set of search agents communicate and move throughout search
approaches(crossover,mutation,elitism,andsoon). spaceaccordingtophysicalrules.Thismovementisimplemented,
(cid:2) SIalgorithmsareeasytoimplement. forexample,usinggravitationalforce,raycasting,electromagnetic
force,inertiaforce,weights,andsoon.
Regardless of the differences between the meta-heuristics, a Forexample,theBBBCalgorithmwasinspiredbythebigbang
common feature is the division of the search process into two and big crunch theories. The search agents of BBBC are scattered
phases:explorationandexploitation[8–12].Theexplorationphase fromapointinrandomdirectionsinasearchspaceaccordingto
referstotheprocessofinvestigatingthepromisingarea(s)ofthe the principles of the big bang theory. They search randomly and
searchspaceasbroadlyaspossible.Analgorithmneedstohavesto- thengatherinafinalpoint(thebestpointobtainedsofar)accord-
chasticoperatorstorandomlyandgloballysearchthesearchspace ingtotheprinciplesofthebigcrunchtheory.GSAisanotherphys-
inordertosupportthisphase.However,exploitationreferstothelo- ics-basedalgorithm.ThebasicphysicaltheoryfromwhichGSAis
calsearchcapabilityaroundthepromisingregionsobtainedinthe inspired is Newton’s law of universal gravitation. The GSA algo-
exploration phase. Finding a proper balance between these two rithm performs search by employing a collection of agents that
phasesisconsideredachallengingtaskduetothestochasticnature havemassesproportionaltothevalueofafitnessfunction.During
of meta-heuristics. This work proposes a new SI technique with iteration, the masses are attracted to each other by the gravita-
inspirationfromthesocialhierarchyandhuntingbehaviorofgrey tionalforcesbetweenthem.Theheavierthemass,thebiggerthe
wolfpacks.Therestofthepaperisorganizedasfollows: attractive force. Therefore, the heaviest mass, which is possibly
Section2presentsaliteraturereviewofSItechniques.Section3 closetotheglobaloptimum,attractstheothermassesinpropor-
outlinestheproposedGWOalgorithm.Theresultsanddiscussion tiontotheirdistances.
ofbenchmarkfunctions,semi-realproblems,andarealapplication The thirdsubclass of meta-heuristicsis theSI methods.These
arepresentedinSections4-6,respectively.Finally,Section7con- algorithms mostly mimic the social behavior of swarms, herds,
cludestheworkandsuggestssomedirectionsforfuturestudies. flocks,orschoolsofcreaturesinnature.Themechanismisalmost
similartophysics-basedalgorithm,butthesearchagentsnavigate
usingthesimulatedcollectiveandsocialintelligenceofcreatures.
2.Literaturereview ThemostpopularSItechniqueisPSO.ThePSOalgorithmwaspro-
posed by Kennedy and Eberhart [3] and inspired from the social
Meta-heuristics may be classified into three main classes: behavior of birds flocking. The PSO algorithm employs multiple
evolutionary, physics-based, and SI algorithms. EAs are usually particles that chase the position of the best particle and their

48 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
own best positions obtained so far. In other words, a particle is beenobserved,inwhichanalphafollowstheotherwolvesinthe
movedconsideringitsownbestsolutionaswellasthebestsolu- pack. In gatherings, the entire pack acknowledges the alpha by
tiontheswarmhasobtained. holdingtheirtailsdown.Thealphawolfisalsocalledthedominant
AnotherpopularSIalgorithmisACO,proposedbyDorigoetal. wolfsincehis/herordersshouldbefollowedbythepack[46].The
in2006[2].Thisalgorithmwasinspiredbythesocialbehaviorof alphawolvesareonly allowedtomateinthepack. Interestingly,
antsinanantcolony.Infact,thesocialintelligenceofantsinfind- the alpha is not necessarily the strongest member of the pack
ingtheshortestpathbetweenthenestandasourceoffoodisthe but the best in terms of managing the pack. This shows that the
maininspirationofACO.Apheromonematrixisevolvedoverthe organizationanddisciplineofapackismuchmoreimportantthan
courseofiterationbythecandidatesolutions.TheABCisanother itsstrength.
popular algorithm, mimicking the collective behavior of bees in Thesecondlevelinthehierarchyofgreywolvesisbeta.Thebe-
findingfoodsources.TherearethreetypesofbeesinABS:scout, tasaresubordinatewolvesthathelpthealphaindecision-making
onlooker, and employed bees. The scout bees are responsible for orotherpackactivities.Thebetawolfcanbeeithermaleorfemale,
exploringthesearchspace,whereasonlookerandemployedbees andhe/sheisprobablythebestcandidatetobethealphaincase
exploit the promising solutions found by scout bees. Finally, the oneofthealphawolvespassesawayorbecomesveryold.Thebeta
Bat-inspiredAlgorithm(BA),inspiredbytheecholocationbehavior wolfshouldrespectthealpha,butcommandstheotherlower-level
ofbats,hasbeenproposedrecently[33].Therearemanytypesof wolvesaswell.Itplaystheroleofanadvisortothealphaanddis-
batsinthenature.Theyaredifferentintermsofsizeandweight, cipliner for the pack. The beta reinforces the alpha’s commands
but they all have quite similar behaviors when navigating and throughoutthepackandgivesfeedbacktothealpha.
hunting.Batsutilizenaturalsonarinordertodothis.Thetwomain The lowest ranking grey wolf is omega. The omega plays the
characteristics of bats when finding prey have been adopted in roleofscapegoat.Omegawolvesalwayshavetosubmittoallthe
designing the BA algorithm. Bats tend to decrease the loudness otherdominantwolves.Theyarethelastwolvesthatareallowed
andincreasetherateofemittedultrasonicsoundwhentheychase to eat. It may seem the omega is not an important individual in
prey. Thisbehavior has beenmathematically modeledfor theBA thepack,butithasbeenobservedthatthewholepackfaceinternal
algorithm. The rest of the SI techniques proposed so far are as fightingand problemsincase oflosingtheomega.Thisisdue to
follows: theventingofviolenceand frustrationofallwolves bythe ome-
ga(s). This assists satisfying the entire pack and maintaining the
(cid:2) MarriageinHoneyBeesOptimizationAlgorithm(MBO)in2001 dominancestructure.Insomecasestheomegaisalsothebabysit-
[34]. tersinthepack.
(cid:2) ArtificialFish-SwarmAlgorithm(AFSA)in2003[35]. Ifawolfisnotanalpha,beta,oromega,he/sheiscalledsubor-
(cid:2) TermiteAlgorithmin2005[36]. dinate(ordeltainsomereferences).Deltawolveshavetosubmit
(cid:2) WaspSwarmAlgorithmin2007[37]. toalphasand betas,but theydominatetheomega. Scouts,senti-
(cid:2) MonkeySearchin2007[38]. nels,elders,hunters,andcaretakersbelongtothiscategory.Scouts
(cid:2) BeeCollectingPollenAlgorithm(BCPA)in2008[39]. are responsible for watching the boundaries of the territory and
(cid:2) CuckooSearch(CS)in2009[40]. warningthepackincaseofanydanger.Sentinelsprotectandguar-
(cid:2) DolphinPartnerOptimization(DPO)in2009[41]. anteethesafetyofthepack.Eldersaretheexperiencedwolveswho
(cid:2) FireflyAlgorithm(FA)in2010[42]. usedtobealphaorbeta.Huntershelpthealphasandbetaswhen
(cid:2) BirdMatingOptimizer(BMO)in2012[43]. huntingpreyandprovidingfoodforthepack.Finally,thecaretak-
(cid:2) KrillHerd(KH)in2012[44]. ersareresponsibleforcaringfortheweak,ill,andwoundedwolves
(cid:2) FruitflyOptimizationAlgorithm(FOA)in2012[45]. inthepack.
Inadditiontothesocialhierarchyofwolves,grouphuntingis
ThislistshowsthattherearemanySItechniquesproposedso another interesting social behavior of grey wolves. According to
far, many of them inspired by hunting and search behaviors. To Muro et al. [47] the main phases of grey wolf hunting are as
the best of our knowledge, however, there is no SI technique in follows:
theliteraturemimickingtheleadershiphierarchyofgreywolves,
well known for their pack hunting. This motivated our attempt (cid:2) Tracking,chasing,andapproachingtheprey.
tomathematicallymodelthesocialbehaviorofgreywolves,pro- (cid:2) Pursuing, encircling, and harassing the prey until it stops
poseanewSIalgorithminspiredbygreywolves,andinvestigate moving.
itsabilitiesinsolvingbenchmarkandrealproblems. (cid:2) Attacktowardstheprey.
ThesestepsareshowninFig.2.
3.GreyWolfOptimizer(GWO)
Inthisworkthishuntingtechniqueandthesocialhierarchyof
greywolvesaremathematicallymodeledinordertodesignGWO
In this section the inspiration of the proposed method is first
andperformoptimization.
discussed.Then,themathematicalmodelisprovided.
3.1.Inspiration
Greywolf(Canislupus)belongstoCanidaefamily.Greywolves
areconsideredasapexpredators,meaningthattheyareatthetop
ofthefoodchain.Greywolvesmostlyprefertoliveinapack.The
group size is 5–12 on average. Of particular interest is that they
haveaverystrictsocialdominanthierarchyasshowninFig.1.
Theleadersareamaleandafemale,calledalphas.Thealphais
mostly responsible for making decisions about hunting, sleeping
place,timetowake,andsoon.Thealpha’sdecisionsaredictated
tothepack.However,somekindofdemocraticbehaviorhasalso Fig.1. Hierarchyofgreywolf(dominancedecreasesfromtopdown).

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 49
3.2.Mathematicalmodelandalgorithm pointsillustratedinFig.3.Soagreywolfcanupdateitspositionin-
|     |     |     |     |     |     | side | the space | around | the | prey in | any random | location | by using |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ------ | --- | ------- | ---------- | -------- | -------- |
Inthissubsectionthemathematicalmodelsofthesocialhierar- Eqs.(3.1)and(3.2).
chy,tracking,encircling,andattackingpreyareprovided.Thenthe The same concept can be extended to a search space with n
GWOalgorithmisoutlined. dimensions,andthegreywolveswillmoveinhyper-cubes(orhy-
per-spheres)aroundthebestsolutionobtainedsofar.
3.2.1.Socialhierarchy
Inordertomathematicallymodelthesocialhierarchyofwolves
3.2.3.Hunting
whendesigningGWO,weconsiderthefittestsolutionasthealpha
|     |     |     |     |     |     |     | Grey wolveshave |     | the abilityto |     | recognizethelocationofprey |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | -------------------------- | --- | --- |
(a).Consequently,thesecondandthirdbestsolutionsarenamed
|     |     |     |     |     |     | and | encircle | them. The | hunt | is usually | guided | by  | the alpha. The |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ---------- | ------ | --- | -------------- |
beta(b)anddelta(d)respectively.Therestofthecandidatesolu- betaanddeltamightalsoparticipateinhuntingoccasionally.How-
(x).
tions are assumed to be omega In the GWO algorithm the ever,inanabstractsearchspacewehavenoideaabouttheloca-
hunting(optimization)isguidedbya,b,andd.Thexwolvesfol- tion of the optimum (prey). In order to mathematically simulate
lowthesethreewolves. the hunting behavior of grey wolves, we suppose that the alpha
|     |     |     |     |     |     | (best | candidate | solution) | beta, | and | delta | have better | knowledge |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | ----- | --- | ----- | ----------- | --------- |
3.2.2.Encirclingprey about the potential location of prey. Therefore, we save the first
Asmentionedabove,greywolvesencirclepreyduringthehunt. three best solutions obtained so far and oblige the other search
Inordertomathematicallymodelencirclingbehaviorthefollow- agents(includingtheomegas)toupdatetheirpositionsaccording
ingequationsareproposed: to the position of the best search agents. The following formulas
| ~D¼j~C(cid:3)~X |                  |     |     |     |       | areproposedinthisregard. |     |     |     |     |     |     |     |
| --------------- | ---------------- | --- | --- | --- | ----- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                 | ðtÞ(cid:4)~XðtÞj |     |     |     | ð3:1Þ |                          |     |     |     |     |     |     |     |
p
|            |              |     |     |     |       | ~Da¼j~C | (cid:3)~Xa(cid:4)~Xj;~D |                    | ¼j~C (cid:3)~X | (cid:4)~Xj;~D         | ¼j~C     | (cid:3)~X (cid:4)~Xj | ð3:5Þ              |
| ---------- | ------------ | --- | --- | --- | ----- | ------- | ----------------------- | ------------------ | -------------- | --------------------- | -------- | -------------------- | ------------------ |
|            |              |     |     |     |       |         | 1                       | b                  | 2              | b                     | d        | 3 d                  |                    |
| ~Xðtþ1Þ¼~X | ~A(cid:3)~D  |     |     |     |       |         |                         |                    |                |                       |          |                      |                    |
|            | p ðtÞ(cid:4) |     |     |     | ð3:2Þ |         |                         |                    |                |                       |          |                      |                    |
|            |              |     |     |     |       | ~X      | ¼~Xa(cid:4)             | ~A (cid:3)ð~DaÞ;~X | ¼~X            | (cid:4) ~A (cid:3)ð~D | Þ;~X ¼~X | (cid:4) ~A           | (cid:3)ð~D Þ ð3:6Þ |
wheretindicatesthecurrentiteration,~Aand~Carecoefficientvec- 1 1 2 b 2 b 3 d 3 d
tors,~X isthepositionvectoroftheprey,and~Xindicatestheposi-
| p                       |     |                         |     |     |     |          |     | ~X þ~X þ~X |     |     |     |     |       |
| ----------------------- | --- | ----------------------- | --- | --- | --- | -------- | --- | ---------- | --- | --- | --- | --- | ----- |
| tionve ctorofagreywolf. |     |                         |     |     |     | ~Xðtþ1Þ¼ |     |            |     |     |     |     |       |
|                         |     |                         |     |     |     |          |     | 1 2        | 3   |     |     |     | ð3:7Þ |
| Thevectors~Aand~C       |     | arecalculatedasfollows: |     |     |     |          |     | 3          |     |     |     |     |       |
~A¼2~a(cid:3)~r Fig.4showshowasearchagentupdatesitspositionaccordingto
|     | (cid:4)~a |     |     |     | ð3:3Þ |                                                         |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ----- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 1         |     |     |     |       | alpha,beta,anddeltaina2Dsearchspace.Itcanbeobservedthat |     |     |     |     |     |     |     |
thefinalpositionwouldbeinarandomplacewithinacirclewhich
~C¼2(cid:3)~r
| 2   |     |     |     |     | ð3:4Þ |     |         |                  |     |           |       |           |               |
| --- | --- | --- | --- | --- | ----- | --- | ------- | ---------------- | --- | --------- | ----- | --------- | ------------- |
|     |     |     |     |     |       | is  | defined | by the positions |     | of alpha, | beta, | and delta | in the search |
wherecomponentsof~aarelinearlydecreasedfrom2to0overthe space. In other words alpha, beta, and delta estimate the position
courseofiterationsandr ,r arerandomvectorsin[0,1]. of the prey, and other wolves updates their positions randomly
1 2
| ToseetheeffectsofEqs.(3.1)and(3.2),atwo-dimensionalpo- |     |     |     |     |     | aroundtheprey. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
sitionvectorandsomeofthepossibleneighborsareillustratedin
Fig.3(a).Ascanbeseeninthisfigure,agreywolfinthepositionof 3.2.4.Attackingprey(exploitation)
(X,Y)canupdateitspositionaccordingtothepositionoftheprey Asmentionedabovethegreywolvesfinishthehuntbyattack-
(X(cid:5),Y(cid:5)).Differentplacesaroundthebestagentcanbereachedwith
|            |             |          |              |           |            | ing                                                    | the prey | when | it stops | moving. | In order | to mathematically |     |
| ---------- | ----------- | -------- | ------------ | --------- | ---------- | ------------------------------------------------------ | -------- | ---- | -------- | ------- | -------- | ----------------- | --- |
|            |             |          |              |           | of~A and~C | modelapproachingthepreywedecreasethevalueof~a.Notethat |          |      |          |         |          |                   |     |
| respect to | the current | position | by adjusting | the value |            |                                                        |          |      |          |         |          |                   |     |
(X(cid:5)–X, Y(cid:5)) thefluctuationrangeof~Aisalsodecreasedby~a.Inotherwords~Ais
| vectors. | For instance, |     | can | be reached | by setting |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
~A¼ð1;0Þand~C¼ð1;1Þ.Thepossibleupdatedpositionsofagrey
arandomvalueintheinterval[(cid:4)2a,2a]whereaisdecreasedfrom
2to0overthecourseofiterations.Whenrandomvaluesof~Aarein
| wolf in 3D | space are | depicted | in Fig. 3(b). | Note that | the random |     |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | ------------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
vectorsr andr allowwolvestoreachanypositionbetweenthe [(cid:4)1,1],thenextpositionofasearchagentcanbeinanyposition
| 1   | 2   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.2. Huntingbehaviorofgreywolves:(A)chasing,approaching,andtrackingprey(B–D)pursuiting,harassing,andencircling(E)stationarysituationandattack[47].

50 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
(X,Y,Z)
|     |          | X*-X   |       |               | (X*-X,Y,Z)  | (X*,Y,Z)   |          |     |
| --- | -------- | ------ | ----- | ------------- | ----------- | ---------- | -------- | --- |
|     | (X*-X,Y) | (X*,Y) | (X,Y) |               | (X*-X,Y,Z*) | (X*,Y,Z*)  | (X,Y,Z*) |     |
|     |          |        |       | (X*-X,Y,Z*-Z) | (X*,Y,Z*-Z) | (X,Y,Z*-Z) |          |     |
(X,Y*,Z)
Y*-Y
(X*,Y*,Z*)
|     | (X*,Y*) |     |     |     |     |     | (X,Y*,Z*) |     |
| --- | ------- | --- | --- | --- | --- | --- | --------- | --- |
(X*-X,Y*)
|     |     |     |     | (X*-X,Y*,Z*-Z) | (X*,Y*,Z*-Z) | (X,Y*,Z*-Z) |     | (X,Y*-Y,Z) |
| --- | --- | --- | --- | -------------- | ------------ | ----------- | --- | ---------- |
(X,Y*)
(X,Y,Z*)
|     |             | (X*,Y*-Y) |          | (X*-X,Y*-Y,Z-Z*) | (X*,Y*-Y,Z*-Z) | (X,Y*-Y,Z*-Z) |     |     |
| --- | ----------- | --------- | -------- | ---------------- | -------------- | ------------- | --- | --- |
|     | (X*-X,Y*-Y) |           | (X,Y*-Y) |                  |                |               |     |     |
|     |             | (a)       |          |                  |                |  (b)          |     |     |
Fig.3. 2Dand3Dpositionvectorsandtheirpossiblenextlocations.
a1
C1
a2
C2
R
Dalpha
Dbeta
Move
Ddelta
a3
|     |     | C3  |     |     |     | or any other hunters |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
Estimated position of the
prey
|     |     |     | Fig.4. PositionupdadinginGWO. |     |     |     |     |     |
| --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
betweenitscurrentpositionandthepositionoftheprey.Fig.5(a)
showsthat|A|<1forcesthewolvestoattacktowardstheprey. If |A|>1
Withtheoperatorsproposedsofar,theGWOalgorithmallows
If |A|<1
itssearchagentstoupdatetheirpositionbasedonthelocationof
thealpha,beta,anddelta;andattacktowardstheprey.However,
theGWOalgorithmispronetostagnationinlocalsolutionswith
theseoperators.Itistruethattheencirclingmechanismproposed
showsexplorationtosomeextent,butGWOneedsmoreoperators
toemphasizeexploration.
|     |     |     |     |     | (a) |     | (b)  |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- |
3.2.5.Searchforprey(exploration)
Greywolvesmostlysearchaccordingtothepositionoftheal-
Fig.5. Attackingpreyversussearchingforprey.
| pha, beta, | and delta. They | diverge from each | other to search for |     |     |     |     |     |
| ---------- | --------------- | ----------------- | ------------------- | --- | --- | --- | --- | --- |
preyandconvergetoattackprey.Inordertomathematicallymod-
el divergence, we utilize~A with randomvalues greater than 1 or AnothercomponentofGWO thatfavors exploration is~C. As may
less than -1 to oblige the search agent to diverge from the prey. beseeninEq.(3.4),the~C vectorcontainsrandomvaluesin[0,2].
This emphasizes exploration and allows the GWO algorithm to Thiscomponentprovidesrandomweightsforpreyinordertosto-
search globally. Fig. 5(b) also shows that |A|>1 forces the grey chastically emphasize (C>1) or deemphasize (C<1) the effect of
wolves to diverge from the prey to hopefully find a fitter prey. preyindefiningthedistanceinEq.(3.1).ThisassistsGWOtoshow

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 51
amorerandombehaviorthroughoutoptimization,favoringexplo- However,wehavekepttheGWOalgorithmassimpleaspossible
rationandlocaloptimaavoidance.Itisworthmentioningherethat with the fewest operators to be adjusted. Such mechanisms are
CisnotlinearlydecreasedincontrasttoA.Wedeliberatelyrequire recommendedforfuturework.Thesourcecodesofthisalgorithm
C to provide random values at all times in order to emphasize canbefoundinhttp://www.alimirjalili.com/GWO.htmlandhttp://
exploration not only during initial iterations but also final itera- www.mathworks.com.au/matlabcentral/fileexchange/44974.
tions.Thiscomponentisveryhelpfulincaseoflocaloptimastag-
nation,especiallyinthefinaliterations. 4.Resultsanddiscussion
TheCvectorcanbealsoconsideredastheeffectofobstaclesto
| approaching | prey in | nature. | Generally | speaking, | the | obstacles | in  |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | --------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
InthissectiontheGWOalgorithmisbenchmarkedon29bench-
natureappearinthehuntingpathsofwolvesandinfactprevent
markfunctions.Thefirst23benchmarkfunctionsaretheclassical
themfromquicklyandconvenientlyapproachingprey.Thisisex-
functionsutilizedbymanyresearchers[16,48–51,82].Despitethe
actlywhatthevectorCdoes.Dependingonthepositionofawolf,it simplicity,wehavechosenthesetestfunctionstobeabletocompare
canrandomlygivethepreyaweightandmakeitharderandfar- ourresultstothoseofthecurrentmeta-heuristics.Thesebenchmark
thertoreachforwolves,orviceversa. functionsarelistedinTables1–3whereDimindicatesdimensionof
To sum up, the search process starts with creating a random thefunction,Rangeistheboundaryofthefunction’ssearchspace,
populationofgreywolves(candidatesolutions)intheGWOalgo- andf istheoptimum.Theothertestbedsthatwehavechosen
min
rithm.Overthecourseofiterations,alpha,beta,anddeltawolves aresixcompositebenchmarkfunctionsfromaCEC2005specialses-
estimatetheprobablepositionoftheprey.Eachcandidatesolution sion[52].Thesebenchmarkfunctionsaretheshifted,rotated,ex-
| updatesits | distancefromthe |              | prey.The | parameter   | ais | decreased     |     |         |     |                   |     |                  |           |       |
| ---------- | --------------- | ------------ | -------- | ----------- | --- | ------------- | --- | ------- | --- | ----------------- | --- | ---------------- | --------- | ----- |
|            |                 |              |          |             |     |               |     | panded, | and | combined variants |     | of the classical | functions | which |
| from 2 to  | 0 in order      | to emphasize |          | exploration | and | exploitation, |     |         |     |                   |     |                  |           |       |
offerthegreatestcomplexityamongthecurrentbenchmarkfunc-
| respectively. | Candidate | solutions | tend | to diverge | from | the | prey |     |     |     |     |     |     |     |
| ------------- | --------- | --------- | ---- | ---------- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
tions[53].Tables4liststheCEC2005testfunctions,whereDimindi-
whenj~Aj>1andconvergetowardsthepreywhenj~Aj<1.Finally,
|     |     |     |     |     |     |     |     | cates | dimension | of the | function, | Range is | the boundary | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------ | --------- | -------- | ------------ | ------ |
the GWO algorithm is terminated by the satisfaction of an end function’ssearchspace,andf istheoptimum.Figs.7–10illustrate
min
| criterion. |     |     |     |     |     |     |     | the2Dversionsofthebenchmarkfunctionsused. |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
ThepseudocodeoftheGWOalgorithmispresentedinFig.6. Generallyspeaking,thebenchmarkfunctionsusedareminimi-
To see how GWO is theoretically able to solve optimization zation functions and can be divided into four groups: unimodal,
problems,somepointsmaybenoted: multimodal, fixed-dimension multimodal, and composite func-
|     |     |     |     |     |     |     |     | tions. | Note | that a detailed | descriptions | of  | the composite | bench- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --------------- | ------------ | --- | ------------- | ------ |
(cid:2) The proposed social hierarchy assists GWO to save the best markfunctionsareavailableintheCEC2005technicalreport[52].
solutionsobtainedsofaroverthecourseofiteration.
TheGWOalgorithmwasrun30timesoneachbenchmarkfunc-
| (cid:2) The proposed | encircling |     | mechanism | defines | a   | circle-shaped |     |     |     |     |     |     |     |     |
| -------------------- | ---------- | --- | --------- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tion.Thestatisticalresults(averageandstandarddeviation)arere-
| neighborhood | around | the | solutions | which | can be | extended | to  |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --------- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
portedinTables5–8.Forverifyingtheresults,theGWOalgorithm
higherdimensionsasahyper-sphere.
iscomparedtoPSO[3]asanSI-basedtechniqueandGSA[24]asa
(cid:2) The random parameters A and C assist candidate solutions to physics-basedalgorithm.Inaddition,theGWOalgorithmiscom-
havehyper-sphereswithdifferentrandomradii. pared with three EAs: DE [15], Fast Evolutionary Programing
(cid:2) The proposed hunting method allows candidate solutions to (FEP)[16],andEvolutionStrategywithCovarianceMatrixAdapta-
| locatetheprobablepositionoftheprey. |                  |     |            |            |         |              |     | tion(CMA-ES)[18].        |     |     |     |     |     |     |
| ----------------------------------- | ---------------- | --- | ---------- | ---------- | ------- | ------------ | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| (cid:2) Exploration                 | and exploitation |     | are        | guaranteed | by      | the adaptive |     |                          |     |     |     |     |     |     |
| valuesofaandA.                      |                  |     |            |            |         |              |     | 4.1.Exploitationanalysis |     |     |     |     |     |     |
| (cid:2) The adaptive                | values           | of  | parameters | a and      | A allow | GWO          | to  |                          |     |     |     |     |     |     |
smoothlytransitionbetweenexplorationandexploitation.
AccordingtotheresultsofTable5,GWOisabletoprovidevery
(cid:2) WithdecreasingA,halfoftheiterationsaredevotedtoexplora-
competitiveresults.ThisalgorithmoutperformsallothersinF1,F2,
| tion (|A|P1) | and | the other | half | are dedicated | to  | exploitation |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
andF7.Itmaybenotedthattheunimodalfunctionsaresuitablefor
(|A|<1).
|     |     |     |     |     |     |     |     | benchmarking |     | exploitation. | Therefore, | these | results | show the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | ---------- | ----- | ------- | -------- |
(cid:2) TheGWOhasonlytwomainparameterstobeadjusted(aand superiorperformanceofGWOintermsofexploitingtheoptimum.
C). This is due to the proposed exploitation operators previously
discussed.
| There | are possibilities | to  | integrate | mutation | and | other | evolu- |     |     |     |     |     |     |     |
| ----- | ----------------- | --- | --------- | -------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
tionary operators to mimic the whole life cycle of grey wolves. 4.2.Explorationanalysis
|     |     |     |     |     |     |     |     | In  | contrast | to the unimodal |     | functions, | multimodal | functions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ---------- | ---------- | --------- |
havemanylocaloptimawiththenumberincreasingexponentially
|     |     |     |     |     |     |     |     | with | dimension. | This makes | them | suitable | for benchmarking | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ---------- | ---- | -------- | ---------------- | --- |
Table1
Unimodalbenchmarkfunctions.
|     |     |     |     |     |     |     |     | Function |     |     |     | Dim | Range | fmin |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ----- | ---- |
f1ðxÞ¼Pn
|     |     |     |     |     |     |     |     |                        | i¼1                         | x2 i                    |     | 30  | [(cid:4)100,100] | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --------------------------- | ----------------------- | --- | --- | ---------------- | --- |
|     |     |     |     |     |     |     |     | f2ðxÞ¼Pn               |                             | jxijþQn                 |     |     |                  |     |
|     |     |     |     |     |     |     |     |                        | i¼1                         | i¼1 jxij                |     | 30  | [(cid:4)10,10]   | 0   |
|     |     |     |     |     |     |     |     |                        |                             | 2                       |     | 30  | [(cid:4)100,100] | 0   |
|     |     |     |     |     |     |     |     | f3ðxÞ¼Pn               |                             | ðPi xjÞ                 |     |     |                  |     |
|     |     |     |     |     |     |     |     |                        | i¼1                         | j(cid:4)1               |     |     |                  |     |
|     |     |     |     |     |     |     |     | f4ðxÞ¼maxifjxij;16i6ng |                             |                         |     | 30  | [(cid:4)100,100] | 0   |
|     |     |     |     |     |     |     |     | f5ðxÞ¼Pn               | (cid:4) 1½100ðxiþ1(cid:4)x2 | Þ2þðxi(cid:4)1Þ2(cid:6) |     | 30  | [(cid:4)30,30]   | 0   |
|     |     |     |     |     |     |     |     |                        | i¼ 1                        | i                       |     |     |                  |     |
|     |     |     |     |     |     |     |     | f6ðxÞ¼Pn               |                             | ð½xiþ0:5(cid:6)Þ2       |     | 30  | [(cid:4)100,100] | 0   |
i¼1
|     |     |     |     |     |     |     |     | f7ðxÞ¼Pn |     | ix4            |     | 30  | [(cid:4)1.28,1.28] | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | --- | ------------------ | --- |
|     |     |     |     |     |     |     |     |          | i¼1 | i þrandom½0;1Þ |     |     |                    |     |
Fig.6. PseudocodeoftheGWOalgorithm.

52 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
Table2
Multimodalbenchmarkfunctions.
| Function |     |     |                            |     |     |     |     |     |     | Dim | Range |     | fmin |     |
| -------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- |
| F8ðxÞ¼Pn |     |     | pffi ffixffiffi ffi ffiffi |     |     |     |     |     |     |     |       |     |      |     |
(cid:4)xisinð j i j Þ 30 [(cid:4)500,500] (cid:4)418.9829(cid:7)5
F9ðxÞ¼Pn i¼1
|     | i¼1 | ½x2 (cid:4)10cosð2pxiÞþ10(cid:6) |                                                   |                         |     |     |     |     |     | 30  | [(cid:4)5.12,5.12] |     | 0   |     |
| --- | --- | -------------------------------- | ------------------------------------------------- | ----------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
|     |     | i (cid:3)                        | q ffi ffiffiPffiffiffiffiffi ffi ffiffiffi ffiffi | ffiffiffi ffiffi(cid:4) |     |     |     |     |     |     |                    |     |     |     |
F10ðxÞ¼(cid:4)20exp (cid:4)0:2 1 n x 2 (cid:4)exp(cid:5)1 Pn cosð2pxiÞ(cid:6)þ20þe 30 [(cid:4)32,32] 0
|         |       |                 | n i ¼ 1 | i n i¼1    |     |     |     |     |     |     |                  |     |     |     |
| ------- | ----- | --------------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|         |       |                 | (cid:3) | (cid:4)    |     |     |     |     |     | 30  | [(cid:4)600,600] |     | 0   |     |
| F11ðxÞ¼ | 1     | Pn x2 (cid:4)Qn | cos     | pxiffii þ1 |     |     |     |     |     |     |                  |     |     |     |
|         | 40 00 | i¼1 i           | i¼1     |            |     |     |     |     |     |     |                  |     |     |     |
F12ðxÞ¼p f10sinðpy 1ÞþPn (cid:4) 1ðy i(cid:4)1Þ2½1þ10sin2ðpy n(cid:4)1Þ2gþPn 30 [(cid:4)50,50] 0
|     | n   |     | i¼ 1 |     | iþ1Þ(cid:6)þðy |     | i¼1 uðxi;10;100;4Þ |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | -------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
i¼1þxi þ1
y 4
8 <kðxi(cid:4)aÞm
xi>a
| uðxi;a;k;mÞ¼ |     | 0   | (cid:4)a<xi<a |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
:kð(cid:4)xi(cid:4)aÞm
xi<(cid:4)a
F13ðxÞ¼0:1fsin2ð3px1ÞþPn ðxi(cid:4)1Þ2½1þsin2ð3pxiþ1Þ(cid:6)þðxn(cid:4)1Þ2½1þsin2ð2pxnÞ(cid:6)gþPn 30 [(cid:4)50,50] 0
|     |     |     | i¼1 |     |     |     |     | i¼1 uðxi;5;100;4Þ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
[0,p]
F14ðxÞ¼(cid:4)Pn sinðxiÞ(cid:3) (cid:3) sin (cid:3)i: x2 (cid:4)(cid:4)2m ;m¼10 30 (cid:4)4.687
|     |     | i¼1 | p i |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | h   | Pn  | Pn  | i   |     |     |     |     |     |     |     |     |     |     |
F15ðxÞ¼ e(cid:4) ðxi=bÞ2m(cid:4)2e(cid:4) x2 (cid:3)Qn cos2xi;m¼5 30 [(cid:4)20,20] (cid:4)1
|     |     | i¼1 | i¼1 | i i¼1 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F16ðxÞ¼f½Pn sin2ðxiÞ(cid:6)(cid:4)expð(cid:4)Pn Þg(cid:3)exp½(cid:4)Pn sin2pffi ffixffiffi ffi ffiffi 30 [(cid:4)10,10] (cid:4)1
|     |     | i¼1 |     | i¼1 x2 | i¼1 | j i j (cid:6) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
i
Table3
Fixed-dimensionmultimodalbenchmarkfunctions.
| Function |         |           |                    |                 |     |     |     |     |     |     |     | Dim Range        | fmin |     |
| -------- | ------- | --------- | ------------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --- |
|          | (cid:7) |           |                    | (cid:8)(cid:4)1 |     |     |     |     |     |     |     | 2 [(cid:4)65,65] | 1    |     |
| F14ðxÞ¼  |         | 1 þP2 5   | 1                  |                 |     |     |     |     |     |     |     |                  |      |     |
|          | 5       | 00 j¼ 1jþ | P2 ðxi(cid:4)aijÞ6 |                 |     |     |     |     |     |     |     |                  |      |     |
i¼1
|           |     | (cid:9)        | 2 (cid:10)2      |     |     |     |     |     |     |     |     | 4 [(cid:4)5,5] | 0.00030 |     |
| --------- | --- | -------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --- |
| F15ðxÞ¼P1 |     | 1 ai(cid:4) x1 | ð b i þ b ix 2 Þ |     |     |     |     |     |     |     |     |                |         |     |
|           |     | i¼ 1 b 2 i     | þ b i x3 þ x 4   |     |     |     |     |     |     |     |     |                |         |     |
F16ðxÞ¼4x2 1 (cid:4)2:1x4 1 þ1 3 x6 1 þx1x2(cid:4)4x2 2 þ4x4 2 2 [(cid:4)5,5] (cid:4)1.0316
|     | (cid:3) |     | (cid:4)2 |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F17ðxÞ¼ x2(cid:4) 5 :1 x2 þp 5x1(cid:4)6 þ10(cid:5)1(cid:4) 1 (cid:6)cosx1þ10 2 [(cid:4)5,5] 0.398
|     |     | 4 p 2 1 |     | 8 p |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F18ðxÞ¼½1þðx1þx2þ1Þ2ð19(cid:4)14x1þ3x2 (cid:4)14x2þ6x1x2þ3x2 Þ(cid:6)(cid:7)½30þð2x1(cid:4)3x2Þ2(cid:7)ð18(cid:4)32x1þ12x2 þ48x2(cid:4)36x1x2þ27x2 Þ(cid:6) 2 [(cid:4)2,2] 3
|     |     |     |     | 1   |     | 2   |     |     | 1   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F19ðxÞ¼(cid:4)P4 ciexpð(cid:4)P3 aijðxj(cid:4)p ijÞ2Þ 3 [1,3] (cid:4)3.86
|     |     | i¼1 | j¼1 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F20ðxÞ¼(cid:4)P4 ciexpð(cid:4)P6 aijðxj(cid:4)p ijÞ2Þ 6 [0,1] (cid:4)3.32
|     |     | i¼1 | j¼1 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F21ðxÞ¼(cid:4)P5 ½ðX(cid:4)aiÞðX(cid:4)aiÞTþci(cid:6) (cid:4)1 4 [0,10] (cid:4)10.1532
i¼1
F22ðxÞ¼(cid:4)P7 ½ðX(cid:4)aiÞðX(cid:4)aiÞTþci(cid:6) (cid:4)1 4 [0,10] (cid:4)10.4028
i¼1
F23ðxÞ¼(cid:4)P1 0 ½ðX(cid:4)aiÞðX(cid:4)aiÞTþci(cid:6) (cid:4)1 4 [0,10] (cid:4)10.5363
i¼ 1
exploration ability of an algorithm. According to the results of 4.4.Convergencebehavioranalysis
| Tables | 6 and | 7, GWO | is able | to provide | very competitive |     | results |     |     |     |     |     |     |     |
| ------ | ----- | ------ | ------- | ---------- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
on the multimodal benchmark functions as well. This algorithm InthissubsectiontheconvergencebehaviorofGWOisinvesti-
outperformsPSOandGSAonthemajorityofthemultimodalfunc- gated.AccordingtoBergetal.[54],thereshouldbeabruptchanges
tions.Moreover,GWOshowsverycompetitiveresultscompareto inthemovementofsearchagentsovertheinitialstepsofoptimi-
DE and FEP; and outperforms them occasionally. These results zation. This assists a meta-heuristic to explore the search space
showthattheGWOalgorithmhasmeritintermsofexploration. extensively.Then,thesechangesshouldbereducedtoemphasize
exploitationattheendofoptimization.Inordertoobservethecon-
|     |     |     |     |     |     |     |     | vergence behavior |     | of the GWO | algorithm, | the | search history | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ---------- | --- | -------------- | --- |
4.3.Localminimaavoidance trajectoryofthefirstsearchagentinitsfirstdimensionareillus-
tratedinFig.11.Theanimatedversionsofthisfigurecanbefound
The fourth class of benchmark functions employed includes in Supplementary Materials. Note that the benchmark functions
composite functions, generally very challenging test beds for are shifted in this section, and we used six search agents to find
| meta-heuristic |     | algorithms. |     | So, exploration | and | exploitation | can | theoptima. |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | --------------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
be simultaneously benchmarked by the composite functions. ThesecondcolumnofFig.11depictsthesearchhistoryofthe
Moreover, the local optima avoidance of an algorithm can be searchagents.ItmaybeobservedthatthesearchagentsofGWO
examinedduetothemassivenumberoflocaloptimainsuchtest tendtoextensivelysearchpromisingregionsofthesearchspaces
functions. According to Table 8, GWO outperforms all others on andexploitthebestone.Inaddition,thefourthcolumnofFig.11
half of the composite benchmark functions. The GWO algorithm showsthetrajectoryofthefirstparticle,inwhichchangesofthe
alsoprovidesverycompetitiveresultsontheremainingcomposite firstsearchagentinitsfirstdimensioncanbeobserved.Itcanbe
benchmarkfunctions.ThisdemonstratesthatGWOshowsagood seenthatthereareabruptchangesintheinitialstepsofiterations
balancebetweenexplorationandexploitationthatresultsinhigh which are decreased gradually over the course of iterations.
localoptimaavoidance.Thissuperiorcapabilityisduetotheadap- According to Berg et al. [54], this behavior can guarantee that a
tivevalueofA.Asmentionedabove,halfoftheiterationsarede- SIalgorithmeventuallyconvergencestoapointinsearchspace.
voted to exploration (|A|P1) and the rest to exploitation Tosumup,theresultsverifytheperformanceoftheGWOalgo-
(|A|<1).ThismechanismassistsGWOtoprovideverygoodexplo- rithm in solving various benchmark functions compared to well-
ration,localminimaavoidance,andexploitationsimultaneously. knownmeta-heuristics.Tofurtherinvestigatetheperformanceof

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 53
Table4
Compositebenchmarkfunctions.
Function Dim Range fmin
F24(CF1):
f1,f2,f3,...,f10=SphereFunction 10 [(cid:4)5,5] 0
½, 1;, 2;, 3;...;, 10(cid:6)¼½1;1;1;...;1(cid:6)
[k1,k2,k3...,k10]=[5/100,5/100,5/100,...,5/100]
F25(CF2):
f1,f2,f3,...,f10=Griewank’sFunction 10 [(cid:4)5,5] 0
½, 1;, 2;, 3;...;, 10(cid:6)¼½1;1;1;...;1(cid:6)
[k1,k2,k3,...,k10]=[5/100,5/100,5/100,...,5/100]
F26(CF3):
f1,f2,f3,...,f10=Griewank’sFunction 10 [(cid:4)5,5] 0
½, 1;, 2;, 3;...;, 10(cid:6)¼½1;1;1;...;1(cid:6)
[k1,k2,k3,...,k10]=[1,1,1,...,1]
F27(CF4):
f1,f2=Ackley’sFunction 10 [(cid:4)5,5] 0
f3,f4=Rastrigin’sFunction
f5,f6=Weierstras’sFunction
f7,f8=Griewank’sFunction
f9,f10=SphereFunction
½, 1;, 2;, 3;...;, 10(cid:6)¼½1;1;1;...;1(cid:6)
[k1,k2,k3,...,k10]=[5/32,5/32,1,1,5/0.5,5/0.5,5/100,5/100,5/100,5/100]
F28(CF5):
f1,f2=Rastrigin’sFunction 10 [(cid:4)5,5] 0
f3,f4=Weierstras’sFunction
f5,f6=Griewank’sFunction
f7,f8=Ackley’sFunction
f9,f10=SphereFunction
½, 1;, 2;, 3;...;, 10(cid:6)¼½1;1;1;...;1(cid:6)
[k1,k2,k3,...,k10]=[1/5,1/5,5/0.5,5/0.5,5/100,5/100,5/32,5/32,5/100,5/100]
f29(CF6):
f1,f2=Rastrigin’sFunction 10 [(cid:4)5,5] 0
f3,f4=Weierstras’sFunction
f5,f6=Griewank’sFunction
f7,f8=Ackley’sFunction
f9,f10=SphereFunction
½, 1;, 2;, 3;...;, 10(cid:6)¼½0:1;0:2;0:3;0:4;0:5;0:6;0:7;0:8;0:9;1(cid:6)
[k1,k2,k3,...,k10]=[0.1(cid:5)1/5,0.2(cid:5)1/5,0.3(cid:5)5/0.5,0.4(cid:5)5/0.5,0.5(cid:5)5/100,0.6(cid:5)5/100,0.7(cid:5)5/32,0.8(cid:5)5/32,0.9(cid:5)5/100,1(cid:5)5/100]
(F1) (F2) (F3) (F4)
(F5) (F6) (F7)
Fig.7. 2-Dversionsofunimodalbenchmarkfunctions.
the proposed algorithm, three classical engineering design prob- designs,areemployed.Theseproblemshaveseveralequalityand
lems and a real problem in optical engineering are employed in inequalityconstraints,sotheGWOshouldbeequippedwithacon-
thefollowingsections.TheGWOalgorithmisalsocomparedwith strainthandlingmethodtobeabletooptimizeconstrainedprob-
well-knowntechniquestoconfirmitsresults. lems as well. Generally speaking, constraint handling becomes
verychallengingwhenthefitnessfunctiondirectlyaffectstheposi-
tionupdatingofthesearchagents(GSAforinstance).Forthefitness
5.GWOforclassicalengineeringproblems independentalgorithms,however,anykindofconstrainthandling
can be employed without the need to modify the mechanism of
Inthissectionthreeconstrainedengineeringdesignproblems: thealgorithm(GAandPSOforinstance).Sincethesearchagentsof
tension/compression spring, welded beam, and pressure vessel theproposedGWOalgorithmupdatetheirpositionswithrespect

54 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
|     | (F8) |     | (F9) |     | (F10)                              |     | (F11)   |     |
| --- | ---- | --- | ---- | --- | ---------------------------------- | --- | ------- | --- |
 (F12)
(F13)
Fig.8. 2-Dversionsofmultimodalbenchmarkfunctions.
|     | (F14)   |                                                                 | (F16) |        | (F17) |       | (F18) |     |
| --- | ------- | --------------------------------------------------------------- | ----- | ------ | ----- | ----- | ----- | --- |
|     |         | Fig.9. 2-Dversionoffixed-dimensionmultimodalbenchmarkfunctions. |       |        |       |       |       |     |
|     |         | (F24)                                                           |       | (F25)  |       |       | (F26) |     |
|     |         | (F27)                                                           |       | (F28)  |       | (F29) |       |     |
Fig.10. 2-Dversionsofcompositebenchmarkfunctions.
Table5
Resultsofunimodalbenchmarkfunctions.
| F GWO |     | PSO |     | GSA |     | DE  |     | FEP     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------- |
| Ave   | Std | Ave | Std | Ave | Std | Ave | Std | Ave Std |
F1 6.59E(cid:4)28 6.34E(cid:4)05 0.000136 0.000202 2.53E(cid:4)16 9.67E(cid:4)17 8.2E(cid:4)14 5.9E(cid:4)14 0.00057 0.00013
F2 7.18E(cid:4)17 0.029014 0.042144 0.045421 0.055655 0.194074 1.5E(cid:4)09 9.9E(cid:4)10 0.0081 0.00077
F3 3.29E(cid:4)06 79.14958 70.12562 22.11924 896.5347 318.9559 6.8E(cid:4)11 7.4E(cid:4)11 0.016 0.014
F4 5.61E(cid:4)07 1.315088 1.086481 0.317039 7.35487 1.741452 0 0 0.3 0.5
F5 26.81258 69.90499 96.71832 60.11559 67.54309 62.22534 0 0 5.06 5.87
F6 0.816579 0.000126 0.000102 8.28E(cid:4)05 2.5E(cid:4)16 1.74E(cid:4)16 0 0 0 0
F7 0.002213 0.100286 0.122854 0.044957 0.089441 0.04339 0.00463 0.0012 0.1415 0.3522
tothealpha,beta,anddeltalocations,thereisnodirectrelationbe- areassignedbigobjectivefunctionvaluesiftheyviolateanyofthe
tweenthesearchagentsandthefitnessfunction.Sothesimplest constraints, can be employed effectively to handle constraints in
constrainthandlingmethod,penaltyfunctions,wheresearchagents GWO.Inthiscase,ifthealpha,beta,ordeltaviolateconstraints,they

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 55
Table6
Resultsofmultimodalbenchmarkfunctions.
| F   | GWO |     |     |     | PSO |     | GSA |     |     | DE  |     |     | FEP |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Ave |     | Std |     | Ave | Std | Ave | Std |     | Ave |     | Std | Ave | Std |     |
F8 (cid:4)6123.1 (cid:4)4087.44 (cid:4)4841.29 1152.814 (cid:4)2821.07 493.0375 (cid:4)11080.1 574.7 (cid:4)12554.5 52.6
F9 0.310521 47.35612 46.70423 11.62938 25.96841 7.470068 69.2 38.8 0.046 0.012
F10 1.06E(cid:4)13 0.077835 0.276015 0.50901 0.062087 0.23628 9.7E(cid:4)08 4.2E(cid:4)08 0.018 0.0021
F11 0.004485 0.006659 0.009215 0.007724 27.70154 5.040343 0 0 0.016 0.022
F12 0.053438 0.020734 0.006917 0.026301 1.799617 0.95114 7.9E(cid:4)15 8E(cid:4)15 9.2E(cid:4)06 3.6E(cid:4)06
F13 0.654464 0.004474 0.006675 0.008907 8.899084 7.126241 5.1E(cid:4)14 4.8E(cid:4)14 0.00016 0.000073
Table7
Resultsoffixed-dimensionmultimodalbenchmarkfunctions.
| F   | GWO |     |     |     | PSO |     | GSA |     |     | DE  |     |     | FEP |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Ave |     | Std |     | Ave | Std | Ave | Std |     | Ave |     | Std | Ave | Std |     |
F14 4.042493 4.252799 3.627168 2.560828 5.859838 3.831299 0.998004 3.3E(cid:4)16 1.22 0.56
F15 0.000337 0.000625 0.000577 0.000222 0.003673 0.001647 4.5E(cid:4)14 0.00033 0.0005 0.00032
F16 (cid:4)1.03163 (cid:4)1.03163 (cid:4)1.03163 6.25E(cid:4)16 (cid:4)1.03163 4.88E(cid:4)16 (cid:4)1.03163 3.1E(cid:4)13 (cid:4)1.03 4.9E(cid:4)07
F17 0.397889 0.397887 0.397887 0 0.397887 0 0.397887 9.9E(cid:4)09 0.398 1.5E(cid:4)07
F18 3.000028 3 3 1.33E(cid:4)15 3 4.17E(cid:4)15 3 2E(cid:4)15 3.02 0.11
F19 (cid:4)3.86263 (cid:4)3.86278 (cid:4)3.86278 2.58E(cid:4)15 (cid:4)3.86278 2.29E(cid:4)15 N/A N/A (cid:4)3.86 0.000014
F20 (cid:4)3.28654 (cid:4)3.25056 (cid:4)3.26634 0.060516 (cid:4)3.31778 0.023081 N/A N/A (cid:4)3.27 0.059
F21 (cid:4)10.1514 (cid:4)9.14015 (cid:4)6.8651 3.019644 (cid:4)5.95512 3.737079 (cid:4)10.1532 0.0000025 (cid:4)5.52 1.59
F22 (cid:4)10.4015 (cid:4)8.58441 (cid:4)8.45653 3.087094 (cid:4)9.68447 2.014088 (cid:4)10.4029 3.9E(cid:4)07 (cid:4)5.53 2.12
F23 (cid:4)10.5343 (cid:4)8.55899 (cid:4)9.95291 1.782786 (cid:4)10.5364 2.6E(cid:4)15 (cid:4)10.5364 1.9E(cid:4)07 (cid:4)6.57 3.14
areautomaticallyreplacedwithanewsearchagentinthenextiter- mathematical approaches that have been adopted to solve this
ation.Anykindofpenaltyfunctioncanreadilybeemployedinorder problem are the numerical optimization technique (constraints
topenalizesearchagentsbasedontheirlevelofviolation.Inthis correction at constant cost) [55] and mathematical optimization
case,ifthepenaltymakesthealpha,beta,ordeltalessfitthanany technique[56].Thecomparisonofresultsofthesetechniquesand
|     |     |     |     |     |     |     |     | GWO are | provided | in  | Table 9. | Note that | we use | a similar | penalty |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | --------- | ------ | --------- | ------- |
otherwolves,itisautomaticallyreplacedwithanewsearchagent
inthenextiteration.Weusedsimple,scalarpenaltyfunctionsfor function for GWO to perform a fair comparison [63]. Table 9
therestofproblemsexceptthetension/compressionspringdesign suggeststhatGWOfindsadesignwiththeminimumweightforthis
| problemwhichusesamorecomplexpenaltyfunction. |     |     |     |     |     |     |     | problem. |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
5.2.Weldedbeamdesign
5.1.Tension/compressionspringdesign
Theobjectiveofthisproblemistominimizethefabricationcost
Theobjectiveofthisproblemistominimizetheweightofaten-
ofaweldedbeamasshowninFig.13[60].Theconstraintsareas
sion/compressionspringasillustratedinFig.12[55–57].Themin-
follows:
| imization | process |     | is subject | to  | some constraints | such | as shear |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | ---------- | --- | ---------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
stress,surgefrequency,andminimumdeflection.Therearethree
(cid:2) Shearstress(s).
| variables | in  | this problem: |     | wire diameter |     | (d), mean coil | diameter |     |     |     |     |     |     |     |     |
| --------- | --- | ------------- | --- | ------------- | --- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2) Bendingstressinthebeam(h).
(D),andthenumberofactivecoils(N).Themathematicalformula-
(cid:2) Bucklingloadonthebar(P).
| tionofthisproblemisasfollows: |     |     |     |     |     |     |     |     |     |     | c   |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2) Enddeflectionofthebeam(d).
|           |     | ~x¼½x    |               |                          |     |     |     | Sideconstraints. |            |     |                |        |                 |     |      |
| --------- | --- | -------- | ------------- | ------------------------ | --- | --- | --- | ---------------- | ---------- | --- | -------------- | ------ | --------------- | --- | ---- |
| Consider  |     |          | 1 x 2         | x 3 (cid:6)¼½dDN(cid:6); |     |     |     | (cid:2)          |            |     |                |        |                 |     |      |
| Minimize  |     | fð~xÞ¼ðx |               | þ2Þx                     | x2; |     |     |                  |            |     |                |        |                 |     |      |
|           |     |          | 3             | 2                        | 1   |     |     |                  |            |     |                |        |                 |     |      |
|           |     |          |               |                          |     |     |     | This             | problemhas |     | four variables | suchas | thicknessofweld |     | (h), |
| Subjectto |     | g        | ð~xÞ¼1(cid:4) | x 3 x 3                  | 60; |     |     |                  |            |     |                |        |                 |     |      |
1 2 x4 lengthofattachedpartofbar(l),theheightofthebar(t),andthick-
|     |     |     |     | 71 7 8 5 | 1   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nessofthebar(b).Themathematicalformulationisasfollows:
|     |     | g   | ð~xÞ¼        | 4x2 2 (cid:4)x1x2 | þ 1                | 60; |     |          |       |     |                          |     |     |     |     |
| --- | --- | --- | ------------ | ----------------- | ------------------ | --- | --- | -------- | ----- | --- | ------------------------ | --- | --- | --- | --- |
|     |     |     | 2 12566ðx2x3 |                   | (cid:4)x4 Þ 5108x2 |     |     | Consider | ~x¼½x | x x | x 4(cid:6)¼½hltb(cid:6); |     |     |     |     |
|     |     |     |              | 1                 | 1                  | 1   |     |          |       | 1 2 | 3                        |     |     |     |     |
2
g ð~xÞ¼ 4 x 2 (cid:4) x 1 x 2 þ 1 60; M i n i m iz e ðf ~x Þ ¼ 1 :1 0 4 71 x 2 1 x 2 þ 0 :04811x 3 x 4ð14:0þx 2Þ;
|               |     |     | 2 125         | 6 6 ð x2 x 3 | (cid:4) x4 Þ 510 | 8x2 | ð5:1Þ |              |          |                |                 |     |     |     |       |
| ------------- | --- | --- | ------------- | ------------ | ---------------- | --- | ----- | ------------ | -------- | -------------- | --------------- | --- | --- | --- | ----- |
|               |     |     |               | 1            | 1                | 1   |       | S u b j e ct | t o g ð~ | xÞ ¼ s ð~ xÞ   | (cid:4) s 6 0   | ;   |     |     |       |
|               |     |     | ~             | 1 4 0 : 4    | 5 x 16           |     |       |              | 1        |                | m ax            |     |     |     |       |
|               |     | g   | ð x Þ ¼ 1     | (cid:4)      | 0;               |     |       |              | g ð      | ~ x Þ ¼ r ð ~x | Þ (cid:4) r 6   | 0 ; |     |     |       |
|               |     |     | 3             | x 2 x        | 3                |     |       |              | 2        |                | m ax            |     |     |     |       |
|               |     |     |               | 2            |                  |     |       |              | g ð      | ~ x Þ ¼ dð ~x  | Þ (cid:4) d 6 0 | ;   |     |     | ð5:2Þ |
|               |     | g   | ð ~ x Þ ¼x 1þ | x2 (cid:4) 1 | 6 0;             |     |       |              | 3        |                | m ax            |     |     |     |       |
|               |     |     | 4             | 1: 5         |                  |     |       |              | ð~xÞ¼x   |                | 60;             |     |     |     |       |
| Variablerange |     | 0   | :056x         | 6 2:00;      |                  |     |       |              | g 4      | 1(cid:4)x      | 4               |     |     |     |       |
|               |     |     | 1             |              |                  |     |       |              |          |                | cð~xÞ60;        |     |     |     |       |
g 5 ð~xÞ¼P(cid:4)P
|     |     | 0:256x |     | 61:30; |     |     |     |     |     |               |                   |     |     |     |     |
| --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | ------------- | ----------------- | --- | --- | --- | --- |
|     |     |        | 2   |        |     |     |     |     | g ð | ~ x Þ ¼ 0 : 1 | 2 5 (cid:4) x 6 0 |     |     |     |     |
|     |     | 2:006x |     | 615:0  |     |     |     |     | 6   |               | 1                 |     |     |     |     |
3 g ð ~ x Þ ¼ 1 : 1 0 47 1x 2 þ 0 :04811x x 4ð14:0þx 2Þ(cid:4)5:060
|     |     |     |     |     |     |     |     |     | 7   |     | 1   | 3   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisproblemhasbeentackledbybothmathematicalandheuristic Variablerange 0:16x 62;
1
| approaches. |     | Ha and | Wang | tried | to solve | this problem | using PSO |     |     |       |      |     |     |     |     |
| ----------- | --- | ------ | ---- | ----- | -------- | ------------ | --------- | --- | --- | ----- | ---- | --- | --- | --- | --- |
|             |     |        |      |       |          |              |           |     |     | 0:16x | 610; |     |     |     |     |
[58]. The Evolution Strategy (ES) [59], GA [60], Harmony Search 2
|     |     |     |     |     |     |     |     |     |     | 0:16x | 610; |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- |
(HS) [61], and Differential Evolution (DE) [62] algorithms have 3
also been employed as heuristic optimizers for this problem. The 0:16x 62
4

56 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
Table8
Resultsofcompositebenchmarkfunctions.
| F   | GWO |     | PSO     | GSA |     | DE  |     | CMA-ES |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ------ | --- |
|     | Ave | Std | Ave Std | Ave | Std | Ave | Std | Ave    | Std |
F24 43.83544 69.86146 100 81.65 6.63E(cid:4)17 2.78E(cid:4)17 6.75E(cid:4)02 1.11E(cid:4)01 100 188.56
F25 91.80086 95.5518 155.91 13.176 200.6202 67.72087 28.759 8.6277 161.99 151
F26 61.43776 68.68816 172.03 32.769 180 91.89366 144.41 19.401 214.06 74.181
F27 123.1235 163.9937 314.3 20.066 170 82.32726 324.86 14.784 616.4 671.92
F28 102.1429 81.25536 83.45 101.11 200 47.14045 10.789 2.604 358.3 168.26
F29 43.14261 84.48573 861.42 125.81 142.0906 88.87141 490.94 39.461 900.26 8.32E(cid:4)02
|     | qffi ffi ffiffiffi ffi ffiffi ffiffiffi ffiffiffiffiffi | ffiffiffi ffiffi ffiffi ffiffi ffi ffiffi ffiffi ffiffiffi ffiffiffiffiffi ffiffi ffiffi ffi ffi ffiffi ffiffi |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
where sð~xÞ¼ ð s 0 Þ 2 þ 2 s 0 s 0 0 x 2 þ ð s 0 0 Þ 2 ; inFig.14.Bothendsofthevesselarecapped,andtheheadhasa
2R
s0¼pffi2ffix P ;s00¼M R;M¼PðLþx 2Þ; hemi-sphericalshape.Therearefourvariablesinthisproblem:
|     | 1x2 | J 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
|     | R x 2 (cid:5) x1 þ x (cid:6) | 2;  |     |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
¼ 4 2 þ 2 3 (cid:2) T h i c k n e s s o f t h e s h e l l( T ) .
|     | np ffi2 ffiffix1 h 2 | (cid:6)2io |     |     |     |     | s   |     |     |
| --- | -------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
J ¼ 2 x x 2 þ (cid:5)x1þ x3 ; (cid:2) T h i c k n e s s o f t h e h e a d ( T ) .
|     | 2 4                  | 2   |     |     |                         |     | h   |     |     |
| --- | -------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
|     | rð~xÞ¼6PL;dð~xÞ¼6PL3 |     |     |     | (cid:2) Innerradius(R). |     |     |     |     |
x4x2 Ex2
3 3x4 (cid:2) Lengthofthecylindricalsectionwithoutconsideringthehead
qffiffiffiffiffiffi x2 6
|     | 4:013E 3 x     | 4(cid:3) qffi ffi ffiffi(cid:4) |     |     | (L). |     |     |     |     |
| --- | -------------- | ------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
|     | Pcð~xÞ¼ L2 3 6 | 1(cid:4)x 3 E ;                 |     |     |      |     |     |     |     |
2 L 4 G
|     | P¼6000lb;L¼14in:; | dmax¼0:25in: | ;E¼30(cid:7)16psi;G¼12(cid:7)106psi; |     |     |     |     |     |     |
| --- | ----------------- | ------------ | ------------------------------------ | --- | --- | --- | --- | --- | --- |
s max¼13600psi; r max¼30000psi This problem is subject to four constraints. These constraints
andtheproblemareformulatedasfollows:
Coello[64]andDeb[65,66]employedGA,whereasLeeandGeem Consider ~x¼½x 1 x 2 x 3 x 4(cid:6)¼½T s T h RL(cid:6);
[67] used HS to solve thisproblem. Richardson’s randommethod, Minimize fð~xÞ¼0:6224x x x 4þ1:7781x x2 þ3:1661x2 x 4þ19:84x2 x ;
|     |     |     |     |     |     |     | 1 3 | 2 3 1 | 1 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Simplex method, Davidon-Fletcher-Powell, Griffith and Stewart’s Subjectto g ð~xÞ¼(cid:4)x 1þ0:0193x 60;
|     |     |     |     |     | 1   |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
successive linear approximation are the mathematical approaches g ð~xÞ¼(cid:4)x 3þ0:00954x 60;
|     |     |     |     |     | 2   |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t h a t h a v e b e en a d o p t e d b y R a g s d e l l a n d P h i li p s [6 8] fo r t h i s p r o b - ~ p x2 4 p x3 þ129600060;
|     |     |     |     |     | g 3 | ð x Þ ¼(cid:4) 3 x | 4 (cid:4) 3 3 |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --- | --- |
le m . T h e c o m p a r i s o n r es u lt s a r e p r o v i d ed i n T a b l e 1 0 . T h e re s u l t s 6
|         |                    |                    |                          |                        | g   | ð ~ x Þ¼ x 4 (cid:4) 2 4 | 0 0 ; |     |     |
| ------- | ------------------ | ------------------ | ------------------------ | ---------------------- | --- | ------------------------ | ----- | --- | --- |
| s h o w | t h a t G W O fi n | d s a d e s ig n w | it h t h e m i n i m u m | co s t c o m p a r e d | 4   |                          |       |     |     |
ð5:3Þ
toothers.
|     |     |     |     |     | Variablerange | 06x | 699; |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | ---- | --- | --- |
1
06x 699;
| 5.3.Pressurevesseldesign |     |     |     |     |     |     | 2   |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
106x 6200;
3
Theobjectiveofthisproblemistominimizethetotalcostcon- 106x 6200;
4
sistingofmaterial,forming,andweldingofacylindricalvesselas
Fig.11. Searchhistoryandtrajectoryofthefirstparticleinthefirstdimension.

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 57
Fig.11(continued)
Fig.12. Tension/compressionspring:(a)shematic,(b)stressheatmap(c)displacementheatmap.
This problem has also been popular among researchers and Insummary,theresultsonthethreeclassicalengineeringprob-
optimizedinvariousstudies.Theheuristicmethodsthathavebeen lems demonstrate that GWO shows high performance in solving
adoptedtooptimizethisproblemare:PSO[58],GA[57,60,69],ES challenging problems. This is again due to the operators that are
[59], DE [62], and ACO [70]. Mathematicalmethodsusedareaug- designedtoallowGWOtoavoidlocaloptimasuccessfullyandcon-
mentedLagrangianMultiplier[71]andbranch-and-bound[72].The verge towards the optimum quickly. The next section probes the
resultsofthisproblemareprovidedinTable11.Accordingtothista- performanceoftheGWOalgorithminsolvingarecentrealprob-
ble,GWOisagainabletofindadesignwiththeminimumcost. leminthefieldofopticalengineering.

58 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
| Table9 |     |     |     |     |     |     | Table10 |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
Comparisonofresultsfortension/compressionspringdesignproblem. Comparisonresultsoftheweldedbeamdesignproblem.
Algorithm Optimumvariables Optimum Algorithm Optimumvariables Optimum
|     |     |     |     |     | weight |     |     |     |     |     | cost |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---- |
|     |     | d   | D   | N   |        |     |     | h   | l t | b   |      |
GWO 0.05169 0.356737 11.28885 0.012666 GWO 0.205676 3.478377 9.03681 0.205778 1.72624
GSA 0.050276 0.323680 13.525410 0.0127022 GSA 0.182129 3.856979 10.00000 0.202376 1.879952
PSO(HaandWang) 0.051728 0.357644 11.244543 0.0126747 GA(Coello) N/A N/A N/A N/A 1.8245
ES(CoelloandMontes) 0.051989 0.363965 10.890522 0.0126810 GA(Deb) N/A N/A N/A N/A 2.3800
GA(Coello) 0.051480 0.351661 11.632201 0.0127048 GA(Deb) 0.2489 6.1730 8.1789 0.2533 2.4331
HS(Mahdavietal.) 0.051154 0.349871 12.076432 0.0126706 HS(Leeand 0.2442 6.2231 8.2915 0.2443 2.3807
| DE(Huangetal.) |     | 0.051609 | 0.354714 | 11.410831 | 0.0126702 |     | Geem) |     |     |     |     |
| -------------- | --- | -------- | -------- | --------- | --------- | --- | ----- | --- | --- | --- | --- |
Mathematical 0.053396 0.399180 9.1854000 0.0127303 Random 0.4575 4.7313 5.0853 0.6600 4.1185
| optimization |     |     |     |     |     |     | Simplex | 0.2792 | 5.6256 7.7512 | 0.2796 | 2.5307 |
| ------------ | --- | --- | --- | --- | --- | --- | ------- | ------ | ------------- | ------ | ------ |
| (Belegundu)  |     |     |     |     |     |     | David   | 0.2434 | 6.2552 8.2915 | 0.2444 | 2.3841 |
Constraintcorrection 0.050000 0.315900 14.250000 0.0128334 APPROX 0.2444 6.2189 8.2915 0.2444 2.3815
(Arora)
6.RealapplicationofGWOinopticalengineering(opticalbuffer Therearetwo metricsfor comparingtheperformance ofslow
design) light devices: Delay-Bandwidth Product (DBP) and Normalized
DBP(NDBP),whicharedefinedasfollows[74]:
Theprobleminvestigatedinthissectioniscalledopticalbuffer DBP¼Dt(cid:3)Df ð6:1Þ
design.Infact,anopticalbufferisoneofthemaincomponentsof
optical CPUs. The optical buffer slows the group velocity of light whereDtindicatesthedelayandDfisthebandwidthoftheslow
| and allows | the optical | CPUs | to process | optical | packets or | adjust | lightdevice. |     |     |     |     |
| ---------- | ----------- | ---- | ---------- | ------- | ---------- | ------ | ------------ | --- | --- | --- | --- |
itstiming.ThemostpopulardevicetodothisisaPhotonicCrystal Inslowlightdevicestheultimategoalistoachievemaximum
Waveguide (PCW). PCWs mostly have a lattice-shaped structure transmission delay of an optical pulse with highest PCW band-
with a line defect in the middle. The radii of holes and shape of width. Obviously, Dt should be increased in order to increase
thelinedefectyielddifferentslowlightcharacteristics.Varyingra- DBP. This is achieved by increasing the length of the device (L).
diiandlinedefectsprovidesdifferentenvironmentsforrefracting Tocomparedeviceswithdifferentlengthsandoperatingfrequen-
the light in the waveguide. The researchers in this field try to cies,NDBPisabetterchoice[75]:
manipulate the radii of holes and pins of line defect in order to NDBP¼n (cid:3)Dx=x ð6:2Þ
|                   |     |         |                            |     |       |          | g   | 0   |     |     |     |
| ----------------- | --- | ------- | -------------------------- | --- | ----- | -------- | --- | --- | --- | --- | --- |
| achieve desirable |     | optical | buffering characteristics. |     | There | are also |     |     |     |     |     |
different types of PCW that are suitable for specific applications. wherengistheaverageofthegroupindex,Dxisthenormalized
In this section the structure of a PCW called a Bragg Slot PCW bandwidth, and x is the normalized central frequency of light
0
| (BSPCW) | is optimized | by  | the GWO algorithm. |     | This problem | has | wave. |     |     |     |     |
| ------- | ------------ | --- | ------------------ | --- | ------------ | --- | ----- | --- | --- | --- | --- |
severalconstraints,soweutilizethesimplestconstrainthandling SinceNDBPhasadirectrelationtothegroupindex(n ),canbe
g
| methodforGWOinthissectionaswell. |     |     |     |     |     |     | formulatedasfollows[76]: |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
BSPCWstructurewasfirstproposedbyCaeretal.in2011[73].
|     |     |     |     |     |     |     | C   | dk  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThestructureofBSPCWsisillustratedinFig.15.Thebackground n ¼ ¼C ð6:3Þ
|                 |           |              |                   |          |           |          | g v        | dx              |             |          |                  |
| --------------- | --------- | ------------ | ----------------- | -------- | --------- | -------- | ---------- | --------------- | ----------- | -------- | ---------------- |
| slab is silicon | with      | a refractive | index             | equal to | 3.48. The | slot and | g          |                 |             |          |                  |
| holes are       | filled by | a material   | with a refractive |          | index of  | 1.6. The |            |                 |             |          |                  |
|                 |           |              |                   |          |           |          | where x is | the dispersion, | k indicates | the wave | vector, C is the |
Bragg slot structure allows the BSPCW to have precise control of velocityoflightinfreespace,andshowsthegroupindex.Sincen
g
dispersion and slow light properties. The first five holes adjacent is changing in the bandwidth range, it should be averaged as
| totheslothavethehighestimpactonslowlightproperties,asdis- |     |     |     |     |                |     | follows: |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | -------------- | --- | -------- | --- | --- | --- | --- |
| cussedin[73].AsmaybeseeninFig.15,                         |     |     |     | l,w | andw definethe |     |          |     |     |     |     |
|                                                           |     |     |     |     | l, h           |     | Z x H    | dx  |     |     |     |
shape of the slot and have an impact on the final dispersion and n ¼ n ðxÞ ð6:4Þ
|                                                            |     |     |     |     |     |     | g   | g Dx |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
| slowlightpropertiesaswell.So,variousdispersionandslowlight |     |     |     |     |     |     | x   |      |     |     |     |
L
propertiescanbeachievedbymanipulatingtheradiiofholes,l,w
|        |     |     |     |     |     | l,  | ThebandwidthofaPCWreferstotheregionofthen             |     |     |     | curvewhere |
| ------ | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | ---------- |
| andw . |     |     |     |     |     |     |                                                       |     |     |     | g          |
| h      |     |     |     |     |     |     | n hasanapproximatelyconstantvaluewithamaximumfluctua- |     |     |     |            |
g
|     |     |     | Fig.13. Structureofweldedbeamdesign(a)shematic(b)stressheatmap(c)displacementheatmap. |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 59
Fig.14. Pressurevessel(a)shematic(b)stressheatmap(c)displacementheatmap.
Table11
Comparisonresultsforpressurevesseldesignproblem.
| Algorithm |     |     | Optimumvariables |          |     |            |     |            |     |     | Optimumcost |     |
| --------- | --- | --- | ---------------- | -------- | --- | ---------- | --- | ---------- | --- | --- | ----------- | --- |
|           |     |     | Ts               | Th       |     | R          |     | L          |     |     |             |     |
| GWO       |     |     | 0.812500         | 0.434500 |     | 42.089181  |     | 176.758731 |     |     | 6051.5639   |     |
| GSA       |     |     | 1.125000         | 0.625000 |     | 55.9886598 |     | 84.4542025 |     |     | 8538.8359   |     |
PSO(HeandWang) 0.812500 0.437500 42.091266 176.746500 6061.0777
| GA(Coello) |     |     | 0.812500 | 0.434500 |     | 40.323900 |     | 200.000000 |     |     | 6288.7445 |     |
| ---------- | --- | --- | -------- | -------- | --- | --------- | --- | ---------- | --- | --- | --------- | --- |
GA(CoelloandMontes) 0.812500 0.437500 42.097398 176.654050 6059.9463
GA(DebandGene) 0.937500 0.500000 48.329000 112.679000 6410.3811
ES(MontesandCoello) 0.812500 0.437500 42.098087 176.640518 6059.7456
DE(Huangetal.) 0.812500 0.437500 42.098411 176.637690 6059.7340
ACO(KavehandTalataheri) 0.812500 0.437500 42.103624 176.572656 6059.0888
LagrangianMultiplier(Kannan) 1.125000 0.625000 58.291000 43.6900000 7198.0428
Branch-bound(Sandgren) 1.125000 0.625000 47.700000 117.701000 8129.1036
|     |     |              |     |     | Consider: |     | ~x¼½x x          | x x x x | x x (cid:6)¼ | (cid:11)R 1 R 2 | R 3 R 4 R 5 | l w h w l (cid:12) ; |
| --- | --- | ------------ | --- | --- | --------- | --- | ---------------- | ------- | ------------ | --------------- | ----------- | -------------------- |
|     |     |              |     |     |           |     | 1 2              | 3 4 5   | 6 7 8        | a a             | a a a       | a a a                |
|     |     | a Super cell |     |     | Maximize: |     | fð~xÞ¼NDBP¼ngDx; |         |              |                 |             |                      |
x
0
ðxÞjÞ<106a=2pc2;
|     | 2R   |     |     |     | Subjectto: |     | maxðjb   |        |     |     |     |     |
| --- | ---- | --- | --- | --- | ---------- | --- | -------- | ------ | --- | --- | --- | --- |
|     | 5    |     |     |     |            |     | 2        |        |     |     |     |     |
|     |      |     |     |     |            |     | x <minðx |        | Þ;  |     |     |     |
|     | 2R 4 |     |     |     |            |     | H        | upband |     |     |     |     |
Si
|     | 2R   |     |     |        |        |     | x >maxðx        |            | Þ;  |     |     |       |
| --- | ---- | --- | --- | ------ | ------ | --- | --------------- | ---------- | --- | --- | --- | ----- |
|     | 3    |     |     |        |        |     | L               | downband   |     |     |     |       |
|     | 2R 2 |     |     | Filled |        |     | k >k !x         |            | >x  | ;   |     |       |
|     |      |     |     |        |        |     | n nH            | Guidedmode |     | H   |     |       |
|     | 2R   |     |     |        |        |     | k <k !x         |            | <x  | ;   |     | ð6:5Þ |
|     | 1    |     |     |        |        |     | n nL            | Guidedmode |     | L   |     |       |
|     | w    |     |     | w      |        |     |                 |            |     |     |     |       |
|     | l    |     |     | h      |        |     |                 |            |     |     |     |       |
|     |      |     |     |        | where: |     | x ¼xðk Þ¼xð1:1n |            | Þ;  |     |     |       |
|     |      |     |     |        |        |     | H nH            |            | g0  |     |     |       |
|     |      |     |     |        |        |     | x ¼xðk Þ¼xð0:9n |            | Þ;  |     |     |       |
|     | l    |     |     |        |        |     | L nL            |            | g0  |     |     |       |
|     |      |     |     |        |        |     | k ¼ka           |            |     |     |     |       |
n 2p
|     |     |     |     |     |     |     | Dx¼x (cid:4)x |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
H L ;
|     |     |     |     |     |     |     | a¼x (cid:5)1550ðnmÞ; |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
0
Fig.15. BSPCWstructurewithsupercell,nbackground=3.48andnfilled=1.6. 06x 60:5;
|     |     |     |     |     | Variablerange: |     |     | 1(cid:4)5 |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     |     |                |     | 06x | 61;       |     |     |     |     |
6
tion rage of ±10% [75]. Detailed information about PCWs can be 06x 61;
7;8
foundin[77–80].
Finally,theproblemismathematicallyformulatedforGWOas NotethatweconsiderfiveconstraintsfortheGWOalgorithm.
follows: Thesecondtofifthconstraintsavoidbandmixing.Tohandlefeasi-
bility,weassignsmallnegativeobjectivefunctionvalues((cid:4)100)to
thosesearchagentsthatviolatetheconstraints.
Table12
TheGWOalgorithmwasrun20timesonthisproblemandthe
Structuralparametersandcalculationresults.
bestresultsobtainedarereportedinTable12.Notethatthealgo-
| Structuralparameter |     |     | Wuetal.[81] | GWO      |             |     |                  |      |         |                   |         |             |
| ------------------- | --- | --- | ----------- | -------- | ----------- | --- | ---------------- | ---- | ------- | ----------------- | ------- | ----------- |
|                     |     |     |             |          | rithm       | was | run by 24 CPUs   | on a | Windows | HPC               | cluster | at Griffith |
| R1                  |     |     | –           | 0.33235a |             |     |                  |      |         |                   |         |             |
|                     |     |     |             |          | University. |     | This table shows | that | there   | is a substantial, |         | 93% and     |
| R2                  |     |     | –           | 0.24952a |             |     |                  |      |         |                   |         |             |
R3 – 0.26837a 65% improvement in bandwidth (Dk) and NDBP utilizing the
| R4  |     |     | –   | 0.29498a | GWOalgorithm. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
R5 – 0.34992a ThephotonicbandstructureoftheBSPCWoptimizedisshown
l – 0.7437a inFig.16(a).Inaddition,thecorrespondedgroupindexandopti-
| Wh    |     |     | –   | 0.2014a  |       |       |                |           |             |        |           |           |
| ----- | --- | --- | --- | -------- | ----- | ----- | -------------- | --------- | ----------- | ------ | --------- | --------- |
|       |     |     |     |          | mized | super | cell are shown | in        | Figs. 16(b) | and    | 17. These | figures   |
| Wl    |     |     | –   | 0.60073a |       |       |                |           |             |        |           |           |
|       |     |     |     |          | show  | that  | the optimized  | structure | has         | a very | good      | bandwidth |
| a(nm) |     |     | 430 | 343      |       |       |                |           |             |        |           |           |
n(cid:2) 23 19.6 without band mixing as well. This again demonstrated the high
g
Dk(nm) 17.6 33.9 performanceoftheGWOalgorithminsolvingrealproblems.
Orderofmagnitudeofb2(a/2pc2) 103 103 ThiscomprehensivestudyshowsthattheproposedGWOalgo-
NDBP 0.26 0.43 rithm has merit among the current meta-heuristics. First, the re-

100
80
60
40
20
0
0.214 0.216 0.218 0.22 0.222 0.224
Normalized Frequency (ωa/2πc=a/ )
(a) (b)
nally,theconvergenceanalysisofGWOconfirmedtheconvergence
ofthisalgorithm.
Moreover,theresults ofthe engineering designproblemsalso
showed that the GWO algorithm has high performance in un-
known,challengingsearchspaces.TheGWOalgorithmwasfinally
appliedtoarealprobleminopticalengineering.Theresultsonthis
problemshowedasubstantialimprovementofNDBPcomparedto
current approaches, showing the applicability of the proposed
algorithminsolvingrealproblems.Itmaybenotedthattheresults
on semi-real and real problems also proved that GWO can show
high performance not only on unconstrained problems but also
onconstrainedproblems.
For future work, we are going to develop binary and multi-
objectiveversionsoftheGWOalgorithm.
AppendixA.Supplementarymaterial
Supplementarydataassociatedwiththisarticlecanbefound,in
theonlineversion,athttp://dx.doi.org/10.1016/j.advengsoft.2013.
sults of the unconstrained benchmark functions demonstrate the
12.007.
performanceoftheGWOalgorithmintermsofexploration,exploi-
tation, local optima avoidance, and convergence. Second, the re-
sults of the classical engineering problems show the superior
References
performance of the proposed algorithm in solving semi-real con-
strainedproblems.Finally,theresultsoftheopticalbufferdesign
[1] Bonabeau E, Dorigo M, Theraulaz G. Swarm intelligence: from natural to
problemshowtheabilityoftheGWOalgorithminsolvingthereal artificialsystems:OUPUSA;1999.
problems. [2] DorigoM,BirattariM,StutzleT.Antcolonyoptimization.ComputIntellMagaz,
IEEE2006;1:28–39.
[3] KennedyJ,EberhartR.Particleswarmoptimization,inNeuralNetworks,1995.
In:Proceedings,IEEEinternationalconferenceon;1995.p.1942–1948.
[4] WolpertDH,MacreadyWG.Nofreelunchtheoremsforoptimization.Evolut
7.Conclusion Comput,IEEETrans1997;1:67–82.
[5] KirkpatrickS,Jr.DG,VecchiMP.Optimizationbysimulatedannealing.Science,
vol.220;1983.p.671–80.
ThisworkproposedanovelSIoptimizationalgorithminspired
[6] BeniG,WangJ.Swarmintelligenceincellularroboticsystems.In:Robotsand
bygreywolves.Theproposedmethodmimickedthesocialhierar- biologicalsystems:towardsanewbionics?,ed.Springer;1993.p.703–12.
chyand huntingbehaviorofgreywolves.Twentyninetestfunc- [7] BasturkB,KarabogaD.Anartificialbeecolony(ABC)algorithmfornumeric
tions were employed in order to benchmark the performance of functionoptimization.In:IEEEswarmintelligencesymposium;2006.p.12–4.
[8] Olorunda O, Engelbrecht AP. Measuring exploration/exploitation in particle
theproposedalgorithmintermsofexploration,exploitation,local swarmsusingswarmdiversity.In:Evolutionarycomputation,2008.CEC2008
optimaavoidance,andconvergence.TheresultsshowedthatGWO (IEEEWorldCongressonComputationalIntelligence).IEEECongresson;2008.
wasabletoprovidehighlycompetitiveresultscomparedtowell- p.1128–34.
[9] AlbaE,DorronsoroB.Theexploration/exploitationtradeoffindynamiccellular
knownheuristicssuchasPSO,GSA,DE,EP,andES.First,theresults
geneticalgorithms.EvolutComput,IEEETrans2005;9:126–42.
ontheunimodalfunctionsshowedthesuperiorexploitationofthe [10] Lin L, Gen M. Auto-tuning strategy for evolutionary algorithms: balancing
GWOalgorithm.Second,theexplorationabilityofGWOwascon- betweenexplorationandexploitation.SoftComput2009;13:157–68.
[11] Mirjalili S, Hashim SZM. A new hybrid PSOGSA algorithm for function
firmed by the results on multimodal functions. Third, the results
optimization. In: Computer and information application (ICCIA), 2010
ofthecompositefunctionsshowedhighlocaloptimaavoidance.Fi- internationalconferenceon;2010.p.374–77.
n—xednI
puorG
ehT
g
0.26
0.24
0.22
Δω
0.2
ω
H
0.18
ω
ω 0
L
0.16
0.25 0.3 0.35 0.4 0.45 0.5
Wavevector--ka/2π
)λ/a=cπ2/aω(
ycneuqerF
dezilamroN
60 S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61
Light line
of SiO 2
Guided mode
Fig.16. (a)PhotonicbandstructureoftheoptimizedBSPCWstructure(b)Thegroupindex(ng)oftheoptimizedBSPCWstructure.
R=120nm
5
R=101nm
4
R=92nm 3
R=84nm
2
R=114nm
1
w l =69nm w h =206nm
l=255nm
Fig.17. OptimizedsupercellofBSPCW.

S.Mirjalilietal./AdvancesinEngineeringSoftware69(2014)46–61 61
[12] Mirjalili S, Mohd Hashim SZ, Moradian Sardroudi H. Training feedforward [48] DigalakisJ,MargaritisK.Onbenchmarkingfunctionsforgeneticalgorithms.
neuralnetworksusinghybridparticleswarmoptimizationandgravitational IntJComputMath2001;77:481–506.
searchalgorithm.ApplMathComput2012;218:11125–37. [49] MolgaM,SmutnickiC.Testfunctionsforoptimizationneeds.Testfunctionsfor
[13] HollandJH.Geneticalgorithms.SciAm1992;267:66–72. optimizationneeds;2005.
[14] GoldbergD.GeneticAlgorithmsinoptimization,searchandmachinelearning, [50] Yang X-S. Test problems in optimization, arXiv, preprint arXiv:1008.0549;
AddisonWesley,NewYork.In:EibenAE,SmithJE,editors.2003Introduction 2010.
toevolutionarycomputing.Springer.JacqJ,RouxC(1995)Registrationofnon- [51] MirjaliliS,LewisA.S-shapedversusV-shapedtransferfunctionsforbinary
segmented images using a genetic algorithm. Lecture notes in computer ParticleSwarmOptimization.SwarmEvolutComput2013;9:1–14.
science,vol.905;1989.p.205–11. [52] LiangJ,SuganthanP,DebK.Novelcompositiontestfunctionsfornumerical
[15] StornR,PriceK.Differentialevolution–asimpleandefficientheuristicfor global optimization. In: Swarm intelligence symposium, 2005. SIS 2005.
globaloptimizationovercontinuousspaces.JGlobalOptim1997;11:341–59. Proceedings2005IEEE;2005.p.68–75.
[16] YaoX,LiuY,LinG.Evolutionaryprogrammingmadefaster.EvolutComput, [53] SuganthanPN,HansenN,LiangJJ,DebK,ChenYP,AugerA,etal.Problem
IEEETrans1999;3:82–102. definitionsandevaluationcriteriafortheCEC2005specialsessiononreal-
[17] FogelD.Artificialintelligencethroughsimulatedevolution.Wiley-IEEEPress; parameteroptimization,TechnicalReport,NanyangTechnologicalUniversity,
2009. Singapore,2005,http://www.ntu.edu.sg/home/EPNSugan.
[18] HansenN,MüllerSD,KoumoutsakosP.Reducingthetimecomplexityofthe [54] van den Bergh F, Engelbrecht A. A study of particle swarm optimization
derandomizedevolutionstrategywithcovariancematrixadaptation(CMA- particletrajectories.InfSci2006;176:937–71.
ES).EvolutComput2003;11:1–18. [55] AroraJS.Introductiontooptimumdesign.AcademicPress;2004.
[19] RechenbergI.Evolutionstrategy.ComputIntelImitatLife1994;1. [56] BelegunduAD,AroraJS.AStudyofmathematicalprogrammingmethodsfor
[20] KozaJR.Geneticprogramming;1992. structuraloptimization.PartI:Theory.IntJNumerMethEng1985;21:1583–99.
[21] Simon D. Biogeography-based optimization. Evolut Comput IEEE Trans [57] CoelloCoelloCA,MezuraMontesE.Constraint-handlingingeneticalgorithms
2008;12:702–13. throughtheuseofdominance-basedtournamentselection.AdvEngInform
[22] Webster B, Bernhard PJ. A local search optimization algorithm based on 2002;16:193–203.
natural principles of gravitation. In: Proceedings of the 2003 international [58] HeQ,WangL.Aneffectiveco-evolutionaryparticleswarmoptimizationfor
conference on information and knowledge engineering (IKE’03), Las Vegas, constrainedengineeringdesignproblems.EngApplArtifIntell2007;20:89–99.
Nevada,USA;2003.p.255–61. [59] Mezura-Montes E, Coello CAC. An empirical study about the usefulness of
[23] ErolOK,EksinI.Anewoptimizationmethod:bigbang–bigcrunch.AdvEng evolutionstrategiestosolveconstrainedoptimizationproblems.IntJGenSyst
Softw2006;37:106–11. 2008;37:443–73.
[24] Rashedi E, Nezamabadi-Pour H, Saryazdi S. GSA: a gravitational search [60] Coello Coello CA. Use of a self-adaptive penalty approach for engineering
algorithm.InfSci2009;179:2232–48. optimizationproblems.ComputInd2000;41:113–27.
[25] KavehA,TalatahariS.Anovelheuristicoptimizationmethod:chargedsystem [61] Mahdavi M, Fesanghary M, Damangir E. An improved harmony search
search.ActaMech2010;213:267–89. algorithm for solving optimization problems. Appl Math Comput
[26] FormatoRA.Centralforceoptimization:anewmetaheuristicwithapplications 2007;188:1567–79.
inappliedelectromagnetics.ProgElectromagRes2007;77:425–91. [62] HuangF,WangL,HeQ.Aneffectiveco-evolutionarydifferentialevolutionfor
[27] AlatasB.ACROA:artificialchemicalreactionoptimizationalgorithmforglobal constrainedoptimization.ApplMathComput2007;186:340–56.
optimization.ExpertSystAppl2011;38:13170–80. [63] YangXS.Nature-inspiredmetaheuristicalgorithms.LuniverPress;2011.
[28] Hatamlou A. Black hole: a new heuristic optimization approach for data [64] CarlosA,COELLOC.Constraint-handlingusinganevolutionarymultiobjective
clustering.InfSci2012. optimizationtechnique.CivilEngSyst2000;17:319–46.
[29] Kaveh A, Khayatazad M. A new meta-heuristic method: ray optimization. [65] Deb K. Optimal design of a welded beam via genetic algorithms. AIAA J
ComputStruct2012;112:283–94. 1991;29:2013–5.
[30] Du H, Wu X, Zhuang J. Small-world optimization algorithm for function [66] DebK.Anefficientconstrainthandlingmethodforgeneticalgorithms.Comput
optimization. In: Advances in Natural Computation, ed.: Springer; 2006. p. MethodsApplMechEng2000;186:311–38.
264–73. [67] LeeKS,GeemZW.Anewmeta-heuristicalgorithmforcontinuousengineering
[31] Shah-HosseiniH.Principalcomponentsanalysisbythegalaxy-basedsearch optimization: harmony search theory and practice. Comput Methods Appl
algorithm:anovelmetaheuristicforcontinuousoptimisation.IntJComputSci MechEng2005;194:3902–33.
Eng2011;6:132–40. [68] RagsdellK,PhillipsD.Optimaldesignofaclassofweldedstructuresusing
[32] Moghaddam FF, Moghaddam RF, Cheriet M. Curved space optimization: a geometricprogramming.ASMEJEngIndust1976;98:1021–5.
random search based on general relativity theory. arXiv, preprint [69] DebK,GeneAS.Arobustoptimaldesigntechniqueformechanicalcomponent
arXiv:1208.2214;2012. design.In:PresentedattheDasguptaD,MichalewiczZ,editors.Evolutionary
[33] Yang X-S. A new metaheuristic bat-inspired algorithm. In: Nature inspired algorithmsinengineeringapplications,Berlin;1997.
cooperativestrategiesforoptimization(NICSO2010),ed.:Springer;2010.p. [70] KavehA,TalatahariS.Animprovedantcolonyoptimizationforconstrained
65–74. engineering design problems. Eng Comput Int J Comput-Aided Eng
[34] Abbass HA. MBO: Marriage in honey bees optimization – a haplometrosis 2010;27:155–82.
polygynous swarming approach. In: Evolutionary computation, 2001. [71] KannanB,KramerSN.AnaugmentedLagrangemultiplierbasedmethodfor
Proceedingsofthe2001congresson;2001.p.207–214. mixed integer discrete continuous optimization and its applications to
[35] LiX.Anewintelligentoptimization-artificialfishswarmalgorithm.Doctor mechanicaldesign.JMechDes1994;116:405.
thesis,ZhejiangUniversityofZhejiang,China;2003. [72] Sandgren E. Nonlinear integer and discrete programming in mechanical
[36] RothM.Termite:aswarmintelligentroutingalgorithmformobilewireless design;1988.p.95–105.
ad-hocnetworks;2005. [73] CaerC,LeRouxX,Marris-MoriniD,IzardN,VivienL,GaoD,etal.Dispersion
[37] PintoPC,RunklerTA,SousaJM.WaspswarmalgorithmfordynamicMAX-SAT engineering of wide slot photonic crystal waveguides by Bragg-like
problems. In: Adaptive and Natural Computing Algorithms, ed.: Springer; corrugationoftheslot.PhotonicsTechnolLett,IEEE2011;23:1298–300.
2007.p.350–57. [74] BabaT.Slowlightinphotoniccrystals.NatPhotonics2008;2:465–73.
[38] MucherinoA,SerefO.Monkeysearch:anovelmetaheuristicsearchforglobal [75] Zhai Y, Tian H, Ji Y. Slow light property improvement and optical buffer
optimization.In:AIPconferenceproceedings;2007.p.162. capability in ring-shape-hole photonic crystal waveguide. Light Technol J
[39] Lu X, Zhou Y. A novel global convergence algorithm: bee collecting pollen 2011;29:3083–90.
algorithm.In:Advancedintelligentcomputingtheoriesandapplications.With [76] WangD,ZhangJ,YuanL,LeiJ,ChenS,HanJ,etal.Slowlightengineeringin
AspectsofArtificialIntelligence,ed.:Springer;2008.p.518–25. polyatomic photonic crystal waveguides based on square lattice. Optics
[40] Yang X-S, Deb S. Cuckoo search via Lévy flights. In: Nature & Biologically Commun2011;284:5829–32.
InspiredComputing,2009.NaBIC2009.WorldCongresson;2009.p.210–14. [77] Mirjalili SM, Mirjalili S. Light property and optical buffer performance
[41] ShiqinY,JianjunJ,GuangxingY.Adolphinpartneroptimization.In:Intelligent enhancement using Particle Swarm Optimization in Oblique Ring-Shape-
systems,2009.GCIS’09.WRIGlobalCongresson;2009.p.124–28. Hole Photonic Crystal Waveguide. In: Photonics global conference (PGC);
[42] YangX-S.Fireflyalgorithm,stochastictestfunctionsanddesignoptimisation. 2012.p.1–4[2012].
IntJBio-InspiredComput2010;2:78–84. [78] Mirjalili SM, Abedi K, Mirjalili S. Optical buffer performance enhancement
[43] Askarzadeh A, Rezazadeh A. A new heuristic optimization algorithm for using Particle Swarm Optimization in Ring-Shape-Hole Photonic Crystal
modelingofprotonexchangemembranefuelcell:birdmatingoptimizer.IntJ Waveguide.Optik–IntJLightElectOptics2013;124:5989–93.
EnergyRes2012. [79] Mirjalili SM, Mirjalili S, Lewis A. A novel multi-objective optimization
[44] GandomiAH,AlaviAH.KrillHerd:anewbio-inspiredoptimizationalgorithm. framework for designing photonic crystal waveguides. Photonics Technol
CommunNonlinearSciNumerSimul2012. LettIEEE2014;26:146–9.
[45] PanW-T.Anewfruitflyoptimizationalgorithm:takingthefinancialdistress [80] Mirjalili SM, Mirjalili S, Lewis A, Abedi K. A tri-objective particle swarm
modelasanexample.Knowl-BasedSyst2012;26:69–74. optimizerfordesigninglinedefectphotoniccrystalwaveguides.Photonicsand
[46] MechLD.Alphastatus,dominance,anddivisionoflaborinwolfpacks.CanJ Nanostructures–FundamentalsandApplications.
Zool1999;77:1196–203. [81] WuJ,LiY,PengC,WangZ.Widebandandlowdispersionslowlightinslotted
[47] MuroC,EscobedoR,SpectorL,CoppingerR.Wolf-pack(Canislupus)hunting photoniccrystalwaveguide.OpticsCommun2010;283:2815–9.
strategies emerge from simple rules in computational simulations. Behav [82] MirjaliliS,MirjaliliSM,YangX.Binarybatalgorithm.NeuralComputAppl,in
Process2011;88:192–7. press,DOI:10.1007/s00521-013-1525-5.