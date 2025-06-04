#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, surname;

    // รับชื่อและนามสกุลจากผู้ใช้
    cout << "Enter your first name: ";
    cin >> name;

    cout << "Enter your surname: ";
    cin >> surname;

    // สร้างชื่อแฝงจาก 2 ตัวอักษรแรกของชื่อและนามสกุล
    string nickname = name.substr(0, 2) + surname.substr(0, 2);

    // แสดงผล
    cout << "Hello " << name << " " << surname << endl;
    cout << "Your nickname is: " << nickname << endl;

    return 0;
}
