#include <iostream>
using namespace std;

int main() {
    int tahunLahir, tahunSekarang, usia;
    
    // Asumsikan tahun sekarang adalah 2024
    tahunSekarang = 2024;
    
    // Meminta input dari pengguna
    cout << "Masukkan tahun kelahiran kalian: ";
    cin >> tahunLahir;
    
    // Menghitung usia
    usia = tahunSekarang - tahunLahir;
    
    // Menampilkan hasil
    cout << "Berarti usia kalian sekarang adalah " << usia << " tahun." << endl;
    
    return 0;
}
