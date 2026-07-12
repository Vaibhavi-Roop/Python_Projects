number_1 = int(input("Enter a number:"))
number_2 = int(input("Enter another number:"))
number_3 = int(input("Enter another number:"))
temp = number_1
number_1 = number_2
number_2 = number_3 
number_3 = temp
print("The exchanged values are:", number_1, number_2, number_3)