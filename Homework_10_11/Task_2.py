# დაწერეთ პროგრამა, რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1. პროგრამამ უნდა დააგენერიროს n ცალი წყვილი შემთხვევითი რიცხვი a,b, სადაც 0<a<1 და 0<b<1. შემოიღეთ მთვლელი counter, თუ დაგენერირებული რიცხვი აკმაყოფილებს პირობას math.sqrt(a ** 2 + b ** 2) <=1, counter-ის მნიშვნელობა გაზარდეთ 1-ით. ეკრანზე დაბეჭდეთ 4 * counter / n. გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 100000, 10000000. Რას ამჩნევთ?

import random
import math

# Ask user to enter a natural number greater than 1
n = int(input("Enter a natural number greater than 1: "))

# Ensure that the input value is greater than 1
while n <= 1:
    n = int(input("Invalid input! The number should be greater than 1: "))
 
# Initialize counter to 0   
counter = 0

# Generate n pairs of random numbers between 0 and 1
for _ in range(n):
    a = random.random()
    b = random.random()
    
    # Check if the values of 'a' and 'b' meet the condition
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

result = 4 * counter / n
print(result)

# როდესაც n = 10, result-ში მძიმის შემდეგ გვაქვს მხოლოდ ათეული, როდესაც n = 100, result-ში მძიმის შემდეგ გვაქვს ასეული და ა.შ. შესაბამისად, რაც უფრო მეტია n-ის მნიშვნელობა, მით უფრო ზუსტია მიღებული შედეგიც, რაც შემთხვევითობისა და შერჩევის უფრო დიდ რაოდენობასთანაა დაკავშირებული (Monte Carlo method to estimate the value of π). 
