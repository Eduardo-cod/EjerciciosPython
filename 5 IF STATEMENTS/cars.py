#This program demonstrates the use of if statements to check for a specific condition in a list of cars. It will print the name of the car in uppercase if it is 'bmw', and in title case for all other cars.
cars = ['audi', 'bmw', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())