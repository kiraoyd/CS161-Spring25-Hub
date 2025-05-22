


def main():

    data = []
    
    #input loop to put data in the list
    item = int(input("Enter a positive integer, type -1 to stop: "))
    while item != -1:
        data.append(item)
        item = int(input("Enter a positive integer, type -1 to stop: "))

    #now we have a list called data, full of information

    #traverse the list
    #calculate the sum of all data items in the list
    #we need to figure out how many data items in the list

    length = len(data) #how many items are in the list
    last_index = length - 1 #this is the value of the last index
    index = 0 #start at the begining of the list
    my_sum = 0 #to hold the calculated sum
    while index <= last_index:
        #each data item needs to be added to a sum
        my_sum = my_sum + data[index]

        #move on to the next index
        index = index + 1

    #Now we have a sum of all data, and we know how many items are in the list
    average = my_sum / length
    print(f"The average of all data is: {average}")

main()
    
    
    
    