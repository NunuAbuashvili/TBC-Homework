# დაწერეთ პროგრამა, რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 10000 და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას და ამ რიცხვში შემავალი ციფრების ჯამს. გამოიყენეთ while ციკლი. მაგალითი: enter number: 7923 reversed number is 3297 sum of digits: 21

# Ask user to enter a number between 0 and 1000
num = int(input("Enter a whole positive number between 0 and 10000: "))

# Check if the number is within the valid range
while num < 0 or num >= 10000:
    num = int(input("Invalid input, the number should be between 0 and 10000, try again! - "))

# Initalize variables to store the reversed number and the sum of digits
sum_digits = 0
num_reversed = 0

print(f"Reversed number of {num} is:", end=" ")

while num != 0:
    # Extract the last digit
    digit = num % 10
    
    # Add the last digit to the reversed number and print the result
    num_reversed = digit
    print(num_reversed, end="")
    
    # Add the last digit to the sum of digits
    sum_digits += digit
    
    # Remove the last digit from the number
    num = num // 10
    
print(f"\nSum of digits is: {sum_digits}")
