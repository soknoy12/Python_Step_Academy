#Solve Problem:1
# Write a program to: 
# Ask the user for their name and age. 
# Print: Hello [name], you are [age] years old.
#Step:1 Read probem
  # To input name and age
  # print name, print age
#Step:2 Think of steps
  # Two input (name and age)
  # print them out
#Step:3 Write it in code
#Step:4 Test it
#Step:5 Fix mistakes
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello",name,",you are",age,"years old")

#Solve Problem:2
# Problem 2: Write a program that asks the user for two numbers and prints the larger one.
num_1 = int(input("Enter your number: "))
num_2 = int(input("Enter your number: "))
if num_1 > num_2:
    print("Larger number is: ",num_1)
elif num_1 <= num_2: #it is not correct yet try to search
    print("Your number is equally:",num_2)
else:
    print(num_1)
          
#Solve Problem:3
# Problem 3: Write a program that asks for three numbers and prints their average.
num_1 = int(input("Enter your number: "))
num_2 = int(input("Enter your number: "))
num_3 = int(input("Enter your number: "))

print("Average Number is: ",(num_1 + num_2 + num_3)/3)

