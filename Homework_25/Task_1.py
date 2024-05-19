import json

class Employee:
    def __init__(self, name: str, position: str, salary: str):
        # Initialize an Employee object with name, position, and salary
        self.name = name
        self.position = position
        self.salary = int(salary)

class Department:
    def __init__(self, name: str, description: str, employees: list):
        # Initialize a Department object with name, description, and a list of employees
        self.name = name
        self.description = description
        self.employees = []
        # Create Employee objects from the employee data and add them to the department
        for employee_data in employees:
            employee = Employee(employee_data['name'], employee_data['position'], employee_data['salary'])
            self.employees.append(employee)
    
    def average(self):
        # Calculate and return the average salary of the employees in the department
        if len(self.employees) == 0:
            return 0
        return sum(employee.salary for employee in self.employees) / len(self.employees)
    
    def max(self):
        # Find and return the highest salary among the employees in the department
        if len(self.employees) == 0:
            return 0
        return max(employee.salary for employee in self.employees)
    
    def min(self):
        # Find and return the lowest salary among the employees in the department
        if len(self.employees) == 0:
            return 0
        return min(employee.salary for employee in self.employees)
    
    def positions(self):
        # Count the number of employees in each position and return a dictionary
        if len(self.employees) == 0:
            return "There are no employees in this department."
        number_of_employees = {}
        for employee in self.employees:
            number_of_employees[employee.position] = number_of_employees.get(employee.position, 0) + 1
        return number_of_employees

def main():
    try:
        # Open the JSON file and load the data
        with open ("Homework_25/Homework_1.json", "r") as file:
            data = json.load(file)
            
        departments = {}
        # Create Department objects from the JSON data
        for departments_data in data.values():
            department = Department(departments_data["name"], departments_data["description"], departments_data["employees"])
            departments[departments_data["name"]] = department
        
        # Print information about each department
        for department_name, department in departments.items():
            print("Department:", department_name)
            print("Description:", department.description)
            print("Average Salary:", department.average())
            print("Highest Salary:", department.max())
            print("Lowest Salary:", department.min())
            print("Positions:")
            try:
                for position, number in department.positions().items():
                    print(f"   {position}: {number}")
            except Exception:
                print("   There are no employees in this department.")
            print()            
            
    except FileNotFoundError:
        print("Error: file not found!")
    except PermissionError:
        print("Permission to access the file has been denied.")
    except json.JSONDecodeError as e:
        print("Error decoding JSON file:", e)
    except Exception as e:
        print("Sorry, something went wrong:", e)

if __name__ == "__main__":
    main()
