# (5 ქულა) დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: სახელი, გვარი და ასაკი. Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში: Hello სახელი გვარი. Age: ასაკი.

def greet_user(name: str, surname: str, age: int):
    # This function takes three arguments: name, surname and age from the user, and greets the user
    return f"Hello {name} {surname}. \nAge: {age}"

def main():
    # User input
    user_name = input("Please, enter your name: ")
    user_surname = input("Please, enter your surname: ")
    user_age = int(input("Please, enter your age: "))
    
    # Print the greeting
    print(greet_user(user_name, user_surname, user_age))

if __name__ == "__main__":
    main()
