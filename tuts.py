import random

def play():
    user_choices = ["r","p", "s"]
    player = input("Input your choice \nYou can enter either r for Rock, p for Paper or s for Scissors\n")
    opponent = random.choice(user_choices)

    if(player in user_choices):
        if(player == opponent):
            print('It\'s a tie')
        if is_win(player, opponent):
            print('You won 🎉🥳🔥')
        print('You lost 🃏')
    else:
        print('Invalid input, you should enter r, p or s')

def is_win(p1, p2):
    if(p1 == 'r' and p2 == 's') or (p1 == 'p' and p2 == 'r') \
        or (p1 == 's' and p2=='p'):
        return True
play()