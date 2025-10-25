"""# Take input from the user
text = input("Enter a string: ")

# Reverse the string using slicing
reversed_text = text[::-1]

# Display the reversed string
print("Reversed string:", reversed_text)"""

text = input("Enter a string: ")

reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text   # add each character to the front

print("Reversed string:", reversed_text)

