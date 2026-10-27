/*Given that an EMPLOYEE class contains following members. Data members: Eno, Ename
and salary Member functions: to read the data, to print data members. Write a C++ program
to read the data of N employees and display details of each employee.(use Array of objects
concept) */

#include <iostream>
#include <string>

using namespace std;

class Employee {
    int eno;
    string name;
    float salary;

public:
    void read() {
        cout << "Employee ID: ";
        cin >> eno;

        cout << "Name: ";
        cin >> name;

        cout << "Salary: ";
        cin >> salary;
    }

    void display() {
        cout << eno << "\t" << name << "\t" << salary << endl;
    }
};

int main() {
    int n;
    cout << "Enter the number of employees: ";
    cin >> n;

    Employee employees[n];

    cout << "Enetr employee details: ";
    for (int i = 0; i < n; i++) {
        cout << "Employee - " << i + 1 << endl;
        employees[i].read();
        cout << "\n";
    }

    cout << "\n\n-----Employee Details-----\n";
    cout << "ID\tName\tSalary\n";
    cout << "--------------------------\n";
    for (int i = 0; i < n; i++)
        employees[i].display();
    cout << "--------------------------\n";

    return 0;
}
