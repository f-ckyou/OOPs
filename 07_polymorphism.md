### **7. Polymorphism in Python**

- **Polymorphism** in OOP allows objects of different classes to be treated as objects of a common superclass. 
- It means "many forms," and in Python, it allows methods with the same name in different classes to have different implementations. 
- This concept provides flexibility in coding by enabling one interface to control access to a range of different types of objects.

Polymorphism is a powerful feature that helps in achieving clean and maintainable code.

---

### **Types of Polymorphism**

1. **Compile-Time Polymorphism (Method Overloading)**:
   - Python doesn't support traditional method overloading like some other languages (e.g., Java or C++). However, you can use default arguments or `*args`/`**kwargs` to achieve similar functionality.
   
2. **Run-Time Polymorphism (Method Overriding)**:
   - Occurs when a child class overrides a method inherited from a parent class. This allows objects to behave differently even if they share the same method name.

---

### **Example of Polymorphism in Action:**

#### **1. Polymorphism with Functions**

Polymorphism can be used with functions or built-in types, where the same function can operate on objects of different types.

```python
# Example of polymorphism with functions
def add(a, b):
    return a + b

print(add(5, 3))        # Output: 8 (adding integers)
print(add("Hello, ", "world!"))  # Output: Hello, world! (concatenating strings)
```

- **Explanation**:
  - The `add` function works both with integers and strings. This shows Python’s inherent support for polymorphism, where the `+` operator performs addition or concatenation depending on the data type.

---

#### **2. Polymorphism with Classes and Methods**

Let’s see how polymorphism works with methods in different classes. When two or more classes have methods with the same name, Python can apply polymorphism, depending on the object being used.

##### **Example:**
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action: both objects respond to the same method 'speak'
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
```

- **Explanation**:
  - The `animal_sound()` function can accept both a `Dog` and a `Cat` object. Though both classes have a method named `speak`, their implementation is different, which is an example of **run-time polymorphism**.

---

#### **3. Method Overriding (Run-Time Polymorphism)**

Method overriding is a key part of polymorphism. When a subclass provides a specific implementation of a method that is already defined in its superclass, this is known as **method overriding**. 

##### **Example:**
```python
class Bird:
    def fly(self):
        return "Flies at a certain height."

class Sparrow(Bird):
    def fly(self):  # Overriding the parent class method
        return "Flies at a low altitude."

class Eagle(Bird):
    def fly(self):  # Overriding the parent class method
        return "Flies at a high altitude."

# Polymorphism through method overriding
def flight_test(bird):
    return bird.fly()

sparrow = Sparrow()
eagle = Eagle()

print(flight_test(sparrow))  # Output: Flies at a low altitude.
print(flight_test(eagle))    # Output: Flies at a high altitude.
```

- **Explanation**:
  - The `fly` method is overridden in both `Sparrow` and `Eagle`. When `flight_test()` is called, it invokes the appropriate `fly` method based on the object type passed to it.

---

#### **4. Polymorphism with Inheritance**

Polymorphism often works hand-in-hand with inheritance. The derived class can be used in place of the base class, allowing the same method or operation to be applied to objects of different derived classes.

##### **Example:**
```python
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphism with a common method 'area'
shapes = [Square(4), Circle(7)]

for shape in shapes:
    print(f"Area: {shape.area()}")
# Output:
# Area: 16  (Square)
# Area: 153.86  (Circle)
```

- **Explanation**:
  - Both `Square` and `Circle` are derived from the `Shape` class. Each class has its own version of the `area` method. Polymorphism allows us to call `area()` on both objects, but the behavior differs depending on whether the object is a `Square` or a `Circle`.

---

#### **5. Polymorphism with Abstract Base Classes (ABC)**

An **Abstract Base Class** defines a set of methods that must be created within any child classes built from it. These methods are implemented in the child classes to allow polymorphic behavior.

##### **Example:**
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # This must be implemented by the subclass

# Subclasses providing their own implementation of sound()
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Using polymorphism with abstract classes
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
# Output:
# Woof!
# Meow!
```

- **Explanation**:
  - `Animal` is an abstract base class with an abstract method `sound()`. Both `Dog` and `Cat` classes implement their version of `sound`. By looping through the `animals` list, we can access each animal’s unique sound through polymorphism.

---

### **Key Points to Remember**
1. **Polymorphism** allows objects of different types to be processed using the same interface.
2. **Method Overriding** is a form of polymorphism where child classes provide their own implementation of methods inherited from a parent class.
3. **Python supports polymorphism naturally**, and its dynamic typing system allows flexibility in dealing with multiple types.
4. **Abstract Base Classes** enforce that certain methods must be implemented by derived classes, making the code more structured.

---

### **Summary**
Polymorphism enables a single method to operate on objects of different types, making the code more flexible and easier to extend. Python's support for polymorphism through method overriding, abstract classes, and dynamic typing makes it a highly effective tool for creating reusable and modular code.

---
