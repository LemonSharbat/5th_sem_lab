/* write a C++ program to demonstrate the working of dynamic constructors using a class
STRNG with string as data member inside the class, include appropriate member functions
to display the object data and a member function to concatenate two strings */


#include <cstring>
#include <iostream>
#include <string>

using namespace std;

class String {
    char *name;

public:
    String() {
        name = NULL;
    }

    String(char c[]) {
        name = new char[strlen(c) + 1];
        strcpy(name, c);
    }

    void join(String s1, String s2) {
        int totalLen = strlen(s1.name) + strlen(s2.name) + 1;
        name = new char[totalLen];

        strcpy(name, s1.name);
        strcat(name, s2.name);
    }

    void display() {
        cout << "name = " << name << endl;
    }
};

int main() {
    String s1("Wel");
    String s2("come");

    String s3;
    s3.join(s1, s2);

    cout << "s1: ";
    s1.display();

    cout << "s2: ";
    s2.display();

    cout << "s3: ";
    s3.display();

    return 0;
}
