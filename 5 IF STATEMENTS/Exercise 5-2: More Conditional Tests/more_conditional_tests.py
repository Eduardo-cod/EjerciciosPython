#test for equality and inequality with strings
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#Tests using the lower() method
car = 'Audi'
print("\nIs car == 'audi'? I predict True.")
print(car.lower() == 'audi')

#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 30? I predict True.")
print(age < 30)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age <= 30? I predict True.")
print(age <= 30)

#Test whether an item is in a list
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in the list of fruits? I predict True.")
print('banana' in fruits)

#Test whether an item is not in a list
print("\nIs 'grape' not in the list of fruits? I predict True.")
print('grape' not in fruits)