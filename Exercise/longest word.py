# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Assume the first word is the longest
longest_word = words[0]

# Check each word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Print the longest word
print("The longest word is:", longest_word)