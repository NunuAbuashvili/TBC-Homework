# დაწერეთ პროგრამა, რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20. პროგრამამ უნდა იპოვოს მიმდევრობის 0-დან n-მდე წევრები. მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. გამოიყენეთ while ციკლი და არ შეიძლება list-ის გამოყენება. მაგალითი: Enter number: 5 output: 0 1 1 2 3
import sys

# Ask user to enter a positive number between 0 and 20
n = int(input("Enter a positive number between 0 and 20: "))

# Check if the number is inside the valid range, if not, exit the program
if n < 0 or n >= 20:
    print("The number should be between 0 and 20, try again!")
    sys.exit(1)

# Create variables for the first and second numbers of the fibonacci series
a = 0
b = 1

if n == 1:
    print(f"Fibonacci series up to the {n}st term is: ", end="")
else:
    print(f"Fibonacci series up to the {n}th term is: ", end="")
    
# Create a variable for iteration
i = 0

# Print the fibonacci sequence up to the 'n'th term
while i < n:
    print(a, end=" ")
    # Calculate the next term of the sequence
    c = a + b
    # Update 'a' and 'b' variables
    a = b
    b = c
    # Update the iteration
    i += 1
