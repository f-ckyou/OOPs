class Dog:
    def __init__(self, name, age):
        self.name = name  # Here, self.name is an instance attribute
        self.age = age    # Here, self.age is also an instance attribute

    def bark(self):
        return f"{self.name} says Woof!"  # Accessing the instance attribute self.name

    def get_age(self):
        return f"{self.name} is {self.age} years old."  # Accessing self.name and self.age

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing methods
print(my_dog.bark())         # Output: Buddy says Woof!
print(my_dog.get_age())      # Output: Buddy is 3 years old.
