# Write a program to find left shift and right shift values of a given number.

x=int(input("Enter the number: "))
y=x>>2
z=x<<2
print("The number after right shift 2 is {0} and the number after left shift 2 is {1} ".format(y,z))