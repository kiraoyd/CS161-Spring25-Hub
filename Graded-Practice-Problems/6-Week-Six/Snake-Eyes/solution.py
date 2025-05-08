

import random

def snake_eyes_sim(trials):
    count = 0
    die1 = 0
    die2 = 0
    tally = 0
    while count < trials:
        #roll the die
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        #check for snake eyes
        if die1 == 1 and die2 == 1:
            #tally it
            tally = tally + 1
        count = count + 1

    probability = tally / trials
    return probability

def main():
    n = int(input("enter the number of trials to run, or type 0 to quit: "))
    while n != 0:
        prob = snake_eyes_sim(n)
        print(f"the probability of rolling snake eyes is: {prob}")
        n = int(input("enter the number of trials to run, or type 0 to quit: "))
        

main()
            
    