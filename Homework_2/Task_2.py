# დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს, დაადგენს პირველი რიცხვი არის თუ არა მეორე რიცხვის ჯერადი და დაბეჭდავს ეკრანზე. A რიცხვს ეწოდება B რიცხვის ჯერადი, თუ A = B * n, სადაც n ნატურალური რიცხვია.

# Ask the user to enter two numbers
print("Enter two numbers and I will tell you if the first number is a multiple of the second number!")
a = float(input("Please, enter the first number: "))
b = float(input("Please, enter the second number: "))

# Check if the first number is a multiple of the second number
if b % a == 0:
    print("The first number is a multiple of the second number.")
else:
    print("The first number is not a multiple of the second number.")
