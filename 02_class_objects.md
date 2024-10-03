### **2. Classes and Objects in Python**


---

#### **What is a Class?**

- A **class** is a blueprint for creating objects. 
- It defines a set of attributes (data) and methods (functions) that characterize any object of the class. 
- In Python, classes are created using the `class` keyword.

##### **Syntax:**
```python
class ClassName:
    # Class attributes and methods
```

##### **Example:**
```python
class Dog:
    # Class attributes
    species = "Canis familiaris"  # Shared by all instances

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method
    def bark(self):
        return f"{self.name} says woof!"
```

---

#### **What is an Object?**

- An **object** is an instance of a class. 
- When a class is defined, no memory is allocated until an object of that class is created. 
- Each object can have different attribute values, even though they share the same class structure.

##### **Creating an Object:**
To create an object, you simply call the class as if it were a function.

##### **Example:**
```python
my_dog = Dog("Buddy", 3)  # Create an object of Dog class
print(my_dog.bark())      # Output: Buddy says woof!
```

---

### **Class Attributes vs Instance Attributes**

- **Class Attributes**:
  - Shared across all instances of the class.
  - Defined within the class but outside any methods.
  
  Example:
  ```python
  class Dog:
      species = "Canis familiaris"  # Class attribute
  ```

- **Instance Attributes**:
  - Specific to each instance of the class.
  - Defined in the `__init__` method (the constructor) using `self`.

  Example:
  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name  # Instance attribute
          self.age = age    # Instance attribute
  ```

### **The `self` Keyword**

- `self` refers to the instance of the class and allows access to the attributes and methods of the class in Python.
- It must be the first parameter of any function in the class, although it is not explicitly passed when you call the method on an object.

##### **Example:**
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says woof!
```

---

### **Creating Methods in a Class**

- Methods are functions defined within a class that can operate on instance attributes. 
- They define the behavior of the objects created from the class.

##### **Example:**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 3)
print(my_dog.bark())      # Output: Buddy says woof!
print(my_dog.get_age())   # Output: Buddy is 3 years old.
```

---

### **Summary of Classes and Objects**

- A **class** is a blueprint for creating objects, containing attributes and methods.
- An **object** is an instance of a class, created using the class name.
- **Class attributes** are shared across all instances, while **instance attributes** are unique to each object.
- The `self` keyword allows access to instance attributes and methods within a class.
- Methods define the behavior of the class and can operate on instance attributes.

### Next Steps
With a solid understanding of classes and objects, you can now explore **Constructors** in Python, which are essential for initializing objects when they are created.