try:
    a = float(input("Enter a number to add:"))
    b = float(input("Enter another number:"))
    def add (a,b):
       return(a+b)
    print(add(a,b))
except ValueError:
    print("That is not a number!")

try:
    c = float(input("Enter a number to subtract:"))
    d = float(input("Enter another number:"))
    def subtract (c,d):
         return(c-d)
    print(subtract(c,d))
except ValueError:
    print("That is not a number!")

try:
    e = float(input("Enter a number to multiply:"))
    f = float(input("Enter another number:"))
    def multiply (e,f):
        return(e*f)
    print(multiply(e,f))
except ValueError:
    print("That is not a number!")

try:
    g = float(input("Enter a dividend:"))
    h = float(input("Enter a divisor:"))
    def divide (g,h):
        return(g/h)
    print(divide(g,h))
except ZeroDivisionError:
    print("You can't divide by 0!")
except ValueError:
    print("That is not a number!")