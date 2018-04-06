# table.py

print('Welcome to Period Mortgage Payment Calculator(Table)') # Program Startup
hvalue = float(input('Tell me the home value($) :')) # Enter the Home Value
dpayment_max = float(input('Tell me the maximum down payment: '))# Enter the Maximum Down payment
dpayment_min = float(input('Tell me the minimum down payment: '))# Enter the Minimum Down payment
yrate = float(input('Tell me the (annual) interet rate:'))# Enter the (Annual) interests rate
yperiods = float(input('Tell me the terms(in years):')) # Enter the Term(in years)

import numpy as np # Import the numpy module
arange = np.arange(dpayment_min, dpayment_max, 1000)
# Define the float range from "dpayment_min" to "dpayment_max"
# References: http://stackoverflow.com/questions/477486/python-decimal-range-step-value
periods = yperiods * 12 # Calculate the monthly periods in the loans
rate = (yrate / 100)/12 # Calculate the monthly interests rate

import mortgage # Import the mortgage module
import math # Import the math module
for dpayment in arange: # For different amounts of down payments in the float range:
    loan = hvalue - dpayment # Calculate the amounts of loan
    print(dpayment, round(mortgage.mortgage_payment(loan, periods, rate),2))
    # Calculate the monthly mortgage payments given different amounts of down payment(and other inputs)
    # For each $1000 increment in down payments, print the corresponding monthly payment
