# Create a class for operator overloading which adds two Point Objects where Point has x & y values
# e.g. if
# P1(x=10,y=20)
# P2(x=12,y=15)
# P3=P1+P2 => P3(x=22,y=35)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(10, 20)
p2 = Point(12, 15)
p3 = p1 + p2
print(p3.x, p3.y)  
