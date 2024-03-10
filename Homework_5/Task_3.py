# დაწერეთ პროგრამა, რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50. პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *, /, | და \ . 

# Create variables for the symbols that make up the Christmas Tree
top = "*"
left = "/"
central = "|"
right = "\\"

# Ask user to enter the height of the Christmas Tree
height = int(input("Enter the Christmas Tree 🎄 size between 0 and 50: "))

# Check if the number is within the valid range
if height <= 0 or height >= 50:
    print("Invalind input, the number should be between 0 and 50, try again!")

else:
    # Draw the Christmas Tree
    for i in range(height + 1):
        # Top *
        if i == 0:
            line = (" " * (height - i) + top)
        # Bottom |
        elif i == height:
            line = (" " * height + central)
        # Body with /, | and \
        else:
            line = (" " * (height - i)) + (i * left) + central + (i * right)
            
        print(line)
