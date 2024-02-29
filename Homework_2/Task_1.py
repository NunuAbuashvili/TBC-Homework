# დაწერეთ პროგრამა რომელიც მიიღებს true ან false. თუ პროგრამამ მიიღო true, ეკრანზე დაბეჭდეთ “whoala”.

# Let the user enter True or False
isTrue = input("Enter True or False: ")

if isTrue == "True" or isTrue == "true":
    print("Whoala!")
elif isTrue == "False" or isTrue == "false":
    print("You entered 'False'!")
else:
    print("You didn't enter 'True' or 'False'!")