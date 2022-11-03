# while loop
i = 0
while i < 10:
    if i % 2 == 0:
       print(i)
    i = i + 1

#using break
i = 0
while i < 20:
    print(i)
    if i == 5:
        break
    i = i + 1

# using continue to skip the particular number which is 5 in the case
i = 0
while i < 20:
    i = i + 1
    if i == 5:
        continue
    print(i)
