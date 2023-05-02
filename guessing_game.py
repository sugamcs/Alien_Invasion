import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 100
    while guess != random_number:
        guess = int(input("Guess: "))
        if guess < random_number:
            print(f"Your guess is too low!")
        elif guess > random_number:
            print("Your guess is too high!")
    print(f"Your guess is right!")


guess(10)
