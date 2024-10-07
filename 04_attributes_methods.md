### **4. Attributes and Methods in Python**

In Python’s Object-Oriented Programming (OOP), **attributes** and **methods** are key components of a class. They define the structure and behavior of objects.

- **Attributes** are variables that hold data about the object.
- **Methods** are functions defined within a class that describe the behaviors or actions the object can perform.

---

### **Attributes in Python**

Attributes represent the data or properties associated with an object. There are two types of attributes:
1. **Instance Attributes**: These are specific to each instance of a class.
2. **Class Attributes**: These are shared by all instances of the class.

---

#### **1. Instance Attributes**

Instance attributes are unique to each object created from a class. They are defined inside the `__init__` method using `self`, which refers to the specific instance of the class.

##### **Example:**
```python
class Person:
    def __init__(self, name, age):  # Instance attributes
        self.name = name
        self.age = age

# Creating two different objects with unique instance attributes
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name, person1.age)  # Output: Alice 30
print(person2.name, person2.age)  # Output: Bob 25
```
- Here, `name` and `age` are instance attributes. Each `Person` object can have different values for these attributes.

---

#### **2. Class Attributes**

Class attributes are shared among all instances of a class. They are defined outside the `__init__` method and inside the class itself. All objects of that class have access to the same class attributes.

##### **Example:**
```python
class Person:
    species = "Homo sapiens"  # Class attribute, shared by all instances

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing class attribute
print(person1.species)  # Output: Homo sapiens
print(person2.species)  # Output: Homo sapiens
```
- Both `person1` and `person2` share the `species` attribute because it is a class attribute.

---

### **Methods in Python**

**Methods** are functions that define the behaviors or actions that an object can perform. They are defined inside a class and typically operate on the object's attributes.

#### **Types of Methods**:
1. **Instance Methods**: Operate on instance attributes and require the `self` parameter.
2. **Class Methods**: Operate on class attributes and take `cls` as the first parameter.
3. **Static Methods**: Neither operate on instance nor class attributes. They behave like regular functions but belong to the class’s namespace.

---

#### **1. Instance Methods**

Instance methods work with an object’s instance attributes and typically use the `self` keyword to access or modify these attributes.
- **Purpose**:  They can access and modify the instance's attributes.

##### **Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):  # Instance method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
```
- The `greet` method is an instance method because it operates on the instance's `name` and `age` attributes.

---

#### **2. Class Methods**

Class methods operate on class attributes and are marked with the `@classmethod` decorator. They take `cls` as the first parameter, which refers to the class itself, not an instance.
- **Purpose**: They can access or modify class-level attributes, which are shared among all instances of the class.

##### **Example:**
```python
class Person:
    species = "Homo sapiens"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):  # Class method
        return cls.species

# Accessing class method
print(Person.get_species())  # Output: Homo sapiens
```
- The `get_species` method is a class method, and it returns the value of the class attribute `species`.

---

#### **3. Static Methods**

Static methods are defined using the `@staticmethod` decorator. They don’t operate on class or instance attributes and behave like regular functions but are included within the class. Static methods do not take `self` or `cls` as a parameter.
- **Purpose**: They do not access or modify class or instance attributes and are used for **utility functions** related to the class. 
    - **Utility Functions** : Utility functions are simple, often reusable functions designed to perform specific tasks or calculations. 
    - They typically do not depend on the state of an object (like instance methods) and can be used across different parts of a program or in different programs altogether.

##### **Example:**
```python
class Math:
    @staticmethod
    def add(a, b):  # Static method
        return a + b

# Accessing static method
print(Math.add(5, 10))  # Output: 15
```
- `add` is a static method because it does not depend on any instance or class attributes.

---

### **Instance Methods vs Class Methods vs Static Methods**

| **Feature**        | **Instance Method**          | **Class Method**             | **Static Method**                |
|--------------------|------------------------------|------------------------------|----------------------------------|
| Operates on        | Instance attributes (`self`)  | Class attributes (`cls`)      | No attributes                   |
| First Parameter    | `self`                       | `cls`                        | None                            |
| Access Instance Data | Yes                         | No                           | No                              |
| Access Class Data  | Yes                          | Yes                          | No                              |
| Use Cases          | Modify object’s state        | Access/modify class attributes| Utility functions related to class|

---

### **Accessing Attributes and Methods**

- **Attributes** and **methods** can be accessed using the dot (`.`) operator.

##### **Example:**
```python
class Person:
    species = "Homo sapiens"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def greet(self):  # Instance method
        return f"Hello, my name is {self.name}."

# Creating an object
person1 = Person("Alice", 30)

# Accessing instance attributes and methods
print(person1.name)        # Output: Alice
print(person1.greet())     # Output: Hello, my name is Alice.

# Accessing class attributes
print(person1.species)     # Output: Homo sapiens
```

---

### **Modifying Attributes and Methods**

- You can modify **instance attributes** for a specific object or **class attributes** that affect all instances.

##### **Modifying Instance Attributes**:
```python
person1.age = 31  # Modify the instance attribute 'age'
print(person1.age)  # Output: 31
```

##### **Modifying Class Attributes**:
```python
Person.species = "Homo neanderthalensis"  # Modify the class attribute
print(person1.species)  # Output: Homo neanderthalensis
```

---

### **Summary of Attributes and Methods**

- **Attributes** represent the data or state of an object, and they can be instance-specific or shared by all instances (class attributes).
- **Methods** define the behaviors or actions of an object, and they can be instance methods, class methods, or static methods.
- **Instance methods** work with instance-specific data, **class methods** work with class-level data, and **static methods** are independent of both.
  
---


### Next Step: Encapsulation