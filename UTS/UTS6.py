# Deklarasi fungsi-fungsi
def menu():
    print("=== Menu ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar")
    print("=============")

def tambah():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    print("Penjumlahan:", a + b)

def kurang():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    print("Pengurangan:", a - b)

def kali():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    print("Perkalian:", a * b)

def bagi():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    if b != 0:
        print("Pembagian:", a / b)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

# Main program
while True:
    menu()
    pilihan = input("Pilih operasi (1-4) atau 0 untuk keluar: ")

    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        kurang()
    elif pilihan == '3':
        kali()
    elif pilihan == '4':
        bagi()
    elif pilihan == '0':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
