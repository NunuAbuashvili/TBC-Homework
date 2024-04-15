# დაწერეთ პროგრამა, რომელიც დააგენერირებს 100 შემთხვევით რიცხვს 10-დან 1000000000-მდე. პროგრამამ უნდა იპოვოს ყველაზე მოკლე რიცხვი მიმდევრობაში, ყველაზე გრძელი რიცხვი. პროგრამამ უნდა დაალაგოს რიცხვები სიგრძის მიხედვით ზრდადობით, კლებადობით. ყველა შედეგი დაბეჭდეთ ეკრანზე. გამოიყენეთ min, max, sorted ფუნქციები.
import random 

def generate_random_numbers(length: int, below_range: int, upper_range: int) -> list:
    random_numbers = []
    
    for i in range(length):
        random_number = random.randint(below_range, upper_range)
        random_numbers.append(random_number)
    
    return random_numbers

def main():
    random_numbers_list = generate_random_numbers(100, 10, 1000000000)
    
    # Calculate the length of the list item
    item_length = lambda item: len(str(item))
    
    # Find the shortest number and the longest numbers
    shortest_number = min(random_numbers_list, key = item_length)
    longest_number = max(random_numbers_list, key = item_length)
    
    # Sort numbers by length in ascending order and in descending order
    sorted_ascending = sorted(random_numbers_list, key = item_length)
    sorted_descending = sorted(random_numbers_list, key = item_length, reverse = True)
    
    # Print the results
    print("Random numbers list:", random_numbers_list)
    print("Shortest number from the list:", shortest_number)
    print("Longest number from the list:", longest_number)
    print("Sorted by length (Ascending):", sorted_ascending)
    print("Sorted by length (Descending):", sorted_descending)
    
if __name__ == "__main__":
    main()
