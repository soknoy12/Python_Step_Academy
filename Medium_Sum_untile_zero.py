#Enter number: 5
#Enter number: 3
#Enter number: 2
#Enter number: 0
#Total = 10 


total = 0 
while True:
    number = int(input("Enter number: "))
    if number == 0:
        break 
    total += number
print("Total", total)
