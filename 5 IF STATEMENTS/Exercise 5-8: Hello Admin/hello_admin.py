#This program checks if the list of users is empty. If it is not empty, it greets each user. If it is empty, it prompts to find users.
user_name = ['admin', 'user1', 'user2', 'user3', 'user4']

for user in user_name:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")