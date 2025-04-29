
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Can I Watch Deadpool?
# To run: open the terminal, type python3 deadpool.py
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "deadpool.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment

import random
def rated_r_approved(age, roll):
    old_enough = False #assume not old enough
    #Job of the function is to determine if the person is old enough
    #determine if the person rolled a 6 and age doesn't matter
    if roll < 6:
        old_enough = True
    else:
        if age >= 17:
            #they are old enough!
            old_enough = True
        else:
            #not old enough
            old_enough = False
            
    return old_enough

def main():
    age = int(input("Please enter your age in years: "))
    #illegal die roll to let anyone in if they roll a 6
    roll = random.randint(1,6)
    print(f"you rolled a {roll}")

    old_enough = rated_r_approved(age, roll)

    if old_enough == True:
        print("You are old enough hurrah!")
    else:
        print("You're too young.")
main()
              


    



