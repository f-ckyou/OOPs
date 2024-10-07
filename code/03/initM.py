
# example 1
class Dog:
    def __init__(self, name, breed):
        self.name = name   # Instance variable for the dog's name
        self.breed = breed # Instance variable for the dog's breed

    def describe(self):
        return f"My dog's name is {self.name} and it is a {self.breed}."

# Creating an instance of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Accessing method
print(dog1.describe())  # Output: My dog's name is Buddy and it is a Golden Retriever.



# example 2
class Car:
    def __init__(self, make, model, year=2020):
        self.make = make    # Instance variable for car make
        self.model = model  # Instance variable for car model
        self.year = year    # Instance variable for car year with a default value of 2020

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an instance of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic", 2022)

# Accessing methods
print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2022 Honda Civic




# example 3 (little complex)
class BankAccount:
    def __init__(self, owner, balance=0):
        # instance variables
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. Current Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough balance!"
        else:
            self.balance -= amount
            return f"${amount} withdrawn. Current Balance: ${self.balance}"

# creating object of class BankAccount
account1 = BankAccount("Zoro", 100)

# Accessing methods
print(account1.deposit(20))
print(account1.withdraw(150))
print(account1.withdraw(70))



# example 4 (initializatin with conditional logic)
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect1 = Rectangle(10, 5)
print(f"Area of rect1: {rect1.area()}")

try:
    rect2 = Rectangle(-5, 3)
except ValueError as e:
    print(e)  # Output: Width and height must be positive values.
    # this will print the value error statement



# example 5 (initialization with lists or other data structures)
class Classroom:
    def __init__(self, teacher_name, students=None):
        self.teacher_name = teacher_name # initialize the teacher's name
        # if no students are provided, create an empty list
        self.students = students if students is not None else []

    def add_student(self, student_name):
        self.students.append(student_name)
        return f"{student_name} added to the class"

    def list_students(self):
        return f"Students in {self.teacher_name}'s class: {', '.join(self.students)}"

# creating objects
class1 = Classroom("Majanua")
class2 = Classroom("Priyanka")
# adding studetns
print(class1.add_student("Zoro"))
print(class1.add_student("Langra"))
print(class2.add_student("Pal"))
print(class2.add_student("Dealer"))
# listing students
print(class1.list_students())
print(class2.list_students())

