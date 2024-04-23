# (8 ქულა) დაწერეთ პროგრამა, რომელიც მოხმარებელს მოსთხოვს შეიყვანოს მთელი რიცხვი n, სადაც 100 <= n < 1000. თუ მომხმარებელი შეიყვანს არასწორ რიცხვს, ეკრანზე დაბეჭდეთ, რომ პროგრამას გადმოეცა არასწორი რიცხვი და შეწყვიტეთ პროგრამის მუშაობა. თუ მომხმარებელი შეიყვანს სწორ რიცხვს, პროგრამამ უნდა იპოვოს ყველა 13-ის ჯერადი რიცხვი 1-დან n-მდე. ეკრანზე დაბეჭდოს ეს რიცხვები და მათი საერთო რაოდენობა.

# Prompt user to enter number in range of 100 (inclusive) and 1000 (exclusive)
n = int(input("Please, enter a number (100 <= number < 1000): "))

# Check if the input number is within the valid range    
if n < 100 or n >= 1000:
    print("Invalid input, try again!")
    exit()

count_of_multiples = 0
print("Multiples of 13:", end=" ")

for i in range(1, n):
    if i % 13 == 0:
        print(i, end = " ") # Multiples of 13
        count_of_multiples += 1 # Number of the multiples

print(f"\nThere are {count_of_multiples} multiples of 13 from 1 to {n}")
