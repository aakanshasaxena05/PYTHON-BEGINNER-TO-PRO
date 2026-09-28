class Student:

    # Constructor
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

        print("Constructor is called")
        print("Object is created")

    # Normal method
    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    # Destructor
    def __del__(self):
        print("\nDestructor is called")
        print("Object is destroyed")


# Creating object
s1 = Student("Aakansha", 22, 85)

# Calling method
s1.display()

# Accessing object attributes
print("\nAccessing Data:")
print(s1.name)
print(s1.age)
print(s1.marks)

# Deleting object
del s1