#   Q1 using any of the loop write a python code that sums all even numbers between 0 t0 25
# Hint: 0 + 2 + 4 + 6 .........

# Q2 Create a function named area that calculates the area of circle (PI r^2)
# PI = 22/7 the function should take an arguement called radius r should be able to work with any number

# Question 1
sum = 0
for i in range(25):
    if i % 2 == 0:
        sum = sum + i
        print("sum =",sum)

# Question 2
pi = 3.14
def CircleArea (myradius):
    myarea = pi * myradius ** 2
    print (myarea)
    
CircleArea (5)

