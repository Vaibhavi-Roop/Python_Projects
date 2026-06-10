#break and continue can't work without a loop

word = input("Enter a word:")
for letter in word:
    if letter == 'N' or letter == 'n':
        print("Required letter is found.")
        break
    else:
        print("Letter is not found")
        

a = 10
while a > 0:
    a = a-1
    if a == 5:
        continue
    print (a) 

 