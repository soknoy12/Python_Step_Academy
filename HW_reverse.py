# Ask the user to enter a number
number = int(input("Enter a number: "))

# Keep going until the number becomes a palindrome
while True:
    # Reverse the number using math
    temp = number
    reversed_number = 0
    
    while temp > 0:
        digit = temp % 10           # Get the last digit
        reversed_number = reversed_number * 10 + digit  # Add it to reversed number
        temp = temp // 10            # Remove the last digit
    
    # Check if the number is a palindrome
    if number == reversed_number:
        break  # Stop if it's a palindrome
    
    # Add the reversed number to the original number
    new_number = number + reversed_number
    print(f"{number} + {reversed_number} = {new_number}")
    
    # Update the number for the next loop
    number = new_number

# Print the final palindrome
print(f"The palindrome is {number}")