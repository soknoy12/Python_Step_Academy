#Write a program to check if a person is a teenager (age between 13 and 19). by asking user to input their age. print "You are a teenager."
age = int(input("Please enter your age: "))
if 13 <= age <= 19: # if age >= 13 and age <= 19:
    print("You are a teenager.")
elif age == 0:
    months = int(input("You are less than a year old. Please enter your age in months: "))
    if 0 < months < 12:
        print("You are an infant.")
elif 1 <= age <= 12: # elif age >= 0 and age <= 12:
    print("You are a child.")
elif 20 <= age <= 39: # elif age >= 20 and age <= 39:
    print("You are a young adult.")
elif 40 <= age <= 64: # elif age >= 40 and age <= 64:
    print("You are a middle-aged adult.")
elif 65 <= age <= 120: # elif age >= 65 and age <= 120:
    print("You are a senior citizen.")
else:
    print("Invalid age input.") 