/* Write a C++ program to create a class sample with integer, character and float data
members. Demonstrate Constructor Overloading on this class with all types of constructors
including default argument constructor. */

#include <iostream>

using namespace std;

class Sample {
    int i;
    char c;
    float f;

public:
    // Default constructor
    Sample() {
        i = 0;
        c = 'X';
        f = 0.0;
    }

    // Parameterized constructor
    Sample(int i, char c, float f) {
        this->i = i;
        this->c = c;
        this->f = f;
    }

    // Copy constructor
    Sample(Sample &s) {
        i = s.i;
        c = s.c;
        f = s.f;
    }

    // Parameterized with Default argument
    // IMP: Change the order of arguments
    Sample(int i, float f, char c = 'D') {
        this->i = i;
        this->f = f;
        this->c = c;
    }

    void display() {
        cout << "i = " << i;
        cout << "\nc = " << c;
        cout << "\nf = " << f << endl;
    }
};

int main( ){

    Sample s1;
    cout << "Default constructor: \n";
    s1.display();

    Sample s2(2, 'g', 3.14);
    cout << "Parameterized cnstructor: \n";
    s2.display();

    Sample s3(s2);
    cout << "Copy constructor: \n";
    s3.display();

    Sample s4(9, 9.992);
    cout << "Parameterized constructor with default argument: \n";
    s4.display();

    return 0;
}
