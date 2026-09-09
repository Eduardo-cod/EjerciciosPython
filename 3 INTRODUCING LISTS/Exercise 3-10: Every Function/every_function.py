languages_programming = ["Python", "C", "JavaScript", "Java", "C++"]

print(f"Original list: {languages_programming}")

print(f"Number of programming languages: {len(languages_programming)}")

print("\nSorted list of programming languages:")
print(sorted(languages_programming))

print("\nProgramming languages in reverse alphabetical order:")
print(sorted(languages_programming, reverse=True))

print("\nOriginal list after sorting:")
print(languages_programming)

print("\nReversed list of programming languages:")
languages_programming.reverse()
print(languages_programming)

print("\nReversed list again to restore original order:")
languages_programming.reverse()
print(languages_programming)

print("\nSort list of programming languages in place:")
languages_programming.sort()
print(languages_programming)

print("\nSort list of programming languages in reverse alphabetical order:")
languages_programming.sort(reverse=True)
print(languages_programming)

# Append a new programming language to the list
languages_programming.append("c#")
print(f"\nList after appending 'c#': {languages_programming}")

# Change a programming language at a specific index
languages_programming[1] = 'go'
print(f"\nList after changing the element at index 1 to 'go': {languages_programming}")

# Insert a new programming language at a specific index
languages_programming.insert(2, "ruby")
print(f"\nList after inserting 'ruby' at index 2: {languages_programming}")

# Remove a programming language from the list
languages_programming.pop()
print(f"\nList after popping the last element: {languages_programming}")

# Remove a specific programming language from the list
languages_programming.pop(1)
print(f"\nList after popping the element at index 1: {languages_programming}")

# Remove a specific programming language by value
languages_programming.remove("ruby")
print(f"\nList after removing 'ruby': {languages_programming}")

# Print the number of programming languages in the list
print(f"Number of programming languages: {len(languages_programming)}")
