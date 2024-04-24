# დაწერეთ პროგრამა, რომელიც მიიღებს ინფორმაციას, ვის ვინ დაუმეგობრდა. თუ პროგრამამ მიიღო სიტყვა FINISH, უნდა დაასრულოს მუშაობა. თუ პროგრამამ მიიღო სიტყვა Giorgi – Nini, ნიშნავს რომ Nini დაუმეგობრდა Giorgi-ს და Giorgi დაუმეგობრდა Ninis. პროგრამამ მუშაობის დასრულების წინ, ეკრანზე უნდა დაბეჭდოს ვინ ვისი მეგობარია. Მაგალითად: 
# Input: 
# Giorgi – Nini 
# Nini – Nika 
# Giorgi – Nika 
# FINISH 
# Output: 
# Giorgi – Nini, Nika 
# Nini – Giorgi, Nika 
# Nika – Nini, Giorgi

# Constant to terminate the program
FINISH_KEYWORD = 'FINISH' 

def friendships_dictionary(user: str, friend: str, dictionary: dict) -> dict:
    # This function takes two user strings ('user' and 'friend') and a dictionary as arguments. It adds a friendship relationship between two people to the dictionary, and returns the updated dictionary
    
    # 1. For user's name
    if user not in dictionary:
        dictionary[user] = [friend]
    # Handle duplicate friendships
    if user in dictionary and friend not in dictionary[user]: 
        dictionary[user].append(friend)
    
    # 2. For friend's name  
    if friend not in dictionary:
        dictionary[friend] = [user]
    # Handle duplicate friendships
    if friend in dictionary and user not in dictionary[friend]:
        dictionary[friend].append(user)
    
    return dictionary
    
def main():
    friendships = {}
    
    while True:
        user_input = input("Please, enter your name and who you are friends with (Name - Friend's name) or 'FINISH' to end: ")
        
        # Exit the loop if the user enters the FINISH_KEYWORD
        if user_input.upper() == FINISH_KEYWORD:
            break
        
        # Split the input string into two parts: user's name and friend's name
        user_name, friend_name = user_input.split('-')
        
        # Remove extra spaces and capitalize the first letter of the name
        user_name = user_name.strip().title()
        friend_name = friend_name.strip().title()
        
        # Update the dictionary by calling the friendships_dictionary function
        friendships_dictionary(user_name, friend_name, friendships)
    
    # Print the result (Person's name - names of the person's friends)
    for name, friends in friendships.items():
        friends_names = ', '.join(friends)
        print(f"{name} - {friends_names}")
            
if __name__ == "__main__":
    main()
