## nasy-lib
[nasy-lib](https://nasy-lib.adaptable.app/main)
1. Step-by-step pembuatan proyek Django nasy-lib
Langkah pertama yaitu saya membuat proyek django baru diawali dengan membuat direktori lokal dan menjalankan virtual environment pada folder tersebut.Setelah itu saya men-install semua requirements yang diperlukan kemudian start new project dengan command "django-admin startproject nasy-lib". Setelah itu, pada settings.py saya mengisi * pada ALLOWED_HOST dengan tujuan mengizinkan semua host untuk mengakses web saya. Kemudian saya memastikan project saya sudah dapat dijalankan dengan "py manage.py runserver".
Setelah proyek berhasil diinisiasi, langkah selanjutnya yang saya lakukan adalah membuat satu aplikasi bernama 'main' dengan command "py manage.py startapp main" melalui virtual environment. Setelah terbuat, aplikasi 'main' akan dimasukkan ke dalam list INSTALLED APPS pada settings.py.
Langkah berikutnya yang saya lakukan adalah mengisi models.py dengan atribut dan field yang digunakan untuk website nasy-lib. Saya menggunakan atribut nama buku, pengarang, kuantitas buku, genre buku, dan deskripsi buku.
Selanjutnya saya membuat file html di dalam folder templates dalam folder main sebagai template frontend. Saya menampilkan judul website, nama, kelas, npm dan memasukkan data suatu buku dengan jinja sebagai placeholder suatu variabel. Variabel dari data yang ingin dimasukkan ke dalam tabel akan diisi di views.py. 
Kemudian langkah selanjutnya saya mengonfigurasi URL pada folder main dan folder nasy_lib. urls pada folder main untuk mengatur rute URL pada aplikasi main, sedangkan urls.py pada folder nasy-lib adalah untuk mengatur rute URL pada proyek website ini.
Kemudian langkah terakhir adalah saya membuat unit tes untuk mengecek apakah path url main dapat diakses atau tidak dan mengecek apakah /main/ di render menggunakan main.html yang dibuat dalam folder templates.

2. Bagan request client
![gambar bagan request client]("C:\Users\Dwi Wahyu Lestari\Desktop\Nasya\college\pbp\nasy-lib\nasy-lib\bagan.png")
hubungan antara urls.py, views.py, models.py, dan berkas html yaitu pertama user membuka website kemudian melakukan HTTP request yang dikirimkan ke urls.py untuk dilakukan routing. dengan memanggil fungsi yang terdapat di views.py. Views.py sendiri terhubung dengan models.py sebagai penghubung untuk menampilkan data dari models.py dan dikirimkan ke template atau ke berkas html untuk ditampilkan dengan bantuan {{Jinja}}.

3. Menggunakan virtual environment untuk django project
Menggunakan virtual environment untuk membuat django project sebenarnya tidak wajib. Kita masih tetap dapat membuat django project tanpa virtual environment. Tetapi, menggunakan virtual environment direkomendasikan karena dapat mengisolasi project django yang kita buat dengan project python lain dalam sistem. Hal ini dilakukan dengan tujuan menghindari gangguan  dari project-project python lainnya. Selain itu, dengan menggunakan virtual environment kita dapat dengan mudah menginstall berbagai requirements dengan mudah untuk berbagai project yang akan kita buat.

4. Perbedaan MVC, MVT, MVVM
    * MVC = Model-View-Controller, pola desain pengembangan perangkat lunak dimana model berperan sebagai penyimpan data dari database yang akan digunakan di dalam aplikasi, view sebagai pengatur tampilan interface antar data dan yang ingin ditampilkan kepada user, dan controller sebagai perantara antara model dan view yang menerima HTTP request dan memproses dengan view dan model untuk menghasilkan output yang sesuai.
    * MVT = Model-View-Template, pola desain pengembangan perangkat lunak dengan pola mirip seperti MVC, namun terdapat perbedaan di Template, dimana template berfokus pada tampilan saja dan bagaimana data dapat ditampilkan sesuai dengan keinginan. 
    * MVVM = Model-View-ViewModel, pola desain pengembangan perangkat lunak dengan fungsi model dan view yang sama dengan MVC dan MVT, tetapi template dan controller tergantikan oleh viewmodel. Viewmodel sebagai penghubung antar model dan view, viewmodel mengambil data dari model kemudian diproses untuk menjadi suatu interface.
| MVC | MVT | MVVM |
| ---         |     ---      |          --- |
| Model-View-Controller   | Model-View-Template    | Model-View-ViewModel   |
| Controller sebagai penghubung view dan model    | Template berfokus pada tampilan data dari model     | ViewModel sebagai perantara view dan model dengan data binding     |
| Controller melakukan perubahan tampilan secara manual    | Template melakukan pengembangan dan perubahan secara manual     | ViewModel mengurangi perubahan tampilan secara manual     |