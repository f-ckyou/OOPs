# Q. How can encapsulation be used to restrict direct access to class attributes?

class Person:
    def __init__(self, name, age):
        # private attributes using double underscores
        self.__name = name
        self.__age = age

    # public method to access private attributes
    def get_name(self): # alt: use @property
        return self.__name

    # public method to set private attributes
    def set_name(self, name): # alt: use @name.setter
        self.__name = name

# create object
person = Person("Zoro", 19)

# Access the private attribute using the public method
print(person.get_name())  # Output: Alice

# Trying to access private attribute directly will cause an error
# print(person.__name)  # AttributeError

# Modify private attribute using setter method
person.set_name("Number 1")
print(person.get_name())  
