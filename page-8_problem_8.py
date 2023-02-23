#Write a program to swap two numbers without taking additional variable.

x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
print("before swapping the numbers are {0} and {1}".format(x,y))
x=x*y
y=int(x/y)
x=int(x/y)
print("after swapping the numbers are {0} and {1}".format(x,y))
