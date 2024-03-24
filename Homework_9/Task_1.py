# დაწერეთ პროგრამა, რომელიც მიიღებს სტრიქონს და დაადგენს ეს ტექსტი არის თუ არა პალინდრომი. პალინდრომი არის სიტყვა, რომელიც მარცხნიდან და მარჯვნიდან ერთნაირად იკითხება. მაგალითად: radar, level, racecar არის პალინდრომები. პროგრამამ უნდა დააიდენტიფიციროს პალინდრომი წინადადებაც. წინადადებიდან უნდა უგულებელყოს ყველა სიმბოლო, გარდა ინგლისური სიმბოლოსებისა a-z, A-Z. პროგრამამ უნდა უგულებელყოს სიმბოლოს რეგისტრი. 

# Ask user to enter a string and convert it to lowercase
user_input = input("Please, enter a string: ").lower()

# Initialize an empty string to store the alphabetic characters from the user input
user_string = ''

# Iterate through each character in the user input, and if the character is alphabetic, add it to the user_string
for c in user_input:
    if c.isalpha() == True:
        user_string += c

# Check if the cleaned string is a palindrome and print a corresponding message
if user_string[::-1] == user_string:
    print("The word/phrase you've entered is a palindrome")
else:
    print("The word/phrase you've entered is not a palindrome")
