from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from unicodedata import name
from unittest import result


print(True + True)
print(False * 20)

a = 5; b = 17

result = a * 2 + b - 1
print(result)

name = "Aptech"
print(name)

print("\a")
#concatenation
print("Aptech" + "Computer")
#Repetition
print("God bless me o!" * 20)
#slice
school = 'University of Lagos'
print(school[5])
#range
print(school[14:20])
#membership
print("Lagos" in school)
print("Abuja" not in school)
#raw
print(R"/n")
#format
print("He attends %s" %school)
#triple quote
quote = """Hello
I think Python 
is so nice
already!
"""
print(quote)

#uppercase
print(school.upper())
#length
print(len(school))
#list
persons = ['Abayomi', 'Moses', 'Bello']
print((persons)[2])
print(len(persons))
#type
print(type(persons))
print(type(school))

#List constructor
states = list(("Lagos", "Ogun", "Osun", "Ondo"))
print (states)
#append
states.append("Borno")
print(states)
#insert
states.insert(3,"Abuja")
print(states)
#extend
persons.extend(states)
print(persons)
#index
print(states.index("Abuja"))
#remove
states.remove("Osun")
print(states)
#sort
states.sort()
print(states)
#reverse
states.reverse()
print(states)
#pop
states.pop(3)
print(states)
#Assignment 1:
#Use list constructor to create a lsit called cars with the following names: G-wagon, Lexus, Toyota 2020
#Use one of the lists methods to add another car Kia in between Lexus and Toyota
#Sort the list in a reverse order

cars = list(('G-wagon', 'Lexus', 'Toyota 2022'))
print(cars)
cars.insert(2,"Kia")
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)
#min
sales = [60000, 34000, 7400, 87400, 20000]
print(min(sales))

#max
print(max(sales))

#slice
print(sales[0:3])
print(sales[3:])
print(sales[3:-1])