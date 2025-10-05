age = int(input("Enter your age: "))
#1 - 13 kid
#13 - 19 teenager
#19 - 22 adult
#22 up chill guy

if age >= 2 and age < 13:
    print("kid")
elif age <=1 and age >= 0:
    if age == 0:
        month = int(input("How many month were you born: "))
        if month >= 0:
            print("Valid month")
        else:
            print("Invalid month")
        print("Infant")
elif age >= 13 and age < 19:
    print("teenager")
elif age >= 19 and age < 22: 
    print("adult")
elif age >= 22: 
    print("Chill guy")
else: 
    print("Invalid")

