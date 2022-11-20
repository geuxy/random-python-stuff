# import random module.
import random

# new variable which will be the opponents choice set to one of these strings.
rands_choice = random.choice(['rock', 'paper', 'scissors'])

# ask user.
print('Rock, Paper or Scissors?: ')

# make variable set to users input and set to lower case.
users_choice = input().lower()

# print opponents choice.
print('Opponent chooses:', rands_choice)

# check if both players chose the same.
if rands_choice == users_choice:
    print('Tie!')

# check if opponent chose rock.
elif rands_choice == 'rock':

    # if player chose scissors, they win, else they lose.
    print('you win!' if users_choice == 'paper' else 'You lose!')

# check if opponent chose paper.
elif rands_choice == 'paper':

    # if player chose scissors, they win, else they lose.
    print('you win!' if users_choice == 'scissors' else 'You lose!')

# check if opponent chose scissors.
elif rands_choice == 'scissors':

    # if player chose rock, they win, else they lose.
    print('you win!' if users_choice == 'rock' else 'You lose!')
