def countdown(num): #lets imagine num = 3
    #display every number in the sequence from num to 1
    #display "Liftoff!"
    count = num # count starts at 3
    while count >= 1:
        print(count)
        count = count - 1

    print("Liftoff!")


#Solution for the Sequence problem
def show_sequence(up_to):
    count = 1
    while count <= up_to:
        print(count)
        count = count + 1

    print("Goodbye!")

def main():
    num = int(input("enter a number: "))
    show_sequence(num)


main()
              
    