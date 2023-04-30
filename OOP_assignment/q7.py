# WAP to call a class method from another method of the same class.

class MyClass:
    def method1(self):
        print("This is method 1")
        self.method2()

    def method2(self):
        print("This is method 2")

my_object = MyClass()
my_object.method1()
