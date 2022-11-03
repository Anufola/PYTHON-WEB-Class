numbers = [2, 4, 3, 5, 7, 8, 11, 10, 12, 3]

oddNumbers = filter(lambda x : x % 2 != 0, numbers)

print(list(oddNumbers))