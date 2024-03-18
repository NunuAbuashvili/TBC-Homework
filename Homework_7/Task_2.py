# დაწერეთ პროგრამა, რომელიც მიიღებს დადებით მთელ რიცხვს - n. 0 < n <= 1000. პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა, რომელიც მიიღება შემდეგი პირობით: თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, ხოლო თუ რიცხვი კენტია ეს რიცხვი უნდა გავამრავლოთ 3-ზე და დავუმატოთ 1, იქამდე სანამ არ მივიღებთ 1-ს. მაგალითი: Enter number: 10 output: 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# Ask user to enter a number between 0 and 1000
n = int(input("Enter a whole positive number between 0 and 1000: "))

# Check if the number is within the valid range
while n <= 0 or n > 1000:
    n = int(input("Invalid input, the number should be between 0 and 1000, try again! - "))

# Print the number (as the first member of the sequence)
print(n, end=" ")

while n != 1: 
    # If the number is even
    if n % 2 == 0:
        n = n // 2
        print("->", n, end=" ")
    # If the number is odd
    else:
        n = n * 3 + 1
        print("->", n, end=" ")
