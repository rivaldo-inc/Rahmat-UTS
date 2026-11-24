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

    print("\n=== Tambah Nasabah ===")

    id_nasabah = input("Masukkan ID Nasabah: ")

    #Validasi input ID agar tidak duplikat
    for nasabah in daftar_nasabah:
        if nasabah.get_id() == id_nasabah:
            print(" ID Nasabah sudah ada. Silakan gunakan ID lain.")
            return

       