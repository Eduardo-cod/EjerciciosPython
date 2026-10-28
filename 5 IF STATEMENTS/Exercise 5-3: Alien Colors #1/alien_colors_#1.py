#This program demonstrates the use of if statements in Python.
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points!")

# This prints nothing because alien_color is "red", but the condition only checks for "yellow".
alien_color = "red"

if alien_color == "yellow":
    print("You just earned 10 points!")