
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:
# DATE:
# CLASS:
# Program Title: Average of User Data
# To run: open the terminal, type python3 average.py
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "average.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment

def calculate_average():
    average = 0
    my_sum = 0
    count = 0

    number = int(input("Enter data one at a time, enter a -1 to stop: "))
    while number != -1:
        my_sum = my_sum + number #add the new data to the total
        count = count + 1 #tally up the data

        #get a new piece of data, it might be the terminating value of -1
        number = int(input("Enter data one at a time, enter a -1 to stop: "))

    #After the loop breaks, we have all the info we need to calculate the average
    #but only if we got data entered, if there was no data entered
    if my_sum != 0 and count != 0:
        average = my_sum / count
    else:
        average = -1 #error flag, no data entered

    return average
        
                
def main():
    result = calculate_average()
    if result > 0:
        print(f"The average of all data entered is: {result}")
    else:
        print("No data was entered.")


main()
