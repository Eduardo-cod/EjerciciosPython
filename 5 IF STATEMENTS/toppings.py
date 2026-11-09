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
print()

#Here s a version of the program that uses a for loop to iterate through the list of requested toppings and print a message for each topping.
requested_topping = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_topping:
    print(f"Adding: {requested_topping}")

print("\nFinished making your pizza!")
print()

#Here s a version of the program that uses a for loop to iterate through the list of requested toppings and print a message for each topping, but also checks if a topping is out of stock.
requested_topping = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_topping:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding: {requested_topping}")

print("\nFinished making your pizza!")
print()

#Here s a version of the program that checks if the list of requested toppings is empty and prints a message if it is.
requested_topping = []

if requested_topping:
    for requested_topping in requested_topping:
        print(f"Adding: {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
print()

#Here s a version of the program that checks if each requested topping is available and prints a message for each topping.
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']

requested_topping = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_topping:
    if requested_topping in available_toppings:
        print(f"Adding: {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")