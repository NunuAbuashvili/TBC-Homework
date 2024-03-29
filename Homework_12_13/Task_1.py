# დაწერეთ პროგრამა, რომელსაც გადაეცემა სტრიქონი და ამ სტრიქონიდან დააგენერირებს გადანაცვლებულ სტრიქონს და დაბეჭდავს ეკრანზე. გადანაცვლებული სტრიქონის მიღების წესი შემდეგია: სიმბოლო უნდა გადანაცვლდეს თავში. გადანაცვლება უნდა დაგენერირდეს ყოველი სიმბოლოსთვის.

# Define a function to format a given string
def format_string(string):
    # Format the string by shifting its last character to the beginning
    formatted_string = string[-1] + string[:-1]
    
    return formatted_string

# Define the main function    
def main():
    user_input = input("Enter a word or a phrase: ")
    for _ in range(len(user_input)):
        user_input = format_string(user_input)
        print(user_input)
        
if __name__ == "__main__":
    main()
    