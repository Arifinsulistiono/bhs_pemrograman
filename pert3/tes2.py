# Definisikan fungsi kalkulator
def kalkulator():
    print("=== Kalkulator Sederhana ===")
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Pilih operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Pembagian dengan nol tidak valid.")
            return

    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")

# Program Utama
while True:
    kalkulator()
    ulang = input("Apakah Anda ingin mengulang perhitungan? (ya/tidak): ")
    if ulang.lower() != 'ya':
        print("Terima kasih telah menggunakan kalkulator.")
        break
