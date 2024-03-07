'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: finance.py

DESCRIPTION: Mortgage Functions
'''


def mortgage_residual(loan_amount, apr, term_years, payment):
    
    # Set constraints used in calculations
    term_months = 12 * term_years
    monthly_rate = (apr / 100) /12
    
    # Simulate payments over the term of the loan
    balance = loan_amount
    for i in range(term_months):
        interest = round(balance * monthly_rate, 2)
        balance -= (payment - interest)
    
    # Return the residual balance
    return balance


def mortgage_payment(loan_amount, apr, term_years):
    
    # Set initial bounds and guess
    lower_bound = round(loan_amount / (12 * term_years), 2)
    upper_bound = round(lower_bound + loan_amount * (apr/1200), 2)
    
    while (upper_bound - lower_bound) > 0.015:
        payment = round((lower_bound + upper_bound) / 2, 2)
        residual = mortgage_residual(loan_amount, apr, term_years, payment)
        
        if residual < 0:
            upper_bound = payment
            
        else:
            lower_bound = payment
            
    upper_residual = mortgage_residual(loan_amount, apr, term_years, upper_bound)
    lower_residual = mortgage_residual(loan_amount, apr, term_years, lower_bound)
    
    if abs(upper_residual) < abs(lower_residual):
        payment = upper_bound
        residual = upper_residual
        
    else:
        payment = lower_bound
        residual = lower_residual
        
    return(payment, payment + residual)
            

def mortgage_amortization_payment(amount, rate, term, increment=1):
    
    monthly_payment, final_payment = mortgage_payment(amount, rate, term)
    total_paid = monthly_payment * term * 12
    cost_of_credit = total_paid - amount
    
    # Forming the summary string
    summary = f"Loan amount: ${amount:.2f}\n"
    summary += f"Loan rate: {rate:.3f}%\n"
    summary += f"Loan term: {term} years\n"
    summary += f"Monthly payment: ${monthly_payment:.2f}\n"
    summary += f"Total paid: ${total_paid:.2f}\n"
    summary += f"Cost of credit: ${cost_of_credit:.2f}\n"
    
    # Forming the header string
    header = "      /-------   PAYMENT   --------\\  /---------   TOTAL   ---------\\\n"
    header += "month  payment  interest principal  interest   principal     paid   balance\n"
    
    # Forming the table string
    table = ""
    for i in range(1, term * 12 + 1, increment):
        interest = amount * (rate / 100 / 12)
        principal = monthly_payment - interest
        amount -= principal
        
        if (i % 12 == 0):
 
            table += f"{i:>5} {monthly_payment:>8.2f} {interest:>9.2f} {principal:>10.2f} "
            table += f"{interest * i:>9.2f} {principal * i:>10.2f} {monthly_payment * i:>9.2f} {amount:>9.2f}\n"
        
    return ("MORTGAGE AMORTIZATION SCHEDULE", summary, header, table)
        
    
def mortgage_report(amount, rate, term, increment=1):
    
    report = ""
    for s in mortgage_amortization_payment(amount, rate, term, increment):
        report += s
    return report
