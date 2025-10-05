## Keep asking the user for numbers. Add them to a running total. Stop when the user enters zero. Print the total sum.

total = 0
while True:
    num = int(input("Enter a number (0 to stop):"))
    if num == 0:
        break
    total += num
print("Total sum of the numers entered:", total)
