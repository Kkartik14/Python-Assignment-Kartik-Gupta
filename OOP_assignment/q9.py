# WAP to add variables to a class at run-time.

class person:
    def __init__(self, name):
        self.name = name

obj= person("kartik")
setattr(person, "age", 18)
setattr(obj, "gender", "Male")
print(person.age)
print(obj.gender)
