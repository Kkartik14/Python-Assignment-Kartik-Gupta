class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks in Physics: {self.marks[0]}")
        print(f"Marks in Chemistry: {self.marks[1]}")
        print(f"Marks in Mathematics: {self.marks[2]}")

students = []
for i in range(3):
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    marks = []
    for subject in ["Physics", "Chemistry", "Mathematics"]:
        marks.append(int(input(f"Enter marks in {subject}: ")))
    student = Student(name, sap_id, marks)
    students.append(student)
for student in students:
    student.display_details()
    print()
