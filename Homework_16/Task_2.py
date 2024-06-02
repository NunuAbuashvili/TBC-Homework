# დაწერეთ პროგრამა, რომელიც დააგენერირებს 50 ცალ შემთხვევით რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. პროგრამამ უნდა გადაუაროს სიას და თითოეული ელემენტისთვის ეს ელემენტი ჩაწეროს ახალ სიაში, იმდენჯერ, რაც არის მისი მნიშვნელობა. დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე.
import random

def generate_random_numbers(quantity: int, below_range: int, upper_range: int) -> list:
    # This function generates [quantity] random numbers in range of (below_range, upper_range) and stores them into an array
    
    random_numbers_array = []
    
    for _ in range(quantity):
        random_number = random.randint(below_range, upper_range)
        random_numbers_array.append(random_number)
    
    return random_numbers_array

def format_numbers_array(numbers: list):
    # This function takes an array of randomly generated numbers and creates a new array, where each number is repeated as many times as its value. It returns the new array, as well as its length
        
    formatted_array = []
    
    # Loop through each number in the input array
    for i in range(len(numbers)):
        # Append the current number to formatted_array as many times as its value
        for j in range(numbers[i]):
            formatted_array.append(numbers[i])
            
    length = len(formatted_array)
    return formatted_array, length
            
def main():
    random_number_array = generate_random_numbers(quantity = 50, below_range = 1, upper_range = 30)
    formatted_numbers_array, length_of_the_array = format_numbers_array(random_number_array)
    print('List -', formatted_numbers_array)
    print('Length -', length_of_the_array)      

if __name__ == "__main__":
    main()
