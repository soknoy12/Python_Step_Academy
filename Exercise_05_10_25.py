#Print all numbers from 100 down to 1
#Skip multiplies of 5
#When devisible by 7, print "Boom!" instead of number 
#Example out put 
#100
#99
#Boom!
# Print all numbers from 100 down to 1
# Skip multiples of 5
# When divisible by 7, print "Boom!" instead of the number

# Print all numbers from 100 down to 1
# Skip multiples of 5
# When divisible by 7, print "Boom!" instead of the number



# Print all numbers from 100 down to 1
# Skip multiples of 5
# When divisible by 7, print "Boom!" instead of the number

for i in range(100, 0, -1):
    if i % 5 == 0:
        continue  # skip multiples of 5
    elif i % 7 == 0:
        print("Boom!")
    else:
        print(i)
