"""
დაწერეთ პროგრამა, რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10. პროგრამამ უნდა დაბეჭდოს ქვემოთ მოცემული სტრუქტურა. გამოიყენეთ while

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

n = int(input("Enter the number between 0 and 10: "))

# Check if the number of raws is within the valid range
while n <= 0 or n >= 10:
    n = int(input("The number should be between 0 and 10, try again! - "))
    
# Printing rows in ascending order
i = 0 # Variable for iteration

while i < n:
    j = 1

    while j <= i + 1:
        
        print(j, end=" ")
        j += 1
        
    print() # Move to the next line
    i += 1 # Update the iteration
    
# Printing rows in descending order
i = n - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
        
    print() # Move to the next line
    i -= 1 # Update the iteration
