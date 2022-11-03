# assignment
firstname, surname = "Jonathan","Samu"
print(firstname, surname)

# control structure
# if else
today = "Monday"
if today == "Friday":
    print("Thank God is Friday")
else:
    print("I guess today is not Friday")

#short hand

age = 21
print("You are an under age") if age < 18 else print("You are an adult")  

# elif
day = input("what is today please?")
if day == "Monday" or day == "Tuesday" or day ==  "WEDNESDAY" or day == "Thursday":
    print("Concentrate on work!")
elif day =="Friday":
    print ("Jollificate")
elif day == "Saturday":
    print("Rest")
else:
    print("Go to church")