import random
import math
lucky = random.randint(1,10)
print(lucky)
fun = ['Build a dollhouse', 'make a game book', 'dye a shirt', 'invent your own game']
choice = random.choice(fun)
print(choice)
number =  random.randint(1,5)
while True:
    guess = int(input("Guess a number between 1 and 5:"))
    if guess == number:
        print("You win! That was the lucky number")
        break
    else:
        print("Wrong! Try again")
decimal = float(input("Enter a decimal number:"))
up = math.ceil(decimal)
print("The number rounded up is", up)
down = math.floor(decimal)
print("The number rounded down is", down) 
x = -6
print(x)
y = 7
print(y)
sign = math.copysign(x,y)
print(sign)
absolute = math.fabs(x)
print("The absolute value of -6 is", absolute)
two = int(input("Enter a number:"))
more = int(input("Enter another number:"))
numbers = math.gcd(two, more)
print("The gcd of those numbers is", numbers)
