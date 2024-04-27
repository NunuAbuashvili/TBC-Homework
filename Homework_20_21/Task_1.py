# დაწერეთ პროგრამა, რომელსაც გადაეცემა რიცხვი n. პროგრამამ n რიცხვისთვის უნდა დააგენერიროს მიმდევრობა. მიმდევრობის პირველი ელემენტია n. ყოველი მომდევნო ელემენტი განისაზღვრება შემდეგი წესით: თუ წინა წევრი ლუწია - წინა წევრი გავყოთ 2-ზე, თუ წინა წევრი კენტია - წინა წევრი გავამრავლოთ 3-ზე და დავუმატოთ 1. მიმდევრობის გენერირება უნდა შეწყდეს, როცა მიიღწევა რიცხვი 1. მიმდევრობის გენერაციისთვის გააკეთეთ 2 ფუნქცია, ერთი ჩვეულებრივი, მეორე ქეშირებით. ქეშირება გააკეთეთ ცოტა განსხვავებულად, ვიდრე ლექციაშია განხილული. ლექციაში განხილულ ქეშირებაში გვქონდა ერთი გასაღებისთვის ერთი მნიშვნელობა, აქ ერთი გასაღებისთვის შეინახეთ ბევრი მნიშვნელობა. მაგალითად, რომ დაქეშავთ n=3, მნიშვნელობა უნდა იყოს 10, 5, 16, 8, 4, 2, 1.

cache = {}

def generate_sequence(number: int) -> list:  
    # This function generates a sequence of numbers starting from <number> to 1 using recursion and returns a list with the sequence
    
    if number == 1:
        return [1]
    
    # Initialize <sequence>, with <number> as the first item
    sequence = [number]
    
    if number % 2 == 0:
        next_item = number // 2
    else:
        next_item = number * 3 + 1
    
    # Append the subsequent terms to the sequence recursively
    sequence.extend(generate_sequence(next_item))
    
    return sequence

def generate_sequence_cached(number: int, cache):
    # This function generates the same sequence as the function above, but the difference is, this function allows us to cache the values
    
    if number == 1:
        return [1]
    
    # Check if the sequence for the <number> is already in cache
    if number in cache:
        return cache[number]
    
    sequence = [number]
    
    if number % 2 == 0:
        next_item = number // 2
    else:
        next_item = number * 3 + 1
    
    sequence.extend(generate_sequence_cached(next_item, cache))
    
    # Cache the sequence for the current item
    cache[number] = sequence
    return sequence

def main():
        
    # Verify if both functions are operating properly
    for _ in range(3):
        n = int(input("Please, enter a positive whole number: "))
        while n <= 0:
            n = int(input("Invalid input! Please, enter a number greater than 0: "))
        
        print("Generated sequence using recursion")
        print(generate_sequence(n))
        print("Generated sequence using function caching")
        print(generate_sequence_cached(n, cache))

if __name__ == "__main__":
    main()
