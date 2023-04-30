# WAP to differentiate between class variable and object variables

class newclass:
    def __init__(self, x):
        self.y= x
obj1 = newclass(10)
print(obj1.y)
obj1.y = 20
print(obj1.y)
