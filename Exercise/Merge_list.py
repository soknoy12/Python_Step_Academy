# Example lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine the two lists
merged_list = list1 + list2

# Display the result
print(merged_list)

print("="*30)

# Get input from the user
input1 = input("Enter the first list (numbers separated by spaces): ")
input2 = input("Enter the second list (numbers separated by spaces): ")


# Convert the input string into a list of numbers

list1 = list(map(int, input1.strip().split()))
list2 = list(map(int, input2.strip().split()))
# Combine the two lists
merged_list = list1 + list2

# Display the result
print("Merged list:", merged_list)