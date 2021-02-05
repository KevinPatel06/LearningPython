class Student:

    def __init__(self, name, age, gender, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def __str__(self):
        return self.name + " " + str(self.age)