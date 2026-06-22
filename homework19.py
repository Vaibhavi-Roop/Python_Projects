rows = int(input("Enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")

print("Inverted triangle")
inverted_rows = int(input("Enter number of rows:"))
for inverted_i in range(inverted_rows, 0, -1):
    for inverted_j in range(inverted_i):
        print("*", end=" ")
    print(" ")
    