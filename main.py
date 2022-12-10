from order import get_order
from price import Price
from transaction import Transaction


flavor_dict, topping_dict, container_dict, size_dict = get_order()
price = Price(flavor_dict, topping_dict, container_dict, size_dict)

total_price = price.get_price()
print(f"Total price is {total_price}.")

paid_amount = float(input("Enter paid amount: "))
while paid_amount < total_price:
    print("Not enough money. Please try again.")
    paid_amount = float(input("Enter paid amount: "))
else:
    paid_amount, change = price.get_change(paid_amount)

transaction = Transaction(flavor_dict, topping_dict, container_dict, size_dict,\
                            total_price, paid_amount, change)
transaction.record()
transaction.display()