my_foods = ['spaghetti', 'lasagna', 'salad', 'breadsticks']
friend_foods = my_foods[:]

my_foods.append('tiramisu')
friend_foods.append('gelato')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)