data_pasien = data_pasien = [
    {"id": 1, "nama": "Anto", "umur": 25, "penyakit": "Flu"},
    {"id": 2, "nama": "Ben", "umur": 30, "penyakit": "Demam"},
    {"id": 3, "nama": "Calvin", "umur": 22, "penyakit": "Batuk"},
    {"id": 4, "nama": "Doni", "umur": 28, "penyakit": "Asma"},
    {"id": 5, "nama": "Edo", "umur": 35, "penyakit": "Diabetes"}
]

# VALIDASI UMUR (0–100)
def input_umur(prompt):
    while True:
        try:
            umur = int(input(prompt))
            if umur < 0 or umur > 100:
                print("Umur harus antara 0 - 100!")
                continue
            return umur
        except ValueError:
            print("Input harus berupa angka (integer)!")

# VALIDASI ID (INTEGER + UNIQUE)
def input_id():
    while True:
        try:
            id_pasien = int(input("ID Pasien: "))
            if any(p["id"] == id_pasien for p in data_pasien):
                print("ID sudah digunakan! Masukkan ID lain.")
                continue
            return id_pasien
        except ValueError:
            print("ID harus berupa angka (integer)!")

# TAMPILKAN TABEL + SORTING ID
def tampilkan_tabel(data):
    if not data:
        print("Data kosong.")
        return

    # SORT BY ID
    data_sorted = sorted(data, key=lambda x: x["id"])

    print("\n=== DATA PASIEN ===")
    print("-" * 60)
    print(f"{'ID':<10} {'Nama':<15} {'Umur':<5} {'Penyakit':<20}")
    print("-" * 60)

    for p in data_sorted:
        print(f"{p['id']:<10} {p['nama']:<15} {p['umur']:<5} {p['penyakit']:<20}")

    print("-" * 60)

# CREATE
def tambah_pasien():
    print("\n=== Tambah Pasien ===")

    id_pasien = input_id()
    nama = input("Nama: ")
    umur = input_umur("Umur: ")
    penyakit = input("Penyakit: ")

    pasien = {
        "id": id_pasien,
        "nama": nama,
        "umur": umur,
        "penyakit": penyakit
    }

    data_pasien.append(pasien)
    print("Data berhasil ditambahkan!")

# READ
def tampilkan_pasien():
    tampilkan_tabel(data_pasien)

# UPDATE
def update_pasien():
    print("\n=== Update Pasien ===")
    try:
        id_pasien = int(input("Masukkan ID pasien: "))
    except ValueError:
        print("ID harus angka!")
        return

    for p in data_pasien:
        if p["id"] == id_pasien:
            p["nama"] = input("Nama baru: ")
            p["umur"] = input_umur("Umur baru: ")
            p["penyakit"] = input("Penyakit baru: ")
            print("Data berhasil diupdate!")
            return

    print("ID tidak ditemukan.")

# DELETE
def hapus_pasien():
    print("\n=== Hapus Pasien ===")
    try:
        id_pasien = int(input("Masukkan ID pasien: "))
    except ValueError:
        print("ID harus angka!")
        return

    for p in data_pasien:
        if p["id"] == id_pasien:
            data_pasien.remove(p)
            print("🗑️ Data berhasil dihapus!")
            return

    print("ID tidak ditemukan.")

# SEARCH
def cari_pasien():
    print("\n=== Cari Pasien ===")
    keyword = input("Masukkan nama: ").lower()

    hasil = [p for p in data_pasien if keyword in p["nama"].lower()]
    tampilkan_tabel(hasil)

# STATISTIK
def statistik():
    print("\n=== Statistik ===")
    print(f"Total pasien: {len(data_pasien)}")

# MENU
def menu():
    while True:
        print("\n=== SISTEM DATA PASIEN ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Pasien")
        print("3. Update Pasien")
        print("4. Hapus Pasien")
        print("5. Cari Pasien")
        print("6. Statistik")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            tampilkan_pasien()
        elif pilihan == "3":
            update_pasien()
        elif pilihan == "4":
            hapus_pasien()
        elif pilihan == "5":
            cari_pasien()
        elif pilihan == "6":
            statistik()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# RUN
menu()
