#include<iostream>
#include<iomanip>

using namespace std;

double calcAmountInvested(double, double);

int main()
{
    double investment, rate, tenure;
    cout << "Input investment value: ";
    cin >> investment;
    cout << "\nInput rate of interest for the investment: ";
    cin >> rate;
    cout << "\nInput the tenure of the investment in years: ";
    cin >> tenure;
    cout << "\nPrinting below the table comparing the investment"
        << endl << "against the standard 5% FD interest rate."
        << endl << "--------------------------------------------------------------"
        << endl << setw(20) << "Tenure (in years) |" << setw(17) << "Amount Invested |"
        << setw(24) << " Amount if invested in FD"
        << endl << "--------------------------------------------------------------" << endl;
    double investmentOrg = investment, investmentFD = investment;
    for(int i = 0; i<tenure;i++){
        investmentOrg = calcAmountInvested(investmentOrg, rate);
        investmentFD = calcAmountInvested(investmentFD, 5.00);
        cout << setw(18) << i+1 << " |" << setiosflags(ios::fixed)
            << setw(15)  << setprecision(2) << investmentOrg << " |" 
            << setw(15)  << setprecision(2) << investmentFD << endl; 
    }
    return 0;
}

double calcAmountInvested(double investment, double rate){
    return investment*(100+rate)/100;
} 
