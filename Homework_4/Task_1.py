# დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას. პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი კამათლების წყვილი და დაბეჭდოს ეკრანზე.
import random

# Ask user to enter the number of players
players_number = int(input("Enter the number of players: "))

# Roll dice for the players
if players_number <= 0:
    print("There should be at least one player!")
else:
    for _ in range(players_number):
        # Generate two dice numbers
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        # Print the output
        print(dice_one, dice_two)
