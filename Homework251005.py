#Ask the user for a number n
#Print all prime numbers between 2 and n using a for loop 

n = int(input("Enter a number n: "))    
for num in range(2, n + 1):  
    is_prime = True  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            is_prime = False  
            break  
    if is_prime:  
        print(num)

#Ask the user for a number
#Use a while loop to keep reversing its digits and adding until the result becomes a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def reverse_number(num):
    return int(str(num)[::-1])
number = int(input("Enter a number: "))
while not is_palindrome(number):
    reversed_num = reverse_number(number)
    number += reversed_num
    print(f"{reversed_num} + {number - reversed_num} = {number}")
print(f"Palindrome found: {number}")
