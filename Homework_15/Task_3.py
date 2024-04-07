# დაწერეთ რეკურსიული ფუნქცია, რომელსაც გადაეცემა სტრიქონი და დააბრუნებს მის შებრუნებულს. Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენ მიერ შექმნილი ფუნქციის გამართულად მუშაობის სადემონსტრაციოდ.

def reverse_string(string):
    # This function recursively reverses the given string
    if len(string) == 1:
        return string
    return string[-1] + reverse_string(string[:-1])

def main():
    # Test data
    test_string_one = "Pizza"
    test_string_two = "Strawberry"
    test_string_three = "Chocolate"
    
    print(f"'{test_string_one}' reversed is '{reverse_string(test_string_one)}'")
    print(f"'{test_string_two}' reversed is '{reverse_string(test_string_two)}'")
    print(f"'{test_string_three}' reversed is '{reverse_string(test_string_three)}'")

if __name__ == "__main__":
    main()
