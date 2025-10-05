import random
#blank///
#! This is about ALL LOOPS in Python.
#? For in Range() function loop. it iterate over fix number of times.

# for x in reversed(range(1, 11)):
#     print(x)
# print("Happy fucking new Year!")
# for n in range(1, 20):
#     if n == 13:
#         continue #* skip 13 and continue to the next number.
#     else:
#         print(n)
# for y in range(1,5):
#     if y == 3:
#         break #* stop the loop at 3.
#     else:
#         print(y)

# x = 1
# for y in range(1, 11):
#     result = x * y
#     print(f"{x} x {y} = {result}")


#! Write a program asks the user for a starting number and ending number print only even numbers in range.

# print("This Program only show Even Number")
# x = int(input("Choose a starting number: "))
# y = int(input("Choose a ending number: "))

# for z in range(x, y + 1):
#     if z % 2 == 0:
#         print(z)

#! Write a program, takes two numbers and operators (+,-,*,/)

# print("This is a calculator Program")
# z = (input("Choose the operators (+,-,*,/): "))
# x = int(input("Choose First Number: "))
# y = int(input("Choose Second Number: "))

# match z:
#     case '+':
#         result = x + y
#         print(result)
#     case '-':
#         result = x - y
#         print(result)
#     case '*':
#         result = x * y
#         print(result)
#     case '/':
#         result = x / y
#         print(result)


#Print numbers until the user enters: 0
# number = int(input("Enter a number: "))
# while number != 0:
#     print(f"You have enter {number}")
#     number = int(input("Enter a number: "))

# print("End of code")

# number1 = int(input("Enter n: "))
# for number2 in range(number1, 0, -1):
#     print(number2)

# total = 0

# while (True):
#     num = int(input("Enter number: "))
#     if num == 0:
#         break
#     else:
#         total += num
# print(total)
    


# attempt = 0
# while (True):
#     guess = int(input("Guess number 1 to 100: "))
#     attempt += 1
#     correct = 69

#     if guess == correct:
#         print(f"Correct! you have try {attempt} times") 
#         break
#     elif guess < 69:
#         print("Too low")
#     else:
#         guess >= 99
#         print("Too high")
    
#different approach

number = random.randint(1,100)
guess = int(input("Enter number: "))
count = 1

while guess != number:
    if guess > number:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess the numbers: "))
    count += 1
print(f"Correct! You have tried {count} times")