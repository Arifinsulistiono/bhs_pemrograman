import tkinter as tk
from tkinter import messagebox

# Membuat instance dari Tkinter
root = tk.Tk()

# Mengatur judul jendela
root.title("Contoh GUI dengan Tkinter")

# Mengatur ukuran jendela
root.geometry("300x200")

# Fungsi yang akan dipanggil saat tombol ditekan
def tombol_ditekan():
    messagebox.showinfo("Informasi", "Tombol telah ditekan!")

# Membuat tombol dan menempatkannya di jendela utama
tombol = tk.Button(root, text="Tekan Saya", command=tombol_ditekan)
tombol.pack(pady=20)

# Menjalankan loop utama Tkinter
root.mainloop()
