# შექმენით სია და შეავსეთ სიტყვებით. პროგრამამ უნდა გაფილტროს სია, გადაყაროს ყველა ელემენტი, რომელიც შეიცავს 3-ზე მეტ სიმბოლოს და ეკრანზე უნდა დაბეჭდოს დარჩენილი სიტყვები მაღალ რეგისტრში.

def main():
    # Create a list of words
    my_list = ["map", "function", "returns", "a", "map", "object", "of", "the", "results", "after", "applying", "the", "given", "function", "to", "each", "item", "of", "a", "given", "iterable"]

    # Filter the list to keep only words with three or fewer characters
    filtered_words = list(filter(lambda word: len(word) <= 3, my_list))
        
    # Convert the filtered words to uppercase
    uppercase_filtered_words = list(map(lambda word: word.upper(), filtered_words))
    
    # Print the original and modified list
    print("Original list:", my_list)
    print("Modified list:", uppercase_filtered_words)

if __name__ == "__main__":
    main()
