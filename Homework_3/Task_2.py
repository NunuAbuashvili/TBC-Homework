# დაწერეთ პროგრამა რომელიც მიიღებს 3 მნიშვნელობას: რომელ წელსაა დაბადებული ადამიანი, მერამდენე თვეშია დაბადებული და რა რიცხვშია დაბადებული. Შემდეგ კი ეკრანზე გამოიტანს კვირის რომელ დღესაა დაბადებული ადამიანი.
import datetime

# Introduction
print("Enter your date of birth (YY/MM/DD) and I will tell you what day of the week you were born on!")

# Ask the user for the birth year, month and day
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Format the date
birth_date = datetime.date(birth_year, birth_month, birth_day)

# Create a list of weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get the day of the week the person was born on
birth_weekday = weekdays[birth_date.weekday()]

# Print the result
print("You were born on", birth_weekday + ".")