age = 25
print(age)
age = 25
print(float(age))


name = input("Enter your name: ")
print("My name is", name)

#If condiction
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade E")
else:
    print("Grade: F")
#Number Guessing Game (Mini)
secret = 7
guess = int(input("Guess the number (1-10): "))

'''if guess == secret:
    print("Correct! 🎉")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")'''

result = "Correct! 🎉 " if guess == secret else("Too low" if guess < secret else"Too hight")
print("Result", result)



