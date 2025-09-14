#if...elif...else: (in case multiple if)
# age 1 to 13 Kid
# age 13 to 19 teenager
# age 19 to 25 Adult
# age 25 up is chill guy
age = int(input("Enter your age: "))
if age > 1 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 19:
    print("You are a teenager")
elif age >= 19 and age < 25:
    print("You are a adult")
elif age >= 25:
    print("You are a chill guy")
else:
    print("Invalid information")
