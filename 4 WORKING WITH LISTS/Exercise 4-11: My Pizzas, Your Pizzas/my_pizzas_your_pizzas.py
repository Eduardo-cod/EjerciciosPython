pizzas = ['pepperoni', 'mushroom', 'pineapple', 'sausage', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('beef')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)