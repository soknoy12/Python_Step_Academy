
# Simple Calculator (Multiply Condition)

# Take inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Print result
print("Result:", result)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operater = input("Enter the operater: ")

if operater == "+":
    print(num1 + num2)
elif operater == "-":
    print(num1 - num2)
elif operater == "*":
    print(num1 * num2)
elif operater == "/":
    if num2 == 0:
        print("Can not device by zero")
    else:
        print(num1 / num2)
else:
    print("invalid operater")

