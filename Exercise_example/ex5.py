# EX1:
# n = int(input('enter n: '))

# while n <= 1:
#     print(n)

# EX2:
# num1 = 0
# num = int(input('enter number'))
# while num != 0 :
#     print('enter number', num)
#     num = int(input('enter number'))
#     num1 += num


# print("the sum is : ",(num1))

#EX3
num = 0
count = 0
while num != 34:
    num = int(input("Enter number: "))
    count += 1
    if num < 34 :
        print("too low")
    elif num > 34:
        print("too high")
    else:
        print("Correct")

print(f"correct! you guessed it in {count} tries")


        




    