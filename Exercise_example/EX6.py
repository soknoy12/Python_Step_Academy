import random

number = random.randint(1,100)
guess = int(input("Guess the number: "))
count = 1
while guess != number:
    if guess > number:
        print("Lower")
    else:
        print("Higher")
    guess = int(input("Guess the number: "))
    count += 1
print(f"correct you have tried {count} times")
