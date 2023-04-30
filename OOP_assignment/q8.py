# WAP to show how a class method calls a function defined in the global namespace.

def global_function():
    print("This is a function in the global namespace.")

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        global_function()

MyClass.class_method()
