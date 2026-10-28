#This program determines the cost of admission to an amusement park based on a person's age.
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#Here's a version of the program that uses a variable to hold the price, and then prints the price at the end of the program.
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#Here's a version of the program that adds a third age group, for senior citizens who are 65 or older.
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#Here's a version of the program that uses the elif chain to determine the price for each age group, and then prints the price at the end of the program.
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")