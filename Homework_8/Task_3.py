# პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, პირველი და შუა ასოები 5-ჯერ while ლუპით. თუ შემოყვანილი ტექსტის ზომა არის ლუწი, მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო.

# Ask user to enter a word
user_input = input("Please, enter a word: ")

# Calculate the length of the input word
input_length = len(user_input)

# Create variables for the first, middle and last characters
first_character = user_input[0]
last_character = user_input[-1]
middle_character = user_input[input_length // 2]
if input_length % 2 == 0:
    middle_character = user_input[input_length // 2 - 1] + middle_character

# Create a variable for the frequency of printing first, middle and last characters
repetition = 5 

# Initialize en empty string to store the output word
output_word = ''

i = 0

while i < input_length:
    j = 0
    while j < repetition:
        if i == 0:
            output_word += first_character
        elif i == input_length // 2:
            output_word += middle_character
        elif i == input_length - 1:
            output_word += last_character
        j += 1
        
    # Add a space after printing all the characters of each type
    if i < input_length:
        output_word += " "
    
    i += 1
    
print(output_word)
