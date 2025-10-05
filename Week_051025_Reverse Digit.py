#Reverse Digits until Palindrome
#Ask the user for a number.
#Use a while loop to keep reversign its digits and adding until the result becomes a palindrome.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = int(input("Enter a number: "))

while not is_palindrome(n):
    reverse_n = int(str(n)[::-1])
    print(f"{n} + {reverse_n} = {n + reverse_n}")
    n = n + reverse_n

print(f"Palindrome found: {n}")
