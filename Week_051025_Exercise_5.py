#Medium-Sum until zero
#keep asking the user for numbers.Add them to a runnign total. Stop when ther user enters 0 .print the total sum.
# Medium - Sum until Zero

total = 0  # running total

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break  # exit the loop
    
    total += num  # add number to total

print("Total sum =", total)
