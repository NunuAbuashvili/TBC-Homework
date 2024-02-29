# დაწერეთ პროგრამა, რომელიც არგუმენტად მიიღებს მანქანის სიჩქარეს, განსაზღვრავს მისი სიჩქარის კატეგორიას და დაბეჭდავს ეკრანზე. Სიჩქარის კატეგორიები განისაზღვრება შემდეგნაირად: თუ ავტომობილის სიჩქარე 30 კმ/სთ-ზე ნაკლებია, მისი კატეგორიაა - SLOW. როცა ავტომობილის სიჩქარე 120 კმ/სთ-ზე მეტია, მისი კატეგორიაა - VERY FAST. თუ ავტომობილის სიჩქარე მეტია 60 კმ/სთ-ზე, მისი კატეგორიაა - FAST. ხოლო თუ ავტომობილის სიჩქარე მეტია 30 კმ/სთ-ზე, მისი კატეგორიაა - MODERATE. (თუ ავტომობლი ხვდება ორ კატეგორაიში, უნდა შეირჩეს უფრო სწრაფი კატეგორია)

# Ask the user to enter the car speed
car_speed = float(input("Enter the car speed in km/h: "))

# Print the category for the speed
print("The speed that you have entered is", end=" ")
# 1. Under 30 km/h
if car_speed < 30 and car_speed > 0:
    print("SLOW")
# 2. Between 30 and 60 km/h
elif car_speed >= 30 and car_speed < 60:
    print("MODERATE")
# 3. Between 60 and 120 km/h
elif car_speed >= 60 and car_speed < 120:
    print("FAST")
# 4. Higher than 120 km/h
elif car_speed >= 120:
    print("VERY FAST")
# 5. If the user enters an invalid number
else:
    print("of unknown category")