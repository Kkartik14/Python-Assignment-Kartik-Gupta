# WAP that uses class to store the name and marks of students. Use list to store the marks in the three subjects.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
students = []
students.append(Student("kartik", [85, 90, 92]))
students.append(Student("kartik1", [78, 80, 82]))
students.append(Student("kartik2", [92, 95, 88]))

for student in students:
    print("Name:", student.name)
    print("Marks:", student.marks)
