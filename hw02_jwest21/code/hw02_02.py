'''
PROGRAMMER: .... Jakob K. West
USERNAME: ...... jwest21
PROGRAM: ....... hw02_02.py

DESCRIPTION: Creating a mortgage_residual function
'''

def mortgage_residual(amount, rate, term, monthly_payment):
    monthly_interest_rate = rate / 100 /12
    total_payments = term * 12
    
    for i in range(total_payments):
        interest_charge = amount * monthly_interest_rate
        principal_payment = monthly_payment - interest_charge
        amount -= principal_payment
        
    return round(amount, 2)

def mortgage_payment(amount, rate, term):
    monthly_interest_rate = rate / 100 / 12
    total_payments = term * 12
    
    # Calculate monthly payment
    monthly_payment = amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_payments)
    
    final_payment = monthly_payment + (amount * monthly_interest_rate)
    
    return round(monthly_payment, 2), round(final_payment, 2)

def main():
    # Get input from user (loan_amount, apr, loan_term)
    print("DATA ENTRY")
    loan_amount = float(input("Enter loan amount ($):...... "))
    apr = float(input("Enter loan APR (%):......... "))
    loan_term = int(input("Enter loan term (yr):....... "))
    
    # Calculate mortgage terms
    monthly_payment, final_payment = mortgage_payment(loan_amount, apr, loan_term)
    residual = mortgage_residual(loan_amount, apr, loan_term, monthly_payment)
    total_paid = monthly_payment * loan_term * 12
    cost_of_credit = total_paid - loan_amount
    
    # Display mortgage terms (final print statements)
    print("\nMORTGAGE TERMS")
    print(f"Loan amount:................ {'$':<10}{loan_amount:.2f}")
    print(f"Loan rate:.................. {'':<10}{apr:.3f} %")
    print(f"Loan term:.................. {'':<10}{loan_term} years")
    print(f"Monthly payment:............ {'$':<10}{monthly_payment:.2f}")
    print(f"Final Payment:.............. {'$':<10}{final_payment:.2f}")
    print(f"Total paid:................. {'$':<10}{total_paid:.2f}")
    print(f"Cost of credit:............. {'$':<10}{cost_of_credit:.2f}")
    
    
if __name__ == "__main__":
    main()