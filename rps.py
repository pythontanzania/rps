# Rock, Paper Scissors game
# A begginer friendly game built using python

import random

# python variables 
# https://www.w3schools.com/python/python_variables.asp

# python built in function
# https://docs.python.org/3/library/functions.html

# python built in module 
# https://www.w3schools.com/python/module_random.asp

user_choices = ['r','p', 's']

user = input("Enter r for Rock, s for Scissors or p for Paper \n")

computer = random.choice(user_choices)

# r > s, s > p , p > r

def is_win(player, computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player =='p' and computer =='r'):
        print("You win")
    elif(player == computer):
        print('It\'s a tie')
    else: 
        print("You lost")


# python function
# https://www.w3schools.com/python/python_functions.asp
def play(player, computer):

    if(player in user_choices):
        print("Your choice is", player)
        print("Computer choice is", computer)

        is_win(player, computer)
    else:
        print("Invalid choice, please enter r, p or s")

play(user, computer)
