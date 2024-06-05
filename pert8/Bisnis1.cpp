#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip> // untuk setprecision dan fixed
#include <sstream> // untuk stringstream

using namespace std;

struct Motor {
    string merek;
    string model;
    int tahun;
    double harga;
    string kondisi;
};

class PasarMotor {
private:
    vector<Motor> daftarMotor;

public:
    void tambahMotor(const string& merek, const string& model, int tahun, double harga, const string& kondisi) {
        Motor motorBaru = {merek, model, tahun, harga, kondisi};
        daftarMotor.push_back(motorBaru);
    }

    void editMotor(int index, const string& merek, const string& model, int tahun, double harga, const string& kondisi) {
        if (index >= 0 && index < daftarMotor.size()) {
            daftarMotor[index] = {merek, model, tahun, harga, kondisi};
            cout << "Detail motor berhasil diperbarui." << endl;
        } else {
            cout << "Indeks motor tidak valid." << endl;
        }
    }

    void hapusMotor(int index) {
        if (index >= 0 && index < daftarMotor.size()) {
            daftarMotor.erase(daftarMotor.begin() + index);
            cout << "Motor berhasil dihapus." << endl;
        } else {
            cout << "Indeks motor tidak valid." << endl;
        }
    }

    void tampilkanMotor() const {
        if (daftarMotor.empty()) {
            cout << "Tidak ada motor yang tersedia." << endl;
            return;
        }
        for (int i = 0; i < daftarMotor.size(); ++i) {
            cout << i + 1 << ". " << daftarMotor[i].merek << " " << daftarMotor[i].model 
                 << " (" << daftarMotor[i].tahun << ") - Rp" << fixed << setprecision(2) << daftarMotor[i].harga
                 << " [" << daftarMotor[i].kondisi << "]" << endl;
        }
    }

    void cariMotor(const string& merek, const string& model) const {
        bool ditemukan = false;
        for (const auto& motor : daftarMotor) {
            if (motor.merek == merek && motor.model == model) {
                cout << "Ditemukan: " << motor.merek << " " << motor.model 
                     << " (" << motor.tahun << ") - Rp" << fixed << setprecision(2) << motor.harga
                     << " [" << motor.kondisi << "]" << endl;
                ditemukan = true;
            }
        }
        if (!ditemukan) {
            cout << "Tidak ada motor yang cocok dengan kriteria." << endl;
        }
    }
};

int main() {
    PasarMotor pasar;
    int pilihan;

    do {
        cout << "\nMenu Pasar Motor:\n";
        cout << "1. Tambah Motor\n";
        cout << "2. Edit Motor\n";
        cout << "3. Hapus Motor\n";
        cout << "4. Tampilkan Semua Motor\n";
        cout << "5. Cari Motor\n";
        cout << "6. Keluar\n";
        cout << "Masukkan pilihan Anda: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1: {
                string merek, model, kondisi;
                int tahun;
                double harga;
                cout << "Masukkan merek: ";
                cin >> merek;
                cout << "Masukkan model: ";
                cin >> model;
                cout << "Masukkan tahun: ";
                cin >> tahun;
                cout << "Masukkan harga: ";
                cin >> harga;
                cout << "Masukkan kondisi: ";
                cin >> kondisi;
                pasar.tambahMotor(merek, model, tahun, harga, kondisi);
                break;
            }
            case 2: {
                int index;
                string merek, model, kondisi;
                int tahun;
                double harga;
                cout << "Masukkan indeks motor yang akan di-edit: ";
                cin >> index;
                cout << "Masukkan merek baru: ";
                cin >> merek;
                cout << "Masukkan model baru: ";
                cin >> model;
                cout << "Masukkan tahun baru: ";
                cin >> tahun;
                cout << "Masukkan harga baru: ";
                cin >> harga;
                cout << "Masukkan kondisi baru: ";
                cin >> kondisi;
                pasar.editMotor(index - 1, merek, model, tahun, harga, kondisi);
                break;
            }
            case 3: {
                int index;
                cout << "Masukkan indeks motor yang akan dihapus: ";
                cin >> index;
                pasar.hapusMotor(index - 1);
                break;
            }
            case 4:
                pasar.tampilkanMotor();
                break;
            case 5: {
                string merek, model;
                cout << "Masukkan merek yang dicari: ";
                cin >> merek;
                cout << "Masukkan model yang dicari: ";
                cin >> model;
                pasar.cariMotor(merek, model);
                break;
            }
            case 6:
                cout << "Keluar..." << endl;
                break;
            default:
                cout << "Pilihan tidak valid. Silakan coba lagi." << endl;
        }
    } while (pilihan != 6);

    return 0;
}
