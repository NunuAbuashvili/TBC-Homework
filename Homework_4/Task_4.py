# დაწერეთ პროგრამა, რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20. პროგრამამ უნდა იპოვოს მიმდევრობის n-ური წევრი. მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. 

# Ask user to enter a positive whole number between 0 (inclusive) and 20
n = int(input("Enter a positive whole number between 0 (inclusive) and 20: "))

# Check if input is within the valid range
if n < 0 or n >= 20:
    print("Wrong number, try again!")
# If n = 0 or n = 1
elif n == 0:
    print("The 0th term of this sequence is 0")
elif n == 1:
    print("The 1st term of this sequence is 1")
    
else:
    # Initialize first two numbers of Fibonacci series
    a = 0
    b = 1
    
    # Print first two numbers
    print(a, b, end=" ")
    
    # Initialize the loop
    for i in range(2, n + 1):
        # Calculate the value of the next term in the sequence and store it as variable 'c'
        c = a + b
        # Print this value in the same line as the first two terms
        print(c, end=" ")
        
        # Update the values of 'a' and 'b' variables
        a = b # 'a' is set to current value of 'b'
        b = c # 'b' is set to current value of 'c'
        
    print("- The", n, "th term of this sequence is", b)
