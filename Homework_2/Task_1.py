# დაწერეთ პროგრამა რომელიც მიიღებს true ან false. თუ პროგრამამ მიიღო true, ეკრანზე დაბეჭდეთ “whoala”.

# Let the user enter True or False
is_true = input("Enter True or False: ")

if is_true == "True" or is_true == "true":
    print("Whoala!")
elif is_true == "False" or is_true == "false":
    print("You entered 'False'!")
else:
    print("You didn't enter 'True' or 'False'!")
