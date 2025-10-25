number = int(input("Enter Number : "))
# Keep going until the number becomes a palindrome
while True:
    # Convert number to string and reverse it
    reversed_number = int(str(number)[::-1])
    
    # Check if the number is a palindrome
    if number == reversed_number:
        break  # Stop the loop if it's a palindrome
    
    # Add the reversed number to the original number
    new_number = number + reversed_number
    
    # Show the calculation
    print(f"{number} + {reversed_number} = {new_number}")
    
    # Update the number for the next loop
    number = new_number

# Print the final palindrome
print(f"The palindrome is {number}")