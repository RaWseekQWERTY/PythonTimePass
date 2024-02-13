import random

range_input = int(input("Type a number:\n"))

random_number = random.randint(0, range_input)

while True:
    user_guess = int(input("Make a guess:\n"))