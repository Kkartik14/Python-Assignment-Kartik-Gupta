# Check whether given number is divisible by 3 and 5 both.

n=int(input("enter your number: "))
if(n%3==0 and n%5==0):
    print("the number {} is divisble by 3 & 5".format(n))
else:
    print("the number is not divisible by 3 & 5")