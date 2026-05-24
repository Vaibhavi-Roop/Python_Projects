print("Half a pyramid of *")
rows = int(input("Enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()
print ("Floyd's Triangle")

rows = int(input("Enter number of rows:"))
number = 1
for i in range(rows):
    for j in range(i+1):
        print(number, end=" ")
        number = number+1
    print()