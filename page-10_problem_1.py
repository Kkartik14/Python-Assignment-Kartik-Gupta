#Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
#CGPA=percentage/10
# CGPA range:
# 0 to 3.4 -> F
# 3.5 to 5.0->C+
# 5.1 to 6->B
# 6.1 to 7-> B+
# 7.1 to 8-> A
# 8.1 to 9->A+
# 9.1 to 10-> O (Outstanding)

name=input("Enter your name:")
roll=input("Enter roll number:")
sem=int(input("Enter your sem[1-8]:"))
sap=int(input("Enter your SAP ID:"))
crs=input("Enter your full course name: ")
print("Name: {0} , Roll number {1} , Semester {2} , SAPID {3} , Course {4} ".format(name,roll,sem,sap,crs))
subject1 = float(input("Enter the marks of subject 1: "))
subject2 = float(input("Enter the marks of subject 2: "))
subject3 = float(input("Enter the marks of subject 3: "))
subject4 = float(input("Enter the marks of subject 4: "))
subject5 = float(input("Enter the marks of subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100
print("The percentage is {0}".format(percentage))
cgpa = percentage / 10
print("The CGPA is {0}".format(cgpa))

if cgpa < 3.5:
    print("Grade: F")
elif cgpa < 5.1:
    print("Grade: C+")
elif cgpa < 6.1:
    print("Grade: B")
elif cgpa < 7.1:
    print("Grade: B+")
elif cgpa < 8.1:
    print("Grade: A")
elif cgpa < 9.1:
    print("Grade: A+")
else:
    print("Grade: O (Outstanding)")