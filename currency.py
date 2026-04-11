amount = int(input("How much do you want to withdraw?"))
note_1 = amount //100
note_2 = (amount % 100) //50
note_3 = ((amount % 100) % 50) //20
note_4 = (((amount % 100) % 50) % 20) //10
note_5 = ((((amount % 100) % 50) % 20) % 10) //5
note_6 = (((((amount % 100) % 50) % 20) % 10) % 5) //2
note_7 = ((((((amount % 100) % 50) % 20) % 10) % 5) % 2)//1
print("The number of $100 notes are",note_1)
print("The number of $50 notes are",note_2)
print("The number of $20 notes are",note_3)
print("The number of $10 notes are",note_4)
print("The number of $5 notes are",note_5)
print("The number of $2 notes are",note_6)
print("The number of $1 notes are",note_7)