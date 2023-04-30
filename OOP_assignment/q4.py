# WAP to modifying a mutable type attribute.

class Car:
    def __init__(self, brand, model, colours):
        self.brand = brand
        self.model = model
        self.colours = colours

    def add_colour(self, colour):
        self.colours.append(colour)
car1 = Car('Toyota', 'Camry', ['white', 'black'])
print(car1.colours)  
car1.add_colour('red')
print(car1.colours)  
