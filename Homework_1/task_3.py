# Import math to use built-in math functions
import math

# Ask the user to enter the lengths of the triangle's sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the perimeter of the triangle's sides (P = a + b + c)
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# Calculate the area of the triangle using the heron's formula
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("The area of the triangle is", area)