try:
    number = int(input("Enter a number:"))
    print("The number is", number)
except ValueError as ex:
    print("Error, it is a value error.")
    print(ex)




# eval means evaluate and is the same as an integer but can take 2 values.
try:
    number_1,number_2 = eval(input("Enter two numbers:"))
    result = number_1/number_2
    print (result)
except ZeroDivisionError as zde:
    print("It is a ZeroDivisionError.")
    print(zde)
except SyntaxError as se: 
    print("It is a SyntaxError.")
    print(se)
except:
    print("Wrong value.")
else:
    print("No error.")
finally:
    print("Statment")
    