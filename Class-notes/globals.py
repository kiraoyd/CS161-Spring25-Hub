#Global Space
import math

#
MY_PI = math.PI
DAMAGE_MAX = 20

#making this global presents a problem:
#both eat() and drink() change the value stored
#This makes it hard to trace and track why and where drink_counter is being altered
drink_counter = 0 

def eat():
    global drink_counter
    hunger = 10
    while hunger > 0:
        print("Eat more!")
        hunger = hunger - 3

    drink_counter = 200


def drink():
    global drink_counter
    thirst = 5
    while thirst > 0:
        print("Sip water...")
        thirst = thirst - 1
        drink_counter = drink_counter + 1

        
def main():
    global drink_counter
    drink()
    eat()
    print(drink_counter)

main()