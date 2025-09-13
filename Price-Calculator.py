# Price Calculator
# This program allows a user to input items and their prices,
# then calculates and displays the total price of all items.
# I First created a list to store items and prices.
items = []
prices = []
# I created a variable to store the total price.
total = 0
# I created a loop to allow the user to input multiple items and prices, if the user inputs an invalid item, it prompts them to enter a valid item, and if they input 'q', it exits the loop.
while True:
    item = input("Enter a item to buy (q to quit): ")
    if item == "":
        print("You must enter an item or 'q' to quit.")
    elif item.isalpha() == False:
        print("You must enter an item or 'q' to quit.")
    elif item.lower() == "q":
        break
    else:
        items.append(item)
        price = float(input(f"Enter the price for a {item}: $"))
        prices.append(price)
# After the loop, I printed the items and their prices in a formatted manner, and calculated the total price.
print("----YOUR CART----")
print_items = [print(item, end=" | ") for item in items]
print()
print_prices = [print(f"${price:,.2f}", end=" | ") for price in prices]
print()
total_price = [total := total + price for price in prices]
print(f"Your total is ${total:,.2f}")