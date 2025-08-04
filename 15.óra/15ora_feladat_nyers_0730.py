import random
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"This person is  {self.name} and {self.age} years old")

class Teacher(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        subjects = ["biology", "math", "literature", "PE", "French", "Music"]
        self.subject = random.choice(subjects)

    def assign_class(self):
        classes = ["1a", "2a", "3a", "4a", "1b", "2b", "3b", "4b"]
        self.classroom = random.choice(classes)

    def introduction(self):
        print(f"This person is {self.name}, and he/she is {self.age} years old. "
              f"He/She teach {self.subject} to class {self.classroom}.")

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = []
    def add_grades(self, grade):
        self.grades.append(grade)
    def average(self):
        self.average = sum(self.grades)/len(self.grades)
    def set_class(self):
        classes = ["1a", "2a", "3a", "4a", "1b", "2b", "3b", "4b"]
        self.classroom = random.choice(classes)
    def introduction(self):
        print(f"This person is {self.name}, and he/she is {self.age} years old. "
              f"The student's average is {self.average()} and he/she goes to class {self.classroom}.")


class Class(Human):
    def add_student(self):
        pass
    def add_teacher(self):
        pass
    def class_info(self):
        pass
