'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: hw03_01.py

DESCRIPTION: Mortgage Amortization Table
'''

import finance

def main():

    # Prompt the user for loan details
    print("DATA ENTRY")
    loan_amount = float(input("Enter loan amount ($):...... "))
    apr         = float(input("Enter loan APR (%):......... "))
    term_years  =   int(input("Enter loan term (yr):....... "))
    filename    =   str(input("Filename (w/o ext):......... "))
    print()

    # Generate full and abbreviated Amortization Schedules

    with open(filename + ".txt", "wt") as fp:
        for s in finance.mortgage_amortization_payment(loan_amount, apr, term_years):
            fp.write(s)
        
    # Print abbreviated amortization schedule to console
    for s in finance.mortgage_amortization_payment(loan_amount, apr, term_years, increment=1):
        print(s)


if __name__ == "__main__":
    main()


