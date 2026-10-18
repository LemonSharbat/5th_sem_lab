#include <iostream>
using namespace std;


class BankAccount {
    int accountNumber;
    string name;
    float balance;

    public:
        void read() {
            cout << "Enter account number: ";
            cin >> accountNumber;
            cout << "Enter name: ";
            cin >> name;
            cout << "Enter balance: ";
            cin >> balance;
        }

        void deposite() {
            float amount;

            cout << "Enter amount to deposite: ";
            cin >> amount;

            balance += amount;
            cout << "Amt. " << amount << " is credited\n";
        }

        void withdeaw() {
            float amount;

            cout << "Enter amount to withdraw: ";
            cin >> amount;

            if (balance < amount) {
                cout << "Insufficient balence\n";
                return;
            }

            balance -= amount;
            cout << "Amt. " << amount << " is debited\n";
        }

        void display() {
            cout << "Account number: " << accountNumber << endl;
            cout << "Name: " << name << endl;
            cout << "Balance: " << balance << endl;
        }
};

int main() {
    BankAccount b;

    b.read();
    b.deposite();
    b.withdeaw();
    b.display();

    return 0;
}
