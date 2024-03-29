# პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.

# Create a variable containing all the consonants
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ' 

# Ask user to enter a word and convert it to uppercase to match the consonants
user_input = input("Please, enter a word: ")

# Initialize en empty string to store the output word containing only consonants
output_word = ''

# Iterate over each character in the user input and append consonants to the output_word
for c in user_input:
    if c.upper() in CONSONANTS:
        output_word += c

# Print the output after converting it to lowercase
print(output_word)
