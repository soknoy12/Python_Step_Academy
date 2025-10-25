word = input("Enter a word: ")

# make lowercase so 'Madam' and 'madam' are the same
word = word.lower()

# check if the word is the same backward
if word == word[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")