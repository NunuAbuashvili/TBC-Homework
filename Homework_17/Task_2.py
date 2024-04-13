# შექმენით სამი სია და შეავსეთ შემთხვევითი რიცხვებით. ეკრანზე დაბეჭდეთ ერთსა და იმავე ინდექსზე მდგარი რიცხვების ჯამები.

# Import function to generate random numbers
from Task_1 import generate_random_numbers

def main():
    # Generate three lists with random numbers in range of (0, 100)
    list_1 = generate_random_numbers(10, 0, 100)
    list_2 = generate_random_numbers(10, 0, 100)
    list_3 = generate_random_numbers(10, 0, 100)
    
    # Print the original lists
    print("List 1:", list_1)
    print("List 2:", list_2)
    print("List 3:", list_3)
    
    # Print the sums of numbers at the same index
    sums_at_indices = list(map(lambda a, b, c: a + b + c, list_1, list_2, list_3))
    for i in range(len(sums_at_indices)):
        print(f"Sum at index {i}: {sums_at_indices[i]}")

if __name__ == "__main__":
    main()
