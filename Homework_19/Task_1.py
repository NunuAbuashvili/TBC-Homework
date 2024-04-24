# დააგენერირეთ 100 ცალი შემთხვევითი რიცხვი. გააკეთეთ ლექსიკონი ორი გასაღებით even და odd, მათი მნიშვნელობა უნდა იყოს ლუწი და კენტი რიცხვების რაოდენობები დაგენერირებული 100 რიცხვიდან.

import random

def generate_random_numbers(quantity: int, below_range: int, upper_range: int) -> list:
    # This function generates <quantity> random numbers in range of (below_range, upper_range) and returns them as a list
    random_numbers = []
    for _ in range(quantity):
        random_numbers.append(random.randint(below_range, upper_range))
    
    return random_numbers

def main():
    random_numbers = generate_random_numbers(100, 1, 1000)
    
    even_count = 0
    odd_count = 0
    
    for number in random_numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Dictionary with two keys: 'Even' with a value of the quantity of even numbers, and 'Odd' with a value of the quantity of odd numbers 
    even_odd_count_dictionary = {'Even': even_count, 'Odd': odd_count}
    
    print(even_odd_count_dictionary)

if __name__ == "__main__":
    main()
