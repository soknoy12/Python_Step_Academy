num1 = int(input("Choose one number "))
num2 = int(input("Choose other number "))

operator = input("Choose an operator ")

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2 
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divine by 0"
    case _:
        result = "Invaild"

print(result)