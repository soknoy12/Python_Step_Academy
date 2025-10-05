num1 = int(input("Enter the first number: "))
num2 = int(input("Enter The second number: "))
operator = input("Enter operator: ")
match operator:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
    case _:
        print("Invalid Operator")

languages = ['Swift', 'Python', 'Go']
# Access elements of the list one by one 
for lang in languages:
    print(lang)