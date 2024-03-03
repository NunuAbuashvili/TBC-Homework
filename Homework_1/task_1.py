# Ask the user for their name
user_name = input("Enter your name: ")

# Ask the user for their surname
user_surname = input("Enter your surname: ")

# Ask the user for their age
user_age = int(input("Enter your age: "))

# Print a greeting message
if user_age < 0:
    print("Invalid number! Please, enter your real age.")
else: 
    print("Hello,", user_name, user_surname, ", you are", user_age, "years old.")
