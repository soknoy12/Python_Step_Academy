#Simple Calculator (Multiple Conditions)
#Write a program that takes two numbers and an operator (+, -, *, /) and prints the result. 
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Error: Division by zero is not allowed.")

#One more Example
#Write a program that takes two numbers and an operator (+, -, *, /) and prints the result with a message.
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# operator = input("Enter an operator (+, -, *, /): ")
# if operator == "+":
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif operator == "-":   
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif operator == "*":
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif operator == "/":
#     if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Error: Invalid operator.")   