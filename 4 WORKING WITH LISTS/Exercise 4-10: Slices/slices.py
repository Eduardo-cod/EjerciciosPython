slices = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

print("The first three items in the list are:")
for slice in slices[:3]:
    print(slice.title())

print('\nThe middle three items in the list are:')
for slice in slices[1:4]:
    print(slice.title())

print('\nThe last three items in the list are:')
for slice in slices[2:5]:
    print(slice.title())