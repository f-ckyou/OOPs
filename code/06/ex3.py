class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def enroll(self, course):
        print(f"{self.name} enrolled in {course}")

class Teacher(Person):
    def assign(self, course):
        print(f"{self.name} assigned homework for {course}")


student = Student("Zoro", 19)
teacher = Teacher("Amit", 50)

student.enroll("OOPS")        
teacher.assign("OOPS") 