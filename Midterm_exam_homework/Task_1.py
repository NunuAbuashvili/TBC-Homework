# დაწერეთ თამაში rock, paper, scissor. დაწერეთ ფუნქცია, რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S. დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S. შეადარეთ ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო და გამოავლინეთ გამარჯვებული. თამაში მთავრდება მაშინ, როდესაც ერთ-ერთი მოიპოვებს 3 ქულას.
# R ამარცხებს S
# S ამარცხებს P
# P ამარცხებს R

import random

# Define a constant string that contains the symbols for the game
SYMBOLS_SET = 'RPS'

def generate_random_symbol(symbols: str):
    # This function returns a randomly selected symbol from the provided set
    
    i = random.randint(0, 2)
    return symbols[i]

def determine_winner(player_choice, computer_choice):
    # This function determines the winner based on the players choice and the computer's choice
    
    # 1. Tie
    if player_choice == computer_choice:
        return 'Tie'
    # 2. Player wins
    elif (player_choice == 'R' and computer_choice == 'S') or (player_choice == 'S' and computer_choice == 'P') or (player_choice == 'P' and computer_choice == 'R'):
        return 'Player'
    # 3. Computer wins
    else:
        return 'Computer'

def main():
    # This is the main function that runs the Rock, Paper, Scissors game
    
    player_score = 0
    computer_score = 0
    winning_score = 3
    
    print("Let's play Rock, Paper, Scissors!")
    
    # Game continues until one side reaches the winning score
    while player_score < winning_score and computer_score < winning_score:
        player_choice = input("Please, enter your choice (R/P/S): ").upper()
        
        # Validate the player's input
        while player_choice != 'R' and player_choice != 'P' and player_choice != 'S':
            player_choice = input("Unknown choice! Please, enter 'R', 'P' or 'S':  ").upper()

        computer_choice = generate_random_symbol(SYMBOLS_SET)
        
        # Print the symbols chosen by the player and the computer
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner of each round and update the relevant score
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'Player':
            print("You win!")
            player_score += 1
        elif winner == 'Computer':
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        # Print the score after each round
        print(f"Player score: {player_score}, Computer score: {computer_score}")
    
    # Print the final result for the player (win or loss)
    if player_score == 3:
        print("Congratulations! You won the game.")
    else:
        print("Sorry, computer won the game.")

if __name__ == "__main__":
    main()
