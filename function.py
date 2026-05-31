def well_wishes():
    print("hello")
    print("how are you")
well_wishes()

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
number_1 = int(input("Enter first number:"))
number_2 =int(input("Enter second number:"))
sum = add(number_1, number_2)
sub = subtract(number_1,number_2)
m = multiply(number_1,number_2)
div = divide(number_1,number_2)
print(sum)
print(sub)
print(m)
print(div)