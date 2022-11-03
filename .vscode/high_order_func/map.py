# map is used to modify what is inside a list
numbers = [2, 5, 6, 2, 6, 2]

def multiply(x):
    return x * 2

newList = map(multiply, numbers)

# using lambda func
# newList = map(lambda x: x * 2, numbers)

print(list(newList))