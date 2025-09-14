#num1 = 8
#num2 = 2

# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter operator: ")
if operator == "+":  
        print("The result for num1 + num2: ",num1 + num2)  
elif operator == "-":
        print("The result for num1 - num2: ",num1 - num2)
elif operator == "*":
        print("The result for num1 * num2: ",num1 * num2)       
elif operator == "/":
        if num2 == 0:
            print("Cannot divide by Zero")
        else:            
            print("The result for num1 / num2: ",num1 / num2)
else:
        print("that is an Invalid Operator")
        

        



