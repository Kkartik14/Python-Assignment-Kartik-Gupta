# Declare three variables, consisting of your first name, your last name and Nickname. Write a  program that prints out your first name, then your nickname in parenthesis and then your last name.  Example output : George ( woody ) Washington.

a=input("Enter your first name: ")
b=input("Enter your last name: ")
c=input("Enter your Nickname")
print("your first name{0}, then your nickname in parenthesis{1} , then your last name{2} and together is {0}({1}){2}".format(a,c,b))