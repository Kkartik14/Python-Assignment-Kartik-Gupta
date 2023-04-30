# WAP that has a class fraction with attributes numerator and denominator. Enter the values of the attributes and print the fraction in simplified from.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def simplify(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            t = b
            b = a % b
            a = t
        gcd = a
        numerator = self.numerator // gcd
        denominator = self.denominator // gcd
        print(f"{numerator}/{denominator}")

fraction = Fraction(24, 36)
fraction.simplify() 
