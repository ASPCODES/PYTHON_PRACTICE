# Q1.
# Take a string input from the user and print:

# The first and last character

# The total number of characters

# The string reversed


text = str(input("Enter the Strings: "))

print(text[0])
print(text[-1])
print(len(text))

reversed_text = text[::-1]

print(reversed_text)