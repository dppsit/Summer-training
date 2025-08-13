


class Student:
    def __init__(self, name, age, course):  # ✅ Proper spacing & colon
        self.name = name
        self.age = age
        self.course = course

# Creating multiple student objects
s1 = Student("Rohan", 17, "mern")
s2 = Student("Raman", 20, "mern")
s3 = Student("Riya", 67, "mern")
s4 = Student("Rishab", 47, "mern")

# Printing details of one student
print(s1)               # Shows memory address unless __str__ is defined
print(s1.name)          # ✅ Access name
print(s1.course)        # ✅ Access course
print(s1.age)           # ✅ Access age
