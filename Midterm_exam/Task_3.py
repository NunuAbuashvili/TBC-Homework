"""
3. (12 ქულა) დაწერეთ თამაში rock, paper, scissor. დაწერეთ ფუნქცია, რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S. დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S. სიმარტივისთვის შეგიძლიათ უგულებელყოთ ყველა შემოწმება მომხმარებლის ინფუთზე. შეადარეთ ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო და გამოავლინეთ გამარჯვებული. წესები: R ამარცხებს S, S ამარცხებს P, P ამარცხებს R, P P, R R, S S არის ფრე
"""
import random

def generate_random_symbol():
    # This function generates a random symbol 'R', 'P' or 'S'
    symbol_number = random.randint(1, 3)
    if symbol_number == 1:
        return 'R'
    if symbol_number == 2:
        return 'P'
    if symbol_number == 3:
        return 'S'

def main():
    # We get two symbols: one from the user, and one from the computer
    user_symbol = input("Let's play rock, paper and scissors. Please, enter 'R' for rock, 'P' for paper, and 'S' for scissors: ").upper()
    computer_symbol = generate_random_symbol()
    
    # Print the symbols
    print("User:", user_symbol)
    print("Computer:", computer_symbol)
    
    # 1. When there is no winner (draw)
    if user_symbol == computer_symbol:
        print("Result: Draw")
    else:
        # 2. When the user wins
        if user_symbol == 'R' and computer_symbol == 'S':
            print("User wins!")
        elif user_symbol == 'S' and computer_symbol == 'P':
            print("User wins!")
        elif user_symbol == 'P' and computer_symbol == 'R':
            print("User wins!")
        # 3. When the computer wins
        else:
            print("Computer wins!")

if __name__ == "__main__":
    main()
