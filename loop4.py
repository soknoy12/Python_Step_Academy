start_num = int(input("Enter Start Number : "))
end_num = int(input("Enter End Number : "))
for even_num in range(start_num,end_num):
    if (even_num % 2 == 0) :
        print(even_num)
