try:
    age = int(input("Enter your age:"))
    if age % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError as ve:
    print("Wrong value.")

    

