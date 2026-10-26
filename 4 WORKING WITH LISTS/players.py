#this program creates a list of players and then prints the first three players in the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#this program creates a list of players and then prints the second through fourth players in the list
print(players[1:4])

#this program creates a list of players and then prints the last three players in the list
print(players[:4])

#this program creates a list of players and then prints the last three players in the list
print(players[2:])

#this program creates a list of players and then prints the last three players in the list
print(players[-3:])

print('\nHere are the first three players on my team:')
for player in players[:3]:
    print(player.title())