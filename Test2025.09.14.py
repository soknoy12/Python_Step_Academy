#Write a program that prints the number frome 1 to 10.Done
# for i in range(1, 11):
#     print(i)

#Write a program that prints the multiplication table of 5 (frome 1x5 to 10x5).Done
# for i in range(1, 11):
#     result = i * 5
#     print(f"{i} × 5 = {result}")

# number = int(input("Enter a number : "))
# for i in range(1, 11):
#     result = i * number
#     print(f"{i} × {number} = {result}")

# number = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(i, "x", number, "=", i * number)
    
#Write a programe that finds the sum of all number from 1 to 100 
#(Hint: You will need a variable to keep track of the total while looping)
total = 0 

for number in range(1, 101):
    total += number 

print(f"The sum is: {total}")