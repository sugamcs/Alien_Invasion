def main():
    while True:
        print("Welcome to email slicer! \n")
        user_input = input("Please enter your email address or type q to quit: ")
        if user_input.lower() == "q":
            break
        
        (username, domain) = user_input.split("@")
        (domain, extension) = domain.split(".")

        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension)

       
main()






