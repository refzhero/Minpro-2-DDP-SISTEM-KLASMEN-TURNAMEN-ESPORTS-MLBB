import os
import time
import pwinput

# DATA AKUN
akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

# DATA TIM
data_tim = {
    "ONIC": 0,
    "Alter Ego": 0,
    "Team Liquid PH": 0,
    "Aurora Gaming PH": 0,
    "Selangor Red Giants": 0,
    "CG Esports": 0
}

# FUNCTION MEMBERSIHKAN LAYAR
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

# FUNCTION LOGIN
def login():
    while True:
        bersihkan_layar()

        print("===== LOGIN DATA TIM M7 =====")

        username = input("Username : ")

        password = pwinput.pwinput("Password : ")

        if username in akun:
            if akun[username]["password"] == password:
                print("Login berhasil!")
                print("Role :", akun[username]["role"])

                time.sleep(1)

                return akun[username]["role"]
            else:
                print("Password salah.")

        else:
            print("Username tidak ditemukan.")

        print("Silakan coba login lagi.")

        time.sleep(1)

# FUNCTION TAMPILKAN DATA
def tampilkan_data():
    print("===== DAFTAR TIM M7 =====")

    if len(data_tim) == 0:
        print("Tidak ada data tim.")

    else:
        nomor = 1

        for nama, poin in data_tim.items():
            print(nomor, ".", nama, "-", poin, "poin")
            nomor += 1

# FUNCTION TAMBAH TIM
def tambah_tim():

    print("===== TAMBAH TIM =====")

    nama = input("Masukkan nama tim: ")

    if nama == "":
        print("Nama tim tidak boleh kosong.")
        return

    if nama in data_tim:
        print("Tim sudah terdaftar.")
        return

    poin = input("Masukkan poin: ")

    if not poin.isdigit():
        print("Poin harus berupa angka.")
        return

    poin = int(poin)

    if poin < 0:
        print("Poin tidak boleh negatif.")
        return

    data_tim[nama] = poin

    print("Tim berhasil ditambahkan.")

# FUNCTION UBAH POIN
def ubah_poin():

    print("===== UBAH POIN =====")

    nama = input("Masukkan nama tim: ")

    if nama not in data_tim:
        print("Tim tidak ditemukan.")
        return

    poin = input("Masukkan poin baru: ")

    if not poin.isdigit():
        print("Poin harus berupa angka.")
        return

    poin = int(poin)

    if poin < 0:
        print("Poin tidak boleh negatif.")
        return

    data_tim[nama] = poin

    print("Poin berhasil diubah.")

# FUNCTION HAPUS TIM
def hapus_tim():

    print("===== HAPUS TIM =====")

    nama = input("Masukkan nama tim: ")

    if nama not in data_tim:
        print("Tim tidak ditemukan.")
        return

    del data_tim[nama]

    print("Tim berhasil dihapus.")

# FUNCTION CARI PEMENANG
def pemenang():

    print("===== HASIL AKHIR M7 =====")

    if len(data_tim) == 0:
        print("Tidak ada data tim.")
        return

    tim_menang = ""
    poin_tertinggi = 0

    for nama, poin in data_tim.items():

        if poin > poin_tertinggi:
            poin_tertinggi = poin
            tim_menang = nama

    print("Pemenang:", tim_menang)
    print("Poin:", poin_tertinggi)

# PROGRAM MENU dan LOGIN
role = login()

if role is None:
    print("Program selesai.")
    bersihkan_layar()

else:
    while True:

        print("===== DATA POIN TIM M7 =====")

        print("Role:", role)
        print()

        if role == "admin":

            print("1. Tampilkan data")
            print("2. Tambah tim")
            print("3. Ubah poin")
            print("4. Hapus tim")
            print("5. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tampilkan_data()

            elif pilihan == "2":
                tambah_tim()

            elif pilihan == "3":
                ubah_poin()

            elif pilihan == "4":
                hapus_tim()

            elif pilihan == "5":
                print()
                pemenang()
                print()
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak tersedia.")

        elif role == "user":

            print("1. Tampilkan data")
            print("2. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tampilkan_data()

            elif pilihan == "2":
                print()
                pemenang()
                print()
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak tersedia.")

