# WAP a class Rectangle that has attributes length and breath and a method area which returns the area of the rectangle. 

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

rectangle = Rectangle(5, 10)
area = rectangle.area()
print(area) 
