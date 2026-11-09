current_users = ['admin', 'user1', 'user2', 'user3', 'user4']

new_users = ['user5', 'user6', 'user7', 'user1', 'user2']

lower_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")