def interest_rate_calculator():
    principal_amount = float(input("Enter the principal monthly amount: "))
    apr = float(input("Enter the annual interest rate on your principal amount: "))
    years = int(input("Enter the number of years the loan is for: "))

    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal_amount * monthly_interest_rate / (1 -(1 + monthly_interest_rate) **(-amount_of_months))


    print("The monthly payment for this loan is : %.2f"% monthly_payment)


interest_rate_calculator()
