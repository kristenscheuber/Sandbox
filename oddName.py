"""
Kristen Scheuber

Ask the user for their name, error-check to make sure their name is not blank then print every second letter
of their name.
"""

user_name = input("Your Name: ")
while user_name == "":
    user_name = input("Your Name: ")
print(user_name[::2])