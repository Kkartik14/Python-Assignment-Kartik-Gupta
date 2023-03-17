#WAP to calculate distance between two points. 

print("Input the variables")
x1=float(input("Enter value of x1"))
x2=float(input("Enter value of x2"))
y1=float(input("Enter value of y1"))
y2=float(input("Enter value of y2"))
dx = x2 - x1
dy = y2 - y1
dist = ((dx**2 + dy**2)**0.5)
print("The distance is {0}".format(dist))

