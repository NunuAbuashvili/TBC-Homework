# პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა. დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი.

# Ask user to enter a word
user_input = input("Please, enter a word: ")

# Initialize en empty string to store the output word
output_word = ''

# Iterate over each character in the user input
for i in range(len(user_input)):
    # Append characters with an even index, except the "e" character, to the output_word
    if i % 2 == 0 and user_input[i] != "e":
        output_word += user_input[i]

print(output_word)
