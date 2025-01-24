# დაწერეთ პროგრამა, რომელიც მოცემული ტემპერატურების [22, 25, 19, 23, 25, 26, 23] მიხედვით გამოითვლის საშუალო ტემპერატურას და დაბეჭდავს ეკრანზე.

def calculate_average_temperature(temperatures: list) -> float:
    # This function takes a list of temperatures as a parameter and returns the average temperature as a float number
    
    temperature_sum = 0
    length = len(temperatures)
    
    # Loop through each temperature in the list, adding it to temperature_sum
    for temp in temperatures:
        temperature_sum += temp
    
    # Calculate the average temperature and round it to 2 decimal places
    average_temperature = temperature_sum / length
    return round(average_temperature, 2)

def main():
    temperature_array = [22, 25, 19, 23, 25, 26, 23]
    result = calculate_average_temperature(temperature_array)
    print(f"Average temperature is {result}°C")

if __name__ == "__main__":
    main()
