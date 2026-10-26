#This program creates a list of foods and then makes a copy of that list. It then adds new foods to both lists to show that they are separate lists. Finally, it demonstrates what happens when you try to assign one list to another without making a copy.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#Here we add new foods to both lists to show that they are separate lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print('')

#This doen't work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("This doesn't work:")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
