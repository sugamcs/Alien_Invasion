import random
def coin():
    possibilities = ["Heads", "Tails"]
    iterations = 0
    consecutive_heads = 0
    while consecutive_heads < 10:
        iterations +=1
        outcome = random.choice(possibilities)

        if outcome == "Heads":
            consecutive_heads +=1
        else:
            consecutive_heads = 0

    return f"10 heads in a row achived after {iterations} iterations"


print(coin())


