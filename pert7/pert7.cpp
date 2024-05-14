#include <iostream>

using namespace std;

void menuMakanan();
void menuMinuman();
void hitungTotal(int harga);

int main() {
    int pilihan;

    do {
        cout << "Menu Utama:\n";
        cout << "1. Makanan\n";
        cout << "2. Minuman\n";
        cout << "3. Exit\n";
        cout << "Pilih menu: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                menuMakanan();
                break;
            case 2:
                menuMinuman();
                break;
            case 3:
                cout << "Keluar dari program.\n";
                break;
            default:
                cout << "Pilihan tidak valid. Coba lagi.\n";
        }
    } while (pilihan != 3);

    return 0;
}

void menuMakanan() {
    int pilihanMakanan;
    char ulang;

    do {
        cout << "Menu Makanan:\n";
        cout << "1. Pecel Lele\n";
        cout << "2. Nasi Goreng\n";
        cout << "3. Kembali\n";
        cout << "Pilih menu makanan: ";
        cin >> pilihanMakanan;

        switch (pilihanMakanan) {
            case 1:
                cout << "Anda memilih Pecel Lele.\n";
                hitungTotal(15000); // Harga Pecel Lele
                break;
            case 2:
                cout << "Anda memilih Nasi Goreng.\n";
                hitungTotal(20000); // Harga Nasi Goreng
                break;
            case 3:
                cout << "Kembali ke menu utama.\n";
                break;
            default:
                cout << "Pilihan tidak valid. Coba lagi.\n";
        }

        if (pilihanMakanan != 3) {
            cout << "Apakah Anda ingin membeli lagi? (y/n): ";
            cin >> ulang;
        } else {
            ulang = 'n';
        }
    } while (ulang == 'y' || ulang == 'Y');
}

void menuMinuman() {
    int pilihanMinuman;
    char ulang;

    do {
        cout << "Menu Minuman:\n";
        cout << "1. Teh Manis\n";
        cout << "2. Air Putih\n";
        cout << "3. Kembali\n";
        cout << "Pilih menu minuman: ";
        cin >> pilihanMinuman;

        switch (pilihanMinuman) {
            case 1:
                cout << "Anda memilih Teh Manis.\n";
                hitungTotal(5000); // Harga Teh Manis
                break;
            case 2:
                cout << "Anda memilih Air Putih.\n";
                hitungTotal(2000); // Harga Air Putih
                break;
            case 3:
                cout << "Kembali ke menu utama.\n";
                break;
            default:
                cout << "Pilihan tidak valid. Coba lagi.\n";
        }

        if (pilihanMinuman != 3) {
            cout << "Apakah Anda ingin membeli lagi? (y/n): ";
            cin >> ulang;
        } else {
            ulang = 'n';
        }
    } while (ulang == 'y' || ulang == 'Y');
}

void hitungTotal(int harga) {
    int qty;
    cout << "Masukkan jumlah pesanan: ";
    cin >> qty;
    int total = harga * qty;
    cout << "Total harga: " << total << " IDR\n";
}
