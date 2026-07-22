items = ['pencil', 'eraser', 'ruler', 'sharpener']
stock_count = [0, 10, 12, 4]
inventory = {item: count for item, count in zip(items, stock_count)}
print(inventory)
in_stock_items = [i for i in items if inventory[i]>0]
print(in_stock_items)
customer_choice = input("What would you like to get?")
if customer_choice not in inventory or inventory [customer_choice] ==0 :
    print("That is not in our stock")
    exit()
else:
    print("That is in our stock")