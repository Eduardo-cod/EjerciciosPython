magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

print("\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

'''
#muestra error Expected an indented block after 'for' statement on line 1
for magician in magicians:
print(magician)
'''