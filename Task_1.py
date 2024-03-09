# დაწერეთ პროგრამა, რომელიც მიიღებს ნატურალურ რიცხვს - n , სადაც 0 < n < 50 . პროგრამამ უნდა იპოვოს n მდე არსებული ყველა რიცხვის გამყოფი. დაბეჭდეთ მაქსიმუმ 3 ცალი გამყოფი.

# Ask the user to enter a natural number between 0 and 50
n = int(input("Enter a natural number between 0 and 50: "))

# Check if the number is within the valid range
if n <= 0 or n >= 50:
    print("Invalid input! Please enter a natural number between 0 and 50.")

else:
    for num in range(1, n + 1):
        # Print the number
        print(f"{num} -", end=" ")
        # Initialize the number of divisors to 0
        divisor_count = 0
        for divisor in range(1, n + 1):
            if num % divisor == 0:
                # Update the number of divisors
                divisor_count += 1
                # If the number of divisors exceeds 3
                if divisor_count > 3:
                    continue
                # Print the divisors
                else:
                    print(divisor, end=" ")
        print('')
