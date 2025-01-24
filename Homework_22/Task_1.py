# დაწერეთ პროგრამა, რომელიც წაიკითხავს data.txt ფაილს. data.txt ფაილში მოცემულია პროდუქციის შესყიდვის მონაცემები. მონაცემები ერთმანეთისგან გამოყოფილია მძიმით. მონაცემების მიმდევრობა შემდეგია: user_name,product_name,amount,price - სადაც price არის ერთეული პროდუქციის ღირებულება. პროგრამამ უნდა გააკეთოს ორი ახალი ფაილი small.txt და high.txt. პროგრამა small.txt ფაილში უნდა გადაწეროს ის შესყიდვები, რომელთა ღირებულება ნაკლებია 10-ზე, ხოლო ყველა სხვა დანარჩენი - high.txt ფაილში.        

def process_data(data_line: str) -> tuple[str, str, int, float, float]:
    # This function unpacks the user data into four different variables (user_name, product_name, quantity and unit_price) and calculates the total cost
    
    user_details = data_line.strip().split(",")
    user_name, product_name, quantity, unit_price = user_details
    quantity = int(quantity)
    total_cost = quantity * float(unit_price)
    
    return user_name, product_name, quantity, unit_price, total_cost

def main():
    # Open the data file for reading
    with open("Homework_22/data.txt", "r") as file:
        data_lines = file.readlines()
        
    # Open small.txt and high.txt files for writing
    with open("Homework_22/small.txt", "w") as small_file, open("Homework_22/high.txt", "w") as high_file: 
    
        # Iterate over each line (each user details) in the data file
        for line in data_lines:
            user_name, product_name, amount, price, total_cost = process_data(line)
            # Construct the output sring using the user details
            output_string = f"{user_name},{product_name},{amount},{price}\n"
            
            # Determine which file to write the purchase date to
            if total_cost < 10:
                small_file.write(output_string)
            else:
                high_file.write(output_string)

if __name__ == "__main__":
    main()
