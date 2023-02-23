# Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))
def addition():
    print("value after addition is: {}".format(x+y+z))
def substract():
    print("value after performing substraction is : {}".format((x-y)-z))
def multi():
    print("value after multiplication is : {}".format((x*y)*z))
def div():
    print("Value after division is : {}".format((x/y)/z))

print("your results are : {}{}{}{}".format(addition(),substract(),multi(),div()))
