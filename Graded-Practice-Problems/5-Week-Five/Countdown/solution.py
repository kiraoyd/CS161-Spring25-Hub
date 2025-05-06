#Solution for the Countdown problem





def countdown(num): #lets imagine num = 3
    #display every number in the sequence from num to 1
    #display "Liftoff!"
    count = num # count starts at 3
    while count >= 1:
        print(count)
        count = count - 1

    print("Liftoff!")

def main():
    start = int(input("Enter a number to start the countdown: "))
    countdown(start)

main()