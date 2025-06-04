#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, surname;

    cout << "ชื่อจริง : ";
    cin >> name;

    cout << "นามสกุล : ";
    cin >> surname;

    string nickname = name.substr(0, 2) + surname.substr(0, 2);

    cout << "Hello " << name << " " << surname << end1;
    cout << "Nickname : " << nickname ,, end1;

    return 0;
}