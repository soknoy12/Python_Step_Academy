#Write a program that asks the user for a starting number and an ending number.
#Print only the even numbers in that range.

#input: 1, 100
#output: 
#2
#4
#6
#....
#100

# Print even numbers in a given range

# Get input from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop through the range
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
        


