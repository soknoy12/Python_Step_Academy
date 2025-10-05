## Write a program that asks for a number "n" and prints numbers from "n" down to 1 using a while loop.

n = int(input("Enter a number: "))
while n > 0:
    print(n)
    n -= 1
print("Countdown finished!")