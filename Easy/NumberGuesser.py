import random

range_input = int(input("Type a number:\n"))
guesses = 0
random_number = random.randint(0, range_input)

while True:
    guesses+=1
    user_guess = int(input("Make a guess:\n"))
    if range_input == user_guess:
        print("Yay!! It matches")
        break
else:
    print("Boo!!! Try again")
print("You got it in",guesses,"guesses")