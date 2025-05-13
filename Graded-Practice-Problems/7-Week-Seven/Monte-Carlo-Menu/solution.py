import random

def coin_flip():
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
    print("Welcome to my Monte Carlo Simulation Program!")
    print("Type 1 to run coin flip, Type 2 to run snake eyes, type 0 to quit.")
    choice = int(input())
    while choice != 0:
        if choice == 1:
            coin_flip()
        elif choice == 2:
            trials = int(input("Please enter number of trials you wish to run: "))
            result = snake_eyes_sim(trials)
            print(f"The probability of rolling snake eyes is: {result}.")
        else:
            print("sorry that wasn't a choice from the menu. Please try again.")

        print("Type 1 to run coin flip, Type 2 to run snake eyes, type 0 to quit.")
        choice = int(input())

    print("Thanks for using my program, goodbye!")

main()
        
            





