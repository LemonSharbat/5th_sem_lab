
#include <iostream>
using namespace std;

class Complex {
    int r, i;

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

    friend Complex add(int, Complex);
    friend Complex add(Complex, Complex);
};

Complex add(int a, Complex b) {
    Complex c;

    c.r = a + b.r;
    c.i = b.i;

    return c;
}

Complex add(Complex a, Complex b) {
    Complex c;

    c.r = a.r + b.r;
    c.i = a.i + b.i;

    return c;
}

int main() {
    int a;
    Complex c1, c2;

    cout << "Enter a number: ";
    cin >> a;

    cout << "Enter 1st complex number:\n";
    c1.read();

    cout << "Enter 2nd complex number:\n";
    c2.read();

    Complex c3 = add(a, c1);
    Complex c4 = add(c1, c2);

    cout << "\nc1 = ";
    c1.display();

    cout << "c2 = ";
    c2.display();

    cout << "a + c1 = ";
    c3.display();

    cout << "c1 + c2 = ";
    c4.display();

    return 0;
}
