# Create programs to implement different types of inheritances.

class Animal:
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")

# Single inheritance
class dog(Animal):
    def bark(self):
        print("I bark bhau")

# Multi-level inheritance
class cat(dog):
    def meow(self):
        print("I meow")

class goat(cat):
    def burp(self):
        print("I burp")

class pet:
    def eat_1(self):
        print("I don't eat")
    def eat_2(self):
        print("i might eat")

# multiple inhertiance
class me(goat,pet):
    def eat_3(self):
        print("heheh")