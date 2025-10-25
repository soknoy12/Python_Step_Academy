numbers = list(map(int, input("Enter Number: ").strip().split()))
# Ask the user for the number to count
value = int(input("Enter the number to count: "))

# Count how many times the value appears
count = numbers.count(value)

# Print the result
print(count)