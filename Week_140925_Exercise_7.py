#write a program that asks the user for a starting number and an ending number.Print only the even numbers in that range.Input 1, 100

# Ask user for inputs
num1 = int(input("Starting number: "))
num2 = int(input("Ending number: "))

print(f"Even numbers between {num1} and {num2}:")

# Loop through the range
for i in range(num1, num2 + 1):
    if i % 2 == 0:   # Check if number is even
        print(i)
