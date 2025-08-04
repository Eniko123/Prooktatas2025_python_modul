"""
This function simulates a school system using object-oriented programming, modeling students, teachers, and class groups.
"""

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"This person is  {self.name} and {self.age} years old.")

class Teacher(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subject = None
        self.classroom = []
    def set_subject(self, subject):
        self.subject = subject
    def set_class(self, classroom):
        self.classroom.append(classroom)
    def introduction(self):
        print(f"The new teacher is {self.name}, and is {self.age} years old. "
              f"Subject of the new teacher {self.subject}.")
        for c in self.classroom:
            print(f"Classes of the teacher teaches: {c}")

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = []
        self.classroom = None

    def add_grades(self, grade):
        self.grades.append(grade)

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def set_class(self, classroom):
        self.classroom = classroom

    def introduction(self):
        print(f"The new student is {self.name}, and is {self.age} years old. "
              f"The student's average is {round (self.average(), 2)} and goes to class {self.classroom}.")


class Class(Human):
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self, student):
        self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def class_info(self):
        print(f"Class: {self.name}\n"
              f"The students in the class:")
        sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
        for student in sorted_students:
            print(f" - {student.name}, average: {round(student.average(), 2):}")
        for teacher in self.teachers:
            print("The teacher of the class:")
            print(f" - {teacher.name}, subject: {teacher.subject}")


class School:
    def __init__(self, name):
        self.name = name
        self.classrooms = []
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
    def school_info(self):
        print(f"School: {self.name}\n"
              f"The classes in the school:")
        for c in self.classrooms:
            print(f" - {c.name}")

"""
Task 4:
teacher1 = Teacher("Kovács János", 34)
teacher1.set_class("7a")
teacher1.set_subject("math")
teacher1.introduction()

student1 = Student("Kiss Anna", 13)
student1.add_grades(4)
student1.add_grades(5)
student1.add_grades(5)
student1.set_class("7a")
student1.introduction()

student2 = Student("Horváth Kata", 14)
student2.add_grades(2)
student2.add_grades(3)
student2.add_grades(2)
student2.set_class("7a")
student2.introduction()

student3 = Student("Virág Zoltán", 13)
student3.add_grades(5)
student3.add_grades(2)
student3.add_grades(3)
student3.set_class("7a")
student3.introduction()

classroom1 = Class("7a")
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)
classroom1.add_teacher(teacher1)
classroom1.class_info()

teacher2 = Teacher("Ormányosi Kelemen", 34)
teacher2.set_class("7b")
teacher2.set_subject("literature")
teacher2.introduction()

student4 = Student("Hollósi István", 13)
student4.add_grades(4)
student4.add_grades(4)
student4.add_grades(4)
student4.set_class("7b")
student4.introduction()

student5 = Student("Gálos Noémi", 13)
student5.add_grades(5)
student5.add_grades(5)
student5.add_grades(5)
student5.set_class("7b")
student5.introduction()

student6 = Student("Lovász Erika", 14)
student6.add_grades(3)
student6.add_grades(5)
student6.add_grades(5)
student6.set_class("7b")
student6.introduction()

classroom2 = Class("7b")
classroom2.add_student(student4)
classroom2.add_student(student5)
classroom2.add_student(student6)
classroom2.add_teacher(teacher2)
classroom2.class_info()

school = School("Fővárosi Általános Iskola")
school.add_classroom(classroom1)
school.add_classroom(classroom2)
school.school_info()
"""

def main():
    school = School("József Attila Elementary School")
    print("Welcome in the editing system of József Attila Elementary School")
    answer = input("What would you like to do next?\n"
                   "Press 1 to add new teacher to the system.\n"
                   "Press 2 to add new student to the system.\n"
                   "Press 3 to add new class to the system.\n"
                   "Press 4 to show school details.\n"
                   "Press end/quit/q to leave the program.\n"
                   "Your answer: ")
    while answer.lower() not in ["end", "quit", "q"]:
        if answer == "1":
            name_teacher = input("Name of the new teacher: ")
            age_teacher = int(input("Age of the new teacher: "))
            teacher = Teacher(name_teacher, age_teacher)

            teacher_class = input("Class the teacher teaches in: ")
            teacher.set_class(teacher_class)

            teacher_subject = input("Subject the teacher teaches: ")
            teacher.set_subject(teacher_subject)
            teacher.introduction()

            found = False
            for c in school.classrooms:
                if c.name == teacher_class:
                    c.add_teacher(teacher)
                    found = True
                    break

            if not found:
                print(f"Class {teacher_class} not found. Creating new class.")
                new_class = Class(teacher_class)
                new_class.add_teacher(teacher)
                school.add_classroom(new_class)

            print("Teacher added successfully:")
            teacher.introduction()

        elif answer == "2":
            name_student = input("Name of the new student: ")
            age_student = int(input("Age of the new student: "))
            student = Student(name_student, age_student)

            student_class = input("Class the student goes to: ")
            student.set_class(student_class)

            student_grades = []
            print("Enter grades one by one. Press Enter to finish.")
            while True:
                grade = input("Grade: ")
                if grade == "":
                    break
                try:
                    student.add_grades(int(grade))
                except ValueError:
                    print("Please enter a valid number.")

            found = False
            for c in school.classrooms:
                if c.name == student_class:
                    c.add_student(student)
                    found = True
                    break

            if not found:
                print(f"Class {student_class} not found. Creating new class.")
                new_class = Class(student_class)
                new_class.add_student(student)
                school.add_classroom(new_class)

            print("Student added successfully:")
            student.introduction()

        elif answer == "3":
            new_class = input("Enter here the class you would like to create: ")
            found = False
            for c in school.classrooms:
                if c.name == new_class:
                    found = True
                    break

            if not found:
                print(f"Class {new_class} not found. Creating new class.")
                new_class = Class(new_class)
                school.add_classroom(new_class)

            print("Class added successfully:")
            new_class.class_info()

        elif answer == "4":
            school.school_info()

        answer = input("What would you like to do next?\n"
                       "Press 1 to add new teacher to the system.\n"
                       "Press 2 to add new student to the system.\n"
                       "Press 3 to add new class to the system.\n"
                       "Press 4 to show school details.\n"
                       "Press end/quit/q to leave the program.\n"
                       "Your answer: ")