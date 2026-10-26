#This program demonstrates how to define a tuple and access its elements. It also shows that tuples are immutable, meaning their elements cannot be changed after they are created.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print()
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

# This will cause an error because tuples are immutable
#dimensions[0] = 250
#print(dimensions[0])