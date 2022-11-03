from tkinter import Y


class Person:
    def __init__(self,  name, gender, age, complexion):
        self.name = name
        self.gender = gender
        self.age = age
        self.complexion = complexion

    def showInfo(self):
        print("Name : {}\nGender : {}\nAge : {}\nComplexion : {}".format(self.name, self.gender, self.age, self.complexion))

person1 = Person("Johnson Borris", "Male", 53, "Dark")
person2 = Person("mercy Chinwo", "Female", 33, "Light skin")

person1.showInfo()
person2.showInfo()

#Class work
# create a class called calculator
# it should have 2 properties x, y
# it should have a constructor having x and y
# it should have 2 methods/function: add, subtract
# create an object called calc
# use the object to call the add and subtract method/function

class Calculator:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def add(self):
        print("sum {}" .format(self.X + self.Y))

    def subtract(self):
        print(" subtraction {}" .format(self.Y - self.X))

calc = Calculator(5, 6)

calc.add()
calc.subtract()
