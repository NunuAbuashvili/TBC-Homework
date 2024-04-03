# დაწერეთ პროგრამა, რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b, სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უდიდეს საერთო გამყოფს. გადაჭერით ეს პრობლემა როგორც იტერაციული, ისე რეკურსიული მეთოდით.

# This function calculates the greatest common divisor (GCD) of two integers using iteration
def iter_gcd(num1: int, num2: int):
    gcd = 1
    
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    
    return gcd

# This function calculates the greatest common divisor (GCD) of two integers using recursion
def rec_gcd(num1: int, num2: int):
    lowest_number = min(num1, num2)
    highest_number = max(num1, num2)
    
    # Base case: GCD of a nonzero number and 0 is the nonzero number itself
    if lowest_number == 0:
        return highest_number
    
    # The Euclidean algorithm (gcd(a, b) = gcd(b, a % b))
    return rec_gcd(lowest_number, highest_number % lowest_number)

def main():
    a = int(input("Enter the first number, that is between 0 and 10000: "))
    b = int(input("Enter the second number, that is between 0 and 10000: "))
    
    print(f"GCD of {a} and {b} is {iter_gcd(a, b)}")
    print(f"GCD of {a} and {b} is {rec_gcd(a, b)}")

if __name__ == "__main__":
    main()
