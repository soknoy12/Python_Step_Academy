# List of numbers
"""numbers = [1, 2, 3, 4, 5]

# Calculate the sum using sum() function
total = sum(numbers)

# Print the result
print("The sum of all elements is:", total)"""


user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers

numbers = list(map(int, user_input.strip().split()))

# Calculate the sum using sum()
total = sum(numbers)

# Print the result
print("The sum of all elements is:", total)
