import json

person = '{"name":"John", "age": 25, "city" : "Lagos"}'

newPerson = json.loads(person)
print(newPerson["name"])

player = {
    "name" : "K Benzema",
    "team": "Real Madrid",
    "age": 34
}

#converts python dictionary to json 
newPlayer = json.dumps(player, indent=5, sort_keys=True)

print(newPlayer)

# Assignment 
# using filter high order function 
# count the number of people that are online in the list below

whatsapp =  [
    {
        "name": "Abraham",
        "status" : "Life is good",
        "online" : False
    },
     {
        "name": "Seun",
        "status" : "I have too muuch money",
        "online" : True
    },
     {
        "name": "God's Power",
        "status" : "All power belongs to God",
        "online" : False
    },
     {
        "name": "Anu",
        "status" : "Enjoying my life like there is no tomorrow",
       "online" : True
    },
     {
        "name": "Favour",
        "status" : "Sweet mom sweet. I can't wait to go and eat.",
       "online" : True
    },
    {
        "name": "Malik",
        "status" : "I am a rich kid.",
        "online" : False
    },
    {
        "name": "Saheed",
        "status" : "Get well soon bro. i've got you!",
        "online" : True
    }
]

people = json.dumps(whatsapp)
def people_online(x):
    info = x
    condition0 = info["online"] == True
    return condition0
wepeople = dict(filter(people_online, people.online()))
print(wepeople)
