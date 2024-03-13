"""
დაწერეთ პროგრამა, რომელიც დაბეჭდავს გამრავლების ტაბულას ერთიდან ცხრის ჩათვლით. 
ტაბულა უნდა იყოს სვეტებად შედგენილი. ყოველ მომდევნო სვეტში არ უნდა იყოს გამეორებული ნამრავლი წინა სვეტიდან. 

Output:
1 * 1 = 1  
1 * 2 = 2  2 * 2 = 4  
1 * 3 = 3  2 * 3 = 6  3 * 3 = 9  
1 * 4 = 4  2 * 4 = 8  3 * 4 = 12  4 * 4 = 16  
...

"""
# Create a variable for multiplicand outside the while loop and initialize it to 1
multiplicand = 1

# Outer while loop for multiplicand will run from 1 to 9
while multiplicand < 10:
    # Create a variable for multiplier inside the while loop and initialize it to 1
    multiplier = 1
    # Inner loop for multiplier will run from 1 to 9
    while multiplier <= multiplicand:
        _sum = multiplier * multiplicand
        if _sum < 10:
            print(f"{multiplier} * {multiplicand} = {_sum}", end="   ")
        else:
            print(f"{multiplier} * {multiplicand} = {_sum}", end="  ")
        multiplier += 1 # Update the multiplier
        
    multiplicand += 1 # Update the multiplicand
    print() # New line
