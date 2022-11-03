from unicodedata import name


class Parent():
    def __init__(self, familyName, cars):
        self.familyName = familyName
        self.cars = cars

    def showFamilyInfo(self):
        print("Family Name: {}\nNo of cars : {}".format(self.familyName, self.cars))

family = Parent("The Ademola's", 3)

family.showFamilyInfo()

# create a child class
class Child(Parent):
    def __init__(self, familyName, cars, name, school):
        super().__init__(familyName, cars)
        self.name = name
        self.school = school

    def childInfo(self):
        super().showFamilyInfo()
        print("Child's name : {}\nSchool  attending : {}". format(self.name,self.school))

child1 = Child("The Ademola's",3,"Jonathan","Unilag")
child1.childInfo()