#include <iostream>
#include <cctype> 
#include <string>
using namespace std;

int main() {
    string kalimat;
    cout << "Masukkan kalimat: ";
    getline(cin, kalimat);

    int vokal = 0, konsonan = 0, numerik = 0;

    cout << "Jumlah Vokal: ";
    for (char karakter : kalimat) {
        if (tolower(karakter) == 'a' || tolower(karakter) == 'e' || tolower(karakter) == 'i' || tolower(karakter) == 'o' || tolower(karakter) == 'u') {
            vokal++;
            cout << karakter << " ";
        }
    }
    cout << "= " << vokal << endl;

    cout << "Jumlah Konsonan: ";
    for (char karakter : kalimat) {
        if (isalpha(karakter) && !(tolower(karakter) == 'a' || tolower(karakter) == 'e' || tolower(karakter) == 'i' || tolower(karakter) == 'o' || tolower(karakter) == 'u')) {
            konsonan++;
            cout << karakter << " ";
        }
    }
    cout << "= " << konsonan << endl;

    cout << "Jumlah Numerik: ";
    for (char karakter : kalimat) {
        if (isdigit(karakter)) {
            numerik++;
            cout << karakter << " ";
        }
    }
    cout << "= " << numerik << endl;

    return 0;
}