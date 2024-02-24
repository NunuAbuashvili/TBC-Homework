# Ask the user for their name
user_name = input("Enter your name: ")

# Ask the user for their birth year
user_birth_year = int(input("Enter your birth year: "))

# Create a variable to store the information of the current year
current_year = 2024

# Calculate the user's age
user_age = current_year - user_birth_year

# Print a greeting message
print("Hello, " + user_name + ", you are " + str(user_age) + " years old.")