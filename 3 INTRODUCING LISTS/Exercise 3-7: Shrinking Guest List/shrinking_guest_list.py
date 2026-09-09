guest_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
guest_list[0] = "Frank"

guest_list.insert(0, "Grace")
guest_list.insert(2, "Hannah")
guest_list.append("Ian")

print("\nNew guests:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner.")

print("\nUnfortunately, we can only invite two guests to dinner.")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print("\nThe following guests are still invited to dinner:")
for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner.")

del guest_list[0]
del guest_list[0]
print("\nThe guest list is now empty:", guest_list)