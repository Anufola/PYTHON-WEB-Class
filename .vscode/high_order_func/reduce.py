import functools

numbers = [3, 5, 6, 3, 6]

sum = functools.reduce(lambda x, y : x + y, numbers)

print(sum)