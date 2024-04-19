# მოცემულია ტემპერატურების მონაცემები კვირის განმავლობაში. თითოეული დღისთვის ჩაინიშნეს დილის, შუადღის და საღამოს ტემპერატურები. ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28)) . თქვენი ამოცანაა, იპოვოთ თითოეული დღის საშუალო, მაქსიმალური და მინიმალური ტემპერატურა. ასევე გამოთვალეთ კვირის საშუალო ტემპერატურა. კვირის საშუალო გამოითვალეთ დღიური საშუალოების გამოყენებით. ყველა ნაპოვნი მონაცემი დაბეჭდეთ ეკრანზე. ბეჭდვისას გამოიყენეთ ისეთი ტექსტები, რომ გასაგები იყოს პროგრამის შედეგი.

# Constant tuple that contains the temperature data for the week
TEMPERATURES_DATA = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

def temperatures_daily_data(daily_temperatures: tuple[int, int, int]) -> tuple[float, int, int]:
    # This function calculates the average, maximum, and minimum temperatures for a given day's temperatures
    daily_average = sum(daily_temperatures) / len(daily_temperatures)
    daily_maximum = max(daily_temperatures)
    daily_minimum = min(daily_temperatures)
    return round(daily_average, 2), daily_maximum, daily_minimum

def main():
    # The main function calculates and prints the daily and weekly average temperatures, as well as the daily maximum and minimum temperatures.
    
    average_temperatures_sum = 0 # Store the sum of daily average temperatures for calculating the weekly average
        
    for day, daily_temperatures_data in enumerate(TEMPERATURES_DATA, start = 1):
        # Calculate average, maximum, and minimum temperatures of the day
        daily_average, daily_maximum, daily_minimum = temperatures_daily_data(daily_temperatures_data)
        # Update the average_temperatures_sum
        average_temperatures_sum += daily_average
        
        # Print the daily temperature data
        print(f"Day {day}")
        print(f"Average temperature of the day: {daily_average}°C")
        print(f"Highest temperature of the day: {daily_maximum}°C")
        print(f"Lowest temperature of the day: {daily_minimum}°C")
    
    # Calculate and print the weekly average temperature
    weekly_average = round(average_temperatures_sum / len(TEMPERATURES_DATA), 2)
    print(f"Average temperature of the week was {weekly_average}°C")     

if __name__ == "__main__":
    main()
