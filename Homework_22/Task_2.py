"""
დაწერეთ პროგრამა, რომელიც წინა ამოცანაში აღწერილი სტრუქტურის ფაილიდან წაიკითხავს გაყიდვების ინფორმაციას.

a. პროგრამამ უნდა იპოვოს მაქსიმალური შესყიდვის (პროდუქტების რაოდენობით, ერთ შესყიდვაში) განხორციელებელი მომხმარებელი, თუ რამდენიმეა, მაშინ - მომხმარებლების სია.

b. პროგრამამ უნდა იპოვოს მაქსიმალური შესყიდვის (ყველა შესყიდვის ჯამური ღირებულებით) განხორციელებელი მომხმარებელი, თუ რამდენიმეა, მაშინ - მომხმარებლების სია.

c. პროგრამამ უნდა იპოვოს შესყიდვების ღირებულების საშუალო არითმეტიკული.

d. პროგრამამ უნდა იპოვოს შესყიდვების რაოდენობების საშუალო არითმეტიკული.

e. პროგრამამ უნდა იპოვოს ყველაზე დიდი რაოდენობით გაყიდული პროდუქტი. თუ რამდენიმეა, მაშინ - პროდუქტების სია.

ნაპოვნი მონაცემები შეაგროვეთ dict ტიპის ობიექტში და ჩაწერეთ stats.json ფაილში. დააფორმატეთ stats.json ფაილი ისე, რომ მონაცემები ჩაიწეროს ადვილად წაკითხვადი ფორმით.

"""
import json
from Task_1 import process_data

def calculate_average(data_lines: str) -> tuple[float, float]:
    # This function calculates the average cost and the average amount of products purchased
    products_prices = []
    purchase_amounts = []
    
    for line in data_lines:
        _, _, amount, _, total_cost = process_data(line)
        purchase_amounts.append(amount)
        products_prices.append(total_cost)
    
    purchase_amount_average = round(sum(purchase_amounts) / len(purchase_amounts), 2) 
    products_price_average =  round(sum(products_prices) / len(products_prices), 2)
    
    return purchase_amount_average, products_price_average

def find_single_largest_purchase(data_lines: str) -> list:
    # This function finds the user(s), who made the largest single purchase
    single_largest_purchase = 0
    single_largest_purchase_users = []
    
    for line in data_lines:
        user_name, _, amount, _, _ = process_data(line)
        
        if amount > single_largest_purchase:
            single_largest_purchase = amount
            single_largest_purchase_users = [user_name]
        elif amount == single_largest_purchase:
            single_largest_purchase_users.append(user_name)
    
    return single_largest_purchase_users

def find_total_largest_purchase(data_lines: str) -> list:
    # This function fins the user who made the largest purchase in total
    largest_purchase = 0
    largest_purchase_users = []
    total_purchases = {}
    
    for line in data_lines:
        user_name, _, _, _, total_cost = process_data(line)
        total_purchases[user_name] = total_purchases.get(user_name, 0) + total_cost

    for user_name, total_cost in total_purchases.items():
        if total_cost > largest_purchase:
            largest_purchase = total_cost
            largest_purchase_users = [user_name]
        elif total_cost == largest_purchase:
            largest_purchase_users.append(user_name)
        
    return largest_purchase_users

def most_purchased_product(data_lines: str) -> list:
    # This function finds the product with the largest number of sales
    most_purchased_products = []
    products_quantity = {}
    
    for line in data_lines:
        _, product_name, amount, _, _ = process_data(line)
        products_quantity[product_name] = products_quantity.get(product_name, 0) + amount
    
    for product, amount in products_quantity.items():
        if amount == max(products_quantity.values()):
            most_purchased_products.append(product)
    
    return most_purchased_products

def main():
    with open("Homework_22/data.txt", "r") as file:
        data = file.readlines()
        
        amount_average, price_average = calculate_average(data)
        single_largest_purchase_users = find_single_largest_purchase(data)
        largest_purchase_users = find_total_largest_purchase(data)
        most_purchased_products = most_purchased_product(data)
        
        stats_dictionary = {
            "Users, who made the biggest single purchase": single_largest_purchase_users,
            "Users, who made the largest purchase in total": largest_purchase_users, 
            "Average cost of products purchased": price_average, 
            "Average amount of products purchased": amount_average, 
            "Product with the largest number of sales": most_purchased_products
        }
    
    with open("Homework_22/stats.json", "w") as stats_file:
        json.dump(stats_dictionary, stats_file, indent = 4)        
        
if __name__ == "__main__":
    main()
