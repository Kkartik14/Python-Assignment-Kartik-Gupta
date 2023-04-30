# Write a class that store a string and all its status details such as number of uppercase character, vowel, consonants, spaces, etc.

class StringStats:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.num_uppercase = sum(1 for c in string if c.isupper())
        self.num_vowels = sum(1 for c in string if c.lower() in 'aeiou')
        self.num_consonants = sum(1 for c in string if c.isalpha() and c.lower() not in 'aeiou')
        self.num_spaces = sum(1 for c in string if c.isspace())

    def __str__(self):
        return (f"String: {self.string}\n"
                f"Length: {self.length}\n"
                f"Number of uppercase characters: {self.num_uppercase}\n"
                f"Number of vowels: {self.num_vowels}\n"
                f"Number of consonants: {self.num_consonants}\n"
                f"Number of spaces: {self.num_spaces}")

my_string = StringStats("Hello, World!")
print(my_string)
