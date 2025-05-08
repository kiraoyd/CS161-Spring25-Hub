
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Coin Flip Monte Carlo Probability
# To run: open the terminal, type python3 coin.py
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "coin.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment

import random
MAX_TRIALS = 100000

count = 0
tally = 0
while count < MAX_TRIALS:
    #flip coin
    coin = random.randint(1,2) #1 is heads, 2 is tails
    #check to see if we landed on heads
    if coin == 1:
        tally = tally + 1
    count = count + 1

probability = (tally / MAX_TRIALS) * 100
print(f"The probability is: {probability}%")
    