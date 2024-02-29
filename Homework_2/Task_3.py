# დაწერეთ პროგრამა, რომელიც მიიღებს მთელ რიცხვს. პროგრამამ უნდა დაბეჭდოს ყველა მარტივი გამყოფი ერთ ხაზზე. შემოსული რიცხვის მაქსიმალური მნიშვნელობა უნდა იყოს 10. მაგალითი: თუ პროგრამას გადავეცით 6, გამოსავალზე უნდა დაიბეჭდოს 2, 3. ახსნა: 6 იყოფა 2-ზეც და 3-ზეც. 2 და 3 არის მარტივი რიცხვები. დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.

# Ask the user to enter a whole number from 1 to 10
num = int(input("Enter a whole number from 1 to 10: "))

# Check if the number the user has entered is a valid number
if num < 1 or num > 10:
    print("Incorrect number! Please, try again.")

# Check for prime multiples using nested if statements
else:
    print("The number's prime multiples are:", end=" ")
    if num % 2 == 0 and num != 2:
        print("2", end=" ")
        if num % 3 == 0 and num != 3:
            print("3", end=" ")
        elif num % 5 == 0 and num != 5:
            print("5")
    elif num % 3 == 0 and num != 3:
        print("3", end=" ")
        if num % 5 == 0 and num != 5:
            print("5")
    elif num % 5 == 0 and num != 5:
        print("5")
    else:
        print("1 and the number itself.")
