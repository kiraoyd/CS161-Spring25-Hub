
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Luggage Calculator SOLUTION
# To run: open the terminal, type the follow command and hit enter:  python3 EXTRA_luggage_SOLUTION.py
############################################################################

# Scroll down to line 50 to view one possible solution


































#--------------SOLUTION CODE BELOW ------------------------------------#



def welcome(name):
    print(f"Welcome to the luggage volume calculator program, {name}!")

def get_height():
    print("Please enter the height for your luggage: ")
    height = float(input())
    return height

def get_width():
    print("Please enter the width for your luggage: ")
    width = float(input())
    return width

def get_length():
    print("Please enter the length for your luggage: ")
    length = float(input())
    return length

def calculate_volume(height, width, length):
    volume = height * width * length
    return volume

def goodbye(name):
    print(f"Goodbye {name}!")

def main():
    print("Hello!")
    print("What is your name?")
    name = input()
    welcome(name)
    luggage_height = get_height()
    luggage_width = get_width()
    luggage_length = get_length()

    final_volume = calculate_volume(luggage_height, luggage_width, luggage_length)

    print(f"The total volume of your {luggage_height} x {luggage_width} x {luggage_length} luggage is: {final_volume}")

    goodbye(name)

main()




