# for number in range(1,100):
#     if number % 5 != 0:
#         print(number)
#     if number % 7 == 0:
#         print("BOOM!")

# number = 1
# while number <= 100 :
#     if number % 5 != 0:
#         print(number)
#     number += 1
#     if number % 7 == 0:
#         print("BOOM!")
#EX
# n = int(input("Enter a number: "))

# for num in range(2, n + 1):  
#     for i in range(2, num):   
#         if num % i == 0:
#             break           
#     else:
#         print(num)     
# 
# EX
# 

num = int(input("Enter a number: "))

while True:
    reversed_num = int(str(num)[::-1])
    print(f"{num} + {reversed_num} = {num + reversed_num}")
    num = num + reversed_num

    if str(num) == str(num)[::-1]:
        print(f"Palindrome reached: {num}")
        break


        

                  



