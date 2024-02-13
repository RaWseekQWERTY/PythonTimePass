import random
CLEAR = "\033[2J"
while True:
    print(CLEAR)
    try:
        range_input = int(input("Type a number:\n"))
        break
    except ValueError:
        print("Please enter a valid number.")

guesses = 0
random_number = random.randint(0, range_input)

while True:
    guesses += 1
    try:
        user_guess = int(input("Make a guess:\n"))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if random_number == user_guess:
        print("Yay!! It matches")
        break
    else:
        print("Boo!!! Try again")

print("You got it in", guesses, "guesses")
