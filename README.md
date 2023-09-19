# shopping-list
TUTORIAL 2
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
