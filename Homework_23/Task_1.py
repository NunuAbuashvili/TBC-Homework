# დაწერეთ პროგრამა, რომელიც წაიკითხავს JSON ფაილს. პროგრამამ უნდა დაამუშავოს შეცდომა, თუ ფაილი არ არსებობს და დაბეჭდოს ეკრანზე ინფორმაციული შეტყობინება. პროგრამამ ფაილში არსებული დეპარტამენტებისთვის უნდა დათვალოს თითოეული დეპარტამენტის საშუალო ხელფასი. უნდა დაამუშავოს პოტენციური შეცდომები. დათვლილი საშუალო ხელფასები უნდა დაბეჭდოს ეკრანზე და ჩაწეროს JSON ფაილში avg_salary.json ({"department_name": "average_salary"}).

# Errors that might occur:
# 1. FileNotFoundError: If the program tries to read a file that doesn't exist in the specified location.
# 2. PermissionError: If the program tries to access a file for which it doesn't have the necessary permissions.
# 3. JSONDecodeError: If the JSON file is not properly formatted or contains invalid data.
# 4. KeyError: If the program tries to access a key that doesn't exist in the JSON data ("name", "employees", "salary").
# 5. ValueError: If the program tries to convert a string (e.g., the value of "salary") to a numeric value and the string doesn't represent a valid number.
# 6. ZeroDivisionError: If the program tries to divide a number by zero (e.g., there is no data about the employees of a department).

import json
from json import JSONDecodeError

def calculate_average_salaries(data: dict) -> dict:
    # This function calculates the average salary for each department in the provided data
    department_average_salaries = {}
    
    for department_data in data.values():
        try:
            department_salaries = [] # When iterating through each department, store the salaries of its employees
            invalid_salary_data = False # Variable to handle those cases, when the salary of at least one employee can't be converted to a numeric value
            
            # Iterate over employees in the department
            for employee in department_data["employees"]:
                # If number == 'None', consider it as 0, otherwise, convert the salary into an integer and append it to department_salaries
                if employee["salary"] == "None":
                    department_salaries.append(0)
                else:
                    try:
                        department_salaries.append(int(employee["salary"]))
                    except ValueError:
                        print(f"Failed to convert the salary '{employee["salary"]}' of {employee["name"]} in {department_data["name"]} to a numeric value.")
                        invalid_salary_data = True
                        
            # If any invalid salary data has been found
            if invalid_salary_data:
                department_average_salaries[department_data["name"]] = "Could not calculate the average salary due to invalid salary data"
            else:
                try:
                    # Calculate the average salary for each department and add it as a string value to the dictionary
                    average_salary = sum(department_salaries) / len(department_salaries)
                    department_average_salaries[department_data["name"]] = str(average_salary)
                except ZeroDivisionError:
                    department_average_salaries[department_data["name"]] = "There are no employees in this department"
                    
        except KeyError as e:
            print(f"Error processing department '{department_data['name']}'. There is no key with name '{e}'.")
            
    return department_average_salaries

def main():
    # The main function reads the input JSON file, calculates the average salaries, and writes the result to an output JSON file
    try:
        with open("Homework_23/Salaries.json", "r") as file:
            data = json.load(file)
            
            department_average_salaries = calculate_average_salaries(data)
            print(department_average_salaries)
            
        with open("Homework_23/avg_salary.json", "w") as output_file:
            json.dump(department_average_salaries, output_file, indent = 4)
                
    except FileNotFoundError:
        print("Error: file not found!")
    except PermissionError:
        print("Permission to access the file has been denied.")
    except JSONDecodeError as e:
        print("Error decoding JSON file:", e)
    except Exception as e:
        print("Sorry, something went wrong:", e)

if __name__ == "__main__":
    main()
