# Get user input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Keep only numbers that appear exactly once
unique = [num for num in numbers if numbers.count(num) == 1]

"""unique = []
for num in numbers:
    c = numbers.count(num)   # how many times num appears in the whole list
    if c == 1:
        unique.append(num)"""

print("Unique elements:", unique)