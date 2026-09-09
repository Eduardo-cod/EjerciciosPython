guest_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Alice can't make it to dinner, so we need to replace her with a new guest
guest_list[0] = "Frank"
print("\nUpdated guest list:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner.")

guest_list.insert(0, "Grace")
guest_list.insert(2, "Hannah")
guest_list.append("Ian")

print("\nNew guests:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner.")