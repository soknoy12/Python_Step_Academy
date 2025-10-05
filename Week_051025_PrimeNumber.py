#Ask the user for a number n.
#Print all prime numbers between 2 and n using a for loop

n = int(input("Enter a number: "))

print(f"Prime numbers between 2 and {n}:")

for num in range(2, n + 1):
    is_prime = True  # assume it's prime

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # stop checking once divisible

    if is_prime:
        print(num, end=" ")
