# დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n. პროგრამამ უნდა დააგენერიროს n ცალი შემთხვევითი მთელი რიცხვი 0 – 1000 დიაპაზონიდან და ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30.

# Another solution using list - ვიფიქრე, რომ list-ის გამოყენებით უკეთესი იყო ამ ამოცანის ამოხსნა, რადგან list საშუალებას გვაძლევს თვალი ვადევნოთ არა მხოლოდ მაქსიმალურ რიცხვს, არამედ პროგრამის მიერ დაგენერირებულ ყველა რიცხვს.
import random

# Ask user to enter a positive whole number between 0 and 30
number = int(input("Enter a positive whole number between 0 and 30: "))

# Make an empty list
random_numbers_list = []

# Check if input is within the valid range
if number <= 0 or number >= 30:
    print("Invalid input, try again!")
    
else:
    for _ in range(number):
        # Generate random numbers between 0 and 1000 and add them to the list
        random_number = random.randint(0, 1000)
        random_numbers_list.append(random_number)

    # Find maximum number in the list
    max_number = max(random_numbers_list)

    # Print output
    print("Generated random numbers:", random_numbers_list)
    print("Maximum number among them:", max_number)
