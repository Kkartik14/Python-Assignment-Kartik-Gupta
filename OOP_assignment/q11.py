# WAP with class Employee that keeps a track of the number of employees in an organization and also store their name, designation, and salary details.

class Employee:
    num_employees = 0  
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.num_employees += 1
employee1 = Employee("kartik", "engineer", 100000)
employee2 = Employee("john", "manager", 75000)
employee3 = Employee("shyam", "Assistant", 50000)

print("Number of employees:", Employee.num_employees)
print("Employee 1:", employee1.name, employee1.designation, employee1.salary)
print("Employee 2:", employee2.name, employee2.designation, employee2.salary)
print("Employee 3:", employee3.name, employee3.designation, employee3.salary)
