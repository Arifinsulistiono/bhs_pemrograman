# Fungsi Sederhana
def sapa_pengguna(nama):
    """Fungsi sederhana untuk menyapa pengguna."""
    print(f"Selamat datang, {nama}!")

# Memanggil fungsi sederhana
sapa_pengguna("Budi")

print()  # Menambahkan baris kosong untuk pemisah output

# Fungsi Rekursif
def hitung_fibonacci(n):
    """Fungsi rekursif untuk menghitung angka Fibonacci ke-n."""
    if n <= 1:
        return n
    else:
        return hitung_fibonacci(n-1) + hitung_fibonacci(n-2)

# Memanggil fungsi rekursif dan menampilkan hasilnya
print(f"Fibonacci ke-7 adalah: {hitung_fibonacci(7)}")
