""""
shop_calculator.py
The program allows the user to enter the number of items and the price
of each different item.
Then the program computes and displays the total price of those items.
"""

number_of_items = float(input("Number of items: "))

if number_of_items <= 0:
    print("Invalid Number of Items. Please Re-enter: ")
    number_of_items = float(input("Number of items: "))

item_countdown = number_of_items
total_price = 0

while item_countdown > 0:
    total_price = total_price + float(input("Price of item: "))
    item_countdown = item_countdown - 1
print("Total price for ",number_of_items," is $",total_price)