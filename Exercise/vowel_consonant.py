sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for ch in sentence:
    if ch.isalpha():  # check if it's a letter
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


"""text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)"""