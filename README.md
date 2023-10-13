# shopping-list



# TUGAS 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
 Dalam metode pengiriman data, form POST digunakan untuk mengirim data ke server sedangkan form GET digunakan untuk membaca atau mengambil data dari web server.
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
 XML: mengirimkan data yang terstruktur, JSON: mengirimkan data struktur objek dan array, HTML: tidak digunakan untuk pengiriman data dan hanya untuk membuat tampilan web dapat diakses pengguna
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
 JSON memiliki format pertukaran data yang ringan untuk dibaca dan ditulis oleh manusia sehingga mudah untuk ditranslate oleh komputer.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
 Membuat input form untuk menambahkan objek model pada app sebelumnya:
a. membuat berkas baru pada direktori main dengan nama forms.py
b. menambahkan beberapa import pada view.py
c. membuat fungsi baru dengan nama create_product pada berkas views.py yang menerima parameter request
d. import fungsi create_product pada urls.py
e. menambahkan path url ke dalam urlpatterns pada urls.py di main
f. membuat berkas HTML baru dengan nama create_product.html
 Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID:
a. menambahkan import HttpResponse dan Serializer pada views.py
b. membuat sebuah fungsi yang menerima parameter request dengan nama show_xml dan show_json dan variabel yang menyimpan hasil query data dalam product
c. menambahkan return function berupa HttpResponse dan parameter content_type="application/xml" atau content_type="application/json"
 Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2:
a. menambahkan path url ke dalam urlpatterns
screenshot:
![image](https://github.com/bingqiu-exe/shopping-list/assets/113889689/55a53066-bfbe-4d49-86b6-4f791427c507)
![image](https://github.com/bingqiu-exe/shopping-list/assets/113889689/0f74fdec-00c6-4e52-9724-45194a86bb5d)
![image](https://github.com/bingqiu-exe/shopping-list/assets/113889689/ab744131-7617-4787-a73f-dec53389948d)
![image](https://github.com/bingqiu-exe/shopping-list/assets/113889689/5085cbab-8348-4b88-af1a-009c17a089d1)

# TUGAS 4
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
   UserCreationForm adalah sebuah formulir yang digunakan untuk membuat proses pembuatan pengguna (user) lebih mudah dalam aplikasi web, dengan informasi seperti username, password, dan email. Kelebihan yang didapatkan dari UserCreationForm adalah mudah digunakan (membuat formulir tanpa harus menulis kode dari awal), validasi otomatis (validasi yang memastikan bahwa pengguna memasukkan informasi yang benar), konfigurasi kustom (kita dapat menyesuaikan UserCreationForm sesuai dengan kemauan kita), dan integrasi dengan django authentication (kita dapat dengan mudah mengelola authetication). Kekurangan yang ada pada UserCreationForm diantaranya adalah tampilan default tidak menarik dan tidak mendukung fitur lanjutan
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
   Autentikasi lebih mengarah pada proses yang memverifikasi identitas pengguna sebagai izin untuk memasuki aplikasi sedangkan otorisasi lebih mengarah pada proses yang melibatkan izin dan hak akses dari pengguna.
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookies merupakan mekanisme kecil yang menyimpan data di browser pengguna, pengelolaan data:
   a) server akan membuat sesi baru untuk pengguna yang memasukin web yang menggunakan sesi django
   b) cookies akan menyimpan data dari pengguna
   c) django memberikan cookies session id pada pengguna
   d) data sesi sesungguhnya disimpan pada server
   e) browser mengirimkan kembali cookie dengan ID sesi ke server ketika pengguna membuat permintaan ke server
   f) data sesi akan dihapus ketika sesi berakhir
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
   Harus, sebab ada cookies yang memiliki risiko seperti kebocoran informasi pribadi, cookie theft, dan tracking pengguna.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Untuk membuat halaman registrasi:
    Formulir:
    1) dalam views.py import -> from django.shortcuts import redirect, from django.contrib.auth.forms import UserCreationForm, from django.contrib import messages
    2) tambahkan fungsi register
    3) buat HTML baru dengan nama register.html
    4) dalam urls.py import -> from main.views import register
    5) tambahkan path register
    Login:
    1) dalam view.py import -> from django.contrib.auth import authenticate, login
    2) tambahkan fungsi login_user
    3) buat HTML baru dengan nama login.html
    4) dalam urls.py import -> from main.views import login_user
    5) tambahkan path login
    Logout:
    1) dalam views.py import -> from django.contrib.auth import logout
    2) tambahkan fungsi logout_user
    3) tambah HTML di main.html di bawah add new product
    4) dalam urls.py import -> from main.views import logout_user
    5) tambahkan path logout
    Cookies:
    1) dalam views.py import -> import datetime, from django.http import HttpResponseRedirect, from django.urls import reverse
    2) mengganti kode pada fungsi login_user
    3) mengubah kode pada fungsi logout_user
    4) tambahkan potongan kode pada HTML
    Menghubungkan product dengan user:
    1) pada models.py import -> from django.contrib.auth.models import User
    2) tambahkan class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    3) mengubah potongan kode pada fungsi create_product
    4) mengubah fungsi show_main



# TUGAS 5
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
   Element selector adalah salah satu jenis selektor dalam CSS yang digunakan untuk memilih elemen HTML berdasarkan nama elemennya. Penggunaan element selector sifatnya sederhana dan mudah dimengerti secara anda hanya perlu menentukan nama elemen yang ingin Anda gayakan. Selain itu, penggunaan global dalam element selector dapat mengubah tampilan semua elemen dengan nama yang sama secara global di seluruh halaman web Anda. Element selector juga mengikuti aturan semantik secara element selector membantu menjaga struktur dan semantik HTML Anda tetap utuh. Element selector digunakan pada saat mengaplikasikan gaya global pada elemen-elemen dasar di seluruh halaman web.
   
2. Jelaskan HTML5 Tag yang kamu ketahui.
   a. <header> digunakan untuk mendefinisikan bagian atas dari suatu elemen. Biasanya digunakan untuk menyertakan elemen seperti judul situs, logo, dan elemen navigasi di bagian atas halaman.
   b. <nav> digunakan untuk mengelompokkan elemen-elemen yang berhubungan dengan navigasi di dalam dokumen.
   c. <main> digunakan untuk mendefinisikan konten utama yang ada di dalam dokumen/elemen HTML.
   d. <section> digunakan untuk mengelompokkan konten terkait dalam dokumen/elemen.
   e. <footer> digunakan untuk mendefinisikan bagian bawah atau kaki dari suatu elemen atau bagian dalam dokumen.

3. Jelaskan perbedaan antara margin dan padding.
  Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya sedangkan padding digunakan untuk mengatur jarak antara konten elemen dan batas atau tepi elemen itu sendiri.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
   Bootstrap digunakan pada saat anda ingin membuat website dengan cepat seperti proyek - proyek kecil dan jika anda tidak memiliki banyak waktu untuk mendesign.
   Tailwind digunakan pada saat anda ingin membuat website dengan tingkat kustomisasi yang tinggi dalam desain tampilan Anda dan jika Anda siap untuk menghabiskan waktu membangun tampilan Anda dari nol.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - buat folder static untuk menyimpan image, css, dan js (sediakan 3 custom css untuk 3 html yang berbeda)
   - buat elemen - elemen dengan classnya masing2 sesuai dengan kode yag kemarin untuk mempermudah mendesign website pada css
   - sertakan tag html untuk deskripsi produk, dll
   - implementasi 3 css pada 3 html



# TUGAS 6
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming mengeksekusi tugas - tugas secara bersamaan atau dalam urutan yang berbeda tanpa menghentikan eksekusi program utama.
Synchronous programming mengeksekusi tugas-tugas secara satu per satu dalam urutan tertentu. Saat tugas tertentu sedang berjalan, program akan "menghentikan" eksekusi sampai tugas tersebut selesai.
   
3. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah suatu pendekatan dalam mengembangkan perangkat lunak di mana program merespons events yang terjadi, seperti interaksi pengguna, masukan pengguna, atau perubahan status.
Contoh penerapan paradigma event-driven programming adalah klik tombol (ketika kita membuat sebuah tombol di halaman web dengan javascript, kita dapat menetapkan fungsi yang akan dijalankan ketika tombol tersebut diklik) dan AJAX request (dalam penggunaan AJAX, kita mengirimkan permintaan HTTP asinkron ke server dan menentukan fungsi yang akan dijalankan ketika respons dari server diterima)

5. Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX:
a) asynchronous request handling
Ketika Anda menggunakan AJAX untuk mengirim permintaan ke server, Anda dapat mengatur permintaan tersebut sebagai asinkron. Ini berarti bahwa program JavaScript akan melanjutkan eksekusi tanpa menunggu respons dari server.
b) event handling
Setelah Anda mengirim permintaan asinkron, Anda juga dapat mengatur event listener untuk menangani respons ketika server mengirimkan data kembali.
c) callback functions
Anda dapat menentukan fungsi yang akan dipanggil ketika respons dari server sudah tersedia. Ini memungkinkan Anda untuk merespons data yang diterima secara asinkron dan melakukan tindakan yang sesuai, seperti pembaruan antarmuka pengguna.

7. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
a) jQuery merupakan pustaka yang kompatibel dengan sebagian besar browser yang sudah lama digunakan dalam pengembangan web. Sedangkan, Fetch API hanya kompatibel dengan mayoritas browser modern sehingga ada beberapa browser lama yang mungkin sudah tidak kompatibel lagi.
b) Fetch API merupakan bagian dari JavaScript sehingga kerjanya lebih ringan dan lebih baik daripada jQuery.
c) Fetch API memiliki sintaks yang lebih modern dan sederhana daripada jQuery. 
d) Fetch API memiliki kapasitas memory yang lebih kecil daripada jQuery.
e) jQuery memiliki lebih banyak plugin dan ekstensi yang siap pakai daripada Fetch API.
f) jQuery tidak memiliki banyak maintenance daripada Fetch API yang memerlukan banyak pengubahan.

8. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a) buat fungsi baru pada views.py dengan nama get_product_json dan add_product_ajax yang menerima parameter request.
b) impor from django.views.decorators.csrf import csrf_exempt di berkas views.py.
c) tambahkan @csrf_exempt di atas fungsi add_product_ajax
d) impor fungsi get_product_json serta add_product_ajax di urls.py dan tambahkan pathnya
e) hapus kode table yang tugas kemarin lalu tambahkan kode "<table id="product_table"></table>" di kolom table
f) buat block <Script> di bagian bawah berkas dan buat fungsi baru bernama getProducts() pada block <Script>
g) buat fungsi baru pada block <Script> dengan nama refreshProducts()
h) tambahkan kode pada bootstrap dan tambahkan kode button
i) buat fungsi baru pada block <Script> dengan nama addProduct()
