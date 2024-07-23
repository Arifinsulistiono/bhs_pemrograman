# Fungsi untuk melakukan pembagian dengan penanganan eksepsi
def bagi(angka1, angka2):
    try:
        hasil = angka1 / angka2
    except ZeroDivisionError:
        return "Kesalahan: Tidak dapat membagi dengan nol."
    except TypeError:
        return "Kesalahan: Masukan harus berupa angka."
    else:
        return f"Hasil: {hasil}"
    finally:
        print("Eksekusi blok 'try-except' selesai.")

# Memanggil fungsi dengan argumen valid
print(bagi(10, 2))

# Memanggil fungsi dengan argumen pembagian nol
print(bagi(10, 0))

# Memanggil fungsi dengan argumen tipe yang salah
print(bagi(10, "a"))
