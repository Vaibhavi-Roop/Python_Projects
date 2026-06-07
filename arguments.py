def total_amount(bill, tip):
    total = bill *(1 + 0.01 * tip)
    total = round (total, 2)
    print ("Your total amount is $", total)
total_amount(748, 29)

def cube(number):
    return number*number*number
print(cube(5))