Cost_price = float(input("Enter cost price here:"))
Selling_price = float(input("Enter selling price here:"))
if Cost_price > Selling_price:
    Loss = Cost_price-Selling_price
    print("Loss of", Loss)
elif Cost_price < Selling_price:
    Profit = Selling_price-Cost_price
    print("Profit of", Profit)
else:
    print("No profit or loss")
    