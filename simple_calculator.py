def calculator():
    digit_one = int(input("Enter your first digit: "))
    digit_two = int(input("Enter your second digit: "))


    operation = input("""Which operation do you want to apply?
A for sum, M for multiply, D for devide, S for subtract: """ )
    if operation.lower() == "a":
        print("Your answer is " , digit_one + digit_two) 
    elif operation.lower() == "m":
        print("Your answer is " , digit_one * digit_two) 
    elif operation.lower() == "d":
        print("Your answer is " , digit_one / digit_two) 
    elif operation.lower() == "s":
        print("Your answer is" , digit_one - digit_two) 
    

calculator()
