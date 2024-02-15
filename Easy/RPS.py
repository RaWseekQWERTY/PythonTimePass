import random
CLEAR = "\033[2J"
user_wins = 0
comp_wins = 0
comp_options = ["Rock","Paper","Scissor"]
while True:
    print(CLEAR)
    user_input = int(input("Type \n"+"1. For Rock\n"+"2. For Paper\n"+"3. For Scissors \n"+"4. To Quit\n"))
    
    if user_input == 4:
        break
    if user_input not in [1,2,3]:
        continue
    
    random_num = random.randint(0,2) #rock:0, paper:1, scissor:2
    comp_pick = comp_options[random_num]
    print("Computer Picked:"+comp_pick+".")
    if user_input == 1 and comp_pick == "Scissor":
        print("You won")
        user_wins+=1
    elif user_input == 2 and comp_pick == "Rock":
        print("You won")
        user_wins+=1
    elif user_input == 3 and comp_pick == "Paper":
        print("You won")
        user_wins+=1
    elif user_input == comp_pick:
        print("Its a tie")
    else:
        print("You lost")
        comp_wins+=1
        
print("Scores:")
print("You won:",user_wins)
print(f"Computer won: {comp_wins}")
print("!!!Thank You For Playing!!!")