
#TODO DFDF DFDF
# ! this is alert comment 
# ? this is question comment 
# * my note 

#this is about Lists in Python: use for compound data example: [apple, banana, orange, watermelon], # ! list usage are in ordered and changeable. Duplicate are ok.
# car_brand = ["BMW", "AUDI", "MERCESDES", "LEXUS"]
#print(len(car_brand))
#print("bmw" in car_brand)
#car_brand.append("TOYOTA")
#car_brand.remove("BMW")
#car_brand.insert(1, "TOYOTA")
#car_brand.clear
# print(car_brand.count("BMW"))
# print(car_brand)
# * set {"apple", "banana", "oragne"} usage : unordered immutable, but Add/Remove OK. No duplicate.
# * tuple ("apple", "banana", "orange") usage : ordered unchangeable. Good for constant datatype value.
#TODO exercise of lists
#ex1 make list and print 1st and last
def ex1():
    fruits = ["apple", "banana", "orange", "coconut", "strawberry"]
    print(fruits)
    print(fruits[0], fruits[4])

#ex2 
def ex2():
    numbers = [10, 20, 30, 40, 50]
    print(numbers[1])
    print(numbers[3:5])

#ex3
def ex3():
    colors = ["red", "blue", "green"]
    colors[1] = "yellow"
    colors.append("purple")
    colors.remove("red")
    print(colors)

#ex4
def ex4():
    names = ["alice", "bob", "charlie"]
    for name in names:
        print(name)

#ex5
def ex5():
    animals = ["dog", "cat", "bird", "fish"]
    print(len(animals))

#ex6
def ex6():
    numbers1 = [2, 4, 6, 8, 10]
    x = int(input("Enter a number: "))
    if x in numbers1:
         print("Yes")
    else:
          print("No")

#ex7 sum the items in the list
def ex7():
    numbers2 = [1, 2, 3, 4, 5, 6]
    total = 0
    for num in numbers2:
         total = total + num

    print(total)

#ex8 
def ex8():
    numbers3 = [3, 8, 2, 10, 5]
    largest = numbers3[0]
    for num in numbers3:
         if num > largest:
           largest = num

    print(largest)

#ex9 
def ex9():
    items = [1, 2, 3, 4, 5]
    items.reverse()
    print(items)

#ex10 print only even
def ex10():
    numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numbers4:
         if num % 2 == 0:
          print(num)

#ex11 find average of numbers
def ex11():
    numbers5 = [3, 7, 2, 9, 4]
    total = 0 
    for sum in numbers5:
        total = total + sum

    division = len(numbers5)
    average = total / division
    print(average)

#ex12
def ex12():
    numbers6 = [12, 5, 7, 20, 33, 8, 15]
    larger_than_10 = numbers6[0]
    for num in numbers6:
        if num >= larger_than_10 and num >= 10:
            print(num)

#ex13 find larger and smallest 
def ex13():
    numbers7 = [14, 3, 27, 8, 19, 5]
    largest = numbers7[0]
    smallest = numbers7[0]

    for num in numbers7:    
        if num > largest:
            largest = num
        if num < smallest:
             smallest = num

    print(f"Largest is {largest}\nSmallest is {smallest}")

if __name__ == "__main__":
    ex12()