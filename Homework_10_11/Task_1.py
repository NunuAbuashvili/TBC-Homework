# დაწერეთ პროგრამა, რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1. პროგრამამ უნდა დაითვალოს რიცხვი x და დაბეჭდოს ეკრანზე. რიცხვი x ის დათვლის პრინციპი ასეთია: x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) ) გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 10000, 100000. რას ამჩნევთ?

# Ask user to enter a natural number greater than 1
n = int(input("Enter a natural number greater than 1: "))

# Ensure that the input value is greater than 1
while n <= 1:
    n = int(input("Invalid input! The number should be greater than 1: "))

# Initialize x to 0 to store the value of the series
x = 0
# Initialize sign to 1 to alternate between adding and subtracting terms in the series
sign = 1

# Iterate over odd numbers from 1 to (2n - 1)
for i in range(1, 2 * n, 2):
    # Calculate the term and add it to x
    x += sign * (1 / i)
    # Negate the sign for the next iteration
    sign *= -1

# Calculate the final value of x and print the result
calculated_x = 4 * x
print("The value of x for n =", n, "is", calculated_x)

# თუ პროგრამას გადავცემთ შემდეგ რიცხვებს: 10, 100, 1000, 10000, 100000... x-ის მნიშვნელობა მოქცეული იქნება 3-სა და ≈ 3.14159...(π)-ს შორის (The Gregory-Leibniz Series). n-ის მნიშვნელობა რაც უფრო მეტია, მით უფრო ზუსტია x და, შესაბამისად, მით უფრო ახლოს არის π-სთან.
