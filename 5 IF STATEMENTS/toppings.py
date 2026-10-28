#This program demonstrates the use of if statements in Python.
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Here's a version of the program that uses a list to hold multiple toppings that have been requested.
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Here's a version of the program that uses an if-elif-else chain to determine which toppings have been requested.
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")