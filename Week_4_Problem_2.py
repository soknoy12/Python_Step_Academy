#How to guess number
secret = 33
num = 0

while num != secret:
    num = int(input("Gest the number"))
    if num < secret:
        print("It is too low")
    elif num > secret:
        print("It is too high")
    else:
        print("WoW, you are correct")
        print("The secret number is ", secret)



