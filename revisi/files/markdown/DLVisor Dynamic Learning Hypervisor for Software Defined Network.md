# DLVisor Dynamic Learning Hypervisor for Software Defined Network

> Source file: `DLVisor Dynamic Learning Hypervisor for Software Defined Network.pdf`

---

Subscribe to DeepL Pro to translate larger documents.
Visit www.DeepL.com/pro for more information.
Diterima 5 Juli 2023, disetujui 30 Juli 2023, tanggal terbit 4 Agustus 2023, tanggal versi cetak 14 Agustus 2023.
Pengidentifikasi Objek Digital 10.1109/ACCESS.2023.3302266
DLVisor: Hypervisor Pembelajaran Dinamis
untuk Jaringan yang Ditentukan Perangkat
Lunak
MOHAMED KHALAFALLA HASSAN 1,2,
SHARIFAH HAFIZAH SYED ARIFFIN 2, (Anggota Senior, IEEE), SHARIFAH KAMILAH SYED-YUSOF2,
NURZAL EFFIYANA BINTI GHAZALI 2, MOHAMMED E. A. KANONA 1,
KHALID S. MOHAMED 1, (Anggota, IEEE), MUTAZ H. H. KHAIRI1, (Anggota Senior, IEEE), DAN
MOSAB HAMDAN2, (Anggota Senior, IEEE)
1 Fakultas Teknologi Telekomunikasi dan Antariksa, Universitas Masa Depan, Khartoum 10553, Sudan
2 Fakultas Teknik Elektro, Universitas Teknologi Malaysia, Johor Bahru 81310, Malaysia
3 Pusat Penelitian Interdisipliner untuk Sistem Keamanan Cerdas, Universitas Perminyakan dan Mineral King Fahd, Dhahran 31261, Arab Saudi
Penulis yang berkorespondensi: Mohamed Khalafalla Hassan (memo1023@hotmail.com)
ABSTRAK Software Defined Network (SDN) adalah salah satu teknologi jaringan modern yang
memberikan fleksibilitas jaringan dan menyederhanakan manajemen jaringan. Virtual SDN (vSDN)
meningkatkan fleksibilitas berbagi sumber daya jaringan fisik dengan beberapa irisan yang mewakili
beberapa penyewa atau layanan di mana setiap penyewa memiliki kendali atas layanan atau aplikasi
mereka melalui Virtual Network (VN). Virtualisasi jaringan memberikan fleksibilitas yang lebih besar
kepada penyedia layanan untuk menawarkan layanan baru dan inovatif dengan efisiensi dan keandalan
ekstra. Menjalankan beberapa jaringan virtual melalui infrastruktur yang diberikan menciptakan tantangan
untuk mekanisme alokasi sumber daya yang efisien untuk menghindari kemacetan dan kekurangan
sumber daya serta untuk mempertahankan Service Level Agreement (SLA), di mana manajemen sumber
daya di vSDN dilakukan oleh hypervisor. Hanya sedikit penelitian yang membahas alokasi sumber daya
dinamis dalam domain vSDN. Oleh karena itu, untuk memanfaatkan sumber daya infrastruktur jaringan
tervirtualisasi secara efisien, hypervisor jaringan harus proaktif dengan kemampuan konfigurasi ulang
mandiri untuk menetapkan sumber daya fisik dan sangat mudah beradaptasi serta bereaksi terhadap
perubahan permintaan vSDN di masa depan. Dengan demikian, hypervisor berbasis pembelajaran dinamis
adalah untuk meningkatkan operasi hypervisor. Berdasarkan hal tersebut, penelitian ini bertujuan untuk
meningkatkan teknologi vSDN untuk menyediakan mekanisme alokasi sumber daya slice dinamis proaktif
yang lebih baik, untuk meningkatkan pengiriman trafik dan pemanfaatan sumber daya. Hal ini dapat
dipenuhi dengan mengusulkan model peramalan cerdas yang disempurnakan untuk pemanfaatan sumber
daya slice vSDN berdasarkan teknik statistik dan Machine Learning (ML) yang ditingkatkan. Model yang
diusulkan akan bereaksi secara dinamis terhadap pergeseran konsep dan kemudian digunakan untuk
mengembangkan mekanisme alokasi sumber daya untuk alokasi sumber daya slice vSDN. Mekanisme
alokasi sumber daya peramalan dinamis yang ditingkatkan diverifikasi melalui kumpulan data jejak
jaringan nyata yang tersedia dari berbagai sumber. DLVisor dengan Dynamic Learning Framework (DLF)
dapat mengurangi penggunaan yang berlebihan dan, akibatnya, kelaparan sumber daya hingga 100%
dibandingkan dengan tolok ukur terkait.
INDEKS ISTILAH Pembelajaran mesin, alokasi sumber daya, perkiraan sumber daya, jaringan berbasis perangkat
lunak, virtualisasi.

I. PENDAHULUAN pesawat. Di sisi lain, virtualisasi jaringan memungkinkan
Software-defined networking (SDN) telah muncul sebagai pembagian sumber daya jaringan fisik di mana penyewa
teknologi jaringan yang menjanjikan yang memungkinkan atau pemilik slice memiliki otoritas atas sumber daya
manajemen data yang fleksibel dalam jaringan komputer jaringan virtual mereka. Jaringan dapat memanfaatkan
dan komunikasi di mana ia memisahkan bidang penerusan manfaat SDN dan Network Function Virtualization (NFV)
data dan kontrol melalui virtualisasi jaringan SDN. Hypervisor SDN
memisahkan jaringan SDN fisik yang mendasarinya menjadi
Editor pendamping yang mengkoordinasikan tinjauan naskah ini dan beberapa vSDN yang terpisah secara logis, masing-masing
menyetujuinya untuk diterbitkan adalah Mahdi Zareei . dengan pengontrolnya. Misalnya, setiap Virtual
Karya ini dilisensikan di bawah Lisensi Creative Commons Atribusi-NonKomersial-TanpaTurunan 4.0.
84144 Untuk informasi lebih lanjut, lihat https://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
hypervisor jaringan SDN harus
TABEL 1. Daftar singkatan.
Machine (VM) dan sistem operasi tamunya berjalan di atas
| platform  | komputasi  | fisik  | tertentu  | [1],  | [2],  | [3].  Selain  |
| --------- | ---------- | ------ | --------- | ----- | ----- | ------------- |
memonitor mesin virtual, hypervisor memberikan sumber
daya platform komputasi yang sebenarnya ke setiap mesin
virtual. Hypervisor membuat beberapa vSDN menggunakan
| protokol   | Open          | Flow  (OF)   | berdasarkan  |         | jaringan  | fisik         |
| ---------- | ------------- | ------------ | ------------ | ------- | --------- | ------------- |
| tertentu.  | Setiap  vSDN  | berhubungan  |              | dengan  |           | bagian  dari  |
seluruh jaringan. Teknologi jaringan masa depan di Generasi
Kelima (5G) dan seterusnya akan diaktifkan oleh vSDN [4],
| [5],  [6].  | Menjalankan  | vSDN  | pada  | infrastruktur  |     | tertentu  |
| ----------- | ------------ | ----- | ----- | -------------- | --- | --------- |
dengan mekanisme alokasi sumber daya yang efisien dapat
meningkatkan pemanfaatan perangkat keras jaringan yang
memenuhi spesifikasi penyewa dan layanan serta Perjanjian
| Tingkat  | Layanan  | (SLA).  | Tabel  | 3  menunjukkan  |     | daftar  |
| -------- | -------- | ------- | ------ | --------------- | --- | ------- |
simbol yang akan digunakan pada bagian berikut
| Selain                  | itu,  vSDN         | memungkinkan  |           |                      | penyedia   | layanan   |
| ----------------------- | ------------------ | ------------- | --------- | -------------------- | ---------- | --------- |
| jaringan                | untuk  memberikan  |               | layanan   |                      | baru  dan  | inovatif  |
| dengan  fleksibilitas,  |                    | efisiensi,    |           | dan  ketergantungan  |            | yang      |
| lebih  besar.           | Mengoperasikan     |               | beberapa  |                      | jaringan   | virtual   |
membutuhkan sumber daya jaringan fisik yang cukup besar.
Oleh karena itu, metode alokasi sumber daya yang cerdas
| dan  efisien    | sangat  | penting.  |          | Untuk   | mencapai        | dan  |
| --------------- | ------- | --------- | -------- | ------- | --------------- | ---- |
| mempertahankan  |         | kinerja   | terbaik  | secara  | terus-menerus,  |      |
VOLUME 11, 2023 84145

untuk mencapai efisiensi sumber daya yang tinggi untuk
dirancang untuk dapat beradaptasi, di mana ia haruMs. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukans Puemranbgekra td Lauynaak yang divirtualisasi. Oleh karena itu,
mengadopsi dan menerapkan pendekatan untuk konfigurasi
ulang sendiri. Untuk memastikan alokasi dan pengoptimalan
sumber daya yang lebih baik, vSDN membutuhkan kondisi
jaringan saat ini dan masa depan untuk diramalkan dan terus
dijalankan dalam mode online atau semi-online untuk
beradaptasi dengan variasi permintaan jaringan. Mekanisme dan
pendekatan semacam itu harus bekerja dalam skala waktu yang
bervariasi untuk mencapai efisiensi sumber daya yang tinggi
untuk sumber daya yang tervirtualisasi. Oleh karena itu,
hypervisor berbasis pembelajaran dinamis diperlukan untuk
meningkatkan operasi hypervisor. Desain algoritma manajemen
sumber daya hypervisor dalam menyelesaikan tantangan ini
merupakan bidang penelitian yang masih terbuka dan
membutuhkan investigasi yang mendetail [1], [4].
Untuk memanfaatkan sumber daya infrastruktur jaringan
yang tervirtualisasi secara efisien, kerangka kerja alokasi
sumber daya berbasis peramalan yang canggih diperlukan
untuk sumber daya fisik. Kerangka kerja ini harus memiliki
kecerdasan untuk mengatasi permintaan Quality of Service
(QoS) yang dinamis dan dapat bereaksi secara otonom terhadap
situasi yang dinamis dan dapat mengatur dirinya sendiri tanpa
mempengaruhi SLA. Oleh karena itu, pendekatan proaktif
untuk mengelola bandwidth dan sumber daya jaringan sangat
dibutuhkan [7], [8]. Alokasi sumber daya jaringan dinamis
y a n g proaktif bergantung pada peramalan permintaan
jaringan dan bertindak sesuai dengan itu untuk memungkinkan
respons yang tepat waktu dan dinamis. Dengan demikian,
keakuratan pendekatan prediktif dianggap sebagai faktor
penting dalam berbagai aplikasi kerangka kerja pra-diktat.
Teknik ML yang akurat sangat penting dan banyak
digunakan dalam berbagai aplikasi ferent , seperti lalu lintas
jaringan fore- casts [9], [10], [11], [12], [13], [14], Internet of
Things (IoT) [15], dan komunikasi nirkabel [16]. Manajemen
sumber daya di vSDN dilakukan oleh hypervisor SDN. Tidak
ada mekanisme alokasi sumber daya dinamis proaktif yang
disediakan dalam semua literatur terkait, metode dan kerangka
kerja yang disediakan bersifat statis (tidak dapat beradaptasi
dengan perubahan lalu lintas/jaringan) atau reaktif karena
bekerja pada kondisi saat ini tanpa peramalan sumber daya
yang dapat menyebabkan kelaparan sumber daya. Oleh karena
itu, sangat penting untuk mengembangkan kerangka kerja
pembelajaran yang dinamis untuk mengalokasikan dan
memodifikasi irisan lebar pita untuk pemanfaatan sumber daya
yang lebih baik dan untuk menghindari kelaparan sumber daya
dan pelanggaran SLA karena kemacetan dan degradasi QoS.
Penelitian ini bertujuan untuk meningkatkan teknologi
vSDN dengan menyediakan mekanisme alokasi sumber daya
slice dinamis yang lebih baik untuk meningkatkan
pemanfaatan sumber daya dan meminimalkan kelaparan
sumber daya. Tujuan khusus dari penelitian ini adalah untuk
meningkatkan mekanisme alokasi slice di vSDN berdasarkan
manajemen slice proaktif berdasarkan sumber daya (bandwidth
fore- cast) yang akan direfleksikan sebagai hasil untuk
menghilangkan jumlah penggunaan yang berlebihan dan
meminimalkan kemacetan dan kelaparan sumber daya.
Penelitian ini memberikan kontribusi pada teknologi vSDN
dengan memberikan kemampuan kepada hypervisor untuk
mengelola dan meningkatkan kinerjanya secara mandiri karena
manajemen bandwidth slice merupakan salah satu sumber daya
penting yang harus bekerja dalam skala waktu yang singkat
84146 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
Embedding (VNE) [1].
penelitian ini akan secara proaktif menyediakan hypervisor
Masalah VNE adalah Non-deterministic Polynomial-
berbasis pembelajaran ML untuk menghindari kelaparan
|     |     |     |     |     |     |     |     | time  hardness  | (NP-hard)  dan  | masih  diselidiki  | secara  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------------- | ------------------ | ------- |
sumber daya slice dan viola- si SLA di vSDN. Hal ini
ekstensif. Secara umum, menerima dan menolak sumber
mencakup:
daya jaringan virtual
| 1) mengintegrasikan  |     |               | model      |              | peramalan  |     | statis  yang  |     |     |     |     |
| -------------------- | --- | ------------- | ---------- | ------------ | ---------- | --- | ------------- | --- | --- | --- | --- |
| disempurnakan        |     |               | ke  dalam  |              | manajemen  |     | slice  vSDN   |     |     |     |     |
| untuk                |     | meningkatkan  |            | pemanfaatan  |            |     | slice  vSDN   |     |     |     |     |
berdasarkan teknik ML.
| 2) mengadopsi  |     |     | model    | peramalan  |     | statis     | dengan  |     |     |     |     |
| -------------- | --- | --- | -------- | ---------- | --- | ---------- | ------- | --- | --- | --- | --- |
| menggunakan    |     |     | dynamic  | learning   |     | framework  | (DLF)   |     |     |     |     |
untuk mengurangi kesalahan peramalan model statis
| akibat  | perubahan  |     | konsep  |     | untuk  | memperbarui  | dan  |     |     |     |     |
| ------- | ---------- | --- | ------- | --- | ------ | ------------ | ---- | --- | --- | --- | --- |
meningkatkan validitas model.
3) mengusulkan alokasi slice sumber daya (bandwidth)
yang ditingkatkan secara proaktif serta manajemen
| penawaran     |     | dan    | permintaan    |     | di  vSDN  | menggunakan  |         |     |     |     |     |
| ------------- | --- | ------ | ------------- | --- | --------- | ------------ | ------- | --- | --- | --- | --- |
| kerangka      |     | kerja  | pembelajaran  |     |           | dinamis      | untuk   |     |     |     |     |
| meminimalkan  |     |        | kemacetan     |     | dan       | kelaparan    | sumber  |     |     |     |     |
daya. Kerangka kerja manajemen slice vSDN yang
diusulkan akan diberi nama DLVisor.
Organisasi makalah ini adalah sebagai berikut, bagian II
memberikan pengantar singkat tentang jaringan virtual dan
| virtualisasi,  | SDN  |     | dan  vSDN,  |     | bagian  | III  | membahas  |     |     |     |     |
| -------------- | ---- | --- | ----------- | --- | ------- | ---- | --------- | --- | --- | --- | --- |
manajemen sumber daya mutakhir dalam teknologi vSDN,
bagian IV menyajikan metodologi keseluruhan, algoritma,
| arsitektur  | dan  | implementasi  |     | alokasi  |     | slice  | bandwidth  |     |     |     |     |
| ----------- | ---- | ------------- | --- | -------- | --- | ------ | ---------- | --- | --- | --- | --- |
dinamis, bagian VI membahas hasil dan temuan sementara
bagian VII memberikan kesimpulan
II. LATAR BELAKANG
| Network  | Virtualization  |     |     | (NV)  | telah  | diturunkan  | dari  |     |     |     |     |
| -------- | --------------- | --- | --- | ----- | ------ | ----------- | ----- | --- | --- | --- | --- |
keberhasilan virtualisasi dalam domain komputasi [1], [17].
| NV  menciptakan  |     | jaringan  |     | virtual  | yang  | terpisah  | (slices)  |     |     |     |     |
| ---------------- | --- | --------- | --- | -------- | ----- | --------- | --------- | --- | --- | --- | --- |
melalui abstraksi khusus dan isolasi blok fungsional [1].
Dalam domain jaringan, konsep slicing sudah ada. Sebagai
contoh, jaringan berbasis serat optik, Wavelength Division
| Multiplexing  |         | (WDM)      | [18]  | dapat          | membuat  |       | slices  pada   |     |     |     |     |
| ------------- | ------- | ---------- | ----- | -------------- | -------- | ----- | -------------- | --- | --- | --- | --- |
| lapisan       | fisik,  | sedangkan  |       | pada  lapisan  |          | link  | dapat  dibuat  |     |     |     |     |
Virtual Local Area Network (VLAN) dan Multiple Protocol
Label Switching (MPLS) [7], [19].
| Sebaliknya,   |          | virtualisasi  |            | jaringan  | cenderung  |     | membuat   |     |     |     |     |
| ------------- | -------- | ------------- | ---------- | --------- | ---------- | --- | --------- | --- | --- | --- | --- |
| irisan  dari  | seluruh  |               | jaringan,  | yaitu     | membentuk  |     | jaringan  |     |     |     |     |
virtual (irisan) di semua lapisan protokol jaringan. Setiap
saat, slice yang diberikan harus memiliki sumber dayanya
(abstraksi spesifik dari topologi jaringan, bandwidth tautan,
sumber daya komputasi switch dan tabel penerusan switch).
| Jaringan  | virtual  |     | (slice)  | memungkinkan  |     |     | pengujian  |     |     |     |     |
| --------- | -------- | --- | -------- | ------------- | --- | --- | ---------- | --- | --- | --- | --- |
paradigma jaringan baru, tanpa memperhatikan kepatutan
| dan  pembatasan  |     | yang  | diberlakukan  |     |     | oleh  | struktur  dan  |     |     |     |     |
| ---------------- | --- | ----- | ------------- | --- | --- | ----- | -------------- | --- | --- | --- | --- |
protokol internet saat ini [1]. Menjalankan beberapa jaringan
| virtual  | melibatkan  | konsumsi  |     | sumber  |     | daya  jaringan  | fisik  |     |     |     |     |
| -------- | ----------- | --------- | --- | ------- | --- | --------------- | ------ | --- | --- | --- | --- |
dalam jumlah tertentu. Oleh karena itu, mekanisme alokasi
sumber daya yang efisien dan canggih sangat dibutuhkan
[8], [20]. Sebagai contoh, interkoneksi antara node virtual,
jalur virtual dan penempatan VM pada infrastruktur fisik,
| hal  ini        | juga  | dikenal  | sebagai  | masalah  |     | Virtual  | Network  |     |     |     |       |
| --------------- | ----- | -------- | -------- | -------- | --- | -------- | -------- | --- | --- | --- | ----- |
| VOLUME 11, 2023 |       |          |          |          |     |          |          |     |     |     | 84147 |

melalui protokol SDN, OF sebagai contoh. Dalam kasus
M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
DitentukanN PeVra,n hgkyapt eLurnvaiksor beroperasi
GAMBAR 1. Arsitektur vSDN.
Permintaan alokasi dapat dilakukan dengan mekanisme kontrol
penerimaan. Algoritma optimasi VNE saat ini berkisar dari
formulasi yang tepat, seperti pro- gram linear bilangan bulat
campuran, hingga pendekatan heuristik berdasarkan,
dimungkinkan untuk menghubungkan
penetapan sumber daya vSDN ke probabilitas VNE umum
dan menguraikan penggunaan metrik kinerja VNE umum
rics dalam konteks SDN. Beberapa survei tinjauan umum yang
telah dipublikasikan telah membahas prinsip, manfaat, dan
pendekatan virtualisasi jaringan. Sebagai contoh, survei
terperinci mengenai hypervisor virtualisasi jaringan untuk SDN
dapat ditemukan di [1].
Kemampuan untuk memprogram jaringan virtual
menggunakan SDN merupakan aspek kunci penting lainnya
dari virtualisasi jaringan total [21]. Melihat virtualisasi
jaringan lama, seperti virtualisasi berbasis VLAN tanpa fitur
pemrograman, penyewa tidak akan dapat menginstruksikan
sakelar untuk melakukan tindakan seperti manajemen lalu
lintas, yaitu pengarahan lalu lintas. Namun demikian, untuk
mewujudkan NFV sepenuhnya, penyewa harus mendapatkan
sumber daya jaringan virtual, seperti tampilan total topologi
jaringan dan sumber daya jaringan yang dialokasikan, yang
melibatkan kecepatan data tautan dan sumber daya simpul
jaringan. Selain itu, menyediakan jaringan virtual yang
terisolasi dan dapat diprogram memiliki keuntungan yang
signifikan. Dalam kasus seperti ini, operator jaringan dapat
mengembangkan dan menguji teknologi jaringan dengan
batasan yang tidak terlalu berat [22]. Selain itu, NV dianggap
sebagai pemain kunci dalam menyediakan kinerja jaringan
yang dapat diprediksi (terjamin) [23]. Secara berurutan,
Penyedia Layanan (SP) akan dapat menyediakan atau
menyediakan layanan baru melalui infrastruktur yang ada
dengan cara yang jauh lebih cepat dan lebih dapat diandalkan.
Selain itu, SP akan memungkinkan jaringan mereka untuk
secara dinamis mengubah dan memodifikasi jaringan virtual
mereka ork sesuai dengan perubahan permintaan pengguna dan
layanan [24], [25], [26]. Lapisan virtualisasi jaringan
memungkinkan hosting beberapa pengontrol [26], [27].
Hypervisor jaringan berkomunikasi dengan perangkat keras
jaringan yang mendasarinya melalui antarmuka southbound
84148 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
|     |     |     |     |     |     |     |     | berbeda  yang ditulis  |     | untuk  | pengontrol  | tertentu  untuk  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------ | ----------- | ---------------- |
di atas antarmuka jalur selatan yang sama untuk operator
berjalan pada pengontrol lain yang ditulis dalam bahasa
| jaringan    | virtual      | dan  | menuju  | penyewa  |           | jaringan  | SDN.     |                    |     |           |          |                  |
| ----------- | ------------ | ---- | ------- | -------- | --------- | --------- | -------- | ------------------ | --- | --------- | -------- | ---------------- |
|             |              |      |         |          |           |           |          | lain;  hypervisor  |     | komposit  | membuat  | kebijakan  yang  |
| Hypervisor  | dihubungkan  |      | dengan  |          | beberapa  | jalur     | selatan  |                    |     |           |          |                  |
disusun yang mewakili daftar aturan yang diprioritaskan
dengan beberapa pengontrol SDN [27]. Hypervisor SDN
per sakelar SDN yang disediakan oleh pengontrol SDN
beroperasi sebagai proxy. Ini mencegat dan menerjemahkan
|                 |     |         |          |      |           |      |         | yang  sesuai,  | dan  | kemudian  | hypervisor  | komposit  |
| --------------- | --- | ------- | -------- | ---- | --------- | ---- | ------- | -------------- | ---- | --------- | ----------- | --------- |
| pesan  kontrol  |     | antara  | penyewa  | dan  | jaringan  | SDN  | fisik.  |                |      |           |             |           |
membentuk
Gambar 1 menunjukkan arsitektur vSDN.
Dengan menggabungkan SDN dan NFV, penyewa akan
| memiliki  | keunggulan  |     | fleksibilitas  |     | dalam  | berbagi  | sumber  |     |     |     |     |     |
| --------- | ----------- | --- | -------------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- |
daya melalui berbagi jaringan virtual selain memiliki fitur
| programabilitas  |     | dari  SDN,  |     | sedangkan  | NFV  | memberikan  |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | ---------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
kemampuan untuk memprogram sumber daya virtual [25]
di mana kombinasi tersebut disebut vSDN [24], [26]. Hal
| ini  dapat  | dilihat  | pada  | Gambar  |     | 1  yang  | menunjukkan  |     |     |     |     |     |     |
| ----------- | -------- | ----- | ------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
arsitektur vSDN.
III. PEKERJAAN TERKAIT
| Bagian  | ini  membahas  |     | pekerjaan  |     | terkait  | dalam  | konteks  |     |     |     |     |     |
| ------- | -------------- | --- | ---------- | --- | -------- | ------ | -------- | --- | --- | --- | --- | --- |
manajemen bandwidth dinamis (slice) di vSDN. Seperti
| yang  telah  | dijelaskan  |            | di  bagian  |          | sebelumnya,   |      | hypervisor  |     |     |     |     |     |
| ------------ | ----------- | ---------- | ----------- | -------- | ------------- | ---- | ----------- | --- | --- | --- | --- | --- |
| melakukan    | tugas       | manajemen  |             | sumber   | daya,         | dan  | semua       |     |     |     |     |     |
| hypervisor   | vSDN        | dianggap   |             | sebagai  | perpanjangan  |      | dari        |     |     |     |     |     |
hypervisor FlowVisor.
| FlowVisor  |     | (FV)  adalah  |     | hypervisor  |     | pertama  | untuk  |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- |
jaringan SDN, yang menyediakan fitur berbagi sumber daya
| jaringan  | SDN  | di  antara  | beberapa  |     | pengontrol.  |     | FV  pada  |     |     |     |     |     |
| --------- | ---- | ----------- | --------- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
akhirnya dapat menjalankan sebagai perangkat lunak yang
| berdiri  | sendiri  | pada  perangkat  |     | keras  | komoditas  |     | (server)  |     |     |     |     |     |
| -------- | -------- | ---------------- | --- | ------ | ---------- | --- | --------- | --- | --- | --- | --- | --- |
[28]. FV adalah hypervisor untuk keperluan umum dan
| merupakan  | dasar  | untuk  | hypervisor  |     | vSDN  | lainnya.  | Ia  |     |     |     |     |     |
| ---------- | ------ | ------ | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
menawarkan isolasi atribut node seperti Central Processing
Unit (CPU) dan Flow table selain bandwidth sebagai isolasi
atribut link. FV terutama menekankan pendekatan untuk
mengisolasi lalu lintas jaringan di jaringan eksperimental
dari lalu lintas di jaringan produksi di mana ia menyediakan
| definisi     | yang  | fleksibel  | dari   | irisan  | jaringan.  | Namun,   | ia     |     |     |     |     |     |
| ------------ | ----- | ---------- | ------ | ------- | ---------- | -------- | ------ | --- | --- | --- | --- | --- |
| menambahkan  |       | latensi    | dalam  | pesan   |            | OF  dan  | tidak  |     |     |     |     |     |
menunjukkan kontrol penerimaan dan tidak ada mekanisme
untuk manajemen dan optimasi irisan.
| MobileVisor  |        | dalam     | [29]  | ,  menerapkan  |     | pendekatan  |           |     |     |     |     |     |
| ------------ | ------ | --------- | ----- | -------------- | --- | ----------- | --------- | --- | --- | --- | --- | --- |
| FlowVisor    | dalam  | jaringan  |       | inti  paket    |     | seluler;    | di  mana  |     |     |     |     |     |
fungsionalitas FlowVisor diintegrasikan ke dalam struktur
arsitektur jaringan paket seluler virtual yang terdiri dari
beberapa jaringan seluler fisik di bawahnya, seperti jaringan
| 3G  dan  | 4G.  | Hal  ini  | memungkinkan  |     | Penyedia  |     | Layanan  |     |     |     |     |     |
| -------- | ---- | --------- | ------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- |
Internet (ISP) untuk menentukan kebijakan dan layanan
berbasis QoS di samping operator seluler tersebut. Selain
citiue,s  lIeSbPi ha ekfaisni end.apat mengelola kebijakan pengisian daya
mereka.
Tidak ada penghitungan latensi yang
disebutkan; namun, karena hypervisor ini mengadopsi FV,
ia tidak memiliki manajemen sumber daya dinamis .
| Dalam  | [30]  | penulis  |     | memperkenalkan  |     | hypervisor  |     |     |     |     |     |     |
| ------ | ----- | -------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
komposisional untuk menyediakan platform fleksibel yang
| memungkinkan  |     | operator jaringan  |     |     | SDN  | memilih berbagai  |     |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | --- | ---- | ----------------- | --- | --- | --- | --- | --- | --- |
aplikasi jaringan yang dikembangkan untuk pengontrol SDN
| yang  berbeda.  |     | Ini  akan  | memungkinkan  |     |     | aplikasi  | yang  |     |     |     |     |       |
| --------------- | --- | ---------- | ------------- | --- | --- | --------- | ----- | --- | --- | --- | --- | ----- |
| VOLUME 11, 2023 |     |            |               |     |     |           |       |     |     |     |     | 84149 |

|     |     |     |     |     |     |     |     | diperlukan,  | yaitu  load  balancer  | tidak  selalu  | memerlukan  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------- | -------------- | ----------- |
konfigurasi  komposisi  untuk  memproses  aturan  SDNM,.  K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukant aPemrapniglkaant  Ltuonpaoklogi yang terperinci
penelitian ini menekankan pada waktu pembentukan kebijakan
komposisi yang ditambahkan pada latensi hypervisor OF, selain
itu, daftar prioritas bersifat statis dan tidak mengalokasikan
atau mengelola sumber daya secara dinamis.
Penulis [21] mengusulkan Network Virtualization Plat- form
(NVP), dengan fokus pada abstraksi sumber daya jaringan
pusat data yang dikelola oleh penyewa cloud untuk lingkungan
| multi-penyewa,  | yang  |     | berfungsi  | sebagai  |     | pengontrol  | untuk  |     |     |     |     |
| --------------- | ----- | --- | ---------- | -------- | --- | ----------- | ------ | --- | --- | --- | --- |
menyediakan penyewa SDN untuk mengoperasikan pengontrol
SDN mereka melalui Antarmuka Pemrograman Aplikasi (API)
dan mengontrol irisan mereka di pusat data. Hal ini dilakukan
| dengan  | membentuk  | klaster  |     | pengontrol  | terdistribusi  |     | untuk  |     |     |     |     |
| ------- | ---------- | -------- | --- | ----------- | -------------- | --- | ------ | --- | --- | --- | --- |
menskalakan beban penyewa sesuai kebutuhan dengan sakelar
tervirtualisasi untuk mengarahkan lalu lintas penyewa ke mesin
virtual yang sesuai dengan berfokus pada perangkat lunak yang
ada di dalam sakelar virtual di server host. NVP umumnya
| membuat      | jalur  data    | logis  | (terowongan)  |        | antara   |       | tujuan  dan   |     |     |     |     |
| ------------ | -------------- | ------ | ------------- | ------ | -------- | ----- | ------------- | --- | --- | --- | --- |
| sumber       | Open  Virtual  |        | Switch        | (OVS)  | di       | mana  | jalur  logis  |     |     |     |     |
| berhubungan  | dengan         |        | potongan      |        | penyewa  | yang  | sesuai        |     |     |     |     |
menggunakan teknik tunneling Generic Routing Encapsulation
(GRE) .
| Hypervisor         | OpenVirteX  |         | pada      | [31]    | diperkenalkan  |     | dengan   |     |     |     |     |
| ------------------ | ----------- | ------- | --------- | ------- | -------------- | --- | -------- | --- | --- | --- | --- |
| dua  kontribusi    |             | utama:  | topologi  | dan     | virtualisasi   |     | alamat.  |     |     |     |     |
| OpenVirteX         | memperluas  |         | FV        | dengan  | menangani      |     | masalah  |     |     |     |     |
| ruang  aliran.     | Hal         | ini     | dicapai   | dengan  | menggunakan    |     | header   |     |     |     |     |
| untuk  membedakan  |             | vSDN    | daripada  |         | menyediakan    |     | seluruh  |     |     |     |     |
ruang bidang header ke vSDN. Dalam OpenVirteX, switch
menulis ulang alamat Internet Protocol (IP) dan Media Access
Control (MAC) yang diberikan secara virtual yang digunakan
| oleh  host   | setiap      | vSDN  | (penyewa).  |           | Open-  | Virtex  | tidak  |     |     |     |     |
| ------------ | ----------- | ----- | ----------- | --------- | ------ | ------- | ------ | --- | --- | --- | --- |
| menambahkan  | kontribusi  |       | yang        | berharga  | pada   | sumber  | daya   |     |     |     |     |
dinamis manajemen.
| Dalam  | [32],  hypervisor  |     | Datapath  |     | centric  | diperkenalkan  |     |     |     |     |     |
| ------ | ------------------ | --- | --------- | --- | -------- | -------------- | --- | --- | --- | --- | --- |
untuk mengatasi masalah redundansi pada FV (Single point of
failure) dan meningkatkan kinerja lapisan virtualisasi melalui
implementasi fungsi virtualisasi sebagai ekstensi switch. Ini
bekerja dengan mengimplementasikan Agen Virtualisasi (VA)
di dalam sakelar di samping Virtualization Agent Orchestrator
(VAO). Tanggung jawab utama VAO adalah pemantauan dan
konfigurasi slice, contohnya adalah menambah atau menghapus
slice. Di sisi lain, VA bertanggung jawab untuk berkomunikasi
dengan pengontrol vSDN selain abstraksi sumber daya untuk
| VAO.  | Jika  VAO  | gagal,  |     | VA  dapat  |     | terus  | beroperasi,  |     |     |     |     |
| ----- | ---------- | ------- | --- | ---------- | --- | ------ | ------------ | --- | --- | --- | --- |
menghindari satu titik kegagalan dalam arsitektur Flow visor.
Datacentris tidak mendukung isolasi bandwidth tetapi masih
dapat mendukung QoS berdasarkan evaluasi yang ekstensif.
Kasus VA menambahkan overhead sebesar 18% dibandingkan
dengan kasus referensi. Latensi overhead failover sekitar 3ms.
Meskipun dapat mendukung QoS, kurangnya isolasi bandwidth
| tidak  akan  | memungkinkan  |     |     | alokasi  | potongan  |     | bandwidth  |     |     |     |     |
| ------------ | ------------- | --- | --- | -------- | --------- | --- | ---------- | --- | --- | --- | --- |
dinamis.
Dalam [33], CoVisor diperkenalkan sebagai perpanjangan dari
sebuah
hypervisor komposisi yang memfasilitasi kerja sama
pengontrol heterogen untuk bekerja pada jenis trafik yang
sama
fic dengan lebih fokus pada peningkatan kinerja jaringan fisik
| SDN,        | yaitu  ruang  | tabel      | aliran       |       | dan  abstraksi  |           | topologi    |     |     |     |                 |
| ----------- | ------------- | ---------- | ------------ | ----- | --------------- | --------- | ----------- | --- | --- | --- | --------------- |
| sedemikian  | rupa          | untuk      | menyediakan  |       | sumber          |           | daya  yang  |     |     |     |                 |
| diperlukan  | seperti       | informasi  |              | atau  | abstraksi       | topologi  | saat        |     |     |     |                 |
| 84150       |               |            |              |       |                 |           |             |     |     |     | VOLUME 11, 2023 |

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
virtual, yang dapat berbeda dari satu domain ke domain
| untuk  memutuskan  |     |     | untuk  | menjatuhkan  |     | atau  | meneruskan  |     |     |     |
| ------------------ | --- | --- | ------ | ------------ | --- | ----- | ----------- | --- | --- | --- |
lainnya ternyata cukup tinggi (sekitar 5,85 ms). Proses
sebuah paket. Selain itu, ini memberikan bentuk keamanan
kontrol bersifat manual dan tidak mempertimbangkan
| terhadap  | pengontrol  |     | SDN  | yang  |     | curang.  | CoVisor  |     |     |     |
| --------- | ----------- | --- | ---- | ----- | --- | -------- | -------- | --- | --- | --- |
distribusi beban dinamis.
meningkatkan latensi hypervisor komposisional sebanyak
|              |       |       |         |         |             |     |            | Dalam  [39],      | ONVisor  Hypervisor  | disajikan  sebagai  |
| ------------ | ----- | ----- | ------- | ------- | ----------- | --- | ---------- | ----------------- | -------------------- | ------------------- |
| dua  hingga  | tiga  | kali  | lipat.  | Namun,  | hypervisor  |     | ini tidak  |                   |                      |                     |
|              |       |       |         |         |             |     |            | platform  SDN-NV  | untuk  memberikan    | fleksibilitas       |
menyediakan alokasi sumber daya dinamis .
|        |        |     |          |               |     |     |             | dengan  mengadopsi  | instance  hypervisor  | terdistribusi  |
| ------ | ------ | --- | -------- | ------------- | --- | --- | ----------- | ------------------- | --------------------- | -------------- |
| Dalam  | [34],  |     | DFVisor  | (Distributed  |     |     | FlowVisor)  |                     |                       |                |
yang memungkinkan berbagi status VN. Selain itu,
| diperkenalkan  |     | untuk  | mengatasi  |     | masalah  | skalabilitas  | FV  |     |     |     |
| -------------- | --- | ------ | ---------- | --- | -------- | ------------- | --- | --- | --- | --- |
sebagai hypervisor virtualisasi SDN terpusat. Ini membahas
| kemungkinan  |     | memperluas  |     | sakelar  |     | SDN  | dengan  |     |     |     |
| ------------ | --- | ----------- | --- | -------- | --- | ---- | ------- | --- | --- | --- |
kemampuan hypervisor, menghasilkan sakelar OpenFlow
| yang  | disempurnakan  |     | yang  | dapat  |     | dicapai  | dengan  |     |     |     |
| ----- | -------------- | --- | ----- | ------ | --- | -------- | ------- | --- | --- | --- |
memperluas sakelar SDN dengan modul tunneling lokal
dan pengiris vSDN. DFVisor menggunakan tunneling GRE
untuk pemotongan paket data dan enkapsulasi aliran data
yang sangat bermanfaat dalam mengadopsi QoS. DFvisor
| mengadopsi  |           | database  | terdistribusi  |          | tersinkronisasi  |     | dua          |     |     |     |
| ----------- | --------- | --------- | -------------- | -------- | ---------------- | --- | ------------ | --- | --- | --- |
| tingkat,    | database  |           | pertama        | (lokal)  | berada           |     | di  switch,  |     |     |     |
| sedangkan   | database  |           | global         |          | mempertahankan   |     | irisan       |     |     |     |
informasi statistik, operasi jaringan, dan skalabilitas yang
| ditingkatkan.  |     | Namun,  | solusi  | yang  | diusulkan  |     | ditujukan  |     |     |     |
| -------------- | --- | ------- | ------- | ----- | ---------- | --- | ---------- | --- | --- | --- |
untuk lingkungan cluster.
| EnterpriseVisor  |     | di  | [35],  | adalah  | salah  | satu  | hypervisor  |     |     |     |
| ---------------- | --- | --- | ------ | ------- | ------ | ----- | ----------- | --- | --- | --- |
yang paling terkenal terkait alokasi sumber daya slice. Ini
| memperkenalkan    |       | modul        | perangkat     |         | lunak        | yang       | diperluas  |     |     |     |
| ----------------- | ----- | ------------ | ------------- | ------- | ------------ | ---------- | ---------- | --- | --- | --- |
| untuk  memonitor  |       | dan          | menganalisis  |         | pemanfaatan  |            | slice.     |     |     |     |
| Selain            | itu,  | pemrograman  |               | linier  |              | digunakan  | untuk      |     |     |     |
menyesuaikan irisan bandwidth secara dinamis, mesin yang
diusulkan menghalangi peminta irisan dan penyedia sumber
| daya  untuk      | memenuhi  |               | persyaratan  |              | layanan.  |                 | Selanjutnya,  |     |     |     |
| ---------------- | --------- | ------------- | ------------ | ------------ | --------- | --------------- | ------------- | --- | --- | --- |
| EnterpriseVisor  |           | berinteraksi  |              |              | dengan    | Flow            | Visor,        |     |     |     |
| menerapkan       |           | kebijakan     | slicing      |              | untuk     | mengonfigurasi  |               |     |     |     |
| jaringan.        | Dengan    |               | demikian,    | konfigurasi  |           | slice           | dapat         |     |     |     |
disesuaikan untuk memenuhi persyaratan layanan.
Dalam [36], platform manajemen jaringan virtual berbasis
niat berdasarkan SDN diusulkan untuk mengotomatiskan
| konfigurasi  | dan  | manajemen  |     | sumber  | daya  | VN  | dari  sisi  |     |     |     |
| ------------ | ---- | ---------- | --- | ------- | ----- | --- | ----------- | --- | --- | --- |
penyewa. Kerangka kerja ini didasarkan pada OpenVirtex.
Kerangka kerja yang diusulkan menyederhanakan definisi
dan manajemen sumber daya dari sisi administratif melalui
| representasi  |     | kebutuhan  | bisnis  |     | tingkat  | tinggi  | karena  |     |     |     |
| ------------- | --- | ---------- | ------- | --- | -------- | ------- | ------- | --- | --- | --- |
manajemen sumber daya VN merupakan proses yang rumit
dan memakan waktu selain kurangnya proses penyediaan
| otomatis  | yang  | tersedia.  | Lapisan  |     | maksud  | membantu  | s   |     |     |     |
| --------- | ----- | ---------- | -------- | --- | ------- | --------- | --- | --- | --- | --- |
penyewa untuk menentukan persyaratan tingkat tinggi.
Dalam [37] dan [38], AutoVFlow diperkenalkan sebagai
hypervisor yang didelegasikan untuk digunakan di jaringan
| area  luas  | di  | mana  | infrastruktur  |     | yang  | mendasarinya  |     |     |     |     |
| ----------- | --- | ----- | -------------- | --- | ----- | ------------- | --- | --- | --- | --- |
menjangkau domain yang tidak tumpang tindih. Hypervisor
| bertanggung  | jawab       |           | untuk           | setiap      | domain      | dan            | bertindak      |     |     |     |
| ------------ | ----------- | --------- | --------------- | ----------- | ----------- | -------------- | -------------- | --- | --- | --- |
| sebagai      | proxy       | yang      | melakukan       |             | pemetaan    |                | irisan  dan    |     |     |     |
| abstraksi    | AutoVFlow   |           | mendelegasikan  |             |             | administrasi   | dari           |     |     |     |
| pengontrol   | beban       | berat     | ke              | pengontrol  |             | lain           | yang  lebih    |     |     |     |
| ringan.      | Kebijakan   |           | pembaruan       | yang        | solid       | dipertahankan  |                |     |     |     |
| antara       | pengontrol  | terpusat  |                 | dan         | pengontrol  |                | terdistribusi  |     |     |     |
| karena       | satu        | slice     | dapat           | menjangkau  |             | beberapa       | domain.        |     |     |     |
Beberapa identitas yang digunakan, seperti alamat MAC
VOLUME 11, 2023 84151

masa depan
mendukung berbagai protokol SDN seperti Netconf dan LISPM.. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
Terakhir, ini diuji dan dievaluasi dalam skenario minimal.
Tidak ada alokasi sumber daya dinamis yang dibahas.
Dalam [40], sebuah kerangka kerja manajemen
diperkenalkan untuk menyediakan manajemen bandwidth
melalui definisi ambang batas statis untuk setiap slice
berdasarkan prioritas slice sebelumnya; kerangka kerja ini
disajikan sebagai mekanisme kontrol penerimaan. kerangka
kerja yang diusulkan terdiri dari Decision Making (DM)
Module, yang memutuskan berapa banyak bandwidth yang
akan dialokasikan berdasarkan permintaan request handler dan
informasi database module (DB). Namun, tidak ada penilaian
rinci yang diberikan pada latensi dan overhead. Selain itu,
kerangka kerjanya adalah statis dan hanya didasarkan pada
kondisi saat ini.
Dalam [41] kerangka kerja DART dapat secara dinamis
mendistribusikan bandwidth jaringan ke berbagai tempat untuk
memanfaatkan sumber daya jaringan secara efisien. Kerangka
kerja ini mengadopsi mekanisme kontrol penerimaan untuk
mendistribusikan bandwidth jaringan sesuai permintaan.
Ruang lingkupnya terbatas pada Industrial Internet of Things
(IIOT) dan hanya bekerja pada kondisi saat ini. Dalam
kerangka kerja ini, dua modul diusulkan, modul komunikasi
dan penerbitan. Modul komunikasi digunakan untuk mengirim
dan menerima informasi, sedangkan modul penerbitan
digunakan untuk mengkoordinasikan antara pengontrol.
Komputasi terpusat bertanggung jawab untuk memberi saran
bandwidth terbaik untuk setiap pengontrol SDN. Kontrol
penerimaan dapat dipicu oleh beban, prioritas, dan rasio
kehilangan paket untuk mendistribusikan kembali bandwidth
jaringan. Makalah ini menggunakan prioritas untuk lalu lintas
sebagai pemicu berdasarkan tingkat QoS yang diminta.
Dalam [42], manajer sumber daya PrioSDN (PrioSDN_RM)
disajikan sebagai kerangka kerja manajemen sumber daya
untuk memberikan kontrol penerimaan untuk jaringan berbasis
SDN yang tervirtualisasi. Mekanisme yang diusulkan
menerapkan batasan pada pemanfaatan sumber daya untuk
irisan virtual. Ini mengadopsi pendekatan untuk memanfaatkan
mekanisme distribusi bandwidth untuk bereaksi secara dinamis
terhadap perubahan beban. Mekanisme ini bergantung pada
prioritas aliran, bukan prioritas perangkat. Selain itu, ambang
batas bandwidth bergerak sesuai dengan aliran kritis yang telah
ditentukan sebelumnya. penyimpanan terus melacak
pemanfaatan bandwidth saat ini, dan modul komputasi
menghitung sumber daya bandwidth yang tersedia. Kemudian,
ia mengalokasikan jumlah sumber daya bandwidth yang
diperlukan dengan bantuan manajer aturan aliran dan manajer
ambang batas, yang menetapkan jumlah bandwidth
berdasarkan prioritas aliran, asalkan ambang batas prioritas
dapat dipindahkan berdasarkan prioritas aliran yang telah
ditentukan. Metodologi yang diusulkan bekerja mirip dengan
pendekatan kami, tetapi bekerja dalam konsumsi bandwidth
saat ini, yang dapat menyebabkan kelaparan sumber daya ation.
Pada [43], hypervisor Libera diperkenalkan untuk mengatasi
skalabilitas dan kemudahan penyewa untuk menyediakan
layanan mereka. Masalah skalabilitas terutama diselesaikan
dengan melakukan migrasi VM dan modifikasi arsitektur di
mana aturan Flow dikurangi; oleh karena itu, bandwidth antara
pengontrol dan sakelar virtual akan diminimalkan. Libera
dianggap sebagai perpanjangan dari OpenVirtx. Skalabilitas
sumber daya dilakukan pada saat ini tanpa mempertimbangkan
84152 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 2. Cakupan manajemen sumber daya di vSDN.
bandwidth di hypervisor vSDN yang dapat dikonfigurasi
tuntutan. Selain itu, tidak ada investigasi terperinci yang
sendiri dan dioptimalkan di mana solusi yang disajikan
dilakukan pada skalabilitas berdasarkan migrasi VM.
(DLVisor) akan menjadi yang pertama untuk
Dalam [44], TeaVisor disajikan untuk menjamin isolasi
menggabungkan hypervisor berbasis pembelajaran
bandwidth di vSDN. Hypervisor yang diusulkan menangani
melalui ML dan manajemen sumber daya berbasis
masalah tautan yang kelebihan beban dengan menggunakan
matematika.
algoritma heuristik serakah untuk membagi lalu lintas
ment di vSDN.
tautan yang kelebihan beban ke beberapa jalur yang tidak
kelebihan beban. Hasilnya cukup menjanjikan dan mirip
dengan apa yang dibahas dalam makalah ini. Namun,
algoritma ini didasarkan pada pengukuran trafik saat ini,
yang dapat menyebabkan sumber daya (kelaparan
bandwidth).
Dalam [45], penulis mengusulkan arsitektur manajemen
sumber daya untuk skalabilitas beban pengontrol SDN
multidomain menggunakan hypervisor non-SDN. Kerangka
kerja ini didasarkan pada pembuatan VM baru untuk
pengontrol atau migrasi pengontrol SDN berdasarkan
peningkatan beban; Agen perangkat lunak digunakan dalam
memantau beban pengontrol. Namun, tidak seperti
hypervisor berbasis SDN, menggunakan hypervisor yang
berdiri sendiri menambah masalah kurangnya isolasi sumber
daya untuk pengontrol SDN. Selain itu, pembuatan dan
migrasi langsung VM melibatkan waktu henti layanan.
Dalam semua literatur terkait, metodologi dan kerangka
kerja yang disediakan bersifat statis (tidak dapat beradaptasi
dengan perubahan lalu lintas/jaringan) atau reaktif karena
bekerja dalam kondisi saat ini tanpa peramalan sumber
daya, yang dapat menyebabkan kelaparan sumber daya.
Seperti yang digambarkan pada Gambar 2, makalah ini
akan berkonsentrasi pada manajemen sumber daya
VOLUME 11, 2023 84153

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 3. Komponen manajemen sumber daya vSDN di DLVisor.
IV. ALOKASI PENGIRIMAN LEBAR BAND DINAMIS
UNTUK vSDN
| Pekerjaan  | ini  didasarkan  | pada  | EnterpriseVisor  |     | [35]  yang  |
| ---------- | ---------------- | ----- | ---------------- | --- | ----------- |
berfokus pada
pada peningkatan hypervisor yang ada saat ini yang harus
| dapat  bekerja  | terlepas         | dari  topologi  | yang          | mendasari   | dan    |
| --------------- | ---------------- | --------------- | ------------- | ----------- | ------ |
| tuntutan        | jaringan.  Oleh  | karena          | itu,          | hypervisor  | harus  |
| menunjukkan     | kemampuan        | untuk           | meningkatkan  | kinerjanya  |        |
secara mandiri dan
84154 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
akan menerapkan berbagai algoritma smoothing berbasis
|     |     |     |     |     |     |     | windows  Long  | Short-Term  | Memory  (LSTM)  | hibrida  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --------------- | -------- |
dengan kehilangan data minimum yang diperkenalkan
sebelumnya di [46]. Kemudian, algoritma terbaik akan
|     |     |     |     |     |     |     | digunakan  untuk  | meramalkan  | trafik  jaringan  | untuk  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | ----------------- | ------ |
setiap potongan layanan
GAMBAR 4. Diagram alir untuk DLVisor.
| secara  | transparan  | dengan  | biaya  | tambahan  | minimum.  |     |     |     |     |     |
| ------- | ----------- | ------- | ------ | --------- | --------- | --- | --- | --- | --- | --- |
Manajemen irisan bandwidth adalah salah satu sumber daya
penting yang perlu bekerja dalam skala waktu yang singkat
untuk mencapai efisiensi sumber daya yang tinggi untuk
| sumber  | daya  yang  | tervirtualisasi.  |     | Hal  ini  | dapat  | dicapai  |     |     |     |     |
| ------- | ----------- | ----------------- | --- | --------- | ------ | -------- | --- | --- | --- | --- |
melalui hypervisor berbasis kognitif dan pembelajaran dan
| di  bawah  | berbagai  | tujuan  | dan  | batasan  | pemodelan  |     |     |     |     |     |
| ---------- | --------- | ------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- |
matematika. Hypervisor yang diusulkan untuk ditingkatkan
yang ditunjukkan dalam penelitian ini diberi nama DLVisor
| (Dynamic  | learning  | hypervisor),  |     | di  mana  | Gambar  | 3   |     |     |     |     |
| --------- | --------- | ------------- | --- | --------- | ------- | --- | --- | --- | --- | --- |
menunjukkan komponen manajemen sumber daya vSDN
yang diusulkan dalam DLVisor.
| Untuk          | tujuan       | ini  dan           | seperti  yang  | ditunjukkan  |                 | pada  |     |     |     |     |
| -------------- | ------------ | ------------------ | -------------- | ------------ | --------------- | ----- | --- | --- | --- | --- |
| Gambar         | 3,  Dynamic  | Learning           | Framework      |              | (DLF)           | yang  |     |     |     |     |
| diperkenalkan  |              | dan  didiskusikan  |                | pada         | pekerjaan       | kami  |     |     |     |     |
| sebelumnya     | [46]         | akan  digabungkan  |                | dan          | diintegrasikan  |       |     |     |     |     |
dengan modul manajemen sumber daya EnterpriseVisor di
| hypervisor   | EnterpriseVisor.  |                  | DLF            | akan        | menangkap     |           |     |     |     |     |
| ------------ | ----------------- | ---------------- | -------------- | ----------- | ------------- | --------- | --- | --- | --- | --- |
| potongan     | bandwidth         | jaringan         | kerja          | dari        | server        | Cacti     |     |     |     |     |
| menggunakan  |                   | Simple  Network  |                | Management  |               | Protocol  |     |     |     |     |
| (SNMP).      | Jejak             | langsung         | bisa  diakses  |             | langsung      | dari      |     |     |     |     |
| penyimpanan  | jaringan          | dalam            | mode           | online,     | semi-online,  |           |     |     |     |     |
atau dalam mode batch. Pendekatan pembelajaran dinamis
| VOLUME 11, 2023 |     |     |     |     |     |     |     |     |     | 84155 |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

GAMBAR 5. Komponen-komponen testbed. M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
TABEL 2. Hiperparameter LSTM.
TABEL 3. Deskripsi dataset.
atau penyewa. Pekerjaan ini terutama berfokus pada
virtualisasi vSDN di mana pemotongan ujung ke ujung RAN
berada di luar cakupan makalah ini dan dapat ditemukan di
pekerjaan terkait lainnya seperti di [47]. Tiga tingkat
pemanfaatan akan didefinisikan sebagai pemanfaatan rendah
dalam kisaran 0% hingga β, pemanfaatan menengah adalah β
hingga γ, dan pemanfaatan tinggi antara γ dan 100%. Gambar 4
menunjukkan diagram alir keseluruhan untuk DLVisor.
Bagian putih menunjukkan DLF sedangkan bagian biru tua
menunjukkan alokasi slice dan manajemen bandwidth yang
diperkenalkan oleh EnterpriseVisor sesuai dengan komponen
DLVisor yang ditunjukkan pada Gambar 3.
84156 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 6. Diagram urutan untuk skenario testbed.
GAMBAR 7. Pembuatan irisan ATN-OBY.
jaringan.
Seperti yang digambarkan pada Gambar 4, alur dimulai
dengan membangun model ML yang lebih baik dengan
| memasukkan  | penghalusan  |                | berbasis  | loss-aware            | window  |
| ----------- | ------------ | -------------- | --------- | --------------------- | ------- |
| sebagai     | teknik       | preprocessing  |           | untuk  menghilangkan  |         |
komponen derau jangka pendek/panjang yang tidak perlu
dan menghindari erosi tren dan pola berkala dalam derau
deret dan fluktuasi trafik yang cepat, output dari proses ini
adalah ML berbasis LSTM hibrida yang lebih baik yang
akan digunakan untuk prakiraan trafik. Kemudian, untuk
| mengatasi  | keandalan  | dan  | validitas  | model  | ML  karena  |
| ---------- | ---------- | ---- | ---------- | ------ | ----------- |
karakteristik data yang cepat dan perubahan distribusi yang
| diakibatkan  | oleh  | sifat  | dinamis  | dari  properti  | jaringan,  |
| ------------ | ----- | ------ | -------- | --------------- | ---------- |
kerangka kerja peramalan harus mendeteksi dan beradaptasi
| dengan  | semua  perubahan  |     | dalam  | sifat  statistik  | trafik  |
| ------- | ----------------- | --- | ------ | ----------------- | ------- |
VOLUME 11, 2023 84157

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 8. Pesan log selama pembuatan irisan ATN-OBY.
GAMBAR 9. Skrip yang digunakan untuk memodifikasi batas bandwidth slice
oleh DLVisor.
Perubahan profil lalu lintas, seperti lonjakan lalu lintas yang
tiba-tiba, terjadi karena perubahan atau variasi dalam
84158 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 10. Pemanfaatan irisan dalam Wa = 1.
digunakan.
permintaan perilaku aplikasi. Oleh karena itu, pendeteksi
| perubahan   | menggunakan  | Anderson         | Darling  | (AD)        |
| ----------- | ------------ | ---------------- | -------- | ----------- |
| dimasukkan  | karena       | sensitivitasnya  | untuk    | mendeteksi  |
perubahan karakteristik data, yang dapat berdampak negatif
| pada  akurasi  | model              | ML.  Kemudian    | jika         | perubahan  |
| -------------- | ------------------ | ---------------- | ------------ | ---------- |
| terdeteksi,    | uji  signifikansi  | statistik        | digunakan    | untuk      |
| memvalidasi    | output  dari       | data  yang       | diramalkan.  | Dengan     |
| demikian,      | jika  output       | dari  algoritma  | ML  yang     | saat  ini  |
digunakan tidak signifikan, maka model saat ini (lama) akan
dipertahankan, jika tidak, model hibrida ML yang baru akan
VOLUME 11, 2023 84159

model  yang  dibangun  asalkan  hasilnya  signifikan.  RinciaMn.  K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
prosesnya telah dibahas dalam penelitian kami sebelumnya di
| [46].  Karena  | keandalan  dan  | kesederhanaannya,  | pemilihan  |
| -------------- | --------------- | ------------------ | ---------- |
hyperparameter dilakukan melalui pencarian grid, seperti yang
digambarkan pada Tabel 2 [46]. Akhirnya, bandwidth yang
diperkirakan digunakan sebagai input untuk alokasi slice untuk
mengidentifikasi penyedia sumber daya dan peminta sumber
| daya  menggunakan  | klasifikasi       | slice  ke  dalam  | slice  dengan  |
| ------------------ | ----------------- | ----------------- | -------------- |
| pemanfaatan        | rendah,  sedang,  | dan  tinggi,      | dan  kemudian  |
memasok dan
84160 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
TABEL 4. Daftar simbol.

GAMBAR 11. Jumlah pemanfaatan berlebihan dalam Wa = 1. deret waktu. Tabel 3 menunjukkan nama-nama set data.
Perhitungan permintaan dilakukan untuk mengalokasikan
irisan vSDN secara proaktif guna menghindari penggunaan
| berlebihan  | untuk  meminimalkan  | dan  | menghilangkan  |     |
| ----------- | -------------------- | ---- | -------------- | --- |
kemacetan dan kelaparan sumber daya.
A. DATASET
Dataset dikumpulkan dari Penyedia Layanan Internet (ISP)
utama di mana rangkaian waktu pemanfaatan bandwidth
yang berbeda diperiksa. Data yang dikumpulkan mewakili
lalu lintas backbone gabungan untuk Long Term Evolution
| (LTE),    | MPLS,  dan  enodeB.     | Data  diambil    | sampelnya  |        |
| --------- | ----------------------- | ---------------- | ---------- | ------ |
| sebanyak  | 50  dan  350  langkah.  | Setiap  langkah  |            | waktu  |
mewakili 28,8 menit, di mana setiap 50 langkah waktu
mewakili satu hari, dan 350 langkah waktu mewakili satu
| minggu.      | Hal  ini  disebabkan  | oleh  keterbatasan  |     | alat      |
| ------------ | --------------------- | ------------------- | --- | --------- |
| pengumpulan  | data,  sementara      | nilai-nilai         |     | tersebut  |
diinterpolasi dan digunakan untuk mengembangkan model
VOLUME 11, 2023 84161

B. PENGELOLAAN SLICE DALAM vSDN M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
Tabel 4 menunjukkan daftar simbol yang akan digunakan pada
bagian berikut
Algoritma 1 menunjukkan alokasi peminta dan penyedia
Bandwidth Slice. Kompleksitas Algoritma 1 adalah O(nmh
+ m).
Jaringan vSDN dimodelkan sebagai sekumpulan entitas (node
dan sisi) yang saling terhubung oleh satu set tautan. Dalam
| penelitian ini, sebuah jaringan dimodelkan sebagai graf G(ν |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
SDN
| , ε SDN  ) yang terdiri dari ν |     |     | SDN  node jaringan (yaitu sakelar SDN)  |     |     |     |
| ------------------------------ | --- | --- | --------------------------------------- | --- | --- | --- |
| yang terhubung dengan ε        |     |     |  edge. Hypervisor SDN diberikan         |     |     |     |
SDN
| oleh himpunan H    |     |  , di mana H |     |  adalah subset dari ν |     |  .  |
| ------------------ | --- | ------------ | --- | --------------------- | --- | --- |
|                    |     | SDN          |     | SDN                   |     | SDN |
| Permintaan vSDN, r |     |              |  ,  |                       |     |     |
SDN
| di mana r |  ∈ R |  (R |  adalah set dari total permintaan),  |     |     |     |
| --------- | ---- | --- | ------------------------------------ | --- | --- | --- |
|           | SDN  | SDN | SDN                                  |     |     |     |
dibuat di antara sakelar SDN di Vr (Set
| node  dari    | permintaan  |           | vSDN)       | dan  pengontrol  | cr                | (Virtual  |
| ------------- | ----------- | --------- | ----------- | ---------------- | ----------------- | --------- |
| Controller    | node        | dari      | permintaan  | vSDN             | r  )  di  lokasi  | yang      |
| disumbangkan  |             | oleh  cr  | ∈           | ν   .  Tujuan    | terakhir          | adalah    |
SDN
memetakan controller cr ke
sakelar host fisik yang sesuai, yang diwakili oleh
84162 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 12. Pemanfaatan irisan dalam Wa = 2.
∀r
SDN
∈ R
SDN
, ∀νr ∈ Vr ∪ cr → ν
SDN
. Penyediaan irisan Algoritma dimulai dengan meramalkan bandwˆidth y
t
melalui jaringan virtual dan fisik berada di luar cakupan sebagai deret waktu dari langkah waktu t dalam slice SL
i i
dari makalah ini. Algoritma 1 menunjukkan klasifikasi milik jendela W . Slices kemudian dialokasikan
a
peminta dan penyedia sumber daya. Algoritma ini mencari berdasarkan utilisasi yang dihitung dalam u (baris 5 sampai
i
di setiap ˆlangkah waktu t ∈ y dˆi SL ∈ W , di mana y adalah 13 dari Algoritma 1) ke kandidat pemohon. Jika utilisasi
j i a
bandwidth yang diperkirakan lebih tinggi dari batas atas γ dan ke kandidat penyedia
untuk penyedia sumber daya dan peminta sumber daya lainnya, jika utilisasi lebih rendah dari batas bawah β, daftar
dalam bentuk irisan
kandidat penyedia dan peminta disimpan dalam daftar
SL berjalan pada satu set ν yang sudah disediakan di
i SDN peminta irisan
jendela W .
a
VOLUME 11, 2023 84163

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
|     | Algoritma  | 1   | Alokasi  | Peminta  |     | dan  Penyedia  |     | Irisan  |
| --- | ---------- | --- | -------- | -------- | --- | -------------- | --- | ------- |
Bandwidth
Masukan SL : iˆrisan, y : perkiraan bandwidth dalam
|     |     |     | i   |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
irisan SL , δ:
i
|     | LSTM                       | yang  | dihaluskan  |                                    | secara  | statistik    | signifikan,  |      |
| --- | -------------------------- | ----- | ----------- | ---------------------------------- | ------- | ------------ | ------------ | ---- |
|     | infrastruktur jaringan G(ν |       |             |                                    |  , ε    |  ), dengan r |              |  di  |
|     |                            |       |             |                                    | SDN     | SDN          |              | SDN  |
|     | mana r                     |  ∈ R  |             |  dan terhubung ke pengontrol cr ,  |         |              |              |      |
SDN SDN
|     | diberikan ∀r        |     |  ∈ R |  , ∀Vr ∈ νr ∪ cr → ν |     |     |     |  , i:  |
| --- | ------------------- | --- | ---- | -------------------- | --- | --- | --- | ------ |
|     |                     |     | SDN  | SDN                  |     |     |     | SDN    |
|     | indeks, j: indeks W |     |      |  :                   |     |     |     |        |
tot
jumlah total irisan, t: waktu, a: langkah indeks, β :
Batas bawah, γ : Batas atas, h : jumlah penyedia sumber
daya, g : jumlah pemohon sumber daya
i: indeks, z: Hitung jumlah penggunaan berlebih 100%
|     | untuk y di SL ϵW |     |       |  ϵW |     |     |     |     |
| --- | ---------------- | --- | ----- | --- | --- | --- | --- | --- |
|     |                  | t   | i tot | a   |     |     |     |     |
Keluaran:
|     | ˆR {..} | :   | Calon Pemohon |     |     | daftar |     | ,ˆP  |
| --- | ------- | --- | ------------- | --- | --- | ------ | --- | ---- |
|     | {..}    | :   |               |     |     |        |     |      |
Daftar calon penyedia, X: Hitung jumlah 100%
 ϵp^ m (i) ˆϵW
|     | overutilisasi untuˆk y |     |     | t  di SL | i   | a   |  ϵP {..} |     |
| --- | ---------------------- | --- | --- | -------- | --- | --- | -------- | --- |
01: mulai
02: ˆR {..} :← ∅;
03: ˆP{..} ←
04: untuk semua langkah waktu dalam irisan
∅;
|     | bandwidth yang diperkirakan t ϵy di SL ϵW |     |     |     |     |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |                                           |     |     |     | j   | t i | tot |     |
 do /ˆ/ menggunakan δ
ϵW
a
05: u ← Hitung pemanfaatan irisan
i
06 sementara g =! 0
07 jika u ≥ γ
i
|     | 08  | ˆ R {..} ←: SL //kandidat pemohon 09 |     |     |     |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
i
Lain-lain
10 sementara h =! 0
11 Jika u ≤ β
i
|     | 12  | {ˆP} ←: SL //kandidat penyedia |     | i   |     |     |     |     |
| --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
13 Lain
14Hitung penawaran dan permintaan menggunakan
algoritme 2
 di p^
|     | 15untuk SL |                                    |     | m (i) di ˆW |  ϵP {..}   |     |     |     |
| --- | ---------- | ---------------------------------- | --- | ----------- | ---------- | --- | --- | --- |
|     |            |                                    | i   |             | a          |     |     |     |
|     | 16         | X ← Hitung irisan atas pemanfaatan |     |             |            |     |     |     |
|     | 17         | Jika X ≥ z                         |     |             |            |     |     |     |
|     | 18-        | Jatuhkan SL                        |     |  ϵp^        | m (i) di W | ˆ   |     |     |
|     |            |                                    |     | i           |            | a   |     |     |
dari P{..} 19 Perulangan:

GAMBAR 13. Jumlah pemanfaatan berlebihan dalam Wa = 2. Pada baris 8, jumlah sumber daya yang dipasok p^ m (i) dari
sekumpulan irisan pasokan P..{} dihitung dan dibatasi oleh
ˆ
batasan pada Persamaan 2-5. Selain itu, pemanfaatan irisan
ˆR {..} dan irisan daftar penyedˆia P {..}, dan kedua ˆdaftar R
setelah sumber daya
ˆ {..  dan  P  {..}  akan  diteruskan  ke  Algoritma  2  untuk  donasi harus berada di antara batas bawah β dan batas atas γ
mendapatkan jumlah sumber daya yang akan menyediakan
. Jumlah sumber daya yang disediakan yang diminta oleh
p^
m (i) dan ˆjumlah sumber daya yang diminta r(i). Kemudian  pemohon dan disediakan oleh penyedia m slice dihitung
untuk semua irisan penyedia di jenˆdela W  dalam daftar  oleh fungsi biaya, C, dengan syarat semua kendala dalam
a
penyedia yang diperkirakan P {..}, overutilisasi X Persamaan 2 sampai 5 terpenuhi.
apderaklairha anjumlah  hitungan  dari  100%  overutilisasi  untuk  X
n
bandwidth (ˆy ), jika X ≥ z, di mana z adalah jumlah hitungan  min(C) =  w x (1)
100%
| t   | mengg |     | ban |     | a   | u   |     | y  ,  |
| --- | ----- | --- | --- | --- | --- | --- | --- | ----- |
t
overutilisasi  untuk  semua  irisan  SL   di  jendela  W   unaka dwi k a p^ m
i a
|     | n   |     | dth  |     | t   | l   |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
ˆ84164 VOLUME 11, 2023

( i)   a k a n   d i k e l u a r k a n   d a r i   d a f t a r   p e n y e d ia   P   u n t u k   m  m
M .  K .  H as sa n  d k k .:  D L V is o r:  H yp e rv i s or  P e m b e l aj ar a n  Di n am is  u nt uk {   . J . a } r   in ga n  y a ng   m=1
mDiteenntgukhainn Pdeararnig kkaet lLaupnaakran bandwidth.
Kendala:
Algoritma 2 menunjukkan perhitungan penawaran dan
| permintaan di mana |     |     |     |     | Xn  |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
x
m ≤ p (2)
m=1 t
Kompleksitas Algoritma 2 adalah O(nmh). Pada baris 4,  p^ m (i) ≤ A  (t) - S  (3)
|                      |                         |                     |                              |     |                 | i     | i             |
| -------------------- | ----------------------- | ------------------- | ---------------------------- | --- | --------------- | ----- | ------------- |
| p ermintaan          |                         |                     |                              |     |                 | X     |               |
| ˆ                    |                         |                     | ˆ                            |     |                 |       |               |
|                      |                         |                     |                              |     | X               |       | n             |
| r (i )   d i h i t u | n g  d a r i  s e k u m | p u l a n   p em in | t a   ir is a n R {..} yang  |     | n  i            |       |               |
|                      |                         |                     |                              |     | min  p^ m (i) ≤ |  ≤  ≤ | Max  p^ m (i) |
te r b a t a s   p a d a  n i l a i  a n ta ra   b a t a s  b aw a h   β  d a n =  1 i=1
x
m
batas atas γ , dan yang paling penting, dibatasi oleh Max(r ). x  , x  , . . . . .., x  ≥ 0 (4)
|     |     |     |     | t   |     | 1 1 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- |
VOLUME 11, 2023 84165

IEEE7tccess
M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang Ditentukan
Perangkat Lunak
|     | Sumber daya yang disediakan |     |     |     | Sumber daya yang disediakan |     |      |
| --- | --------------------------- | --- | --- | --- | --------------------------- | --- | ---- |
| 600 |                             |     |     | 300 |                             |     |      |
|     |                             |     |     |     |                             | -   | Asli |
—-I- - tanpa DLF.
+
| 500 |     |     |     |     |     | —6 - dengan DLF. |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- |
|     |     | \   |     | 250 |     |                  |     |
200
0
| 300 |     |     |     | 150 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
IOO
200
100
s
0
100 105 110 115 120 125 130 135 140 145 150 100 105 110 115 120 125 130 135 140 145 150
|                          | Langkah-langkah waktu (menit) |                             |     |     | Langkah waktu (menit) |     |     |
| ------------------------ | ----------------------------- | --------------------------- | --- | --- | --------------------- | --- | --- |
|                          | (a) ATN-OBY                   |                             |     |     | (b) ATN-PSD           |     |     |
| Sumber Daya yang Diminta |                               | Sumber daya yang disediakan |     |     |                       |     |     |
100
90
|     |     |     |       | g0  |     | —-I- - tanpa DLF. |     |
| --- | --- | --- | ----- | --- | --- | ----------------- | --- |
|     |     |     | Asli. |     |     | —6 - dengan DLF.  |     |
—-I- - tanpa DLF.
|     |     | —6 - dengan DLF. |     | gp  |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- |
| 70- |     | g                |     | 70  |     |     |     |
60-
6'
- 50
-
z
40-
30-
| 20      | ' ' "                         | ' ' '           | ' ' |         |                               |                 |         |
| ------- | ----------------------------- | --------------- | --- | ------- | ----------------------------- | --------------- | ------- |
| 100 105 | 110 115 120 125               | 130 135 140 145 | 150 |         |                               |                 |         |
|         |                               |                 |     | 100 105 | 110 115 120                   | 125 130 135 140 | 145 150 |
|         | Langkah-langkah waktu (menit) |                 |     |         | Langkah-langkah waktu (menit) |                 |         |
|         | (c)                           | LTE             |     |         |                               |                 |         |
|         |                               |                 |     |         | (d)                           | MPLS            |         |
GAMBAR 14. Pemanfaatan irisan dalam Wa = 3.
| 84156 |     |     |     |     |     |     | VOLUME 11, 2023 |
| ----- | --- | --- | --- | --- | --- | --- | --------------- |

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
|     |     |     |     |     |     |     |     | Algoritma  |     | 2  Perhitungan  | Sumber  | Daya  | Pasokan  | dan  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | ------- | ----- | -------- | ---- |
Permintaan
Masukanˆ: R {..} : Daftar kandidat pemohon, P {..} :
|     |     |     |     |     |     |     |     |     | Daftar kandidat penyedia, SL : slice , y |     |     |     |     | ˆ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |                                          |     |     | i   |     | :   |
perkiraan bandwidth pada slice SL , i : indeks,
i
|     |     |     |     |     |     |     |     |     | z:  thHitungan         | jumlah  | overutilisasi                     |     | 100%  | dalam  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | ------- | --------------------------------- | --- | ----- | ------ |
|     |     |     |     |     |     |     |     |     | menggunakan y di SL ϵp |         |  (i), β : batas bawah, γ : batas  |     |       |        |
|     |     |     |     |     |     |     |     |     |                        | t i     | m                                 |     |       |        |
atas, A : alokasi Bandwidth maksimum untuk irisan ke- i
i,   r : total kebutuhan, Sˆ :
|     |     |     |     |     |     |     |     |     | t   |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Jaminan Bandwidth Minimum untuk ith Slice, hal :ˆ
t
Total sumber daya dari semua penyedia sumber daya
|     |     |     |     |     |     |     |     |     | Keluaran: C: Fungsi biaya, p^ |     |     | m (i): jumlah sumber daya  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | -------------------------- | --- | --- |
yang disedˆiakan, r(i): jumlah sumber daya yang diminta
01: mulai
02: untuk semua langkah waktu dalam irisan
|     |     |     |     |     |     |     |     |     | bandwidˆth yang diperkirakan t ϵy in SL ϵW |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |                                            |     |     | j t | i   | a   |
do
03 untuk SL di ˆR {..} do
i
|     |     |     |     |     |     |     |     |     | 04: selesˆaikan r(i)  |     | t   |  ˆ y |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ---- | --- | --- |
≤  γ , Asalkan ˆr
|     |     |     |     |     |     |     |     |     |      |       | Ai  +   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | dala | m β ≤ | rˆ(i)   |     |     |     |
P
g
|     |     |     |     |     |     |     |     |     | =                        | ˆr               |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | ---------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |                          | i=1  i           |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 05:                      | Jikˆa R {..} ≠ ∅ |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 06:                      | Lingkaran        |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 07:                      | Lain             |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 08: untuk SL di ˆP{..}do | i                |     |     |     |     |
ˆyt
|     |     |     |     |     |     |     | 09: |     | Memecahkan | p^ m (i) dalam (β |     |     |     | γ , |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | --- | --- | --- |
≤
Ai-p^m (i)
P h
≤
ˆ
|     |     |     |     |     |     |     |     | Di mana |     | p^ m (i) ≤ A |  - S |  dan asalkan p |      | p^ m (i) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- | -------------- | ---- | -------- |
|     |     |     |     |     |     |     |     |         |     |              | i i  |                | t  = |          |
i=1
|     |     |     |     |     |     |     |     |     | 10: | Jiˆka p {..} ≠ ∅ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | 11: | Lingkaran        |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 12: | Lain-lain        |     |     |     |     |
13: Selesaikan min C // Persamaan 1
14: Lingkaran
komponen test bed.
|     |     |     |     |     |     |     |     |     | Gambar  | 6  menunjukkan  |     | diagram  | urutan  | untuk  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | -------- | ------- | ------ |
skenario uji coba, termasuk interaksi antara DLVisor,
jaringan vSDN, dan Libera.
GAMBAR 15. Jumlah pemanfaatan berlebihan dalam Wa = 3.
X n
|     |     | min (rt) ≤ |     |  xm ≤ Max (rt) |     |     | (5) |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m=1
| Fungsi  biaya    | dan    | batasan   | diadopsi  | dari             | kerangka  |     | kerja   |     |     |     |     |     |     |     |
| ---------------- | ------ | --------- | --------- | ---------------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| EnterpriceVisor  | [35].  | Keluaran  |           | dari  Algoritma  |           | 2   | adalah  |     |     |     |     |     |     |     |
jumlah sumber daya yang disediakan p^
m (i) dan jumlah
yangˆ
| sumber  daya  |     | diminta  | r(i)  | yang  | digunakan  |     | oleh  |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ----- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Algoritma 2 untuk alokasi slice.
| Pekerjaan  | ini  | didasarkan  |     | pada  | perluasan  |     | modul  |     |     |     |     |     |     |     |
| ---------- | ---- | ----------- | --- | ----- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
manajemen sumber daya yang tertanam dalam kerangka
kerja EnterpriseVisor. Selain itu, makalah ini mengadopsi
| topologi  yang  | sama       | dengan    | yang        | digunakan  |         | pada         | [35]  |     |     |     |     |     |     |       |
| --------------- | ---------- | --------- | ----------- | ---------- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | ----- |
| Selain  itu,    | test  bed  | dengan    | hypervisor  |            | Libera  | digunakan    |       |     |     |     |     |     |     |       |
| sebagai         | platform   | emulasi.  | Gambar      |            | 5       | menunjukkan  |       |     |     |     |     |     |     |       |
| VOLUME 11, 2023 |            |           |             |            |         |              |       |     |     |     |     |     |     | 84157 |

Testbed  terdiri  dari  lima  entitas  fungsional  yanMg.  K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
direpresentasikan oleh tiga VM yang berada dalam satu host,
| rincian  mesin  | virtual  ditunjukkan  | pada  Tabel  | 5.  Platform  |
| --------------- | --------------------- | ------------ | ------------- |
testbed adalah komputer dengan CPU Core i7 2.1 GHZ, RAM
32 GB, antarmuka jaringan 1GB, sistem operasi windows 10
64-bit untuk mesin host dan dengan ubuntu Linux untuk VM
tamu yang divirtualisasi. Tabel 5 menunjukkan IP VM yang
diuji coba
Seperti yang digambarkan pada Gambar 6, Virtual Network
| Manager  | (VNM)  pada  awalnya  | membuat  | jaringan  fisik  |
| -------- | --------------------- | -------- | ---------------- |
menggunakan simulator MININET- SDN. Kemudian, jaringan
| fisik  ditemukan  | dan  dimulai  | oleh  hypervisor  | Libera.  |
| ----------------- | ------------- | ----------------- | -------- |
Pengontrol VN yang merupakan ONOS dalam kasus kami
akan diaktifkan dalam penggunaan ONOS VM. Segera setelah
jaringan fisik diaktifkan, Libera membuat beberapa jaringan
vSDN sambil mempertahankan isolasi jaringan. Libera dipilih
| sebagai  platform  | emulasi             | karena  fleksibilitasnya  | dalam        |
| ------------------ | ------------------- | ------------------------- | ------------ |
| menciptakan        | VN  dan  kemudahan  | penggunaan                | fitur-fitur  |
| pemrogramannya.    | Setiap  VNM         | penyewa  bertindak        | sebagai      |
operator VN dan mengajukan berbagai permintaan ke Libera.
| Perlu  disebutkan  | bahwa,  kerangka  | kerja  | yang  diusulkan  |
| ------------------ | ----------------- | ------ | ---------------- |
berinteraksi secara horizontal dengan lalu lintas oleh karena itu
tidak mengganggu arus lalu lintas / jalur lalu lintas secara
vertikal antara pengontrol dan vSwitches (Gbr. 5), oleh karena
itu ia memiliki
84158 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 16. Pemanfaatan irisan dalam Wa = 4.
Latensi FlowVisor yang sama yaitu 17ms ketika aliran baru Permintaan diklasifikasikan ke dalam dua kategori:
OpenFlow diproses dan meningkatkan latensi respons status penyediaan topologi dan modifikasi topologi. Pertama,
port sekitar 0,71ms ketika status port OpenFlow diminta VNM mulai membuat VN dengan topologi dan entitas VN
mirip dengan latensi EnterpriseVisor [35]. yang ditentukan. Istilah ''entitas virtual'' mengacu pada
semua entitas yang terdiri dari
84158 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
TABEL 5. Alamat IP testbed.
|     |     |     |     |     |     | memodifikasi  |     | irisan  | seperti  | yang  | digambarkan  |     | pada  |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----- | ------------ | --- | ----- |
Gambar 6, langkah 6. Gambar 7 menunjukkan keluaran dari
pembuatan irisan satu.
|     |     |     |     |     |     | Empat  | VN  | dibuat  | di  Libera.  |     | Gambar  | 7   | dan  8  |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ------------ | --- | ------- | --- | ------- |
menunjukkan keluaran dari pembuatan irisan satu. Gambar
7 menunjukkan pembuatan irisan satu, yang mewakili irisan
ATN-OBY yang disebut sebagai penyewa
_id 1; irisan dipetakan ke sakelar fisik dengan ID sakelar,
port, dan tautan yang sesuai. Selain itu, slice juga terkait
dengan ONOS Controller yang sesuai di 10.0.0.3 melalui
port 1000: TCP. Gambar 8 menunjukkan pesan log yang
|     |     |     |     |     |     | lebih  rinci,  | termasuk        |     | pembentukan  |       | sakelar    | dan  | tautan.  |
| --- | --- | --- | --- | --- | --- | -------------- | --------------- | --- | ------------ | ----- | ---------- | ---- | -------- |
|     |     |     |     |     |     | Gambar         | 9  menunjukkan  |     | skrip        | yang  | digunakan  |      | untuk    |
memodifikasi batas bandwidth slice pada langkah nomor 6
pada Gambar 6 dan sebagai hasil dari algoritme 1 dan 2.
Gambar 8 menunjukkan pesan log yang terperinci selama
pembuatan slice ATN-OBY yang menunjukkan skrip yang
digunakan untuk mengontrol disiplin antrian trafik (secara
default, First in First Out FIFO). Ini didasarkan pada perintah
kontrol lalu lintas di Linux yang memungkinkan konfigurasi
penjadwalan paket untuk mendukung qdisc. Di sisi lain,
argumen tbf menunjukkan bahwa mekanisme token bucket
filter mengontrol arus lalu lintas. Disebutkan di sini bahwa
kecepatan dibatasi hingga 90Mbps. Alat IPERF digunakan
|     |     |     |     |     |     | sebagai  | generator  | beban  | untuk  | menekankan  |     | bandwidth  |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ------ | ------ | ----------- | --- | ---------- | --- |
irisan VN
VN, pesan kontrol setiap VN dialihkan secara terpisah
|     |     |     |     |     |     | ke  | Libera.  | Untuk  | Flow  | rules  | (FR),  | VNC  | dapat  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ------ | ------ | ---- | ------ |
menginstal FR yang diinginkan ke vSwitch mana pun
|     |     |     |     |     |     | kapan       | pun,  | sehingga  | memungkinkan  |         |           | paket      | untuk    |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | ------------- | ------- | --------- | ---------- | -------- |
|     |     |     |     |     |     | diteruskan  |       | atau      | dibuang       | secara  | dinamis.  |            | Sebagai  |
|     |     |     |     |     |     | tambahan,   |       | Libera    | mengumpulkan  |         | data      | statistik  | dari     |
vSwitch dan port virtual. Dengan demikian, DLVisor
dapat mengkonfigurasi ulang atau
GAMBAR 17. Jumlah pemanfaatan berlebihan dalam Wa = 4.
| VN,  seperti  | vSwitch,  | port,  | dan  | tautan.  Sebagai  | contoh,  |     |     |     |     |     |     |     |     |
| ------------- | --------- | ------ | ---- | ----------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
VNM dapat menentukan apakah vSwitch adalah OpenFlow,
| kotak  putih,  | atau  | P4.  Selain  | itu,  | VNM  dapat  | membuat  |     |     |     |     |     |     |     |     |
| -------------- | ----- | ------------ | ----- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
beberapa port pada setiap sakelar virtual. Demikian pula,
tautan virtual dapat dibangun dengan menghubungkan dua
port virtual.
| Pada     | Gambar     | 6,  setelah  | VNM      | membuat         | VN  dan  |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | -------- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network  | Interface  | (NI)         | virtual  | yang  terkait,  | penyewa  |     |     |     |     |     |     |     |     |
mengoperasikan VN melalui pengontrol VN (VNC). VNC
| dapat  mengonfigurasi  |     | vSwitch  | atau  | port  virtual  | dengan  |     |     |     |     |     |     |     |     |
| ---------------------- | --- | -------- | ----- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
mengirimkan pesan perintah ke Libera melalui I2 (saluran
kontrol). Libera menawarkan saluran kontrol untuk setiap
sakelar virtual. Karena vSwitch hanya dimiliki oleh satu
| VOLUME 11, 2023 |     |     |     |     |     |     |     |     |     |     |     |     | 84159 |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V. HASIL DAN PEMBAHASAN
M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Dalam  penelitian  ini,  algoritma  alokasi  sumber  daya  yanDgit entukan Perangkat Lunak
diusulkan hanya dapat melayani satu pemohon sumber daya
dalam satu waktu max(g) = 1, dan jumlah maksimum penyedia
sumber daya adalah empat max(h) =
4. Oleh karena itu, prioritas diberikan kepada pemohon irisan.
Prioritas ditetapkan untuk LTE, ATN-OBY, ATN-PSD, dan
MPLS secara berurutan. Untuk menciptakan sumber daya yang
terbatas pada bandwidth jaringan, jumlah maksimum total
sumber daya yang diminta dan yang disediakan dipilih sama
| dengan (r ) = (p | t t   ). Batasan bandwidth maksimum untuk  |     |     |     |
| ---------------- | ------------------------------------------ | --- | --- | --- |
irisan adalah 90 Mbps untuk ATN-OBY dan ATN-PSD, 1,43
Gbps
untuk potongan MPLS dan 1,5 Gbps untuk potongan LTE.
Kapasitas jaringan maksimum M adalah 3,2 Gbps dan tingkat
| pemanfaatan  | target,  batas  | pemanfaatan  | bawah,  | dan  batas  |
| ------------ | --------------- | ------------ | ------- | ----------- |
pemanfaatan atas adalah
| yang dipilih menjadi ideal (u |     |  ) = 50%, β = 40% dan γ =  |     |     |
| ----------------------------- | --- | -------------------------- | --- | --- |
x
60%.
Nilai-nilai ini ditentukan secara empiris berdasarkan irisan
kumpulan data yang dipilih untuk menciptakan situasi di mana
penyedia sumber daya dapat mengalami kelaparan sumber daya
sambil menyediakan
| kelebihan sumber daya mereka pada saat ini (t ) dan sampai  |                                                |     | j   |     |
| ----------------------------------------------------------- | ---------------------------------------------- | --- | --- | --- |
| dengan (t                                                   |  ) di mana n adalah jumlah langkah waktu yang  |     |     |     |
j+n
diperkirakan.
| Gambar  | 10  menunjukkan  | pemanfaatan  | irisan  | ATN-OBY,  |
| ------- | ---------------- | ------------ | ------- | --------- |
ATN-PSD, LTE, dan MPLS, dengan dan tanpa alokasi sumber
| daya  menggunakan  | kerangka  | kerja  | pembelajaran  | dinamis  |
| ------------------ | --------- | ------ | ------------- | -------- |
(DLF) untuk
semua langkah waktu di jendela 1 dengan syarat t ϵy di SL  ˆ
j t i
ϵW  (a = 1 dan j = 1 hingga 50, yaitu 50 langkah waktu
a
| pertama);  | di  mana  garis  | biru  | pada  grafik  menunjukkan  |     |
| ---------- | ---------------- | ----- | -------------------------- | --- |
pemanfaatan irisan aktual (asli)
84160 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 18. Pemanfaatan irisan dalam Wa = 5.
tanpa menggunakan algoritma alokasi sumber daya yang slice lain yang diminta seperti LTE, karena pemanfaatan
digunakan sebagai tolok ukur dalam penelitian ini. Pada slice LTE lebih dari batas atas u ≥ γ , di mana γ = 60% dan
i
window satu dan berdasarkan pemanfaatan slice, slice pemanfaatan slice lainnya kurang dari batas bawah u ≤ β
i
ATN-OBY, slice ATN-PSD, dan slice MPLS dianggap di mana β = 40% pada pemanfaatan target (u ) = 50%;
x
sebagai penyedia sumber daya karena asalkan semua batas dan batasan terpenuhi dalam
Persamaan 1 hingga 5. The
pemanfaatan yang rendah u ≤ β, sedangkan slice LTE
i
Garis oranye menggambarkan pemanfaatan baru tanpa DLF.
dianggap sebagai peminta sumber daya u ≥ γ .
i
Gambar 10a menunjukkan bahwa pemanfaatan irisan
Pada langkah waktu 1 dan Menurut algoritme 1 dan 2, ATN-
tanpa DLF melebihi pemanfaatan penuh 100%, yang
Irisan OBY, ATN-PSD, dan MPLS akan menyediakan sumber daya
untuk menyebabkan irisan tersebut kelaparan
VOLUME 11, 2023 84161

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
penyedia sumber daya P{..}. Garis kuning menunjukkan
bahwa penggunaan slice dijaga agar tetap sama dengan
penggunaan slice yang asli
|     |     |     |     | karena  irisan  | tidak  dianggap  | sebagai  penyedia  | irisan  |
| --- | --- | --- | --- | --------------- | ---------------- | ------------------ | ------- |
setelah menggunakan
GAMBAR 19. Jumlah pemanfaatan berlebihan dalam Wa = 5.
| untuk  sumber  | daya  | karena  ketidakmampuan  | untuk  |     |     |     |     |
| -------------- | ----- | ----------------------- | ------ | --- | --- | --- | --- |
memulihkan sumber daya yang disediakan (disumbangkan)
| karena  penggunaan  | irisan  | lainnya.  Hal  | ini  terutama  |     |     |     |     |
| ------------------- | ------- | -------------- | -------------- | --- | --- | --- | --- |
disebabkan oleh penerapan algoritma alokasi sumber daya
dalam benchmark (EnterpriseVisor) secara real-time tanpa
| mempertimbangkan  | kebutuhan  | di  masa  | depan.  Dari  sisi  |     |     |     |     |
| ----------------- | ---------- | --------- | ------------------- | --- | --- | --- | --- |
lain, dalam penelitian kami
alokasi sumber daya penawaran dan permintaan algoritma
yang diusulkan, perhitungan didasarkan pada perkiraan
sumber daya di masa depan
konsumsi (disorot dalam garis kuning). Oleh karena itu, ada
| pengetahuan  | sebelumnya  | tentang  apakah  | akan  terjadi  |     |     |     |     |
| ------------ | ----------- | ---------------- | -------------- | --- | --- | --- | --- |
kelaparan sumber daya atau tidak sebelum memutuskan
| untuk  tidak  | mempertimbangkan  | (mencoret)  | penyedia  |     |     |     |     |
| ------------- | ----------------- | ----------- | --------- | --- | --- | --- | --- |
sumber daya (donoˆr) dari pertimbangan sebagai kandidat
| 84162 |     |     |     |     |     | VOLUME 11, 2023 |     |
| ----- | --- | --- | --- | --- | --- | --------------- | --- |

|     |     |     |     |     |     |     |     | alokasi  dengan  | DLF.  Peningkatan  | tajam  pada  | hasil  ini  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------ | ------------ | ----------- |
DLFM y. aKn. Hga sksaanm dki ku.: sDuLVlkisaorn: .H yApenravilsiosri Pse myabnelgaj asraanm Dain admitise urnatpukk aJanri npgaand yaa ng
adalah untuk mengkompensasi jumlah sumber daya yang
potonDgiteanntu kAanT PNer-a nPgkSaDt L upnaakda Gambar 10b. Sementara itu, pada
pada awalnya disediakan oleh slice yang diturunkan (slice
slice MPLS, pemanfaatan dalam alokasi sumber daya dengan
ATN-OBY dan slice ATN-PSD). Gambar 13a dan Gambar
DLF meningkat karena sumber daya tambahan yang diberikan
13b menunjukkan hitungan berapa kali pemanfaatan slice
| kepada  | pemohon  | untuk  | mengkompensasi  |     | sumber  | daya  | yang  |     |     |     |     |
| ------- | -------- | ------ | --------------- | --- | ------- | ----- | ----- | --- | --- | --- | --- |
melebihi pemanfaatan 100% untuk slice ATN-OBY dan
hilang dari slice ATN-OBY dan ATN-PSD yang dijatuhkan.
slice ATN-PSD.
Gambar 11 menunjukkan hitungan berapa kali pemanfaatan
slice melebihi pemanfaatan 100% untuk ATN-OBY (a) dan
ANT-PSD pada (b).
| Pada        | Gambar  | 11a,  | irisan  | ATN-OBY  | digunakan     |     | secara  |     |     |     |     |
| ----------- | ------- | ----- | ------- | -------- | ------------- | --- | ------- | --- | --- | --- | --- |
| berlebihan  | 27      | kali  | lebih   | banyak   | dibandingkan  |     | saat    |     |     |     |     |
menggunakan yang asli (tanpa alokasi sumber daya) dan saat
| menggunakan  |         | DLF  kami,   | yang    | mengonfirmasi  |              | keefektifan  |     |     |     |     |     |
| ------------ | ------- | ------------ | ------- | -------------- | ------------ | ------------ | --- | --- | --- | --- | --- |
| algoritme    | yang    | diusulkan.   | Namun,  |                | pada  slice  | ATN-PSD,     |     |     |     |     |     |
| alokasi      | sumber  | daya  tanpa  | DLF     | menyebabkan    |              | penggunaan   |     |     |     |     |     |
yang berlebihan 30 kali lebih banyak daripada DLF. Gambar
12 menunjukkan pemanfaatan irisan
ˆ
| tion untuk jendela 2 untuk semua t ϵy di SL ϵW |     |     |     | j   | t   | i a  (a = 2 dan j  |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
=
51 hingga 100). Demikian juga, grafik menunjukkan data aktual
(asli).
nal) pemanfaatan slice tanpa menggunakan algoritma alokasi
sumber daya dan tanpa DLF.
Pada jendela 2, ATN-OBY pada langkah waktu 51 dan 53
merupakan penyedia sumber daya ketika alokasi tanpa DLF
| digunakan.  | Hal  | ini  disebabkan  |     | oleh  | pemanfaatannya  |     | yang  |     |     |     |     |
| ----------- | ---- | ---------------- | --- | ----- | --------------- | --- | ----- | --- | --- | --- | --- |
rendah, β < 40% (kotak biru). Namun demikian, pada langkah
56, slice meminta sumber daya karena pemanfaatannya lebih
tinggi dari batas atas, γ > 60%. Selain itu, slice ATN-OBY
| adalah  | peminta  | sumber  | daya  | pada  | langkah  | waktu  | 66  |     |     |     |     |
| ------- | -------- | ------- | ----- | ----- | -------- | ------ | --- | --- | --- | --- | --- |
menggunakan alokasi sumber daya dengan DLF. Di sisi lain,
potongan ATN-PSD pada langkah waktu 53 dan 56 masing-
masing merupakan penyedia sumber daya dan peminta sumber
daya ketika menggunakan alokasi tanpa DLF (kotak biru) dan
dengan DLF (kotak oranye). Pada ATN-OBY dan ATN-PSD,
garis oranye menunjukkan bahwa pemanfaatan slice melebihi
pemanfaatan penuh 100%, yang menyebabkan slice kelaparan
| sumber  | daya  | karena  | ketidakmampuan  |     | untuk  | memulihkan  |     |     |     |     |     |
| ------- | ----- | ------- | --------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- |
sumber daya yang disediakan (disumbangkan) yang sedang
| digunakan.  | Hal  | ini  terutama  |     | disebabkan  |     | oleh  penerapan  |     |     |     |     |     |
| ----------- | ---- | -------------- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- |
algoritme alokasi sumber daya dalam benchmark secara real-
time tanpa mempertimbangkan permintaan di masa mendatang.
Garis kuning menunjukkan pemanfaatan slice menggunakan
DLF yang kami usulkan. Berbeda dengan alokasi sumber daya
| tanpa  menggunakan  |       | DLF           | dengan       |      | warna  | kuning,      | alokasi   |     |     |     |     |
| ------------------- | ----- | ------------- | ------------ | ---- | ------ | ------------ | --------- | --- | --- | --- | --- |
| sumber              | daya  | menggunakan   |              | DLF  | tidak  | menyebabkan  |           |     |     |     |     |
| overutilisasi       |       | (pemanfaatan  | Bandwidth).  |      | Hal    | ini          | terutama  |     |     |     |     |
disebabkan oleh
irisan yang dikeluarkan dari daftar kandidat penyedia sumber
ˆ
| daya  P    | {..}  karena  | perhitungan  |             | permintaan  |              | dan  penawaran  |            |     |     |     |     |
| ---------- | ------------- | ------------ | ----------- | ----------- | ------------ | --------------- | ---------- | --- | --- | --- | --- |
| untuk  50  | kali          | langkah      | berikutnya  |             | menunjukkan  |                 | kelaparan  |     |     |     |     |
sumber daya ketika menggunakan sumber daya
alokasi tanpa DLF (grafik berwarna oranye). Di sisi lain, irisan
| LTE  adalah  |     | peminta  sumber  |     | daya  | dan  sumber  | daya  | yang  |     |     |     |     |
| ------------ | --- | ---------------- | --- | ----- | ------------ | ----- | ----- | --- | --- | --- | --- |
diminta dalam alokasi tanpa DLF disediakan oleh irisan ATN-
OBY pada langkah waktu 51 dan dari semua irisan lainnya
pada langkah waktu 53. Hal ini terlihat jelas pada penurunan
tajam sumber daya yang dikonsumsi pada langkah waktu 53.
Sementara itu, jumlah sumber daya yang lebih tinggi disediakan
oleh slice MPLS, yang tercermin dari peningkatan yang lebih
tinggi pada sumber daya yang dikonsumsi ketika menggunakan
| VOLUME 11, 2023 |     |     |     |     |     |     |     |     |     |     | 84163 |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 20. Pemanfaatan irisan dalam Wa = 6.
Tidak ada pemanfaatan berlebih pada slice yang diamati algoritma. Gambar 14 menunjukkan pemanfaatan slice
dengan menggunakan DLF yang diusulkan dibandingkan untukˆ jendela 3 untuk semua t ϵy dalam SL ϵW (a = 3
j t i a
dengan alokasi sumber daya asli tanpa DLF, yang
dan j = 101 hingga 150) dengan dan tanpa DLF.
mengonfirmasi keefektifan usulan tersebut.
84164 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
kelaparan sumber daya atau tidak sebelum memutuskan
untuk tidak

GAMBAR 21. Jumlah pemanfaatan berlebihan dalam Wa = 6.
| Pada  | jendela  | ini,  | ATN-OBY  | dan  | ATN-PSD  |     |
| ----- | -------- | ----- | -------- | ---- | -------- | --- |
memberikan sumber daya dari 100-105 langkah waktu
| ke  LTE  | slice  | tanpa  | menggunakan  |     | DLF  | karena  |
| -------- | ------ | ------ | ------------ | --- | ---- | ------- |
pemanfaatannya yang rendah β < 40% (kotak biru). Di
sisi lain, pada time step 120, ATN-OBY meminta sumber
daya yang disediakan oleh LTE dan MPLS slice karena
utilisasi ATN-OBY mendekati utilisasi 100% (kotak biru)
| dan  (kotak  | kuning  | dengan  | DLF).  | Sebaliknya,  |     | karena  |
| ------------ | ------- | ------- | ------ | ------------ | --- | ------- |
pemanfaatannya yang rendah β < 40%, potongan MPLS
menyediakan sumber daya pada langkah waktu 104
dan 106 ke potongan LTE. Pada jendela ini, slice ATN-
| PSD  tidak   | menyediakan  |          | sumber  | daya        | apapun      | karena  |
| ------------ | ------------ | -------- | ------- | ----------- | ----------- | ------- |
| perhitungan  | alokasi      | pasokan  | dan     | permintaan  | didasarkan  |         |
pada perkiraan konsumsi sumber daya. Oleh karena itu,
| akan  ada  | pengetahuan  |     | sebelumnya  | apakah  | akan  | ada  |
| ---------- | ------------ | --- | ----------- | ------- | ----- | ---- |
VOLUME 11, 2023 84165

|     |     |     |     |     |     |     |     | mirip  dengan  | utilisasi  aktual.  | Gambar  | 18  menunjukkan  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | ------- | ---------------- | --- |
mempertimbangkan (drop) penyedia sumber daya (donor) daMri.  K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
pemanfaatan irisan untuk jendela 5 untuk semua
pertimbangan sebagai kandidat penyedia sumber daya P{..D}.it entukan Perangkat Lunak
t ˆϵy dalam SL ϵW
Garis  kuning  menunjukkan  bahwa  penggunaan  slice  dijaga   (a = 5 dan j = 201 hinˆgga 250)
|                        |     |     |     |     |     |     |     | j t                   | i a          |           |           |      |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------ | --------- | --------- | ---- |
| agar tetap sama dengan |     |     |     |     |     |     |     | dengan dan tanpa DLF. |              |           |           |      |
|                        |     |     |     |     |     |     |     | Pada  Gambar          | 18,  irisan  | ATN-OBY,  | ATN-PSD,  | dan  |
pemanfaatan slice asli karena slice tersebut tidak dianggap
sebagai penyedia slice setelah menggunakan DLF yang kami  MPLS (karena pemanfaatannya yang rendah β <40% dalam
kotak biru) menyediakan sumber daya ke irisan LTE pada
usulkan. Analisis yang sama diterapkan pada irisan ATN-OBY
langkah waktu 201 sejak
untuk langkah waktu 100 hingga
120. Hasil alokasi sumber daya di atas menunjukkan bahwa
| alokasi  | sumber  | daya  | menggunakan  |     | DLF  | (garis  | kuning)  |     |     |     |     |     |
| -------- | ------- | ----- | ------------ | --- | ---- | ------- | -------- | --- | --- | --- | --- | --- |
mengurangi pemanfaatan berlebih dibandingkan dengan yang
| lain.  Gambar  |     | 15a  dan  | Gambar  | 15b  | menunjukkan  |     | hitungan  |     |     |     |     |     |
| -------------- | --- | --------- | ------- | ---- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
berapa kali pemanfaatan irisan melebihi tanda pemanfaatan
100% untuk irisan ATN-OBY dan irisan ATN-PSD.
Dari Gambar 15a dan Gambar 15b, alokasi sumber daya
| dengan  | DLF  | mengurangi  | jumlah  |     | 100%  overutilisasi  |     | untuk  |     |     |     |     |     |
| ------- | ---- | ----------- | ------- | --- | -------------------- | --- | ------ | --- | --- | --- | --- | --- |
potongan ATN-OBY dan mempertahankan jumlah yang tepat
dibandingkan dengan rasio asli untuk potongan ATN-PSD.
Berbeda dengan irisan ATN-OBY, alokasi sumber daya yang
| diusulkan  | dengan  | DLF  | meningkatkan  |     | alokasi  | sumber  | daya  |     |     |     |     |     |
| ---------- | ------- | ---- | ------------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- |
dengan mengurangi jumlah jumlah overutilisasi seperti yang
| digambarkan  | pada  | Gambar  |     | 15b.  | Gambar  | 16  menunjukkan  |     |     |     |     |     |     |
| ------------ | ----- | ------- | --- | ----- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
irisan
| pemanfaatan untuk jendela 4 untuk semua t ϵy di SL ϵW |     |     |     |     |     |     |  (a  |     |     | ˆ   |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|                                                       |     |     |     |     |     | j t | i a  |     |     |     |     |     |
= 4 dan
j = 151 hingga 200) dengan dan tanpa DLF.
Pada Gambar 16, irisan LTE adalah peminta sumber daya
karena
| γ  >  60%,  | sedangkan  |     | irisan  | ATN-OBY  |     | dan  | ATN-PSD  |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | -------- | --- | ---- | -------- | --- | --- | --- | --- | --- |
menyediakan sumber daya untuk irisan LTE pada langkah 151
(karena pemanfaatannya yang rendah yaitu β < 40% dalam
kotak biru). Hal ini pada akhirnya menyebabkan kekurangan
sumber daya untuk irisan ATN-OBY dan ATN-PSD seperti
yang digambarkan pada garis oranye pada Gambar 16a dan
16b. Sebaliknya, ketika menggunakan DLF, karena alokasi
| sumber     | daya      | penawaran  | dan     | permintaan  |        | didasarkan  | pada      |     |     |     |     |     |
| ---------- | --------- | ---------- | ------- | ----------- | ------ | ----------- | --------- | --- | --- | --- | --- | --- |
| perkiraan  | konsumsi  |            | sumber  | daya,       | kedua  | irisan      | tersebut  |     |     |     |     |     |
dibebaskan dari
ˆ
daftar penyedia sumber daya P {..} seperti yang diilustrasikan
| oleh  garis  | kuning  |     | pada  Gambar  |     | 16a  dan  | 16b.  | Dengan  |     |     |     |     |     |
| ------------ | ------- | --- | ------------- | --- | --------- | ----- | ------- | --- | --- | --- | --- | --- |
demikian, ada pengetahuan sebelumnya
apakah akan terjadi kelaparan sumber daya atau tidak, sebelum
memutuskan untuk tidak mempertimbangkan (drop) penyedia
sumber daya (donor) sebagai kandidat penyedia sumber daya.
Garis kuning menunjukkan bahwa pemanfaatan slice dijaga
agar tetap sama dengan pemanfaatan slice asli karena slice
| tersebut     | tidak  | dianggap   | sebagai     |     | penyedia     | slice  | setelah  |     |     |     |     |     |
| ------------ | ------ | ---------- | ----------- | --- | ------------ | ------ | -------- | --- | --- | --- | --- | --- |
| menggunakan  |        | DLF  yang  | diusulkan.  |     | Sebaliknya,  | slice  | MPLS     |     |     |     |     |     |
menyediakan sumber daya ke slice LTE pada langkah 153 dan
155. Di sisi lain, mengenai penggabungan sumber daya dengan
DLF, slice ATN-OBY menerima sumber daya dari slice LTE
pada langkah 162. Jelas bahwa alokasi sumber daya dengan
| DLF  mengurangi  |     | pemanfaatan  |     |     | keseluruhan  | dan  | jumlah  |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | --- | ------------ | ---- | ------- | --- | --- | --- | --- | --- |
pemanfaatan yang berlebihan. Gambar 17a dan Gambar 17b
| menunjukkan  |     | berapa  | kali  pemanfaatan  |     | slice  | melebihi  | batas  |     |     |     |     |     |
| ------------ | --- | ------- | ------------------ | --- | ------ | --------- | ------ | --- | --- | --- | --- | --- |
pemanfaatan 100% untuk slice ATN-OBY dan ATN-PSD.
Dari Gambar 17a dan Gambar 17b, alokasi sumber daya
menggunakan DLF pada irisan ATN-OBY mengurangi jumlah
| overutilisasi  | dibandingkan  |      | dengan      |                | alokasi          | asli  dan  | alokasi  |     |     |     |                 |     |
| -------------- | ------------- | ---- | ----------- | -------------- | ---------------- | ---------- | -------- | --- | --- | --- | --------------- | --- |
| tanpa  DLF.    | Demikian      |      | juga,       | pada           | slice  ATN-PSD,  |            | alokasi  |     |     |     |                 |     |
| menggunakan    |               | DLF  | mengurangi  | overutilisasi  |                  | menjadi    | nol,     |     |     |     |                 |     |
| 84166          |               |      |             |                |                  |            |          |     |     |     | VOLUME 11, 2023 |     |

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
GAMBAR 22. Penggunaan irisan dalam Wa = 6.
supply dan demand didasarkan pada
LTE adalah peminta sumber daya dengan γ > 60%. Hal ini
pada akhirnya menyebabkan kelaparan sumber daya untuk
ATN-OBY, dan ATN-PSD seperti yang digambarkan pada
| garis  merah  | pada  | Gambar  18a  | dan  18b.  Sementara  | itu,  |
| ------------- | ----- | ------------ | --------------------- | ----- |
untuk alokasi sumber daya menggunakan DLF, slice MPLS
| hanya  menyediakan  |     | sumber  daya  | yang  diminta  | dan  |
| ------------------- | --- | ------------- | -------------- | ---- |
mengkompensasi sumber daya yang turun dari ATN-OBY
| dan  ATN-PSD  | karena  | perhitungan  | alokasi  sumber  | daya  |
| ------------- | ------- | ------------ | ---------------- | ----- |
VOLUME 11, 2023 84167

konsumsi sumber daya yang diperkirakan; kedua irisaMn. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
dikecualikan dari daftar penyedia sumber daya P {..}. Hal inDiit entukan Perangkat Lunak
ˆ
menjelaskan rendahnya pemanfaatan di ATN-OBY dan ATN-
PSD (berwarna kuning sejajar
dengan pemanfaatan yang sebenarnya). Di sisi lain, ATN-OBY
juga meminta sumber daya pada langkah waktu 210 yang
disediakan oleh LTE slice. ATN-PSD juga meminta sumber
daya pada langkah waktu 212, yang juga disediakan oleh LTE.
Gambar 19a dan 19b menunjukkan hitungan
84168 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
|     |     |     |     |     | menunjukkan  |     | jumlah  | kali  | pemanfaatan  | irisan  | melebihi  |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | ----- | ------------ | ------- | --------- |
pemanfaatan 100% untuk irisan ATN-OBY dan irisan ATN-
PSD, masing-masing.
Pada Gambar 21, alokasi sumber daya ATN-PSD secara
|     |     |     |     |     | signifikan    |     | meningkatkan  |          | pemanfaatan  |          | berlebih  |
| --- | --- | --- | --- | --- | ------------- | --- | ------------- | -------- | ------------ | -------- | --------- |
|     |     |     |     |     | dibandingkan  |     | dengan        | alokasi  | tanpa        | DLF.     | Gbr  22   |
|     |     |     |     |     | menunjukkan   |     | pemanfaatan   | irisan   | untuk        | jendela  | 7  untuk  |
semua
|     |     |     |     |     | t ˆϵy dalam SL ϵW |     |     |  (a = 7 dan j = 300 hingga 350)  |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | -------------------------------- | --- | --- | --- |
|     |     |     |     |     | j t               |     | i   | a                                |     |     |     |
dengan dan tanpa DLF.
Pada windows 7, hanya irisan MPLS dengan β <40%
yang menyediakan sumber daya untuk LTE dengan γ >60%.
|     |     |     |     |     | Sementara  | itu,  | irisan  | ATN-OBY  |     | dan  ATN-PSD  | tidak  |
| --- | --- | --- | --- | --- | ---------- | ----- | ------- | -------- | --- | ------------- | ------ |
menyediakan atau menerima sumber daya apa pun. Gambar
|     |     |     |     |     | 23a  dan  | 23b  | menunjukkan  |     | hitungan  |     | berapa  kali  |
| --- | --- | --- | --- | --- | --------- | ---- | ------------ | --- | --------- | --- | ------------- |
pemanfaatan slice melebihi pemanfaatan 100% untuk slice
ATN-OBY dan ATN-PSD.
|     |     |     |     |     | Secara  | keseluruhan,  |     | DLVisor  |     | dapat  meningkatkan  |     |
| --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | --- | -------------------- | --- |
alokasi sumber daya dibandingkan dengan tolok ukur kami
(EnterpriseVisor) dengan
|     |     |     |     |     | 1- Mengurangi  |     | dan  | menghilangkan  |     | penggunaan  | irisan  |
| --- | --- | --- | --- | --- | -------------- | --- | ---- | -------------- | --- | ----------- | ------- |
yang berlebihan di Enter- priseVisor
2- Mengurangi kelaparan sumber daya yang diakibatkan
oleh donasi sumber daya yang dilakukan oleh modus
manajemen sumber daya di EnterpriseVisor
|     |     |     |     |     | 3- Meningkatkan  |     |     | pemanfaatan  |     | slice  vSDN  | secara  |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------ | --- | ------------ | ------- |
keseluruhan
|     |     |     |     |     | mengingat  |     | bahwa  | perhitungan  |     | alokasi  | sumber  daya  |
| --- | --- | --- | --- | --- | ---------- | --- | ------ | ------------ | --- | -------- | ------------- |
penawaran dan permintaan didasarkan pada perkiraan
konsumsi sumber daya, ATN-PSD
slice dikecualikan dari daftar penyedia sumber daya P
{..}
(Garis kuning sejajar dengan yang sebenarnya) seperti
pada Gbr 20b. Dengan demikian, nilai
|     |     |     |     |     | MPLS  | mengkompensasi  |     |     | jumlah  | yang  | hilang  dengan  |
| --- | --- | --- | --- | --- | ----- | --------------- | --- | --- | ------- | ----- | --------------- |
sumber daya ekstra. Hal ini membenarkan peningkatan
penggunaan dalam MPLS untuk alokasi menggunakan
DLF (garis kuning) pada Gambar 20d. Gambar 21a dan
Gambar 21b
GAMBAR 23. Jumlah pemanfaatan berlebihan dalam Wa = 7.
berapa kali pemanfaatan irisan melebihi pemanfaatan 100%
untuk ATN-OBY dan ATN-PSD, masing-masing
Dari Gambar 19, manajemen sumber daya menggunakan
DLF menghasilkan alokasi sumber daya yang lebih baik
daripada tanpa DLF dan meningkatkan pemanfaatan slice
untuk penyedia sumber daya ATN-OBY dan slice ATN-
PSD. Gambar 20 menunjukkan pemanfaatan irisan untuk
jendela 6 untuk semua
| t ˆϵy dalam SL ϵW |     |  (a = 6 dan j = 251 hingga 300)  |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| j t               |     | i a                              |     |     |     |     |     |     |     |     |     |
dengan dan tanpa DLF.
Pada Gambar 20, di Jendela 6 pada langkah waktu 251
| dan  tanpa  | DLF,  | ATN-PSD  | dan  irisan  | MPLS  (karena  |     |     |     |     |     |     |     |
| ----------- | ----- | -------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
pemanfaatannya yang rendah β < 40% dalam kotak biru)
menyediakan sumber daya untuk irisan LTE karena γ >
| 60%.  Sementara  |     | itu,  dengan  | menggunakan  | DLF  dan  |     |     |     |     |     |     |       |
| ---------------- | --- | ------------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME 11, 2023  |     |               |              |           |     |     |     |     |     |     | 84169 |
ˆ

VI. KESIMPULAN M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Sebagai kesimpulan, makalah ini menunjukkan pengembangaDnit entukan Perangkat Lunak
dan implementasi metode untuk manajemen sumber daya slice
(bandwidth) di vSDN. Ditemukan bahwa manajemen sumber
daya dan alokasi sumber daya bandwidth, terutama pada waktu
aktual saat ini, dapat menyebabkan kelaparan sumber daya
karena penggunaan sumber daya yang berlebihan; terutama
mengingat bahwa perhitungan pasokan dan permintaan sumber
| daya  dalam  | solusi  | manajemen  |     | sumber  | daya  | terkait  tidak  |
| ------------ | ------- | ---------- | --- | ------- | ----- | --------------- |
memperhitungkan permintaan di masa depan dan perubahan
yang cepat dalam profil lalu lintas. Oleh karena itu, kerangka
| kerja  manajemen  |     | sumber  | daya  | yang  | proaktif  | dan  cerdas  |
| ----------------- | --- | ------- | ----- | ----- | --------- | ------------ |
diperlukan. Dengan demikian, algoritme pengalokasian sumber
daya (lalu lintas) yang akurat dan kuat sangat penting. Oleh
| karena        | itu,  DLVisor  | dikembangkan  |         | dengan         | kerangka  | kerja          |
| ------------- | -------------- | ------------- | ------- | -------------- | --------- | -------------- |
| pembelajaran  |                | dinamis       | yang    | menggabungkan  |           | algoritme  ML  |
| dengan        | bantuan        | halus         | untuk   | mempelajari    |           | (meramalkan)   |
| permintaan    | di             | masa          | depan.  | Ia  bereaksi   | dan       | beradaptasi    |
terhadap setiap perubahan signifikan dalam profil trafik dengan
menggunakan pendeteksi perubahan konsep dan pengujian yang
| signifikan.  | Metode  |     | berbasis  | jendela  | digunakan  | untuk  |
| ------------ | ------- | --- | --------- | -------- | ---------- | ------ |
mengurangi atau menghilangkan fluktuasi lalu lintas data, yang
| dapat  memperburuk  |     | kinerja  |     | ML  sesuai  | dengan  | penelitian  |
| ------------------- | --- | -------- | --- | ----------- | ------- | ----------- |
sebelumnya. Akhirnya, kerangka kerja pembelajaran dinamis
| yang  telah  | ditingkatkan  |       | diterapkan  | pada        | kerangka  | kerja        |
| ------------ | ------------- | ----- | ----------- | ----------- | --------- | ------------ |
| manajemen    | sumber        | daya  | untuk       | memberikan  |           | pemanfaatan  |
sumber daya yang lebih baik dan menghilangkan penggunaan
yang berlebihan yang dihasilkan dari perhitungan penawaran
dan permintaan.
REFERENSI
[1] A. Blenk, A. Basta, M. Reisslein, and W. Kellerer, ''Survey on network vir-
tualization hypervisors for software defined networking,'' IEEE Commun.
Survey Tuts, vol. 18, no. 1, hal. 655-685, 1st Quart., 2016.
[2] A. Kivity, Y. Kamay, D. Laor, U. Lublin, and A. Liguori, ''kvm: The Linux
virtual machine monitor,'' in Proc. Linux Symp., Canada, America, Jun. 2007,
pp. 225-230.
[3] C. A. Waldspurger, ''Manajemen sumber daya memori di server VMware
ESX,'' ACM SIGOPS Operating Syst. Rev. vol. 36, hal. 181-194, Desember
2002.
84170 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
diskalakan dalam jaringan yang ditentukan oleh perangkat lunak,''
[4] A. A. Blenk, ''Menuju virtualisasi jaringan yang ditentukan perangkat
IEEE Internet Comput., vol. 17, no. 2,
lunak: Analisis, pemodelan, dan optimasi,'' Dept. Inf. Technol,
pp. 20-27, Maret 2013.
Technis- che Universität München, Munich, Germany, Tech. Rep.
[25] R. R. Jain dan S. Paul, ''Virtualisasi jaringan dan jaringan berbasis
21.11.2017, 2018.
perangkat lunak untuk komputasi awan: Sebuah survei,'' IEEE
[5] F. Rodríguez-Haro, F. Freitag, L. Navarro, E. Hernánchez-sánchez,
Commun. Mag, vol. 51, no. 11,
N. N. Farías-Mendoza, J. A. Guerrero-Ibáñez, and A. González-Potes,
pp. 24-31, November 2013.
''Sebuah ringkasan teknik virtualisasi,'' Proc. Technol., vol. 3,
pp. 267-272, Januari 2012.
[6] T. Anderson, L. Peterson, S. Shenker, dan J. Turner, ''Mengatasi
kebuntuan Internet melalui virtualisasi,'' Computer, vol. 38, no. 4,
pp. 34-41, April 2005.
[7] M. Yu, J. Rexford, X. Sun, S. Rao, dan N. Feamster, ''Survei penggunaan
LAN virtual di jaringan kampus,'' IEEE Commun. Mag, vol. 49, no. 7,
pp. 98-103, Juli 2011.
[8] A. Belbekkouche, Md. M. Hasan, dan A. Karmouch, ''Penemuan dan
alokasi sumber daya dalam virtualisasi jaringan,'' IEEE Commun. Survei
Tuts, vol. 14, no. 4, pp. 1114-1128, 4th Quart., 2012.
[9] R. Boutaba, M. A. Salahuddin, N. Limam, S. Ayoubi, N. Shahriar,
F. Estrada-Solano, dan O. M. Caicedo, ''Survei komprehensif tentang
pembelajaran mesin untuk jaringan: Evolusi, aplikasi, dan peluang
penelitian,'' J. Internet Services Appl., vol. 9, no. 1, hlm. 1-99, Des. 2018.
[10] M. H. H. Khairi, S. H. S. Ariffin, N. M. A. Latiff, K. M. Yusof,
M. K. Hassan, F. T. Al-Dhief, M. Hamdan, S. Khan, dan M. Hamzah,
''Deteksi dan klasifikasi aliran konflik di SDN menggunakan algoritme
pembelajaran mesin,'' IEEE Access, vol. 9, hlm. 76024-76037, 2021.
[11] K. Z. Ghafoor, L. Kong, D. B. Rawat, E. Hosseini, dan A. S. Sadiq,
''Kualitas protokol perutean yang sadar akan layanan di Internet
Kendaraan yang ditentukan perangkat lunak,'' IEEE Internet Things J.,
vol. 6, tidak ada. 2, hal. 2817-2828, Apr. 2019.
[12] M. K. Hassan, S. H. Ariffin, S. K. Syed-Yusof, N. E. Ghazali, dan
M. E. Kanona, ''Analisis hybrid non-linear autoregressive neural
network dan teknik local smoothing untuk peramalan irisan
bandwidth,'' TELKOMNIKA, Telecommun. Comput. Elektron. Kontrol,
vol. 19, no. 4,
pp. 1078-1089, 2021.
[13] M. Alauthman, N. Aslam, M. Al-kasassbeh, S. Khan, A. Al-Qerem, and
K.-K. R. Choo, ''Sebuah pendekatan deteksi botnet berbasis
pembelajaran penguatan yang efisien,'' J. Netw. Comput. Appl., vol. 150,
Jan. 2020, Art. no. 102479.
[14] X. Li, S. Li, P. Zhou, dan G. Chen, ''Peramalan aliran antarmuka jaringan
menggunakan sistem pembelajaran yang luas berdasarkan algoritme
pencarian burung pipit,'' Entropy, vol. 24, no. 4, p. 478, Mar. 2022.
[15] A. R. Abdellah dan A. Koucheryavy, ''Prediksi lalu lintas VANET
menggunakan LSTM dengan pembelajaran jaringan syaraf tiruan,'' dalam
Proc. Int. Conf. Next Gener. Jaringan Kabel/Nirkabel. Cham, Swiss:
Springer, 2020, pp. 281-294.
[16] S. K. Singh, M. M. Salim, J. Cha, Y. Pan, dan J. H. Park, ''Kerangka kerja
sub-slicing jaringan berbasis pembelajaran mesin dalam lingkungan 5G
yang berkelanjutan,'' Sustainability, vol. 12, no. 15, hlm. 6250, Agustus
2020.
[17] M. Berman, J. S. Chase, L. Landweber, A. Nakao, M. Ott,
D. Raychaudhuri, R. Ricci, dan I. Seskar, ''GENI: Sebuah testbed federasi
untuk eksperimen jaringan inovatif,'' Comput. Netw., vol. 61, hal. 5-23,
Mar. 2014.
[18] H. H. Ishio, J. Minowa, dan K. Nosu, ''Tinjauan dan status teknologi
pembagian-panjang-gelombang-multipleks dan aplikasinya,'' J. Lightw.
Technol., vol. 2, no. 4, hal. 448-463, Agustus 1984.
[19] X. Xiao, A. Hannan, B. Bailey, dan LM Ni, ''Rekayasa trafik dengan
MPLS di Internet,'' IEEE Netw., vol. 14, no. 2, hal. 28-33, April 2000.
[20] A. Leon-Garcia dan L. G. Mason, ''Pengelolaan sumber daya jaringan
virtual untuk jaringan generasi berikutnya,'' IEEE Commun. Mag, vol. 41,
no. 7,
pp. 102-109, Juli 2003.
[21] T. Koponen, K. Amidon, P. Balland, M. Casado, A. Chanda, B. Fulton,
I. Ganichev, J. Gross, P. Ingram, E. Jackson, dan A. Lambeth,
''Virtualisasi jaringan di pusat data multi-tenant,'' in Proc. 11th USENIX
Symp. Networked Syst. Design Implement. (NSDI), 2014, pp. 203-216.
[22] S. Shenker, L. Peterson, dan J. Turner, ''Mengatasi kebuntuan Internet
melalui virtualisasi,'' dalam Proc. ACM HotNets-III, 2004, hal. 1-8.
[23] H. Ballani, P. Costa, T. Karagiannis, dan A. Rowstron, ''Menuju jaringan
pusat data yang dapat didikte,'' dalam Proc. ACM SIGCOMM Conf., Aug.
2011,
hal. 242-253.
[24] D. Drutskoy, E. Keller, dan J. Rexford, ''Virtualisasi jaringan yang dapat
VOLUME 11, 2023 84171

[26] N. Feamster, J. Rexford, dan E. Zegura, ''Jalan menuju SDN: SejaraMh. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
intelektual jaringan yang dapat diprogram,'' ACM SIGCOMM CompuDti.t entukan Perangkat Lunak
Commun. Rev. vol. 44, no. 2, hal. 87-98, Apr. 2014.
[27] R. Sherwood, M. Chan, A. Covington, G. Gibb, M. Flajslik, N. Handigol, T.-
Y. Huang, P. Kazemian, M. Kobayashi, J. Naous, S. Seetharaman,
D. Underhill, T. Yabe, K.-K. Yap, Y. Yiakoumis, H. Zeng, G. Appenzeller,
R. Johari, N. McKeown, dan G. Parulkar, ''Mengukir irisan penelitian dari
jaringan produksi Anda dengan OpenFlow,'' ACM SIGCOMM Comput.
Commun. Rev. vol. 40, no. 1, hal. 129-130, Jan. 2010.
[28] R. Sherwood, G. Gibb, K.-K. Yap, G. Appenzeller, M. Casado,
N. McKeown, dan G. Parulkar, ''Flowvisor: Sebuah lapisan virtualisasi
jaringan,'' OpenFlow Switch Consortium, vol. 1, hal. 132, Oktober 2009.
[29] N. Van Giang and Y. H. Kim, ''Slicing the next mobile packet core network,''
in Proc. 11th Int. Symp. Wireless Commun. Syst. (ISWCS), Aug. 2014, pp.
901-904.
[30] X. Jin, J. Rexford, dan D. Walker, ''Pembaruan inkremental untuk hypervisor
SDN komposisi,'' dalam Proc. 3rd Workshop Hot Topics Softw. Defined Netw.,
Agustus 2014, hal. 187-192.
[31] A. Al-Shabibi, M. De Leenheer, M. Gerola, A. Koshibe, W. Snow, dan
G. Parulkar, ''OpenVirteX: Sebuah hypervisor jaringan,'' dalam Proc. Open
Netw. Summit (ONS), 2014, pp. 1-9.
[32] R. Doriguzzi-Corin, E. Salvadori, M. Gerola, M. Suñé, and H. Woesner, ''A
datapath-centric virtualization mechanism for OpenFlow networks,'' in Proc.
3rd Eur. Workshop Softw. Defined Netw., Sep. 2014, pp. 19-24.
[33] X. Jin, J. Gossels, J. Rexford, and D. Walker, ''CoVisor: A compositional
hypervisor for software-defined networks,'' in Proc. 12th USENIX Symp.
Networked Syst. Design Implement. (NSDI), 2015, pp. 87-101.
[34] L. Liao, A. Shami, dan V. C. M. Leung, ''FlowVisor terdistribusi: Platform
FlowVisor terdistribusi untuk virtualisasi jaringan awan yang sadar akan
kualitas layanan,'' IET Netw., vol. 4, no. 5, pp. 270-277, Sep. 2015.
[35] J.-L. Chen, Y.-W. Ma, H.-Y. Kuo, C.-S. Yang, dan W.-C. Hung, ''Platform
virtualisasi jaringan yang ditentukan perangkat lunak untuk manajemen
sumber daya jaringan perusahaan,'' IEEE Trans. Emerg. Topics Comput., vol.
4, no. 2,
Hal. 179-186, April 2016.
[36] Y. Han, J. Li, D. Hoang, J.-H. Yoo, and J. W. Hong, ''An intent-based network
virtualization platform for SDN,'' in Proc. 12th Int. Conf. Netw. Service
Manage. (CNSM), Oct. 2016, pp. 353-358.
[37] H. Yamanaka, E. Kawai, dan S. Shimojo, ''AutoVFlow: Virtualisasi jaringan
OpenFlow area luas berskala besar,'' Comput. Commun, vol. 102,
Hal. 28-46, April 2017.
[38] H. Yamanaka, E. Kawai, S. Ishii, dan S. Shimojo, ''AutoVFlow: Virtualisasi
otonom untuk jaringan OpenFlow area luas,'' dalam Proc. 3rd Eur. Workshop
Softw. Defined Netw., Sep. 2014, pp. 67-72.
[39] Y. Han, T. Vachuska, A. Al-Shabibi, J. Li, H. Huang, W. Snow, dan
J. W.-K. Hong, ''ONVisor: Menuju platform virtualisasi jaringan berbasis
SDN yang terukur dan fleksibel pada ONOS,'' Int. J. Netw. Manage, vol. 28,
no. 2, p. e2012, Mar. 2018.
[40] S. Agliano, M. Ashjaei, M. Behnam, dan L. L. Bello, ''Manajemen dan kontrol
sumber daya dalam jaringan SDN tervirtualisasi,'' dalam Proc. Real-Time
Embedded Syst. Technol. (RTEST), 2018, pp. 47-53.
[41] V. Struhár, M. Ashjaei, M. Behnam, S. S. Craciunas, dan
A. V. Papadopoulos, ''DART: Kerangka kerja distribusi bandwidth dinamis
untuk jaringan yang didefinisikan oleh perangkat lunak tervirtualisasi,'' dalam
Proc. 45th Annn. Conf. IEEE Ind. Electron. Soc. (IECON), vol. 1, Oct. 2019,
pp. 2934-2939.
[42] L. Leonardi, L. Lo Bello, dan S. Aglianó, ''Manajemen bandwidth berbasis
prioritas dalam jaringan yang ditentukan perangkat lunak tervirtualisasi,''
Electronics, vol. 9, no. 6, hal. 1009, Jun. 2020.
[43] G. Yang, B.-Y. Yu, H. Jin, dan C. Yoo, ''Libera untuk virtualisasi jaringan
yang dapat diprogram,'' IEEE Commun. Mag, vol. 58, no. 4, pp. 38-44, Apr.
2020.
[44] G. Yang, Y. Yoo, M. Kang, H. Jin, dan C. Yoo, ''Bandwidth isolation guar-
antee for SDN virtual networks,'' in Proc. IEEE Conf. Comput. Commun.
(INFOCOM), Mei 2021, pp. 1-10.
[45] A. Ahmadian dan M. Ahmadi, ''DC-CAMP: Pembuatan kontroler dinamis,
alokasi dan protokol manajemen di SDN,'' Wireless Pers. Commun, vol. 125,
pp. 531-558, Feb. 2022.
[46] M. K. Hassan, S. H. Syed Ariffin, N. E. Ghazali, M. Hamad, M. Hamdan,
M. Hamdi, H. Hamam, dan S. Khan, ''Kerangka kerja pembelajaran dinamis
untuk prakiraan lalu lintas backbone berbasis pembelajaran mesin
berbantuan,'' Sen-sors, vol. 22, no. 9, hal. 3592, Mei 2022.
[47] G. Sun, K. Xiong, G. O. Boateng, G. Liu, dan W. Jiang, ''Pemotongan dan
penyesuaian sumber daya di RAN dengan duel jaringan Q-dalam,''
J. Netw. Comput. Appl., vol. 157, Mei 2020, Art. no. 102573, doi:
10.1016/j.jnca.2020.102573.
84172 VOLUME 11, 2023

M. K. Hassan dkk.: DLVisor: Hypervisor Pembelajaran Dinamis untuk Jaringan yang
Ditentukan Perangkat Lunak
MOHAMED KHALAFALLA HASSAN menerima MOHAMMED E. A. KANONA menerima gelar
meraih gelar B.Sc. di bidang teknik komputer B.Sc., M.Sc., dan Ph.D. di bidang teknik
dari Future University, Sudan, pada tahun 2004, telekomunikasi dari Future University,
dan gelar M.Sc. di bidang teknik jaringan Sudan. Saat ini beliau menjabat sebagai Wakil
komunikasi dari University Putra Malaysia Dekan Fakultas Teknologi
(UPM), pada tahun 2009. Saat ini beliau sedang Telekomunikasi dan Antariksa dan Kepala Pusat
mengejar gelar Ph.D. di bidang teknik Penelitian IoT. Beliau secara aktif terlibat dalam
komunikasi di University Technol- ogy Malaysia penelitian tentang radar hamburan maju. Minat
(UTM). Beliau juga merupakan Associate penelitiannya meliputi teori informasi, SDN, IoT,
Professor di Future University. Beliau juga komputasi awan, pembelajaran mesin dan
seorang peneliti dan spesialis TIK dengan jaringan syaraf, dan
pengalaman 17 tahun. komunikasi seluler. Beliau menerima Penghargaan Makalah Terbaik dari
berbagai pengalaman penelitian dan TIK. Beliau telah menerbitkan 20 Konferensi ICCCEEE20.
makalah dalam konferensi dan jurnal internasional yang ditinjau sejawat.
Bidang penelitiannya meliputi radar hamburan ke depan, pembelajaran
mesin, NFV, vSDN, dan manajemen sumber daya dalam jaringan
komunikasi.
mobile, manajemen mobilitas, protokol
komunikasi jaringan, dan sistem pemantauan
olahraga.
SHARIFAH HAFIZAH SYED ARIFFIN (Senior
Anggota IEEE) menerima gelar B.Eng. (Hons.)
di London, pada tahun 1997, gelar M.E.E. dari
Universiti Teknologi Malaysia, pada tahun 2001,
dan gelar Ph.D. dari Queen Mary, University of
London, London, pada tahun 2006. Saat ini
beliau adalah Associate Professor di Fakultas
Teknik Elektro, Universiti Teknologi Malaysia.
Beliau telah menerbitkan 116 artikel, 17 hak
cipta, satu sirkuit terpadu, dan satu merek
dagang. Saat ini
Minat penelitiannya meliputi Internet of Things, komputasi di mana-mana
dan perangkat pintar, jaringan sensor nirkabel, ipv6, manajemen handoff,
jaringan, dan sistem komputasi seluler.
SHARIFAH KAMILAH SYED-YUSOF menerima
Gelar B.Sc. di bidang teknik elektro dari George
Washington University, Amerika Serikat, pada
tahun 1988, dan
M.E.E. dan gelar Ph.D. dari UTM, masing-
masing pada tahun 1994 dan 2006. Saat ini
beliau adalah Profesor Penuh di Fakultas Teknik
Elektro, UTM. Minat penelitiannya meliputi
komunikasi nirkabel.
NURZAL EFFIYANA BINTI GHAZALI
menerima
meraih gelar M.S. di bidang teknik elektro dari
Shibaura Institute of Technology dan gelar Ph.D.
dari UTM, pada tahun 2016. Saat ini, ia sedang
melakukan penelitian di bidang komputasi
VOLUME 11, 2023 84173

Beliau juga seorang peneliti dan ahli teknologi
KHALID S. MOHAMED (Anggota, IEEE) M. K. Hassan dkk.: DLVisor: Hypervisori nPfeomrmbealsai jdaraann k Doinmaumniisk uansti.uk Jaringan yang
menerima  gelar  sarjana  di  bidang  teknDikit entukans Ppeersaianlgiks adte Lnugnaank 16 tahun pengalaman penelitian dan TIK yang luas. Minat
telekomunikasi  dari  Future  University,  penelitiannya meliputi software define network (SDN), machine learning,
Sudan,  pada  tahun  2011,  dan  gelar  Master  of  jaringan telekomunikasi, serta desain dan implementasi antena.
Engineering di bidang telekomunikasi serta gelar
|     | Ph.D.  (Teknik)  | di  bidang   | telekomunikasi            | dari  |     |     |     |     |
| --- | ---------------- | ------------ | ------------------------- | ----- | --- | --- | --- | --- |
|     | Multimedia       | University,  | Malaysia,  masing-masing  |       |     |     |     |     |
pada tahun 2014 dan 2020. Beliau telah terdaftar di
|     |     |     |     |     | MOSAB  | HAMDAN  | (Anggota  Senior,  | IEEE)  |
| --- | --- | --- | --- | --- | ------ | ------- | ------------------ | ------ |
Dewan Teknik Sudan (SEC) sebagai Insinyur
menerima gelar B.Sc. di bidang teknik komputer
Profesional, sejak Januari 2022, dan Dewan
dan sistem elektronika dari University of Science
Engineers Malaysia (BEM) sebagai Insinyur Pascasarjana, sejak April 2019.
and Technology (UST), Sudan, pada tahun 2010,
Saat ini beliau adalah Asisten Profesor di Fakultas Teknologi Telekomunikasi
gelar M.Sc. di bidang arsitektur komputer dan
dan Antariksa dan Pelaksana Tugas Direktur Pusat Inovasi, Penelitian dan
|               |                       |               |                       |     | jaringan  | dari  University  | of  Khartoum  | (UofK),  |
| ------------- | --------------------- | ------------- | --------------------- | --- | --------- | ----------------- | ------------- | -------- |
| Pengembangan  | (IRDC),  Universitas  | Masa  Depan.  | Minat  penelitiannya  |     |           |                   |               |          |
Sudan, pada tahun 2014, dan gelar Ph.D. di
| meliputi  komunikasi  | seluler,  | 5G,  permukaan  | reflektif  cerdas  | (IRS),  |     |     |     |     |
| --------------------- | --------- | --------------- | ------------------ | ------- | --- | --- | --- | --- |
beamforming, dan manajemen interferensi dalam jaringan nirkabel. bidang teknik elektronika (jaringan komputer)
dari Faculty of Engineering, School of Electrical
|     |     |     |     |     | Engi-  | nering,  Universiti  | Teknologi  | Malaysia  |
| --- | --- | --- | --- | --- | ------ | -------------------- | ---------- | --------- |
(UTM),
Malaysia, pada tahun 2021. Dari tahun 2010 hingga 2015, ia adalah
MUTAZ H. H. KHAIRI (Anggota Senior, IEEE) Asisten Pengajar dan Dosen di Departemen Teknik Sistem Komputer dan
menerima gelar B.S. di bidang teknik komputer dari
Elektronika, Fakultas Teknik, Universitas Sains dan Teknologi (UST). Saat
Future University, pada tahun 2002, dan gelar M.S.
ini, ia adalah seorang Peneliti di Pusat Penelitian Interdisipliner untuk
di bidang teknik elektro dari Linkoping University,
|     |     |     |     | Sistem  | Keamanan  Cerdas,  | Universitas  | Perminyakan  | dan  |
| --- | --- | --- | --- | ------- | ------------------ | ------------ | ------------ | ---- |
pada tahun 2007. Saat ini beliau sedang mengejar
|     |     |     |     | Pertambangan  | King  Fahd,  Arab  | Saudi.  | Minat  penelitiannya  | saat  ini  |
| --- | --- | --- | --- | ------------- | ------------------ | ------- | --------------------- | ---------- |
gelar Ph.D. di Universiti Technologi Malaysia (UTM).
meliputi jaringan yang ditentukan perangkat lunak (SDN), penyeimbangan
Dari tahun 2002 hingga 2007, beliau adalah seorang
beban, klasifikasi lalu lintas jaringan, Internet of Things (IoT), komputasi
Dosen di Fakultas Teknik, Universitas Masa Depan,
awan, keamanan jaringan, dan jaringan masa depan.
|       | dan  Direktur  | Departemen  | Teknologi  Informasi.  |     |     |     |     |                 |
| ----- | -------------- | ----------- | ---------------------- | --- | --- | --- | --- | --------------- |
| 84174 |                |             |                        |     |     |     |     | VOLUME 11, 2023 |