#Print all numbers from 100 down to 1
#Skip multiplies of 5
#When devisible by 7, print "Boom!" instead of number 

i = 100

while i > 0:
    if i % 5 == 0:
        i -= 1
        continue      # skip multiples of 5
    elif i % 7 == 0:
        print("Boom!")
    else:
        print(i)
    
    i -= 1
