"""
დაწერეთ პროგრამა, რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10. პროგრამამ უნდა დაბეჭდოს ქვემოთ მოცემული სტრუქტურა. გამოიყენეთ while

          0
        1 0 1
      2 1 0 1 2
    3 2 1 0 1 2 3
  4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4 5

"""

# Ask user to enter the number of rows
n = int(input("Enter a number between 0 and 10: "))

# Check if the number is within the valid range
while n <= 0 or n >= 10:
  n = int(input("The number should be between 0 and 10, try again! - "))
  
i = 0 # Variable for iteration

while i <= n:
  j = 0 # Variable for counter
    
  # The number of spaces on each row is equal to (the number of rows - the current number we are iterating over - 1)
  while j < (n - i):
    print(" ", end=" ")
    j += 1
    
  # Print numbers in descending order
  j = i 
  while j >= 0:
    print(j, end=" ")
    j -= 1
    
  # Print numbers in ascending order
  j = 1
  while j <= i:
    print(j, end=" ")
    j += 1
      
  print() # Move to the next line
  i += 1 # Update the iteration
