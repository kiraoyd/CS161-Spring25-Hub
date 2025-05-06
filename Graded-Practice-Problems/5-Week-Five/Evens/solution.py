
#show evens solution
def show_evens(up_to):
    count = 1
    while count <= up_to:

        #check to see if the number in count is even
        #if it is, print it
        if count % 2 == 0:
            print(count)
        #otherwise, don't print it
        count = count + 1

def main():
    n = int(input("Enter a number: "))
    show_evens(n)


main()
            