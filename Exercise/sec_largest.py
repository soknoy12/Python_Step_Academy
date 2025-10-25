# Get list input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize two variables
largest = second_largest = float('-inf')

# Find largest and second largest
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number is:", second_largest)