#Reverse Countdown with skips
#Print all numbers from 100 down to 1
#Skip multiples of 5
#When a number is divisible by 7, print " Boom" instead of the number.

# Reverse Countdown with Skips

for i in range(100, 0, -1):
    # Skip multiples of 5
    if i % 5 == 0:
        continue
    
    # Replace multiples of 7 with "Boom"
    if i % 7 == 0:
        print("Boom")
    else:
        print(i)
