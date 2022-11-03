# Local
def sayHI():
    global age
    age = 20
    print(age , "years old says hi")

sayHI()

# print(age) will not work cos age is constrained to sayHI however you can convert it to global by using the keyword
print(age)

# global variable where the declaration is not in the function
school = "Aptech"

def greetings():
    print("Hello, I am a student of", school)

greetings()
print(school, "is a tech school")