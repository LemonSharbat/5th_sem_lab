/*Write a C++ program with class Time with data members that represents hours and minutes.
Include appropriate member functions to compute time in hours and minutes. (Use of
objects as arguments). */

#include <iostream>
using namespace std;

class Time {
    int hr, min;

public:
    void read() {
        cout << "Enter hour: ";
        cin >> hr;

        cout << "Enter minute: ";
        cin >> min;
    }

    void add(Time t1, Time t2) {
        int totalMin = t1.min + t2.min;
        min = totalMin % 60;
        hr = t1.hr + t2.hr + (totalMin / 60);
    }

    void display() {
        cout << hr << "hr : " << min << "min" << endl;
    }
};


int main() {
    Time t1, t2, t3;

    cout << "Enter t1: \n";
    t1.read();

    cout << "Enter t2: \n";
    t2.read();

    t3.add(t1, t2);

    cout << "t1 = ";
    t1.display();

    cout << "t2 = ";
    t2.display();

    cout << "t1 + t2 = ";
    t3.display();

    return 0;
}
