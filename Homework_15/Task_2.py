# დაწერეთ ფუნცია, რომელიც დაადგენს რიცხვი არის თუ არა მარტივი. Რიცხვი მარტივია, თუ მისი გამყოფებია 1 და თავისი თავი. Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენ მიერ შექმნილი ფუნქციის გამართულად მუშაობის სადემონსტრაციოდ.

def is_prime(number: int):
    # This function checks if a given integer is prime or not
    
    # Negative numbers, 0 and 1 are not prime numbers
    if number < 2:
        return 'IS NOT A PRIME NUMBER'
    
    # 2 is the only even prime number
    if number == 2:
        return 'IS A PRIME NUMBER'
    
    # Iterate from 3 to 'n // 2', step = 2
    upper_range = number // 2
    for i in range(3, upper_range, 2):
        if number % i == 0:
            return 'IS NOT A PRIME NUMBER'
        
    return 'IS A PRIME NUMBER'  

def main():
    # Test data
    test_number_one = 24
    test_number_two = 17
    test_number_three = -5
    test_number_four = 1
    test_number_five = 2
    
    # Print results
    print(test_number_one, is_prime(test_number_one)) # NO
    print(test_number_two, is_prime(test_number_two)) # YES
    print(test_number_three, is_prime(test_number_three)) # NO
    print(test_number_four, is_prime(test_number_four)) # NO
    print(test_number_five, is_prime(test_number_five)) # YES

if __name__ == "__main__":
    main()
