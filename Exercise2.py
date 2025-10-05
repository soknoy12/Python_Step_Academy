#Multiplication Table (Mudium)
#Write the program that print the multiplication table of 5 (From 1x5 up to 10X5)

multiplication = int(input("Enter multiplication of: "))
for idx in range(1, 11):
    result = multiplication * idx
    print(f"{idx} x {multiplication} = {result}")

#Let user enter their favorite number

