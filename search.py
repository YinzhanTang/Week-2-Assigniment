# search.py

def search(hvalue,periods,rate,desiredpay): # Define a new Bisection search function
    # Start with an interval that we know contains a solution
    a = 0 # Set one side of the interval as a = 0
    b = hvalue # Set the other side of the interval as b = hvalue
    # "hvalue equals to the home price, which is upper bound of down payment"

    while True: # Start the loop
        import mortgage # Import the mortgage module
        c = (a+b)/2 # Bisect the interval
        dpayment = c # Define dpayment (down payment)
        loan = hvalue - dpayment # Define loan
        Fc = mortgage.mortgage_payment(loan, periods, rate) - desiredpay
        # Calculate F(c) to determine which side of the origin interval contains the solution
        if abs(Fc) < 0.000001:
            return dpayment # If F(c) is infinately close to zero, the search is finished
                            # Return c, which is also the down payment, as the result of the function
        elif Fc < 0: # If F(c) is below 0, then the solution is in the left side of the interval
            b = c # Replace b with c and continue
        else: # If F(c) is above 0, then the solution is in the right side of the interval
            a = c # Replace a with c and continue

        # Continue the loop until we found the down payment that induce the desired payment

print('Welcome to Period Mortgage Payment Calculator') # Program Startup
hvalue = float(input('Tell me the home value($) :')) # Enter the Home Value
yrate = float(input('Tell me the (annual) interet rate:'))# Enter the (Annual) interests rate
yperiods = float(input('Tell me the terms(in years):')) # Enter the Term(in years)
desiredpay = float(input('Tell me the desired monthly payment:')) # Enter the Desired Monthly Payment

periods = yperiods * 12 # Calculate the monthly periods in the loans
rate = (yrate / 100)/12 # Calculate the monthly interests rate

import math # Import the math module
down_payment = round(search(hvalue,periods,rate,desiredpay),2) # Round the answer to the nearest cent
print('Hey! Your suggested down payment amount is around $',down_payment) # Print the answer
