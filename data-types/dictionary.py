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

#delete
del seun["age"]
print(seun)

#Nesting
student = [
    {
        "name": "seun",
        "id": "1",
        "gender":"male",
        "course":"web development"
    },
        {
        "name": "Anu",
        "id":"2",
        "gender":"male",
        "course":"Python Programming"
    },
        {
        "name": "Malik",
        "id":"3",
        "gender":"male",
        "course":"web development"
    },
        {
        "name": "Promise",
        "id":"4",
        "gender":"female",
        "course":"web development"
    }
]
#accessing the name of the third dictionary in the list
print(student[2]["name"])

#clear
seun.clear()
print(seun)

#create an array of dictionary with at least five dictionary within called car
# 1. keys = make, model, price, name
# 2. Keys = make, model,name
# 3. keys = make, model, price, name
# 4. Keys = make, model,name
# 5. Keys = make, model, price, name
# check if price key exist then don't add  the price property with a default price of 0

# for Loop
names = ["Ade", "James", "Hannah"]
for name in names:
    print(name)