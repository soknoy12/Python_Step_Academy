#Hard-Guess the Secret Number
#Pick a random number between 1 and 100.
#Ask the user to guess until they get it right
#Print "Too high" if guess is above the number.
#Print "Too low" if guess is below the number.
#Print "Correct" when guessted.
#count the number of attempts and show it at the end.

# Hard - Guess the Secret Number

import random

secret = random.randint(1, 100)  # pick a random number
attempts = 0  # to count how many guesses

print("I'm thinking of a number between 1 and 100...")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  # increase attempts each time

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break  # exit loop when correct

print(f"You guessed it in {attempts} attempts!")
