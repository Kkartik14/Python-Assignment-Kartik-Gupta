# Using membership operator find whether a given character is in a string.

str = input("Enter a string: ")
char = input("Enter a character: ")

if char in str:
    print(char, "is in the string.")
else:
    print(char, "is not in the string.")