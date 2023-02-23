# Check whether given number is palindrome or not.

num = int(input("Enter a number: "))
rev_num = str(num)[::-1]
if str(num) == rev_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")