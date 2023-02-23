# Find whether the given number is Armstrong number.

num = input("Enter a number: ")
order = len(num)
sum = 0
for i in num:
    sum += int(i) ** order
if sum == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
