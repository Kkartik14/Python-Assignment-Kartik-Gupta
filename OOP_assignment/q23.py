# Create a class to implement method Overriding.

class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  
dog.make_sound() 
cat.make_sound() 
