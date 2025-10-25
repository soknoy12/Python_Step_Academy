user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers

numbers = list(map(int, user_input.strip().split()))
# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Print the results
print("Largest number:", largest)
print("Smallest number:", smallest)



numbers = list(map(int, input("Enter Number").strip().split()))
