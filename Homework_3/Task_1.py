# დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს (x,y) და დაბეჭდავს რიცხვს რომელიც მიიღება x-ის y ხარისხში აყვანით.
import math

# Introduction
print("Enter two numbers and I will calculate the first number raised to the power of the second number")

# Ask the user to enter two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Calculate x raised to the power of y
_power = math.pow(x, y)

# Print the result
print(x, "raised to the power of", y, "is equal to", _power)