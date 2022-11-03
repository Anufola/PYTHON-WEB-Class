#tuple
students = ("Seun", "Anu", "Malik", "God's Power","Saheed","Ade")

#length
print(len(students))

#type
print(type(students))

# accessing element
print(students[1])

#last element
print(students[-1])

#check if something exists
if "Ade" in students:
    print("Yes,it is there")

#converting a tuple to a list so that you can add something to it
students = list (students)    
students.append("Jonathan")
print(students)

#converting back to tuple
students = tuple(students)

#counting with tuple
print(students.count("Ade"))

#Unpacking
id = ("001", "002", "003", "004", "005")
(Malik,Seun,Anu,*others) = id
print(others)