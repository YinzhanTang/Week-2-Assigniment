# calculator.py

print('Welcome to Period Mortgage Payment Calculator') # Program Startup
hvalue = float(input('Tell me the home value($) :')) # Enter the Home Value
dpayment = float(input('Tell me the down payment: '))# Enter the Down payment
yrate = float(input('Tell me the (annual) interet rate:'))# Enter the (Annual) interests rate
yperiods = float(input('Tell me the terms(in years):')) # Enter the Term(in years)

loan = hvalue - dpayment # Calculate the loan amount
periods = yperiods * 12 # Calculate the monthly periods in the loans
rate = (yrate / 100)/12 # Calculate the monthly interests rate

import mortgage # Import the mortgage module
mortgage_payment = mortgage.mortgage_payment(loan, periods, rate)
# Call your mortgage_payment() function with the appropriate inputs

import math # Import the math module
mortgage_payment = round(mortgage_payment,2) # Round the answer to the nearest cent
print('Hey! Your period mortgage payment is around $',mortgage_payment)
# Print the answer (periods mortgage payment)
