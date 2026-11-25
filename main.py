
# ==========================================
# APLIKASI ASURANSI NASABAH
# Konsep: OOP, Inheritance, Encapsulation,
# Constructor, dan Association
# ==========================================


# ==========================================
# 1. SUPERCLASS NASABAH
# ==========================================

class Nasabah:

    def __init__(self, id_nasabah, nama, umur):
        # Atribut private (Encapsulation)
        self.__id_nasabah = id_nasabah
        self.__nama = nama
        self.__umur = umur
        self.__daftar_polis = []

    # Getter
    def get_id(self):
        return self.__id_nasabah

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_daftar_polis(self):
        return self.__daftar_polis

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_umur(self, umur):
        self.__umur = umur

    # Method tambahan 1
    def tambah_polis(self, polis):
        self.__daftar_polis.append(polis)

    # Method tambahan 2
    def tampilkan_data(self):
        print("ID Nasabah :", self.__id_nasabah)
        print("Nama       :", self.__nama)
        print("Umur       :", self.__umur)


# ==========================================
# 2. SUBCLASS NASABAH KESEHATAN
# ==========================================

class NasabahKesehatan(Nasabah):

    def __init__(self, id_nasabah, nama, umur,
                 jenis_perlindungan, premi, kamar):

        super().__init__(id_nasabah, nama, umur)

        self.__jenis_perlindungan = jenis_perlindungan
        self.__premi = premi
        self.__kamar = kamar

    # Method tambahan 1
    def ubah_perlindungan(self, jenis):
        self.__jenis_perlindungan = jenis

    # Method tambahan 2
    def hitung_premi_tahunan(self):
        return self.__premi * 12

    # Getter
    def get_premi(self):
        return self.__premi

    def get_jenis_perlindungan(self):
        return self.__jenis_perlindungan

    def get_kamar(self):
        return self.__kamar

    # Override method superclass
    def tampilkan_data(self):
        print("\n=== NASABAH ASURANSI KESEHATAN ===")
        super().tampilkan_data()
        print("Perlindungan :", self.__jenis_perlindungan)
        print("Premi/Bulan  : Rp", self.__premi)
        print("Kelas Kamar  :", self.__kamar)


# ==========================================
# 3. SUBCLASS NASABAH JIWA
# ==========================================

class NasabahJiwa(Nasabah):

    def __init__(self, id_nasabah, nama, umur,
                 ahli_waris, uang_pertanggungan, premi):

        super().__init__(id_nasabah, nama, umur)

        self.__ahli_waris = ahli_waris
        self.__uang_pertanggungan = uang_pertanggungan
        self.__premi = premi

    # Method tambahan 1
    def ubah_ahli_waris(self, nama):
        self.__ahli_waris = nama

    # Method tambahan 2
    def hitung_total_pertanggungan(self):
        return self.__uang_pertanggungan

    # Getter
    def get_ahli_waris(self):
        return self.__ahli_waris

    def get_uang_pertanggungan(self):
        return self.__uang_pertanggungan

    def get_premi(self):
        return self.__premi

    # Override method superclass
    def tampilkan_data(self):
        print("\n=== NASABAH ASURANSI JIWA ===")
        super().tampilkan_data()
        print("Ahli Waris   :", self.__ahli_waris)
        print("Uang Jaminan : Rp", self.__uang_pertanggungan)
        print("Premi/Bulan  : Rp", self.__premi)


# ==========================================
# 4. CLASS POLIS (ASSOCIATION)
# ==========================================

class Polis:

    def __init__(self, nomor_polis, jenis_polis,
                 premi, pemilik):

        self.__nomor_polis = nomor_polis
        self.__jenis_polis = jenis_polis
        self.__premi = premi
        self.__status = "Aktif"
        self.__pemilik = pemilik

    # Getter
    def get_nomor(self):
        return self.__nomor_polis

    def get_status(self):
        return self.__status

    def get_pemilik(self):
        return self.__pemilik

    # Method tambahan 1
    def ubah_status(self, status):
        self.__status = status

    # Method tambahan 2
    def tampilkan_polis(self):
        print("Nomor Polis :", self.__nomor_polis)
        print("Jenis Polis :", self.__jenis_polis)
        print("Premi       : Rp", self.__premi)
        print("Status      :", self.__status)
        print("Pemilik     :", self.__pemilik.get_nama())


# ==========================================
# 5. MAIN PROGRAM / MENU CLI
# ==========================================

daftar_nasabah = []
nomor_polis = 1


def tambah_nasabah():
    global nomor_polis

    print("\n=== TAMBAH NASABAH ===")

    id_nasabah = input("Masukkan ID Nasabah : ")

    # Validasi ID agar tidak duplikat
    for nasabah in daftar_nasabah:
        if nasabah.get_id() == id_nasabah:
            print("ID Nasabah sudah digunakan!")
            return

    nama = input("Nama Nasabah : ")

    try:
        umur = int(input("Umur : "))
        if umur <= 0:
            print("Umur harus lebih dari 0!")
            return
    except ValueError:
        print("Umur harus berupa angka!")
        return

    print("\nJenis Asuransi:")
    print("1. Asuransi Kesehatan")
    print("2. Asuransi Jiwa")

    pilihan = input("Pilih jenis asuransi : ")

    if pilihan == "1":

        perlindungan = input("Jenis Perlindungan : ")
        kamar = input("Kelas Kamar : ")

        try:
            premi = int(input("Premi Per Bulan : Rp"))
            if premi <= 0:
                print("Premi harus lebih dari 0!")
                return
        except ValueError:
            print("Premi harus berupa angka!")
            return

        nasabah = NasabahKesehatan(
            id_nasabah, nama, umur,
            perlindungan, premi, kamar
        )

        jenis = "Kesehatan"

    elif pilihan == "2":

        ahli_waris = input("Nama Ahli Waris : ")

        try:
            uang = int(input("Uang Pertanggungan : Rp"))
            premi = int(input("Premi Per Bulan : Rp"))

            if uang <= 0 or premi <= 0:
                print("Nominal harus lebih dari 0!")
                return

        except ValueError:
            print("Nominal harus berupa angka!")
            return

        nasabah = NasabahJiwa(
            id_nasabah, nama, umur,
            ahli_waris, uang, premi
        )

        jenis = "Jiwa"

    else:
        print("Pilihan tidak tersedia!")
        return

    # Membuat objek Polis dengan pemilik Nasabah
    polis = Polis(
        "PLS" + str(nomor_polis),
        jenis,
        nasabah.get_premi() if isinstance(
            nasabah, NasabahJiwa
        ) else nasabah.get_premi(),
        nasabah
    )

    # Association: polis dimiliki nasabah
    nasabah.tambah_polis(polis)

    daftar_nasabah.append(nasabah)

    nomor_polis += 1

    print("\nNasabah berhasil ditambahkan!")


def tampilkan_nasabah():

    print("\n=== DAFTAR NASABAH ===")

    if len(daftar_nasabah) == 0:
        print("Belum ada data nasabah.")
        return

    for nasabah in daftar_nasabah:

        nasabah.tampilkan_data()

        print("\nData Polis:")

        for polis in nasabah.get_daftar_polis():
            polis.tampilkan_polis()

        print("-" * 35)


def cari_nasabah():

    print("\n=== CARI NASABAH ===")

    id_cari = input("Masukkan ID Nasabah : ")

    for nasabah in daftar_nasabah:

        if nasabah.get_id() == id_cari:

            print("\nData ditemukan!")
            nasabah.tampilkan_data()

            for polis in nasabah.get_daftar_polis():
                polis.tampilkan_polis()

            return

    print("Nasabah tidak ditemukan!")


def ubah_nasabah():

    print("\n=== UBAH DATA NASABAH ===")

    id_cari = input("Masukkan ID Nasabah : ")

    for nasabah in daftar_nasabah:

        if nasabah.get_id() == id_cari:

            nama_baru = input("Masukkan Nama Baru : ")
            nasabah.set_nama(nama_baru)

            print("Data nasabah berhasil diubah!")
            return

    print("Nasabah tidak ditemukan!")


def cek_status():

    print("\n=== CEK STATUS POLIS ===")

    nomor = input("Masukkan Nomor Polis : ")

    for nasabah in daftar_nasabah:

        for polis in nasabah.get_daftar_polis():

            if polis.get_nomor() == nomor:

                print("\nPolis ditemukan!")
                polis.tampilkan_polis()
                return

    print("Polis tidak ditemukan!")


# ==========================================
# MENU UTAMA
# ==========================================

while True:

    print("\n================================")
    print("    APLIKASI ASURANSI NASABAH")
    print("================================")
    print("1. Tambah Data Nasabah")
    print("2. Tampilkan Data Nasabah")
    print("3. Cari Data Nasabah")
    print("4. Ubah Data Nasabah")
    print("5. Cek Status Polis")
    print("6. Keluar")
    print("================================")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        tambah_nasabah()

    elif pilihan == "2":
        tampilkan_nasabah()

    elif pilihan == "3":
        cari_nasabah()

    elif pilihan == "4":
        ubah_nasabah()

    elif pilihan == "5":
        cek_status()

    elif pilihan == "6":
        print("Terima kasih telah menggunakan aplikasi!")
        break

    else:
        print("Pilihan tidak valid!")
