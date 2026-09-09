# Sort the list in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sort the list in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# Sort the list temporarily in alphabetical order
print("\nHere is the sorted list:")
print(sorted(cars))

# Show that the original list is still in its original order
print("\nHere is the original list:")
print(cars)
print("\nHere is the reversed list:")
cars.reverse()
print(cars)

# Show the length of the list
print("\nThe length of the list is:")
print(len(cars))