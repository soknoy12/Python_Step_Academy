num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# count and if
for i in range(num1, num2 + 1):  # include num2
    if i == 3:
        print("Three")
    elif i == 5:
        print("Five")
    else:
        print(i)