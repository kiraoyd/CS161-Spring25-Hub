import math
PI = math.pi

def welcome_message(name):
    print(f"Hello {name}!")
    print("Welcome to the pizza calculator program.")

def get_name():
    name = input("What is your name? >>> ")
    return name

def get_size(order):
    diameter = float(input(f"Enter the size of the {order} pizza >>> "))
    return diameter

def get_price(order):
    price = float(input(f"Enter the price of the {order} pizza >>> "))
    return price

def calculate_pizza_cpsi(pizza_size, pizza_price):
    radius = pizza_size / 2
    surface_area = PI * (radius * radius)
    cpsi = pizza_price / surface_area
    return cpsi

def compare_pizzas(pizza_1, pizza_2):
    result = 0 #assume they are the same value
    if pizza_1 < pizza_2:
        #pizza 1 is the better deal, set result to 1
        result = 1
    elif pizza_2 < pizza_1:
        #pizza 1 is the better deal, set result to 2
        result = 2
    else:
        #if one pizza cpsi is not less than the other, they must be the same
        result = 0 #doesn't hurt to reset the value in result here 

    #return the final result
    return result     

def main():
    #...welcome the person
    person = get_name() 
    welcome_message(person)

    #...get the size and price for the first pizza
    size_1 = get_size("first")
    price_1 = get_price("first")

    #get the size and price for the second pizza
    size_2 = get_size("second")
    price_2 = get_price("second")
  
    #...calculate cost_per_square_inch (cpsi) of the first pizza
    value_pizza_1 = calculate_pizza_cpsi(size_1, price_1)

    #calculate cost_per_square_inch (cpsi) of the second pizza
    value_pizza_2 = calculate_pizza_cpsi(size_2, price_2)

    #round the cost per square inch for the first pizza
    rounded_result_1 = round(value_pizza_1, 2)
    print(f"The cost per square inch of the first pizza is: {rounded_result_1}")

    #round the cost per square inch for the second pizza
    rounded_result_2 = round(value_pizza_2, 2)
    print(f"The cost per square inch of the second pizza is: {rounded_result_2}")

    #call and use your new pizza comparison function
    value = compare_pizzas(rounded_result_1, rounded_result_2)
    if value == 1:
        print("The first pizza is the better deal!")
    elif value == 2:
        print("The second pizza is the better deal!")
    else:
        print("Both pizzas are the same value, either is a great choice.")
    
    #...say goodbye
    print("Goodbye!")


main()