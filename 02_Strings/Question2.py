# Write a Python program that takes a string as input and prints the number of vowels and consonants in it.

word = str(input("Enter the String: ").lower())

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in word:
    if char.isalpha():  
        # check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("consonant:", consonant_count)