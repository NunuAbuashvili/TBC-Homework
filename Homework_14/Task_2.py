# დაწერეთ პროგრამა, რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b, სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უმცირეს საერთო ჯერადს. მინიშნება: lcm(a, b) = (a * b) / gcd(a, b). დააიმპორტეთ და გამოიყენეთ უდიდესი საერთო გამყოფის დათვლის ფუნქციონალი პირველი დავალების ფაილიდან.

# Import function to calculate GCD of two integers
from Task_1 import rec_gcd

# This function calculates the least common multiple (LCM) of two integers
def lcm(num1: int, num2: int):
    return (num1 * num2) // rec_gcd(num1, num2)

def main():
    a = int(input("Enter the first number, that is between 0 and 10000: "))
    b = int(input("Enter the second number, that is between 0 and 10000: "))
    
    print(f"LCM of {a} and {b} is {lcm(a, b)}")

if __name__ == "__main__":
    main()
