# დაწერეთ ფუნქცია, რომელსაც შეეძლება ცელსიუსის ფარენჰეიტებში გადაყვანა და პირიქით. C = (F - 32) * 5/9 , F = C * 9/5 + 32. Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენ მიერ შექმნილი ფუნქციის გამართულად მუშაობის სადემონსტრაციოდ.

def convert_temperature(temp: float, unit: str):
    # This function converts between Celsius and Fahrenheit. It takes two parameters: temp (float) that is the temperature value to be converted, and unit (str) that is the unit of the temperature, either 'C' for Celsius or 'F' for Fahrenheit
    
    # Convert Celsius to Fahrenheit
    if unit.upper() == 'C':
        converted_temperature = (temp * 9/5) + 32
        converted_unit = 'F'
    
    # Convert Fahrenheit to Celsius
    elif unit.upper() == 'F':
        converted_temperature = (temp - 32) * 5/9
        converted_unit = 'C'
    
    # Return converted temperature and unit    
    return str(converted_temperature) + ' ' + converted_unit

def main():
    # Prompt user to enter the temperature unit
    temperature_unit = input("Enter the temperature unit ('C' for Celsius, 'F' for Fahrenheit): ")
    
    # Test data to convert Celsius to Fahrenheit
    celsius_temp = 25.0  # -> 77.0 F
    # Test data to convert Fahrenheit to Celsius
    fahrenheit_temp = 212.0 # -> 100.0 C
    
    if temperature_unit.upper() == 'C':
        print(celsius_temp, 'Celsius is equal to', convert_temperature(celsius_temp, temperature_unit))
    if temperature_unit.upper() == 'F':
        print(fahrenheit_temp, 'Fahrenheit is equal to', convert_temperature(fahrenheit_temp, temperature_unit))       

if __name__ == "__main__":
    main()
