# დაწერეთ პროგრამა რომელიც გაშვებისას დაბეჭდავს ბანქოს შემთხვევით მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა: 4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠)) და 13 მნიშვნელობა (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))
import random 

# Make two lists, one for the colours and one for the ranks
colours_list = ["♣", "♦", "♥", "♠"]
ranks_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

# Choose a random colour
random_colour = random.choice(colours_list)

# Choose a random rank
random_rank = random.choice(ranks_list)

# Print the result
print("From a standard deck of 52 playing cards, you get", random_colour,  random_rank)