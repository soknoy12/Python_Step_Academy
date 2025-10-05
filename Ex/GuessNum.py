## Pick a random number between 1 and 100. Ask the user to guess until they get it right.
## -Print "Too High!" if guess is above the number.
## -Print "Too Low!" if the guess is below the number.
## -Print "You got it!" if the guess is correct.
## -Count the number of attempts and show it at the end.

import random
number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    elif guess > 100:
        print("Error please enter number from 1 to 100!")
    else:
        print("Correct!")
        print("Number of attempts:", attempts)
        