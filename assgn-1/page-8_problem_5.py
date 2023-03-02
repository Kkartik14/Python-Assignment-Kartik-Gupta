# Write a program to find simple interest.

amt=int(input("Enter Number Amount: "))
rate=float(input("Enter Number Rate: "))
time=float(input("Enter Number Time:"))

interest=float((amt*rate*time)/100)
print("The simple intrest calculated upon the given amount {0}, rate charged {1} and time {2} is : {3}".format(amt,rate,time,interest))