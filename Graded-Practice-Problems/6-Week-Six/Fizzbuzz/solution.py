
"""
Write a function that takes one positive, integer-valued argument, called n. The function should iterate over every number between 0 and n, inclusive, following the rules below:

If a number is divisible by 3, print "Fizz"

If a number is divisible by 5, print "Buzz"

If a number is divisible by 3 AND 5, print "FizzBuzz"

If a number does not meet any of the above criteria, simply display the number.
"""

def fizzbuzz(n):
    count = 1
    while count <= n:
        #do something with count
        if count % 3 == 0 and count % 5 == 0:
            print("Fizzbuzz")
        elif count % 5 == 0:
            print("Buzz")
        elif count % 3 == 0:
            print("fizz")
        else:
            print(count)
        count += 1

def main():
    n = int(input("Enter a number: "))
    fizzbuzz(n)

main()
