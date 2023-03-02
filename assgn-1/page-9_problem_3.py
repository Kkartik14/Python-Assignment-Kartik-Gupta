# Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.

a=int(input("Enter the value of 1st number: "))
b=int(input("Enter the value of 2nd number: "))
if(a==b):
    print("numbers are equal")
else:
    max=(a if a > b else b)
    print("The greater number among the both is : {} ".format(min))