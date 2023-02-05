#include<iostream>
#include<iomanip>
using namespace std;
class investment{
    private:
        double amount, rate, tenure, taxSlab;

        double updateAmount(double amount, double rate){
            return amount*(100+rate)/100;
        }

    public:
        void getInput(){
            cout << "Input investment amount: ";
            cin >> amount;
            cout << "Input rate of interest: ";
            cin >> rate;
            cout << "Input tenure (in years): ";
            cin >> tenure;
        }
        void printData(){
            cout << "\nAmount: " << amount << " , rate: " << rate
                << " , tenure: " << tenure << endl;
        }
        void preTaxComparison(){
            cout << ":::PRE-TAX RETURNS COMPARISON TABLE:::";
            cout << "\nPrinting below the table comparing the pre-tax returns"
                << endl << "against the standard 5% FD interest rate."
                << endl << "--------------------------------------------------------------"
                << endl << setw(20) << "Tenure (in years) |" << setw(17) << "Amount Invested |"
                << setw(24) << " Amount if invested in FD"
                << endl << "--------------------------------------------------------------" << endl;
            
            double investmentOrg = amount, investmentFD = amount;

            for(int i = 0; i<tenure;i++){
                investmentOrg = updateAmount(investmentOrg, rate);
                investmentFD = updateAmount(investmentFD, 5.00);
                cout << setw(18) << i+1 << " |" << setiosflags(ios::fixed)
                    << setw(15)  << setprecision(2) << investmentOrg << " |"
                    << setw(15)  << setprecision(2) << investmentFD << endl;
            }
            cout << "--------------------------------------------------------------" << endl;
        }
        void postTaxComparison(){
            cout << "Enter the tax slab you reside in (in %): ";
            cin >> taxSlab; 
            cout << ":::POST-TAX RETURNS COMPARISON TABLE:::";
            cout << "\nPrinting below the table comparing the post tax returns"
                << endl << "against the standard 5% FD interest rate."
                << endl << "--------------------------------------------------------------"
                << endl << setw(20) << "Tenure (in years) |" << setw(17) << "Amount Invested |"
                << setw(24) << " Amount if invested in FD"
                << endl << "--------------------------------------------------------------" << endl;
            
            double investmentOrg = amount, investmentFD = amount;
            for(int i = 0; i<tenure;i++){
                investmentOrg = updateAmount(investmentOrg, rate);
                investmentFD = updateAmount(investmentFD, 5.00);
                double profitPostTaxOrg = (investmentOrg - amount)*(100 - taxSlab)/100;
                double profitPostTaxFD = (investmentFD - amount)*(100 - taxSlab)/100;
                cout << setw(18) << i+1 << " |" << setiosflags(ios::fixed)
                    << setw(15)  << setprecision(2) << amount + profitPostTaxOrg << " |"
                    << setw(15)  << setprecision(2) << amount + profitPostTaxFD << endl;
            }
            cout << "--------------------------------------------------------------" << endl;
        }
};

int main(){
    investment myInvestment;
    myInvestment.getInput();
    myInvestment.printData();
    myInvestment.preTaxComparison();
    myInvestment.postTaxComparison();
    return 0;
}

