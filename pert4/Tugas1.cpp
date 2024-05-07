#include <iostream>
using namespace std;

// Deklarasi fungsi-fungsi operasi
void tambah(double x, double y) {
    cout << "Hasil: " << x + y << endl;
}

void kurang(double x, double y) {
    cout << "Hasil: " << x - y << endl;
}

void kali(double x, double y) {
    cout << "Hasil: " << x * y << endl;
}

void bagi(double x, double y) {
    if (y == 0) {
        cout << "Tidak bisa dibagi dengan nol" << endl;
    } else {
        cout << "Hasil: " << x / y << endl;
    }
}

int main() {
    char opsi;
    double angka1, angka2;

    do {
        // Menampilkan menu
        cout << "Pilih operasi:" << endl;
        cout << "1. Tambah" << endl;
        cout << "2. Kurang" << endl;
        cout << "3. Kali" << endl;
        cout << "4. Bagi" << endl;
        cout << "5. Keluar" << endl;

        // Meminta input operasi dari pengguna
        cout << "Masukkan pilihan (1/2/3/4/5): ";
        cin >> opsi;

        // Melakukan operasi sesuai pilihan pengguna
        switch (opsi) {
            case '1':
                cout << "Masukkan angka pertama: ";
                cin >> angka1;
                cout << "Masukkan angka kedua: ";
                cin >> angka2;
                tambah(angka1, angka2);
                break;
            case '2':
                cout << "Masukkan angka pertama: ";
                cin >> angka1;
                cout << "Masukkan angka kedua: ";
                cin >> angka2;
                kurang(angka1, angka2);
                break;
            case '3':
                cout << "Masukkan angka pertama: ";
                cin >> angka1;
                cout << "Masukkan angka kedua: ";
                cin >> angka2;
                kali(angka1, angka2);
                break;
            case '4':
                cout << "Masukkan angka pertama: ";
                cin >> angka1;
                cout << "Masukkan angka kedua: ";
                cin >> angka2;
                bagi(angka1, angka2);
                break;
            case '5':
                cout << "Terima kasih!" << endl;
                break;
            default:
                cout << "Pilihan tidak valid" << endl;
        }
    } while (opsi != '5');

    return 0;
}
