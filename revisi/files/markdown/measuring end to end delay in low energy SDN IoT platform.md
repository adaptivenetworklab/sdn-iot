# measuring end to end delay in low energy SDN IoT platform

> Source file: `measuring end to end delay in low energy SDN IoT platform.pdf`

---

Machine Translated by Google
Komputer, M aterial & L anjutan Pers Sains T eknologi
DOI:10.32604/cmc.2022.018579
Artikel
Mengukur P enundaan End-to-End p ada Platform I oT SDN B erenergi R endah
Mykola Beshley1 ,Natalia Kryvinska2,*, Halyna B eshley1 , Orest Kochan1 d an L eonard B arolli3
1Departemen Telekomunikasi, Universitas Nasional P oliteknik L viv, 79013 Lviv, Ukraina
2Departemen Sistem Informasi, Fakultas M anajemen, Universitas Comenius d i Bratislava, 82005 Bratislava, S lovakia
3Departemen Teknik Informasi dan K omunikasi, Fakultas T eknik Informatika, I nstitut Teknologi Fukuoka ( FIT) , 3 -30-1
Wajiro-Higashi, H igashi-Ku, F ukuoka 8 11-0295, Jepang *Penulis Koresponden:
Natalia K ryvinska. Email: natalia.kryvinska@uniba.sk D iterima: 1 2 M aret 2021;
Diterima: 17 A pril 2 021
Abstrak: Dalam tulisan ini, k ami mengembangkan p latform Internet of Things ( IoT) berbasis
Software Defined Networking (SDN) h emat e nergi b aru y ang dapat d ikonfigurasi u lang
sesuai d engan kebutuhan aplikasi IoT target.
Secara teknis, platform ini t erdiri dari s eperangkat komputer p apan t unggal berbiaya r endah
dan h emat energi, y ang saling t erhubung dalam j aringan dengan konfigurasi yang
ditentukan p erangkat l unak. Sakelar S DN yang diusulkan diterapkan pada papan R aspberry
Pi 3 menggunakan perangkat l unak O pen vSwitch (OvS), s edangkan pengontrol Floodlight
diterapkan pada papan Orange P i P rime. K ami pertama kali mempresentasikan dan
menerapkan metode u ntuk mengukur penundaan y ang diperkenalkan o leh setiap k omponen
infrastruktur I oT, mulai dari sensor, i nti SDN, broker I oT, h ingga p elanggan IoT. O leh karena
itu, k ami m enyajikan p endekatan u ntuk memperkirakan e fisiensi energi u ntuk platform IoT
berbasis SDN yang sebanding d engan l alu l intas.
Eksperimen yang dilakukan p ada topologi SDN nyata berdasarkan komputer p apan t unggal
menunjukkan b ahwa pendekatan k ami tidak h anya m enghemat hingga 5 3,56% energi p ada
intensitas lalu l intas rendah, n amun j uga m emberikan j aminan QoS u ntuk aplikasi IoT.
Kata K unci: I nternet of T hings; j aringan y ang ditentukan perangkat l unak; aliran terbuka; buka
vswitch; raspberry-pi
1. Perkenalan
1.1 L atar Belakang dan Rumusan M asalah
Di dunia modern, Internet t elah m enjadi k ebutuhan d asar setiap orang. Efisiensi energi dan infrastruktur
jaringan ramah lingkungan sangat d iminati k arena m engurangi biaya e nergi sehingga menghemat uang
konsumen. Efisiensi e nergi m engurangi polusi lingkungan, menyediakan l ebih b anyak e nergi, d an meningkatkan
perekonomian. Dalam m akalah [1–4] A lgoritma O ptimasi P aus-Optimasi A pi Ngengat hibrida d iusulkan u ntuk
memilih C luster H ead yang o ptimal, yang p ada gilirannya m engoptimalkan konsumsi e nergi untuk j aringan IoT.
Pendekatan ini m emberikan p enyeimbangan beban y ang e fisien, e nergi sisa y ang l ebih b aik, d an latensi y ang
lebih p endek, s ehingga menghasilkan masa p akai j aringan yang l ebih l ama. Salah s atu t antangan terpenting
adalah m enjaga masa p akai baterai pada perangkat yang d igunakan d i s emua j aringan IoT. K arena b anyak p erangkat IoT
Karya ini dilisensikan di b awah Lisensi I nternasional Creative C ommons Attribution 4.0, yang mengizinkan
penggunaan, d istribusi, d an reproduksi tanpa batas d alam media a pa pun, a salkan karya a sli d ikutip dengan
benar.

Machine Translated by Google
20 CMC, 2 022, j ilid 7 0, n o.1
tidak mengisi u lang, penulis di [ 5] mengusulkan p endekatan untuk menghemat masa pakai b aterai jaringan IoT
menggunakan prediksi m asa pakai baterai a wal.
Dalam makalah [ 5], A nwaar membuktikan bahwa Raspberry Pi m engkonsumsi l ebih sedikit d aya d an dapat
menghemat sejumlah besar e nergi s aat melakukan t ugas komputasi r utin. Dalam makalah [6], p enulis menyarankan
alternatif y ang lebih h emat b iaya untuk m engimplementasikan S DN t estbed d engan Open vSwitch (OvS), berdasarkan
komputer mini R aspberry-Pi berenergi rendah d engan kemampuan p rogram y ang mudah. Testbed ini d iusulkan untuk
jaringan skala k ecil. N amun p enulis t idak melakukan p enelitian m engenai k ualitas p emberian layanan. P ara penulis d i
[7] m engembangkan prototipe saklar S DN yang hemat b iaya, terukur, d an berkemampuan Q oS untuk komunikasi I oT
berdasarkan Raspberry P i 3. Namun, penulis t idak melakukan penelitian t entang kesesuaian platform t ersebut untuk
misi. - aplikasi I oT penting sesuai d engan persyaratan QoS y ang dapat diterima. M ereka juga t idak m empertimbangkan
pendekatan perutean SDN dalam k ondisi beban jaringan yang tinggi d engan adanya l alu lintas IoT multilayanan
dengan p ersyaratan QoS y ang b erbeda. K arena tingginya b iaya d an k ompleksitas d ari perangkat keras switch SDN
yang ada, penulis di [8] m embuat switch S DN yang h emat b iaya m enggunakan Raspberry Pi u ntuk menguji i de-ide
mereka. P ara penulis d i [ 9] menyarankan penggunaan komputer papan t unggal y ang hemat b iaya d alam k ombinasi
dengan l ayanan j aringan k emas y ang dapat diskalakan (misalnya, V OIP, l ayanan w eb, dll.) m enggunakan SDN untuk
menyediakan m anajemen p erangkat terpusat. Konfigurasi prototipe b erdasarkan Raspberry P i d ijelaskan s ecara rinci
dan pengujian o perasional a wal disajikan s ebagai sarana untuk memastikan kelayakan teknologi k onsep dalam
berbagai konfigurasi t opologi. Konsumsi e nergi p eralatan jaringan dan p emanfaatan saluran bervariasi tergantung
pada b eban dan struktur lalu lintas jaringan. Integrasi bidang k ontrol d an d ata ke dalam p erangkat individual dalam
sistem j aringan tradisional memerlukan l ebih banyak pemrosesan, sehingga menghasilkan konsumsi e nergi y ang lebih
tinggi dibandingkan p erangkat SDN. A kibatnya, jaringan IP tradisional memiliki lebih b anyak masalah konsumsi energi
karena k ompleksitasnya d alam m anajemen l alu lintas, p engendalian, dan p engoperasian [ 10-13].
Untuk aplikasi I oT yang sangat p enting, i nfrastruktur jaringan merupakan k omponen ekosistem y ang penting.
Untuk menyediakan QoS y ang sulit untuk a plikasi I oT, penting u ntuk memastikan mekanisme yang sesuai d i s etiap
lapisan infrastruktur IoT, k arena beberapa faktor, s eperti p enundaan E2E, sangat p enting [ 13-16]. Penundaan pada
lapisan m ana pun dapat m engakibatkan QoS yang tidak dapat diterima untuk aplikasi k eselamatan penting, seperti
sistem penggerak otomatis y ang selalu m embutuhkan umpan balik u ntuk mempertahankan kendali. Hasil a khir tersebut
adalah a lasan utama mengapa kepatuhan yang k etat terhadap persyaratan QoS d iperlukan d alam I oT yang sangat
penting. Hal i ni j uga merupakan salah satu alasan mengapa p erancangan platform I oT yang sangat p enting s angatlah
rumit.
Saat i ni, t erdapat b anyak solusi SDN, p engontrol, dan b erbagai p rotokol terkenal untuk komunikasi jaringan.
Namun, s ebagian b esar solusi ini mahal d an rumit. S elain i tu, mereka tidak s elalu t ersedia dan s esuai u ntuk tugas-
tugas aplikasi k ecil dan menengah, k hususnya dalam b isnis [17]. Studi t erbaru [18-21] m enunjukkan bahwa keputusan
untuk mengatur jaringan berdasarkan platform m ikrokontroler akan m enjaga efisiensi e nergi, keandalan, d an keamanan
jaringan, dan khususnya integrasi d engan I nternet tidak memerlukan banyak usaha.
Keserbagunaan m ikrokontroler juga t erletak pada m odel K otak Putih, yang menunjukkan bahwa solusi perangkat k eras
tidak terikat d engan s olusi perangkat lunak, d an a kan memungkinkan seseorang dengan mudah berpindah ke satu
atau solusi p erangkat lunak lainnya sehubungan dengan relevansi d an k ebutuhan. Setiap elemen jaringan dapat
mengubah t ujuan dan perannya dalam j aringan k apan saja.
1.2 Motivasi
Setelah m enganalisis k arya ilmiah, k ami belum m enemukan pendekatan yang memungkinkan memperkirakan
penundaan y ang ditimbulkan oleh setiap k omponen i nfrastruktur IoT, m ulai dari sensor,

Machine Translated by Google
CMC, 2022, j ilid 7 0, n o.1 21
inti S DN, b roker IoT, d an d iakhiri d engan p elanggan layanan IoT. Pendekatan ini a kan memungkinkan identifikasi h ambatan
infrastruktur yang menyebabkan degradasi parameter QoS dan m embuat k eputusan t entang cara m engatasi hambatan ini.
Karena biaya energi b erkontribusi signifikan terhadap biaya jaringan s ecara keseluruhan, efisiensi energi m erupakan
persyaratan desain y ang penting untuk p latform j aringan modern. N amun, m erancang s olusi h emat energi m erupakan s uatu
tantangan karena t erdapat t rade-off a ntara efisiensi e nergi d an k inerja jaringan.
1.3 K ontribusi Kami
Untuk mengatasi t antangan-tantangan yang d isebutkan di a tas, makalah ini berfokus p ada pembuatan platform baru
yang hemat b iaya d an h emat e nergi yang d apat d isesuaikan berdasarkan arsitektur S DN yang d apat m enyesuaikan
konfigurasinya untuk memenuhi persyaratan Q oS p ada aplikasi I oT t arget. Kontribusi utama k ami dalam m akalah ini
dirangkum sebagai b erikut: (cid:127) Kami mengembangkan prototipe s aklar
SDN y ang berbiaya rendah dan f leksibel s erta p engontrol b erdasarkan komputer p apan t unggal Raspberry P i 3 dan
orange P i P rime u ntuk komunikasi I oT;
(cid:127) Kami m erealisasikan broker IoT dan k lien w eb u ntuk platform IoT b erbasis SDN; (cid:127) Kami
mengembangkan metode u ntuk m engukur p enundaan E 2E pada platform IoT b erbasis SDN dan
sistem pemantauan k ualitas p engoperasian platform;
(cid:127) Kami m empresentasikan bukti konsep p latform I oT b erbasis SDN yang m enggunakan e nergi
komputer papan tunggal yang e fisien d an h emat b iaya;
(cid:127) Kami m empresentasikan pendekatan efisiensi e nergi untuk p latform IoT b erbasis SDN secara proporsional
untuk lalu l intas.
1.4 O rganisasi K ertas
Makalah i ni disusun sebagai b erikut. Bagian 1 menyajikan latar b elakang, rumusan masalah dan t injauan singkat karya
terkait. B agian 2 menjelaskan u sulan arsitektur p latform I oT b erbasis SDN. B agian 3 menjelaskan m etode baru untuk
mengukur penundaan E 2E p ada p latform I oT berbasis SDN dan s istem pemantauan. B agian 4 menjelaskan u sulan
pendekatan efisiensi e nergi proporsional u ntuk Platform IoT B erbasis SDN. T erakhir, k ami menarik kesimpulan d i B agian 5.
2 Platform IoT B erbasis SDN yang H emat E nergi dan Bersaing B iaya 2.1
Arsitektur Platform I oT B erbasis S DN
Pada b agian ini, k ami memperkenalkan p latform IoT b erbasis SDN yang hemat e nergi untuk a plikasi y ang s angat
penting. Arsitektur platform t erdiri dari bagian IoT dan S DN seperti y ang d itunjukkan pada Gambar 1.
Bagian ini berkomunikasi melalui B luetooth. Akses k e platform ini d ipastikan m elalui I nternet m enggunakan a plikasi W eb.
Bagian IoT. K ami berasumsi bahwa layanan IoT penting d alam p latform ini a dalah transmisi data s uhu dan k elembapan.
Untuk tujuan ini, s ensor s uhu sederhana D HT11 d igunakan [ 22].
DHT11 menyediakan pengukuran suhu s ekitar d ari 0ÿC h ingga +50ÿC dengan akurasi ± 2ÿC. S ensor ini dihubungkan ke
Raspberry Pi, yang bertindak s ebagai p emancar d ari s ensor melalui B luetooth L ow Energy (BLE). B ersama d engan s ensor,
komponen B luetooth di bagian IoT mengumpulkan data.
IoT H ub d irancang s ebagai R aspberry Pi. IoT H ub m engumpulkan data dari beberapa k omponen I oT, berkomunikasi
melalui B LE. Dengan IoT Hub, data d apat d iterima

Machine Translated by Google
22
CMC, 2 022,  jilid 7 0, n o.1
sensor  menggunakan a lgoritma y ang  efisien  dan a daptif, y ang  menjadikan  sistem p roduktif  dan h emat e nergi
[23].
bagian I oT
|     | DHT  11 Kabel | Raspberry P i | Raspberry P i e th0 |
| --- | ------------- | ------------- | ------------------- |
Bluetooth
|     | Suhu | Budak B luetooth | Pusat  IoT |
| --- | ---- | ---------------- | ---------- |
sensor
|     |     | komponen | (Master  Bluetooth) |
| --- | --- | -------- | ------------------- |
bagian S DN
Ethernet  eth0 R aspberry  Pÿ .eth0 E thernet e th1  Raspberry P ÿ
Pialang
saklar
|     |     | OpenFlow | soket w eb |
| --- | --- | -------- | ---------- |
Wifi
Oranye P i Wifi
|     | Pengontrol O penFlow | Internet Perute  Wi-Fi |     |
| --- | -------------------- | ---------------------- | --- |
klien  web
|     | Gambar 1 : A  rsitektur p latform I oT  berbasis  SDN |     |     |
| --- | ----------------------------------------------------- | --- | --- |
bagian  SDN.  Jaringan  SDN h arus  dapat  mengkonfigurasi  perangkat  jaringan s ecara  terprogram s esuai
idenya.  Pada g ilirannya,  jaringan i ni  harus  terdiri d ari  setidaknya  satu s witch, d ua h ost y ang t erhubung m  elalui
switch i ni, d an  sebuah  pengontrol y ang  memungkinkan j aringan  untuk  dikelola. B  agian  SDN d alam  arsitektur
ini t erdiri d ari  3  komponen u tama: s aklar  Openflow,  broker W  ebSockets,  dan p engontrol O  penflow.
Kami m  engembangkan  sakelar S  DN 5 -port  dengan p erangkat  Raspberry P  i 3  d an p erangkat  lunak  Open
vSwitch  (OvS).  Karena  komputer  papan  tunggal R  aspberry P  i d i p apannya  hanya  memiliki s atu p ort  Ethernet,
penggunaan a daptor  USB  ke  Ethernet p ada p apan i ni  dapat  membuat  hingga 5  p ort  Ethernet.
Karena  komputer  papan t unggal R  aspberry P  i p ada  dasarnya  bukan s aklar  SDN,  dengan  menggunakan
lingkungan  tervirtualisasi p erangkat  keras, d imungkinkan  untuk  menginstal  dan m  engkonfigurasi  saklar  virtual.
Implementasi  paling  populer d engan d ukungan  open  source  dan O  penFlow  adalah O  vS [ 24]. S  akelar  OpenFlow
berbasis R  aspberry  Pi  bertindak  sebagai s akelar v irtual  berbasis  OvS. O  vS a dalah  saklar  virtual  multilapis
berkualitas  produksi  yang  dilisensikan  di b awah l isensi s umber  terbuka A  pache 2 .0. T  ujuan  utama  dari  OvS
adalah  untuk  menyediakan  tumpukan  peralihan u ntuk  lingkungan t ervirtualisasi p erangkat  keras  untuk
mendukung  berbagai  protokol  dan s tandar,  yang d igunakan  dalam  jaringan k omputer  [25-27].
| 2.2  Uji B  ukti  Konsep  untuk P  | latform  IoT B  | erbasis S  DN |     |
| ---------------------------------- | --------------- | ------------- | --- |
Sakelar d an  pengontrol S  DN b erbiaya  rendah  dan f leksibel b erdasarkan  komputer  papan t unggal
| (Raspberry  Pi 3   dan  Orange  Pi P  | rime) d igambarkan p ada  Gambar 2 . |     |     |
| ------------------------------------- | ------------------------------------ | --- | --- |
OvS  adalah i mplementasi  perangkat  lunak d ari  saklar  jaringan m  ulti-lapis v irtual  yang  dirancang u ntuk
| memberikan  otomatisasi  jaringan y ang  efektif m  |     | elalui e kstensi p erangkat  lunak. |     |
| --------------------------------------------------- | --- | ----------------------------------- | --- |

Machine Translated by Google
CMC, 2022, jilid 70, no.1 23
Lampu Sorot Terbuka
Pengendali S DN
Papan M ini
Oranye Pi
Ethernet cepat
1 Pelabuhan 1 00Mbps
Buka vSwitch
Jalur data
Aliran T erbuka
Kelompok Meter Saluran Lapisan
Meja Meja Saluran K ontrol perangkat l unak
Pelabuhan Pelabuhan
Mengalir Mengalir Mengalir
Meja Meja Meja
Pelabuhan Pelabuhan
Saluran p ipa
OS R aspbian
Raspberry P i 3 ( model B) Lapisan
perangkat k eras
Adaptor USB-ke-Ethernet
Port Ethernet 4 Cepat
100Mbps
Gambar 2 : S akelar d an p engontrol SDN b erbiaya rendah d an f leksibel berdasarkan k omputer papan t unggal
(Raspberry Pi 3 dan j eruk Pi Prime)
OvS m enyediakan konsep j embatan. Ini b erarti satu s aklar v irtual d apat berisi banyak s aklar v irtual
jembatan, y ang pada g ilirannya d apat menggunakan tabel r outing y ang b erbeda a tau port y ang berbeda.
Untuk kenyamanan d an komunikasi real-time y ang cepat a ntar l ayanan (bukan d alam m ode p ermintaan-respons),
protokol WebSocket dipilih. WebSocket a dalah protokol y ang dirancang untuk p ertukaran i nformasi waktu n yata a ntara
browser d an server web. Ini m enyediakan s aluran k omunikasi d upleks p enuh d ua arah melalui satu s oket T CP. W ebSocket
dirancang untuk d iimplementasikan di b rowser Web dan s erver W eb, tetapi juga d apat digunakan oleh a plikasi s erver-klien
apa pun.
Antarmuka p erangkat lunak a plikasi WebSocket telah distandarisasi oleh W 3C ( World W ide Web C onsortium) dan W ebSocket
juga distandarisasi oleh IETF sebagai R FC 6 455 [28].
Meskipun WebSocket terutama dirancang u ntuk k omunikasi real-time a ntara klien Web d an l ayanan Web, WebSocket
juga berguna untuk l ayanan. Kami berencana m enggunakan p rotokol ini u ntuk k omunikasi antara server W eb d an broker.
Oleh k arena itu, kami t elah menerapkan logika b erikut dalam b entuk l angkah-langkah: (cid:127) Broker
menjalankan s erver WebSocket. (cid:127) Layanan
yang t ertarik terhubung sebagai klien k e s erver W ebSocket (klien Web dan
pusat I oT).
(cid:127) Setelah k oneksi b erhasil, k lien web m engirimkan permintaan ke s erver W ebSocket. (cid:127) Pada g ilirannya, broker
(server W ebSocket) mengirimkan p ermintaan ke h ub I oT. (cid:127) IoT Hub, pada g ilirannya,
membuat p ermintaan u ntuk komponen B luetooth yang sudah terhubung
perangkat.

Machine Translated by Google
24 CMC, 2 022, j ilid 70, no.1
(cid:127) Saat k omponen Bluetooth menerima permintaan t ersebut, komponen t ersebut m eminta d ata dari s ensor dan
mengirimkannya kembali. S etiap p erangkat, pada gilirannya, meneruskannya l ebih j auh k e k lien Web.
Setelah data dialihkan o leh tabel p erutean ke port yang s esuai, data tersebut t iba di Websocket broker. Broker ini
menggunakan protokol Websocket dengan nama y ang s ama dan merupakan servernya, yang m enyediakan k omunikasi real-
time a ntara sensor a khir dan klien web.
Kami m enggunakan papan Orange Pi P rime y ang m emiliki empat inti prosesor d an dua gigabyte RAM, yang s eharusnya
cukup untuk pengontrol SDN sederhana. U ntuk mengimplementasikan p latform IoT b erbasis S DN, pengontrol F loodlight
dipilih k arena k omponennya lebih s edikit, sehingga papan O range Pi Prime akan m engatasi tugas tersebut d engan l ebih baik.
Floodlight menunjukkan dalam p ersyaratan sistemnya kebutuhan a kan s istem operasi Ubuntu atau Debian. Sistem operasi
Ubuntu untuk Orange P i P rime dipilih karena p opularitasnya. T estbed platform I oT berbasis S DN d iberikan p ada G ambar 3.
Gambar 3 : B ukti uji konsep u ntuk platform I oT berbasis S DN
Dalam platform y ang d iusulkan, p engontrol SDN m erupakan titik k ontrol untuk m emantau jaringan, mengendalikan aliran
data, s erta p enyeimbangan b eban, penskalaan o tomatis, dan manfaat S DN lainnya. Pengontrol i ni tidak m engalami kegagalan
tunggal, yang berarti jaringan d apat terus beroperasi dalam mode n ormal. P engontrol l ampu sorot d i antarmukanya memiliki
dua c ara mudah untuk mengelola j aringan-REST A PI dan GUI. G UI d ibuat s ebagai k lien W eb.
3 M etode A kurat B aru u ntuk Mengukur Delay E nd-to-End ( E2E) di IoT B erbasis S DN
Platform
3.1 Metode Pengukuran Delay p ada Platform I oT Berbasis S DN
Dalam pekerjaan i ni, sistem untuk memantau kualitas p engoperasian platform I oT berbasis S DN d ikembangkan. Untuk
menilai e fisiensi operasinya dengan b enar, beberapa kriteria k ualitas sistem dipilih. Salah s atunya adalah p enundaan. S ampai
saat i ni, i ni adalah s alah satu k riteria u tama kualitas s istem untuk layanan p enting. Untuk tujuan i ni, m etode pengukuran
penundaan E 2E t elah d ikembangkan. K eunikan m etode ini adalah m emungkinkan penentuan p enundaan p ada s etiap
komponen platform y ang d iusulkan. Metode p engukuran penundaan m embuat s truktur d ata tertentu yang b erisi metadata
dan d ata yang b erguna (payload) sebagai objek. Formatnya a dalah J SON (JavaScript Object Notation), karena dalam format
ini data dapat dibaca oleh m anusia dan nyaman untuk d iproses o leh komputer.

Machine Translated by Google
| CMC,  2022,  jilid  70, n o.1 |     |     |     |     |     | 25  |
| ----------------------------- | --- | --- | --- | --- | --- | --- |
Setiap k omponen  menerima p aket  dan m  enambahkan  stempel  waktunya  sendiri  ke m  etadata, s ehingga  dengan m  embandingkan
dua  label  satu  sama  lain,  waktu  tunda  dapat  ditentukan.  Secara  skematis, m  etode p engukuran  penundaan  ini d iberikan p ada  Gambar 4 .
Untuk  menghitung p enundaan  antara k edua  modul,  cukup d engan m  engurangi c ap  waktu  modul  terakhir d ari m  odul  sebelumnya,  dan
selisihnya  akan  menjadi p enundaan y ang  tepat.
|     |     | Komponen  #1 | Komponen # 2 |     |     |     |
| --- | --- | ------------ | ------------ | --- | --- | --- |
Memasukkan
|     |        | Metadata |        | Metadata            |        |     |
| --- | ------ | -------- | ------ | ------------------- | ------ | --- |
|     | Muatan |          | Muatan | Stempel  waktu S #1 | Muatan |     |
Stempel w aktu  S#1
Stempel w aktu  S#2
|     | Pesan |     | Pesan | Pesan |     |     |
| --- | ----- | --- | ----- | ----- | --- | --- |
Gambar  4:  Prinsip  kerja  metode y ang d iusulkan
Metode i ni  mengharuskan  jam  pada s emua  komponen  disinkronkan s emaksimal m  ungkin u ntuk  perhitungan y ang a kurat.  Untuk i ni
kami m  enggunakan m  etode  paling u mum u ntuk  menyinkronkan w  aktu s istem m  elalui  jaringan  di  desktop  atau  server  Linux  adalah  dengan
menjalankan p erintah n tpdate  yang  dapat  mengatur  waktu s istem d ari  server  waktu N  TP  dengan k esalahan  satu  mikrodetik [ 29].  Jadi,
ketika  semua  komponen b erada  dalam j aringan  internal, t ermasuk  broker,  kesalahan  pengukuran p enundaan  adalah s atu  mikrodetik. J ika
broker  berlokasi  di j aringan  eksternal,  sulit u ntuk m  emastikan  akurasi  pengukuran p enundaan  yang t inggi,  kesalahan d apat b ervariasi
dalam  beberapa m  ilidetik.
Metode i ni  memudahkan  pengukuran  penundaan a ntara k omponen  tertentu d an t otal  penundaan  E2E. H  al  ini j uga  memungkinkan
sistem u ntuk b ereaksi d engan  benar  ketika  penundaan m  eningkat  secara d ramatis  atau  mencapai  ambang b atas  yang d itetapkan.
(cid:127)  N p ertama  =  10 p esan  yang  diterima  dengan s emua s tempel  waktu  stempel  waktu,  dimana s tempel  waktu a dalah v ariabel  yang
menunjukkan  stempel w  aktu,  komponen  m  (pengontrol  SDN,  saklar S DN,  broker,  sensor, d ll.).  (cid:127)  Penundaan d ihitung  antara
seluruh  komponen  jaringan
menggunakan p ersamaan  berikut
| penundaanm2ÿm1  =  stempel  waktu2  ÿ s tempel  waktu1 |     |     |     |     |     | (1) |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
(cid:127)  Nilai  ambang b atas u ntuk  setiap p enundaan k omponen d ihitung  dengan c ara
n = 10 1
| ambang b atasm2ÿm1  = |     | penundaanm2ÿm1i ·  1 ,20 |     |     |     | (2) |
| --------------------- | --- | ------------------------ | --- | --- | --- | --- |
N
Saya
| (cid:127)  dimana  1,20  adalah o ffset m  | aksimum  dari p enundaan r ata-rata.  (cid:127)  Total   |     |     |     |     |     |
| ------------------------------------------ | -------------------------------------------------------- | --- | --- | --- | --- | --- |
penundaan a mbang b atas  dihitung d engan
| jumlah  ambang b atas =   ambang  batasm2ÿm1 |     |     |     |     |     | (3) |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- |
(cid:127)  Selanjutnya,  pesan  hanya  dikirim d engan  stempel  waktu  awal  untuk  menentukan  total  penundaan.  (cid:127)  Jika t otal  penundaan
terlampaui, p esan  berikut  akan  dikirim d engan  stempel w  aktu d an p enundaan  tersebut  dipantau  pada  setiap  modul. S istem  akan
secara o tomatis  menerima o ptimasi u ntuk m  enghilangkan p enundaan  yang t inggi u ntuk  aplikasi y ang s angat  penting.  (cid:127)  Setelah
menyelesaikan  optimasi  kita k embali k e  langkah p ertama.

Machine Translated by Google
26 CMC, 2022, jilid 7 0, n o.1
Algoritma p engukuran p enundaan p ada p latform IoT b erbasis SDN diberikan pada Gambar 5 .
Gambar 5 : Algoritma p engukuran penundaan pada platform I oT b erbasis SDN
3.2 Hasil Eksperimen
Platform i ni hanya memiliki s atu switch y ang menghubungkan dua h ost dan s atu pengontrol SDN.
Perangkat IoT d iimplementasikan sebagai s ensor suhu dan k elembaban sederhana. Sensor i ni h anya
mengirimkan d ua parameter yaitu data p engukuran kelembapan dan s uhu melalui Bluetooth. K lien
Web d iimplementasikan d alam d ua pilihan: s erver Web dan k lien Web berada d i jaringan i nternal
(localhost). Server W eb d itempatkan dari j arak j auh di salah s atu layanan h osting W eb gratis, dan
klien t erhubung m elalui j aringan seluler 4G ( Heroku).
Salah satu tugas k onsep IoT a dalah mentransfer dan m enyimpan data pengukuran d ari berbagai
sensor d engan kemungkinan pemrosesan d an p enyimpanan lebih l anjut [ 30].
Pengukuran yang dikombinasikan d engan k onsep IoT s eperti “rumah p intar” d an “ kota p intar” m enjadi
sangat p enting. Di a ntara nilai y ang paling s ering diukur adalah parameter lingkungan d an p arameter
iklim d alam ruangan s eperti suhu [31] dan kelembaban [32].
Perlu juga d icatat bahwa dua besaran f isis terakhir sangat penting dalam industri

Machine Translated by Google
CMC, 2022, j ilid 70, no.1 27
[33–35]. B ahkan ada k onferensi k husus y ang didedikasikan untuk pengukurannya, seperti “ TEMP-MEKO”
dan “Suhu: p engukuran d an p engendaliannya d alam s ains d an industri”. O leh k arena itu, karena pentingnya
pengukuran suhu dan k elembaban, penulis m emilih s ensor s uhu dan kelembaban u ntuk membuat testbed
dalam pekerjaan ini.
Contoh sistem monitoring delay p ada platform I oT b erbasis SDN k etika web server d an w eb client
berada pada jaringan i nternal-localhost digambarkan pada Gambar 6 . P ada s istem ini h anya hasil 8
percobaan transmisi data (pengukuran suhu) dan k elembaban) ditampilkan untuk kejelasan.
Gambar 6 : S istem p emantauan penundaan pada platform I oT b erbasis S DN ( web s erver d an web c lient
berada di jaringan i nternal-localhost)
20 p ercobaan t ransmisi d ata dilakukan untuk menilai r ata-rata p enundaan dan p erilaku platform d engan
lebih baik. Salah satu e ksperimennya a dalah m embuat permintaan dari k lien w eb dan m endapatkan respons
dari klien w eb. A da penundaan seperti: penundaan pembacaan sensor, penundaan Bluetooth, penundaan
SDN, p enundaan WebSocket, penundaan Web, p enundaan total E 2E.
Delay b aca Sensor a dalah penundaan p engiriman permintaan dan penerimaan d ata d ari s ensor d alam
satuan milidetik. D alam m odel i ni, DTH11, s ensor s uhu dan k elembaban. R aspberry Pi m enerima d ata ini
melalui antarmuka G PIO. Nilai penundaan ini u ntuk 20 percobaan ditunjukkan p ada Gambar 7 .
Nilai rata-rata penundaan ini a dalah 1814,4 m ilidetik. D eviasi standarnya adalah 2 38 m ilidetik.
Terlihat dari grafik, n ilai ini c ukup konstan, k ecuali untuk permintaan pertama. Nilai p engukuran p enundaan
yang p ertama b erbeda s ecara signifikan d engan n ilai berikutnya karena pada awalnya, sebelum m enyalakan
prototipe, terdapat k onfigurasi metode d an sinkronisasi w aktu semua komponen. Oleh k arena itu, ada
penundaan t ambahan. S elama percobaan k edua semua k omponen d isinkronkan dalam w aktu. Setelah itu,
pada percobaan s elanjutnya t idak t erjadi f luktuasi nilai penundaan yang tinggi. Penundaan B luetooth a dalah
penundaan p ermintaan dan p enerimaan d ata melalui a ntarmuka Bluetooth d alam m ilidetik. R aspberry PI
memiliki m odul Bluetooth i nternal yang mendukung B luetooth L ow E nergy ( BLE). Standar ini b eroperasi
pada 2,4 G Hz d an i tu

Machine Translated by Google
28 CMC, 2022, jilid 70, no.1
kecepatan transfer maksimum adalah 1 M bit/detik, n amun nilai rata-rata d alam praktiknya a dalah 0,27 M bit/
detik. D alam p latform ini, satu Raspberry Pi s ebagai master Bluetooth m engirimkan permintaan ke budak
Bluetooth yang koneksinya telah dibuat. J umlah data d ari s ensor yang d i request kurang lebih 2 00 b yte. N ilai
penundaan i ni untuk 2 0 percobaan d itunjukkan p ada Gambar 9 . Nilai rata-rata p enundaan ini adalah 7 1,2
milidetik. D eviasi s tandarnya adalah 2 2,9 milidetik. N ilai i ni tidak stabil dan s angat b ervariasi.
3000
2800
2600
2400
2200
2000
1800
1600
1400
Pen1u2n0da0a n
1000
800
600
400
200
0
1 2 3 4 5 6 7 8 9 10 11 1 2 1 3 14 15 16 17 18 19 20
Jumlah p ercobaan
Keterlambatan p embacaan s ensor Penundaan Bluetooth
Gambar 7 : Pengukuran penundaan u ntuk b agian I oT ( Pembacaan s ensor dan p enundaan B luetooth)
Penundaan SDN adalah p enundaan y ang t erjadi saat m elewati virtual O pen v Switch.
Raspberry Pi (IOT Hub) t erhubung ke R aspberry Pi ( broker W eb) l ain melalui R aspberry P i p erantara yang
merupakan OvS v irtual. Switch m enghubungkan d ua h ost m elalui p ort E thernet. Raspberry P i m endukung
100 B ase Ethernet, yaitu kecepatan t ransfer melalui p ort i ni maksimal 1 00 M bps. Switch i ni hanya m empunyai
dua n ilai d alam tabel routingnya. Dua h ost berkomunikasi s atu s ama l ain melalui W ebSockets, dan j umlah
data dalam s atu p esan s ekitar 1 k ilobyte. Nilai penundaan ini untuk 2 0 percobaan d itunjukkan pada Gambar
10. Nilai r ata-rata p enundaan i ni adalah 4 ,5 milidetik. D eviasi standarnya a dalah 2,1 m ilidetik. N ilai ini stabil
dan t idak bervariasi b anyak. H anya pada permintaan pertama, p enundaannya terasa l ebih l ama.
Penundaan W ebSocket t erjadi ketika k ami m engirim permintaan dari s erver web ke broker dan m enerima
respons. Broker d an server web b erkomunikasi melalui p rotokol WebSocket. P enundaan sudah d iukur saat
koneksi dibuat. Perlu d iperhatikan b ahwa d alam percobaan i ni, server web berada di jaringan lokal. Volume
data pesannya juga sekitar 1 k ilobyte. Nilai penundaan i ni selama 2 0 kali percobaan d itunjukkan pada
Gambar 1 0. Nilai r ata-rata p enundaan ini adalah 1 4,05 m ilidetik. D eviasi standarnya a dalah 6 ,6 m ilidetik. Nilai
ini cukup s tabil dan sedikit bervariasi, namun t erkadang b isa jauh l ebih lama karena b erbagai alasan.
Penundaan W eb a dalah penundaan ( diukur d alam milidetik) y ang t erjadi k etika k lien web membuat
permintaan dan menerima r espons d ari server w eb. P ermintaan dibuat m enggunakan protokol HTTP, d an
responsnya berukuran 1 k ilobyte. Perlu d icatat bahwa k lien web dan s erver web berada di jaringan internal
yang s ama. N ilai p enundaan i ni untuk 20 p ercobaan ditampilkan

Machine Translated by Google
CMC, 2 022, jilid 70, no.1 29
pada G ambar 8. N ilai r ata-rata penundaan ini adalah 5 ,55 m ilidetik. Deviasi s tandarnya a dalah 1 ,8 milidetik. Nilai i ni t idak
berkelanjutan.
50
40
30
Penundaa2n 0
10
0
1 2 3 4 5 6 7 8 9 10 1 1 12 1 3 1 4 1 5 1 6 1 7 1 8 1 9 2 0
Jumlah percobaan
penundaan S DN Penundaan WebSocket Penundaan j aringan
Gambar 8 : Pengukuran penundaan bagian SDN (SDN, WebSocket, dan p enundaan Web)
Jadi jika kita j umlahkan semua penundaan ini, untuk percobaan sebelumnya, kita mendapatkan p lot b erikut pada
Gambar. 9 dari total penundaan E 2E, yaitu penundaan dari saat p engguna klien w eb mengklik t ombol p ermintaan d ata
sebelum m enerimanya di t abel di klien w eb. Total p enundaan rata-rata adalah 1 909,6 m ilidetik dan s tandar deviasinya adalah
251,4 milidetik. N amun terlihat dari gambar, s etelah permintaan p ertama, n ilai penundaannya c ukup stabil.
3450
3300
3150
3000
2850
2700
2550
2400
2250
2100
1950
1800
Pen1u6n5da0a n
1500
1350
1200
1050
900
750
600
450
300
150
0
1 2 3 4 5 6 7 8 9 10 11 12 1 3 1 4 1 5 1 6 1 7 1 8 1 9 2 0
Jumlah percobaan
Total (md) penundaan E2E (Total)
Gambar 9 : T otal p enundaan E2E p ada platform IoT berbasis S DN y ang diusulkan
Terlihat d ari plot, y ang paling tinggi d iantara semua d elay adalah d elay-delay baca sensor d alam membaca data dari
sensor. Y ang tertinggi k edua a dalah penundaan Bluetooth—penundaan d alam pertukaran

Machine Translated by Google
30 CMC, 2 022, jilid 7 0, no.1
pesan melalui protokol Bluetooth. Menurut b agian I oT, penundaannya a dalah 71.2 + 1814.4 = 1885.6 m ilidetik s edangkan
penundaan bagian SDN hanya 1909.6–1885.6 = 24 milidetik.
Namun p ada p ercobaan i ni web client dan web s erver berada pada jaringan internal.
Klien sebenarnya akan m engakses s erver j arak j auh dari I nternet. Hal i ni akan m engakibatkan penundaan y ang l ebih tinggi.
Oleh karena itu, u ntuk m emeriksanya, s erver web d ikerahkan pada web hosting jarak j auh H eroku dan k lien terhubung
melalui jaringan seluler 4 G. G ambar 10 menunjukkan sistem p emantauan penundaan u ntuk platform I oT berbasis S DN.
Terlihat d ari gambar, s emua p enundaan kurang lebih s ama j ika d ibandingkan dengan j aringan internal ( localhost), kecuali
penundaan Web d an WebSocket.
Gambar 1 0: S istem pemantauan penundaan untuk p latform I oT berbasis S DN ( server w eb diterapkan p ada hosting w eb
jarak jauh Heroku dan klien t erhubung melalui jaringan s eluler 4G)
Perbandingan penundaan w eb (Heroku vs. Localhost) digambarkan pada Gambar 1 1. Dalam h al i ni,
nilai rata-rata p enundaan adalah 1 41,3 m ilidetik d an s tandar deviasinya adalah 73,3 m ilidetik.
450
400
350
300
250
200
Pen1u5nd0aan
100
50
0
1 2 3 4 5 6 7 8 9 10 11 1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 2 0
Jumlah p ercobaan
Heroku ( Penundaan web) Localhost ( penundaan w eb)
Gambar 1 1: P erbandingan p enundaan web (Heroku vs. L ocalhost)

Machine Translated by Google
CMC, 2022, j ilid 7 0, n o.1 31
Perbandingan p enundaan W ebSocket ( Heroku v s. L ocalhost) digambarkan p ada Gambar 1 2.
120
100
80
60
Pen4un0daan
20
0
1 2 3 4 5 6 7 8 9 10 11 1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 2 0
Jumlah percobaan
Heroku ( penundaan W ebSocket) Localhost ( penundaan WebSocket)
Gambar 1 2: P erbandingan penundaan WebSocket ( Heroku v s. Localhost)
Sebagai hasil dari p engujian platform IoT b erbasis SDN, k ami m enemukan b ahwa p enggunaan teknologi
SDN m emastikan persyaratan yang diperlukan untuk penundaan transmisi data penting. Menurut m etode y ang
diusulkan, u ntuk m engurangi penundaan di b agian IoT, p erlu untuk memilih sensor s uhu dan kelembaban d engan
parameter teknis t erbaik u ntuk m embaca d an m emproses informasi dengan c epat. Solusi i ni akan meningkatkan
parameter kualitas layanan s ecara s ignifikan.
Dalam k arya ini, SDN d iimplementasikan untuk Internet of T hings b erbasis komputer papan tunggal.
Platform i ni m erupakan b ukti k onsep (PoC) dan fokus p ada implementasi kinerja, k emungkinan adanya i de d an
analisis s istem. N amun, s olusi akhirnya b isa sangat b eragam, s esuai dengan k ebutuhan yang berbeda. S aat
membuat solusi a khir, p enting untuk m empertimbangkan b erbagai p arameter y ang memungkinkan
pengorganisasian arsitektur s ecara keseluruhan d an dalam m emecahkan m asalah spesifik d engan l ebih b aik
dan lebih cerdas. S aat merancang jaringan yang d itentukan perangkat lunak u ntuk I oT, s eseorang harus
memperhatikan j enis data yang direncanakan u ntuk dikirimkan.
Klasifikasi data real-time dan u nreal-time serta volumenya s angatlah penting. J ika s istem m enyediakan
transmisi d ata real-time, m aka perlu menjaga QoS yang disediakan oleh jaringan k omunikasi. Bagian IoT
diperlukan untuk m emastikan p rotokol transmisi d ata kabel a tau nirkabel b erkecepatan t inggi. D alam k asus k ami,
sensor suhu DHT11 p erlu diganti d engan s ensor yang lebih c epat, y ang akan mengurangi penundaan E2E.
SDN menawarkan s olusi t erbaik d an n yaman u ntuk m emastikan Q oS, justru karena k emampuannya
mengendalikan j aringan secara terprogram. S eorang administrator d apat secara d inamis dan fleksibel m enentukan
kebijakan jaringan u ntuk m engalokasikan sumber daya jaringan k e aliran prioritas y ang berbeda. M isalnya,
administrator dapat memilih t hroughput jaringan u ntuk aliran prioritas, waktu tunda jalur, atau kriteria l ain sebagai
jalur k omunikasi optimal u ntuk aliran data tertentu. Itulah sebabnya di bagian p ekerjaan selanjutnya, kami
menawarkan pendekatan u ntuk perutean optimal a liran data dari berbagai k elas I oT b erdasarkan kriteria k ualitas
layanan untuk j aringan skala besar ( dengan sejumlah besar s akelar S DN).

QoS vs Manajemen Hemat Energi
Manajer L alu L intas Manajer T opologi
Blok pengoptimal
kitsitatS
Machine Translated by Google
32 CMC, 2022, j ilid 7 0, n o.1
4 Pendekatan E fisiensi Energi p ada SDN 4 .1
Pendekatan Efisiensi E nergi P roporsional pada P latform IoT B erbasis SDN
Karena b iaya energi berkontribusi s ignifikan terhadap total biaya jaringan, e fisiensi energi m erupakan persyaratan
penting ketika m erancang m ekanisme jaringan modern, terutama dalam i nfrastruktur I oT. Namun, mengembangkan solusi
hemat e nergi adalah t ugas yang k ompleks, karena t erdapat t rade-off antara efisiensi energi d an k inerja j aringan [ 36]. SDN
memastikan k emampuan program e lemen j aringan d engan memisahkan bidang kendali dan b idang penerusan. K arena
perangkat SDN dapat diprogram dan dikelola, s akelar jaringan y ang diusulkan berdasarkan s atu papan d an t autan d apat
memasuki k ondisi d aya rendah dalam m ode tidur, d an a rsitektur perangkat dapat dirancang untuk m emiliki beban a ktual
berdasarkan konsumsi e nergi yang p roporsional.
Kami m engusulkan pendekatan untuk m erancang struktur SDN y ang h emat e nergi s ehubungan d engan beban j aringan
yang dihasilkan o leh perangkat IoT. P endekatan ini m endukung kompromi antara efisiensi energi d an k inerja. A rsitektur SDN
hemat e nergi untuk komunikasi IoT digambarkan p ada Gambar 13.
Lalu lintas Subgraf Status Topologi
Informasi
Pesawat
Hidupkan/matikan
Sakelar/tautan
Modul Lampu Sorot
Pengontrol Lampu Sorot
Aplikasi
API
Arsitektur
Mode t idur
Modus aktif
Pesawat Sakelar O vS
berdasarkan
Rasberi Pi
Gambar 1 3: Arsitektur SDN e fisiensi energi untuk komunikasi IoT (garis putus-putus m erah adalah blok p rogram yang kami
usulkan)
Prinsip pendekatan yang d iusulkan adalah s ebagai berikut. Dengan dukungan p engontrol SDN, s truktur j aringan
dipantau dan d ikelola s ecara terpusat. Blok p engoptimal d ikembangkan p ada pengontrol SDN u ntuk m engumpulkan s tatistik
dari sakelar O vS tentang topologi jaringan dan beban s akelar. Berdasarkan statistik terkini tentang keadaan jaringan,
keputusan adaptif dibuat untuk m embangun t opologi jaringan y ang o ptimal s ehubungan d engan kriteria QoS d an k onsumsi
energi. Dalam kondisi b eban j aringan rendah yang mendukung pendekatan ini, pengontrol SDN, b erdasarkan data y ang
diterima dari blok pengoptimal j aringan, a kan m emutuskan untuk m embuat g rafik ( topologi) d engan jumlah tautan d an sakelar
aktif yang lebih s edikit, s edangkan beban j aringan t inggi a kan m eningkatkan j umlah s akelar a ktif d an h ubungan di antara
mereka dalam g rafik.
Berdasarkan model p erutean yang dijelaskan d i a tas, p enyesuaian biaya j alur dapat dilakukan dengan menggunakan korektif

Machine Translated by Google
CMC, 2022, j ilid 7 0, no.1 33
bobot untuk memperhitungkan s eberapa besar p enundaan a tau kehilangan p aket yang penting u ntuk aliran IoT
tertentu. Dengan c ara ini, kita d apat menyesuaikan parameter ini a gar sesuai d engan persyaratan k ualitas
layanan dari setiap aliran. Oleh k arena i tu, penyeimbangan b eban antar t autan dapat dilakukan sehingga l ebih
sedikit s akelar y ang t erlibat dan s akelar y ang menganggur dapat dialihkan k e mode t idur u ntuk meningkatkan
efisiensi e nergi jaringan secara k eseluruhan. Ketika b eban dari perangkat IoT b ertambah d an Q oS menurun,
keputusan otomatis d ibuat u ntuk m engaktifkan sakelar tidur d an m engalihkannya ke mode a ktif. Beban
didistribusikan ulang m enggunakan model m atematika b erikut.
Kami menyajikan b agian SDN p ada platform IoT d alam bentuk grafik b erbobot G = (N,M), di m ana N
adalah j umlah sakelar O vS berdasarkan R asberry Pi d an N i ÿ N adalah sakelar ke-i O vS . K ami juga m enyajikan
saluran mij ÿ M antara sakelar N i d an Nj. P arameter Bi,j merupakan t hroughput yang menghubungkan s aklar
OvS N i d an Nj. B iarkan v ariabel b iner Vi d an L ij m enunjukkan k eadaan saklar N i d an s aluran mij s eperti
1, jika OvS Ni aktif 0 ,
Vi =
sebaliknya
1, jika s aluran mij aktif 0 ,
Lij =
sebaliknya
Pi adalah k onsumsi energi O vS Ni d an Cij a dalah konsumsi e nergi s aluran m ij y ang d iukur dalam kilowatt a tau
kilojoule p er jam.
Lalu lintas jaringan d iwakili oleh s ekumpulan aliran F, d i m ana f ÿ F didefinisikan s ebagai f = (sr, ds, ÿf), di
mana sr d an ds a dalah saklar OvS sumber d an t ujuan, dan ÿ f a dalah laju aliran, diukur d alam byte p er d etik.
1, jika aliran f m elewati t epi eij 0,
fij =
sebaliknya
1, ÿmin ÿ ÿ ÿ ÿmaks
Lij =
0, sebaliknya
dimana ÿ min d an ÿmax adalah beban saluran m inimum d an m aksimum untuk menjaga t rade-off antara k inerja
dan efisiensi e nergi.
Fungsi m ultiobjektif (Persamaan (1)) meminimalkan j umlah k onsumsi e nergi s akelar dan s aluran. Ekspresi
matematis pertama dari f ungsi tujuan, jumlah f ij ·Cij, m engacu pada t otal konsumsi e nergi s emua a liran yang
menggunakan s aluran mij. Ekspresi m atematika kedua a dalah jumlah t otal konsumsi e nergi s emua s witch OvS
aktif d i j aringan S DN. Fungsi tujuan secara kolektif meminimalkan j umlah y ang terkena b atasan yang dijelaskan
di b awah.
ÿ ÿ
menit Lij · C ij + Vi · Pi (4)
ÿ ÿ eij ÿZi ÿ
tunduk pada fij · ÿ f ÿ B ij, ÿ mij (5)
ÿf

Machine Translated by Google
34 CMC,  2022, j ilid 7 0,  no.1
(6)
| fij  =  ÿf | fij,Ni&Nj =  s r,Ni&Nj  = d s |     |
| ---------- | ----------------------------- | --- |
ÿf
| fkj  =  fiq,Nk  =  sr,Nq  = d s,  ÿmkj, ÿ miq |     | (7)  |
| --------------------------------------------- | --- | ---- |
| fij ÿ  V  j d an  fji ÿ   Vj,  ÿNj ÿ   N      |     | (8)  |
| fij ÿ  V  jÿNj  ÿ N                           |     | (9)  |
| Vi ÿ                                          |     | (10) |
[fij  +  fji], ÿ Ni ÿ   N
ÿf
| Lij  ÿ V  i,Lij  ÿ V  | jÿNi | (11) |
| --------------------- | ---- | ---- |
Dalam ( Persamaan  (4)),  dinyatakan  bahwa  laju  aliran t otal a ntara k edua s akelar  tidak  boleh  melebihi t hroughput
saluran B  i,j.  Persamaan.  (5) d an ( 6) k eadaan  konservasi a liran, y ang m  enyatakan  tidak  ada  aliran y ang  tercipta  atau
hilang d alam  jaringan. K  endala d alam P  ersamaan.  (6) m  enyatakan b ahwa  jumlah  arus y ang  masuk  dan  keluar d ari
saklar-saklar y ang b ukan m  erupakan  tujuan m  aupun s umber  aliran  harus  genap.  Kendala u ntuk  Persamaan.  (4)
memastikan b ahwa  aliran  yang b erasal d ari  sakelar s umber  harus  meninggalkan  jaringan d i s akelar  tujuan. K  endala
untuk P  ersamaan.  (8)–(10)  mendukung k orelasi  antara s akelar  dan  saluran m  enggunakan  variabel s tatus s akelar d an
variabel s aluran  aliran.  Batasan 8  d an  9 m  enyatakan b ahwa  tidak  boleh  ada a liran  yang m  enggunakan  saluran y ang
terhubung k e s akelar  yang t idak a ktif, s edangkan b atasan 1 0  menyatakan b ahwa  jika t idak  ada  aliran y ang  melewati
saluran y ang  terhubung  ke  sakelar t ertentu, m  aka  sakelar  tersebut  akan  mati. K  endala d alam  Persamaan.  (11)
menyatakan  bahwa  saluran  yang t erhubung k e  saklar  non-aktif  harus  dinonaktifkan.  Mengingat  formulasi d an  parameter
model,  hasil p engoptimal  adalah d aftar l ink d an s akelar  aktif  untuk s etiap  aliran f  ÿ  F .
Oleh  karena  itu, p endekatan  kami  memberikan p enghematan y ang  signifikan d alam k onsumsi e nergi s ecara k eseluruhan
jaringan  sambil m  encapai  kinerja o ptimal u ntuk  memenuhi p ersyaratan  QoS y ang  diperlukan.
| 4.2 H  asil E  | ksperimen |     |
| -------------- | --------- | --- |
Raspberry  Pi 3   dapat d itenagai d engan  catu d aya  sebesar  5 V  olt. U  ntuk p enggunaan n ormal,  Raspberry  Pi  hanya
menggunakan  P =  2 ,25 W   d an  konsumsi e nergi E   =   8,1  kilojoule  per j am [ kJ/h].  Misalnya, j ika j aringan k ami  terdiri  dari
7  sakelar O  vS b erbasis  Raspberry  Pi, k onsumsi  daya d alam m  ode  tidur d apat  diabaikan.  Konsumsi e nergi  dalam  mode
tidur  sangat k ecil.
Total k onsumsi e nergi  jaringan  per h ari  dihitung d engan P  ersamaan.  (12):
24
(12)
| Jaringan E  |  =  (E ·   n)i [ kJ/jam], |     |
| ----------- | ------------------------- | --- |
saya=saya+1
dimana n -jumlah s akelar S  DN a ktif  berdasarkan R  aspberry  Pi, E  –konsumsi e nergi  dari  satu s akelar S  DN.

Machine Translated by Google
CMC, 2 022, jilid 70, no.1 35
Penghematan energi d ihitung dengan P ersamaan. ( 13).
= 1 ÿ Jaringan d engan solusi k ami · 100 (13)
Penghematan keenergi
Enetworktanpa solusi k ami
Untuk p engujian eksperimental kami, k ami m empertimbangkan t opologi jaringan berdasarkan k omputer papan t unggal.
Topologi i ni t erdiri d ari 7 Open vSwitches, 1 pengontrol F loodlight SDN, dan 6 l alu lintas IoT
generator (G1, G2, G3, G4, G5, d an G6). Testbed SDN e ksperimental d igambarkan pada Gambar 14.
G4
G2
2 4
G6
1 7 6
G1
3 5
G3 G5
– Lampu S orot S DN – Buka vSwitch – Generator lalu lintas I oT
Pengendali Oranye (Rasberi Pi 3) (Rasberi Pi 3)
Pi Perdana
Gambar 14: T estbed e ksperimental SDN b erdasarkan komputer papan t unggal
Kami m enghasilkan beban berbeda selama 2 4 j am di jaringan. U ntuk m encapai beban r endah p ada
jaringan, kami tidak m enghasilkan b eban d engan b eberapa g enerator G1, G 2, G 3, G4, G 5 dan G 6. Kami
memperkirakan k onsumsi energi d engan dan tanpa s olusi e fisiensi energi kami u ntuk l ayanan a
beban t ertentu. J adi, r ata-rata beban j aringan p er hari digambarkan pada G ambar 15. Jumlah y ang aktif
Switch S DN berbasis Raspberry P i per h ari digambarkan p ada Gambar 16. Konsumsi energi
perbandingan d alam kilojoule p er hari d itunjukkan pada G ambar 17.
Hasil e ksperimen menunjukkan b ahwa total k onsumsi e nergi jaringan tanpa solusi k ami a dalah E networktanpa solusi
kami = 1 361 [kJ/h] dan dengan s olusi kami ( pendekatan e fisiensi energi)
= 632 [kJ/jam]. Kemudian p enghematan e nergi setelah m enyadari p endekatan kami a dalah
Jaringan dengan s olusi k ami
632
= (1 ÿ )· 1 00% = 53,56%.
Penghematan k eenergi 1361
Eksperimen y ang dilakukan pada t opologi SDN n yata b erdasarkan 7 k omputer papan tunggal Rasp-berry Pi 3, switch,
dan lalu lintas I oT menunjukkan b ahwa pendekatan kami t idak hanya menghemat h ingga 5 3,56% dari
energi pada volume l alu lintas rendah, tetapi juga m emastikan Q oS untuk a plikasi I oT.

Machine Translated by Google
36 CMC, 2 022, jilid 7 0, no.1
Ringkasan pendekatan y ang d ibahas u ntuk m engurangi k onsumsi energi dan meningkatkan
kualitas l ayanan d alam jaringan modern d itunjukkan pada T ab. 1. Pekerjaan kami b erbeda d ari
pekerjaan sebelumnya dalam hal m etode pengukuran penundaan, a lokasi s umber daya, dan
implementasi prototipe.
100
95
90
85
80
75
70
65
60
55
50
45
Beban
40
35
30
25
20
15
10
5
0
1 2 3 4 5 6 7 8 9 10 1 1 12 1 3 1 4 1 5 1 6 1 7 1 8 1 9 20 2 1 2 2 2 3 2 4
Waktu [jam]
Gambar 15: Rata-rata beban j aringan per h ari
9
8
7
6
5
4
3
Jumlah
2
1
0
1 2 3 4 5 6 7 8 9 10 1 1 12 13 14 15 16 1 7 18 19 20 21 22 23 24
Waktu [ jam]
Tanpa s olusi kami Dengan s olusi kami
Gambar 1 6: Jumlah switch SDN a ktif berdasarkan Raspberry Pi per h ari

Machine Translated by Google
CMC, 2022, j ilid 70, no.1 37
60
57
54
51
48
45
42
39
36
33
30
27
24
21
18
15
Ko12n sumsi
9
6
3
0
1 2 3 4 5 6 7 8 9 1 0 1 1 12 13 14 15 16 17 18 19 20 21 22 23 24
Waktu [ jam]
Tanpa s olusi kami Dengan solusi kami
Gambar 1 7: Perbandingan konsumsi energi dalam k ilojoule per j am selama s ehari
Tabel 1: P erbandingan k arya-karya terbaru
Deskripsi R eferensi Bandingkan dengan p ekerjaan kita
[37] Pendekatan ini d idasarkan pada manajemen Berbeda dengan p ekerjaan kami, p enulis di [ 37]
sumber daya s erver u ntuk m engurangi mengusulkan u ntuk m enghemat energi d engan
kemacetan dan e nergi dalam j aringan mematikan server tergantung pada bebannya
VoIP. S elain itu, p enulis m enggunakan s witch menggunakan s akelar O vS. K ami mengusulkan
OpenFlow daripada switch t radisional untuk melakukan p emantauan t erpusat dan
dalam i nfrastruktur j aringan. Hasilnya, h al i ni pengelolaan struktur j aringan m enggunakan
secara e fektif m encegah kemacetan, pengontrol S DN logika c anggih untuk
dan j umlah p eralatan aktif dalam j aringan mematikan s akelar, t ermasuk y ang d ibangun
diminimalkan pada platform Raspberry. Untuk tujuan ini, k ami telah
mengembangkan dan b erhasil
mengimplementasikan pengoptimal b lok d i
pengontrol.
(Lanjutan)

Machine Translated by Google
38 CMC, 2022, jilid 7 0, n o.1
Tabel 1 : Lanjutan
Deskripsi R eferensi [38] Perbandingan d engan p ekerjaan
Strategi yang d iusulkan oleh p enulis adalah kami Berbeda d engan p ekerjaan r outing
menggabungkan p erutean t erpendek sebelumnya yang berfokus pada masalah
berdasarkan prioritas d an perencanaan aliran minimalisasi e nergi d i jaringan p usat data, kami
eksklusif d alam jaringan p usat data y ang bertujuan u ntuk mengoptimalkan k onsumsi energi d i
ditentukan p erangkat lunak. I ni m emiliki Platform I oT B erbasis S DN menggunakan Raspberry Pi 3 .
peningkatan e fisiensi e nergi y ang j elas Eksperimen y ang d ilakukan pada topologi SDN/
untuk mentransfer file b esar d i jaringan B Cube. IoT n yata berdasarkan komputer papan t unggal
Dalam hal ini, perutean E XR yang diprioritaskan menunjukkan b ahwa pendekatan kami tidak h anya
kira-kira 5%–35% l ebih hemat e nergi dibandingkan menghemat hingga 53,56% e nergi p ada intensitas
strategi u mum l ainnya. lalu lintas rendah, namun juga m emberikan
jaminan Q oS u ntuk a plikasi I oT b erdasarkan sistem
pemantauan penundaan E 2E baru. . Penulis a rtikel
[38] h anya membahas prioritas arus untuk
menemukan jalur transmisi y ang l ebih h emat
energi.
Hasil yang d iperoleh juga t idak d iterapkan dalam
praktik, s ehingga m enimbulkan k eraguan m engenai
penerapan dan manfaatnya.
[39] Pendekatan y ang d iusulkan oleh p enulis Berbeda d engan p enelitian yang a da [39], d i mana
secara efisien m engurangi e nergi infrastruktur penulis hanya bekerja d engan p enundaan E 2E,
sekaligus m embangun r ute dinamis d engan kami mengevaluasi p enundaan y ang ditimbulkan
menggabungkan aliran d i seluruh s umber oleh setiap k omponen infrastruktur I oT, m ulai
daya j aringan yang d iaktifkan. Dengan strategi dari sensor, i nti SDN, b roker IoT, d an pelanggan
kesadaran energi i ni m endukung perlunya layanan IoT.
melakukan kompromi berdasarkan jenis aliran Pendekatan ini akan m engidentifikasi hambatan
antara jaminan l ayanan, o ptimalisasi alokasi dalam i nfrastruktur yang m enyebabkan penurunan
sumber daya, dan pengurangan parameter Q oS d an secara o tomatis m emutuskan
konsumsi e nergi untuk m eningkatkan kinerja apakah akan m enghilangkan hambatan t ersebut atau
jaringan s ecara keseluruhan. secara o ptimal m embangun t opologi untuk
mengurangi k onsumsi e nergi jaringan.
5. Kesimpulan
Harga penerapan yang b esar d an persaingan p asar y ang t inggi m enyebabkan penyedia l ayanan IoT seringkali t idak
mendapatkan minat yang m emadai dari investasi m ereka. U ntuk m engatasi masalah i ni, kami menawarkan solusi baru bagi
usaha kecil dan m enengah yang m emungkinkan mereka m emasuki pasar I oT dengan i nvestasi y ang jauh l ebih r endah. S olusi
yang d iusulkan m emungkinkan penggelaran j aringan yang d apat diprogram s esuai p ermintaan untuk berbagai aplikasi I oT,
termasuk l ayanan y ang s angat penting. Kami m engembangkan platform b ukti k onsep yang m enghubungkan b erbagai
perangkat akhir I oT d an m enyediakan mekanisme y ang f leksibel d an terukur u ntuk kontrol Q oS E 2E u ntuk aplikasi y ang
sangat penting. P latform yang diusulkan t erdiri d ari seperangkat k omputer p apan t unggal y ang h emat e nergi dan biaya s erta
menggunakan f itur unik SDN, seperti sifat berbasis aliran, dan fleksibilitas jaringan u ntuk memenuhi Q oS.

Machine Translated by Google
CMC, 2 022, jilid 7 0, n o.1 39
persyaratan setiap a liran IoT d i jaringan. K euntungan u tama dari prototipe j aringan SDN y ang dikembangkan a dalah
biaya r endah dan ketersediaan implementasi, y ang penting untuk p elatihan spesialis d i bidang j aringan yang
ditentukan perangkat lunak dalam proses t ujuan p endidikan, pelatihan dan p enelitian.
Dalam m akalah i ni, p ertama-tama kami m empresentasikan d an m enerapkan metode u ntuk m engukur
penundaan yang diperkenalkan o leh setiap k omponen i nfrastruktur IoT, m ulai dari sensor, i nti S DN, broker I oT,
hingga pelanggan IoT. Kami juga m empresentasikan p endekatan h emat energi untuk platform IoT b erbasis SDN
yang sebanding d engan intensitas lalu lintas I oT. P endekatan i ni m enghemat e nergi dengan s ecara d inamis
menyalakan sejumlah minimum p erangkat jaringan u ntuk mengirimkan lalu l intas sehubungan dengan b eban j aringan
daripada terus-menerus membiarkan s emua s aklar tetap m enyala, s eperti p ada jaringan saat ini.
Keterbatasan p ekerjaan i ni adalah t hroughput saluran k omunikasi p ada level s witch y ang dirancang a dalah 100
Mbps, karena switch dirancang berdasarkan board R aspberry P i 3 m enggunakan Open v Switch (OvS). R aspberry P i
hanya mendukung 100 Base E thernet. Oleh k arena i tu kedepannya kami a kan menguji switch j aringan IoT b ackbone
ZODIAC F X yang memiliki t hroughput 1000 Mbps.
Pekerjaan k ami di masa depan adalah m engembangkan model perutean QoE (Kualitas P engalaman) yang
hemat energi untuk jaringan berbasis t ujuan yang d itentukan p erangkat lunak d i masa depan. K ebaruan model ini
adalah bahwa m etrik r ute berorientasi Q oE adaptif a kan digunakan untuk memilih j alur t ransmisi optimal, berdasarkan
model matematika korelasi Q oS/QoE yang dikembangkan sehubungan dengan p arameter fungsional p emanfaatan
node jaringan. Sebagai hasil dari implementasi perangkat lunak p ada p engontrol S DN/IBN, akan dimungkinkan untuk
mempertahankan k ompromi antara kualitas p engguna layanan y ang berorientasi p ada intensitas y ang diinginkan,
pemanfaatan j aringan, d an efisiensi e nergi dengan m enempatkan node y ang menganggur ke mode h emat energi.
Secara khusus, kami a kan m enerapkan pendekatan ini p ada switch Z ODIAC F X/GX S DN a sli, yang terbuka u ntuk
peningkatan logika manajemen jaringan. K ami sudah m emiliki b eberapa pencapaian sukses d ari prototipe ini, y ang
akan segera kami u las dalam k arya kami s elanjutnya.
Pernyataan P endanaan: Penelitian i ni d idukung o leh Proyek U kraina No. 0120U102201 “Pengembangan m etode
dan s arana p erangkat lunak-perangkat keras terpadu untuk penerapan j aringan informasi d an k omunikasi multiguna
berbasis t ujuan yang hemat energi”.
Konflik Kepentingan: P ara p enulis menyatakan b ahwa mereka tidak memiliki k onflik k epentingan untuk d ilaporkan
mengenai p enelitian ini.
Referensi
[1] PKR M addikunta, T R G adekallu, R. K aluri, G . Srivastava, R M P arizi d kk., “Komunikasi r amah l ingkungan d alam
jaringan I oT menggunakan a lgoritma o ptimasi h ibrid,” Computer C ommunications, vol. 1 59, h lm.97–107, 2 020.
[2] PKR M addikunta, G . S rivastava, T R Gadekallu, N . Deepa dan P . Boopathy, “Model prediktif u ntuk masa pakai baterai
di j aringan I oT,” IET I ntelligent T ransport Systems, v ol. 1 4, tidak. 1 1, hlm.1388–1395, 2 020.
[3] Q. P ham, S . M irjalili, N . K umar, M . A lazab d an W . Hwang, “Algoritma pengoptimalan paus d engan aplikasi u ntuk
alokasi s umber daya di jaringan nirkabel,” IEEE T ransactions on V ehicular T echnology, v ol. 6 9, tidak. 4 , hal.4285–
4297, 2020.
[4] PKR M addikunta, G . S rivastava, TR G adekallu, N . Deepa dan P. B oopathy, “ Model prediktif u ntuk masa pakai b aterai
di j aringan I oT,” IET Intelligent T ransport S ystems, v ol. 1 4, tidak. 1 1, hlm.1388–1395, 2020.
[5] W. A nwaar d an M A Shah, “ Komputasi hemat energi: Perbandingan raspberry pi d engan perangkat m odern,” Jurnal
Internasional Komputer dan T eknologi Informasi, v ol. 4 , t idak. 2 , h al.410–413, 2 015.
[6] H. Kim, J . K im d an Y . K o, “ Mengembangkan p engujian a liran terbuka yang h emat b iaya u ntuk jaringan y ang d itentukan
perangkat l unak s kala k ecil,” di P roc. ICACT, Pyeongchang, K orea S elatan, hlm. 7 58–761, 2 014.

Machine Translated by Google
40
CMC,  2022, j ilid  70,  no.1
[7]  QH N  guyen,  N.  Ha D  o d an  H. L e, “ Pengembangan s witch b erbasis S  DN  yang  mampu  menyediakan Q  oS d an h emat b iaya  untuk
| komunikasi I oT,”  di P  | roc.  ATC, K  | ota  Ho C  hi  Minh, h lm. 2 20–225, 2 018. |     |     |
| ------------------------ | ------------- | ------------------------------------------- | --- | --- |
[8]  V. G  upta,  K. K  aur  dan S  .  Kaur, “ Mengembangkan s witch j aringan y ang  ditentukan p erangkat  lunak b erukuran  kecil d an  berbiaya
rendah m  enggunakan r aspberry p i,” d alam N  ext-Generation N  etworks,  Singapura: S  pringer, h lm. 1 47–152, 2 018.
| [9]  R. B  olla, C  . L ombardo, R  | .  Bruschi d an S  | .  Mangialardi, “ dropv2: E  | fisiensi e nergi m  | elalui  jaringan |
| ----------------------------------- | ------------------ | ---------------------------- | ------------------- | ---------------- |
virtualisasi  fungsi,”  Jaringan I EEE, v ol.  28,  tidak.  2,  hal. 2 6–32,  2014.
[10] B  R  Dawadi, D  B  Rawat,  SR  Joshi  dan  MM K  eitsch,  “Menuju e fisiensi  energi d an p enerapan i nfrastruktur j aringan  ramah l ingkungan
di N  epal m  enggunakan p aradigma  jaringan  IPv6 y ang  ditentukan p erangkat  lunak,” T he  Electronic J ournal  of  Information S  ystems
| in D  eveloping C  | ountries, v ol.  86,  tidak.  1,  hal. e 12114, 2 020. |     |     |     |
| ------------------ | ------------------------------------------------------ | --- | --- | --- |
[11] M  J  Piran, S  . V  erma, V  G  Menon  dan  DY  Suh, “ Model o ptimasi  jangkauan t ransmisi  hemat e nergi u ntuk  internet  of t hings b erbasis
| wsn,” C  omputers,  Materials &  |   Continua,  vol. 6 7,  tidak. 3 ,  hal. 2 989– 3 007, 2 021. |     |     |     |
| -------------------------------- | ------------------------------------------------------------- | --- | --- | --- |
[12] S  . K  rishnamoorthy  dan K  .  Narayanaswamy,  “Alokasi d an  penugasan p engontrol S  DN  berdasarkan a lgoritma  salp g erombolan
multikriterion  yang k acau,” I ntelligent A  utomation &   S  oft C  omputing,  vol.  27,  tidak.  1,  hlm.89–102, 2 021.
[13] I . G  ravalos, P .  Makris,  K. C  hristodoulopoulos  dan  EA  Varvarigos,  “Perencanaan j aringan y ang e fisien  untuk i nternet o f t hings d engan
| batasan Q  oS,” I EEE I nternet o f  Things  Journal, v ol. 5 , t idak. 5 , h al.3823–3836, 2 018. |     |     |     |     |
| -------------------------------------------------------------------------------------------------- | --- | --- | --- | --- |
[14] M  .  Beshley, N  .  Kryvinska,  M. S  eliuchenko, H  . B  eshley, E  M  Shakshuki d kk., A  lgoritme  manajemen  “antrian c erdas”  QoS u jung  ke
ujung  dan m  ekanisme p rioritas  lalu  lintas  untuk  layanan  internet  pita s empit d i j aringan 4 G/5G,” S  ensor,  vol.  20,  tidak.  8,  hal.2324–
2354,  2020.
[15] S  . M  ath, P  . T am d an S  .  Kim, “ Pengarah l alu  lintas I oY r eal-time y ang  cerdas d i j aringan e dge  5G,”
| Komputer, M  aterial &  |  C  ontinua,  vol.  67,  tidak.  3, h al.3433–3450, 2 021. |     |     |     |
| ----------------------- | ---------------------------------------------------------- | --- | --- | --- |
[16] V  S  Naresh, S  S P  ericherla, P  .  Sita d an  S.  Reddi,  “Internet  dalam p erawatan k esehatan: A  rsitektur,  aplikasi,  tantangan, d an s olusi,”
Sains  dan T eknik  Sistem  Komputer, v ol.  35,  tidak.  6, h al.411–421, 2 020.
[17] H  . G  eng, J . Y  ao d an Y  .  Zhang, “ Algoritme p erlindungan  perutean k egagalan t unggal  di  SDN  hybrid
| jaringan,”  Komputer, M  | aterial &    Continua,  vol. 6 4,  tidak. 1 ,  hal.665–679, 2 020. |     |     |     |
| ------------------------ | ------------------------------------------------------------------ | --- | --- | --- |
[18] O  .  Sadio, I .  Ngom d an C  .  Lishou,  “Desain  dan p embuatan p rototipe j aringan  kendaraan y ang  ditentukan p erangkat  lunak,” I EEE
Transactions o n  Vehicular T echnology, v ol.  69, t idak.  1, h al.842–850, 2 020.
[19] D  B  Rawat d an  SR  Reddy, “ Arsitektur j aringan  yang  ditentukan p erangkat  lunak, k eamanan d an  efisiensi e nergi: S  ebuah  survei,”
| IEEE  Communications  Surveys &  |     |   Tutorials, v ol. 1 9,  tidak.  1, h al.325–346, 2 017. |     |     |
| -------------------------------- | --- | -------------------------------------------------------- | --- | --- |
[20] B  G A  ssefa  dan  Ö.  Özkasap, “ RESDN: M  etrik  dan m  etode  baru u ntuk  perutean h emat e nergi d alam j aringan y ang  ditentukan
perangkat  lunak,”  IEEE T ransactions o n  Network  and S  ervice  Management,  vol. 1 7,  tidak. 2 ,  hal.736–749, 2 020.
[21] A  . K  annan, S  .  Vijayan, M  .  Narayanan d an  M. R  eddiar,  “Mekanisme  routing a daptif d i  SDN  untuk  membatasi k emacetan,”  Desain
Sistem  Informasi d an A  plikasi  Cerdas, v ol.  862,  hlm.245–253, 2 019. h ttps://doi.org/10.1007/978-981-13-3329-3.
[22] J . W  ang,  O.  Kochan, K . P rzystupa d an  J. S u,  “Sistem  pengukuran i nformasi  untuk m  empelajari t ermokopel  dengan m  edan s uhu
| terkontrol,” M  easurement  Science R  |     | eview,  vol. 1 9,  tidak. 4 , h lm.161–169,  2019. |     |     |
| -------------------------------------- | --- | -------------------------------------------------- | --- | --- |
[23] H  . B  eshley, M  .  Kyryk, M  .  Beshley  dan O  .  Panchenko,  “Metode r ekayasa a rus i nformasi  dan  distribusi s umber  daya  dalam j aringan
| heterogen  4G/5G u ntuk  penyediaan l ayanan M  |     | 2M,” d i P  | roc. |     |
| ----------------------------------------------- | --- | ----------- | ---- | --- |
IDAACS-SWS,  Lviv,  Ukraina, h lm.229–233,  2018.
[24] A  . P  ryslupskyi, O  .  Panchenko, M  . B  eshley d an  M. S  eliuchenko, “ Peningkatan k inerja j aringan  peralihan  label m  ultiprotokol
menggunakan p engontrol y ang d itentukan p erangkat l unak,” d i P  roc.  CADSM, P  olyana, U  kraina, h lm.106–109, 2 019.
[25] M  .  Beshley, M  .  Seliuchenko, O  .  Panchenko, O  . Z yuzko  dan  I.  Kahalo,  “Analisis k inerja e ksperimental  dari s aklar d an  pengontrol
jaringan y ang  ditentukan p erangkat  lunak,” d i P  roc. T CSET, L viv-Slavske, U  kraina, h lm. 2 82–286, 2 018.

Machine Translated by Google
CMC, 2 022, jilid 70, n o.1 41
[26] M. Beshley, V . Romanchuk, M . S eliuchenko d an A. M asiuk, “ Investigasi metode a ntrian prioritas y ang dimodifikasi
berdasarkan pada test b ed jaringan v irtual,” d i P roc.CADSM, L viv, Ukraina, h al. 1–4, 2 015 .
[27] S. Jun, K . P rzystupa, M . B eshley, O. K ochan, H . B eshley dkk., “ Router d an g enerator lalu l intas b erbasis p erangkat lunak yang hemat
biaya u ntuk simulasi d an p engujian j aringan I P,” Electronics, v ol. 9 , tidak. 1, hal. 4 0–64, 2020.
[28] B. Li d an S. Yu, “ Penambangan k ata k unci untuk protokol p ribadi yang disalurkan m elalui w ebsocket,” di K omunitas IEEE
Surat kation, v ol. 2 0, t idak. 7, hlm.1337–1340, 2 016.
[29] E. Mallada, X . Meng, M . Hack, L . Zhang dan A. T ang, “Sinkronisasi jam jaringan t anpa kemiringan tanpa diskontinuitas:
Konvergensi d an k inerja,” T ransaksi I EEE/ACM pada Jaringan, v ol. 23, tidak. 5 , h lm.1619–1633, 2015.
[30] J. M ichaÿowska, A. Tofil, J . Józwik, J . Pytka, S. L egutko d kk., “Memantau r isiko komponen l istrik yang dikenakan p ada
pilot s elama o perasi p esawat ringan di medan elektromagnetik f rekuensi t inggi, ” S ensor, j ilid. 19, tidak. 24, hal.5537,
2019.
[31] R . K ochan, O . Kochan, M . Chyrka, S . Jun dan P . B ykovyy, “ Pendekatan pengembangan pembagi t egangan untuk v erifikasi m etrologi
ADC,” d i P roc. I DAACS-2013, B erlin, J erman, v ol. 1 , h al.70–75, 2013.
[32] DL Presti, C. Massaroni dan E . Schena, “ Kisi-kisi s erat optik untuk pengukuran kelembaban: A
ulasan,” IEEE Sens. J., v ol. 1 8, t idak. 22, h lm.9065–9074, 2018.
[33] A . Glowacz, “Diagnosis k esalahan b or tumbukan listrik menggunakan pencitraan termal,” P engukuran, vol. 171,
hal.108815, 2 021.
[34] S. Jun, O . Kochan, W . Chunzhi d an R . Kochan, “ Penelitian teoritis d an eksperimental kesalahan m etode t ermokopel
dengan p rofil m edan s uhu terkontrol,” M eas. S ains. Pdt., jilid. 15, tidak. 6, h al.304–312, 2015.
[35] A K M allik, D. Liu, V . Kavungal, Q . Wu, G . F arrell d kk., “Resonator mikro bola berlapis A garose u ntuk pengukuran
kelembapan,” O pt. E kspres, jilid. 2 4, t idak. 19, hal.21216–21227, 2 016.
[36] I . K ahalo, H . B eshley, M . B eshley dan O . P anchenko, “ Meningkatkan q os dan efisiensi e nergi j aringan t erintegrasi lte/lte-
u/wi-fi berdasarkan teknik adaptif u ntuk pembentukan struktur r adio,” d i P roc.
UKRCON, Lviv, U kraina, h lm. 1167–1170, 2019.
[37] A. Montazerolghaem, M H Yaghmaee d an A . Leon-Garcia, “Jaringan m ultimedia c loud hijau: a lokasi sumber d aya hemat
energi berbasis N FV/SDN,” IEEE T ransactions o n G reen C ommunications a nd Networking, vol. 4, t idak. 3, h al.873–889,
2020.
[38] H . Zhu, X. L iao, C. de Laat d an P . Grosso, “ Penjadwalan perutean a liran bersama u ntuk jaringan pusat d ata yang
ditentukan p erangkat lunak hemat e nergi: Sebuah p rototipe p latform manajemen jaringan y ang sadar energi,” J urnal
Jaringan d an K omputer Aplikasi, j ilid. 6 3, h lm.110–124, 2016.
[39] Y. Njah dan M. Cheriet, “ Optimasi r ute p aralel d an jaminan l ayanan dalam perangkat l unak hemat e nergi-
jaringan IoT i ndustri yang ditentukan,” I EEE Access, v ol. 9, h al.24682–24696, 2 021.