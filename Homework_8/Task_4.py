# დაწერეთ პროგრამა, რომელიც მომხმარებლის შემოყვანილ ტექსტს დაშიფრავს ან განშიფრავს და დაბეჭდავს ეკრანზე. დაშიფვრის ლოგიკა ასეთია, ყოველი სიმბოლო უნდა შეიცვალოს კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი. თუ სიმბოლოს მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, მაშინ უნდა გადავიდეს პირველ სიმბოლოში ამ სტრიქონიდან. Მაგალითად: p -> q, l -> a და ა.შ. პროგრამამ უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური სიმბოლოები.

# Define keyboard lines
LINE_1 = 'qwertyuiop'
LINE_2 = 'asdfghjkl'
LINE_3 = 'zxcvbnm'

# Prompt user to choose between encryption ('e') and decryption ('d')
action = input("Should I encrypt or decrypt your text? (e/d): ")
# Validate the user input
while action != 'e' and action != 'd':
    action = input("Invalid input! Please, enter 'e' for encryption and 'd' for decryption: ")

# Ask user to enter the text to be encrypted or decrypted, and convert it to lowercase
user_input = input("Please, enter the text here: ")
user_input = user_input.lower()

# Initialize en empty string to store the output word
output_text = ''

for c in user_input:
    # Determine which line the character belongs to and store it in a new variable
    line = '' 
    if c in LINE_1:
        line = LINE_1   
    elif c in LINE_2:
        line = LINE_2
    elif c in LINE_3:
        line = LINE_3
    
    # Find the index of the character in its respective line
    c_index = -1
    for i in range(len(line)):
        if line[i] == c:
            c_index = i
    
    # If the character does not belong to any line, directly append it to the output text
    if c_index == -1:
        output_text += c
        continue
    
    # Encrypt or decrypt the character and append it to the output text     
    if action == 'e':
        output_index = (c_index + 1) % len(line)
    elif action == 'd':
        output_index = (c_index - 1) % len(line)
                
    output_text = output_text + line[output_index]

print(output_text)    
