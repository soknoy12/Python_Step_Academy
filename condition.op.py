age = int(input("Enter Your age:"))
if(age >= 1 and age < 13):
    print("kid") 
elif(age >= 13 and age < 19):
    print("Teenager")
elif(age >= 19 and age < 22):
    print("Adult")
elif(age >= 22):
    print("Chill Guy")
else :
    print("Invalid")