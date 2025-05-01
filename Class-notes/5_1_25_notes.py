#Are we there yet? EXAMPLE of a while loop
def are_we_there_yet():
    count = 0
    while miles_travelled < 3:
        print("Are we there yet?")
        count = count + 1 
    print("moving on...")

#-------- Tracing Excersize code ------
def eat():
    hunger = 10
    while hunger > 0:
        print("Eat more!")
        hunger = hunger - 3

def drink():
    thirst = 5
    while thirst > 0:
        print("Sip water...")
        thirst = thirst - 1
        
def main():
    drink()
    eat()

main()
    


