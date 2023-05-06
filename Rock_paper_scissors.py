import random
def play():
    user = input("What do you want to chose, s for scissors, p for paper, r for rock: ")
    computer = random.choice(["s","p","r"])
    if (user == "s" and computer == "p") or (user == "p" and computer == "r")  \
        or (user == "r" and computer  == "s"):
        return "You won"
    return "You lost"


print(play())

    
