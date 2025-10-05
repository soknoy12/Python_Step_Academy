#Problem 1
#Step 1: Read the problem
# 1. Write a program to: Ask the user for their name and age.
# 2. Print: Hello [name], you are [age] years old.
#Step 2: Thinking about steps
# 1. Get user input for name 
# 2. Get user input for age
# 3. Print the output in the required format
#Step 3: Write the code
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old." )

#Problem 2
#Step 1: Read the problem
# 1. Write a program that as user for two numbers.
# 2. Print the larger number.
#Step 2: Thinking about steps
# 1. Get user input for first number
# 2. Get user input for second number
# 3. Compare the two numbers
# 4. Print the larger number
#Step 3: Write the code
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
if a > b:
    print(a, "is larger than", b)
elif b > a:
    print(b, "is larger than", a)
else:
    print(a, "is equal to", b)

#Problem 3
#Step 1: Read the problem
# 1. Write a program that as user for two numbers.
# 2. Print out the average of the numbers.
#Step 2: Thinking about steps
# 1. Get user input for first number
# 2. Get user input for second number
# 3. Get user input for third number
# 4. Add the three numbers
# 5. Divided the sum by 3
# 6. Print the output
#Step 3: Write the code
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))
average = (a + b + c) / 3
print("The average of", a, b, "and", c, "is", average)

#Step 4: Test the code
#Step 5: Fix mistakes
# All the code is working fine