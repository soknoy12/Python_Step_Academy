import random
#Random number for guessing
number = random.randint(1,100)
guess = int(input("Guess the number: "))
count = 1
while guess != number:
    if guess > number:
        print("Higher")
    else : 
        print("Lower")
    guess = int(input("Guess the number: "))
    count += 1
    print(f"Correct you have tried {count} times")


