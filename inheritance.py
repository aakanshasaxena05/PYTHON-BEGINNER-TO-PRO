# ==========================================
#       INHERITANCE IN PYTHON
# ==========================================

# Parent class
class Person:

    # Constructor of parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Parent class method
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class
# Student inherits from Person
class Student(Person):

    # Constructor of child class
    def __init__(self, name, age, marks):

        # Calling parent class constructor
        super().__init__(name, age)

        # Student's own property
        self.marks = marks

    # Child class method
    def display_student(self):
        print("Marks:", self.marks)


# Creating object of Student
s1 = Student("Aakansha", 22, 85)


# Calling parent class method
s1.display_person()

# Calling child class method
s1.display_student()