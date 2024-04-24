# დაწერეთ პროგრამა, რომელიც მიიღებს სტრიქონს. პროგრამამ უნდა დაითვალოს ამ სტრიქონში არსებული სიმბოლოები რომელი რამდენჯერ გვხვდება და დაბეჭდოს ეკრანზე. მაგალითად:
# Input: Python 
# P – 1 
# y – 1 
# t – 1 
# h – 1 
# o – 1 
# n – 1

def count_characters(string: str) -> dict:
    # This function takes a string as an argument and returns a dictionary, where the <key> is each symbol from the string, and its <value> is the number of occurances of that symbol
    characters_count = {}
    
    for c in string:
        if c not in characters_count:
            characters_count[c] = 1
        else:
            characters_count[c] += 1  
    
    return characters_count 

def main():
    input_string = input("Please, enter any word or phrase: ")
    characters_count = count_characters(input_string)
    
    print(f"Character counts in the string '{input_string}':")
    for symbol, number in characters_count.items():
        print(symbol, '-', number)    
        
if __name__ == "__main__":
    main()
