# Exercise 4:
# Write a program that asks the user for a starting number and an ending number. 
# Print only the even numbers in that range.


a = int(input("Please Enter your starting number: "))
b = int(input("Please Enter your ending number: "))

for i in range(a, b):
    if i % 2 == 0:
        print(i)