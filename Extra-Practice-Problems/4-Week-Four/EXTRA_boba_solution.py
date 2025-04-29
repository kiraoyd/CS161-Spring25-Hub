import random

def show_order(tea, topping, milk):
    print("Try this boba tea today: ")
    if milk == "regular":
        print(f"{tea} tea with {topping}.")
    else:
        print(f"{tea} tea with {topping}, sub {milk} milk.")

def boba_maker(tea, non_dairy_milk):
    topping = ""
    non_dairy = "regular"
    if tea == "green":
        roll = random.randint(1,3)
        if roll == 1:
            topping = "lychee jelly"
        if roll == 2:
            topping = "grass jelly"
        if roll == 3:
            topping = "boba"

    if tea == "black":
        roll = random.randint(1,3)
        if roll == 1:
            topping = "boba"
        if roll == 2:
            topping = "aloe"
        if roll == 3:
            topping = "coconut jelly"
    if non_dairy_milk == 'yes':
        roll = random.randint(1,3)
        if roll == 1:
            non_dairy = "Almond"
        if roll == 2:
            non_dairy = "Coconut"
        if roll == 3:
            non_dairy = "Oat"

    show_order(tea, topping, non_dairy)
def main():
    print("Welcome to the boba tea order generator!")
    print("What kind of tea do you like? Type 'green' or 'black':")
    tea_type = input()
    print("Do you need non-dairy milk? Type 'yes' or 'no': ")
    non_dairy = input()
    boba_maker(tea_type, non_dairy)

main()