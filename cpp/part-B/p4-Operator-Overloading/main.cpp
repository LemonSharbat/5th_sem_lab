/*  Write a C++ program to overload binary ‘+’ and ‘–‘ operator to add and subtract two
complex numbers. Define relevant data members and member functions for reading and
displaying the complex objects. */

#include <iostream>

using namespace std;

class Complex {
    int r;
    float i;

public:
    void read() {
        cout << "Real part: ";
        cin >> r;

        cout << "Imaginary part: ";
        cin >> i;
    }

    void display() {
        cout << r << " + " << i << "i\n";
    }

    Complex operator + (Complex c) {
        Complex sum;

        sum.r = r + c.r;
        sum.i = i + c.i;

        return sum;
    }

    Complex operator - (Complex c) {
        Complex diff;

        diff.r = r - c.r;
        diff.i = i - c.i;

        return diff;
    }
};

int main() {

    Complex c1, c2, c3, c4;

    cout << "Enter 1st complex number: \n";
    c1.read();

    cout << "Enter 2nd complex number: \n";
    c2.read();

    c3 = c1 + c2;
    c4 = c1 - c2;

    cout << "\nc1 = ";
    c1.display();

    cout << "c2 = ";
    c2.display();

    cout << "\nc1 + c2 = ";
    c3.display();

    cout << "c1 - c2 = ";
    c4.display();

    return 0;
}
