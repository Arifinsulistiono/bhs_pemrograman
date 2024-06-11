# 1. Definisi

Array (dalam bahasa python) adalah struktur yang dapat menyimpan dan mengatur kumpulan data. Struktur data berbicara tentang cara menyimpan, mengatur, mengelompokkan, dan merepresentasikan data. Struktur data sangat penting dan harus dikuasai oleh seorang programmer. Di forum-forum pemrograman, saya sering menemukan pertanyaan yang menurut saya dapat dipecahkan jika orang tersebut memahami konsep struktur data.

Dalam materi ini, kita akan membahas struktur data tingkat lanjut, yaitu set dan dictionary.

# 2. Set

Set dalam bahasa pemrograman python adalah tipe data kolektif yang digunakan untuk menyimpan beberapa nilai dalam satu variabel dengan ketentuan sebagai berikut:

a. Nilai anggota yang disimpan harus unik (tidak duplikat)

b. Nilai anggota yang telah dimasukkan tidak dapat diubah lagi

c. Set bersifat unordered alias tidak berurutan, yang berarti tidak dapat diakses berdasarkan indeks.

Untuk lebih memahami 3 poin di atas, kita akan langsung melakukan latihan.
Bentuk umum Himpunan:

# gunakan kurung kurawal
student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'} print(student_set)
print(student_set)

# ubah daftar menjadi himpunan
fruit_set = set(['mango', 'Apple']) print(set_fruit)
print(set_fruit)

# himpunan dengan tipe data berbeda
set_mix = {'man', 'animal', 5, True, ('A', 'B')}
print(set_mix)

Hasil:
{'Wahid', 'Lendis', 'Basith', 'Huda'}
{'apel', 'mangga'}
(True, 5, ('A', 'B'), 'hewan', 'manusia'}

# a. Tidak Berurut (Himpunan)
Tipe himpunan data tidak berurut. Artinya, kita tidak dapat menggunakan indeks untuk mengakses nilai error: di set. Bahkan jika kita memaksa, kita hanya akan mendapatkan

my_set = {'a'}
print(my_set[8])

Pesan error:
Traceback (panggilan terakhir paling baru):
File "<stdin>", baris 1, di <module>
TypeError: objek 'set' tidak dapat disubskrip

Kita juga dapat melihat kode program yang kita buat sebelumnya:
student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'} print(student_set)

Output:
"Wahid", "Lendis", "Basith", "Huda"}

# b. Tidak dapat diubah (Set)
Set tidak dapat diubah, artinya nilai yang telah kita masukkan ke dalam set tidak dapat diubah lagi.
Namun, kita masih dapat menambahkan dan menghapus anggota ke dalam set. Dan, karena set tidak dapat diubah, maka set hanya dapat menerima anggota dari tipe data yang juga tidak dapat diubah.

Pertimbangkan contoh berikut:
# anggota set harus bertipe data yang tidak dapat diubah
set_fruit = { 'mangga', 'lemon', 'alpukat', True, 1, 2, 3 }
# kita dapat menjadikan tuple sebagai anggota
# karena tidak dapat diubah 
keyboard_= {
(1, 2, 3), (4, 5, 6),
(7, 8, 9),}

Tetapi kita tidak dapat menyertakan list sebagai anggota karena list dapat diubah. Pertimbangkan contoh berikut:

x = set{ 35, 100, ['a', 'b'] }

Pesan kesalahan:

Traceback (panggilan terakhir paling baru):
 File "<stdin>", baris 1, di <module> 
 TypeError: unhashable type: 'list'
# c. Tidak Ada Nilai Duplikat
(Set)
Set dalam python juga tidak dapat menerima nilai duplikat. Jika kita memasukkan nilai yang sudah ada dalam satu set, maka nilai tersebut hanya akan muncul atau dimasukkan satu kali. Perhatikan contoh berikut:
unique_word = {
'pagi', 'ini', 'adalah', 'pagi', 'yang',
'sangat', 'cerah'}
print(unique_word)
Maka kata "pagi" hanya akan dimasukkan satu kali:
{'itu', 'sangat', 'ini', 'pagi', 'cerah', 'adalah')

# d. Menambahkan/Memperbarui Elemen Set
Seperti yang telah disebutkan di atas bahwa meskipun nilai set tidak dapat diubah, nilai tersebut masih dapat ditambahkan dan dihapus. Kita dapat menambahkan anggota baru ke set dengan fungsi add() dan update(). Perhatikan contoh berikut:
alphabet_set = {'a', 'b', 'c'} 
print(alphabetical set)

# tambahkan satu per satu 
set_abjad.add('d') 
set_abjad.add('e')

# tambahkan lebih dari satu anggota sekaligus 
set_abjad.update({ 'f', 'g' })
 # bisa juga menggunakan daftar 
set_abjad.update(['h', 'i'])
print(alphabetical set)
Keluaran: 
('a', 'c', 'b'} ('d', '', 'e',
'b', 'g', 'h', 'f', 'c'}

# e. Hapus/hilangkan Elemen Set
Untuk menghapus anggota dari suatu set, ada 4 fungsi yang dapat kita gunakan:
a.remove(value) Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, maka akan terjadi kesalahan.
b. discard(value) Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, tidak akan ada kesalahan.
c. pop() Mengambil dan menghapus nilai di sebelah kiri. .clear() Menghapus semua anggota.
contoh:

set = {'virtual', 'virtuous', 100, ('a', 'b'), false, True} print (set)


# will error if the value 100 is not in the set
set.remove(100)
print(set)
# will not error if ('a', 'b') is not in the set set.discard (('a', 'b')) print(set)
# remove the value on the left Removedvalue = set.pop()
print('Removed value =', valueDeleted) print(set)
# delete all values set.clear() print(set)
Outputs: Universitas
(False, True, 100, 'maya', 'budi', ('a', 'b')}
(False, True, 'maya', 'budi', ('a', 'b'))
(False, True, 'maya', 'budi'}
nilaiYangDihapus = False (True, 'maya', 'budi'}
set()
nggul
add()
f. Functions (Sets)
The following is a summary of the built-in functions of the data set type that we can use:
|  Function  |               Utility             |
| :--------: | :-----------------------------:   |
|add()       |Menambahkan satu anggota ke set    |
|clear()     |Menghapus seluruh set              |