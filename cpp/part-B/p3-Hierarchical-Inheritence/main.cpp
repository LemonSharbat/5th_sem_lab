#include <iostream>
#include <string>

using namespace std;

class Student {
    string name;
    int age, usn;

public:
    void getStudent() {
        cout << "Name: ";
        cin >> name;

        cout << "Age: ";
        cin >> age;

        cout << "USN: ";
        cin >> usn;
    }
};

class Medical : public Student {

};

class Engineering : public Student {

};


int main() {

    return 0;
}
