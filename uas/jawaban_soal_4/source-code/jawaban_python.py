import sqlite3

# Membuat koneksi ke database (atau membuat database baru jika tidak ada)
conn = sqlite3.connect('contoh_database.db')

# Membuat cursor untuk mengeksekusi perintah SQL
cursor = conn.cursor()

# Menghapus data yang ada sebelum membuat tabel baru
cursor.execute('DROP TABLE IF EXISTS pengguna')

# Membuat tabel baru
cursor.execute('''
    CREATE TABLE pengguna (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        umur INTEGER NOT NULL
    )
''')

# Menyisipkan data ke dalam tabel
cursor.execute('''
    INSERT INTO pengguna (nama, umur) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
    INSERT INTO pengguna (nama, umur) VALUES (?, ?)
''', ('Bob', 25))

# Menyimpan perubahan
conn.commit()

# Mengambil dan menampilkan data dari tabel
cursor.execute('SELECT * FROM pengguna')
data = cursor.fetchall()
print("Data dari tabel pengguna:")
for row in data:
    print(row)

# Menutup koneksi
conn.close()
