# Ask the user to enter the lengths of the triangle's sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the perimeter of the triangle's sides (P = a + b + c)
perimeter = a + b + c

# Calculate the area of the triangle using the heron's formula
s = perimeter / 2
area = (s * (s - a) * (s - b) * (s - c)) **0.5

# Print the output
if a <= 0 or b <= 0 or c <=0:
    print("Invalid number! Please, try again.")
# Determine if three side lengths can make a triangle using the Triangle Inequality Theorem, which states that the sum of two side lengths of a triangle is always greater than the third side. 
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("That's not a triangle! Please, enter valid numbers.")
else:
    print("The perimeter of the triangle is", perimeter)
    print("The area of the triangle is", area)
