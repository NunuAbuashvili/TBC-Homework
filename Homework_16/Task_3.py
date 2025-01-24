# დაწერეთ პროგრამა, რომელიც დააგენერირებს 50 ცალ შემთხვევით რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. პროგრამამ უნდა გადაუაროს სიას და მოაშოროს ყველა დუპლიკატი. დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე.

# Import a function that generates [quantity] random numbers in range of (below_range, upper_range) and stores them into an array
from Task_2 import generate_random_numbers

def remove_duplicates(numbers: list):
    # This function takes an array of randomly generated numbers as a parameter, and removes duplicate elements in place. It returns the array and its length.
    
    for element in numbers.copy():
        while numbers.count(element) > 1:
            numbers.remove(element)
    
    length = len(numbers)
    return numbers, length

def main():
    random_numbers_array = generate_random_numbers(quantity = 50, below_range = 1, upper_range = 30)
    formatted_array, length_of_the_array = remove_duplicates(random_numbers_array)
    print('List -', formatted_array)
    print('Length -', length_of_the_array)

if __name__ == "__main__":
    main()
