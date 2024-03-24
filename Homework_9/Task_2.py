# დაწერეთ პროგრამა, რომელიც მიიღებს ორ სტიქონს. პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი ერთი სტრიქონის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.

# Ask user to input two strings and convert them to lowercase
string_one = input("Please, enter the first string: ").lower()
string_two = input("Please, enter the second string: ").lower()

# Initialize a flag to track if it's possible to obtain string_two from string_one
possible = False

# Check if symbols (including spaces inside the string) are equal
if len(string_one.strip()) == len(string_two.strip()):
    
    # Iterate through each character in string_two
    for c in string_two:
        # If the current character is not in string_one or if its count in string_two is greated than its count in string_one
        if c not in string_one or string_two.count(c) > string_one.count(c):
            possible = False
        else:
            possible = True

# Print if it's possible to obtain string_two from string_one or vice-versa
print("Is it possible to use characters from one string to obtain another string?", end=" ")          
  
if possible == True:
    print("YES")
else:
    print("NO")
