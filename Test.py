#Problem 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello ", name, " you are ", age, " years old")

#Problem 2
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
    print(num1, " is bigger than ", num2)  
elif num1 < num2:
    print(num2," is bigger than ", num1)
else:
    print(num1, " is equal to ", num2)

#Problem 3
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))
average = (num1 + num2 + num3) / 3
print("The average is: ", average)

#Play the Guessing Game
secret = 88
num = 0
while num != secret:
    num = int(input("Enter a number between 1-100: "))
    if num < secret:
        print("Too low")
    elif num > secret:
        print("Too high")
    else:
        print("Congratulations! You guessed the secret number.")
        print("The secret number is ", secret)
