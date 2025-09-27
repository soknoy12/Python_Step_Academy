num1 = int(input("Enter first Number : "))
num2 = int(input("Enter Second Number : "))
operator = input("Enter Operator : ")
match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 + num2)
    case "/":
        if num2 != 0 :
            print(num1 / num2)
        else:
            print("Unsupported Operator")
    case _ :
        print("Invalid Operator")
