---->Penjelasan latihan1.py, latihan2.py, dan program1.py

--> Penjelasan Latihan1.py(Menampilkan bilangan secara acak)

Source Code dari latihan1.py: 

![1](https://user-images.githubusercontent.com/46509513/52943413-aa361b00-339f-11e9-8470-c70252b3dce4.png)

Penjelasan alur program : 
1. Import random digunakan untuk memasukkan modul random ke dalam program latihan1.py. Karena nantinya kita akan menggunakan fungsi random untuk menampilkan jumlah ke-N(Jumlah diinputkan oleh user misalnya nilai N adalah 10 maka akan menampilkan bilangan acak sebanyak 10x).
2. Pada line ke-3 user diminta menginputkan bilangan yang mereka inginkan untuk mengisi nilai N.
3. Untuk line ke-4 itu hanya untuk penomoran saja nantinya.
4. Line ke-5 itu merupakan fungsi for atau bisa dibilang fungsi perulangan. 
->For x in range(0,n)
->X adalah index dari perulangan tersebut.
->Range(0,n) artinya dimulai dari 0 sampai N(Inputan user, misalnya inputannya adalah 10 maka dimulai 0 sampai dengan 10).
5. Line ke-6 nilai i akan menampung bilangan secara acak diantara 0,0 sampai dengan 0,5.
6. Untuk a+=1 ini untuk penomoran nantinya.
7. Untuk Line ke-8, akan menampilkan hasil bilangan yang telah dipilih secara acak pada variabel i tadi.

Hasil eksekusi dari program : 

![output1](https://user-images.githubusercontent.com/46509513/52944608-64c71d00-33a2-11e9-82c4-a550d66f21e8.png)

--> Penjelasan Latihan2.py(Mencari Nilai Terbesar/Max Value)

Source Code dari latihan2.py: 

![2](https://user-images.githubusercontent.com/46509513/52945040-68a76f00-33a3-11e9-960e-851e3303d5b2.png)

Penjelasan Alur Program :
1. Pertama kita akan membuat sebuah variabel penampung nilai max. Untuk awal nilai max akan kita isikan 0 nantinya nilai max ini akan terganti bila ada yang lebih besar dari nilai max awal.
2. Perintah while True merupakan perintah yang digunakan secara terus menerus,  selama perulangan itu bernilai True maka program akan berjalan terus sampai menemukan nilai False.
3. Selanjutnya user akan diminta untuk menginputkan nilai.
4. Pada line ke-4, Jika nilai Max awal itu lebih kecil dari nilai B maka nilai max yang sekarang akan menjadi nilai B. Begitu pun untuk selanjutnya jika terjadi perulangan secara terus menerus.
5. Tapi jika user menginputkan nilai B sama dengan 0 maka perulangan akan berhenti. Karena apa ? Nilai 0 itu bisa dikatakan sebagai nilai False artinya perulangan akan terhenti karena adanya nilai False dalam perulangan tersebut.
6. Terakhir Program akan menampilkan nilai Terbesar diantara banyaknya nilai yang telah diinputkan sebelumnya.

Hasil eksekusi dari program : 

![output2](https://user-images.githubusercontent.com/46509513/52945633-c092a580-33a4-11e9-94eb-3ee1ab777315.png)

-->Penjelasan program1.py

Source Code dari program1.py : 

![3](https://user-images.githubusercontent.com/46509513/52945829-3991fd00-33a5-11e9-82c5-1ea3f15072db.png)

Sebelum kita ke penjelasan program ini memiliki soal yaitu: 
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100juta,  pada bulan pertama dan kedua belum mendaptkan laba. Pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.

Penjelasan Alur program : 
1. Untuk pertama kita akan memasukan modal awal 100juta kedalam variabel a.
2. Disini kita akan melakukan perulangan dimulai dari 1 sampai dengan 9. 
3. Pada line ke-3, jika nilai x lebih dari sama dengan 1 Dan kurang dari sama dengan 2 maka menampilkan hasil dari laba bulan 1 dan 2. nilai B sebagai laba bulan ke1 dan ke2.
4. Pada line ke-6, jika nilai x lebih dari sama dengan 3 Dan kurang dari sama dengan 4 maka menampilkan hasil dari laba bulan 3 dan 4. nilai C sebagai laba bulan ke3 dan ke4.
5. Pada line ke-9, jika nilai x lebih dari sama dengan 5 Dan kurang dari sama dengan 7 maka menampilkan hasil dari laba bulan 5 sampai dengan bulan ke-7. nilai D sebagai laba bulan ke-5, ke-6, dan ke-7.
6. Pada line ke-12, jika nilai x sama dengan 8 maka menampilkan hasil laba bulan 8. nilai E sebagai laba bulan ke-8.
7. Nilai Total adalah nilai dari jumlah seluruh laba bulan ke1 sampai dengan bulan ke8.
8. Terakhir menampilkan Total Laba.

Hasil eksekusi program :

![output3](https://user-images.githubusercontent.com/46509513/52948834-2aaf4880-33ad-11e9-90c6-1f7088e150f7.png)
