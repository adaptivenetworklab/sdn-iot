# DLVisor Dynamic Learning Hypervisor for Software Defined Network (1)

> Source file: `DLVisor Dynamic Learning Hypervisor for Software Defined Network (1).pdf`

---

Machine Translated by Google
Diterima 5 J uli 2023, diterima 30 J uli 2023, t anggal p ublikasi 4 Agustus 2023, t anggal versi s aat i ni 14 A gustus 2023.
Pengenal O bjek Digital 10.1109/ACCESS.2023.3302266
DLVisor: Hypervisor P embelajaran Dinamis u ntuk
Jaringan B uatan Perangkat L unak
MOHAMED KHALAFALLA HASSAN 1,,2
SHARIFAH H AFIZAH SYED ARIFFIN 2, (Anggota S enior, IEEE), SHARIFAH KAMILAH S YED-YUSOF,2
NURZAL E FFIYANA B INTI GHAZALI K HALID 2, MOHAMMED EA K ANONA 1,
S. M OHAMED D AN M OSAB 1, (Anggota, IEEE), M UTAZ H H KHAIRI1 , (Anggota S enior, I EEE),
HAMDAN3 , (Anggota Senior, I EEE)
1Fakultas T eknologi T elekomunikasi d an A ntariksa, Future University, Khartoum 1 0553, Sudan
2Fakultas T eknik Elektro, Universitas Teknologi M alaysia, J ohor Bahru 81310, M alaysia
3Pusat Penelitian Interdisipliner untuk Sistem K eamanan C erdas, Universitas Perminyakan d an Mineral King Fahd, Dhahran 3 1261, A rab Saudi
Penulis k oresponden: Mohamed Khalafalla H assan (memo1023@hotmail.com)
ABSTRAK S oftware D efined N etwork ( SDN) merupakan salah s atu t eknologi j aringan modern y ang m emberikan f leksibilitas j aringan dan
menyederhanakan manajemen jaringan. Virtual S DN ( vSDN) meningkatkan fleksibilitas b erbagi sumber daya j aringan fisik d engan beberapa
irisan yang m ewakili beberapa p enyewa a tau layanan d i mana s etiap penyewa memiliki k endali a tas layanan atau a plikasi mereka melalui
Jaringan Virtual ( VN). Virtualisasi jaringan m emberi penyedia layanan lebih b anyak fleksibilitas u ntuk menawarkan l ayanan baru dan inovatif
dengan efisiensi dan keandalan e kstra. M enjalankan beberapa jaringan v irtual melalui i nfrastruktur t ertentu menciptakan tantangan bagi
mekanisme alokasi s umber d aya y ang e fisien u ntuk m enghindari kemacetan dan kekurangan sumber daya s erta untuk mempertahankan
Perjanjian T ingkat Layanan (SLA), d i m ana pengelolaan s umber d aya d i vSDN d ilakukan oleh hypervisor. Beberapa penelitian t elah
membahas alokasi s umber d aya d inamis d alam d omain v SDN. Oleh k arena i tu, untuk memanfaatkan s umber daya i nfrastruktur j aringan
tervirtualisasi s ecara e fisien, h ypervisor j aringan h arus proaktif d engan k emampuan k onfigurasi u lang mandiri u ntuk menetapkan sumber
daya f isik dan sangat m udah b eradaptasi s erta b ereaksi t erhadap perubahan tuntutan v SDN di masa depan. D engan demikian, h ypervisor
berbasis pembelajaran dinamis b ertujuan u ntuk meningkatkan operasi h ypervisor. Berdasarkan hal tersebut, penelitian i ni bertujuan u ntuk
meningkatkan teknologi v SDN u ntuk m enyediakan mekanisme alokasi sumber daya i risan d inamis proaktif y ang d itingkatkan, untuk
meningkatkan pengiriman lalu lintas d an p emanfaatan s umber d aya. Hal i ni dapat dipenuhi dengan mengusulkan m odel p erkiraan cerdas
yang d itingkatkan untuk p emanfaatan sumber d aya i risan vSDN berdasarkan teknik s tatistik dan P embelajaran M esin (ML) y ang d itingkatkan.
Model yang d iusulkan a kan b ereaksi s ecara d inamis t erhadap p enyimpangan konsep d an k emudian digunakan untuk mengembangkan
mekanisme alokasi s umber d aya u ntuk a lokasi s umber d aya i risan vSDN. Mekanisme alokasi sumber daya p eramalan d inamis yang
ditingkatkan diverifikasi melalui k umpulan d ata jejak j aringan nyata y ang t ersedia dari berbagai sumber. D LVisor dengan Kerangka
Pembelajaran Dinamis (DLF) dapat mengurangi p emanfaatan b erlebihan dan, a kibatnya, kekurangan sumber daya sebesar 100%
dibandingkan dengan tolok u kur t erkait.
ISTILAH I NDEKS Pembelajaran mesin, a lokasi s umber d aya, p erkiraan sumber daya, jaringan yang d itentukan perangkat lunak, virtualisasi.
I. PENDAHULUAN pesawat. Di s isi lain, virtualisasi jaringan memungkinkan berbagi sumber daya
Jaringan yang d itentukan perangkat l unak ( SDN) telah m uncul s ebagai jaringan fisik d i mana p enyewa atau p emilik irisan m emiliki w ewenang a tas
teknologi jaringan m enjanjikan yang m emungkinkan pengelolaan d ata yang sumber daya jaringan virtual mereka.
fleksibel dalam jaringan k omputer d an komunikasi y ang memisahkan bidang Jaringan d apat memanfaatkan m anfaat SDN dan V irtualisasi F ungsi Jaringan
penerusan data dan bidang k endali. (NFV) melalui v irtualisasi jaringan SDN. H ypervisor SDN memisahkan jaringan
SDN fisik yang m endasarinya m enjadi b eberapa vSDN y ang terpisah secara
Editor rekanan yang m engoordinasikan peninjauan n askah ini d an logis, masing-masing dengan pengontrolnya. Misalnya, setiap Virtual
menyetujuinya u ntuk d iterbitkan adalah Mahdi Z areei .
Karya i ni d ilisensikan di b awah Lisensi C reative C ommons Attribution-NonCommercial-NoDerivatives 4 .0.
84144 Untuk informasi lebih l anjut, lihat h ttps://creativecommons.org/licenses/by-nc-nd/4.0/ JILID 1 1, 2 023

Machine Translated by Google
MK  Hassan  dkk.:  DLFisor: D ynamic  Learning  Hypervisor u ntuk S oftware D efined  Network
TABEL  1. D aftar  singkatan.
|     |     | dirancang a gar m                | udah b eradaptasi,  sehingga h arus  mengadopsi d an   |                                 |                   |
| --- | --- | -------------------------------- | ------------------------------------------------------ | ------------------------------- | ----------------- |
|     |     | menerapkan  pendekatan u ntuk m  |                                                        | elakukan  konfigurasi u lang m  | andiri. U  ntuk   |
memastikan a lokasi  dan  pengoptimalan  sumber  daya  yang l ebih  baik,  vSDN
memerlukan  perkiraan s tatus  jaringan  saat  ini d an  masa  depan  dan  terus
|     |     | dijalankan  dalam m               | ode  online  atau  semi-online  untuk b eradaptasi d engan   |                                              |                              |
| --- | --- | --------------------------------- | ------------------------------------------------------------ | -------------------------------------------- | ---------------------------- |
|     |     | variasi  permintaan j aringan. M  |                                                              | ekanisme  dan  pendekatan  tersebut h arus   |                              |
|     |     | bekerja  dalam  skala w           | aktu y ang  bervariasi u ntuk m                              |                                              | encapai  efisiensi s umber   |
daya y ang  tinggi u ntuk s umber  daya  tervirtualisasi.  Oleh k arena  itu,
hypervisor b erbasis p embelajaran d inamis  diperlukan u ntuk m  eningkatkan  pengoperasian  hypervisor.
Desain  algoritma  manajemen s umber  daya h ypervisor d alam  memecahkan
tantangan i ni m  erupakan  bidang p enelitian  terbuka  dan  memerlukan
penyelidikan  terperinci  [1], [ 4].
Untuk m  emanfaatkan s umber  daya  infrastruktur  jaringan  virtual  secara
efisien, d iperlukan k erangka  alokasi  sumber d aya  berbasis p erkiraan y ang
canggih  untuk s umber  daya  fisik. K erangka  kerja i ni h arus  memiliki
|     |     | kecerdasan  untuk m                                           | engatasi p ermintaan K ualitas  Layanan ( QoS)  yang   |                                                    |                     |
| --- | --- | ------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------- | ------------------- |
|     |     | dinamis  dan  mampu  bereaksi s ecara m                       |                                                        | andiri  terhadap  situasi y ang d inamis           |                     |
|     |     | dan  mengatur d irinya  sendiri  tanpa  mempengaruhi  SLA. O  |                                                        |                                                    | leh  karena i tu,   |
|     |     | pendekatan p roaktif  untuk m                                 |                                                        | engelola b andwidth  dan  sumber  daya  jaringan   |                     |
sangat d iperlukan [ 7], [ 8]. A lokasi s umber  daya  jaringan  dinamis  yang
proaktif  bergantung p ada p erkiraan p ermintaan  jaringan  dan  bertindak
|     |     | sesuai  dengan  itu  untuk m  | emungkinkan  respons  yang d inamis  dan  tepat   |     |     |
| --- | --- | ----------------------------- | ------------------------------------------------- | --- | --- |
waktu.  Dengan  demikian,  keakuratan  pendekatan p rediktif  dianggap  sebagai
faktor  penting d alam  berbagai  penerapan k erangka  prediktif.
Teknik M  L y ang  akurat s angat p enting d an  banyak d igunakan d alam
berbagai  aplikasi, s eperti p erkiraan l alu  lintas  jaringan  [9], [ 10],  [11], [ 12],
[13],  [14],  Internet o f T hings ( IoT) [ 15],  dan  komunikasi n irkabel  [16].
Manajemen  sumber  daya  di v SDN d ilakukan o leh  hypervisor S DN.
Tidak  ada  mekanisme  alokasi  sumber  daya d inamis  proaktif  yang  disediakan
|     |     | dalam  semua l iteratur  terkait, m  |     | etodologi  dan  kerangka  kerja y ang   |     |
| --- | --- | ------------------------------------ | --- | --------------------------------------- | --- |
disediakan b ersifat  statis  (tidak  dapat  beradaptasi d engan  perubahan l alu
Mesin ( VM) d an s istem o perasi  tamunya  berjalan p ada  platform  komputasi   lintas/jaringan)  atau r eaktif  karena  bekerja  dalam  kondisi  saat  ini t anpa
fisik  tertentu [ 1],  [2],  [3].  Selain  memantau  mesin v irtual,  hypervisor   perkiraan s umber  daya  yang d apat  menyebabkan  sumber  daya  kelaparan.
menetapkan  sumber  daya p latform  komputasi a ktual  ke s etiap m  esin v irtual. Oleh  karena  itu, p enting  untuk m  engembangkan  kerangka  pembelajaran
|     |     | dinamis  untuk m  | engalokasikan d an  memodifikasi  irisan b andwidth  untuk   |     |     |
| --- | --- | ----------------- | ------------------------------------------------------------ | --- | --- |
Hypervisor  membuat b eberapa v SDN  menggunakan  protokol  Open F low   pemanfaatan s umber  daya  yang l ebih  baik d an  untuk m  enghindari
(OF)  berdasarkan  jaringan  fisik  tertentu.  Setiap  vSDN  berhubungan  dengan   kekurangan s umber  daya  dan  pelanggaran  SLA  karena  kemacetan  dan
| bagian d ari  keseluruhan j aringan.  Teknologi  jaringan  masa d epan  di G  |     | enerasi   degradasi Q  | oS. |     |     |
| ----------------------------------------------------------------------------- | --- | ---------------------- | --- | --- | --- |
Kelima ( 5G)  dan s eterusnya  akan  diaktifkan  oleh v SDN  [4], [ 5], [ 6].
|     |     | Penelitian i ni b ertujuan u ntuk m  |     | eningkatkan t eknologi v SDN g una   |     |
| --- | --- | ------------------------------------ | --- | ------------------------------------ | --- |
Menjalankan  vSDN p ada i nfrastruktur  tertentu d engan  mekanisme  alokasi   menyediakan m  ekanisme  alokasi s umber  daya  irisan d inamis  yang l ebih
sumber  daya y ang e fisien  dapat  meningkatkan  pemanfaatan  perangkat   baik u ntuk m  eningkatkan p emanfaatan s umber d aya  dan  meminimalkan
keras j aringan  yang m  emenuhi s pesifikasi  penyewa d an l ayanan s erta   kekurangan s umber  daya. T ujuan  khusus d ari  pekerjaan i ni a dalah u ntuk
Perjanjian T ingkat  Layanan ( SLA).  Tabel  3 m  enunjukkan  daftar s imbol y ang   meningkatkan m  ekanisme  alokasi  irisan d i v SDN b erdasarkan p engelolaan
akan  digunakan  pada b agian  berikut
irisan p roaktif  berdasarkan s umber  daya  (perkiraan  bandwidth)  yang  akan
tercermin s ebagai  hasil  dalam  menghilangkan j umlah  pemanfaatan
Selain i tu,  vSDN  memungkinkan  penyedia  layanan j aringan  untuk   berlebihan  dan  meminimalkan  kemacetan  dan  kelaparan s umber  daya.
Penelitian i ni b erkontribusi  pada t eknologi v SDN d engan  memberikan
memberikan  layanan b aru d an  inovatif d engan  fleksibilitas, e fisiensi,  dan
keandalan  yang l ebih b esar.  Mengoperasikan  beberapa  jaringan  virtual   hypervisor k emampuan  untuk m  engelola  dan  meningkatkan k inerja  mereka
memerlukan  sejumlah  besar s umber  daya  jaringan  fisik.  Oleh k arena  itu,   secara m  andiri  karena m  anajemen  potongan  bandwidth  adalah s alah  satu
metode  alokasi  sumber  daya  yang c erdas  dan e fisien  sangatlah  penting.   sumber  daya  penting  yang p erlu b ekerja  dalam  skala  waktu s ingkat u ntuk
Untuk t erus  mencapai  dan m  empertahankan  kinerja  terbaik,  hypervisor   mencapai  efisiensi s umber  daya  yang  tinggi u ntuk s umber  daya  tervirtualisasi.
| jaringan  SDN  harus m  | elakukannya | Karena i tu, |     |     |     |
| ----------------------- | ----------- | ------------ | --- | --- | --- |
JILID 1 1,  2023 84145

Machine Translated by Google
MK Hassan dkk.: DLFisor: D ynamic Learning H ypervisor untuk Software D efined Network
penelitian ini akan s ecara p roaktif memberikan pembelajaran berbasis M L
hypervisor u ntuk menghindari k ekurangan sumber d aya irisan dan
pelanggaran SLA d i vSDN. I ni termasuk:
1) m engintegrasikan model peramalan s tatis yang d itingkatkan ke dalam
Manajemen irisan vSDN untuk meningkatkan p emanfaatan i risan
vSDN b erdasarkan teknik ML.
2) mengadopsi model peramalan statis dengan menggunakan model dinamis
kerangka pembelajaran (DLF) u ntuk mengurangi model statis
kesalahan peramalan karena perubahan k onsep untuk m emperbarui dan
meningkatkan validitas m odel.
3) mengusulkan peningkatan sumber d aya ( bandwidth) secara p roaktif
alokasi i risan dan manajemen penawaran dan p ermintaan di
vSDN m enggunakan kerangka p embelajaran dinamis u ntuk
meminimalkan kemacetan dan kekurangan sumber daya. Yang diusulkan
Kerangka k erja m anajemen irisan vSDN akan d iberi n ama
DLVisor.
Susunan m akalahnya a dalah sebagai b erikut, bagian I I m emberikan
pengenalan s ingkat tentang jaringan v irtual d an virtualisasi, S DN dan
vSDN, bagian III membahas t entang teknologi mutakhir GAMBAR 1. A rsitektur vSDN.
manajemen sumber d aya d alam teknologi vSDN, b agian I V memberikan
keseluruhan m etodologi, a lgoritma, a rsitektur dan permintaan a lokasi dapat d ilakukan dengan k ontrol p enerimaan
implementasi alokasi irisan bandwidth dinamis, mekanisme. Kisaran algoritma o ptimasi VNE s aat i ni
bagian V I membahas h asil d an temuan s edangkan bagian dari f ormulasi eksak, s eperti p rogram linier b ilangan bulat campuran, h ingga
VII m emberikan kesimpulan berbasis p endekatan heuristik, dimungkinkan u ntuk m enghubungkan
penugasan sumber d aya vSDN ke masalah V NE u mum dan m enguraikan
II. LATAR B ELAKANG penggunaan metrik kinerja V NE u mum dalam k onteks SDN. Beberapa
Virtualisasi Jaringan ( NV) berasal d ari keberhasilan virtualisasi dalam survei ikhtisar y ang diterbitkan
domain komputasi [1], [ 17]. sudah mendiskusikan p rinsip-prinsip v irtualisasi j aringan,
Ini m enciptakan jaringan v irtual t erpisah ( irisan) m elalui a bstraksi khusus manfaat, d an p endekatan. M isalnya, survei rinci tentang
dan blok fungsional isolasi [1]. D i hypervisor tervirtualisasi j aringan untuk S DN dapat d itemukan di [ 1].
domain jaringan, konsep slicing s udah a da. U ntuk Kemampuan untuk m emprogram j aringan virtual menggunakan SDN
Misalnya, jaringan berbasis s erat optik, W avelength D ivi-sion M ultiplexing adalah aspek k unci penting l ainnya d ari v irtualisasi j aringan total [ 21].
(WDM) [ 18] d apat membuat irisan di Melihat v irtualisasi j aringan lama, seperti
lapisan f isik, s edangkan pada lapisan tautan, Area Lokal V irtual Virtualisasi berbasis V LAN t anpa f itur p emrograman,
Jaringan (VLAN) d an Peralihan L abel Beberapa Protokol penyewa t idak akan d apat menginstruksikan saklar untuk m engambil tindakan
(MPLS) [7], [ 19] dapat dibuat. seperti m anajemen lalu l intas, y aitu kemudi l alu l intas. Meski demikian, untuk
Sebaliknya, virtualisasi jaringan c enderung terbentuk mewujudkan N FV sepenuhnya, p enyewa harus mendapatkan j aringan virtual
irisan dari k eseluruhan j aringan, y aitu membentuk jaringan virtual sumber daya, s eperti t otal t ampilan topologi j aringan dan
(irisan) di s emua l apisan p rotokol jaringan. Kapan saja, sumber d aya jaringan y ang d ialokasikan, y ang m elibatkan kecepatan data t autan dan
irisan tertentu harus m emiliki s umber d ayanya ( abstraksi spesifik dari sumber daya node j aringan. A palagi menyediakan isolasi dan
topologi jaringan, b andwidth link, komputasi s witch jaringan virtual yang dapat d iprogram m emiliki keuntungan y ang signifikan.
sumber d aya dan beralih t abel p enerusan). Jaringan maya Dalam k asus seperti itu, operator j aringan dapat mengembangkan dan menguji h al baru
(slice) m emungkinkan pengujian paradigma j aringan b aru, t erlepas dari teknologi j aringan dengan b atasan y ang lebih sedikit [ 22].
kepatutan dan pembatasan y ang d iberlakukan saat ini Selain i tu, N V dianggap sebagai p emain k unci dalam p enyediaan
struktur d an protokol internet[1]. M enjalankan banyak virtual kinerja j aringan yang dapat d iprediksi ( terjamin) [23]. Oleh karena itu,
jaringan melibatkan konsumsi s ejumlah fisik t ertentu Penyedia Jasa (SP) a kan mampu menyediakannya
sumber d aya j aringan. O leh k arena itu, efisien, d an canggih atau penyediaan layanan b aru melalui i nfrastruktur y ang ada d i a
mekanisme a lokasi s umber d aya s angat dibutuhkan [8], [20]. lebih j auh l agi, S Ps a kan m elakukannya dengan l ebih c epat d an l ebih d apat diandalkan
Misalnya, i nterkoneksi antar n ode virtual, memungkinkan jaringan mereka untuk s ecara d inamis mengubah d an memodifikasi j aringan m ereka
jalur virtual dan Penempatan VM p ada infrastruktur f isik, ini j uga dikenal jaringan virtual sesuai d engan p erubahan pengguna d an l ayanan
sebagai V irtual Network Embedding tuntutan [24], [25], [26]. Lapisan v irtualisasi j aringan
(VNE) m asalah [1]. memungkinkan hosting beberapa pengontrol [ 26], [27]. Jaringan
Masalah VNE a dalah w aktu P olinomial N on-deterministik hypervisor b erkomunikasi dengan p erangkat k eras jaringan yang
kekerasan ( NP-hard) d an masih diselidiki secara l uas. mendasarinya melalui a ntarmuka arah selatan melalui p rotokol SDN,
Umumnya, menerima d an menolak sumber daya j aringan virtual DARI s ebagai c ontoh. D alam kasus N V, h ypervisor b eroperasi
84146 JILID 11, 2023

Machine Translated by Google
MK Hassan dkk.: DLFisor: D ynamic Learning Hypervisor untuk Software D efined Network
di atas a ntarmuka arah selatan y ang sama untuk operator jaringan virtual konfigurasi k omposisi untuk memproses a turan S DN, penelitian ini
dan terhadap p enyewa j aringan S DN. Hypervisor d ihubungkan dengan menekankan p ada waktu pembentukan k ebijakan komposisi yang
beberapa arah selatan d engan b eberapa p engontrol S DN [ 27]. Hypervisor ditambahkan k e h ypervisor OF l atency, selain itu, d aftar p rioritas bersifat
SDN b eroperasi s ebagai p roksi. statis dan tidak m engalokasikan a tau mengelola s umber daya secara dinamis.
Ini m encegat d an m enerjemahkan p esan kontrol antara p enyewa dan Penulis [ 21] mengusulkan P latform V irtualisasi J aringan ( NVP), dengan
jaringan S DN fisik. G ambar 1 menunjukkan arsitektur vSDN. fokus pada abstraksi s umber daya jaringan p usat data yang dikelola o leh
penyewa cloud u ntuk lingkungan multi-penyewa, yang berfungsi s ebagai
Dengan menggabungkan SDN d an NFV, p enyewa akan m emiliki pengontrol u ntuk menyediakan p enyewa SDN untuk mengoperasikan
keuntungan fleksibilitas d alam berbagi sumber daya melalui b erbagi jaringan pengontrol S DN mereka melalui P emrograman Aplikasi A ntarmuka ( API)
virtual selain m emiliki fitur kemampuan program SDN, s ementara NFV dan mengontrol irisannya di p usat data. Hal ini d icapai dengan membentuk
menyediakan kemampuan untuk memprogram sumber daya virtual [ 25] cluster p engontrol t erdistribusi u ntuk menskalakan beban penyewa s esuai
dimana k ombinasi tersebut d isebut vSDN [ 24], [26]. Hal i ni dapat dilihat kebutuhan dengan sakelar v irtual untuk mengarahkan lalu lintas penyewa
pada G ambar 1 yang m enunjukkan arsitektur vSDN. ke m esin v irtual yang sesuai dengan berfokus p ada perangkat l unak y ang
berada d i d alam s akelar v irtual d i s erver host. NVP u mumnya menetapkan
jalur data logis (terowongan) antara t ujuan dan s umber Open Virtual S witch
AKU A KU A KU. PEKERJAAN T ERKAIT (OVS) di m ana j alur logis t erkait d engan potongan penyewa terkait
Bagian i ni membahas p ekerjaan t erkait dalam konteks menggunakan t eknik penerowongan Generic R outing Encapsulation (GRE).
manajemen bandwidth dinamis (irisan) d i v SDN. Seperti yang dibahas di
bagian s ebelumnya, hypervisor melakukan tugas manajemen sumber d aya,
dan semua h ypervisor vSDN d ianggap s ebagai ekstensi dari hypervisor Hypervisor O penVirteX d i [ 31] diperkenalkan d engan dua kontribusi
FlowVisor. utama: t opologi dan virtualisasi alamat.
FlowVisor (FV) a dalah hypervisor pertama untuk jaringan S DN, y ang OpenVirteX m emperluas F V d engan mengatasi m asalah r uang a liran.
menyediakan fitur berbagi sumber daya jaringan SDN a ntara beberapa Hal ini d icapai dengan menggunakan header u ntuk membedakan vSDN
pengontrol. F V pada a khirnya d apat dijalankan sebagai perangkat lunak alih-alih menyediakan seluruh r uang b idang header k e vSDN. D i OpenVirteX,
yang berdiri sendiri pada p erangkat k eras komoditas ( server) [28]. switch menulis u lang alamat Internet P rotocol (IP) dan Media A ccess
FV adalah hypervisor serba guna dan mewakili f ondasi hypervisor vSDN Control (MAC) yang d itetapkan secara v irtual y ang digunakan oleh host
lainnya. Ia menawarkan isolasi atribut node seperti C entral Processing U nit setiap vSDN (penyewa). O pen-Virtex t idak memberikan kontribusi y ang
(CPU) dan tabel Aliran selain bandwidth sebagai isolasi a tribut tautan. berharga terhadap p engelolaan sumber daya dinamis.
FV terutama menekankan pendekatan untuk mengisolasi lalu lintas j aringan Dalam [ 32], hypervisor s entris J alur D ata d iperkenalkan u ntuk mengatasi
di jaringan e ksperimental dari lalu lintas di jaringan produksi s ehingga masalah r edundansi d i FV ( Titik kegagalan tunggal) d an m eningkatkan
memberikan definisi irisan jaringan yang fleksibel. kinerja lapisan virtualisasi melalui penerapan f ungsi virtualisasi sebagai
Namun, ia menambahkan latensi dalam pesan OF dan tidak m enunjukkan ekstensi sakelar. I a b ekerja d engan menerapkan Agen V irtualisasi ( VA) d i
kontrol p enerimaan serta tidak ada mekanisme untuk pengelolaan dan dalam s akelar s elain V irtualization Agent O rchestrator (VAO). Tanggung
pengoptimalan irisan. jawab utama V AO adalah pemantauan d an konfigurasi i risan, contohnya
MobileVisor dalam [29], m enerapkan pendekatan FlowVisor d alam adalah menambah atau menghapus i risan. Di s isi l ain, VA b ertanggung
jaringan inti paket seluler; di mana fungsionalitas FlowVisor d iintegrasikan jawab untuk berkomunikasi dengan pengontrol v SDN s elain a bstraksi
ke dalam struktur arsitektur jaringan paket seluler v irtual yang t erdiri dari sumber daya untuk VAO. Jika V AO gagal, VA dapat terus b eroperasi,
beberapa jaringan s eluler fisik yang mendasarinya seperti jaringan 3 G d an menghindari s atu titik kegagalan dalam a rsitektur Flow visor. Datacentric
4G. tidak m endukung i solasi bandwidth tetapi masih dapat mendukung Q oS
Hal i ni memungkinkan Penyedia Layanan Internet (ISP) untuk menentukan berdasarkan evaluasi ekstensif. Kasus V A m enambahkan overhead s ebesar
kebijakan d an l ayanan b erbasis QoS selain o perator seluler t ersebut. 18% d ibandingkan dengan kasus referensi. Latensi overhead f ailover
Selain itu, ISP akan dapat mengelola k ebijakan penagihan mereka dengan adalah sekitar 3 ms.
lebih e fisien. Tidak ada p enghitungan latensi yang disebutkan; namun,
karena h ypervisor mengadopsi FV, manajemen sumber dayanya tidak
dinamis. Meskipun d apat mendukung Q oS, k urangnya i solasi bandwidth tidak akan
Dalam [ 30] p enulis memperkenalkan hypervisor komposisional untuk memungkinkan alokasi irisan bandwidth dinamis.
menyediakan platform fleksibel yang memungkinkan operator jaringan Dalam [33], CoVisor diperkenalkan s ebagai perpanjangan d ari h ypervisor
SDN m emilih berbagai a plikasi j aringan yang dikembangkan untuk komposisi y ang m emfasilitasi kerja s ama p engontrol h eterogen u ntuk
pengontrol SDN y ang b erbeda. I ni akan memungkinkan aplikasi berbeda bekerja p ada jenis lalu l intas yang sama d engan lebih fokus pada
yang ditulis untuk pengontrol t ertentu untuk dijalankan pada pengontrol lain peningkatan kinerja jaringan f isik S DN, yaitu ruang t abel aliran d an a bstraksi
yang ditulis dalam bahasa l ain; h ypervisor komposisi menetapkan kebijakan topologi di s edemikian rupa u ntuk menyediakan sumber daya yang
tersusun yang m ewakili d aftar aturan yang diprioritaskan per switch SDN diperlukan s eperti informasi topologi atau abstraksi b ila diperlukan, y aitu
yang disediakan oleh pengontrol SDN t erkait, dan kemudian h ypervisor penyeimbang b eban tidak selalu m emerlukan tampilan t opologi yang
komposit m embentuk hypervisor y ang sesuai terperinci
JILID 1 1, 2023 84147

Machine Translated by Google
MK Hassan dkk.: DLFisor: D ynamic Learning H ypervisor untuk Software D efined Network
untuk m emutuskan untuk menjatuhkan atau meneruskan paket. S elain itu, ini mendukung protokol SDN y ang berbeda seperti Netconf dan LISP.
itu memberikan bentuk keamanan t erhadap penipuan pengontrol S DN. Terakhir, d iuji d an dievaluasi d alam s kenario minimal.
CoVisor m eningkatkan latensi hypervisor Komposisional sebanyak d ua hingga Tidak a da alokasi sumber daya d inamis yang d ibahas.
tiga kali lipat. N amun, hypervisor tidak m elakukannya Dalam [40], kerangka m anajemen diperkenalkan untuk m enyediakan
menyediakan alokasi s umber d aya yang d inamis. manajemen bandwidth m elalui definisi statis
Pada [ 34], DFVisor ( Distributed F lowVisor) d iperkenalkan ambang batas u ntuk s etiap i risan b erdasarkan prioritas i risan s ebelumnya; i tu
untuk m engatasi masalah skalabilitas FV s ebagai h ypervisor virtualisasi S DN kerangka k erja d isajikan s ebagai mekanisme kontrol p enerimaan. kerangka
terpusat. Hal ini membahas kemungkinan memperluas switch SDN dengan yang diusulkan t erdiri d ari Pengambilan Keputusan
kemampuan hypervisor, menghasilkan (DM) M odul, yang m emutuskan berapa banyak bandwidth yang a kan
sakelar O penFlow yang d itingkatkan yang d apat d icapai dialokasikan berdasarkan permintaan p enangan p ermintaan d an database
dengan memperluas switch S DN d engan modul tunneling l okal informasi modul ( DB). N amun belum a da penilaian detail
dan p emotong v SDN. D FVisor menggunakan terowongan G RE u ntuk d ata disediakan p ada l atensi dan overhead. Selain i tu, kerangka k erjanya bersifat
merencanakan pemotongan d an enkapsulasi a liran data yang b ermanfaat statis d an hanya d idasarkan p ada keadaan saat ini.
dalam mengadopsi QoS. DFvisor mengadopsi s inkronisasi d ua tingkat Dalam [41] kerangka D ART dapat m endistribusikan secara dinamis
database terdistribusi, database pertama (lokal) b erada bandwidth jaringan b erbeda u ntuk m emanfaatkan s umber daya j aringan
switch, sementara d atabase global memelihara potongan informasi statistik, secara efisien. Kerangka kerja i ni mengadopsi kontrol penerimaan
operasi j aringan, dan s kalabilitas mekanisme untuk m endistribusikan b andwidth jaringan sesuai p ermintaan. I tu
ditingkatkan. Namun, solusi y ang diusulkan m emang dimaksudkan untuk itu ruang l ingkupnya t erbatas pada Industrial I nternet of T hings (IIOT)
lingkungan cluster. dan hanya b ekerja pada k ondisi saat i ni. Dalam kerangka i ni,
EnterpriseVisor di [35], adalah salah s atu h yper-visor paling terkenal dua modul d iusulkan, k omunikasi dan penerbitan
mengenai a lokasi p otongan sumber daya. I ni m emperkenalkan sebuah modul. Modul k omunikasi d igunakan untuk m engirim d an
modul perangkat lunak yang d iperluas untuk m emantau dan menganalisis menerima i nformasi, s edangkan m odul p enerbitan d igunakan u ntuk
pemanfaatan irisan. Selain i tu, p emrograman linier d igunakan u ntuk m enyesuaikan berkoordinasi a ntar p engontrol. K omponen t erpusat bertanggung jawab untuk
membagi bandwidth secara d inamis, mesin y ang d iusulkan menentukan memberikan saran b andwidth terbaik
pemohon irisan dan p enyedia sumber d aya u ntuk m emenuhi persyaratan untuk s etiap p engontrol S DN. K ontrol penerimaan dapat d ipicu o leh beban,
layanan. Selanjutnya, EnterpriseVisor berinteraksi prioritas, d an rasio k ehilangan p aket u ntuk m endistribusikan ulang
dengan Flow Visor, menerapkan kebijakan p emotongan u ntuk m engonfigurasi bandwidth jaringan. M akalah ini menggunakan prioritas untuk l alu lintas
jaringan. O leh k arena itu, konfigurasi i risan dapat disesuaikan sebagai pemicu berdasarkan tingkat Q oS yang d iminta.
untuk m emenuhi kebutuhan layanan. Di [42], m anajer sumber daya P rioSDN ( PrioSDN_RM)
Dalam [ 36], platform manajemen jaringan virtual berbasis niat disajikan sebagai kerangka manajemen sumber d aya untuk m enyediakan
berdasarkan SDN diusulkan u ntuk m engotomatisasi konfigurasi kontrol penerimaan untuk j aringan berbasis SDN t ervirtualisasi.
dan pengelolaan sumber d aya VN dari sisi penyewa. I tu Mekanisme yang d iusulkan menerapkan batasan sumber daya
kerangka kerja didasarkan pada OpenVirtex. K erangka kerja y ang d iusulkan pemanfaatan untuk i risan v irtual. Ini mengadopsi pendekatan u ntuk
menyederhanakan definisi dan pengelolaan s umber daya memanfaatkan m ekanisme distribusi b andwidth u ntuk
sisi a dministratif melalui representasi kebutuhan b isnis t ingkat tinggi k arena bereaksi s ecara dinamis terhadap perubahan b eban. H al ini bergantung p ada
pengelolaan sumber d aya V N a dalah a prioritas aliran, b ukan p rioritas perangkat. A palagi ambang batas b andwidth
proses yang rumit d an m emakan waktu serta k ekurangan bergerak sesuai dengan aliran k ritis y ang telah d itentukan. p enyimpanan
dari p roses p enyediaan otomatis yang t ersedia. Niatnya terus m elacak penggunaan bandwidth s aat ini, dan komputasi
lapisan m embantu penyewa untuk m enentukan persyaratan t ingkat tinggi. modul m enghitung sumber daya bandwidth y ang t ersedia. Kemudian,
Dalam [ 37] d an [ 38], AutoVFlow diperkenalkan s ebagai h ypervisor itu mengalokasikan jumlah sumber daya b andwidth y ang diperlukan
terdistribusi untuk digunakan dalam jaringan a rea luas d i mana bantuan manajer a turan a liran d an manajer a mbang batas,
infrastruktur y ang m endasarinya tersebar secara t idak t umpang tindih yang m enetapkan jumlah bandwidth b erdasarkan prioritas
domain. H ypervisor bertanggung j awab untuk s etiap d omain dan aliran, a salkan ambang batas p rioritas dapat d ipindahkan
bertindak sebagai proxy y ang m elakukan pemetaan i risan dan abstraksi berdasarkan prioritas aliran y ang t elah d itentukan sebelumnya. Metodologi
AutoVflow mendelegasikan administrasi dari pengontrol beban b erat k e yang d iusulkan serupa dengan pendekatan k ami, n amun b erhasil
pengontrol b eban rendah lainnya. Kebijakan p embaruan yang s olid konsumsi b andwidth s aat ini, yang d apat m enyebabkan sumber daya
dipertahankan antara t erpusat dan terdistribusi kelaparan.
pengontrol karena s atu irisan dapat menjangkau beberapa domain. Beberapa Pada [ 43], h ypervisor Libera d iperkenalkan k e alamat
identitas d igunakan, seperti a lamat M AC virtual, y ang skalabilitas dan kemudahan kemampuan penyewa untuk m enyediakannya
dapat berbeda dari satu domain k e d omain l ainnya ditemukan layanan. Masalah s kalabilitas sebagian besar d iselesaikan dengan mendukung
cukup tinggi ( sekitar 5 ,85 ms). Proses p engendaliannya adalah migrasi VM dan modifikasi a rsitektur
manual d an tidak mempertimbangkan distribusi b eban dinamis. aturan A liran m ana y ang d ikurangi; oleh karena itu, bandwidth a ntara
Dalam [ 39], ONVisor H ypervisor disajikan sebagai S DN-NV pengontrol d an s akelar virtual a kan d iminimalkan. L ibera adalah
platform untuk memberikan fleksibilitas dengan m engadopsi i nstance hyper- dianggap s ebagai perpanjangan dari OpenVirtx. S kalabilitas sumber daya
visor terdistribusi y ang m emungkinkan berbagi s tatus VN. Lebih-lebih l agi, dilakukan pada saat i ni tanpa m empertimbangkan masa d epan
84148 JILID 1 1, 2023

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic Learning Hypervisor untuk Software D efined N etwork
GAMBAR 2 . C akupan p engelolaan sumber d aya d i vSDN.
tuntutan. Selain itu, tidak ada penyelidikan mendetail y ang dilakukan mengenai
skalabilitas berdasarkan migrasi VM.
Dalam [ 44], TeaVisor disajikan untuk menjamin i solasi bandwidth di vSDN.
Hypervisor yang diusulkan m engatasi masalah kelebihan t autan dengan
menggunakan algoritma heuristik serakah u ntuk membagi l alu lintas tautan
yang k elebihan b eban k e beberapa jalur yang l ebih sedikit m uatannya.
Hasilnya menjanjikan dan s erupa d engan apa yang d ibahas d alam m akalah
ini. N amun, algoritma ini didasarkan pada pengukuran l alu l intas saat i ni,
yang dapat m enyebabkan sumber d aya ( kelaparan b andwidth).
Dalam [ 45], penulis m engusulkan arsitektur manajemen sumber d aya
untuk skalabilitas beban p engontrol S DN multidomain menggunakan
hypervisor non-SDN. Kerangka kerja ini didasarkan pada pembuatan V M
baru untuk p engontrol atau m igrasi pengontrol S DN berdasarkan ketinggian
beban; A gen perangkat lunak digunakan dalam memantau b eban pengontrol.
Namun, tidak seperti hypervisor b erbasis SDN, penggunaan hypervisor yang
berdiri s endiri m enambah masalah k urangnya isolasi sumber d aya u ntuk
pengontrol SDN. Selain i tu, pembuatan d an m igrasi langsung VM melibatkan
waktu h enti l ayanan. Dalam s emua literatur t erkait, m etodologi d an kerangka
kerja yang disediakan bersifat s tatis (tidak dapat beradaptasi d engan GAMBAR 3. Komponen m anajemen sumber daya v SDN d i DLVisor.
perubahan l alu l intas/jaringan) atau r eaktif karena b ekerja d alam keadaan
saat i ni t anpa perkiraan s umber d aya, yang d apat menyebabkan kekurangan
IV. ALOKASI Slice BANDWIDTH DINAMIS UNTUK
sumber d aya.
vSDN
Seperti yang digambarkan p ada Gambar 2, m akalah ini akan b erkonsentrasi
pada manajemen sumber daya b andwidth dalam h ypervisor v SDN yang Pekerjaan i ni d idasarkan pada EnterpriseVisor [35] yang berfokus pada
dapat d ikonfigurasi sendiri d an d ioptimalkan di mana solusi y ang d isajikan peningkatan hypervisor yang ada yang harus m ampu b ekerja terlepas d ari
(DLVisor) a kan menjadi yang pertama menggabungkan hypervisor b erbasis topologi y ang mendasari dan tuntutan j aringan. Oleh karena i tu, h ypervisor
pembelajaran melalui ML d an p engelolaan sumber d aya b erbasis harus m enunjukkan kemampuan untuk meningkatkan kinerja mereka s ecara
matematika. manajemen d i v SDN. mandiri d an
JILID 1 1, 2023 84149

Machine Translated by Google
MK H assan dkk.: D LFisor: D ynamic Learning H ypervisor untuk S oftware D efined N etwork
GAMBAR 5. Komponen y ang diuji.
TABEL 2. Hyperparameter LSTM.
GAMBAR 4. Diagram a lir u ntuk D LVisor.
transparan dengan biaya overhead m inimum. M anajemen irisan b andwidth
TABEL 3. Deskripsi k umpulan data.
adalah salah satu s umber daya p enting yang p erlu bekerja d alam skala
waktu singkat untuk m encapai e fisiensi s umber daya y ang t inggi untuk
sumber daya t ervirtualisasi. Hal i ni dapat d icapai melalui hypervisor berbasis
kognitif dan pembelajaran serta di b awah berbagai t ujuan dan b atasan
pemodelan matematika. Hypervisor peningkatan yang d iusulkan yang
ditunjukkan dalam k arya ini diberi nama D LVisor ( Hypervisor p embelajaran
dinamis), dimana Gambar 3 menunjukkan komponen m anajemen sumber
daya vSDN yang d iusulkan d i DLFisor.
Untuk t ujuan i ni dan seperti yang d itunjukkan p ada Gambar 3, Kerangka
Pembelajaran Dinamis ( DLF) y ang d iperkenalkan dan dibahas d alam
pekerjaan kami s ebelumnya [46] akan d igabungkan dan d iintegrasikan atau penyewa. Pekerjaan ini t erutama b erfokus p ada virtualisasi vSDN d i
dengan modul manajemen sumber d aya E nterpriseVisor di h ypervisor mana pemotongan ujung k e u jung R AN berada d i luar c akupan makalah ini
EnterpriseVisor. DLF akan m enangkap potongan bandwidth jaringan d ari dan d apat d itemukan dalam p ekerjaan t erkait l ainnya s eperti d i [ 47]. T iga
server C acti m enggunakan Simple N etwork Management Protocol ( SNMP). tingkat pemanfaatan a kan d idefinisikan sebagai p emanfaatan r endah dalam
Jejak l angsung dapat diakses langsung dari p enyimpanan jaringan d alam kisaran 0% hingga ÿ, p emanfaatan m enengah a dalah ÿ hingga ÿ, d an
mode online, semi-online, atau batch. P endekatan pembelajaran dinamis pemanfaatan t inggi a ntara ÿ dan 100%. Gambar 4 menunjukkan diagram
akan m enerapkan berbagai algoritma pemulusan b erbasis w indows Long alur k eseluruhan u ntuk D LVisor.
Short-Term Memory ( LSTM) hybrid d engan kehilangan data m inimum yang Bagian putih m enunjukkan D LF s edangkan b agian biru tua m enunjukkan
diperkenalkan s ebelumnya pada [ 46]. K emudian, algoritma terbaik akan alokasi irisan d an m anajemen bandwidth y ang diperkenalkan o leh
digunakan u ntuk m emperkirakan lalu lintas j aringan u ntuk setiap potongan EnterpriseVisor sejalan d engan komponen DLFisor yang d itunjukkan pada
layanan Gambar 3.
84150 JILID 11, 2 023

Machine Translated by Google
MK Hassan d kk.: DLFisor: D ynamic Learning Hypervisor untuk Software D efined N etwork
GAMBAR 6 . D iagram urutan u ntuk s kenario p engujian.
GAMBAR 7 . P embuatan irisan A TN-OBY.
Seperti yang digambarkan pada Gambar 4, a lurnya dimulai d engan
membangun model ML yang lebih baik dengan menggabungkan pemulusan
berbasis j endela y ang sadar akan kerugian sebagai teknik pra-pemrosesan
untuk menghilangkan komponen k ebisingan jangka pendek/panjang yang GAMBAR 8 . P esan log selama p embuatan irisan A TN-OBY.
tidak p erlu dan m enghindari e rosi tren dan pola periodik dalam k ebisingan
seri d an fluktuasi lalu lintas yang c epat, keluaran d ari proses ini a dalah ML
berbasis LSTM hibrid yang ditingkatkan yang akan digunakan untuk
perkiraan l alu lintas. Kemudian, untuk mengatasi keandalan dan validitas
model M L karena k arakteristik data yang cepat dan perubahan distribusi
GAMBAR 9 . S cript yang digunakan untuk mengubah batas b andwidth irisan o leh DLFisor.
akibat sifat d inamis dari properti jaringan, kerangka perkiraan harus
mendeteksi d an b eradaptasi dengan semua perubahan dalam properti
statistik l alu lintas jaringan. Perubahan profil l alu l intas, seperti lonjakan lalu lintas secara t iba-tiba,
terjadi k arena p erubahan a tau variasi pada pengguna
JILID 1 1, 2 023 84151

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic L earning Hypervisor untuk S oftware Defined Network
GAMBAR 10. Pemanfaatan irisan pada Wa = 1.
permintaan perilaku a plikasi. Oleh k arena i tu, detektor perubahan model d ibangun a salkan hasilnya s ignifikan. Detail prosesnya t elah
menggunakan Anderson Darling (AD) dimasukkan k arena dibahas d alam p ekerjaan kami s ebelumnya di [ 46]. Karena k eandalan
sensitivitasnya untuk mendeteksi perubahan k arakteristik data, yang dan kesederhanaannya, pemilihan hyperparameter dilakukan m elalui
mungkin b erdampak negatif pada a kurasi model ML. Kemudian jika pencarian grid, s eperti yang digambarkan p ada Tabel 2 [46].
terdeteksi perubahan, uji s ignifikansi s tatistik d igunakan untuk Terakhir, b andwidth yang diperkirakan d igunakan s ebagai m asukan
memvalidasi keluaran d ata p erkiraan. O leh k arena i tu, jika k eluaran pada alokasi i risan untuk mengidentifikasi penyedia sumber daya
dari algoritma ML yang digunakan saat ini t idak s ignifikan, model dan peminta sumber daya menggunakan klasifikasi irisan menjadi
saat ini ( lama) akan dipertahankan, jika t idak, model M L h ybrid b aru akan diriipsaenrt a dheanngkaann p .emanfaatan rendah, s edang, dan tinggi, lalu pasokan dan
84152 JILID 1 1, 2023

Machine Translated by Google
MK Hassan dkk.: D LFisor: Dynamic Learning H ypervisor untuk Software Defined N etwork
TABEL 4. Daftar simbol.
GAMBAR 1 1. H itungan p emanfaatan b erlebihan d i Wa = 1. B. M ANAJEMEN SLICE D I v SDN
Tabel 4 m enunjukkan d aftar simbol y ang akan digunakan p ada b agian berikut.
perhitungan permintaan dilakukan u ntuk mengalokasikan irisan v SDN secara proaktif Algoritma 1 m enunjukkan
untuk menghindari p emanfaatan berlebihan g una m eminimalkan dan m enghilangkan alokasi p eminta d an penyedia Bandwidth S lice. K ompleksitas A lgoritma 1 adalah
kemacetan dan k ekurangan sumber daya. O(nmh + m).
A. S ET DATA
Jaringan vSDN d imodelkan sebagai sekumpulan entitas ( node dan e dge) yang
Kumpulan d ata dikumpulkan d ari Penyedia Layanan Internet (ISP) t erkemuka yang saling terhubung oleh sekumpulan tautan. Dalam k arya i ni, jaringan d imodelkan
menguji r angkaian waktu p emanfaatan bandwidth y ang b erbeda. Data yang sebagai g rafik G (ÿSDN , ÿSDN ) y ang terdiri dari n ode j aringan ÿ SDN ( yaitu, sakelar
dikumpulkan m ewakili lalu lintas t ulang p unggung a gregat untuk Long Term Evolution SDN) y ang dihubungkan d engan t epi ÿ SDN . Hypervisor S DN diberikan oleh
(LTE), MPLS d an enodeBs. Data d iambil sampelnya dengan l angkah 50 d an 350 himpunan H SDN , di m ana HSDN a dalah subset dari ÿ SDN .
kali. S etiap l angkah waktu m ewakili 2 8,8 m enit, di m ana s etiap langkah 5 0 kali Permintaan v SDN, rSDN , d i mana r SDN ÿ RSDN (RSDN a dalah
mewakili satu hari, dan 350 l angkah waktu m ewakili s atu minggu. H al i ni disebabkan kumpulan t otal p ermintaan), d ibuat antara s witch SDN d i V ( Kumpulan virtual ( Pengontrol Virtual
oleh keterbatasan a lat pengumpulan data, sedangkan n ilainya diinterpolasi dan
digunakan untuk mengembangkan model d eret w aktu. Tabel 3 m enunjukkan node permintaan v SDN ) d an p engontrol c n ode R
kumpulan d ata permintaan vSDN r ) d i l okasi yang disumbangkan oleh c R ÿ
R
ÿSDN . Tujuan a khirnya a dalah memetakan p engontrol c k e saklar h ost fisik yang
nama. sesuai, y ang diwakili oleh
JILID 1 1, 2023 84153

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic L earning Hypervisor untuk S oftware Defined Network
GAMBAR 12. Pemanfaatan irisan pada Wa = 2.
makalah i ni. A lgoritma 1 menunjukkan peminta r ÿ ÿ S ÿ D N V . P eny R ediaÿa n c irisan r ÿ rSDN ÿ RSDN , ÿ ÿ melalui jaringan virtual d an fisik b erada d i l uar cakupan Algoritma dimulai dengan peramalan bandwidth yt s ebagai rangkaian w aktu l angkah waktu
sumber d aya dan k lasifikasi penyedia. A lgoritma m encari d i s etiap langkah waktu tj ÿ y di S Li ÿ Wa, d imana adalah perkiraan bandwidth u ntuk penyedia ti pada i risan S Li milik window W a. I risan tersebut kemudian dialokasikan berdasarkan
sumber daya dan p eminta sumber daya dalam irisan SLi y ang berjalan pada kumpulan ÿSDN y ang sudah disediakan di j endela W a. pemanfaatannya yang dihitung di u i ( baris 5 h ingga 1 3 dari Algoritma 1) kepada calon
pemohon. Jika p emanfaatannya lebih t inggi d ari batas atas ÿ dan ke c alon p enyedia lainnya,
jika p emanfaatannya lebih r endah dari batas bawah ÿ, m aka daftar c alon p enyedia dan
pemohon disimpan d alam daftar irisan p emohon.
84154 JILID 1 1, 2023

Machine Translated by Google
MK  Hassan  dkk.: D LFisor:  Dynamic  Learning H ypervisor  untuk  Software  Defined N etwork
Algoritma 1  B andwidth S lice  Peminta d an  Penyedia A lokasi I nput: S Li:  irisan,yt :
perkiraan
bandwidth d alam  irisan  SLi, ÿ : L STM  yang d ihaluskan s ecara s ignifikan  secara
|     | statistik, I nfrastruktur j aringan G  | (ÿSDN , ÿ SDN ),  dengan r SDN d imana r SDN  ÿ   |     |     |
| --- | -------------------------------------- | ------------------------------------------------- | --- | --- |
RSDN d an  terhubung  ke p engontrol c r , d iberikan  ÿrSDN  ÿ  ÿ  ci: i ndeks,j: i ndeks
Wtot:  ÿ  ÿSDN ,  jumlah  total  irisan,t:  waktu, a : l angkah  indeks,ÿ :  Batas b awah,
|     | RSDN , ÿ V R | r   ÿ : B a R tasj ua mtalsa h h :  j umlah  penyedia s umber d aya ,  g:   |     |     |
| --- | ------------ | --------------------------------------------------------------------------- | --- | --- |
ÿ ÿ
peminta s umber d aya i :  indeks, z : H itung j umlah  pemanfaatan  berlebihan 1 00%
|     | untuk y t d i S LiÿWtot  ÿWa O  | utput: R   {..}                  | ,   |     |
| --- | ------------------------------- | -------------------------------- | --- | --- |
|     | :                               | Daftar C  alon  Pemohon ,P  {..} |     | :   |
Daftar c alon p enyedia  X:  Hitung j ,umlah 1 00%  overutilisasi  foryt d i
|     | SLiÿpm(i)ÿWaÿP { ..} 0 1: m  | ulai 0 2:R { ..} :ÿ  ÿ;  03:P{..} ÿ   ÿ;   |     |     |
| --- | ---------------------------- | ------------------------------------------ | --- | --- |
04: u ntuk
semua  langkah
waktu  dalam
perkiraan  irisan  bandwidth  tjÿyt d i  SLiÿWtot  ÿWa d o //
|     | menggunakan  ÿ 0 5: u i  ÿ H  | itung p emanfaatan  irisan   |     |     |
| --- | ----------------------------- | ---------------------------- | --- | --- |
06  sementara g  = !  0 0 7  if  ui  ÿ  ÿ 0 8  R  {..} ÿ :
SLi //calon p emohon
09  Else 1 0  while  h
=!  0 1 1  If u i  ÿ  ÿ 1 2  {P} ÿ :  SLi //calon p enyedia 1 3  Else 1 4  Hitung
penawaran
dan p ermintaan
menggunakan
algoritma  2 1 5  untuk  SLi d i  pm(i)  di  WaÿP { ..}
16  X  ÿ H  itung p emanfaatan  irisan 1 7  Jika X  ÿ   z  Jatuhkan
SLiÿpm(i)  di  Wa  dari
|     | 18- P{..} |     |     |     |
| --- | --------- | --- | --- | --- |
19 P utaran:
GAMBAR 1 3. H itungan p emanfaatan b erlebihan d i  Wa  =  2.
Pada b aris 8 ,  jumlah s umber d aya y ang d isediakan p m(i) d ari  sekumpulan
potongan  pasokanP..{}  dihitung d an d ibatasi  oleh  batasan p ada  Persamaan
2-5.  Selain i tu, p emanfaatan  irisan s etelah s umbangan  sumber d aya h arus
R  {..}dan  daftar  penyedia  irisan P {..}, d an k edua  daftar  R{.. d an P {..} a kan
berada d i  antara  batas b awah ÿ   dan b atas  atas  ÿ.
diteruskan k e A lgoritma  2  untuk m  endapatkan j umlah  sumber  daya  yang a kan   Jumlah  sumber d aya y ang d isediakan y ang d iminta  dari p emohon
menyediakan  pm(i) d an  jumlahnya  sumber  daya  yang  diminta  r(i). K emudian
|     | dan d isediakan o leh  penyedia m  |  i risan d ihitung o leh  fungsi  biaya,  C, a salkan   |     |     |
| --- | ---------------------------------- | ------------------------------------------------------- | --- | --- |
untuk s emua i risan  penyedia  di j endela W  a d alam  daftar  penyedia  yang   semua b atasan d alam P ersamaan  2 h ingga  5 t erpenuhi.
diperkirakan  P  {..}, p emanfaatan  berlebih X  a dalah j umlah  penghitungan
pemanfaatan  berlebih 1 00%  untuk  perkiraan b andwidth ( yt),  jika X ÿ  z,  di
N
wmxm
mana z  a dalah  jumlah  penghitungan  Pemanfaatan  berlebihan 1 00%  untuk   menit(C) =  m=1 (1)
semua i risan  SLi  di j endela  Wa  menggunakan  bandwidth a ktual  yt, p m(i)
Batasan:
akan d ihapus  dari d aftar  penyedia P   {..} u ntuk m  enghindari k elaparan
N
bandwidth.
|     |     | xm ÿ   pt |     | (2) |
| --- | --- | --------- | --- | --- |
Algoritma  2  menunjukkan  perhitungan  penawaran d an p ermintaan  dimana   m=1
kompleksitas A lgoritma  2  adalah O  (nmh).  Pada  baris  4, p ermintaan  r(i)   sore(i) ÿ   Ai  (t) ÿ   Si (3)
dihitung  dari s ekumpulan  peminta i risan  R { ..} y ang  dibatasi  pada  nilai  antara   N N
|     | menit  sore(i) ÿ  ÿ   xm  ÿ |     | Maks s ore ( i) |     |
| --- | --------------------------- | --- | --------------- | --- |
batas  bawah  ÿ d an  batas  atas  ÿ , d an y ang  paling p enting, d ibatasi  oleh   saya=1 saya=1
| Max(rt) .        |     | x1, x 1, . . . ..,  xn  ÿ  0 |     | (4)   |
| ---------------- | --- | ---------------------------- | --- | ----- |
| JILID 1 1, 2 023 |     |                              |     | 84155 |

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic L earning Hypervisor untuk S oftware Defined Network
GAMBAR 1 4. Pemanfaatan i risan pada Wa = 3 .
84156 JILID 11, 2023

Machine Translated by Google
MK Hassan dkk.: D LFisor: Dynamic Learning H ypervisor untuk Software Defined N etwork
Algoritma 2 P erhitungan S umber Daya P enawaran dan Permintaan
Masukan: R { ..} : Daftar Kandidat Pemohon, P {..} : Daftar calon
penyedia, SLi: i risan ,y p erkiraan bandwidth dalam irisan SLi , :
i: i ndeks, z: J umlah p enggunaan b erlebihan 1 00% dalam penggunaan yt
di S Liÿpm (i), ÿ : B atas bawah, ÿ : B atas atas, A i : A lokasi B andwidth
Maksimum u ntuk i risan ke-i ,rt : total kebutuhan, Si : J aminan Bandwidth
Minimum untuk I ris k e-i, pt T otal sumber daya d ari s emua p enyedia
sumber daya O utput: C : F ungsi b iaya, pm(i) : jumlah s umber daya yang
Disediakan, r (i) : j umlah s umber daya y ang D iminta 0 1: mulai 02: :
untuk s emua l angkah waktu dalam perkiraan
potongan b andwidth y ang d i S LiÿWa do
03 u ntuk S Li d i R { ..} lakukan
04: selesaikan r(i) di ÿ ÿ kamu ÿ , Asalkan r t ÿ
Udara+r(i)
= g
i=1 r i 05:
If R { ..} ÿ = ÿ 0 6: L oop 07: E lse 0 8: u ntuk
SLi di P{..}lakukan 0 9: S elesaikan
pm(i) d i (ÿ ÿ
kamu ÿ ÿ ,
Aiÿpm(i)
H
Di m ana pm(i) ÿ A i ÿSi d an dengan ketentuan p t = sore ( saya)
saya=1
10: Ifp { ..} ÿ= ÿ 1 1: Loop 1 2:
Else 13: Selesaikan
min C //Persamaan
1 1 4: Loop
Testbed terdiri d ari l ima e ntitas fungsional yang d iwakili oleh tiga V M
yang b erada d alam satu host, r incian m esin virtual ditunjukkan pada T abel
5. P latform testbed adalah komputer d engan CPU C ore i7 2 .1 GHZ, RAM
32 G B, 1 G B a ntarmuka jaringan, sistem o perasi w indows 1 0 6 4-bit untuk
mesin host dan dengan ubuntu Linux u ntuk V M v irtual tamu. Tabel 5
GAMBAR 1 5. H itungan p emanfaatan b erlebihan d i Wa = 3. menunjukkan IP VM yang d iuji
N
menit ( rt) ÿ xm ÿ M aks(rt) (5) Seperti yang d igambarkan p ada G ambar 6 , V irtual N etwork Manager
m=1
(VNM) awalnya m embuat j aringan fisik menggunakan s imulator M ININET-
Fungsi biaya dan batasannya d iadopsi dari k erangka E nter-priseVisor [35]. SDN. Kemudian, jaringan f isik ditemukan d an diinisiasi o leh hypervisor
Output dari A lgoritma 2 adalah j umlah sumber d aya yang disediakan p m(i) Libera. P engontrol VN y ang m erupakan ONOS d alam kasus kami harus
dan jumlah sumber d aya yang dimintar(i) y ang digunakan oleh a lgoritma 2 diaktifkan d i V M O NOS m enggunakan. Segera setelah jaringan f isik
untuk a lokasi i risan. diaktifkan, Libera m embangun b eberapa jaringan vSDN sambil
mempertahankan i solasi jaringan. Ini dipilih s ebagai platform e mulasi
Pekerjaan ini didasarkan pada perluasan modul manajemen s umber karena f leksibilitasnya dalam membuat VN d an kemudahan penggunaan
daya yang tertanam dalam k erangka E nterpriseVisor. Lebih j auh l agi, fitur p emrogramannya. VNM s etiap p enyewa b ertindak sebagai operator
makalah i ni mengadopsi topologi yang sama d engan y ang digunakan pada [ 35] VN d an mengajukan berbagai permintaan ke L ibera. P erlu d isebutkan
Selain i tu, test bed dengan h ypervisor Libera menggunakan p latform bahwa, kerangka kerja y ang d iusulkan b erinteraksi s ecara h orizontal
emulasi. G ambar 5 menunjukkan komponen test bed. dengan lalu lintas s ehingga t idak m engganggu secara v ertikal a rus l alu
Gambar 6 menunjukkan diagram urutan u ntuk s kenario pengujian, lintas/jalur l alu lintas a ntara p engontrol d an vSwitches ( Gambar 5), oleh
termasuk interaksi antara DLFisor, j aringan vSDN, dan L ibera. karena i tu kerangka tersebut memiliki
JILID 1 1, 2 023 84157

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic Learning Hypervisor u ntuk S oftware Defined Network
GAMBAR 1 6. Pemanfaatan irisan pada W a = 4 .
Latensi F lowVisor y ang sama s ebesar 1 7 md k etika aliran Permintaan d iklasifikasikan menjadi dua kategori:
baru OpenFlow diproses d an m eningkatkan latensi respons penyediaan topologi dan modifikasi topologi. P ertama, VNM
status port sekitar 0 ,71 md ketika s tatus p ort O penFlow mulai m embuat V N d engan topologi d an entitas VN t ertentu.
diminta s erupa d engan latensi EnterpriseVisor [35]. Istilah ' 'entitas v irtual'' mengacu p ada s emua entitas yang t erdiri d ari
84158 JILID 11, 2023

Machine Translated by Google
MK Hassan dkk.: D LFisor: Dynamic Learning H ypervisor untuk Software Defined N etwork
TABEL 5. Alamat I P t estbed.
memodifikasi i risan seperti yang digambarkan p ada Gambar 6, langkah 6. Gambar 7
menunjukkan keluaran dari pembuatan irisan s atu.
Empat VN d ibuat di Libera. Gambar 7 dan 8 menunjukkan h asil k reasi
irisan s atu. Gambar 7 menunjukkan p embuatan irisan s atu, mewakili i risan
ATN-OBY yang disebut s ebagai penyewa _ id 1; i risan t ersebut dipetakan
ke s akelar fisik dengan ID sakelar, p ort, dan t autan y ang sesuai. Selain
itu, i risan j uga dikaitkan dengan Pengontrol O NOS y ang sesuai p ada
10.0.0.3 m elalui port 1 000: TCP. G ambar 8 menunjukkan pesan log y ang
lebih rinci, termasuk pembuatan saklar dan t autan. G ambar 9 menunjukkan
skrip yang digunakan u ntuk mengubah b atas b andwidth irisan p ada
langkah nomor 6 pada G ambar 6 dan s ebagai hasil d ari algoritma 1 d an 2 .
Gambar 8 menunjukkan pesan log terperinci selama pembuatan irisan ATN-
OBY menunjukkan s krip yang digunakan u ntuk mengontrol d isiplin a ntrian
lalu lintas (secara default, First i n First Out F IFO). Ini d idasarkan pada
perintah k ontrol lalu lintas di Linux yang memungkinkan konfigurasi
penjadwalan p aket u ntuk mendukung qdisc. D i sisi l ain, a rgumen tbf
menunjukkan bahwa mekanisme filter keranjang token m engontrol arus lalu
lintas. D inyatakan d i sini b ahwa kecepatannya dibatasi h ingga 9 0Mbps.
Alat I PERF d igunakan s ebagai generator beban u ntuk m enekankan
bandwidth irisan V N
V. HASIL D AN P EMBAHASAN
Dalam pekerjaan i ni, a lgoritma alokasi sumber daya yang diusulkan hanya
dapat melayani s atu peminta s umber daya pada w aktu m ax(g) = 1 , d an
jumlah m aksimum p enyedia sumber daya adalah e mpat m ax(h) = 4 . O leh
karena itu, prioritas ditetapkan k e p eminta i risan.
Prioritasnya masing-masing diberikan kepada L TE, ATN-OBY, ATN-PSD
dan M PLS. Untuk m enciptakan b atasan sumber daya dalam b andwidth
GAMBAR 1 7. H itungan p emanfaatan b erlebihan d i Wa = 4. jaringan, jumlah m aksimum t otal sumber daya yang diminta dan d isediakan
dipilih sama dengan (rt ) = ( pt ). B atasan b andwidth maksimum untuk i risan
adalah 9 0 Mbps untuk ATN-OBY d an A TN-PSD, 1,43 Gbps untuk irisan
VN, seperti vSwitches, port, dan t autan. Misalnya, VNM dapat menentukan MPLS d an 1 ,5 Gbps u ntuk irisan L TE. K apasitas jaringan m aksimum M
apakah vSwitch a dalah O penFlow, white-box, atau P 4. Selain itu, V NM adalah 3 ,2 G bps d an t ingkat pemanfaatan target, batas p emanfaatan
dapat membangun beberapa p ort pada setiap s witch virtual. Demikian pula, bawah, d an b atas pemanfaatan atas d ipilih masing-masing menjadi i deal
tautan v irtual d apat d ibangun d engan m enghubungkan dua p ort virtual. (ux ) = 50%, ÿ = 4 0% dan ÿ = 6 0%.
Pada Gambar 6 s etelah VNM membuat V N dan A ntarmuka J aringan
virtual ( NI) t erkait, penyewa m engoperasikan VN m elalui pengontrol V N Nilai-nilai ini ditentukan s ecara empiris berdasarkan potongan k umpulan
(VNC). VNC dapat mengkonfigurasi vSwitch a tau p ort virtual d engan data yang dikumpulkan untuk m enciptakan situasi d i mana p enyedia
mengirimkan p esan perintah ke Libera m elalui I 2 (saluran kontrol). Libera sumber daya dapat mengalami k ekurangan sumber daya sambil
menawarkan saluran k ontrol untuk s etiap saklar v irtual. Mengingat vSwitch menyediakan kelebihan sumber daya mereka pada w aktu s aat ini (t j ) d an
hanya dimiliki oleh satu VN, setiap p esan kontrol V N dirutekan secara hingga ( t j +n ) di mana n adalah j umlah l angkah waktu y ang diperkirakan.
terpisah ke L ibera. Untuk aturan A liran (FR), VNC d apat menginstal F R Gambar 1 0 menunjukkan p emanfaatan masing-masing irisan A TN-OBY,
yang d iinginkan ke v Switch m ana pun k apan saja, sehingga memungkinkan ATN-PSD, LTE, dan M PLS, dengan dan t anpa alokasi sumber daya
paket diteruskan a tau dihapus s ecara dinamis. Selain i tu, L ibera menggunakan kerangka p embelajaran d inamis (DLF) u ntuk semua l angkah
mengumpulkan d ata statistik d ari v Switches dan p ort virtual. Oleh k arena waktu d i jendela 1 yang disediakan t jÿyt di SLiÿWa(a = 1 dan j = 1 sampai
itu, DLFisor d apat mengkonfigurasi u lang a tau 50, yaitu 50 langkah waktu p ertama); d imana garis b iru pada g rafik
menunjukkan p emanfaatan irisan s ebenarnya (asli).
JILID 1 1, 2023 84159

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic Learning Hypervisor u ntuk S oftware Defined Network
GAMBAR 18. Pemanfaatan irisan pada W a = 5.
tanpa menggunakan algoritma alokasi s umber d aya yang dijadikan b enchmark irisan lain y ang d iminta s eperti L TE, k arena pemanfaatan i risan LTE lebih dari
dalam penelitian ini. D i jendela satu d an b erdasarkan pemanfaatan i risan, i risan batas atas u i ÿ ÿ , dimana ÿ = 6 0% d an pemanfaatan i risan lainnya kurang dari
ATN-OBY, irisan ATN-PSD, dan irisan MPLS d ianggap sebagai p enyedia batas bawah ui ÿ ÿ dimana ÿ = 40% p ada pemanfaatan t arget (ux ) = 50%;
sumber d aya k arena p emanfaatannya yang rendah ui ÿ ÿ, s edangkan irisan asalkan s emua b atasan dan batasan terpenuhi p ada Persamaan 1 sampai 5 .
LTE dianggap sebagai peminta s umber daya u i ÿ ÿ . Garis o ranye menggambarkan pemanfaatan b aru t anpa D LF.
Pada l angkah waktu 1 d an Menurut a lgoritma 1 d an 2 , A TN- Gambar 1 0a menunjukkan bahwa pemanfaatan i risan tanpa D LF m elebihi
Irisan O BY, ATN-PSD, dan MPLS a kan m enyediakan s umber daya u ntuk itu pemanfaatan p enuh sebesar 1 00%, y ang menyebabkan irisan menjadi kelaparan
84160 JILID 11, 2023

Machine Translated by Google
MK Hassan dkk.: D LFisor: Dynamic Learning H ypervisor untuk Software Defined N etwork
DLF yang kami u sulkan. A nalisis yang sama d iterapkan pada potongan
ATN-PSD p ada Gambar 10b. S ementara i tu, pada irisan MPLS,
pemanfaatan alokasi sumber d aya dengan DLF meningkat k arena sumber
daya tambahan d iberikan kepada pemohon u ntuk mengkompensasi s umber
daya yang hilang dari i risan ATN-OBY d an A TN-PSD y ang dijatuhkan.
Gambar 11 m enunjukkan hitungan berapa kali p emanfaatan irisan melebihi
pemanfaatan 100% untuk A TN-OBY ( a) d an ANT-PSD pada ( b).
Pada G ambar 11a, i risan ATN-OBY d igunakan secara b erlebihan 27
kali lebih b anyak d ibandingkan saat m enggunakan yang asli (tanpa alokasi
sumber daya) d an saat m enggunakan DLF kami, yang mengonfirmasi
keefektifan algoritme yang diusulkan. Namun, pada bagian ATN-PSD,
alokasi sumber daya tanpa DLF menyebabkan p emanfaatan berlebihan
30 k ali l ebih b anyak d ibandingkan DLF. G ambar 12 m enunjukkan
pemanfaatan irisan untuk jendela 2 u ntuk s emua t jÿyt di S LiÿWa ( a = 2 dan
j = 5 1 h ingga 100). D emikian pula, grafik m enunjukkan p emanfaatan irisan
aktual (asli) tanpa menggunakan algoritma alokasi sumber d aya dan tanpa
DLF.
Di j endela 2 , ATN-OBY p ada l angkah waktu 51 d an 53 a dalah penyedia
sumber d aya ketika alokasi tanpa DLF digunakan.
Hal i ni disebabkan pemanfaatannya yang rendah, ÿ < 4 0% ( kotak biru).
Namun demikian, p ada l angkah 56, i risan meminta s umber d aya karena
pemanfaatannya lebih t inggi d ari b atas a tas, ÿ > 6 0%.
Selain i tu, irisan ATN-OBY a dalah peminta sumber d aya pada l angkah
waktu 66 m enggunakan alokasi sumber d aya dengan DLF. D i s isi lain,
irisan ATN-PSD p ada langkah waktu 53 d an 56 m asing-masing merupakan
penyedia s umber daya dan peminta sumber d aya ketika menggunakan
alokasi tanpa DLF (kotak biru) dan dengan DLF (kotak o ranye). Baik pada
ATN-OBY m aupun ATN-PD, g aris o ranye menunjukkan b ahwa
pemanfaatan irisan melebihi pemanfaatan penuh s ebesar 100%, y ang
menyebabkan i risan kekurangan sumber d aya karena ketidakmampuan
memulihkan sumber daya yang disediakan (disumbangkan) yang sedang
digunakan. H al ini terutama disebabkan oleh p enerapan a lgoritma a lokasi
sumber d aya pada b enchmark secara r eal-time tanpa mempertimbangkan
kebutuhan di m asa d epan. G aris kuning m enunjukkan pemanfaatan irisan
menggunakan DLF yang kami u sulkan. B erbeda dengan alokasi resource
tanpa menggunakan DLF yang berwarna kuning, a lokasi resource
menggunakan DLF tidak menyebabkan o verutilisasi ( pemanfaatan
bandwidth). Hal ini terutama disebabkan oleh h ilangnya potongan tersebut
dari d aftar kandidat penyedia s umber d aya P { ..} karena perhitungan
GAMBAR 1 9. H itungan p emanfaatan b erlebihan d i Wa = 5.
permintaan d an penawaran u ntuk langkah 50 k ali b erikutnya m enunjukkan
kekurangan sumber d aya ketika menggunakan alokasi sumber daya t anpa
untuk sumber daya k arena ketidakmampuan untuk memulihkan s umber DLF (grafik oranye). D i sisi lain, i risan LTE adalah peminta sumber d aya
daya y ang d isediakan (disumbangkan) karena p emanfaatan irisan lainnya. dan sumber d aya yang diminta dalam a lokasi tanpa DLF disediakan o leh
Hal ini terutama disebabkan o leh p enerapan algoritma alokasi s umber d aya irisan ATN-OBY p ada l angkah waktu 51 d an dari s emua i risan lainnya p ada
dalam b enchmark (EnterpriseVisor) secara real-time t anpa langkah waktu 53. H al i ni terlihat j elas pada p enurunan t ajam d alam s umber
mempertimbangkan kebutuhan d i masa d epan. D i s isi l ain, dalam alokasi daya yang dikonsumsi pada langkah w aktu 53. S ementara itu, jumlah
sumber daya p asokan d an permintaan algoritma yang kami u sulkan, sumber d aya yang lebih t inggi d isediakan oleh i risan MPLS, yang tercermin
penghitungannya didasarkan pada p erkiraan k onsumsi sumber daya di dalam peningkatan konsumsi sumber d aya yang lebih t inggi k etika
masa d epan (disorot dengan g aris kuning). Oleh karena i tu, telah diketahui menggunakan alokasi dengan DLF. P eningkatan tajam d alam hasil ini
sebelumnya apakah akan t erjadi kekurangan sumber d aya atau tidak untuk m engkompensasi jumlah s umber d aya yang awalnya d isediakan oleh
sebelum memutuskan untuk tidak m empertimbangkan (mencoret) p enyedia irisan yang dihilangkan (irisan A TN-OBY d an irisan ATN-PSD). G ambar
sumber daya ( doner) d ari p ertimbangan sebagai calon p enyedia sumber 13a dan Gambar 13b menunjukkan hitungan b erapa kali pemanfaatan
daya P {..}. G aris k uning m enunjukkan b ahwa p emanfaatan irisan tetap irisan melebihi pemanfaatan 100% masing-masing untuk irisan ATN-OBY
sama d engan p emanfaatan irisan asli karena i risan tidak dianggap sebagai dan irisan ATN-PSD.
penyedia irisan s etelah digunakan
JILID 1 1, 2023 84161

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic L earning Hypervisor untuk S oftware Defined Network
GAMBAR 2 0. Pemanfaatan irisan pada W a = 6 .
Tidak ada pemanfaatan berlebihan irisan yang teramati m enggunakan algoritma. G ambar 14 m enunjukkan pemanfaatan irisan untuk jendela 3
DLF yang d iusulkan d ibandingkan dengan alokasi s umber d aya asli tanpa untuk s emua t jÿyt di S LiÿWa ( a = 3 dan j = 1 01 hingga 150) d engan dan
DLF, yang m enegaskan keefektifan dari usulan t ersebut. tanpa DLF.
84162 JILID 1 1, 2023

Machine Translated by Google
MK  Hassan  dkk.: D LFisor:  Dynamic  Learning H ypervisor  untuk  Software  Defined N etwork
mempertimbangkan  (menjatuhkan) p enyedia s umber d aya  (doner) d ari
pertimbangan  sebagai c alon  penyedia s umber d aya  P{..}.  Garis  kuning
menunjukkan b ahwa  pemanfaatan  irisan  tetap s ama d engan p emanfaatan
irisan  asli k arena i risan  tersebut  tidak  dianggap s ebagai p enyedia i risan
setelah m  enggunakan  DLF  yang  kami  usulkan. A nalisis  yang  sama
| diterapkan  pada i risan  ATN-OBY  untuk l angkah w  |     | aktu  100 h ingga 1 20.   |
| ---------------------------------------------------- | --- | ------------------------- |
Hasil a lokasi  sumber d aya  di  atas  menunjukkan  bahwa  sumber d aya
| alokasi  menggunakan  DLF  (garis k uning) m                       | engurangi  pemanfaatan   |              |
| ------------------------------------------------------------------ | ------------------------ | ------------ |
| berlebihan  dibandingkan  dengan  yang  lain.  Gambar 1 5a  dan G  |                          | ambar  15b   |
menunjukkan h itungan b erapa  kali p emanfaatan  irisan  melebihi t anda
pemanfaatan  100%  untuk  masing-masing i risan  ATN-OBY  dan i risan  ATN-PSD.
| Dari  Gambar 1 5a d an G  | ambar 1 5b, a lokasi  sumber d aya  dengan  DLF   |     |
| ------------------------- | ------------------------------------------------- | --- |
mengurangi  jumlah  pemanfaatan  berlebihan  100%  untuk  potongan A TN-
OBY  dan  mempertahankan j umlah  yang  tepat d ibandingkan  dengan r asio
asli u ntuk p otongan  ATN-PSD. B erbeda d engan i risan  ATN-OBY,  alokasi
| sumber d aya  yang  diusulkan  dengan D  | LF  meningkatkan  alokasi  sumber   |     |
| ---------------------------------------- | ----------------------------------- | --- |
daya  dengan  mengurangi  jumlah  penggunaan  berlebihan  seperti y ang
| digambarkan  pada G  ambar  15b. G  | ambar 1 6  menunjukkan  pemanfaatan   |     |
| ----------------------------------- | ------------------------------------- | --- |
irisan  untuk j endela 4   untuk s emua t jÿyt d i  SLiÿWa ( a  =  4  dan  j =   151 h ingga
| 200) d engan  dan  tanpa D  LF. |     |     |
| ------------------------------- | --- | --- |
Pada G  ambar 1 6,  irisan  LTE  merupakan  peminta  sumber d aya  karena
| ÿ  >  60%,  sedangkan i risan  ATN-OBY  dan  ATN-PSD m  |     | enyediakan  sumber   |
| ------------------------------------------------------- | --- | -------------------- |
daya  ke  irisan  LTE  pada l angkah 1 51  (karena  rendahnya  pemanfaatan  ÿ <
| 40%  pada w  arna b iru). k otak). H  | al i ni  pada a khirnya m  | enyebabkan   |
| ------------------------------------- | -------------------------- | ------------ |
kekurangan  sumber d aya  untuk i risan  ATN-OBY,  dan A TN-PSD s eperti
| yang  digambarkan  dalam g aris o ranye p ada G  | ambar 1 6a d an 1 6b .   |     |
| ------------------------------------------------ | ------------------------ | --- |
Sebaliknya, k etika  menggunakan  DLF,  karena  alokasi s umber  daya
penawaran  dan  permintaan  didasarkan p ada p erkiraan  konsumsi  sumber
daya,  kedua i risan  dikecualikan  dari d aftar p enyedia s umber d aya  P  {..}
| seperti y ang  diilustrasikan  oleh  garis  kuning  pada G  |     | ambar 1 6a  dan 1 6b.   |
| ----------------------------------------------------------- | --- | ----------------------- |
| Oleh  karena i tu,  terdapat  pengetahuan  sebelumnya m     |     | engenai  apakah a kan   |
| terjadi k ekurangan  sumber d aya  atau t idak,  sebelum m  |     | emutuskan  untuk        |
tidak  mempertimbangkan  (mencoret) p enyedia s umber d aya  (doner)
sebagai c alon  penyedia s umber d aya.  Garis  kuning  menunjukkan b ahwa
pemanfaatan  irisan  tetap s ama d engan p emanfaatan  irisan  asli k arena
| irisan  tersebut t idak  dianggap s ebagai p enyedia i risan  setelah m  |     | enggunakan           |
| ------------------------------------------------------------------------ | --- | -------------------- |
| DLF  yang  diusulkan.  Sebaliknya, p otongan  MPLS m                     |     | enyediakan s umber   |
daya  ke  potongan  LTE  masing-masing p ada l angkah 1 53 d an 1 55. D  i s isi
| lain,  mengenai  alokasi  sumber d aya  dengan D  | LF,  potongan  ATN-OBY   |     |
| ------------------------------------------------- | ------------------------ | --- |
menerima  sumber d aya  dari p otongan  LTE  pada l angkah 1 62. J elas b ahwa
GAMBAR 2 1. H itungan p emanfaatan b erlebihan d i  Wa  =  6.
| alokasi  sumber d aya  dengan D                            | LF  mengurangi  pemanfaatan  keseluruhan   |              |
| ---------------------------------------------------------- | ------------------------------------------ | ------------ |
| dan  jumlah  pemanfaatan  berlebihan.  Gambar 1 7a d an G  |                                            | ambar  17b   |
Di  jendela i ni,  irisan  ATN-OBY d an A TN-PSD m  enyediakan  sumber   menunjukkan  berapa  kali p emanfaatan  irisan  melebihi t anda p emanfaatan
100%  untuk m  asing-masing i risan  ATN-OBY  dan A TN-PSD.
daya d ari  langkah  100–105 k ali  ke  irisan  LTE  tanpa  menggunakan  DLF
karena  pemanfaatannya  yang r endah  ÿ  < 4 0% ( kotak  biru). D  i  sisi  lain,
pada  langkah  waktu 1 20,  ATN-OBY  meminta  sumber d aya y ang d isediakan   Dari  Gambar 1 7a  dan G  ambar 1 7b, a lokasi  sumber d aya  menggunakan
DLF  pada i risan  ATN-OBY  mengurangi  jumlah  pemanfaatan  berlebih
irisan  LTE  dan M  PLS  karena p emanfaatan  ATN-OBY  mendekati u tilisasi
100% ( dalam w  arna  biru-asli)  dan ( berwarna  kuning d engan  DLF).   dibandingkan  dengan a slinya  dan a lokasi  tanpa D  LF.  Demikian  pula, p ada
Sebaliknya,  karena p emanfaatannya  yang r endah  ÿ<40%,  potongan  MPLS   potongan  ATN-PSD,  alokasi  menggunakan  DLF  mengurangi  pemanfaatan
menyediakan  sumber d aya p ada l angkah  waktu  104  dan  106 k e  potongan   berlebihan  menjadi n ol,  serupa d engan p emanfaatan  sebenarnya.  Gambar
LTE.  Di j endela  ini,  potongan  ATN-PSD  tidak  menyediakan  sumber d aya   18  menunjukkan  pemanfaatan  irisan  untuk j endela 5   untuk s emua t jÿyt  di
apa p un k arena  perhitungan a lokasi  pasokan  dan  permintaan  didasarkan   SLiÿWa  (a  =  5  dan  j =   201 h ingga 2 50)  dengan d an t anpa
pada  perkiraan k onsumsi s umber  daya. DLF.
Pada  Gambar 1 8,  irisan  ATN-OBY,  ATN-PSD,  dan  MPLS ( karena
Oleh k arena i tu,  akan a da  pengetahuan  sebelumnya  mengenai  apakah a kan t erjadi   rendahnya  pemanfaatan  ÿ <   40% d alam k otak  biru)  menyediakan s umber
kekurangan  sumber d aya a tau t idak  sebelum  memutuskan u ntuk t idak  melakukan  hal t ersebut daya  ke  irisan  LTE  pada l angkah w  aktu  201 s ejak
JILID 1 1,  2023 84163

Machine Translated by Google
MK Hassan dkk.: D LFisor: D ynamic Learning Hypervisor u ntuk S oftware Defined Network
GAMBAR 22. Pemanfaatan irisan pada Wa = 6.
LTE a dalah pemohon sumber daya dengan ÿ > 60%. Hal ini p ada akhirnya perkiraan konsumsi sumber d aya; k edua i risan dikecualikan dari daftar
menyebabkan kekurangan sumber d aya untuk ATN-OBY, dan ATN-PSD penyedia s umber d aya P {..}. Hal ini menjelaskan rendahnya pemanfaatan
seperti yang d igambarkan dalam g aris merah pada Gambar 18a d an 18b. pada A TN-OBY dan ATN-PSD ( warna kuning s esuai d engan pemanfaatan
Sedangkan untuk a lokasi s umber d aya menggunakan DLF, i risan M PLS sebenarnya). D i sisi lain, A TN-OBY juga meminta s umber d aya pada
hanya m enyediakan sumber d aya yang diminta d an mengkompensasi langkah waktu 210 yang disediakan o leh potongan LTE. ATN-PSD j uga
sumber daya y ang h ilang d ari A TN-OBY d an ATN-PSD karena perhitungan meminta s umber d aya pada l angkah waktu 212, yang juga disediakan o leh
alokasi sumber daya p enawaran dan p ermintaan d idasarkan pada LTE. Gambar 1 9a dan 19b menunjukkan h itungannya
84164 JILID 1 1, 2023

Machine Translated by Google
MK H assan d kk.: DLFisor: D ynamic Learning Hypervisor u ntuk S oftware Defined N etwork
menunjukkan h itungan berapa k ali pemanfaatan i risan m elebihi p emanfaatan
100% m asing-masing u ntuk irisan A TN-OBY dan i risan ATN-PSD.
Pada Gambar 2 1, a lokasi sumber d aya ATN-PSD s ecara s ignifikan
meningkatkan p emanfaatan berlebihan d ibandingkan dengan a lokasi tanpa D LF.
Gambar 2 2 m enunjukkan p emanfaatan irisan untuk jendela 7 u ntuk semua tjÿyt d i
SLiÿWa(a = 7 d an j = 3 00 h ingga 350) d engan d an t anpa D LF.
Di w indows 7, h anya potongan M PLS dengan ÿ < 40% yang menyediakan
sumber d aya ke LTE dengan ÿ > 60%. Sedangkan irisan ATN-OBY dan A TN-PSD
tidak menyediakan a tau m enerima sumber d aya apa p un.
Gambar 2 3a d an 2 3b m enunjukkan h itungan berapa k ali p emanfaatan irisan
melebihi p emanfaatan 100% m asing-masing u ntuk irisan A TN-OBY dan A TN-PSD.
Secara k eseluruhan, DLVisor dapat m eningkatkan a lokasi sumber d aya
dibandingkan dengan t olok ukur kami ( EnterpriseVisor)
dengan 1 - M engurangi d an m enghilangkan p emanfaatan b erlebihan irisan di
Enter-
priseVisor 2- M engurangi k ekurangan s umber d aya akibat d onasi sumber d aya
yang dilakukan oleh modul m anajemen sumber d aya di E nterpriseVisor
3 - Meningkatkan p emanfaatan
irisan vSDN secara k eseluruhan
VI. KESIMPULAN
Sebagai k esimpulan, makalah ini menunjukkan p engembangan dan i mplementasi
metode pengelolaan s umber daya irisan (bandwidth) di v SDN. D itemukan bahwa
pengelolaan s umber d aya dan a lokasi sumber d aya bandwidth, khususnya p ada
waktu a ktual saat ini, dapat m enyebabkan kekurangan s umber d aya karena
pemanfaatan sumber d aya yang berlebihan; t erutama m engingat perhitungan
pasokan d an p ermintaan s umber d aya dalam s olusi pengelolaan s umber d aya
terkait t idak memperhitungkan permintaan d i m asa d epan d an p erubahan c epat
dalam profil l alu lintas. Oleh karena itu, diperlukan kerangka p engelolaan s umber
daya yang proaktif dan c erdas. Oleh karena itu, algoritma peramalan s umber daya
(lalu lintas) y ang akurat dan k uat sangatlah p enting. Oleh karena itu, DLFisor
dikembangkan d engan k erangka pembelajaran d inamis yang menggabungkan
GAMBAR 2 3. Hitungan p emanfaatan berlebihan di Wa = 7.
algoritme ML berbantuan halus u ntuk mempelajari (memperkirakan) p ermintaan di
masa d epan. I a b ereaksi dan b eradaptasi t erhadap p erubahan signifikan d alam
berapa kali p emanfaatan irisan melebihi pemanfaatan 100% untuk A TN-OBY dan profil lalu lintas m enggunakan pendeteksi perubahan konsep dan p engujian
ATN-PSD. Dari Gambar 19, pengelolaan sumber d aya signifikan. M etode berbasis jendela digunakan u ntuk mengurangi a tau
menggunakan DLF m engungguli alokasi sumber d aya t anpa DLF d an menghilangkan f luktuasi lalu lintas d ata, y ang dapat m enurunkan kinerja ML s eperti
meningkatkan pemanfaatan irisan untuk p enyedia sumber daya A TN-OBY d an penelitian sebelumnya. T erakhir, k erangka p embelajaran dinamis y ang ditingkatkan
ATN -Irisan PSD. Gambar 20 menunjukkan pemanfaatan i risan untuk jendela 6 diterapkan p ada k erangka pengelolaan s umber d aya untuk memberikan
untuk semua t jÿyt d i SLiÿWa ( a = 6 d an j = 251 h ingga 3 00) d engan dan t anpa DLF. peningkatan p emanfaatan sumber d aya dan m enghilangkan p emanfaatan
berlebihan y ang diakibatkan o leh perhitungan penawaran d an p ermintaan.
Pada Gambar 20, di Jendela 6 p ada langkah waktu 2 51 d an t anpa DLF, irisan
ATN-PSD dan MPLS ( karena rendahnya pemanfaatan ÿ < 40% d alam kotak b iru)
menyediakan sumber daya untuk i risan LTE karena ÿ > 60%. Sementara i tu,
dengan menggunakan DLF d an m engingat perhitungan alokasi sumber d aya REFERENSI
penawaran dan permintaan didasarkan p ada perkiraan konsumsi sumber d aya, [1] A . Blenk, A . Basta, M. Reisslein, dan W. Kellerer, ' 'Survei p ada h ypervisor
virtualisasi jaringan untuk j aringan yang ditentukan p erangkat lunak,'' IEEE C ommun.
potongan ATN-PSD d ikecualikan dari d aftar penyedia sumber d aya P {..}
Survei Tuts., v ol. 1 8, tidak. 1, hal. 655–685, Kuartal 1, 2016.
[2] A . Kivity, Y. Kamay, D. Laor, U. Lublin, dan A. Liguori, ''kvm: Monitor m esin
(Garis k uning s ejajar dengan sebenarnya) seperti p ada Gambar 2 0b. D engan virtual Linux,'' di Proc. Linux S ymp., K anada, Amerika, J uni 2007, hlm.225–230.
demikian, M PLS m engkompensasi jumlah yang h ilang dengan sumber d aya t ambahan.
[3] C A Waldspurger, ''Manajemen sumber d aya memori di server V Mware E SX,'' S istem Operasi
Hal i ni membenarkan peningkatan p emanfaatan di MPLS u ntuk a lokasi
ACM S IGOPS. Pdt., jilid. 3 6, h lm. 181–194, Desember 2002.
menggunakan DLF ( garis K uning) pada Gambar 2 0d. G ambar 2 1a d an G ambar 2 1b
JILID 1 1, 2023 84165

Machine Translated by Google
MK Hassan dkk.: DLFisor: D ynamic Learning H ypervisor untuk Software D efined Network
[4] AA Blenk, ' 'Menuju v irtualisasi j aringan yang ditentukan p erangkat l unak: A nalisis, [26] N . F eamster, J. R exford, dan E . Z egura, ''Jalan m enuju S DN: Sejarah i ntelektual
pemodelan, d an p engoptimalan,'' D ept. E lectron. I nf. Technol., T echnis-che jaringan yang d apat diprogram,'' A CM S IGCOMM C omput. Komunitas.
Universität M ünchen, M unich, J erman, T ech. Rep.21.11.2017, 2 018. Pdt., j ilid. 44, t idak. 2, hlm.87–98, A pril 2 014.
[5] F. R odríguez-Haro, F . F reitag, L. N avarro, E. Hernánchez-sánchez, N. F arías-Mendoza, [27] R . S herwood, M . Chan, A. C ovington, G . G ibb, M. F lajslik, N. H andigol, T .-Y. H uang, P .
JA G uerrero-Ibáñez, dan A . González-Potes, ' 'Ringkasan t eknik virtualisasi,' ' P roses. Kazemian, M . Kobayashi, J . N aous, S . S eetharaman, D. U nderhill, T . Y abe, K.-K.
Teknologi., j ilid. 3 , h lm. 2 67–272, J anuari 2 012. Yap, Y . Y iakoumis, H. Z eng, G. A ppenzeller, R. J ohari, N . M cKeown, dan G . P arulkar,
''Mengukir p enelitian dari jaringan produksi Anda dengan OpenFlow,'' ACM S IGCOMM
[6] T. A nderson, L. P eterson, S. Shenker, dan J. T urner, ''Mengatasi kebuntuan Internet Comput.
melalui virtualisasi,'' C omputer, v ol. 38, tidak. 4 , hlm. 3 4–41, April 2005. Komunitas. P dt., j ilid. 40, t idak. 1, hlm. 129–130, J anuari 2 010.
[28] R . S herwood, G . G ibb, K.-K. Y ap, G . A ppenzeller, M. C asado, N. M cKeown, dan G.
[7] M. Y u, J . Rexford, X . Sun, S . Rao, d an N. F eamster, ''Survei p enggunaan L AN v irtual Parulkar, ' 'Flowvisor: L apisan virtualisasi j aringan,'' O penFlow S witch C onsortium,
di j aringan k ampus,'' I EEE C ommun. Mag., jilid. 4 9, tidak. 7 , h lm. 98–103, J uli 2011. vol. 1, hal. 132, O ktober 2009.
[29] N . V an G iang dan Y H Kim, ' 'Mengiris jaringan inti p aket seluler berikutnya,'' di P roc.
[8] A. B elbekkouche, M d. M . H asan, d an A. Karmouch, ' 'Penemuan d an alokasi s umber ke-11 I nt. G ejala. K omunikasi Nirkabel. s istem. (ISWCS), Agustus 2014, h lm.901–904.
daya dalam virtualisasi j aringan,'' I EEE Commun. Survei T uts., vol. 14, tidak. 4 , hal.
1114–1128, Kuartal 4 , 2 012. [30] X . J in, J. R exford, dan D . W alker, ' 'Pembaruan bertahap u ntuk hypervisor SDN
[9] R. B outaba, M A S alahuddin, N. Limam, S . Ayoubi, N . S hahriar, F . E strada-Solano, dan OM komposisional,'' d i P roc. P erangkat Lunak Topik H angat L okakarya k e-3. Defined
Caicedo, ' 'Survei k omprehensif t entang p embelajaran m esin u ntuk j aringan: Evolusi, aplikasi, Netw., A gustus 2014, h lm.187–192.
dan p eluang penelitian, '' J. A plikasi Layanan I nternet, v ol. 9, tidak. 1 , h lm. 1 –99, Desember [31] A . A l-Shabibi, M. D e L eenheer, M. Gerola, A . K oshibe, W. S now, d an G . P arulkar,
2018. ''OpenVirteX: Hypervisor j aringan,'' d i P roc. B uka Jaringan.
Summit ( ONS), 2014, hlm.1–9.
[10] M HH Khairi, S HS A riffin, N MA L atiff, KM Yusof, M K Hassan, F T Al-Dhief, M. H amdan, [32] R . D origuzzi-Corin, E . S alvadori, M . G erola, M. S uñé, dan H . W oesner, ' 'Mekanisme
S. K han, d an M . H amzah, ' 'Deteksi d an klasifikasi a liran k onflik d i SDN menggunakan virtualisasi yang b erpusat p ada jalur data u ntuk jaringan OpenFlow,'' di P roc. E uro
algoritma pembelajaran m esin ,'' Akses I EEE, j ilid. 9, h al.76024–76037, 2 021. ke-3. Perangkat Lunak Lokakarya. D efined N etw., S eptember 2 014, hlm.19–24.
[33] X . J in, J. G ossels, J . R exford, dan D . W alker, ' 'CoVisor: S ebuah h ypervisor komposisi
[11] K Z Ghafoor, L. K ong, D B Rawat, E. Hosseini, d an AS S adiq, ' 'Protokol perutean s adar untuk jaringan yang d itentukan perangkat lunak,'' d i P roc. G ejala U SENIX k e-12.
kualitas l ayanan dalam Internet K endaraan y ang d itentukan p erangkat l unak,'' IEEE Sistem J aringan. Implementasi D esain. (NSDI), 2 015, hlm.87–101.
Internet Things J ., v ol. 6, t idak. 2, h lm.2817–2828, April 2019. [34] L . Liao, A. S hami, d an V CM L eung, ''Distributed F lowVisor: Platform F lowVisor
[12] M K H assan, S H Ariffin, S K Syed-Yusof, N E Ghazali, d an ME Kanona, ''Analisis h ybrid terdistribusi u ntuk virtualisasi jaringan cloud yang sadar akan kualitas layanan,'' IET
non-linear a utoregressive n eural n etwork d an teknik p emulusan l okal untuk prakiraan Netw., v ol. 4, tidak. 5, hlm. 270–277, S eptember 2 015.
irisan b andwidth,'' T ELKOMNIKA, T elecommun. H itung. E lektron. Kontrol, j ilid. 19, [35] J .-L. Chen, Y .-W. Bu, H .-Y. K uo, C .-S. Y ang, dan W .-C. H ung, ''Platform v irtualisasi
tidak. 4, h al.1078–1089, 2021. jaringan yang ditentukan perangkat lunak untuk manajemen s umber daya j aringan
perusahaan,'' IEEE Trans. M uncul. Topik K omputasi, v ol. 4, tidak. 2, hlm.179–186,
[13] M . Alauthman, N . Aslam, M . Al-kasassbeh, S. K han, A . Al-Qerem, dan K.-KR C hoo, April 2 016.
''Pendekatan d eteksi B ot-net b erbasis p embelajaran p enguatan y ang e fisien,'' J.Netw. [36] Y .Han, J .Li, D.Hoang, J.-H. Y oo, d an J W Hong, ''Platform v irtualisasi j aringan berbasis
Hitung. A plikasi, jilid. 1 50, Januari 2020, Pasal. T IDAK. 1 02479. niat u ntuk SDN,'' di P roc. k e-12 Int. K onf. jaringan.
Kelola L ayanan. ( CNSM), Oktober 2016, hlm.353–358.
[14] X . L i, S . Li, P . Zhou, d an G . C hen, ' 'Memperkirakan a liran antarmuka j aringan [37] H . Y amanaka, E . K awai, d an S . S himojo, ' 'AutoVFlow: V irtualisasi j aringan OpenFlow
menggunakan s istem p embelajaran yang luas berdasarkan algoritma p encarian area luas berskala besar,'' C omput. Komunitas, j ilid. 102, h lm. 28–46, A pril 2 017.
burung pipit,'' E ntropy, v ol. 24, tidak. 4 , h al. 4 78, M aret 2 022.
[15] A R A bdellah dan A . Koucheryavy, ''prediksi l alu lintas V ANET m enggunakan LSTM [38] H . Y amanaka, E . K awai, S . I shii, dan S . S himojo, ' 'AutoVFlow: Virtualisasi o tonom untuk
dengan pembelajaran jaringan saraf d alam,'' di Proc. I nt. Konf. Generasi Selanjutnya. jaringan OpenFlow a rea luas,'' d i P roc. E uro ke-3. Perangkat Lunak Lokakarya.
Jaringan K abel/Nirkabel. Cham, Swiss: S pringer, 2020, hlm.281–294. Defined N etw., S eptember 2 014, hlm.67–72.
[16] S K Singh, M M S alim, J . Cha, Y. P an, d an JH Park, ''Kerangka kerja sub-slicing j aringan [39] Y . H an, T. V achuska, A . A l-Shabibi, J . L i, H . H uang, W . Snow, d an J W-K. H ong,
berbasis p embelajaran mesin dalam lingkungan 5G y ang b erkelanjutan,'' ''ONVisor: Menuju p latform virtualisasi jaringan berbasis SDN y ang skalabel dan
Sustainability, v ol. 12, t idak. 1 5, hal. 6 250, Agustus 2 020. fleksibel di O NOS,'' Int. J .Netw. Kelola., v ol. 28, t idak. 2, hal. e 2012, Maret 2 018.
[17] M. Berman, J S Chase, L . Landweber, A. Nakao, M. O tt, D. R aychaudhuri, R . Ricci, d an I.
Seskar, ' 'GENI: Tempat pengujian gabungan untuk e ksperimen j aringan inovatif,'' Comput . [40] S . A gliano, M. A shjaei, M. Behnam, d an L L B ello, ''Manajemen d an k ontrol s umber
Jaringan, j ilid. 61, hlm. 5–23, Maret 2 014. daya d alam j aringan SDN t ervirtualisasi,'' d i P roc. S istem Tertanam W aktu N yata.
Teknologi. ( RTEST), 2018, hlm.47–53.
[18] H . I shio, J . Minowa, dan K . Nosu, ' 'Review d an status t eknologi multiplexing p embagian [41] V . S truhár, M. Ashjaei, M. B ehnam, S S Craciunas, dan A V P apadopoulos, ''DART:
panjang gelombang d an p enerapannya,'' J . Lightw. T eknologi., j ilid. 2, t idak. 4 , hlm. Kerangka distribusi b andwidth dinamis untuk jaringan yang ditentukan perangkat
448–463, Agustus 1 984. lunak tervirtualisasi,'' d i P roc. T ahun ke-45. K onf.
[19] X . X iao, A . Hannan, B . Bailey, dan LM Ni, ''Rekayasa lalu lintas d engan M PLS d i IEEE Ind. E lektron. sosial. ( IECON), jilid. 1 Oktober 2019, hlm.2934–2939.
Internet,'' IEEE N etw., v ol. 14, tidak. 2 , h lm. 2 8–33, April 2000. [42] L . Leonardi, L . Lo B ello, d an S . A glianó, ''Manajemen b andwidth berbasis prioritas
[20] A . L eon-Garcia dan L G Mason, ' 'Manajemen sumber d aya jaringan virtual u ntuk dalam j aringan yang ditentukan perangkat lunak tervirtualisasi,'' E lectronics, vol. 9,
jaringan generasi b erikutnya,'' I EEE Commun. Mag., j ilid. 4 1, tidak. 7 , h lm. 102–109, tidak. 6, hal. 1009, J uni 2020.
Juli 2 003. [43] G .Yang, B .-Y. Y u, H . J in, dan C . Y oo, ''Libera u ntuk virtualisasi j aringan yang d apat
[21] T . K oponen, K . Amidon, P . Balland, M . C asado, A . Chanda, B . Fulton, I. G anichev, J . diprogram,'' I EEE Commun. Mag., jilid. 58, t idak. 4, hlm. 38–44, A pril 2 020.
Gross, P. Ingram, E . Jackson, d an A. Lambeth, '' V irtualisasi jaringan di pusat d ata [44] G . Y ang, Y. Y oo, M . Kang, H. J in, dan C . Y oo, ' 'Jaminan i solasi b andwidth untuk
multi-penyewa,'' d i Proc. Gejala USENIX ke-11. jaringan virtual S DN,'' di P roc. K onferensi I EEE. Hitung. K omunitas.
Sistem Jaringan. I mplementasi D esain. (NSDI), 2014, hlm.203–216. (INFOCOM), M ei 2021, hlm.1–10.
[22] S . S henker, L . P eterson, dan J . T urner, ''Mengatasi kebuntuan Internet melalui [45] A . A hmadian d an M . Ahmadi, ''DC-CAMP: Pembuatan p engontrol dinamis, a lokasi d an
virtualisasi,'' d alam Proc. ACM H otNets-III, 2004, hlm.1–8. protokol manajemen di S DN,'' Wireless P ers. K omunitas, j ilid. 125, h lm. 531–558,
[23] H . B allani, P . Costa, T . K aragiannis, d an A. Rowstron, ''Menuju j aringan p usat d ata Februari 2 022.
yang d apat diprediksi,'' di Proc. Konferensi ACM S IGCOMM, A gustus 2011, h lm.242– [46] M K Hassan, SH S yed Ariffin, N E Ghazali, M. H amad, M. Hamdan, M . H amdi, H.
253. Hamam, d an S . K han, ''Kerangka p embelajaran dinamis untuk lalu l intas t ulang
[24] D . D rutskoy, E . Keller, d an J . Rexford, ' 'Virtualisasi j aringan yang dapat diskalakan punggung b erbasis pembelajaran mesin b erbantuan lancar p erkiraan,'' Sensor, vol.
dalam jaringan yang ditentukan p erangkat l unak,'' I EEE Internet Comput., vol. 1 7, 22, t idak. 9, hal. 3 592, Mei 2022.
tidak. 2 , h lm. 2 0–27, M aret 2013. [47] G . S un, K . X iong, GO Boateng, G . L iu, dan W . Jiang, ''Pengirisan dan p enyesuaian
[25] R . J ain d an S . Paul, ' 'Virtualisasi jaringan dan jaringan yang ditentukan p erangkat l unak sumber daya di R AN d engan duel j aringan Q y ang dalam,'' J. N etw. H itung. Aplikasi,
untuk k omputasi a wan: Sebuah survei,'' I EEE Commun. M ag., jilid. 5 1, tidak. 1 1, hlm. jilid. 157, M ei 2020, Pasal. T IDAK. 102573, doi: 1 0.1016/j.jnca.2020.102573.
24–31, November 2 013.
84166 JILID 1 1, 2023

Machine Translated by Google
MK Hassan dkk.: DLFisor: D ynamic L earning Hypervisor u ntuk S oftware Defined N etwork
MOHAMED K HALAFALLA H ASSAN diterima MOHAMMED E A KANONA m enerima
gelar B.Sc. g elar di bidang t eknik k omputer dari B.Sc., M .Sc., dan P h.D. gelar d i b idang teknik
Future U niversity, S udan, p ada tahun 2004, dan M .Sc. telekomunikasi d ari F uture University, S udan.
gelar d i bidang t eknik j aringan komunikasi Saat i ni b eliau m enjabat Wakil Dekan F akultas T eknologi
dari U niversitas P utra M alaysia (UPM), pada tahun 2009. Telekomunikasi dan A ntariksa dan K epala Pusat
Dia s aat ini s edang m engejar gelar Ph.D. gelar di bidang Penelitian I oT.
teknik k omunikasi d engan Universitas T eknologi M alaysia Ia aktif terlibat d alam p enelitian t entang m asa depan
(UTM). Dia j uga seorang Rekanan radar hamburan. Minat p enelitiannya meliputi
Profesor d i Universitas M asa D epan. D ia j uga seorang teori informasi, S DN, IoT, komputasi a wan, p embelajaran
peneliti dan spesialis T IK dengan pengalaman 17 t ahun mesin d an j aringan saraf, dan
berbagai p enelitian dan pengalaman TIK. Dia t elah menerbitkan 20 makalah komunikasi seluler. I a menerima Penghargaan K ertas T erbaik d ari I CCCEEE20
dalam k onferensi dan jurnal p eer-review i nternasional. Minat penelitiannya m eliputi Konferensi.
radar h amburan ke d epan, p embelajaran m esin, N FV, vSDN, dan
manajemen sumber d aya d alam jaringan komunikasi.
KHALID S. M OHAMED (Anggota, IEEE)
menerima gelar s arjana teknik t elekomunikasi dari F uture
University, S udan,
pada t ahun 2 011, d an gelar M aster o f Engineering pada t ahun 2011
telekomunikasi dan P h.D. (Rekayasa)
gelar d i bidang telekomunikasi dari M ultimedia
University, M alaysia, masing-masing p ada t ahun 2014
SHARIFAH H AFIZAH SYED A RIFFIN ( Senior dan 2 020. Dia t elah t erdaftar d i Sudan
Anggota, I EEE) m enerima B .Eng. d erajat Dewan Teknik (SEC) s ebagai Profesional
(Hons.) di London, pada tahun 1 997, gelar MEE Engineer, s ejak Januari 2 022, dan D ewan
dari U niversiti T eknologi M alaysia, pada t ahun 2001, d an Engineers M alaysia ( BEM) s ebagai Graduate Engineer, s ejak April 2019. Beliau adalah
Ph.D. gelar dari Queen Mary, U niversity saat ini m enjabat sebagai Asisten P rofesor d i Fakultas T elekomunikasi
dari L ondon, L ondon, p ada t ahun 2006. Saat i ni dia a dalah s eorang dan T eknologi L uar Angkasa d an P j D irektur Inovasi, P enelitian
Associate P rofessor di F akultas T eknik E lektro, Universiti dan P usat Pengembangan (IRDC), U niversitas M asa Depan. M inat penelitiannya
Teknologi M alaysia. termasuk komunikasi seluler, 5 G, p ermukaan r eflektif c erdas (IRS),
Dia t elah menerbitkan 1 16 artikel, 1 7 hak c ipta, s atu beamforming, dan m anajemen interferensi dalam j aringan nirkabel.
sirkuit t erpadu, dan satu merek dagang. A rusnya
minat p enelitian meliputi I nternet of Things, k omputasi di m ana-mana dan
perangkat p intar, jaringan sensor nirkabel, I Pv6, manajemen h andoff, jaringan, d an
sistem k omputasi s eluler.
MUTAZ HH KHAIRI ( Anggota Senior, I EEE)
menerima gelar B S di b idang teknik k omputer
dari F uture U niversity, p ada t ahun 2002, dan M S
gelar d i bidang teknik elektro d ari L inkoping
Universitas, p ada t ahun 2007. Saat i ni sedang m enempuh p endidikan d i
Ph.D. gelar d engan U niversiti T eknologi M alaysia
(UTM). Pada tahun 2002 h ingga 2007 menjabat s ebagai D osen
dengan F akultas T eknik Universitas M asa Depan,
dan D irektur Teknologi I nformasi
SHARIFAH K AMILAH SYED-YUSOF d iterima
Departemen. Ia juga seorang peneliti dan T IK
B.Sc. gelar di bidang teknik e lektro dari George
spesialis d engan 1 6 t ahun p engalaman p enelitian dan I CT y ang l uas. M iliknya
Washington U niversity, A S, pada tahun 1988, d an minat p enelitian meliputi j aringan definisi perangkat l unak (SDN), pembelajaran m esin,
MEE dan Ph.D. derajat dari UTM, p ada tahun 1994 dan
jaringan telekomunikasi, serta d esain dan i mplementasi antena.
2006, masing-masing. S aat i ni b eliau m enjabat s ebagai
Profesor Penuh d i Fakultas T eknik E lektro,
UTM. Minat p enelitiannya m eliputi komunikasi n irkabel.
MOSAB H AMDAN (Anggota Senior, I EEE)
menerima gelar B .Sc. gelar d i bidang teknik k omputer
dan s istem e lektronik d ari U niversitas
Sains dan T eknologi ( UST), Sudan, p ada t ahun 2 010,
gelar M .Sc. gelar d alam a rsitektur komputer dan j aringan
dari U niversitas K hartoum ( UofK),
Sudan, p ada t ahun 2014, dan P h.D. gelar d i bidang
teknik e lektro (jaringan k omputer) d ari
Fakultas T eknik, S ekolah Teknik Elektro, U niversiti
NURZAL E FFIYANA B INTI GHAZALI d iterima Teknologi M alaysia ( UTM),
gelar MS d i bidang t eknik e lektro dari Malaysia, pada tahun 2 021. Pada t ahun 2 010 h ingga 2015, beliau m enjabat sebagai Asisten Pengajar dan
Institut T eknologi S hibaura d an Ph.D. Dosen D epartemen T eknik Sistem Komputer d an E lektronika, Fakultas T eknik,
gelar d ari UTM, pada t ahun 2016. Saat ini d ia sedang m elakukan Universitas S ains dan T eknologi ( UST).
penelitian dalam k omputasi seluler, m anajemen mobilitas, Saat i ni b eliau m enjabat sebagai Peneliti d i Pusat P enelitian I nterdisipliner
protokol k omunikasi j aringan, dan o lahraga Sistem Aman C erdas, Universitas P erminyakan dan M ineral K ing Fahd, A rab S audi.
sistem p emantauan. Minat penelitiannya s aat ini m encakup bidang yang d itentukan perangkat l unak
jaringan (SDN), penyeimbangan beban, k lasifikasi lalu l intas jaringan, I nternet
of Things (IoT), komputasi a wan, k eamanan jaringan, dan j aringan masa depan.
JILID 1 1, 2023 84167