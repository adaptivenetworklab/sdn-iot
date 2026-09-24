# Paper SDN Cloud MSNw

> Source file: `Paper SDN Cloud MSNw.pdf`

---

Machine Translated by Google
14Tanggal publikasi x xxx 00,0000, tanggal versi s aat ini xxxx 0 0,0000.
Pengenal Objek D igital 10.1109/ACCESS.2022.Nomor Doi
MSNws: P engontrol SDN Berbasis L ayanan M ikro
menggunakan Protokol WebSocket untuk Menstabilkan Jaringan
Penggunaan dan K inerja d alam P engirisan M ulti-Penyewa
Mochamad R afli Hadiana, Muhammad L itfan R ahmansyah, S yekh Maulana Wijaya, S alman A lfarizi N B, Ridha
Muldina N egara dan Sofia Naning H ertiana
Jurusan Teknik E lektro, T elkom University, 4 0257 Indonesia
Penulis k oresponden: Mochamad Rafli H adiana ( email: r aflihadiana@student.telkomuniversity.ac.id).
Pekerjaan ini sebagian d idukung oleh infrastruktur penelitian Adaptive Network L aboratory yang d idanai o leh T elkom U niversity.
ABSTRAK D engan s emakin m araknya teknologi c loud, s eperti o rkestrasi container p ada j aringan seluler generasi k elima (5G),
diperlukan f leksibilitas y ang l ebih besar d alam proses m anajemen j aringan menuju j aringan backend yang kompleks. S oftware
Define N etworking ( SDN) adalah t eknologi l ain yang b anyak d igunakan y ang memungkinkan kontrol jaringan lebih d inamis t erhadap
fungsi j aringan v irtual (VNF), t erutama d alam s kenario jaringan s eluler. M enilai a rsitektur dan protokol k omunikasi yang mengontrol
fungsi s witch s angat p enting untuk mengoptimalkan k inerja jaringan. Karya i ni m enyajikan Microservices-Based SDN C ontroller
WebSocket P rotocol (MSNws), sebuah SDN Controller yang m engimplementasikan a rsitektur modern, y ang berfokus p ada i ntegrasi
ke WebSocket s ebagai p rotokol komunikasi utama dan menerapkan m iddleware yang menyediakan kontrol aliran d an r ute.
Pengontrol yang diusulkan menggunakan t eknologi sumber t erbuka u ntuk memberikan a lternatif b erbiaya rendah s ambil menekankan
fungsionalitas, m anajemen, dan o rkestrasi cloud. Makalah ini m enjelaskan k emampuan pengontrol yang diusulkan u ntuk
menstabilkan k inerja jaringan dalam s kenario implementasi p emotongan jaringan d an k euntungannya d alam mengurangi
pemanfaatan s umber daya komputasi.
ISTILAH I NDEKS Software Defined N etworking ( SDN), K ontainerisasi, Konsumsi C PU, Layanan Mikro
Pengontrol, Pemotongan J aringan.
I. P ENDAHULUAN diimplementasikan sebagai satu kesatuan m onolitik. Bahkan j ika
Pada jaringan s eluler generasi k elima ( 5G), Software-Defined N etwork digunakan s ebagai sistem p engontrol terdistribusi, beberapa subfungsi
(SDN) merupakan s alah satu faktor p enting d alam pengelolaan j aringan belum tentu d igunakan u ntuk mengontrol j aringan [ 5]. Masalah u tama
terpusat. S DN a dalah p aradigma jaringan y ang m emecah i nfrastruktur dengan a rsitektur perangkat l unak monolitik adalah k ebutuhan u ntuk
jaringan t radisional d engan m emisahkan fungsi j aringan d ari r outer dan memberikan l ebih banyak f leksibilitas kepada a dministrator j aringan u ntuk
switch y ang mendasari lalu lintas [ 1]–[3]. Ini membuat p eralihan jaringan memilih k omponen a tau f ungsi t ertentu u ntuk mengimplementasikan
lebih mudah untuk d iteruskan, d an f ungsi k ontrol m enentukan k ebijakan kebutuhan k husus mereka u ntuk skenario y ang berbeda [6].
dan konfigurasi jaringan. F ungsi k ontrol l ainnya a dalah a gen pusat untuk Namun, d engan b angkitnya arsitektur modern d alam rekayasa
mengimplementasikan persyaratan jaringan aplikasi d an m elakukan perangkat l unak, pengontrol SDN d apat didekomposisi dan
beberapa f ungsi d ari aplikasi perangkat lunak, s eperti a nalisis d an diimplementasikan menjadi k omponen mikro yang terdiri dari sub-fungsi
pengukuran Quality o f Service ( QoS), routing lanjutan, d an k ontrol lalu logis d an m asih berbagi layanan jaringan beban yang sama, s ehingga
lintas [4]. Dalam k ebanyakan kasus, i a berkomunikasi dengan p erangkat menciptakan sistem y ang tangguh t erhadap kegagalan [ 5]. Arsitektur
penerus y ang bertanggung j awab untuk meneruskan dan m emanipulasi layanan mikro merupakan b agian p enting d ari strategi untuk membuat
paket m enggunakan OpenFlow s ebagai p rotokol komunikasi jaringan [ 3]. pengontrol arsitektur tradisional m enyediakan penerapan yang lebih
fleksibel. T eknologi container s eperti Docker d an Kubernetes dirancang
untuk menyediakan p latform i solasi terstandar yang membantu
pengembangan a plikasi d engan m enyederhanakan
Fleksibilitas y ang d itujukan o leh fungsi k ontrol t erpusat s aat ini m asih dan m empercepat p roses penerapan [ 7]–[9]. Keuntungan u tama d ari
menimbulkan t oleransi k esalahan, kendala l atensi, d an m asalah layanan mikro adalah m enangani operasional
penyeimbangan b eban karena p engontrol yang a da t idak b erfungsi.
JILID XX, 2 017 1

Machine Translated by Google
tantangan i nfrastruktur d engan membatasi d an m enyepakati b agaimana menekankan tujuan d an p enerapan p raktisnya u ntuk m emberikan konteks
komponen p erangkat lunak d iterapkan d alam c ontainer. Ini m emfasilitasi pada p engujian M SNws. B agian III m enguraikan s truktur logis d an atribut
pemeliharaan d an k eandalan s istem perangkat lunak y ang dikelola o leh utama MSNws. B agian IV m enjelaskan d ua k asus penggunaan yang
orkestrator. dieksplorasi d i m ana t eknik pemotongan j aringan d iterapkan, d an
Oleh karena itu, beberapa s tudi p enelitian telah dimulai untuk pengujian s tres dilakukan menggunakan t estbed, beserta h asil y ang
mengimplementasikan pengontrol SDN untuk l ayanan mikro. ONOS diperoleh. T erakhir, Bagian V menjelaskan l angkah s elanjutnya d ari
menggunakan a rsitektur b erbasis l ayanan mikro y ang dirancang u ntuk terbitan t erbuka d an m enyimpulkan makalah.
skenario pusat data cloud dan menggunakan P anggilan P rosedur Jarak
Jauh Google ( gRPC) s ebagai komunikasi antar-fungsi, namun m asih II. PEKERJAAN T ERKAIT: KONTROLER LAYANAN M IKRO
terbatas p ada kurangnya implementasi dalam k epatuhan 5 G k arena Implementasi pengontrol S DN b erbasis layanan m ikro difokuskan p ada
masih d alam tahap awal. produk dan m embutuhkan l ebih b anyak penguraian v ersi m onolitiknya agar d apat diterapkan dalam arsitektur
pekerjaan untuk menyediakan kerangka b ermain [5], [10]. S elain itu, studi layanan m ikro. D emikian penelitian ini
penelitian l ain yang d isebut Microservice S DN-controller (MSN) mengacu p ada s tudi yang ada t entang d ekomposisi p engontrol SDN
menggabungkan Pengontrol R yu SDN d an R EST API s ebagai p rotokol sebagai panduan u ntuk m erancang t estbed k ami d engan t rade-off minimal
komunikasi u tama yang dirancang k husus u ntuk p enerapan 5 G R AN dalam jaringan m ulti-penyewa. Kami telah menganalisis dua s tudi p enelitian
Edge g enerasi berikutnya. Namun, ini tidak m enunjukkan implementasi yang ada, ONOS dan R yu MSN, dan m enyimpulkan bahwa d ekomposisi
skenario jaringan m ulti-penyewa d an e valuasi k inerja pengontrol [ 5], [11]. Ryu MSN l ebih fleksibel d an dapat diterapkan di p engujian k ami.
Di masa d epan, s alah satu f itur yang diantisipasi dari aplikasi 5 G a dalah
network slicing, y ang berpotensi m enyediakan k onektivitas y ang ONOS adalah arsitektur ONOS generasi berikutnya, yang menganut
disesuaikan. K onektivitas y ang disesuaikan i ni terbukti s angat desain l ayanan m ikro. N amun pengontrol ini t erfokus p ada s kenario pusat
data cloud d an t idak memiliki fleksibilitas d alam mengubah p rotokol
menguntungkan b agi b erbagai industri, k arena m enawarkan pendekatan
yang l ebih c erdas dalam membagi j aringan u ntuk melayani layanan a tau komunikasi [18].
sektor b isnis t ertentu. Oleh k arena itu, p aradigma p emotongan j aringan Selanjutnya, p rotokol k omunikasi default ONOS
yang s esuai untuk memenuhi tujuan i ni mencakup m ulti-tenancy [12]–[15]. adalah gRPC, dan m enurut penelitian terbaru [5], p rotokol i ni m emiliki
Ini juga merupakan g agasan m ulti-tenancy latensi l ebih tinggi d ibandingkan W ebSocket. Penelitian i ni d imaksudkan
untuk m eminimalisir l atensi a ntar m icroservice a gar l ebih dekat d engan
memungkinkan b eberapa o perator j aringan v irtual untuk berbagi pengontrol SDN m onolitik yang tidak memiliki latensi k arena tidak a danya
komunikasi antar n ode d i d alam pengontrol S DN m onolitik itu sendiri.
infrastruktur fisik [ 16], [ 17].
Makalah ini m enjelaskan pengontrol SDN l ayanan m ikro y ang diusulkan Pada a khirnya MSN d igunakan sebagai r eferensi utama, upaya y ang a da
dengan p rotokol k omunikasi W ebSocket dalam menguraikan p engontrol Ryu SDN m enjadi arsitektur b erbasis
diimplementasikan d alam skenario jaringan multi-penyewa. Kontainer- layanan m ikro dengan m emisahkan l ogika aplikasi SDN d ari komponen
orchestrator membuat penerapan a plikasi u ntuk membuat j aringan yang dasar R yu.
saling t erhubung ke s witch O penFlow t ervirtualisasi, pengontrol S DN, dan
Itu ada d i n ode m iddleware u ntuk m engkonversi f ormat dari acara
pengontrol proksi. Testbed d ibangun dengan perangkat lunak s umber
terbuka dan VNF untuk memfasilitasi penerapan d an interoperabilitas OpenFlow ke JSON d an, juga, karena k etidakmampuan l ogika a plikasi
proses penelitian. untuk m emproses o bjek t erkait.
Makalah i ni m enyajikan d ua kasus penggunaan, satu untuk p emotongan multi-penyewa Sedangkan komponen h anya b ertanggung jawab m enyediakan logika
dan s atu lagi untuk pengujian p emanfaatan s umber d aya. Kode sumber jaringan. Melalui p emanfaatan t eknik d ekomposisi ini, komponen logika
disediakan untuk memungkinkan r eplikasi k edua e ksperimen ini. aplikasi dapat didistribusikan s ekaligus m enghindari duplikasi komponen
Kontribusi makalah ini a dalah sebagai berikut: dasar, yaitu middleware [5], [ 19], [20].
(cid:127) Mengusulkan m odifikasi p rotokol WebSocket u ntuk arsitektur
pengontrol SDN b erbasis layanan m ikro untuk m engelola
testbed. Kami telah merancang t estbed k ami d engan m etode d ekomposisi
(cid:127) Makalah ini m engevaluasi b erbagai a rsitektur p engontrol S DN y ang penelitian MSN s ebelumnya. N amun, MSNws, y ang merupakan p engontrol
sesuai u ntuk memberikan k inerja jaringan d an pemanfaatan yang diusulkan, m enggunakan W ebSocket s ebagai protokol k omunikasi
sumber daya y ang lebih s tabil kepada o perator s esuai d engan untuk m eminimalkan latensi, menyederhanakan basis kode logika, d an
meningkatnya jumlah ukuran lalu l intas latar b elakang. menyediakan kode sumber kepada p ublik untuk p engembangan d i m asa
mendatang1 . Selain itu, p enelitian ini m enganalisis i mplementasi
(cid:127) Eksperimen d apat direproduksi, m engingat k ode untuk m enerapkan pengontrol M SNws p ada j aringan m ulti-tenant d engan s kenario network
testbed dan d ua aplikasi kasus p enggunaan tersedia u ntuk slicing. Selain itu, k ami m erancang l ogika jaringan u ntuk m engkonfigurasi
umum. topologi p ohon l emak
Makalah ini d isusun sebagai berikut. Bagian I I m enjelaskan pengontrol sebagai uji k asus implementasi.
layanan m ikro dalam akademi penelitian terbaru,
1https://github.com/adaptivenetworklab/cloud-sdn
8 JILID XX, 2017

Machine Translated by Google
| AKU  AKU A  KU. M  | SNWS:  KONTROLER  SDN W  | EBSOCKET |                                                   |     |                    |             |
| ------------------ | ------------------------ | -------- | ------------------------------------------------- | --- | ------------------ | ----------- |
|                    |                          |          | Untuk  lebih  presisi,  arahkan  perhatian  ke G  |     | ambar  2, y ang m  | emberikan   |
Pengontrol S DN m  odifikasi  yang b aru d iusulkan  menggunakan  Ryu   ilustrasi  detail  tentang d inamika  komunikasi  antara  layanan m  ikro d an
sebagai k erangka  utama. A rsitektur y ang d iusulkan d idasarkan  pada
bidang d ata.
| layanan m  ikro,  seperti  yang  ditunjukkan  pada G  |     | ambar  1.  Dalam  arsitektur   |     |     |     |     |
| ----------------------------------------------------- | --- | ------------------------------ | --- | --- | --- | --- |
ini, s emua k omponen d an  aplikasi  Ryu d idekomposisi s ebagai l ayanan
mikro  daripada  digabungkan d alam  fungsi  lingkungan m  onolit. P enelitian
| ini m  emanfaatkan M   | ininet  SDN  dengan s pesifikasi  yang s esuai  untuk   |     |     |     |     |     |
| ---------------------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
| mengelola  jaringan m  | ulti-tenant y ang k ompleks.                            |     |     |     |     |     |
Integrasi d engan P engontrol  Ryu S DN, b erdasarkan l ayanan  mikro,
| memungkinkan p engembangan s istem  kontrol m  |     | ulti-penyewa  secara   |     |     |     |     |
| ---------------------------------------------- | --- | ---------------------- | --- | --- | --- | --- |
efektif. T ujuannya  adalah  mengelola s umber  daya u ntuk  meningkatkan
kinerja d an s kalabilitas j aringan s ecara e fisien.  Keuntungan M  ininet  adalah
| fleksibilitas  bandwidthnya, y ang m  |     | emungkinkan p enyesuaian  dinamis   |     |     |     |     |
| ------------------------------------- | --- | ----------------------------------- | --- | --- | --- | --- |
berdasarkan p enggunaan. P endekatan  ini  memungkinkan e ksplorasi
tentang b agaimana  pengontrol S DN b erbasis  layanan  mikro b eradaptasi
terhadap p erubahan  dinamika  jaringan,  sehingga  meningkatkan
kemampuan  manajemen  sumber d aya.
GAMBAR  2. A lur  komunikasi  pengontrol l ayanan  mikro k ami.
A. D  ESAIN  KONTROLER  LAYANAN  MIKRO
Pekerjaan k ami m  emanfaatkan k erangka p engontrol R  yu S DN, y ang   Prosesnya  dimulai  dengan  bidang d ata y ang m  entransmisikan
secara  tradisional d ianggap  monolitik, s ebagai  elemen  dasar u ntuk   OpenFlow P acket-In ( opf_packetin)  ke m  iddleware  menggunakan  protokol
pengontrol l ayanan  mikro k ami. K omponen i ni, d isebut O  penFlow   OpenFlow.  Setelah b erada  di  dalam m  iddleware,  opf_packetin  mengalami
Controller  WebSocket ( ofctl_ws), b erada  di d alam l apisan  middleware.   transformasi  menjadi  format J SON, y ang d inotasikan  sebagai
Selain i tu,  kami t elah  memperkenalkan k emampuan b aru y ang b erasal   json_packetin. S elanjutnya, m  iddleware  menggunakan  protokol W  ebSocket
dari p engontrol  monolitik i ni,  yang b ertanggung j awab  untuk m  engelola   untuk m  eneruskan  json_packetin k e l ogika  aplikasi.  Json_packetin y ang
logika  jaringan d an  mengonfigurasi j aringan M  ininet k ami. K ami  dengan   diterima d iproses  dengan c ermat d alam  komponen l ogika  aplikasi,
tepat  menamakan k emampuan i ni  sebagai  logika  aplikasi.  Logika  aplikasi   menerapkan  algoritma t opologi u ntuk  menghasilkan j son_packetout.
ditempatkan  di  layanan  terpisah y ang b erbeda d ari  komponen p engontrol   Json_packetout  yang d ihasilkan  ini  kemudian  diteruskan  kembali k e
Ryu  SDN  dasar.  Pilihan a rsitektur  ini  memastikan p emisahan  tanggung   middleware m  elalui  protokol W  ebSocket. S etelah m  asuk k embali k e
jawab  yang  jelas d an  meningkatkan  modularitas  sistem  kami. middleware,  json_packetout d ikembalikan k e b entuk a slinya  sebagai
|     |     |     | OpenFlow P acket-Out  (opf_packetout). T erakhir, m  |                   | iddleware k embali              |     |
| --- | --- | --- | ---------------------------------------------------- | ----------------- | ------------------------------- | --- |
|     |     |     | menggunakan  protokol O                              | penFlow  untuk m  | engirimkan o pf_packetout k e   |     |
bidang d ata,  mengakhiri  siklus  pertukaran d ata.
Untuk  memfasilitasi  komunikasi a ntara  komponen  dasar  dan l ogika
aplikasi,  yang b erada  di  layanan t erpisah,  kami  membuat k oneksi  melalui
Antarmuka  Pemrograman A plikasi ( API). S eperti y ang d isorot  dalam
makalah [ 5], p rotokol k omunikasi d engan l atensi t erendah  untuk k asus
|     |     |     | VNF  adalah W  ebSocket, i tulah  pilihan  kami.  Di j aringan m  |     |                         | ulti-penyewa,   |
| --- | --- | --- | ----------------------------------------------------------------- | --- | ----------------------- | --------------- |
|     |     |     | tempat k ami  mengelola  bidang d ata,  kami m                    |     | enggunakan F lowvisor   |                 |
GAMBAR  1. A rsitektur p engontrol y ang  diusulkan.
sebagai p engontrol  proksi  untuk  memfasilitasi  pemotongan  jaringan.  Ini
adalah k omponen  virtualisasi  jaringan y ang p enting, d iposisikan s ecara
Komponen  dasar  beroperasi s ebagai  antarmuka O  penFlow,  mengelola
|     |     |     | strategis a ntara p engontrol  SDN  utama d an b idang d ata.  Ia m  |     |     | emanipulasi   |
| --- | --- | --- | -------------------------------------------------------------------- | --- | --- | ------------- |
penerimaan d an  transmisi k ejadian  OpenFlow  ke d an d ari b idang  data.
paket O  penFlow,  membangun  jaringan v irtual t erisolasi d alam i nfrastruktur
| Sebaliknya, l ogika a plikasi m  | endefinisikan l ogika  konfigurasi  untuk   |                             |                                                                               |     |     |           |
| -------------------------------- | ------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------- | --- | --- | --------- |
|                                  |                                             |                             | bidang d ata y ang l ebih  luas.  Masing-masing j aringan  terisolasi i ni m  |     |     | ewakili   |
| jaringan M  ininet  kami. H      | asilnya, k ami m                            | emisahkan f ungsionalitas   |                                                                               |     |     |           |
potongan  jaringan i ndividual,  yang d ioptimalkan  secara  cermat u ntuk
| OpenFlow  dari  logika p emrosesan, m  |     | engalihkan b eban p emrosesan l ogis   |     |     |     |     |
| -------------------------------------- | --- | -------------------------------------- | --- | --- | --- | --- |
melayani  layanan t ertentu.  Akibatnya, s etiap p eristiwa P acket-Out a tau
ke l ayanan y ang  berbeda.  Pemisahan  strategis  ini  menghilangkan
|     |     |     | FlowMod  yang d itujukan  untuk  bidang d ata m  |     | enjalani p emrosesan  awal   |     |
| --- | --- | --- | ------------------------------------------------ | --- | ---------------------------- | --- |
kebutuhan  pemrosesan s emua t ugas  dalam  Ryu B ase  Controller, y ang
|                                 |            |     | oleh  Flowvisor. L angkah  ini  mencakup  pemfilteran u ntuk m   |     |     | encegah     |
| ------------------------------- | ---------- | --- | ---------------------------------------------------------------- | --- | --- | ----------- |
| terletak d i d alam  lapisan m  | iddleware. |     |                                                                  |     |     |             |
|                                 |            |     | komunikasi  yang t idak  diinginkan  antar i risan  jaringan, m  |     |     | emastikan   |
integritas d an i solasi  operasi s etiap i risan  [21].
| Desain  seperti  itu  menumbuhkan m  |     | odularitas d an m  eningkatkan e fisiensi   |     |     |     |     |
| ------------------------------------ | --- | ------------------------------------------- | --- | --- | --- | --- |
arsitektur s istem k ami.
| 8   |     |     |     |     |     | JILID  XX,  2017 |
| --- | --- | --- | --- | --- | --- | ---------------- |

Machine Translated by Google
| B.ORKESTRASI V  | NF  |     |                      |                               |     |               |               |
| --------------- | --- | --- | -------------------- | ----------------------------- | --- | ------------- | ------------- |
|                 |     |     | harus d itangani, m  | encakup t indakan s eperti m  |     | eneruskan, m  | enjatuhkan,   |
Kontainerisasi  adalah  teknologi  yang  menggabungkan  aplikasi,   atau  memodifikasi p aket. E vent  ini s angat  cocok u ntuk m  enerapkan
perpustakaan s istem, d an d ependensi t erkait k e d alam p enerapan
aturan p enerusan k e  beberapa p aket y ang  memiliki k arakteristik y ang
terisolasi y ang t erorganisir d an  dikemas  [22]. P enerapan  yang  dibangun   sama  [26].  Perilaku i ni m  emungkinkan s witch  untuk m  enyimpan t abel
dan d ijalankan  sebagai  container d apat d ieksekusi,  mudah  dimigrasi, d an   aliran  yang  akan  digunakan  untuk m  eneruskan  lalu  lintas  ketika p aket
dapat  diskalakan.  Hal  ini m  embantu m  eningkatnya p ermintaan a plikasi   yang  sama  dengan t ujuan y ang  sama  datang. P engontrol S DN m  odifikasi
atau  fungsi  yang  diminta, m  enambah j umlah k ontainer  untuk m  enangani   yang  baru  diusulkan  menggunakan R  yu  sebagai k erangka  utama.
| lalu  lintas a kan  cukup  untuk m  | enangani l alu  lintas. D  | alam  arsitektur   |                                                           |     |     |                       |     |
| ----------------------------------- | -------------------------- | ------------------ | --------------------------------------------------------- | --- | --- | --------------------- | --- |
|                                     |                            |                    | Arsitektur y ang  diusulkan  didasarkan  pada l ayanan m  |     |     | ikro  seperti y ang   |     |
Pengontrol  SDN m  odifikasi y ang  kami  usulkan,  kami m  enggunakan   ditunjukkan p ada G  ambar 1 . D  alam  arsitektur  ini,  semua k omponen  dan
Docker  untuk  teknologi c ontainerisasi  karena m  erupakan p engelola   aplikasi  Ryu  didekomposisi  sebagai  layanan m  ikro  daripada d igabungkan
container  yang  ringan,  sumber t erbuka, d an  mudah d itangani  [23]. dalam  fungsi  lingkungan m  onolit.
Dengan  spekulasi  mengenai j aringan  lingkungan y ang  luas y ang  akan
| menangani  banyak  container, k ami m                                  | emerlukan o rkestrator  container   |     |     |     |     |     |     |
| ---------------------------------------------------------------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
| untuk m  engelola  dan m  engatur p enerapan c ontainer  Docker  kami. |                                     |     |     |     |     |     |     |
Oleh  karena i tu,  kami a kan  menggunakan K ubernetes  sebagai c ontainer-
orchestrator  karena  beberapa h ak  istimewa  yang  diberikan, s eperti
kemudahan p enerapan p erangkat  lunak d an l ayanan, o tomatisasi
penerapan p erangkat l unak,  ketersediaan p rovisi p erangkat  lunak y ang
tinggi, d an  spesifikasi b atas  sumber d aya  [24].  Kubernetes  akan  membantu
pengelolaan  container  agar  mudah  terhubung  ke p engontrol p roxy
eksternal  atau d ata p lane  tanpa p erlu  memasukkan s umber I P A ddress
secara  manual s etiap k ali  deployment d ibuat. L alu  lintas  antar h ost
Kubernetes  akan d ikelola  oleh  salah s atu  Container  Network  Interface   GAMBAR  3.  Arsitektur m  onolit p engontrol R  yu.
| (CNI) y ang  didukung, F lannel.  Flanel t idak m  | engontrol  bagaimana   |     |     |     |     |     |     |
| -------------------------------------------------- | ---------------------- | --- | --- | --- | --- | --- | --- |
container  dihubungkan k e h ost [ 25], s ehingga s etiap  komunikasi  antar
|     |     |     | Arsitektur y ang  kami u sulkan m  |     | enerima  tantangan  dalam  menggunakan   |     |     |
| --- | --- | --- | ---------------------------------- | --- | ---------------------------------------- | --- | --- |
container  (pod)  akan  diteruskan  melalui  Flanel.  CNI i ni  juga a kan
|     |     |     | arsitektur l ayanan m  | ikro  baru u ntuk m  | enerapkan P engontrol S DN  yang   |     |     |
| --- | --- | --- | ---------------------- | -------------------- | ---------------------------------- | --- | --- |
membantu  menghubungkan  setiap  sub-fungsi P engontrol S DN d an
ada.  Pengontrol S DN y ang  ada b iasanya d iterapkan  sebagai  arsitektur
aplikasi V NF  yang  di-deploy,  karena  setiap p od  didistribusikan d i a ntara
monolitik, s ehingga  membatasi  fleksibilitas p enskalaannya  ketika  sub-
Cluster  Kubernetes  pada  host  yang  berbeda.
fungsi  yang  lebih  spesifik  dalam  pengontrol d iperlukan s eperti y ang
|     |     |     | ditunjukkan p ada G  | ambar.  2. K ami  menggunakan K erangka  Ryu  SDN   |     |     |     |
| --- | --- | --- | -------------------- | --------------------------------------------------- | --- | --- | --- |
karena  ini a dalah  salah s atu p engontrol y ang  Sesuai d engan 5 G d an
Di  SDN, p erangkat p enerus s eperti  switch a kan  memproses  paket
|     |     |     | dapat  dengan m  | udah  diterapkan  di D  | ocker C  | ontainers  [5]. S eperti y ang   |     |
| --- | --- | --- | ---------------- | ----------------------- | -------- | -------------------------------- | --- |
masuk  dan  meminta a liran  dari p engontrol  sehingga p aket  akan  diteruskan
|     |     |     | ditunjukkan p ada G  | ambar 1 , s etiap  sub-fungsi  di R  |     | yu  Controller  akan   |     |
| --- | --- | --- | -------------------- | ------------------------------------ | --- | ---------------------- | --- |
ke  rute  tertentu  yang  sudah d ikonfigurasi  di p engontrol. A da b eberapa
|     |     |     | dimasukkan  ke  dalam  container  dengan b antuan D  |     |     | ocker d an d iatur   |     |
| --- | --- | --- | ---------------------------------------------------- | --- | --- | -------------------- | --- |
tipe  kejadian  atau p esan O  penFlow u ntuk  komunikasi a ntara p engontrol   dengan K ubernetes.
SDN d an  perangkat  penerusan. T ipe  pertama,  dikenal s ebagai E vent
| Packet-In,  terjadi  ketika p erangkat p enerus m  | engirim  pesan P acket-In k e   |     |     |     |     |     |     |
| -------------------------------------------------- | ------------------------------- | --- | --- | --- | --- | --- | --- |
TABEL I
| pengontrol  SDN. |     |     |     | SPESIFIKASI  MESIN |     |     |     |
| ---------------- | --- | --- | --- | ------------------ | --- | --- | --- |
|                  |     |     |     | Node               | CPU | RAM |     |
Penyimpanan
Pesan i ni  dipicu k etika p erangkat  perlu  meneruskan  paket t etapi  tidak
memiliki i nformasi  yang  diperlukan  untuk  membuat  keputusan t ersebut.   Master  Kubernet 2 I nti 2 G  B 50  GB
Fungsi  utamanya  adalah u ntuk  meminta p anduan  dari p engontrol S DN   Pekerja  Kubernetes-1 2 I nti 2 G  B 30  GB
|     |     |     | Pekerja  Kubernetes-2 |     | 2 I nti | 2 G  B | 30  GB |
| --- | --- | --- | --------------------- | --- | ------- | ------ | ------ |
mengenai  tindakan y ang t epat u ntuk  mengambil p aket t ertentu  yang   4 I nti 4 G  B 30  GB
Monolit  Ryu
| dimaksud. |     |     | Pelindung  aliran |     | 2 I nti | 2 G  B | 20 G  B |
| --------- | --- | --- | ----------------- | --- | ------- | ------ | ------- |
|           |     |     | Mininet           |     | 2 I nti | 4 G  B | 20 G  B |
Sebaliknya,  pengontrol  SDN  memulai  Peristiwa P acket-Out,  yang
mengirimkan p esan P acket-Out u ntuk  menginstruksikan  perangkat
penerus  untuk  meneruskan p aket  tertentu  ke  port  tujuan y ang  ditentukan.   Hal i ni m  embuat P engontrol R  yu  lebih  fleksibel d an t erukur s eiring
dengan m  eningkatnya  permintaan l alu  lintas  yang  meminta  fungsi  dan
| Peristiwa i ni b iasanya  digunakan  ketika m        | enerapkan  aturan p enerusan   |                          |                              |                                                           |     |     |     |
| ---------------------------------------------------- | ------------------------------ | ------------------------ | ---------------------------- | --------------------------------------------------------- | --- | --- | --- |
|                                                      |                                |                          | rute  jaringan t ertentu. C  | luster d an l ingkungan t estbed,  seperti d itunjukkan   |     |     |     |
| ke  masing-masing p aket. T erakhir,  Event  Flow M  |                                | odification ( FlowMod)   |                              |                                                           |     |     |     |
pada G  ambar 3 , t erdiri d ari  3  VM u ntuk K ubernetes  Cluster d engan 1
| memiliki k emiripan  dengan E vent P acket-Out n amun m  |                       | emiliki  tujuan y ang   |                                          |     |                                      |     |     |
| -------------------------------------------------------- | --------------------- | ----------------------- | ---------------------------------------- | --- | ------------------------------------ | --- | --- |
|                                                          |                       |                         | Master d an  2  Worker,  1  VM u ntuk R  |     | yu  Monolith, 1   VM u ntuk P roxy   |     |     |
| berbeda. I ni d irancang u ntuk  menambah, m             | emodifikasi,  atau m  | enghapus                |                                          |     |                                      |     |     |
entri  aliran  dalam  tabel a liran p erangkat  penerusan. E ntri  aliran  ini   Controller  dalam  hal i ni k ita m  enggunakan F lowvisor,  dan t erakhir  1  VM
|     |     |     | lainnya  untuk M  | ininet.  Spesifikasi  masing-masing  node d apat  dilihat p ada   |     |     |     |
| --- | --- | --- | ----------------- | ----------------------------------------------------------------- | --- | --- | --- |
menentukan b agaimana  paket d engan  karakteristik  tertentu
Tabel 1 .
| 8   |     |     |     |     |     |     | JILID  XX,  2017 |
| --- | --- | --- | --- | --- | --- | --- | ---------------- |

Machine Translated by Google
IV. S KENARIO KASUS PENGGUNAAN MSNWS penelusuran web, dialokasikan bandwidth 1Mbps, mulai dari H5 hingga
Pengontrol y ang diusulkan d iterapkan p ada s kenario y ang berbeda. H8. T erakhir, irisan kanan, yang melayani V oIP, m emiliki b andwidth
Subbagian berikut menyediakan dua k asus p enggunaan pemotongan 500Kbps, m encakup jalur pemotongan dari H9 ke H12. Skema a lokasi
jaringan d an p emanfaatan sumber d aya. Kami a kan membandingkan bandwidth y ang cermat dan j alur pemotongan y ang dirancang d engan
kinerja MSNws d an R yu M onolith. cermat i ni m emastikan pengoperasian berbagai l ayanan y ang harmonis
dalam jaringan m ulti-penyewa.
GAMBAR 4. Arsitektur t estbed MSNws.
Penerapannya akan dimasukkan k e d alam c ontainer d engan Docker GAMBAR 6 . A turan a liran topologi Fat Tree.
dan d iatur dengan K ubernetes, seperti y ang ditunjukkan p ada G ambar 4
dan d inyatakan d alam subbagian sebelumnya. K omponen m iddleware Untuk membuat i risan jaringan y ang terisolasi, k ami m enggunakan
akan dihubungkan k e p engontrol p roxy e ksternal yaitu F lowvisor. Flowvisor, yang dapat membuat r uang aliran u ntuk m enentukan a turan
Sedangkan u ntuk arsitektur t estbed R yu Monolith t idak m enggunakan aliran s etiap irisan [27]. Seperti yang ditunjukkan p ada G ambar 6 , s etiap
middleware d i R yu M onolith untuk terhubung k e Flowvisor, k arena saklar p ada m asing-masing irisan terhubung k e saklar m asing-masing
penerapan a plikasi Ryu a kan m enggunakan r untime handler R yu pada i risannya sendiri dan k e saklar m ilik irisan lainnya. K ami juga
OpenFlow d efault u ntuk menangani lalu l intas masuk yang dikirim dari membuat t autan k ompleks d alam topologi ini u ntuk m enguji kredibilitas
Flowvisor. Flowvisor dalam mengisolasi j aringan d engan r uang alirannya
konfigurasi. M isalnya, s aklar a tas p ertama di i risan kiri akan dikonfigurasi
sedemikian r upa sehingga lalu lintas pada i risan yang ditentukan hanya
dapat mengalir melalui p ort 1 dan 2 dari antarmuka saklar t etapi t idak
dapat mengalir melalui p ort 3, 4 , 5 , d an 6 karena port tersebut mengarah
ke irisan yang berbeda. C ontoh lainnya adalah saklar k iri bawah p ada
irisan kanan d engan k onfigurasi ruang aliran y ang ditentukan sehingga
aliran hanya d apat melewati port 2 dan 3 , n amun tidak melalui p ort s atu
karena a ntarmuka ini m engarah k e irisan tengah. B egitu s eterusnya,
dengan s witch lain yang terhubung k e port antarmuka.
Skenario p engujian a kan dikelola dengan M ininet dan d iotomatisasi
dengan s krip B ash. Skrip Bash i ni a kan menjalankan s etiap layanan
streaming video, penelusuran w eb, VoIP, d an b erbagai u kuran l alu lintas
GAMBAR 5. Skenario p engujian F at T ree.
latar b elakang secara b ersamaan. Lalu l intas latar b elakang dihasilkan
menggunakan I perf, d engan u kurannya yang meningkat s ecara b ertahap.
Gambar 5 menunjukkan t opologi Fat Tree yang digunakan d i S DN u ntuk
Kami menggunakan l ayanan s treaming yang dibangun di V LC M edia
skenario ini, di m ana b erbagai layanan dibagi m enjadi beberapa b agian
Player, j adi s atu h ost a kan bertindak s ebagai server, d an h ost l ainnya
yang disebut i risan, masing-masing d ialokasikan dengan bandwidth y ang
akan mengalirkan video d ari host s erver. S elanjutnya, k ami m enggunakan
disesuaikan. T erdiri dari 15 s witch d an 1 2 host yang terhubung d alam
situs w eb s ederhana b erdasarkan P ython untuk l ayanan w eb, dan u ntuk
pola yang mencerminkan jaringan m ulti-tenant. S etiap i risan akan
VoIP, k ami m enggunakan D ITG untuk m enghasilkan l alu lintas. Kami j uga
terhubung ke F lowvisor, d an juga akan terhubung k e M SNws d an Ryu
membuat k onfigurasi khusus tambahan d i P engontrol R yu, t erlepas d ari
Monolith s ecara bergantian saat setiap arsitektur d iuji, seperti yang
MSNws a tau Monolith, a gar s etiap layanan m emiliki jalur aliran khusus
ditunjukkan p ada Gambar 4.
yang berbeda d ari lalu lintas latar b elakangnya. S eperti yang ditunjukkan
pada G ambar 6 , k ami m endefinisikan panah h itam sebagai jalur panjang
A. PENGiris J ARINGAN
dan p anah m erah sebagai j alur pendek. Lalu l intas setiap layanan utama,
Kami menerapkan skenario p emotongan jaringan y ang terdiri d ari t iga
seperti s treaming video, penelusuran web, dan V oIP pada s etiap irisan,
irisan seperti yang d itunjukkan p ada G ambar 5 y aitu irisan kiri, d ikhususkan
akan mengalir melalui j alur pendek u ntuk l alu lintasnya. Lalu l intas latar
untuk v ideo streaming dialokasikan bandwidth 3Mbps, dengan jalur
belakang akan menggunakan j alur panjang.
pemotongan d ari H1 hingga H4. B egitu p ula dengan irisan tengahnya, sajikan
8 JILID XX, 2017

Machine Translated by Google
Lebih l anjut, a nalisis G  ambar  8 m  engungkapkan  beberapa  aspek
|     |     |     | menarik  mengenai k inerja M  | SNws  dengan  arsitektur l ayanan m  | ikro   |
| --- | --- | --- | ----------------------------- | ------------------------------------ | ------ |
dibandingkan  dengan p engontrol  monolitik d alam  konteks l ayanan  web.
Pertama, t erdapat  perbedaan l atensi y ang s ignifikan, d i  mana  MSNw
memiliki l atensi l ebih  tinggi  dibandingkan  pengontrol  monolitik. H  al  ini
|     |     |     | menunjukkan  bahwa p engontrol  monolitik m  | ungkin m  emiliki k euntungan               |     |
| --- | --- | --- | -------------------------------------------- | ------------------------------------------- | --- |
|     |     |     | dalam  situasi i ni  dalam  hal w            | aktu  respons.  Namun,  meskipun  latensi   |     |
MSNws  lebih  tinggi, k inerjanya t etap  stabil,  yang d apat d ianggap s ebagai
aspek p ositif  dari p engalaman p engguna.
Kedua, t hroughput M  SNws  menunjukkan  tingkat  stabilitas  yang  lebih
baik d ibandingkan  pengontrol  monolitik. A rtinya  meskipun  latensinya  lebih
|     |     |     | tinggi, M  SNws  mampu  menjaga  konsistensi d alam  pengiriman d ata a tau   |     |     |
| --- | --- | --- | ----------------------------------------------------------------------------- | --- | --- |
layanan, y ang d apat m  enjadi  faktor  penting d alam  penjelajahan  web  yang
memerlukan  pengiriman d ata y ang k onsisten. P ada  skala l alu l intas  latar
GAMBAR  7. H  asil  QoS  video s treaming. belakang  50-55 M  B,  keduanya  tampak m  emiliki k inerja s erupa,  yang
mungkin d isebabkan o leh t ingginya  lalu l intas l atar b elakang  yang  berjalan
|                                         |                                  |     | dan p engaruh y ang s ama p ada  kedua  pengontrol. D  | alam  konteks i ni,   |     |
| --------------------------------------- | -------------------------------- | --- | ------------------------------------------------------ | --------------------- | --- |
| Gambar 7   menunjukkan b ahwa  MSNws m  | emiliki  kinerja  latensi d an   |     |                                                        |                       |     |
penting j uga  untuk m  empertimbangkan  kebutuhan  dan p referensi  spesifik
throughput y ang  lebih s tabil.  Stabilitas p ada g rafik t ersebut b erarti
jaringan d an l ayanan d alam  memilih  pengontrol  yang p aling t epat.  Jadi,
perubahan n ilai d alam  perubahan  periodik p ada k ondisi  yang b erbeda
meskipun M  SNws  memiliki l atensi y ang l ebih  tinggi, p erformanya  tetap
| [28].  Hal i ni s angat  penting  dalam  layanan  streaming v ideo, d i m  |     |     | ana   |     |     |
| -------------------------------------------------------------------------- | --- | --- | ----- | --- | --- |
stabil,  sementara  pengontrol  monolitik m  ungkin m  emiliki k eunggulan
pengguna m  enginginkan  pengalaman y ang l ancar  dan t anpa  kerumitan.
dalam  waktu  respons.
Dengan  latensi y ang  stabil, p engguna d apat  menikmati s treaming v ideo
| tanpa  gangguan b uffering y ang  mengganggu. D                |                                                 | emikian p ula, t hroughput   |                 |     |     |
| -------------------------------------------------------------- | ----------------------------------------------- | ---------------------------- | --------------- | --- | --- |
| yang t inggi  menunjukkan k emampuan M                         | SNws u ntuk m                                   | engirimkan d ata             |                 |     |     |
| video  secara e fisien, s ehingga m                            | emastikan v ideo  dapat d iputar d engan  baik. |                              |                 |     |     |
| Kemudian, t erdapat p erbedaan  yang s ignifikan  setelah m    |                                                 | eningkatkan                  |                 |     |     |
| lalu  lintas  latar  belakang m                                | enjadi  25 M  B  dan k emudian  hingga 6 0 M    |                              | B,              |     |     |
| seperti y ang  ditunjukkan  pada G                             | ambar  7.  MSNws m                              | asih  berkinerja l ebih      |                 |     |     |
| konsisten  dibandingkan M                                      | onolitik  Ryu.  Hal  ini  menunjukkan  bahwa    |                              |                 |     |     |
| meskipun t erjadi  peningkatan b eban t rafik, M               | SNws m                                          | asih d apat  menjaga         |                 |     |     |
| kestabilan k inerjanya.  Sebaliknya, p engontrol m             |                                                 | onolitik  Ryu m              | ungkin  lebih   |     |     |
| rentan t erhadap f luktuasi l alu  lintas l atar b elakang. D  |                                                 | alam  konteks i ni,          |                 |     |     |
MSNws  dapat  dianggap  sebagai  solusi  yang l ebih a ndal d alam
menyediakan l ayanan  streaming  video  berkualitas k epada p engguna,
terutama k etika t erjadi  lonjakan l alu  lintas  yang t idak t erduga.
GAMBAR  9.  Hasil Q  oS  VoIP.
Pada  Gambar  9, M  onolitik R  yu  menunjukkan  kinerja y ang l ebih  baik
dan l ebih  stabil d alam  hal l atensi  dan t hroughput d ibandingkan  dengan
|     |     |     | MSNws. A nalisis P ertama: M  | onolitik R  yu  memiliki k eunggulan  yang c ukup   |     |
| --- | --- | --- | ----------------------------- | --------------------------------------------------- | --- |
signifikan d alam  hal l atensi. H  al  ini  menunjukkan  bahwa  pengontrol
|     |     |     | monolitik d apat m  | erespons p ermintaan  dengan l ebih  cepat,  yang m  | ana   |
| --- | --- | --- | ------------------- | ---------------------------------------------------- | ----- |
hal i ni  sangat p enting d alam  layanan y ang m  emerlukan w  aktu  respons
rendah, s eperti  VoIP a tau l ayanan k omunikasi  real-time  lainnya. M  eski
perbedaannya  sedikit,  namun k estabilan l atensinya  cukup b aik.  Kemudian,
untuk a nalisis k edua, t hroughput  Monolitik R  yu  menunjukkan  kinerja  yang
stabil.  Meskipun  tidak  sepenuhnya  dijelaskan  dalam  referensi  ilmiah
lainnya,  kinerja t hroughput y ang s tabil d apat m  enunjukkan  bahwa
GAMBAR  8. H  asil  QoS  penjelajahan  web.
|     |     |     | pengontrol  monolitik d apat m  | elakukannya |                  |
| --- | --- | --- | ------------------------------- | ----------- | ---------------- |
| 8   |     |     |                                 |             | JILID  XX,  2017 |

Machine Translated by Google
menjaga  konsistensi  dalam p enyampaian  data a tau l ayanan,  yang p enting   hubungannya d engan g rafik h asil Q  oS s ebelumnya  disarankan u ntuk
dalam k onteks  layanan a pa p un.  Oleh k arena i tu,  pengambilan k eputusan   evaluasi k omprehensif.
antara k edua  pengontrol  harus d idasarkan p ada  kebutuhan s pesifik
jaringan d an  layanan y ang  akan d igunakan, d engan  mempertimbangkan   B.  PENGGUNAAN  SUMBER D AYA
trade-off a ntara k inerja  dan  stabilitas  layanan. Pada  subbagian  ini,  kami m  enguji  penggunaan s umber d aya d ari
|     |     |     | MSNws  yang k ami u sulkan  dibandingkan  dengan  arsitektur m  |     |                                             | onolit.   |
| --- | --- | --- | --------------------------------------------------------------- | --- | ------------------------------------------- | --------- |
|     |     |     | Pengujian i ni  bertujuan  untuk m                              |     | elihat p enerapan a rsitektur P engontrol   |           |
SDN m  ana y ang l ebih u nggul  dalam  menangani s umber d aya s ecara l ebih
|     |     |     | efisien. U  ntuk  skenario  pengujian  ini,  kami m  |     | embandingkan p enggunaan   |     |
| --- | --- | --- | ---------------------------------------------------- | --- | -------------------------- | --- |
sumber d aya d ari V M  Kubernetes  Cluster  Worker d an V M  Ryu  Monolith
|     |     |     | karena  ini  lebih m  | erupakan  trade-off  yang  adil d ibandingkan  membandingkan   |     |     |
| --- | --- | --- | --------------------- | -------------------------------------------------------------- | --- | --- |
antara P od  Kubernetes  dan  sebuah I nstance.
|     |     |     | Karena K ubernetes  kami m  |     | enggunakan  teknologi k ontainerisasi   |     |
| --- | --- | --- | --------------------------- | --- | --------------------------------------- | --- |
Docker  dan s umber d aya  infrastruktur p engujian  kami t erbatas,  ada
beberapa  catatan u ntuk l ingkungan p engujian  ini.
|     |     |     | Pertama, c ontainer  Docker  berbagi s umber d aya  komputasi s eperti C  |     |     | PU   |
| --- | --- | --- | ------------------------------------------------------------------------- | --- | --- | ---- |
dan m  emori p ada  host, d an  setiap  container  yang b erjalan  secara
|     |     |     | bersamaan a kan  bersaing  untuk m                   |                                                | endapatkan s umber d aya b ersama t ersebut [ 29]. |     |
| --- | --- | --- | ---------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------- | --- |
|     |     |     | Oleh k arena  itu,  untuk m                          | eminimalkan  efek  perilaku  ini  yang a kan   |                                                    |     |
|     |     |     | menurunkan  kinerja c ontainer  kami [ 29], k ami m  |                                                | enetapkan  permintaan                              |     |
dan  batasan u ntuk s etiap  penerapan K ubernetes  aplikasi k ami a gar
|     |     |     | sumber d aya  terdistribusi  secara  merata. R  |     | asio  distribusi  penerapan   |     |
| --- | --- | --- | ----------------------------------------------- | --- | ----------------------------- | --- |
Kubernetes  aplikasi p ada  irisan k iri,  irisan  tengah,  dan i risan  kanan a dalah
2:1:1. K ami  juga  menghitung s isa  sumber d aya y ang  akan d igunakan  oleh
|     |     |     | host  sekitar 1 0% d ari  seluruh s umber d aya. K edua, k ami m  |                                                       |     | enggunakan   |
| --- | --- | --- | ----------------------------------------------------------------- | ----------------------------------------------------- | --- | ------------ |
|     |     |     | Prometheus  dan G                                                 | rafana s ebagai  alat p emantauan e ksternal u ntuk   |     |              |
infrastruktur k ami. A lat-alat i ni  diterapkan  di l uar  infrastruktur k ami  dan
akan m  embantu  memantau  secara  akurat p enggunaan s umber d aya  kami
|     |     |     | mengenai p enggunaan C  | PU d an p ersentase p enggunaan R  |     | AM  karena   |
| --- | --- | --- | ----------------------- | ---------------------------------- | --- | ------------ |
pengujian  kami a kan  ditekankan p ada  kemampuan  maksimalnya.  Terakhir,
|     |     |     | untuk s kenario  ini,  kami m  | enggunakan  topologi  yang s ama s eperti y ang   |     |     |
| --- | --- | --- | ------------------------------ | ------------------------------------------------- | --- | --- |
ditunjukkan  pada  Gambar 4 .
|     |     |     | Namun,  kami t idak m  | engimplementasikan  FlowMod d i P engontrol  Ryu   |     |     |
| --- | --- | --- | ---------------------- | -------------------------------------------------- | --- | --- |
SDN, s ehingga s akelar a kan s elalu  meminta  Aliran  dari p engontrol, t erus-
|                           |     |     | menerus  menekankan d an m                                            |     | enggunakan  sumber d ayanya p ada  setiap   |                    |
| ------------------------- | --- | --- | --------------------------------------------------------------------- | --- | ------------------------------------------- | ------------------ |
| GAMBAR  10.  Perbedaan Q  | oS  |     |                                                                       |     |                                             |                    |
|                           |     |     | lalu  lintas  masuk. K arena t ujuan  skenario  ini  adalah  untuk m  |     |                                             | elihat  seberapa   |
efisien p enggunaan s umber d aya  MSNws  kami d ibandingkan  dengan
Gambar 1 0 m  engilustrasikan  variasi  QoS  di s eluruh l ayanan  yang d iuji.
|     |     |     | Monolith  SDN C  | ontroller, k ami m  | elihat i ni  sebagai  alternatif  daripada l alu   |     |
| --- | --- | --- | ---------------- | ------------------- | -------------------------------------------------- | --- |
Variasi i ni m  enyoroti  perbedaan y ang  signifikan u ntuk s etiap s kenario  lalu
|                                                                                   |                                         |           | lintas  latar  belakang y ang l ebih l uas  yang j uga  akan m  |                                                                |     | enekankan  sumber   |
| --------------------------------------------------------------------------------- | --------------------------------------- | --------- | --------------------------------------------------------------- | -------------------------------------------------------------- | --- | ------------------- |
| lintas l atar b elakang. D  alam  legenda,  semakin b aik  menunjukkan k inerja   |                                         |           |                                                                 |                                                                |     |                     |
|                                                                                   |                                         |           | daya  di i nstance M                                            | ininet k ami.                                                  |     |                     |
| yang  unggul u ntuk  MSNws. G                                                     | rafik i ni  juga m  emberikan  bukti m  | engenai   |                                                                 |                                                                |     |                     |
|                                                                                   |                                         |           | Sebelum  kita m                                                 | enjalankan s kenario  ini, k ita p erlu  mengetahui  keadaan   |     |                     |
arsitektur  mana  yang  berkinerja l ebih b aik  ketika  menangani l ayanan
|     |     |     | awal m  esin  kita s aat  aplikasi d iterapkan. R  |     | ata-rata p enggunaan C  | PU  dan   |
| --- | --- | --- | -------------------------------------------------- | --- | ----------------------- | --------- |
tertentu d alam b erbagai  kondisi  lalu  lintas  latar b elakang.  Misalnya,  ketika
|                                          |                           |     | penggunaan R                   | AM  pada  VM  Kubernetes  Worker k ami m  |                                          | asing-masing   |
| ---------------------------------------- | ------------------------- | --- | ------------------------------ | ----------------------------------------- | ---------------------------------------- | -------------- |
| memeriksa  layanan V ideo  Streaming, M  | SNws  secara  konsisten   |     |                                |                                           |                                          |                |
|                                          |                           |     | adalah  2,80% d an 3 4,35%. D  |                                           | i  sisi  lain,  rata-rata p enggunaan C  | PU  dan        |
mengungguli m  onolit d i  hampir  semua  skenario l alu  lintas l atar  belakang.
|     |     |     | penggunaan R  | AM  pada  VM  Ryu M  | onolith  kami m  asing-masing a dalah   |     |
| --- | --- | --- | ------------- | -------------------- | --------------------------------------- | --- |
Rata-rata, M  SNws  menunjukkan p engurangan p enundaan  sebesar  21,21%
0,41% d an  13,9%. S umber  daya t inggi y ang s udah  digunakan  untuk V M
| dan p eningkatan t hroughput  sebesar 1 5,49% d ibandingkan  dengan m  |     | onolit. |                              |     |                                                |     |
| ---------------------------------------------------------------------- | --- | ------- | ---------------------------- | --- | ---------------------------------------------- | --- |
|                                                                        |     |         | Pekerja K ubernetes  kami m  |     | enunjukkan  bahwa  Kubernetes  dan i nstance   |     |
penerapannya t elah  mencadangkan s ejumlah  sumber d aya. P enggunaan
| Sebaliknya, L ayanan W  | eb d an V oIP  menunjukkan k inerja  yang l ebih   |     |     |     |     |     |
| ----------------------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
VM  Ryu M  onolith  yang  lebih r endah  menunjukkan b ahwa  aplikasi
baik  dengan  arsitektur  monolit.  Layanan W  eb, r ata-rata,  menunjukkan
disebarkan l angsung k e  host  sebagai  layanan  tanpa p erantara  di a ntara
penundaan  31,80%  lebih r endah d an k eluaran  37,31%  lebih t inggi
keduanya.
dibandingkan  MSNws,  sementara V oIP  menunjukkan p enurunan
penundaan s ebesar  47,32% d an s edikit  peningkatan  keluaran  sebesar
0,45% d ibandingkan  dengan  MSNws. K hususnya,  nilai p ersentase i ni
| tidak  memperhitungkan n ilai  absolut  penundaan d an  throughput. O  |     | leh   |     |     |     |     |
| ---------------------------------------------------------------------- | --- | ----- | --- | --- | --- | --- |
karena i tu,  menilai p ersentase i ni  dalam
| 8   |     |     |     |     |     | JILID  XX,  2017 |
| --- | --- | --- | --- | --- | --- | ---------------- |

Machine Translated by Google
|     |     |     |     | tetap  terjaga,  bahkan m  | enghadapi  tantangan l alu  lintas j aringan  yang  dinamis   |     |     |     |
| --- | --- | --- | --- | -------------------------- | ------------------------------------------------------------- | --- | --- | --- |
dan  beragam.
Sistem y ang d iusulkan  (MSNws) d apat  ditingkatkan u ntuk
mengembangkan k omponen p erangkat l unak  atau  logika a plikasi  yang  lebih
dinamis.  Dalam  konteks i ni, d inamis b erarti p erangkat l unak  mengikuti
|     |     |     |     | praktik  terbaik m   | enggunakan  layanan p endukung  seperti d atabase  untuk   |     |          |            |
| --- | --- | --- | --- | -------------------- | ---------------------------------------------------------- | --- | -------- | ---------- |
|     |     |     |     | menyimpan a lamat M  | AC d an  data  topologi l ainnya. D                        |     | engan m  | enyimpan   |
data  topologi d alam d atabase, l ogika a plikasi  dapat  menjadi l ebih  efisien
|     |     |     |     | dan  terukur k arena d ata  topologi t idak p erlu d iduplikasi s aat m  |     |     |     | elakukan   |
| --- | --- | --- | --- | ------------------------------------------------------------------------ | --- | --- | --- | ---------- |
GAMBAR  11.  Pemanfaatan C PU
|     |     |     |     | upgrade  komponen l ogika a plikasi. H  |     | al  ini k arena k omponen  logika  aplikasi   |     |     |
| --- | --- | --- | --- | --------------------------------------- | --- | --------------------------------------------- | --- | --- |
tidak l agi  memperluas  data  topologi p enyimpanan.  Selain  itu, p enelitian i ni
| Gambar 1 1 m  | enunjukkan  hasil p emanfaatan  CPU  untuk s kenario  ini   |     |     |                      |                                |     |                         |     |
| ------------- | ----------------------------------------------------------- | --- | --- | -------------------- | ------------------------------ | --- | ----------------------- | --- |
|               |                                                             |     |     | diharapkan  dapat m  | empertimbangkan p enggunaan m  |     | ekanisme  penyimpanan   |     |
secara  progresif  dan  dengan  lalu  lintas l atar  belakang  yang  meningkat
persisten s eperti P ersistent V olumes ( PV)  Kubernetes  untuk  layanan
| secara  bertahap. G                   | rafik i ni m  enunjukkan b ahwa p engontrol  layanan m  |                                         | ikro   |                       |                                                               |     |     |     |
| ------------------------------------- | ------------------------------------------------------- | --------------------------------------- | ------ | --------------------- | ------------------------------------------------------------- | --- | --- | --- |
|                                       |                                                         |                                         |        | database. D  engan m  | elakukan h al i ni, d ata  penting  seperti  data  topologi   |     |     |     |
| melakukan  penggunaan p emanfaatan C  |                                                         | PU y ang l ebih  stabil d ibandingkan   |        |                       |                                                               |     |     |     |
akan l ebih  aman  dan  terlindungi  serta d apat d iakses  secara  konsisten
pengontrol  monolit  seiring d engan p eningkatan u kuran  lalu  lintas l atar
|     |     |     |     | bahkan  dalam s ituasi  yang m  | emerlukan  skalabilitas  atau  pemulihan  setelah   |     |     |     |
| --- | --- | --- | --- | ------------------------------- | --------------------------------------------------- | --- | --- | --- |
belakang. P erilaku  ini d imungkinkan k arena  kemampuan K ubernetes  untuk
|     |     |     |     | kegagalan.  Dengan m  | engintegrasikan P V k e d alam a rsitektur, M  |     |     | SNws   |
| --- | --- | --- | --- | --------------------- | ---------------------------------------------- | --- | --- | ------ |
membatasi  dan  mencadangkan s umber d aya  dari p od K ubernetes y ang  di-
dapat m  eningkatkan k eandalan  dan  ketersediaan s istem  secara  keseluruhan,
deploy, s eperti  yang d isebutkan s ebelumnya, d engan p ermintaan d an  batasan  penerapan.
|                                                         |     |                        |     | yang s angat p enting  dalam m  |     | emastikan k inerja  optimal  dalam m  |     | anajemen   |
| ------------------------------------------------------- | --- | ---------------------- | --- | ------------------------------- | --- | ------------------------------------- | --- | ---------- |
| Setelah  lalu l intas l atar b elakang  4 h ingga  6 M  |     | B, M  SNws k ami  bisa |     |                                 |     |                                       |     |            |
jaringan y ang k ompleks.
| mengungguli R                                | yu M  onolith, d engan  rata-rata  penggunaan C                 |     | PU s ekitar  18%   |     |     |     |     |     |
| -------------------------------------------- | --------------------------------------------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |
| lebih  efisien. S elain  itu, j ika  kita m  | empertimbangkan k eadaan  awal                                  |     |                    |     |     |     |     |     |
| penggunaan C                                 | PU s ebelum s kenario d ijalankan,  perbandingan p eningkatan   |     |                    |     |     |     |     |     |
PENGAKUAN
| puncak p enggunaan C  | PU R  yu M  onolith a dalah  21% l ebih  tinggi   |     |     |     |     |     |     |     |
| --------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Kami  mengucapkan  terima  kasih y ang s ebesar-besarnya  atas d ukungan
| dibandingkan  MSNws.  Ini  berarti  Ryu  Monolith m  |     | emiliki p enggunaan C  | PU   |     |     |     |     |     |
| ---------------------------------------------------- | --- | ---------------------- | ---- | --- | --- | --- | --- | --- |
yang  lebih  tinggi  pada  kemampuan  penggunaan  puncaknya d ibandingkan   tak t ernilai  yang d iberikan  selama  penelitian i ni. D  ukungan  ini  dengan  murah
MSNws. hati  diberikan m  elalui i nfrastruktur p enelitian  Adaptive N  etwork  Laboratory,
Di  sisi l ain,  penggunaan  RAM  untuk k edua a rsitektur c ukup sebuah  proyek  yang t erlaksana  melalui p endanaan  dan k omitmen T elkom
University.
tidak  meningkat  secara  signifikan s etelah  skenario b erjalan.  Bahkan k etika
kita m  embandingkan h asil  dari  setiap l alu  lintas l atar  belakang  yang
| berbeda,  peningkatannya  tidak  signifikan  karena  rata-rata s ekitar  0,4%   |     |                               |     | REFERENSI           |                                     |     |     |     |
| ------------------------------------------------------------------------------- | --- | ----------------------------- | --- | ------------------- | ----------------------------------- | --- | --- | --- |
|                                                                                 |     |                               |     | [1] MB  Jimenez, D  | .  Fernandez,  JE  Rivadeneira, L . |     |     |     |
| untuk  Ryu M  onolith  dan  2,2% u ntuk M                                       |     | SNws.  Secara k eseluruhan,   |     |                     |                                     |     |     |     |
ekspektasi  penggunaan s umber d aya  MSNws d ibandingkan  Ryu  Monolith   Bellido,  dan  A. C  ardenas,  “Survei M  asalah  Keamanan U  tama
dan S olusi u ntuk  Arsitektur  SDN,” I EEE  Access, v ol.
| bisa l ebih e fisien  dalam  pemanfaatan C  |     | PU  tetapi d engan b eberapa   |     |     |     |     |     |     |
| ------------------------------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
9, h al.122016–
persyaratan  agar  RAM d apat d igunakan l ebih  banyak  pada k eadaan  awal
122038, 2 021,  doi:
dan  peningkatan  lebih  tinggi  sekitar 1 ,8%.
10.1109/ACCESS.2021.3109564.
[2] MU  Younus, S .ul I slam, I . A li, S .Khan, d an  M.
V.  PERMASALAHAN T ERBUKA  DAN  KESIMPULAN
K. K han, “ Survei t entang  jaringan  yang d itentukan
| Secara k eseluruhan,  penelitian  ini m  |     | emberikan p emahaman y ang   |     |     |     |     |     |     |
| ---------------------------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
perangkat l unak  memungkinkan  bangunan p intar:  Arsitektur,
| lebih  mendalam t entang p eran a rsitektur  layanan m  |     | ikro  dalam m  | engelola   |     |     |     |     |     |
| ------------------------------------------------------- | --- | -------------- | ---------- | --- | --- | --- | --- | --- |
tantangan d an  kasus p enggunaan,” J urnal  Aplikasi J aringan
jaringan d engan l alu l intas  tinggi, k hususnya  dalam k onteks  jaringan p erusahaan.
dan K omputer,  vol.  137,  hlm.  62–77, J uli  2019, d oi:  10.1016/
| Hasil p enelitian  menunjukkan  bahwa S DN C  |     | ontroller  berbasis m  | icroservices   |     |     |     |     |     |
| --------------------------------------------- | --- | ---------------------- | -------------- | --- | --- | --- | --- | --- |
j.jnca.2019.04.002.
| mempunyai  keunggulan d alam m  | enjaga  kestabilan  performa j aringan  dan   |     |     |           |                                                                 |     |     |     |
| ------------------------------- | --------------------------------------------- | --- | --- | --------- | --------------------------------------------------------------- | --- | --- | --- |
|                                 |                                               |     |     | [3] F. H  | u,  Q.  Hao, d an  K. B ao,  “Survei t entang  Jaringan  yang   |     |     |     |
penggunaan r esource  CPU.  Namun,  perlu  dicatat  bahwa  pengontrol  layanan
|     |     |     |     | Ditentukan P erangkat  Lunak d an  OpenFlow: D  |     |     | ari K onsep   |     |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- | ------------- | --- |
mikro m  enunjukkan  kinerja y ang  lebih r endah d an l ebih  tidak  stabil
hingga I mplementasi,” S urvei  &  Tutorial  Komunikasi  IEEE,  vol.
| dibandingkan  dengan p engontrol m  | onolitik  ketika  dihadapkan  dengan   |     |     |     |     |     |     |     |
| ----------------------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
16, t idak.  4, h al.2181–2206, 2 014,  doi:  10.1109/
| layanan d engan a liran d ata k onstan, s eperti  VoIP. O  |     | leh  karena  itu,  pilihan   |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
COMST.2014.2326417.
antara k edua j enis  pengontrol  harus d idasarkan p ada k ebutuhan  jaringan   [4] L. N  óvoa, V . T avares, C  . N  ahum, S . L ins,  dan  A.
| tertentu,  dengan m  | empertimbangkan t rade-off  antara  kinerja d an s tabilitas.   |     |     |                            |     |                                 |     |      |
| -------------------- | --------------------------------------------------------------- | --- | --- | -------------------------- | --- | ------------------------------- | --- | ---- |
|                      |                                                                 |     |     | Klautau,  “Implementasi m  |     | iddleware  untuk  Pengontrol R  |     | YU   |
Penelitian i ni j uga  membuka  pintu  bagi  penelitian  lebih l anjut  dalam   SDN  untuk  mengelola  sakelar  dalam s kenario  C-RAN,” d alam
mengoptimalkan p enggunaan a rsitektur  layanan m  ikro  di l ingkungan   Anais  do  XLVIII  Seminário I ntegrado  de  Software e  H  ardware
jaringan y ang b eragam. P engembangan  lebih l anjut  dari a rsitektur i ni  dapat
(SEMISH  2021), S ociedade B rasileira  de  Computação
meningkatkan  kinerja  di b erbagai  layanan s ekaligus  menjaga  fleksibilitas   -  SBC, J uli  2021,  hlm. 1 9– 2 9. d oi:  10.5753/semish.2021.15803.
yang  diberikan o leh  pendekatan i ni.  Dengan b egitu,  jaringan y ang  efisien
dan  dapat  diandalkan d apat t ercipta [5] ST A rzo  dkk., “ MSN: K erangka K erja u ntuk  Desain d an  Evaluasi
|     |     |     |     | Berbasis L ayanan M  |     | ikro |     |                  |
| --- | --- | --- | --- | -------------------- | --- | ---- | --- | ---------------- |
| 8   |     |     |     |                      |     |      |     | JILID  XX,  2017 |

Machine Translated by Google
sdN C ontroller,” Jurnal M anajemen J aringan dan S istem, Komunikasi, jilid. 35, t idak. 1 1, h al. 2512–2521, November
vol. 30, tidak. 1, h al. 1 9 Januari 2022, d oi: 10.1007/ 2017, doi: 10.1109/JSAC.2017.2760147.
s10922-021-09631-7. [16] A M E scolar, J M Alcaraz-Calero, P. S alva-
[6] Samsung E lectronics Corporation, “Cloud Native 5G C ore Garcia, JB Bernabe, dan Q . Wang, “ Pemotongan J aringan
Samsung 5 G Core Vol.2,” J anuari 2020. Adaptif dalam Jaringan IoT 5 G M ulti-Penyewa,”
[On line]. Tersedia: http:// IEEE A ccess, vol. 9 , h al. 14048–14069, 2021, doi: 10.1109/
gsacom.com/technology/5g/ ACCESS.2021.3051940.
[7] HV N etto, L C Lung, M. Correia, A F Luiz, d an LM S á d e [17] CV Nahum dkk., “Uji Kecerdasan Buatan T erhubung 5 G
Souza, “ Replikasi m esin status dalam c ontainer y ang dikelola di J aringan Virtual,”
oleh K ubernetes,” Jurnal A rsitektur Sistem, vol. 7 3, hlm. 53– Akses IEEE, jilid. 8 , h al. 223202–223213, 2020, doi:
59, Februari 2017, doi: 1 0.1016/j.sysarc.2016.12.007. 10.1109/ACCESS.2020.3043876.
[18] Y ayasan J aringan Terbuka, “ onosproject.”
[8] IM Al Jawarneh d kk., “ Container Orchestration Engines: A Diakses: 03 September 2023. [Online]. Tersedia: h ttps://
Thorough Functional and P erformance Comparison,” d alam docs.onosproject.org/
ICC 2 019 - 2 019 IEEE I nternational C onference [19] S. Y un, J. P ark, H. K im, d an W.-T. K im,
on C ommunications ( ICC), I EEE, M ei 2019, h lm. 1–6. “Importance-aware SDN C ontrol Mechanism for Real-time
doi: 10.1109/ICC.2019.8762053. Data Distribution Services,” pada K onferensi Internasional
tentang K onvergensi T eknologi Informasi d an Komunikasi
[9] L.-M. T ufeanu, A. Mars, M.-C. Vochin, C .-L. (ICTC) 2018, IEEE, Oktober 2 018, hlm. 1 113–1118. doi:
Paraschiv, d an F Y L i, “ Membangun J aringan 5G S A d alam 10.1109/ICTC.2018.8539690.
Kontainer Sumber T erbuka m elalui Docker dan K ubernetes,”
pada Simposium I nternasional k e-25 tentang Komunikasi [20] S. B howmik, “ Memanfaatkan kekuatan jaringan y ang
Multimedia Pribadi Nirkabel ( WPMC) tahun 2 022, I EEE, ditentukan perangkat l unak u ntuk m iddleware
Oktober 2 022, hlm. d oi: 1 0.1109/ komunikasi berkinerja tinggi,” d alam Prosiding L okakarya
WPMC55625.2022.10014753. Internasional Kedua t entang M iddleware Aktif p ada
[10] A. Pacini, D. S cano, L . Valcarenghi, A. Perangkat Keras Modern, New York, NY, AS: ACM, Desember
Sgambelluri, dan A . Giorgetti, “ Mengaktifkan sinkronisasi 2017, hal. 14–14. d oi: 10.1145/3155889.3155894.
hierarki berbasis peristiwa di c luster S DN O NOS,” pada
Konferensi IEEE 2 022 tentang Virtualisasi Fungsi J aringan [21] R. S herwood d kk., “FlowVisor: L apisan V irtualisasi
dan Jaringan yang D itentukan Perangkat L unak ( NFV- Jaringan,” Oktober 2 009.
SDN), I EEE, N ovember 2 022, h lm. [22] A M P otdar, N. D G, S. K engond, d an M M
93. doi: 10.1109/NFV-SDN56302.2022.9974775. Mulla, “ Evaluasi K inerja K ontainer Docker d an M esin
[11] H. D onertasli dan Z. A ltan, “ Vendor Independent S DN Virtual,” Procedia C omput S ci, vol. 1 71, hlm. 1419–1428, 2 020,
Architecture S olution,” p ada K onferensi doi: 10.1016/j.procs.2020.04.152.
Internasional Ilmu dan T eknik Komputer (UBMK) k e-5 tahun
2020, IEEE, S eptember 2 020, h lm. doi: 1 0.1109/ [23] M . Pratap Y adav, N. P al, dan D. K umar Yadav, “Pendekatan f ormal
UBMK50275.2020.9219421. untuk p enerapan c ontainer Docker,”
[12] Z. Awada, K . Boulos, M. El-Helou, K . Khawam, d an S . Komputasi S etuju, vol. 3 3, t idak. 2 0 Oktober 2 021, doi:
Lahoud, “Distributed m ulti-tenant R AN s licing i n 5 G 10.1002/cpe.6364.
network,” Wireless N etworks, v ol. 28, tidak. 7 , hlm. 3185– [24] N . N guyen d an T . K im, “ Menuju P enyeimbangan B eban y ang
3198, Oktober 2 022, d oi: 1 0.1007/ Sangat S kalabel di C luster K ubernetes,” Majalah
s11276-022-03023-8. Komunikasi I EEE, vol. 5 8, t idak. 7 , h al.78–
[13] A. Rafiq, A. Mehmood, d an W .-C. Lagu, “ Pengirisan Berbasis 83, J uli 2 020, doi: 10.1109/MCOM.001.1900660.
Niat a ntar K ontainer d i J aringan O verlay SDN,” Jurnal [25] flanel-io, “flanel.” Diakses: 03 September 2023.
Komunikasi, h al.237– [On line]. Tersedia: h ttps://github.com/flannel-io/flannel
244, 2 020, doi: 10.12720/jcm.15.3.237-244.
[14] X. Zhou, R . L i, T . Chen, d an H . Zhang, “ Pengirisan jaringan [26] O pen N etworking Foundation, “ Spesifikasi OpenFlow Switch Versi
sebagai layanan: m emungkinkan jaringan s eluler yang 1.5.1,” 2 015. [Online].
ditentukan o leh p erangkat l unak m ilik p erusahaan,” Tersedia: h ttp://www.opennetworking.org
IEEE C ommunications M agazine, vol. 5 4, tidak. 7 , hal.146– [27] T. A lharbi d an M . Portmann, “ Keamanan (Dalam) Virtualisasi
153, J uli 2016, doi: dalam Jaringan yang Ditentukan Perangkat L unak,”
10.1109/MCOM.2016.7509393. Akses IEEE, jilid. P P, hal. 1, S eptember 2019, doi:
[15] N .Zhang, Y .-F. Liu, H. F armanbar, T.-H. C hang, M.Hong, d an Z .- 10.1109/ACCESS.2019.2918101.
Q. L uo, “ Pemotongan J aringan untuk J aringan Berorientasi [28] N . X ie, W. Tan, X . Z heng, L. Z hao, L. H uang, dan Y . S un,
Layanan d i B awah K endala Sumber D aya,” Jurnal “Pendekatan dua f ase y ang efisien u ntuk k omposisi
IEEE t entang Area T erpilih di layanan s adar k olaborasi yang andal d i
8 JILID XX, 2017

Machine Translated by Google
manufaktur c loud,” J Ind Inf I ntegr, vol. 23, hal.
100211, S eptember 2 021, doi: 1 0.1016/j.jii.2021.100211.
[29] L. Cai, Y . Q i, W . Wei, dan J . Li, “Meningkatkan
Penggunaan S umber Daya K ontainer melalui
Penyetelan O tomatis P arameter S umber Daya K ontainer,”
IEEE A ccess, vol. 7, hal. 1 08530–108541, 2 019, d oi:
10.1109/ACCESS.2019.2927279.
8 JILID XX, 2017