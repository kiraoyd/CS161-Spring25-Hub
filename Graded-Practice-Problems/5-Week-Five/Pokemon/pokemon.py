
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Pokemon Picker
# To run: open the terminal, type python3 pokemon.py
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "pokemon.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment

import random

def roll_die():
    roll = random.randint(1,6)
    return roll


def choose_pokemon(number):
    if number == 1:
        print("I choose you, Squirtle!")
    elif number == 2:
        print("I choose you, Charmander!")
    elif number == 3:
        print("I choose you, Bulbasaur!")
    elif number > 3 and number <= 5:
        #This should handle any number between 3 and 5, not including 3
        print("Oh no, I still can't decide.")
    elif number > 5:
        print("Super secret glitch")

def main():
    print("Welcome!")
    roll = roll_die()
    #the number I rolled, is stored in the variable "roll"
    print(f"The roll is: {roll}.") #test print
    
    choose_pokemon(roll)
    print("goodbye!")

main()
















    





    