n = int(input("Enter the topmost number:"))
sum = 0
for i in range (1,n+1):
    sum = sum + i
    print("Sum is:",sum)
    

string = input("Enter a word:")
string_2 = ""
for i in string:
    string_2 = i + string_2
print("Word is:", string)
print("Reverse word is:", string_2)
