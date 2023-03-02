# Find the greatest among three numbers assuming no two values are same. 

a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a>b and a>c):
    print("The greatest number is : {}".format(a))
elif(b>a and b>c):
    print("The greatest number is : {}".format(b))
else:
    print("The greatest number is : {}".format(c))