## nasy-lib
[nasy-lib](https://nasy-lib.adaptable.app/main/)
### Tugas 5
1. Selector pada CSS terdapat tiga jenis, yaitu :
* Element selector adalah cara untuk memilih sebuah elemen tipe tertentu pada HTML, seperti elemen h1, h2, p. Element selector cocok digunakan ketika kita ingin mengubah design dari sebuah elemen untuk semua elemen dengan tipe yang sama, seperti mengubah semua font color dari h1. pemanggilan element selector pada css yaitu langsung tipenya tanpa diawali simbol
* ID selector adalah cara untuk memilih sebuah elemen yang sudah di assign dengan suatu id tertentu, dimana ID akan bersifat unik dalam satu halaman web. ID selector cocok digunakan ketika ingin mengubah design dari sebuah elemen hanya untuk elemen itu sendiri yang sudah di assign oleh ID unik. pemanggilan ID selector yaitu dengan diawali # kemudian diikuti nama id nya.
* Class selector adalah cara yang sering saya gunakan, yaitu memilih beberapa elemen identik yang sudah di assign dengan suatu class tertentu agar dapat diubah-ubah designnya. Class selector cocok sigunakan ketika ingin mengubah design dari sebuah atau lebih properti yang memiliki karakteristik sama sehingga tampilannya juga akan sama. pemanggilan class selector yairu dengan diawali . kemudian diikuti nama classnya

2. HTML5 adalah markup language terbaru yang digunakan untuk membuat website. HTML memiliki Tag yaitu berupa elemen yang dapat digunakan untuk mengembangkan isi-isi dari suatu website. Berikut saya akan menjelaskan beberapa tag di HTML5 terutama tag-tag yang telah saya gunakan pada tugas ini.
* **div** = tag untuk mengelompokkan beberapa elemen atau properti agar dapat lebih mudah diatur designnya
* **style** = tag yang membantu agar dapat menulis inline style css, tanpa membuat file css terpisah
* **a** = tag yang akan membuat tautan ke halaman lain pada objek dalam tag a
* **iframe** = tag yang berguna untuk memasukkan gambar atau potongan dari web lain ke dalam web saya
* **table** = tag untuk membuat tabel agar data yang ditampilkan lebih rapih

3. Margin dan padding adalah properti dalam CSS untuk mengatur spacing atau tata letak elemen. Namun, tentu keduanya memiliki perbedaan. Margin adalah properti yang mengatur jarak antara elemen dengan sisi-sisi di luar elemen tersebut. Biasanya margin digunakan untuk mengatur jarak antar elemen. Sedangkan padding adalah properti yang mengatur jarak antara suatu konten di dalam elemen dengan batas dari elemen tersebut, dengan kata lain padding mengatur tata letak atau jarak isi dari suatu elemen. Berikut saya lampirkan gambar untuk memperjelas perbedaan margin dan padding yang saya ambil dari website referensi saya
referensi : [CSS margin vs padding](https://blog.hubspot.com/website/css-margin-vs-padding)
![margin vs padding](<marpad.png>)

4. Tailwind CSS dan Bootstrap adalah framework CSS yang sering digunakan web developer. Perbedaan dari Tailwind dan Bootstrap yaitu :
* Tailwind CSS menggunakan konsep "utility-first CSS framework" yang berarti tailwind menyediakan berbagai utility class sehingga pengguna dapat membuat design tanpa harus menulis CSS. Sedangkan bootstrap merupakan "component-based framework" yang berarti untuk membangun suatu website dapat dengan mudah dilakukan dengan memanfaatkan komponen yang sudah tersedia. Beberapa komponen yang sudah tersedia juga menyediakan utility class yang dapat digunakan
* Karena Tailwind CSS menggunakan konsep "utility-first" maka tailwind lebih unggul dalam kostumisasi ragam design yang dapat dibuat. sedangkan karena bootsrap merupakan "component-based" maka ragam design yang dapat dibuat lebih sedikit
* Bootstrap sudah memiliki komponen dasar yang dapat mempercepat pembuatan proyek dbandingkan Tailwind CSS

Berdasarkan beberapa perbandingan antara tailwind css dan bootstrap, saya dapat menyimpulkan kapan sebaiknya menggunakan tailwind css dan kapan sebaiknya menggunakan bootstrap.
* Bootstrap sebaiknya digunakan untuk membangun website dengan tampilan sederhana dan hanya memiliki sedikit waktu
* Tailwind CSS sebaiknya digunakan ketika ingin membangun website dengan tampilan yang jauh lebih unik karena fleksibilitas tailwind CSS.
referensi : [tailwind css vc bootstrap](https://prismic.io/blog/tailwind-vs-bootstrap#why-compare-tailwind-vs-bootstrap)

5. Pertama yang saya lakukan dalam mengimplementasi chekclist untuk tugas 5 yaitu dengan mempelajari terkait CSS dari berbagai sumber. Kemudian saya melakukan import script bootstrap di base.html. Setelah itu saya menerapkan in-line style CSS untuk halaman html login, register, book_entry, dan main. Saya menerapkan class selector dan element selector untuk implementasi modifikasi design website saya. Untuk main.html saya membuat looping untuk tiap data yang ada agar dimasukkan ke card yang telah saya buat, dan akan memberi warna berbeda pada judul buku apabila merupakan data terakhir

### Tugas 4
user 1 : tsukxireii - pass : hlkt3456
user 2 : usagi - pass : 7azman!a
1. UserCreationForm adalah template form bawaan django yang mempermudah developer untuk membuat formulir registrasi bagi pengguna baru. Pada dasarnya, form ini akan meminta username, password, dan verifikasi password

2. Dalam konteks django, autentikasi adalah menyocokkan usernam dan password yangn diinput pengguna apakah sesuai dengan database yang tersedia apa tidak. Jika sesuai, maka user terautentikasi sebagai salah satu pengguna dalam website tersebut. Sedangkan otorisasi adalah proses django memberikan wewenang bagi pengguna yang memiliki akun di website tersebut untuk mengakses fitur-fitur di website yang ter-restriksi hanya khusus untuk pengguna yang memiliki akun saja

3. Cookies dalam website adalah sebuah data yang dimiliki oleh user di perangkat user ketika mereka menggunakan website atau aplikasi dalam website tersebut. Isi dari cookie adalah informasi dan status sesi pengguna sehingga website atau aplikasi dapat dengan cepat mengenali dan menyimpan preferensi user. Django menggunakan cookies dengan menggunakan method bawaan dari django yaitu set_cookie() saat user berhasil login, dan request cookie untuk mengambil timestamp sesi terakhir login. Selain itu delete_cookie() ketika user logout dari website

4. Meskipun banyak yang mengatakan bahwa cookies itu berbahaya karena dapat mencuri data, kenyataannya tidak jika pengimplementasian cookie nya benar. Perlu diketahui dahulu sebelumnya bahwa cookie adalah berupa potongan data, bukan program yang dapat merusak program yang sudah ada, cookie tidak bisa membaca atau menghapus data yang berada di perangkat user, biasanya cookies berisi informasi-informasi general dan tidak mengandung infpormasi individu. 
Akan tetapi, ada beberapa risiko potensial yang harus diwaspadai, yaitu :
* Jika cookies tidak terlindungi dengan benar dan tingkat keamanan rendah, ada risiko informasi dalam cookies dicuri oleh pihak lain
* Serangan XSS (Cross-Site Scripting) yaitu jika penyerang dapat memanipulasi cookies dengan menyisipkan program yang dapat merusak program asli atau bahkan mencuri data user
* Serangan CSRF (Cross-Site Request Forgery) yaitu kegiatan pembajakan akun user pengguna yang memiliki otentikasi untuk menggunakan fitur di website atau aplikasi

5. Pertama yang saya lakukan adalah membuat fitur registrasi. Fitur registrasi saya buat dengan membuat form registrasi menggunakan UserCreationForm yaitu formulir bawaan dari django. Setelah itu saya membuat function register untuk menyimpan data yang telah dimasukkan di form jika akun berhasil dibuat, membuat register.html dan tidak lupa menambahkan path dan import register di urls.py pada main. Kedua saya membuat fitur login dan menambahkan set cookies di dalamnya. dengan membuat function authenticate dan login agar bisa mengotentikasi password dan username sesuai dengan database yang pernah dimasukkan saat registrasi. Tidak lupa menambahkan login.html dan menambahkan path dan import di urls.py. Ketiga saya membuat fungsi logout untuk mengeluarkan pengguna dari akun yang sedang digunakan dan menambahkan delete cookies di dalamnya. Kemudian saya merestriksi akses halaman ke main agar user perlu melakukan login terlebih dahulu untuk bisa menambahkan buku dan mengakses buku yang hanya dimiliki user tersebut. Terakhir, untuk mengerjakan soal bonus hal pertama yang saya lakukan adalah saya mempelajari terkait CRUD di django. Kemudian saya menambahkan tombol delete untuk setiap buku yang ada pada tabel, sehingga ketika tombol delete ditekan, akan menghapus buku tersebut. Hal tersebut saya terapkan dengan mengambil id dari data buku tersebut kemudian menghapus data yang berada di id tersebut. Lalu, dengan fungsi yang mirip dengan funsi delete, saya menambahkan tombol '+' dan '-' pada setiap data amount buku untuk memodifikasi amount dari buku tersebut sesuai dengan id yang diambil.

### Tugas 3
1. POST adalah HTTP request method yang digunakan untuk mengirim data ke server seperti pada saat pengisian form menambah item atau pengisian form login/register. sedangkan GET adalah HTTP request method untuk membaca atau mengambil data dari website

2. XML digunakan untuk merepresentasikan data dalam format yang lebih terstruktur dengan sintaks "<field ...></field>". JSON juga digunakan untuk merepresentasikan data tetapi dalam format yang lebih simpel, hampir mirip dengan sintaksis dictionary pada suatu program python. Sedangkan HTML adalah tampilan web menampilkan data yang dapat diinteraksi dan ditampilkan kepada pengguna

3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena JSON adalah format data yang tergolong ringan, mudah dibaca sehingga proses transfer data lebih cepat dan efisien. Selain itu, JSON juga dapat dibaca secara oarsial sehingga dapat dibaca dan ditampilkan datanya sebelum semua data diunduh

4. Pertama, yang saya lakukan adalah saya menambahkan dan memperbaiki data-data apa saja yang ingin saya tampilkan di models.py. Kemudian saya membuat base.html sebagai skeleton untuk kerangka views dan menyesuaikan main.html. Setelah itu saya membuat struktur form pada forms.py dengan fields yang disesuaikan dengan kebutuhan website saya. kemudian saya menambahkan fungsi book_entry pada views.py untuk menambahkan data buku ketika form telah diisi dan di-submit oleh user. Pada fungsi show_main juga saya mengambil object Book yang tersimpan di database dan di assign ke products. setelah itu, saya menambahkan import dan path book_entry di urls.py pada main. Baru kemudian saya membuat book_entry.html sebagai interface user untuk mengisi form add book. Pada main.html sata yang sudah diisi dalam form akan ditampilkan dalam bentuk tabel dengan cara looping semua data books, kemudian saya menambahkan button add book untuk diarahkan ke form book entry. Setelah itu saya membuat function show xml, show json, show xml by id, dan show json by id agar dapat melihat data yang sudah diinput di form dalam format xml dan json

*![xml postman](<xml_postman.png>)
*![json postman](<json_postman.png>)
*![html postman](<html_postman.png>)
*![xml by id postman](<xmlbyid_postman.png>)
*![json by id postman](<jsonbyid_postman.png>)
<br />

### Tugas 2
1. Step-by-step pembuatan proyek Django nasy-lib
Langkah pertama yaitu saya membuat proyek django baru diawali dengan membuat direktori lokal dan menjalankan virtual environment pada folder tersebut.Setelah itu saya men-install semua requirements yang diperlukan kemudian start new project dengan command "django-admin startproject nasy-lib". Setelah itu, pada settings.py saya mengisi * pada ALLOWED_HOST dengan tujuan mengizinkan semua host untuk mengakses web saya. Kemudian saya memastikan project saya sudah dapat dijalankan dengan "py manage.py runserver".
Setelah proyek berhasil diinisiasi, langkah selanjutnya yang saya lakukan adalah membuat satu aplikasi bernama 'main' dengan command "py manage.py startapp main" melalui virtual environment. Setelah terbuat, aplikasi 'main' akan dimasukkan ke dalam list INSTALLED APPS pada settings.py.
Langkah berikutnya yang saya lakukan adalah mengisi models.py dengan atribut dan field yang digunakan untuk website nasy-lib. Saya menggunakan atribut nama buku, pengarang, kuantitas buku, genre buku, dan deskripsi buku.
Selanjutnya saya membuat file html di dalam folder templates dalam folder main sebagai template frontend. Saya menampilkan judul website, nama, kelas, npm dan memasukkan data suatu buku dengan jinja sebagai placeholder suatu variabel. Variabel dari data yang ingin dimasukkan ke dalam tabel akan diisi di views.py. 
Kemudian langkah selanjutnya saya mengonfigurasi URL pada folder main dan folder nasy_lib. urls pada folder main untuk mengatur rute URL pada aplikasi main, sedangkan urls.py pada folder nasy-lib adalah untuk mengatur rute URL pada proyek website ini.
Kemudian langkah terakhir adalah saya membuat unit tes untuk mengecek apakah path url main dapat diakses atau tidak dan mengecek apakah /main/ di render menggunakan main.html yang dibuat dalam folder templates.

2. Bagan request client
![gambar bagan request client](<bagan.png>)
hubungan antara urls.py, views.py, models.py, dan berkas html yaitu pertama user membuka website kemudian melakukan HTTP request yang dikirimkan ke urls.py untuk dilakukan routing. dengan memanggil fungsi yang terdapat di views.py. Views.py sendiri terhubung dengan models.py sebagai penghubung untuk menampilkan data dari models.py dan dikirimkan ke template atau ke berkas html untuk ditampilkan dengan bantuan {{Jinja}}.

3. Menggunakan virtual environment untuk django project
Menggunakan virtual environment untuk membuat django project sebenarnya tidak wajib. Kita masih tetap dapat membuat django project tanpa virtual environment. Tetapi, menggunakan virtual environment direkomendasikan karena dapat mengisolasi project django yang kita buat dengan project python lain dalam sistem. Hal ini dilakukan dengan tujuan menghindari gangguan  dari project-project python lainnya. Selain itu, dengan menggunakan virtual environment kita dapat dengan mudah menginstall berbagai requirements dengan mudah untuk berbagai project yang akan kita buat.

4. Perbedaan MVC, MVT, MVVM
    * MVC = Model-View-Controller, pola desain pengembangan perangkat lunak dimana model berperan sebagai penyimpan data dari database yang akan digunakan di dalam aplikasi, view sebagai pengatur tampilan interface antar data dan yang ingin ditampilkan kepada user, dan controller sebagai perantara antara model dan view yang menerima HTTP request dan memproses dengan view dan model untuk menghasilkan output yang sesuai.
    * MVT = Model-View-Template, pola desain pengembangan perangkat lunak dengan pola mirip seperti MVC, namun terdapat perbedaan di Template, dimana template berfokus pada tampilan saja dan bagaimana data dapat ditampilkan sesuai dengan keinginan. 
    * MVVM = Model-View-ViewModel, pola desain pengembangan perangkat lunak dengan fungsi model dan view yang sama dengan MVC dan MVT, tetapi template dan controller tergantikan oleh viewmodel. Viewmodel sebagai penghubung antar model dan view, viewmodel mengambil data dari model kemudian diproses untuk menjadi suatu interface.
![tabel perbedaan MVC, MVT, MVVM](<tabel.png>)
