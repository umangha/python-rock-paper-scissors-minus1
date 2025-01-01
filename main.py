
# Trying to make a simple Rock, Paper, Scissor Minus One Game

import os
import random
from art import rock,paper,scissors,logo

# Clears the terminal screen
def clear():
    '''Clears the terminal screen '''
    os.system('cls' if os.name == 'nt' else 'clear')

def final_game():
    '''Main Game Logic Function'''
    #creating a list of rock , paper and scissors derived from "art.py"
    options=[rock,paper,scissors]

    clear()
    print(logo)
    # Asking the user to input their choice 2 times
    user_choice_1=int(input("Enter 2 times!! Enter 0 for rock, 1 for paper and 2 for scissor: "))
    user_choice_2=int(input())

    # Randomly selecting the play of computer from the list options 
    # Doing 2 times because of the rock, paper scissor minus 1 game
    computer_choice_1=random.randint(0,2)
    computer_choice_2=random.randint(0,2)

    # Error validating for wrong input by user
    if (user_choice_1 >=3 or user_choice_1 <0) and (user_choice_2 >=3 or user_choice_2 <0):
        print("Enter valid Choice from 0 for rock, 1 for paper and 2 for scissor!!!")
    else:
        ## Print the User's Choices
        # print(f"User's Choices: {options[user_choice_1]}{options[user_choice_2]}")

        # Printing the Computer Choices 
        print(f"Computer's Choices: {options[computer_choice_1]}{options[computer_choice_2]}")

        # Getting the user's choice
        final_user_choice = int(input(f"Enter your final choice from the 2 choices you made : \nEnter {user_choice_1} for {options[user_choice_1]} OR {user_choice_2} for {options[user_choice_2]}"))

        # List containing the 2 choices made randomly by computer
        computer_choices = [computer_choice_1,computer_choice_2]
        # Selects one outcome randomly from its two options from previous step
        final_computer_choice = random.choice(computer_choices)

        print(final_user_choice,final_computer_choice)

        # Clear the screen before
        clear()
        # Final User Vs Computer Outcome
        print(f"User's Final Choice: {options[final_user_choice]}")
        print(f"Computer's Final Choice: {options[final_computer_choice]}")

        # Final Game Logic
        if final_user_choice == 0 and final_computer_choice == 2:
            print("\nYou Win!!!!!!!!!!!")
        elif final_computer_choice == 0 and final_user_choice == 2:
            print("\nYou Lose!!!")
        elif final_computer_choice > final_user_choice:
            print("\nYou Lose!!!")
        elif final_user_choice > final_computer_choice:
            print("\nYou Win!!!!!!!!!!!")
        else:
            print("It's a DRAW")

# First run
final_game()

# Run until user enters 'n'
status = True
while status:
    continue_game = input("Enter 'y' to continue or 'n' to exit :")
    if continue_game == 'n':
        status = False
    else:
        final_game()
