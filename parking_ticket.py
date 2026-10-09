def calculate_change(paid, price):
    change = paid - price
    return change
ticket_price = 30
print(f"This parking ticket costs {ticket_price} dollars")
print("Accepted cash: $5, $10, $20")
total_inserted = 0
money_inserted = 0
while True:
    coin = int(input("Insert money:"))
    if coin != 5 and coin != 10 and coin != 20:
        print("Invalid coin try again")
        continue
    total_inserted += coin 
    money_inserted += 1
    print(f"Inserted {coin} \n Total so far: {total_inserted}")
    if total_inserted>=money_inserted:
        print("Ticket sucessfully paid!")
        break
    else: 
        print("More money needed")
        continue
change_value = calculate_change(total_inserted, ticket_price)
if change_value == 0:
    pass
else:
    print("Change: $", change_value)

