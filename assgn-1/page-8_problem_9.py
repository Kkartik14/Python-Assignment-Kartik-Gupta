# Write a program to find sum of first n natural numbers.

n=int(input("Enter the maximum range"))
total=0
for number in range(1,n+1):
    print(number)
    total=total+number

print("The total is {0}".format(total))