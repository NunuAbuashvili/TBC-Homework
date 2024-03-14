# დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს, დაადგენს პირველი რიცხვი არის თუ არა მეორე რიცხვის ჯერადი და დაბეჭდავს ეკრანზე. A რიცხვს ეწოდება B რიცხვის ჯერადი, თუ A = B * n, სადაც n ნატურალური რიცხვია.

# Ask the user to enter two numbers
print("Enter two numbers and I will tell you if the first number is a multiple of the second number!")
a = float(input("Please, enter the first number: "))
b = float(input("Please, enter the second number: "))

# Check if the first number is a multiple of the second number

# 1. When a is 0 and b is a positive number
if a == 0 and b > 0:
    print("Zero is multiple of every integer.")
# 2. When a is 0 and b is also 0 or a negative number
elif a == 0 and b <= 0:
    print("Zero can't be a multiple of a negative number or itself.")
# 3. When both a and b are positive numbers and a is more than b
elif a > 0 and b > 0 and a >= b:
    print("First number should be less than the second number, try again!")
# 4. When both a and b are negative numbers and b is more than a
elif a < 0 and b < 0 and b >= a:
    print("First number should be less than the second number, try again!")
# 5. If a is a multiple of b
elif b % a == 0:
    print(a, "is a multiple of", b)
# 6. If a is not a multiple of b
else:
    print(a, "is not a multiple of", b)
