age = int(input("Enter ur age"))

if age > 1 and age <13:
    print("kid")
elif age <= 1 and age >= 0:
    if age == 0:
        month = int(input("how many month you were born"))
        if month >= 0:
            print("vaild month")
        else:
            print("invaild month")
    print("infant")
elif age >= 13 and age < 19:
    print("teenager")
elif age >=19 and age < 22:
    print("adult")
elif age < 22:
    print("chill guy")
else:
    print("invaild")