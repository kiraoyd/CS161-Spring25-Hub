############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Least Exact Change SOLUTION
# To run: open the terminal, type the follow command and hit enter:  python3 EXTRA_change_SOLUTION.py
############################################################################

# Scroll down to line 50 to view one possible solution for the Least Exact Change problem


































#--------------SOLUTION CODE BELOW ------------------------------------#




import math

print("Welcome to the Least Exact Change calculator!")

#get the number of pennies to change as input
pennies = float(input("How many pennies do you have? "))

dollars = math.floor(pennies/100) #pull out as many dollars as you can, save the value
r = pennies - dollars*100 #reduce the total pennies by the dollars you took out

quarters = math.floor(r/25) #pull out as many quarters as you can, save the value
r = r - quarters*25 #reduce the total pennies by the quarters you took out

dimes = math.floor(r/10) #pull out as many dimes as you can, save the value
r = r - dimes*10# reduce the total pennies by the dimes you took out

nickels = math.floor(r/5) #pull out as many nickels as you can, save the value
r = r - nickels*5 #reduce the total pennies by the nickels you took out

#r now represents any leftover pennies
leftover_pennies = int(r) #convert to a whole number

print('\n') #displays a blank line in the output
print(f"Least Exact Change for {pennies} total pennies is: ")
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {leftover_pennies}")
print('\n') #displays a blank line in the output

print("Thanks for using the program, goodbye!")



