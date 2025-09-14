num1 = int(input("Choose one number "))
num2 = int(input("Choose other number "))

operator = input("Choose an operator ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divine by 0 ")
    else:
        print(num1 / num2)
else:
    print("Invaild")