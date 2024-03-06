# დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს. პროგრამამ უნდა იპოვოს და ეკრანზე ერთ ხაზზე დაბეჭდოს ამ რიცხვის ყველა გამყოფი. 0 < n < 1000. 

# Ask user to enter a positive whole number from 0 to 1000
number = int(input("Enter a whole positive number from 0 to 1000: "))

# Check if input is within the valid range
if number <= 0 or number >= 1000:
    print("Wrong number, try again!")
    
# Print all divisors of the number
else:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end = " ")
