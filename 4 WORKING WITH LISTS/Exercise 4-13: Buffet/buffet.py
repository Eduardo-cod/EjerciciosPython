#This program creates a tuple of foods and then prints the original menu, modifies one of the items in the tuple, and then changes the menu by replacing two items in the tuple.
print('Original menu:')
foods = ('pizza', 'pasta', 'salad', 'soup', 'steak')
for food in foods:
    print(food)

print('\nmodify one of the items in the tuple')
foods = ('pizza', 'pasta', 'salad', 'soup', 'shrimp')
for food in foods:
    print(food)

print('\nchanged the menu, replacing two items in the tuple')
foods = ('pizza', 'tacos', 'salad', 'curry', 'shrimp')
for food in foods:
    print(food)