
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Main Program Menu
# To run: open the terminal, type python3 menu.py
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "menu.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment

def main():
    print("Welcome to my program!")
    print("Type 1 to run the program, type 2 to run a different program, type 0 to quit. Make a selection: ")
    choice = int(input())

    if choice == 1:
        print("Running the program....")
    elif choice == 2:
        print("run the second program")
    elif choice == 0:
        print("Thanks, goodbye. Program ending.")


main()
