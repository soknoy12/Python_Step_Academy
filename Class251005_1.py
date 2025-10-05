#Print numbers from 100 to 1
#Skip multiples of 5
#For multiples of 7, print "Boom!" instead of the number
num = 100

while num > 0:
    if num % 5 != 0:  # Only process if not multiple of 5
        if num % 7 == 0:
            print("Boom!")
        else:
            print(num)
    num -= 1