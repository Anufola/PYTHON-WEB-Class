# if there are two arguement
from re import X


def add(x, y):
    return x + y

print("answer=", add(4,7))

# if you dont know the number of arguement
def add(*x):
    sum = 0
    for i in x:
        sum =sum + i
    return sum

print("answer=", add(4,7,5,70,230))

# default arguement

def greet(name = "Anonymous"):
    print("Good afternoon", name)

greet()
greet("Nino")

# pass
def square():
    pass

# recursion
def factorial(n):
    if n == 1:
        return 1
    else: 
        fact = n * factorial(n -1 )
    return fact

print("factorial =", factorial(5))

# lambda
square = lambda x: x * x 
print("Square of 2 is", square(2))