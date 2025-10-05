#Print "Too hight!" if guess is above the number
#Print "Too low!" if guess is below the number 
#Print "Correct!" When guessed
#Count the number of attempts and show it at the end. 
#Example
#Guess: 50
#Too low!
#Guess: 75
#Too hoght!
#Correct!You guessed it in 3 tries

# Set the secret number
secret_number = 63

# Start counting attempts
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Ask the user for the first guess
guess = int(input("Guess the number: "))
count = 1

# Keep looping until the guess is correct
while guess != number:
    if guess > number:
        print("Higher")
    else:
        print("Lower!")
    # Ask for the next guess
    guess = int(input("Guess the number: "))
    count += 1

# When the guess is correct, print the result
print(f"Correct! You guessed it in {count} tries.")




