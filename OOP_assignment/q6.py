# WAP to illustrate the use of a private method.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add(self):
        return self.num1 + self.num2

    def __subtract(self):
        return self.num1 - self.num2

    def calculate(self, operator):
        if operator == '+':
            return self.__add()
        if operator == '-':
            return self.__subtract()
calc = Calculator(5, 3)
print(calc.calculate('+'))  
print(calc.calculate('-'))  
