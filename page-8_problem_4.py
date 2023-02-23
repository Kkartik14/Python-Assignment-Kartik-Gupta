# Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem. 

import math
a=float(input("enter base of the triangle"))
b=float(input("enter height of the triangel"))
c=math.sqrt(a**2 + b**2)
print("The hypotunese is : {0}".format(c))