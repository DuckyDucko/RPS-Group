import time
import sys
from random import randint

print('Rock Paper Scissors by Ducky and Vinex', '\t')
print('Beta 1.0.3')
print("\t")

win = True
computer_score = 0
user_score = 0

while True:
    userinput = input('Rock, Paper, Scissors? ').lower()
    if (userinput == "rock"):
        print('You choose Rock!')
    elif (userinput == "paper"):
        print('You choose Paper!')
    elif (userinput == "scissors"):
        print('You choose Scissors!')
    else:
        print('That was not a valid answer, are sure you are playing the right game?')
        continue
    # --------------------------------------------------------------------------------------
    print('---Computer is thinking---', '\t')
    time.sleep(1.0)
    computerinput = randint(1, 3)
    # --------------------------------------------------------------------------------------
    if (computerinput == 1):
        print('Computer chose Rock!')
        computerinput = "rock"
    elif (computerinput == 2):
        print('Computer chose Paper!')
        computerinput = "paper"
    elif (computerinput == 3):
        print('Computer chose Scissors!')
        computerinput = "scissors"
    else:
        print('A fatal error has occurred during the computer phase')
    # --------------------------------------------------------------------------------------
    if (userinput == computerinput):
        print('It\'s a draw!', computer_score, ' to ', user_score)
        print("\t")
        continue
    
    elif (userinput == "rock" and computerinput == "paper"):
        win = False
    elif (userinput == "paper" and computerinput == "scissors"):
        win = False
    elif (userinput == "scissors" and computerinput == "rock"):
        win = False

    elif (userinput == "paper" and computerinput == "rock"):
        win = True
    elif (userinput == "scissors" and computerinput == "paper"):
        win = True
    elif (userinput == "rock" and computerinput == "scissors"):
        win = True
    else:
        print('A fatal error has occurred during the last phase')
    # --------------------------------------------------------------------------------------
    if (win == False):
        print('Computer Wins!')
        computer_score += 1
        print('The scores are: ', computer_score, ' to ', user_score)
        print ("\t")
    elif (win == True):
        print('User Wins!')
        user_score += 1
        print('The scores are: ', computer_score, ' to ', user_score)
        print ("\t")
    else:
        print('Error Posting Scores')
    # --------------------------------------------------------------------------------------
    continue

