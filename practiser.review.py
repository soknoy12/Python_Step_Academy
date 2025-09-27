num1 = int(input("Enter Number1 : "))
num2 = int(input("Enter Number2 : "))
operator = input("Enter Operator : ")

"""print(f"Sum = {num1} + {num2}")
print(f"Sub = {num1} - {num2}")
print(f"Multiplication = {num1} * {num2}")
print(f"Division = {num1} / {num2}")"""
if(operator == "+"):
    print(num1 + num2)
elif(operator == "-"):
    print(num1 - num2)
elif(operator == "*"):
    print(num1 / num2)
elif(operator == "/"):
    if(num2 == 0):
        print("Cannot devided by zero")
    else:   
        print(num1 / num2)


else :
    print("Invalid Operator")
    