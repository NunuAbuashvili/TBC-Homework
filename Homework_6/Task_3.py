# დაწერეთ პროგრამა, რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე. Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის. თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს, დაბეჭდეთ You are winner. თუ მომხმარებლის შემოყვანილი რიცხვი მეტია, კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. თუ მომხმარებლის შემოყვანილი რიცხვი ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ low. მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. თუ მომხმარებელმა 10 მცდელობაში ვერ გამოიცნო რიცხვი, დაბეჭდეთ Computer is winner.

import random
# User has ten tries
MAX_GUESSES = 10

# Target number in range of 0, 100
random_number = random.randint(0, 100)

# Print the rules
print("I have generated a random number between 0 and 100. Write a number and I will tell you if your guess is correct. You have 10 guesses in total!")

# Ask user to guess the number
input_number = int(input("Enter the number here: "))

# Create a variable to calculate how many times the user has made a guess and initalize it to 1
guesses = 1

while input_number != random_number:
    # If the user has exceeded the allowed number of guesses
    if guesses == MAX_GUESSES:
        print("You've exceeded the allowed number of guesses. Computer is the winner!")
        break
    # Update the number of attempts
    guesses += 1
    
    # If the user has entered a lower number
    if input_number < random_number:
        input_number = int(input("The number you've entered is lower than the target number 😞 Try again! - "))
    # If the user has entered a higher number
    elif input_number > random_number:
        input_number = int(input("The number you've entered is higher than the target number 😞 Try again! - "))

# If the user's guess is correct
if input_number == random_number:
    print("Congratulations! You are the winner 🥳")
