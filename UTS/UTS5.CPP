#include <iostream>
using namespace std;

int main() {
    // Deklarasi variabel untuk menyimpan angka pertama dan kedua
    int angkaPertama, angkaKedua;
    
    // Meminta input dari pengguna untuk angka pertama
    cout << "Masukan angka pertama :";
    cin >> angkaPertama;

    // Meminta input dari pengguna untuk angka kedua
    cout << "Masukan angka kedua   :";
    cin >> angkaKedua;

    // Melakukan operasi aritmatika
    int penjumlahan = angkaPertama + angkaKedua;
    int pengurangan = angkaPertama - angkaKedua;
    int perkalian = angkaPertama * angkaKedua;
    float pembagian = static_cast<float>(angkaPertama) / angkaKedua;

    // Menampilkan hasil operasi aritmatika
    cout << "Penjumlahan   :" << penjumlahan << endl;
    cout << "Pengurangan   :" << pengurangan << endl;
    cout << "Perkalian     :" << perkalian << endl;
    cout << "Pembagian     :" << pembagian << endl;

    return 0;
}
