#write a program that prints the multiplication table of 5 (from 1x5 up to 10x5)
mul = int(input("Enter multification number of :"))
for index in range(1,11): 
    result = mul * index 
    print(f"{index} x {mul} = {result}")
    # f inside print is for print value in string 