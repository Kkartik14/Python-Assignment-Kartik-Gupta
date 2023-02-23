# Write a program to find area of triangle when length of sides are given.

import math
a=float(input("enter the value of 1st side: "))
b=float(input("Enter the value of 2nd side: "))
c=float(input("Enter the value of 3rd side: "))
s=((a+b+c)/2)
print("the semi-perimeter is {}".format(s))
area=math.sqrt(s(s-a)(s-b)(s-c))
print("the area of the triangle with sides{0}{1}{2} is : {3}".format(1,b,c,area))