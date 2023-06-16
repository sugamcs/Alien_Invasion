test = {
    "What is the color of the banana?": "yellow",
    "What is the color of the sky?": "blue"
}
def quiz():
    tries = 3
    for question,answer in test.items():
        while tries > 0:
            user_input = input(question + " ")
            if user_input.lower() == answer:
                print("You are correct! ")
                break
            elif user_input.lower() != answer:
                tries = tries - 1
                print(f"You are wrong, you now have {tries} left")
        else:
            print("Try again")


quiz()


