# 1. დაწერეთ პროგრამა, რომელიც json ფაილიდან წაიკითხავს რეცეპტებს. რეცეპტი შეიცავს ინგრედიენტების სიას. პროგრამამ ასევე უნდა წაიკითხოს მეორე json ფაილი, რომელშიც მოცემულია მაღაზიებში ხელმისაწვდომი პროდუქტების სია. პროგრამამ მომხმარებელს უნდა ჰკითხოს, რომელი კერძის მომზადებას აპირებს და ეკრანზე დაუბეჭდოს მაღაზიები, რომელში წასვლაც მოუწევს მომხმარებელს ამ კერძის პროდუქტების შესაგროვებლად. პროგრამამ უნდა შეეცადოს, რომ რაც შეიძლება ნაკლებ მაღაზიაში გაუშვას მომხმარებელი დროისა და ფულის დასაზოგად. თუ ვერ ხერხდება არჩეული კერძისთვის საჭირო ინგრედიენტების მოძიება, დაუწეროს რომ ამ კერძს ამ ქალაქში ვერ მოამზადებს.
import json

def read_json_file(filename: str) -> dict:
    # Function to read a JSON file and load its contents into a dictionary
    try:
        with open(filename, "r") as file:
            return json.load(file) 
        
    except FileNotFoundError:
        print("Error: file not found!")
    except PermissionError:
        print("Permission to access the file has been denied.")
    except json.JSONDecodeError as e:
        print("Error decoding JSON file:", e)
    except Exception as e:
        print("Sorry, something went wrong:", e)

def get_ingredients(recipes: dict, dish: str) -> set:
    # Function to get the ingredients for a given dish from the recipes dictionary
    try:
        ingredients = set(recipes[dish]["ingredients"])
    except KeyError as e:
        return f"Error processing the information. There is no key with name {e}."
    
    return ingredients

def find_markets(markets: dict, ingredients: set) -> str:
    # This function takes two arguments: markets and ingredients, and returns a string containing all the markets that the user needs to visit in order to buy all the ingredients. If not found, relevant message is returned.
    remaining_ingredients = ingredients.copy()
    markets_to_visit = [] # List to store the markets that the user needs to visit

    while remaining_ingredients:
        best_market = None
        market_available_ingredients = set() # Set to store the available ingredients in the current market
        
        # Loop through each market and find the one with the maximum available ingredients
        for market, products in markets.items():
            common_products = set(products) & remaining_ingredients
            if len(common_products) > len(market_available_ingredients):
                best_market = market
                market_available_ingredients = common_products
                
        # If no market sells any of the remaining ingredients, return a message
        if not best_market:
            return "Unfortunately, it's not possible to cook this dish in our town, as some of the required ingredients are unavailable at our local markets."

        markets_to_visit.append(best_market)
        remaining_ingredients -= market_available_ingredients

    return f"You should visit these markets to buy the ingredients: {', '.join(markets_to_visit)}."

def main():
    recipes = read_json_file("Homework_24/recipes.json")
    markets = read_json_file("Homework_24/markets.json")
    dishes = set(recipes)
    
    dish = input("What are you going to cook? Please, enter the dish name: ").title()
    if dish not in dishes:
        print("Sorry, I have no recipe for this dish.")
        exit()
    
    ingredients = get_ingredients(recipes, dish)
    
    print(find_markets(markets, ingredients))

if __name__ == "__main__":
    main()
