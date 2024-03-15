# დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n. პროგრამამ უნდა დააგენერიროს n ცალი შემთხვევითი მთელი რიცხვი 0 – 1000 დიაპაზონიდან და ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30.
import random

# Ask user to enter a positive whole number between 0 and 30
number = int(input("Enter a positive whole number between 0 and 30: "))

# Initialize maximum number to 0
max_number = 0

# Check if input is within the valid range
if number <= 0 or number >= 30:
    print("Invalid input, try again!")

else: 
    for _ in range(number):
        # Generate random numbers between 0 and 1000
        random_number = random.randint(0, 1000)
        # Compare randomly generated number to max_number and update max_number if a greater number is found
        if random_number > max_number:
            max_number = random_number
            
    # Print the maximum number among the generated random numbers
    print("Maximum number among the generated random numbers is", max_number)
