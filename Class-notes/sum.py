

def sum_sequence(n):
    count = 1
    my_sum = 0
    while count <= n:
        #do something
        my_sum = my_sum + count
        count = count + 1

    print(f"The sum of 1 to {n} is {my_sum}")

def main():
    n = 100000000
    sum_sequence(n)

main()