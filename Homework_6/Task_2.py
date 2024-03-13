# მომხმარებელმა უნდა შეიყვანოს პაროლი, რისთვისაც მხოლოდ სამი მცდელობა აქვს. სწორი პაროლია "Georgia". გადაჭერით For loop-ის გამოყენებით. 

# Correct password
DB_PASSWORD = "Georgia"
# User has three tries
MAX_TRIES = 3

for tries in range(MAX_TRIES, 0, -1):
    # Ask user to enter the password
    input_password = input("Please, enter password: ")
    
    # If the password is correct
    if input_password == DB_PASSWORD:
        print("Welcome to Georgia!")
        break
    
    # If the password is incorrect, but the user has other tries
    elif input_password != DB_PASSWORD and tries > 1:
        print("Wrong password, try again!")
        
    # If the user has entered incorrect password for three consecutive times
    else:
        print("You've exceeded the allowed number of attempts, so you've been blocked ⛔")
