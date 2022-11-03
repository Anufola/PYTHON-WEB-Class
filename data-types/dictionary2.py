#dictionary
seun = {
    "surname": "Kolade",
    "state" : "Ogun",
    "age" : 20,
    "hobbies" : ["Eating", "Sleeping", "Playing game"]
}
#accessing
print(seun["hobbies"])
# keys
print(seun.keys())
#values
print(seun.values())
#change values
seun["age"] = 25
print(seun)
#Assingment
# check if gender exist then don't add it else add the gender property with an empty string
if "age" in seun:
    print("Yes,it is there")
    

#nesting
people = {1: {'name':'John','age':'27','sex':'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people[1]['name'])

names = ["Ade", "James", "Hannah"]
for name in names:
    print(name)

#create an array of dictionary with at least five dictionary within called car
# 1. keys = make, model, price, name
# 2. Keys = make, model,name
# 3. keys = make, model, price, name
# 4. Keys = make, model,name
# 5. Keys = make, model, price, name
# check if price key exist then don't add  the price property with a default price of 0

car = [ {'make':'Toyota','model':'2022','price':38000,'name':'4runner'},
       {'make':'Honda','model':'2021','name':'Civic'},
       {'make':'Toyota','model':'2022','price':37000,'name':'Avalon'},
       {'make':'Honda','model':'2021','name':'Insight'},
       {'make':'Lexus','model':'2020','price':25000,'name':'ES 350'}]

for ride in car:
    if "price" not in ride:
        ride["price"] = 0

print(car)


