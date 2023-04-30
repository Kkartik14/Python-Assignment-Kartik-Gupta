# WAP that has a class person storing name and DOB of a person. The program should subtract the DOB from today’s date to find out whether a person is eligible to vote or not. 

from datetime import datetime

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    def is_eligible_to_vote(self):
        today = datetime.now()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        if age >= 18:
            return True
        else:
            return False
person1 = Person("kartik", datetime(2004, 7, 14))
if person1.is_eligible_to_vote():
    print(person1.name, "is eligible to vote")
else:
    print(person1.name, "is not eligible to vote")
