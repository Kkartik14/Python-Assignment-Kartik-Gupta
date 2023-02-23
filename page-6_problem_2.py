# WAP to print the sum of all the odd numbers from 1 to 100. 

total=0
x=int(input("enter maximum number"))
for number in range(1,x+1):
    if (number%2!=0):
       print("{}".format(number))
       total=total+number

print("the sum of numbers in range {0} is : {1}".format(x,total))
    