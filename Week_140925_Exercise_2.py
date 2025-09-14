#match case condition

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter operator: ")
match operator:
    case "+":  
        print("The result for num1 + num2: ",num1 + num2)  
    case "-":
        print("The result for num1 - num2: ",num1 - num2)
    case "*":
        print("The result for num1 * num2: ",num1 * num2)       
    case "/":
        if num2 == 0:
            print("Cannot divide by Zero")
        else:        
            print("The result for num1 / num2: ",num1 / num2)
    case _:
        print("that is an Invalid Operator")
        

        



