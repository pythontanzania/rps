import random

user_choices = ["r","p","s"]
user = input("Enter r for Rock p for Paper or s Scissors\n")
computer = random.choice(user_choices)
# computer = "p"

def play(): 
    if(user in user_choices):
        print("You picked", user)
        print("Computer picked", computer)

        if(user == computer):
            print("You tie")

        if is_win(user, computer):
            print("You win")
        elif(user != computer): 
            print("You lost")
        
    else: 
        print("invalid choice")

def is_win(p1, p2):
    if(p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r') \
    or (p1 == 'r' and p2 == 's'):
        return True

play()