# დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს, როცა მომხმარებელმა იყიდა ბიტკოინი, ასევე მიიღებს დოლარში თანხას, რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად და ეკრანზე გამოიტანს დოლარში თანხას, რომელიც მოიგო ან დაკარგა დღევანდელი ფასის გათვალისწინებით.
import datetime
from forex_python.bitcoin import BtcConverter

# Introduction
print("Enter the date (YY/MM/DD) you bought your bitcoin, also the dollar amount paid for it, and I will tell you how much you've won or lost based on today's price.")

# Ask the user for the date and price
btc_purchase_year = int(input("Enter the year you bought the bitcoin: "))
btc_purchase_month = int(input("Enter the month you bought the bitcoin: "))
btc_purchase_day = int(input("Enter the day you bought the bitcoin: "))
btc_purchase_price = float(input("Enter the amount in USD that you've paid for the bitcoin: "))

# Format the puchase date
purchase_date = datetime.date(btc_purchase_year, btc_purchase_month, btc_purchase_day)

# Create a BtcConverter object
btc = BtcConverter()

# Get the price of bitcoin today (in USD)
btc_price_today = btc.get_latest_price('USD')

# Get today's date
today = datetime.date.today()

# Get the current year
current_year = today.year

# Calculate profit or loss
profit_loss = btc_price_today - btc_purchase_price

# Print the result (profit, loss or the same)
if btc_purchase_year > current_year:
    print("Please, enter the true year you bought the bitcoin, try again!")
else:
    if profit_loss > 0:
        print("Congratulations! As of", today, ", you made a profit of", profit_loss,  "USD")
    elif profit_loss < 0:
        print("Sorry! As of", today, ", you suffered a loss of", abs(profit_loss))
    else:
        print("As of", today, ", you neither made a profit nor suffered a loss.")
