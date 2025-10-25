# Get user input
list1 = list(map(int, input("Enter first list numbers separated by space: ").split()))
list2 = list(map(int, input("Enter second list numbers separated by space: ").split()))

# Find common elements using list comprehension
common = [num for num in list1 if num in list2]

"""common = []
for num in list1:
    if num in list2:
        common.append(num)"""


print("Common elements:", common)