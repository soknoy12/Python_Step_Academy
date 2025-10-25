numbers = list(map(int, input("Enter Number: ").strip().split()))
# Remove duplicates by converting the list to a set, then back to a list
unique_numbers = list(set(numbers))

# Print the unique list
print("List with duplicates removed:", unique_numbers)