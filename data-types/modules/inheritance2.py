from unicodedata import name


class Parent():
    def __init__(self):
        self.familyName = "The Ademola's"
        self.cars = 3

    def showFamilyInfo(self):
        print("Family Name: {}\nNo of cars : {}".format(self.familyName, self.cars))


# create a child class
class Child(Parent):
    def __init__(self, name, school):
        super().__init__()
        self.name = name
        self.school = school

    def childInfo(self):
        print("*********************************************************")
        super().showFamilyInfo()
        print("Child's name : {}\nSchool  attending : {}". format(self.name,self.school))

child1 = Child("Jonathan","Unilag")
child1.childInfo()

child2 =Child("Mary", "Covenant University")
child2.childInfo()