Nama: Ahmad Aimar Refaldi Ramang
NIM: 2609116056
Kelas: B 2026


DESKRIPSI SINGKAT

Program Data Poin Tim M7 adalah sebuah program yang dibuat dengan Python dan digunakan untuk mengelola data poin dari berbagai tim dalam sebuah klasemen. Program ini memiliki fitur login dan dua jenis peran, yaitu admin dan user. Admin bisa melakukan semua hal, seperti menampilkan, menambah, mengubah, dan menghapus data tim. Sementara user hanya bisa melihat data tim saja.
Program ini menggunakan dictionary untuk menyimpan informasi akun dan data tim. Untuk menjaga struktur program tetap baik, beberapa fungsi digunakan untuk menjalankan setiap proses. Ada juga validasi input yang diterapkan agar data yang dimasukkan sesuai, misalnya poin harus berupa angka dan nama tim tidak boleh kosong.
Program ini juga menggunakan tiga library. Pertama, os digunakan untuk membersihkan layar. Kedua, time digunakan untuk memberikan jeda pada program. Ketiga, pwinput digunakan agar password tidak terlihat saat login. Jika pengguna memilih menu keluar, program akan mencari tim dengan poin tertinggi dan menampilkan tim tersebut sebagai pemenang sebelum berhenti.


<img width="1969" height="1112" alt="Flowchart Sistem Klasemen Tim Esport Turnamen MLBB drawio" src="https://github.com/user-attachments/assets/9b58ff51-0bac-431b-8967-cde75b50bea0" />

Flowchart ini menunjukkan bagaimana program Data Poin Tim M7 bekerja, mulai dari saat login sampai akhir ketika pemenang ditampilkan. Itulah alur kerja yang mudah diikuti.
Langkah pertama, pengguna mengetik username dan password. Bila login salah, program langsung beri pesan error dan kembali ke halaman login. Bila login benar, program cek apakah pengguna adalah admin atau user. Setiap langkah dipastikan benar sebelum berlanjut. Admin punya menu untuk melihat data tim, menambah tim, mengubah poin, menghapus tim, atau keluar. Sedangkan user hanya bisa melihat data tim atau keluar dari program. Setiap pilihan diproses sesuai menu yang dipilih, dan bila pilihan tidak sesuai, program beri pesan error. Menu ini membantu admin mengelola tim dengan mudah, sementara user hanya melihat data.Saat pengguna memilih keluar, program menampilkan tim dengan poin tertinggi sebagai pemenang, lalu program selesai. 
Itulah cara program ini menutup dengan menampilkan pemenang.



<img width="529" height="958" alt="Screenshot 2026-10-06 213326" src="https://github.com/user-attachments/assets/b86a8eb8-aee1-4352-b179-000eaa9a082f" />

<img width="480" height="366" alt="Screenshot 2026-10-06 213350" src="https://github.com/user-attachments/assets/71e98e52-c65a-4421-9f7e-c6825aa65686" />

<img width="492" height="966" alt="Screenshot 2026-10-06 213341" src="https://github.com/user-attachments/assets/52309d0a-26e3-4bff-87ac-c85162d11b3c" />

Output yang dihasilkan menunjukkan bahwa program Data Poin Tim M7 berjalan dengan baik. Program dimulai dengan login memakai akun admin. Setelah username dan password benar, sistem memberi akses sebagai admin supaya pengguna dapat mengelola data tim. Pada awal, admin memilih menu Tampilkan Data untuk melihat daftar tim dan poinnya. Lalu, admin menambahkan tim EVOS dan memberi 10 poin. Setelah itu, admin mengubah poin ONIC dari 0 menjadi 7 poin. Kemudian, admin menghapus tim CG Esports. Setelah data dihapus, admin menampilkan kembali daftar tim untuk memastikan CG Esports tidak ada lagi. Terakhir, admin memilih menu Keluar. Sebelum program berhenti, sistem mencari tim dengan poin tertinggi. Hasilnya, EVOS menjadi pemenang dengan 10 poin, karena poinnya paling tinggi dibandingkan tim lain. Setelah pemenang ditampilkan, program menampilkan pesan “Program selesai.” dan berhenti. Dengan demikian, output menunjukkan bahwa fitur login, hak akses admin, menampilkan data, menambah data, mengubah data, menghapus data, dan menentukan pemenang berhasil dijalankan.


<img width="539" height="581" alt="Screenshot 2026-10-06 213433" src="https://github.com/user-attachments/assets/d41373c2-0b45-4565-a38c-5532c50b81b3" />

Pengguna berhasil masuk ke sistem dengan akun yang memiliki peran user. Setelah login, program menampilkan menu khusus untuk user, yang hanya memiliki dua pilihan: menampilkan data dan keluar. Pengguna memilih opsi 1 untuk melihat daftar tim beserta poin yang dimiliki masing-masing. Kemudian, pengguna memilih opsi 2 untuk keluar dari program. Sebelum program berhenti, sistem menjalankan proses penampilan hasil akhir dan mencari pemenang. Karena semua tim masih memiliki poin nol, tidak ada nama pemenang yang ditampilkan. Hanya angka poin 0 yang muncul. Setelah itu, program menampilkan pesan “Program selesai.” Gambar ini menunjukkan bahwa pengguna dengan role user memiliki akses yang lebih terbatas dibandingkan admin


<img width="441" height="451" alt="Screenshot 2026-10-06 213505" src="https://github.com/user-attachments/assets/2d578520-59b8-4c14-a2a6-b2f8b18a0d2e" />

Pengguna berhasil masuk menggunakan akun admin. Setelah masuk, tampilan program menampilkan menu admin yang terdiri dari lima pilihan, yaitu menampilkan data, menambah tim, mengubah poin, menghapus tim, dan keluar. Pengguna kemudian memasukkan angka 10, padahal pilihan yang tersedia hanya dari 1 hingga 5. Program mengenali bahwa pilihan tersebut tidak ada dan menampilkan pesan “Pilihan tidak tersedia.” Setelah itu, program menampilkan kembali menu dan meminta pengguna memasukkan pilihan lagi. Gambar ini menunjukkan bahwa program dilengkapi dengan sistem validasi untuk mencegah pengguna memasukkan pilihan yang salah.


<img width="397" height="132" alt="Screenshot 2026-10-06 213552" src="https://github.com/user-attachments/assets/2e09ab48-7d8d-451e-83dc-c062b67409ec" />

Pengguna mencoba masuk ke dalam program dengan memasukkan username 123. Ternyata username itu tidak ada di dalam data akun. Maka program menampilkan pesan “Username tidak ditemukan.” dan “Silakan coba login lagi.” Program tetap berada di proses login dan terus meminta pengguna untuk memasukkan akun yang benar. Gambar ini menunjukkan bahwa program bisa menangani kesalahan username. Program juga bisa melakukan pengulangan login sampai pengguna berhasil masuk.





