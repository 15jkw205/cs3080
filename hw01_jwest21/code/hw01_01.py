'''
PROGRAMMER: .... Jakob K. West
USERNAME: ...... jwest21
PROGRAM: ....... hw_01_01.py

DESCRIPTION: Mortgage payment and residual
'''

# Get input from user (loan amount, APR, loan term, monthly payment)
print("DATA ENTRY")
loan_amount = float(input("Enter loan amount ($): ........... "))
apr = float(input("Enter loan APR (%): ...................... "))
loan_term = int(input("Enter loan term (yr): ................ "))
monthly_payment = float(input("Enter monthly payment ($): ... ")) 

# Calculations
apr_decimal = apr / 100
monthly_interest_rate = apr_decimal / 12
total_payments = loan_term * 12
remaining_balance = loan_amount

# Updating the interest charge, principal payment, and remaining balance
for i in range(total_payments):

    interest_charge = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_charge
    remaining_balance -= principal_payment

    if remaining_balance <= 0:
        remaining_balance = 0

final_payment = float(monthly_payment - remaining_balance)
residual_balance = float(final_payment - monthly_payment)

print("\nANALYSIS RESULTS")
print(f"Loan rate: {apr: .3f} %")
print(f"Loan term: {loan_term} years")
print(f"Loan amount: ${loan_amount: .2f}")
print(f"Monthly payment: ${monthly_payment: .2f}")
print(f"Residual balance: ${residual_balance: .2f}")
print(f"Final Payment: ${final_payment: .2f}")
