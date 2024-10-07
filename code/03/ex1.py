
# default constructors
class Dog:
    def __init__(self):  # Default constructor
        self.name = "Unknown"  # Default value
        self.age = 0           # Default value

    def info(self):
        return f"Dog's name is {self.name} and it is {self.age} years old."

# Creating an object using the default constructor
my_dog = Dog()
print(my_dog.info())  # Output: Dog's name is Unknown and it is 0 years old.



# parameterized constructor
class Dog:
    def __init__(self, name, age):  # Parameterized constructor
        self.name = name
        self.age = age

    def info(self):
        return f"Dog's name is {self.name} and it is {self.age} years old."

# Creating an object with parameters
my_dog = Dog("Buddy", 3)
print(my_dog.info())  # Output: Dog's name is Buddy and it is 3 years old.