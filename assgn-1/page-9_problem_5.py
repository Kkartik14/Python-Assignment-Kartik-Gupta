# Check whether the quadratic equation has real roots or imaginary roots. Display the roots.

import cmath

print("ax^2+bx+c=0 is how a quadratic equation looks like\n")
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))
d = (b**2) - (4*a*c)
if d >= 0:
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    print("The roots are: {0} and {1}".format(root1, root2))
else:
    print("The quadratic equation has imaginary roots")
