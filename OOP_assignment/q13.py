# WAP that has a class Circle. Use a class variable to define the value of constant PI. Use this class variable to calculate area and circumference of a circle with specified radius. 

class Circle:
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
    
    def circumference(self):
        return 2 * Circle.PI * self.radius

circle = Circle(5)
area = circle.area()
circumference = circle.circumference()
print(area) 
print(circumference) 
