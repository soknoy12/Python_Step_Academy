n = int(input("Enter Number : "))
for number in range(2, n):     # loop from 2 to n
    is_prime = True              # we start by assuming it's a prime number

    # check if number has any divisors other than 1 and itself
    for i in range(2, number):
        if number % i == 0:      # if it divides evenly, it's not prime
            is_prime = False
            break                # stop checking further

    # if it stayed True, then it's prime
    if is_prime:
        print(number)
            
    



