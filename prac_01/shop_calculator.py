"""
This program is to make a shop calculator that displays how many items
will the user buy, the user will put the price of each items, and this program
will calculate the total final price for all items.
"""

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number, please try again..")
    number_of_items = int(input("Number of items: "))

total_price = 0

for i in range (0,number_of_items,1):
    price_of_items = float(input("Price of item: "))
    total_price = total_price + price_of_items


if total_price > 100:
    final_price = total_price - (total_price * 0.1)
else:
    final_price = total_price



print("Total price for {}".format(number_of_items) , "items is ${:.2f}".format(final_price))

