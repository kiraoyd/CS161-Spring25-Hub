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