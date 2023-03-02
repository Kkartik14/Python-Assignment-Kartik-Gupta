# WAP to print the prime factor of a number.

n=int(input("Enter your prime number"))
while n % 2 == 0:
    print(2),
    n = n / 2
for i in range(3,int(n**0.5)+1,2):
    while n % i == 0:
        print(i),
        n = n / i
if n > 2:
    print("The prime factors of n is : ",n)