# დაწერეთ ფუნქცია, რომელსაც გადაეცემა სტრიქონი და დააბრუნებს ამ სტრიქონში არსებული ხმოვანი სიმბოლოების რაოდენობას. Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენ მიერ შექმნილი ფუნქციის გამართულად მუშაობის სადემონსტრაციოდ.

def count_vowels(string):
    # This function counts the number of vowels in a given string by iterating over each character in the uppercase version of the input string
    SYMBOLS = 'AEIOU'
    string = string.upper()
    number_of_vowels = 0
    
    for c in string:
        if c in SYMBOLS:
            number_of_vowels += 1
    
    return number_of_vowels

def main():
    test_string_one = 'CNN' # -> 0
    test_string_two = 'Sequoia' # -> 5
    test_string_three = 'Cherry BLOSSOM' # -> 3
    
    print(f"There are {count_vowels(test_string_one)} vowels in '{test_string_one}'")
    print(f"There are {count_vowels(test_string_two)} vowels in '{test_string_two}'")
    print(f"There are {count_vowels(test_string_three)} vowels in '{test_string_three}'")

if __name__ == "__main__":
    main()
