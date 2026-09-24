# VPLS on Software Defined Network Using ONOS Controller Based on Raspberry-Pi 3

> Source file: `VPLS on Software Defined Network Using ONOS Controller Based on Raspberry-Pi 3.pdf`

---

Sekolah S ains Terapan Rizal Sekolah Sains T erapan Sekolah S ains T erapan
Cerdas K urniawan 1 Telkom Rohmat Tulloh k e - 2 Indrarini D yah Irawati k e - 3
University B andung, Universitas Telkom Universitas Telkom
Indonesia Bandung, I ndonesia Bandung, I ndonesia
rizalcerdaskurniawan@gmail.com rohmatth@telkomuniversity.ac.id indrarini@telkomuniversity.ac.id
Abstrak—Dalam t ulisan ini diterapkan t eknologi Software D efined Network
(SDN) d engan m enggunakan O pen N etwork O perating S ystem ( ONOS) y ang
dapat memisahkan c ontrol plane d an data p lane pada s uatu p erangkat
jaringan. O NOS d iinstal p ada R aspberry-Pi 3 untuk m eminimalkan p enggunaan
perangkat Personal Computer ( PC) p ada jaringan SDN. O NOS juga
diimplementasikan u ntuk mendukung fitur Virtual P rivate L AN Service ( VPLS)
yang m embuat j aringan Layer-2 d engan m enggunakan protokol O penFlow.
Perangkat l unak t erhubung ke jaringan host d engan m enghubungkan ke
overlay j aringan yang t erhubung ke protokol bidang data O penFlow. V PLS
dapat memaksimalkan b andwidth yang a da ketika t erjadi k omunikasi antar
perangkat jaringan jarak j auh p ada j aringan lokal. Kami m enguji voice over
Internet P rotocol ( VoIP) dengan b erbagai l alu lintas latar belakang. H asil
pengujian m enunjukkan k inerja j aringan m emenuhi t ingkat baik s esuai s tandar
THIPON.
Kata K unci— Software Defined N etwork, O NOS, Raspberry-Pi
3, V PLS
) ibs on lM e e g rrkb i neeW iaE 1al ffu iankst2nPElniroaes0aAEie
NKAPS2d (It|
Machine Translated by Google
Konferensi I EEE Asia Pasifik tentang N irkabel d an S eluler (APWiMob) 2021
VPLS pada J aringan Buatan Perangkat Lunak M enggunakan O NOS
Pengontrol Berbasis Raspberry-Pi 3
Konsep l ain j uga d igunakan u ntuk m endapatkan e fektivitas pada
jaringan yang ada, y aitu VPLS. K eunggulan k onsep VPLS adalah
menyediakan komunikasi m ultipoint t o m ultipoint b erbasis E thernet
melalui j aringan IP. H al ini dapat mengatasi kendala penyebaran
geografis d alam b erbagi d omain siaran Ethernet d engan
menghubungkan secara virtual.
Beberapa penelitian sebelumnya yang menjadi referensi antara
lain p ada [6], p enulis menganalisis b eberapa p engontrol SDN s eperti
NOX, POX, R YU, Beacon, OpenDaylight, O nix, d an O NOS. K ontroler
POX d an M aestro masih b erfungsi d engan baik, meskipun j aringan
memiliki b anyak perangkat s witch. Secara bersamaan, pengontrol
ONOS m emiliki k inerja y ang lebih baik k etika j uga b erfungsi s ebagai
bidang kendali SDN u ntuk j aringan area l okal (LAN) dan j aringan
pusat data. Pada p enelitian [7], f irewall SDN t elah diimplementasikan
dan d ilakukan dengan menggunakan P OX c ontroller, n amun penelitian
ini hanya d ilakukan dengan p engukuran W ireshark, ICMP, dan iperf
dengan s imulasi m ininet. Dalam penelitian [8] telah dilakukan
pengendalian j aringan transport terbuka d an t erpilah d engan O NOS,
I. PENDAHULUAN implementasi d an s imulasi d ilakukan dengan protokol NETCONF
untuk m empertimbangkan p embentukan l ayanan konektivitas dan
Pertumbuhan p asar VoIP m engalami peningkatan yang signifikan
pemulihan konektivitas jika t erjadi kegagalan selama t ransmisi d ata.
sejak tahun 2016, sehingga perlu a danya peningkatan layanan V oIP
Dalam penelitian lain [ 9], p enulis mengusulkan k onsep SDN y ang
yang e fektif d an h emat b iaya [1]. Infrastruktur berbasis j aringan y ang
dikombinasikan d engan Network Function V irtualization (NFV) untuk
ada harus memenuhi p eningkatan kebutuhan l ayanan. Infrastruktur
meningkatkan k inerja j aringan VPLS. K inerja sistem d iukur d engan
jaringan yang h ampir s eluruhnya d ikelola o leh vendor menyebabkan
menjalankan layanan TCP. T erlepas dari manfaat yang diharapkan,
jaringan yang d ibangun semakin kompleks, s ehingga d iperlukan
beberapa k eterbatasan y ang muncul mencakup interoperabilitas,
suatu s istem u ntuk mengelola d an mengimplementasikan j aringan
keamanan, k inerja, dan s kalabilitas.
untuk m endukung beragam k ebutuhan. S oftware-Defined N etwork
(SDN) m erupakan sebuah konsep baru dalam pengendalian,
implementasi, d an p engelolaan j aringan yang mendukung kebutuhan Penelitian i ni melakukan p erancangan d an i mplementasi j aringan
dan i novasi d i b idang telekomunikasi yang semakin berkembang d an SDN m enggunakan pengontrol ONOS y ang diinstal p ada Raspberry-
kompleks [ 2]. Konsep Sdn a dalah m emisahkan b idang kendali d an Pi 3 d engan aplikasi Virtual Private LAN Service (VPLS). K ami
bidang data. S DN dapat membuat jaringan baik s kala k ecil maupun membangun jaringan kami terdiri d ari 3 s witch OpenFlow, 4 Laptop,
skala besar mampu d ikontrol m enggunakan s atu p engontrol terpusat dan 1 R aspberry-Pi 3 s ebagai pengontrol. U ntuk mengetahui k inerja
[3]. B eberapa pengontrol y ang ada di S DN a ntara lain P OX, R YU, sistem y ang diusulkan, k ami menyediakan layanan VoIP pada
OpenDaylight, d an O NOS. Sistem Operasi J aringan h arus memenuhi jaringan. Kinerja sistem d iukur berdasarkan p arameter t hroughput,
persyaratan yang m enuntut S kalabilitas, K inerja, dan Ketersediaan delay, j itter, packet l oss. Kinerjanya h arus memenuhi p ersyaratan
untuk mendukung jaringan b erskala b esar. U ntuk m engatasi berdasarkan s tandar Telecommunication a nd I nternet P rotocol
tantangan tersebut, O NF m emperkenalkan O pen Network Operating Harmonization O ver Network (TIPHON) [10].
System (ONOS) [4].
ONOS a dalah p engontrol berbasis Java yang memanfaatkan
inisiatif O pen S ervice Gateway (OSGi) kerangka kerja u ntuk lebih
mudah m enginstal d an m emperbarui aplikasi [ 5].
978-1-7281-9475-2/21/$31.00 © 2021 IEEE 19
Penggunaan berlisensi r esmi t erbatas p ada: I nstitut T eknologi Bandung. D iunduh pada 22 J uli 2024 pukul 14:17:26 U TC d ari IEEE Xplore. P embatasan berlaku.

Machine Translated by Google
| Konferensi I EEE  Asia  Pasifik  tentang N  |     | irkabel d an S eluler  (APWiMob)  2021 |     |     |     |     |     |
| ------------------------------------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
II. R  INGKASAN
Layanan  Ethernet  dan  jaminan  Quality  of  Service ( QoS)  [17].
A. J aringan  Buatan  Perangkat L unak
| Software-Defined N  |     | etwork ( SDN)  merupakan  sebuah k onsep  baru   |     |     |     |     |     |
| ------------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
dalam p engendalian, i mplementasi, d an p engelolaan j aringan y ang
mendukung k ebutuhan d an  inovasi  telekomunikasi y ang  semakin
| berkembang d an k ompleks. K  |     | onsep  SDN a dalah m  | emisahkan  control   |     |     |     |     |
| ----------------------------- | --- | --------------------- | -------------------- | --- | --- | --- | --- |
plane d an d ata p lane [ 11]. S DN d apat  membuat j aringan  baik  skala
kecil m  aupun s kala b esar  mampu d ikontrol  menggunakan s atu
pengontrol t erpusat  [12-14].  Beberapa  pengontrol d i  SDN a ntara l ain
| POX, R  | YU, O  penDaylight,  dan O  | NOS. |     |     |     |     |     |
| ------- | --------------------------- | ---- | --- | --- | --- | --- | --- |
Gambar 2 .  Konsep  VPLS
|     |     |     |     | Gambar  2  menunjukkan b eberapa  kelebihan m  |     | enjadi  VPLS y ang   |     |
| --- | --- | --- | --- | ---------------------------------------------- | --- | -------------------- | --- |
lebih b aik  dibandingkan d engan t eknologi t unneling s ebelumnya, y aitu
|     |     |     |     | VPLS m  empunyai p seudowires s ebagai  rangkaian  virtualnya.  VPLS   |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- |
juga m  emiliki  penemuan o tomatis  dan  konfigurasi o tomatis,  yang
|     |     |     |     | memungkinkan b eberapa  perangkat d i j aringan  VPLS s aling m  |     |     | engenali   |
| --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | ---------- |
dan  membangun k abel  semu u ntuk  perangkat y ang b aru  dikenali. V PLS
terdiri  dari V irtual  Switched I nstance  (VSI)  atau  Virtual  Forwarding
Gambar 1 . A rsitektur S DN Instance, y ang d apat  mendefinisikan a nggota  domain V PLS  dan
|                           |     |                                          |     | menyerupai  switch  virtual p ada r outer P E.  VPLS m  |                                            | emungkinkan   |     |
| ------------------------- | --- | ---------------------------------------- | --- | ------------------------------------------------------- | ------------------------------------------ | ------------- | --- |
| Gambar 1   menunjukkan A  |     | rsitektur  SDN t erdiri d ari 3  l ayer. |     |                                                         |                                            |               |     |
|                           |     |                                          |     | antarmuka e thernet y ang m                             | emiliki  LAN  virtual y ang s ama  untuk   |               |     |
(cid:127)  Data  Plane: t erdiri d ari e lemen  jaringan  yang  dapat  mengelola   dihubungkan d engan b anyak p erangkat P E.  Misalnya, p engguna  A d i
domain V PLS t erdiri  dari a ntarmuka  ethernet y ang t erhubung k e
|     | Datapath  SDN m  | engikuti i nstruksi  yang d iberikan  melalui   |     |     |     |     |     |
| --- | ---------------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
Control-Data-Plane I nterface  (CDPI). pengguna A    di r outer C  E  di t empat b erbeda.  VSI  dapat m  eremote
|     |     |     |     | alamat M  AC  dan  memastikan d omain V PLS b ebas d ari p erulangan. V SI   |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------------------------- | --- | --- | --- |
(cid:127)  Control  Plane:  Bagian  dari l ayanan  jaringan  sebagai  pengontrol
|     |                         |                                    |     | memiliki  fungsi m  | anajemen  alamat M  | AC, b anjir, d an  penerusan d ata   |     |
| --- | ----------------------- | ---------------------------------- | --- | ------------------- | ------------------- | ------------------------------------ | --- |
|     | SDN  yang  berfungsi m  | enerjemahkan k ebutuhan l apisan   |     |                     |                     |                                      |     |
[18].
aplikasi k e l apisan i nfrastruktur. P roses  ini d ilakukan d engan
|     | menyediakan S DN D                                     | atapath  yang s esuai  dan m  | emberikan   | D. R  aspberry-Pi  3                                          |               |                                          |              |
| --- | ------------------------------------------------------ | ----------------------------- | ----------- | ------------------------------------------------------------- | ------------- | ---------------------------------------- | ------------ |
|     | informasi  relevan y ang  dibutuhkan o leh l apisan A  |                               | plikasi.    |                                                               |               |                                          |              |
|     |                                                        |                               |             | Penelitian i ni m                                             | enggunakan m  | ini k omputer  sebagai  pengontrolnya.   |              |
|     |                                                        |                               |             | Komputer  mini  tipe  Raspberry-Pi  generasi k etiga y ang m  |               |                                          | enggunakan   |
(cid:127)  Aplikasi:  terletak  di  lapisan p aling  atas, b erkomunikasi d engan   ARM  System-on-chip  (SoC).  Raspberry  3  dipilih  karena  dilengkapi
sistem  melalui N  orthbound  Interface  (NBI). dengan 4   port U  SB 2   dan  port E thernet  100 B  ase  untuk  dihubungkan
|               |                                   |     |     | dengan o pen f low  switch. K  | onfigurasi j aringan  pada p enelitian i ni        |     |                  |
| ------------- | --------------------------------- | --- | --- | ------------------------------ | -------------------------------------------------- | --- | ---------------- |
| B.  Sistem O  | perasi J aringan  Terbuka  ONOS   |     |     |                                |                                                    |     |                  |
|               |                                   |     |     | memerlukan m                   | inimal  3  port e thernet u ntuk  tiga  switch. A  |     | kibatnya,  dua   |
merupakan  salah  satu  pengendali s elain N  OX, P OX,  Ryu,  Floodlight,   port U  SB d iubah m  enjadi  port e thernet m  enggunakan k onverter U  SB
| Opendaylight ( ODL), B  | eacon, d an m  | asih b anyak l ainnya y ang t erus   |     |                  |                                          |     |                     |
| ----------------------- | -------------- | ------------------------------------ | --- | ---------------- | ---------------------------------------- | --- | ------------------- |
|                         |                |                                      |     | ke  ethernet. K  | omputer  mini  ini  juga  menyediakan R  |     | AM  1GB d an  CPU   |
berkembang. M  asing-masing  pengontrol d ari b erbagai  vendor i ni   quad-core  ARMv8  1,2GHx 6 4-bit.  Prosesor d an  RAM  ini b erguna s aat
mempunyai p endekatan  yang  berbeda-beda  dalam m  engimplementasikan   menjalankan f ungsi b idang k endali d an  manajemen  jaringan. B  eberapa
proses  komunikasi p engontrolnya. O  NOS  adalah p engontrol  sumber   fungsi l ain  yang t ersedia s eperti d ukungan B  luetooth 4 .1, L AN n irkabel
terbuka d an b erfungsi s ebagai b idang  kendali p usat  di  SDN. 80.11n, d an  dukungan B  luetooth L ow  Energy  (BLE)
ONOS a dalah p royek s umber t erbuka  yang d idistribusikan d engan
| bahasa p emrograman  berbasis J ava [ 15]. D  |     | engan  ONOS, k ita d apat   |     |     |     |     |     |
| --------------------------------------------- | --- | --------------------------- | --- | --- | --- | --- | --- |
mengelola e lemen j aringan, s eperti s witch d an r outing, s erta
AKU A KU A KU. I MPLEMENTASI  SISTEM
| menjalankan d an m  | engembangkan p rogram  perangkat l unak  secara               |     |     |     |     |     |     |
| ------------------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| modularitas, m      | enyediakan l ayanan  komunikasi y ang a ndal, s kalabilitas   |     |     |     |     |     |     |
A.Topologi  Jaringan
| tinggi, d an d iharapkan m  |     | emiliki k inerja y ang l ebih  baik. |     |                                                               |     |     |            |
| --------------------------- | --- | ------------------------------------ | --- | ------------------------------------------------------------- | --- | --- | ---------- |
|                             |     |                                      |     | Tiga  aplikasi y ang a ktif p ada p engontrol  ONOS  yaitu O  |     |     | penFlow,   |
C. L ayanan  LAN P ribadi V irtual
|     |     |     |     | Forwarding, d an  VPLS. K  | onfigurasi V PLS p ada t erminal  ONOS   |     |     |
| --- | --- | --- | --- | -------------------------- | ---------------------------------------- | --- | --- |
VPLS a dalah V PN m  ultipoint  lapisan 2  y ang  memungkinkan b anyak   menghasilkan  dua  ID V PLS, y aitu V PLS1 d an  VPLS2. H  ost d engan I D
VPLS b erbeda  tidak d apat  berkomunikasi s atu  sama  lain.  Sebaliknya
wilayah t erhubung d alam d omain  jembatan t unggal  yang s ama  melalui
jaringan I nternet  Protocol ( IP).  Seluruh  wilayah  klien d alam i nstance   host y ang m  empunyai I D V PLS y ang s ama  dapat  berkomunikasi s atu
sama  lain.
| VPLS  dapat  seolah-olah b erada  pada  jaringan  LAN y ang  sama m  |     |     | eskipun   |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- |
terpisah  secara g eografis  [16]. Jenis  layanan  ini m  enggunakan V oIP d engan m  enggunakan p erangkat
VPLS m  enggunakan a ntarmuka E thernet k e k lien.  Layanan  VPLS   lunak A  sterisk, Z oiper, d an  iperf  sebagai g enerator l alu  lintas l atar
disediakan u ntuk o perator,  penyedia  layanan,  dan p erusahaan b esar   belakang. P C  1  sebagai  server V oIP d an  tiga  PC  lainnya s ebagai  client.
yang m  embutuhkan k etersediaan k inerja t inggi Parameter p engukuran Q  oS  terdiri  dari  throughput, d elay,  packet l oss,
|                                |     |            |     | dan  jitter  dengan m  | enggunakan s oftware W  | ireshark. |     |
| ------------------------------ | --- | ---------- | --- | ---------------------- | ----------------------- | --------- | --- |
| 978-1-7281-9475-2/21/$31.00 ©  |     | 2021  IEEE |     | 20                     |                         |           |     |
Penggunaan  berlisensi r esmi t erbatas p ada: I nstitut T eknologi  Bandung. D iunduh  pada  22 J uli  2024  pukul  14:17:26 U TC d ari  IEEE  Xplore. P embatasan  berlaku.

Machine Translated by Google
| Konferensi I EEE  Asia  Pasifik  tentang N  | irkabel d an S eluler  (APWiMob)  2021 |     |     |
| ------------------------------------------- | -------------------------------------- | --- | --- |
Gambar  5. A ntarmuka O penFlow  Baru
Gambar  5 m  enunjukkan k onfigurasi  dengan  menambahkan  IP  Address
pengontrol  sehingga  pengontrol  dapat  mengenali  saklar.
Gambar  3.  Desain  topologi  jaringan
Gambar  3 m  enunjukkan b eberapa  perangkat  yang  digunakan p ada
| jaringan  ini y aitu  1 b uah R                 | aspberry-Pi  3  sebagai  pengontrol  ONOS,  2  buah   |                              |                        |
| ----------------------------------------------- | ----------------------------------------------------- | ---------------------------- | ---------------------- |
| konverter  USB-To-Ethernet, 3   buah  switch O  |                                                       | penFlow, 1 0  buah  kabel U  | TP, d an  4  buah P C. |
B.Konfigurasi J embatan
Raspberry-Pi  3 y ang  digunakan s ebagai p erangkat p engontrol   Gambar  6. K onfigurasi P ort  Forwarding
hanya  mempunyai s atu  antarmuka  ethernet [ 19],  untuk  itu d ilakukan
dengan m  enambahkan  perangkat y aitu 2   buah  USB-to-Ethernet   Gambar  6 m  enunjukkan p ort  konfigurasi  data p lane O  penFlow
converter  pada  Raspberry-Pi 3   agar  dapat t erhubung  secara l angsung
dengan  spesifikasi:
| ke  perangkat p engontrol  Raspberry-Pi 3   dengan s aklar O  |     | penFlow p ada  jaringan  SDN. |     |
| ------------------------------------------------------------- | --- | ----------------------------- | --- |
(cid:127)  Ether2:  terhubung k e s witch2
auto  br0
iface b r0 i net a lamat   (cid:127)  Ether3:  terhubung k e s witch3
statis 1 00.100.100.254
(cid:127)  Ether4:  terhubung d engan  PC1
netmask 2 55.255.255.0
jaringan 1 00.100.100.0
(cid:127)  Ether5:  terhubung d engan  PC2
jembatan_ports e th0 e th1  eth2
D. K  onfigurasi V PLS P ada
Gambar  4.  Konfigurasi  Jembatan tulisan  ini, k onfigurasi  VPLS d ilakukan  dengan  membuat  2  ID  VPLS
dengan  nama I D y aitu V PLS1 d an V PLS2.  Setiap  ID V PLS t erdiri  dari 2
Dalam  proses  implementasinya a gar  setiap s witch  OpenFlow  yang   PC. V PLS1 t erdiri d ari P C1 d an P C3, d an V PLS2 t erdiri d ari P C2 d an
| terhubung  dengan  pengontrol  dapat  berkomunikasi d alam  satu      |     |     | PC4. |
| --------------------------------------------------------------------- | --- | --- | ---- |
| jaringan y ang  sama, m  aka  diperlukan  konfigurasi  bridge  pada   |     |     |      |
antarmuka p engontrol  [20].  Gambar  4  menunjukkan p enambahan
| antarmuka b ridge b aru  yaitu b r0 d engan k onfigurasi  IP A  |     | ddress  statis   |     |
| --------------------------------------------------------------- | --- | ---------------- | --- |
dengan t iga a ntarmuka p ort  yang  dijembatani y aitu  eth0, e th1,  eth2.
C.  Konfigurasi O  penFlow  Switch P ada   Gambar  7. P enambahan I D V PLS
jaringan  SDN,  tidak  semua p erangkat j aringan d apat  langsung   Gambar  7 m  enunjukkan I D V PLS d itambahkan  dengan  nama  VPLS1
dan  VPLS2.
| dikenali o leh  controller, h anya  perangkat y ang m  |     | endukung p rotokol   |     |
| ------------------------------------------------------ | --- | -------------------- | --- |
OpenFlow s aja  yang d apat  dikenali [ 21].  Oleh k arena i tu p ada  tulisan
| ini m  enggunakan  switch O  | penFlow  dengan p erangkat  Mikrotik. |     |     |
| ---------------------------- | ------------------------------------- | --- | --- |
Pada  tahap i ni  dilakukan k onfigurasi  switch  OpenFlow, d ilakukan
| beberapa k onfigurasi y aitu I P A  | ddress,  bridge, O  | penFlow  sebagai   |     |
| ----------------------------------- | ------------------- | ------------------ | --- |
control p lane,  dan d ata  plane.
Gambar  8. M  emberikan I D P ada  Antarmuka H ost
Gambar 8  m  enunjukkan  ID d itambahkan k e a ntarmuka  masing-masing  host
sehingga V PLS  dapat m  engenalinya.
| 978-1-7281-9475-2/21/$31.00 ©  | 2021  IEEE |     | 21  |
| ------------------------------ | ---------- | --- | --- |
Penggunaan  berlisensi r esmi t erbatas p ada: I nstitut T eknologi  Bandung. D iunduh  pada  22 J uli  2024  pukul  14:17:26 U TC d ari  IEEE  Xplore. P embatasan  berlaku.

Machine Translated by Google
| Konferensi I EEE  Asia  Pasifik  tentang N  |     | irkabel d an S eluler  (APWiMob)  2021 |     |     |                                                 |                 |                                      |     |        |
| ------------------------------------------- | --- | -------------------------------------- | --- | --- | ----------------------------------------------- | --------------- | ------------------------------------ | --- | ------ |
|                                             |     |                                        |     |     | pengontrol  dapat  mengontrol j aringan  SDN m  |                 | elalui  sakelar  ini.  Langkah       |     |        |
|                                             |     |                                        |     |     | selanjutnya a dalah m                           | enghubungkan m  | asing-masing s witch k e  PC         |     |        |
|                                             |     |                                        |     |     | sesuai t opologinya, k emudian m                |                 | engkonfigurasi  IP  Address p ada m  |     | asing- |
masing P C  seolah-olah b erada  dalam  jaringan  lokal d engan a walan
jaringan  yang  sama.
|     |     |     |     |     |     | IV. H  ASIL D  | AN A  NALISIS |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------- | --- | --- |
A. U  ji  Pengendali
|     |     |     |     |     | Pengendali |     | Tuan r umah 2  |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | --- |
Gambar 9 .  Grup  VPLS
| Gambar 9   menunjukkan p engelompokan H  |     |     | ost p ada V PLS I D.  PC  1 d an   |     | Tuan r umah 3  |     |     |     |     |
| ---------------------------------------- | --- | --- | ---------------------------------- | --- | -------------- | --- | --- | --- | --- |
PC  3 m  enjadi  VPLS1  sedangkan P C  2  dan  PC 4   menjadi V PLS2.
| E. S pesifikasi S istem  (cid:127)   |             |        |     |     | Beralih  2 |     |     |     |     |
| ------------------------------------ | ----------- | ------ | --- | --- | ---------- | --- | --- | --- | --- |
| Spesifikasi K                        | ontroler U  | ntuk   |     |     |            |     |     |     |     |
Beralih  3
| kontroler y ang m  | enggunakan R  | aspberry-pi 3   dengan s pesifikasi   |     |     |     |     |     |     |     |
| ------------------ | ------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Beralih  1
seperti p ada t abel 1
|     | TABEL  1. S pesifikasi R aspberry-Pi  3 |     |     |     |     | Tuan r umah  4 |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- |
Tuan r umah  1
| Jenis |     |     | Spesifikasi |     |     |     |     |     |     |
| ----- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Gambar  11.  Implementasi t opologi  jaringan
| Unit P emrosesan P usat  4x  ARM C ortex-A53, 1 ,2 G  |     |       | Hz  |     |                      |                                                          |     |     |     |
| ----------------------------------------------------- | --- | ----- | --- | --- | -------------------- | -------------------------------------------------------- | --- | --- | --- |
|                                                       |     |       |     |     | Gambar 1 1 m         | enunjukkan p engujian  pada  sisi p engontrol, d imana   |     |     |     |
| RAM                                                   |     | 1  GB |     |     |                      |                                                          |     |     |     |
|                                                       |     |       |     |     | pengontrol s udah m  | engenali  seluruh p erangkat  pada  jaringan S DN.       |     |     |     |
Jaringan Ethernet 1 0/100,  2,4GHz 8 02.11n Pada  pengujian  ini  pengontrol  dapat  mengenali  seluruh  perangkat  yang
WLAN tersedia s esuai t opologi i mplementasi,  dimana  terdapat t iga  switch  dan
4 P C  sesuai p erencanaan t opologi.
| Sistem o perasi |     | Raspbian 4 .19 |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
B. U  ji  Konektivitas
| Gambar 1 0  menunjukkan s kema  rangkaian R  |                                   |     | aspberry-Pi 3   yang d igunakan.   |     |     |     |     |     |     |
| -------------------------------------------- | --------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
| Pada p enelitian i ni  digunakan 2   buah U  |                                   |     | SB-to-Ethernet c onverter u ntuk   |     |     |     |     |     |     |
| menghubungkan R                              | aspberry-Pi 3   dengan s witch O  |     | penFlow y aitu  Switch             |     |     |     |     |     |     |
2 d an S witch  3  serta 1   port E thernet S witch 1 .  Semua  port a kan
| dihubungkan k e  switch m           |                                                            | enggunakan k abel  UTP.  Untuk m    |     | enghubungkan   |     |     |     |     |     |
| ----------------------------------- | ---------------------------------------------------------- | ----------------------------------- | --- | -------------- | --- | --- | --- | --- | --- |
| semua s witch O                     | penFlow d engan p engontrol i ni, k onfigurasi j embatan   |                                     |     |                |     |     |     |     |     |
| dilakukan  di  sisi p engontrol. K  |                                                            | onfigurasi  Raspberry-pi s ebagai   |     |                |     |     |     |     |     |
pengontrol
Gambar  12.  Uji K onektivitas  Melalui  Kontroler
|     |     |     |     |     | Gambar 1 2 m  | enunjukkan p engujian  konektivitas j aringan  untuk   |     |     |     |
| --- | --- | --- | --- | --- | ------------- | ------------------------------------------------------ | --- | --- | --- |
mengetahui s emua p erangkat  switch y ang  terhubung k e p engontrol
|     |     |     |     |     | dapat  berkomunikasi d engan b aik. G                                  |     | ambar  12 j uga m  | enunjukkan  bahwa   |            |
| --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | ------------------ | ------------------- | ---------- |
|     |     |     |     |     | telah  berhasil  melakukan P ING d engan  nilai  paket s ebesar 6 4 B  |     |                    |                     | ytes  ke   |
Gambar 1 0. K onfigurasi R aspberry-pi  3  sebagai p engontrol
3 s witch y ang  terhubung l angsung k e c ontroller d ari  sisi c ontroller.
(cid:127)  Spesifikasi S witch  Untuk
C. T es L ayanan L AN P ribadi  Virtual
| fungsi  forwarding p lane m                                          |     | enggunakan R  | outer M  | ikrotik y ang s udah   |                                            |     |                                |     |     |
| -------------------------------------------------------------------- | --- | ------------- | -------- | ---------------------- | ------------------------------------------ | --- | ------------------------------ | --- | --- |
|                                                                      |     |               |          |                        | Pengujian  VPLS i ni d ilakukan d engan m  |     | elakukan P ING  antara  host   |     |     |
| terinstall O  penflow d engan s pesifikasi s eperti  pada t abel  2. |     |               |          |                        |                                            |     |                                |     |     |
dengan  ID V PLS y ang  sama a tau h ost d engan I D V PLS b erbeda.  Jika
|     | TABEL  2. S pesifikasi M  |     | ikrotik |     |     |     |     |     |     |
| --- | ------------------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
konfigurasi V PLS b elum d ilakukan s ecara o tomatis, s emua h ost  dapat
|                                                                      | Jenis |                          | Spesifikasi   |                 | berkomunikasi. |     |     |     |     |
| -------------------------------------------------------------------- | ----- | ------------------------ | ------------- | --------------- | -------------- | --- | --- | --- | --- |
| Sistem o perasi                                                      |       |                          | RouterOS      |                 |                |     |     |     |     |
| Jumlah  Port L AN                                                    |       |                          | 5             |                 |                |     |     |     |     |
| RAM                                                                  |       |                          | 128MB         |                 |                |     |     |     |     |
| Routernoard                                                          |       |                          | RB-951Ui-2HnD |                 |                |     |     |     |     |
| Langkah  selanjutnya a dalah m                                       |       | elakukan  konfigurasi O  |               | penFlow p ada   |                |     |     |     |     |
| switch a gar s etiap  switch y ang t erhubung  dengan c ontroller R  |       |                          |               | aspberry-       |                |     |     |     |     |
Gambar  13.  Konektivitas  Host d engan  ID  VPLS B erbeda
| Pi 3  d apat m  endeteksi t opologi O  |     | NOS  yang a rtinya  ONOS s ebagai |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 978-1-7281-9475-2/21/$31.00 ©          |     | 2021  IEEE                        |     |     | 22  |     |     |     |     |
Penggunaan  berlisensi r esmi t erbatas p ada: I nstitut T eknologi  Bandung. D iunduh  pada  22 J uli  2024  pukul  14:17:26 U TC d ari  IEEE  Xplore. P embatasan  berlaku.

Machine Translated by Google
Konferensi I EEE Asia Pasifik tentang N irkabel d an S eluler (APWiMob) 2021
Gambar 1 3 menunjukkan b ahwa PING antara h 2 d an h1 Gambar 16 m enunjukkan d elay d ari p engukuran t anpa b ackground
menghasilkan R equest Time Out k arena h2 d an h 1 m empunyai ID VPLS y antrga f bfiecr b beedrnai.lai 2 .75 ms dan p engukuran d engan b ackground t raffic
tertinggi b ernilai 3 .58 ms. Hasil t ersebut menunjukkan b ahwa
penundaan y ang ditunjukkan p ada pengukuran i ni m asih m engikuti
standarisasi TIPHON. R ata-rata p engukuran p enundaan k eseluruhan
adalah 3,11 ms.
(cid:127)
Naik o pelet
Pada b agian ini j itter d iukur dengan m engurangi w aktu t unda
paket p ertama a tau sebelumnya dengan w aktu t unda paket k edua
atau berikutnya.
Gambar 1 4. K onektivitas H ost d engan I D V PLS y ang Sama
Gambar 1 4 menunjukkan P ING antara h2 d an h 4 m enghasilkan
TTL Reply yang b erarti h 2 dan h4 d apat b erkomunikasi k arena h2 d an
h4 termasuk dalam VPLS I D y ang s ama.
D. U ji P erforma ( Voice O ver I nternet Protocol) (cid:127) Throughput
Pada b agian ini
akan d itampilkan pengukuran throughput u ntuk mengetahui
kecepatan sebenarnya j aringan saat m engirimkan d ata.
Pengukuran dilakukan d engan m elakukan panggilan a ntara h1 dan
h3 yang sudah t erhubung d an dapat berkomunikasi m elalui layanan Gambar 1 7. Performa Jitter
VPLS di SDN.
Gambar 17 m enunjukkan b ahwa nilai jitter p ada pengukuran i ni
masih m engikuti s tandarisasi T IPHON. P ada pengukuran i ni, semakin
tinggi n ilai background t raffic maka n ilai jitternya juga akan semakin
besar. N ilai jitter t anpa b ackground t raffic menunjukkan n ilai s ebesar
0.0352 m s, sedangkan n ilai jitter p ada background t raffic tertinggi
bernilai 0 .0414 m s.
Rata-rata p engukuran j itter i ni adalah 0 ,0381 ms.
(cid:127) Paket Hilang
Pada bagian ini p acket l oss diukur dengan m enghitung j umlah
paket y ang dikirim d ikurangi j umlah paket y ang diterima k emudian
Gambar 1 5. K inerja T hroughput
dikalikan 1 00%.
Gambar 1 5 menunjukkan b ahwa throughput y ang dihasilkan pada
pengukuran ini masih s esuai s tandar TIPHON, dimana n ilai t hroughput
tanpa background traffic mencapai 3,62 M bps d an n ilai throughput
tertinggi p ada b ackground traffic mencapai 3,473 Mbps. R ata-rata
throughput k eseluruhan adalah 3 .528 Mbps.
(cid:127) Delay
Pada b agian ini, k ita m elakukan p engukuran delay dengan
menghitung r ata-rata waktu k edatangan paket p ertama atau
sebelumnya d ikurangi dengan w aktu k edatangan p aket kedua atau
setelahnya s elama p roses komunikasi V oIP menggunakan Z oiper.
Gambar 1 8. Kinerja P aket Rugi
Gambar 18 m enunjukkan b ahwa nilai packet loss dari p engukuran
ini m asih s esuai s tandarisasi T IPHON, d imana pada pengukuran ini
nilai packet loss pada pengukuran t anpa b ackground t raffic sebesar
2.1%, d an n ilai packet loss pada pengukuran b ackground traffic
tertinggi s ebesar 7.2 %.
Gambar 1 6. K eterlambatan K inerja
978-1-7281-9475-2/21/$31.00 © 2021 IEEE 23
Penggunaan berlisensi r esmi t erbatas p ada: I nstitut T eknologi Bandung. D iunduh pada 22 J uli 2024 pukul 14:17:26 U TC d ari IEEE Xplore. P embatasan berlaku.

Machine Translated by Google
Konferensi I EEE Asia Pasifik tentang N irkabel d an S eluler (APWiMob) 2021
[6] A A S emenovykh, O R Laponina, “Analisis komparatif pengontrol S DN,” J urnal
Internasional T eknologi Informasi Terbuka, v ol. 6 , tidak. 7 .2018.
TABEL 3. K esimpulan K inerja
[7] W M Othman, H. Chen, A . Al-moalmi, A N Hadi, “Implementasi d an a nalisis kinerja
N Kualitas dari Tanpa Latar B elakang Indeks Indeks firewall SDN pada p engontrol P OX,” pada Konferensi Internasional IEEE ke-9
Hai Melayani Latar Belakang dan tanpa Latar Belakang tentang Perangkat L unak dan Jaringan K omunikasi ( ICCSN) t ahun 2017,
dan Lalu l intas Latar B elakang dan Tiongkok, 2017 .
Lalu lintas Maks dan Lalu lintas [8] A . Giorgetti, A . Sgambelluri, R. Casellas, “Kontrol jaringan t ransportasi terbuka d an
Lalu l intas maks terpilah menggunakan Sistem Operasi Jaringan T erbuka ( ONOS),” Jurnal
1 K eluaran 3,62 3,47Mbps L uar Biasa Bagus s ekali Komunikasi d an J aringan O ptik IEEE/OSA, vol. 1 2, t idak. 2 , hal.A171-A181, 2019.
Mbps
2 P enundaan 2,75 mdtk 3 ,58 m dtk Sempurna Sempurna
[9] M . L iyanage, M . Y lianttila, A. Gurtov, "Arsitektur VPLS y ang D itentukan P erangkat
3 Kegugupan 0,0352 0 ,0414 Bagus Bagus
Lunak: P eluang dan T antangan," Simposium I nternasional T ahunan k e-28 IEEE
MS MS
2017 t entang K omunikasi R adio P ribadi, D alam Ruangan, d an S eluler (PIMRC
4 P aket Hilang 2,1% 7,2% Sempurna Bagus 2017)Di: M ontreal, K anada , D OI: 10.1109/PIMRC.2017.8292519
Berdasarkan T abel 3. hasil p engukuran Q oS yang t elah dilakukan [10] H armonisasi Telekomunikasi d an P rotokol Internet Melalui Jaringan ( TIPHON), “Tr
menggunakan layanan VoIP p ada i mplementasi j aringan ini 101 329,” E tsi, v ol. 1 , tidak. A spek umum Q uality of S ervice (QoS), h al. 1–37, 1 999.
mempunyai kinerja Q oS yang b aik sesuai standarisasi T IPHON.
[11] A . Zahmatkesh, T . Kunz, “Jaringan n irkabel multihop y ang ditentukan perangkat
lunak: Janji dan T antangan,” Jurnal Komunikasi d an J aringan, vol. 19, t idak. 6 ,
2017.
V. KESIMPULAN
[12] Y . Z hou, B. Ramamurthy, B. Guo, “ Mendukung p enyesuaian b andwidth dinamis
Kami m embangun V PLS di j aringan SDN y ang memisahkan berdasarkan t autan t ransport virtual dalam IP y ang d itentukan perangkat lunak
bidang kontrol d ari b idang data. K ami m enggunakan O NOS s ebagai melalui j aringan o ptik,” Jurnal Komunikasi dan J aringan O ptik IEEE/OSA, vol.
10, t idak. 3 , hal.125-137, 2 018.
pengontrol yang d iterapkan p ada R aspberry-Pi 3. Hasil kinerja
[13] R . Tulloh, H . Tussyadiah, RW Hutabri d an RM Negara, “ Analisis distribusi b eban
implementasi V PLS pada j aringan SDN menggunakan pengontrol
pada topologi bipartit m enggunakan pengontrol l ampu sorot,”
ONOS y ang d iterapkan p ada R aspberry-Pi 3 menunjukkan b ahwa
Jurnal Teknologi Informasi Teoritis dan T erapan, v ol. 9 6, t idak. 5 , hal.1238-1252,
nilai k eempat parameter Q oS m asih m engikuti standar TIPHON yang 2018.
baik. Pada penelitian i ni perbandingan h asil pengukuran Q oS dengan [14] R . Tulloh, J G Amri G inting, A. Mulyana, dan M . L utfi, “ Perbandingan Kinerja
background traffic 200Mb, 400Mb, 600Mb, 800Mb d igunakan u ntuk Layanan F ile T ransfer Protocol antara Link State dan D istance V ector R outing
menentukan batas kinerja j aringan pada beban t rafik. H asilnya adalah Protocol in S oftware D efined Network,” Seri K onferensi IOP: Ilmu dan R ekayasa
Material , jilid. 9 82, t idak. 1 A gustus 2 020.
pengukuran d engan b eban t rafik t ertinggi, d an n ilai QoS m asih
menunjukkan nilai y ang b aik sesuai s tandar TIPHON.
[15] A S Muqaddas, P. G iaccone, A. Bianco, “Lalu Lintas Antar-Pengendali untuk
Mendukung K onsistensi d alam Klaster ONOS,” T ransaksi IEEE pada Manajemen
Implementasi V PLS dapat dijalankan d i jaringan SDN menggunakan Jaringan d an Layanan, vol. 1 4, t idak. 4 , hal.1018-1031, 2 017.
pengontrol ONOS untuk b erbagi jaringan pribadi a ntar h ost. [16] C . Fancy, L MM Thanveer, “ Evaluasi L ayanan V irtual P rivate LAN ( VPLS) b erbasis
protokol a lternatif,” p ada Konferensi Internasional t entang I oT dan Aplikasi
REFERENSI (ICIOT) 2017, India, 2 017.
[17] M . L iyanage, M. Y lianttila, A. Gurtov, “Arsitektur VPLS H ierarki Aman untuk
Jaringan y ang D isediakan Penyedia,” I EEE Access, vol. 3 , hal.967-984, 2 015.
[1] A. Bhutani, P. Wadhwani, "Voice over I nternet P rotocol ( VoIP)
Ukuran Pasar B erdasarkan Jenis,” A pril 2 019. [Online]. [Diakses 26 Januari 2021].
[18] M . B arreiros, P . L undqvist, “ Studi K asus VPLS,” Jaringan y ang Diaktifkan Q OS:
Alat dan L andasan, Wiley T elecom, 2015, 163-191.
[2] M. Liyanage, A . G urtov, M. Ylianttila, "Konsep J aringan yang Ditentukan Perangkat [19] R . Heradio, J. Chacon, H . Vargas, “ Perangkat Keras Sumber T erbuka d alam
Lunak," J aringan S eluler yang Ditentukan P erangkat Lunak (SDMN), W iley Pendidikan: Studi P emetaan S istematis,” IEEE Access, v ol. 6, hal.72094-72103,
Telecom, 2 015, 21-44. 2018.
[3] V. M onita, ID Irawati, R. T ulloh, “Perbandingan kinerja p rotokol r outing p ada layanan [20] K . Lee, B . Kwon, J . Kang, “ Kontrol Laju A liran Optimal u ntuk Sistem Angkatan
multimedia p ada j aringan yang ditentukan p erangkat l unak,” Laut Berbasis SDN,” T ransaksi IEEE pada S istem Dirgantara dan E lektronik, vol.
Buletin Teknik E lektro d an Informatika, v ol. 9 , tidak. 4, hal.1612-1619, 2 020. 53, t idak. 6 , hal.2690-2705, 2 017.
[21] M . Y ang, H . Rastegarfar, I B Djordjevic, “ Alokasi s umber daya adaptif lapisan f isik
[4] T. Alharbi, M. P ortmann, “ Keamanan ( Dalam) Virtualisasi dalam J aringan yang dalam jaringan p usat d ata yang d itentukan p erangkat l unak,”
Ditentukan P erangkat L unak,” IEEE A ccess, vol. 7, h al.66584-66594, 2019. Jurnal Komunikasi d an J aringan O ptik IEEE/OSA v ol. 10, t idak. 1 2, h al.1015-1026,
2018.
[5] AH Eljack, A. Hassan, HH E lamin. “ Analisis Kinerja P engontrol SDN O NOS d an
Floodlight berdasarkan Lalu L intas TCP dan U DP,” pada Konferensi Internasional
Teknik K omputer, K ontrol, L istrik, dan E lektronika ( ICCCEEE) 2 019, Sudan, 2 019.
978-1-7281-9475-2/21/$31.00 © 2021 IEEE 24
Penggunaan berlisensi r esmi t erbatas p ada: I nstitut T eknologi Bandung. D iunduh pada 22 J uli 2024 pukul 14:17:26 U TC d ari IEEE Xplore. P embatasan berlaku.