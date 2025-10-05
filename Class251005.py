#using with while loop to print numbers from 5 to 0
number = 5
while number >= 0:
    print(number)
    number -= 1

# Using while loop to take inputs and calculate total
total = 0
count = 0

print("Enter 4 numbers:")

while count < 4:
    try:
        num = int(input("Enter number: "))
        total += num
        count += 1
    except ValueError:
        print("Please enter a valid number!")

print(f"Total = {total}")

#Using while loop to Guess a number

secret_number = 60  # The number to guess
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break

#Random number guessing game to using while true loop
import random
secret_number = random.randint(1, 100)  # Random number between 1 and 100
guess = int(input("Guess the number between 1 and 100: "))
count = 1
while True:
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Correct! You guessed it in {count} tries.")
        break
    guess = int(input("Guess again: "))
    count += 1  

# Ramdon number for guessing using while loop
import random   
number = random.randint(1, 100)
guess = int(input("Guess the number: "))
count = 1
while guess != number:
    if guess < number:
        print("Low!")
    else:
        print("High!")
    guess = int(input("Guess the number: "))
    count += 1
print(f"Correct! You guessed it in {count} tries.")
