guest_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")
print(f"Dear {guest_list[4]}, you are invited to dinner.")

# Alice can't make it to dinner, so we need to replace her with a new guest
guest_list[0] = "Frank"
print("\nUpdated guest list:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner.")