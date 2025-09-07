#creating a price calculator were the user will input there item and price and I will total the price.
#setting the variables
items = []
prices = []
total = 0
while True:
    #asking the user to input there item and if there are done inputting the item, they can input "q" to quit.
    item = input("Enter a item to buy (q to quit):  ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for a {item}: $"))
        items.append(item)
        prices.append(price)
print("----YOUR CART----")
for item in items:
    print(item, end=" ")
for price in prices:
    total = total + price
print()
print(f"Your total is ${total:,}")