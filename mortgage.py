# mortgage.py

def mortgage_payment(loan, periods, rate): # Define a new python function
    payment = (rate * loan)/(1 - (1 + rate)**(-periods)) # Implement the given calculation
    return(payment) # Determine the return value
