# დაწერეთ პროგრამა, რომელიც მიიღებს ორ სტრიქონს. პროგრამამ უნდა შეამოწმოს პირველი სტრიქონის რომელიმე გადანაცვლებით მიიღება თუ არა მეორე სიტყვა. გადანაცვლების წესი შემდეგია: სიმბოლო უნდა გადანაცვლდეს თავში. გადანაცვლებული სტრიქონის გენერაციისთვის გამოიყენეთ ფუნქცია დავალება 1-დან.

# Import format_string function from the Task_1 file
from Task_1 import format_string

def main():
    # Ask user to enter two strings
    string_one = input("Enter the first word: ")
    string_two = input("Enter the second word: ")

    found = False
    
    # Iterate through the first string and check if the formatted string is equal to string_two
    for i in range(len(string_one)): 
        string_one = format_string(string_one)
        
        if string_one == string_two:
            found = True
            break
    
    # Print the result
    if found == True:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
  