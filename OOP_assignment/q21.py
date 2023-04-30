# Add constructor in the above class to initialize student details of n students and implement following methods:
# Display() student details
# Find Marks_percentage() of each student
# Display result() [Note: if marks in each subject >40% than Pass else Fail]
# Write a Function to find average of the class.

class Student:
    def __init__(self, n):
        self.students = []
        for i in range(n):
            name = input("Enter name: ")
            sap_id = input("Enter SAP ID: ")
            marks = []
            for subject in ["Physics", "Chemistry", "Mathematics"]:
                marks.append(int(input(f"Enter marks in {subject}: ")))
            student = {"name": name, "sap_id": sap_id, "marks": marks}
            self.students.append(student)

    def display(self):
        for student in self.students:
            print(f"Name: {student['name']}")
            print(f"SAP ID: {student['sap_id']}")
            print(f"Marks in Physics: {student['marks'][0]}")
            print(f"Marks in Chemistry: {student['marks'][1]}")
            print(f"Marks in Mathematics: {student['marks'][2]}")
            print()

    def marks_percentage(self):
        for student in self.students:
            total_marks = sum(student['marks'])
            percentage = total_marks / 3
            print(f"{student['name']} - Marks percentage: {percentage:.2f}%")

    def result(self):
        for student in self.students:
            if all(mark >= 40 for mark in student['marks']):
                print(f"{student['name']} - Pass")
            else:
                print(f"{student['name']} - Fail")

    def class_average(self):
        total_marks = sum(sum(student['marks']) for student in self.students)
        n_students = len(self.students)
        average = total_marks / (3 * n_students)
        print(f"Class average: {average:.2f}")


n = int(input("Enter the number of students: "))
students = Student(n)
print("Student Details:")
students.display()
print("Marks Percentage:")
students.marks_percentage()
print("Result:")
students.result()
students.class_average()
