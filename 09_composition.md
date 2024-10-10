### **Composition vs. Inheritance in OOP**

Both **composition** and **inheritance** are ways to establish relationships between classes in Object-Oriented Programming (OOP). However, they serve different purposes and are used in different scenarios. Let's explore both in detail:

---

### **1. Inheritance**

**Inheritance** is a mechanism in which a new class (called a subclass or child class) derives properties and behaviors from an existing class (called a superclass or parent class). It promotes **code reuse** and creates a **"is-a" relationship** between the parent and child classes.

#### **Key Points about Inheritance:**
- It supports **hierarchical classification**.
- The child class can **override** methods of the parent class to provide specific behavior.
- Inheritance creates a **tight coupling** between parent and child classes because changes to the parent class affect all subclasses.
- **When to use**: When there is a clear **"is-a" relationship** (e.g., a `Dog` **is a** `Animal`).

#### **Example: Inheritance**
```python
# Parent class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class (Subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Child class (Subclass)
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Usage
dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Rex barks
print(cat.speak())  # Output: Whiskers meows
```

Here:
- `Dog` and `Cat` are subclasses of `Animal`. They inherit the `name` attribute from `Animal` and **override** the `speak` method to provide their own behavior.
- This is an **"is-a" relationship**: A `Dog` **is a** `Animal`.

---

### **2. Composition**

**Composition** is a design principle in which one class contains an object of another class as an attribute, meaning it models a **"has-a" relationship** between classes. Instead of inheriting, a class includes an instance of another class to use its functionality.

#### **Key Points about Composition:**
- It supports **modular design** by delegating responsibilities to different classes.
- Composition allows for **flexibility** as the contained objects can easily be swapped or replaced.
- Composition creates **looser coupling** than inheritance, making the system more maintainable and adaptable.
- **When to use**: When there is a **"has-a" relationship** (e.g., a `Car` **has an** `Engine`).

#### **Example: Composition**
```python
# Class representing Engine
class Engine:
    def start(self):
        return "Engine is starting"

# Class representing Car
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        return self.engine.start()

# Usage
engine = Engine()
car = Car(engine)
print(car.start())  # Output: Engine is starting
```

Here:
- `Car` **has an** `Engine`. The `Car` class contains an instance of `Engine` and uses its functionality by delegation.
- This is a **"has-a" relationship**, where a `Car` **has an** `Engine`.

---

### **3. Composition vs. Inheritance**

| **Feature**             | **Composition**                             | **Inheritance**                               |
|-------------------------|---------------------------------------------|-----------------------------------------------|
| **Relationship**         | "Has-a" relationship                        | "Is-a" relationship                           |
| **Coupling**             | Looser coupling, more flexible              | Tighter coupling, less flexible               |
| **Code Reuse**           | Achieved by using existing classes as components | Achieved by inheriting methods and properties |
| **Design Flexibility**   | More flexible, components can be swapped    | Less flexible, child class is tightly tied to parent |
| **Maintainability**      | Easier to maintain due to loose coupling    | Harder to maintain as changes affect subclasses |
| **When to Use**          | When you want to build classes with components | When there is a clear "is-a" relationship     |
| **Reusability**          | High: Easily reuse components in other classes | Moderate: Subclasses reuse functionality      |

---

### **4. Key Differences**

- **In a "has-a" relationship (composition)**, the classes are independent. If one class changes, it has minimal impact on the other.
- **In an "is-a" relationship (inheritance)**, the child class is dependent on the parent class. Any change in the parent class affects the child class.
  
#### **Example: When to Use Inheritance or Composition**
- **Inheritance** is appropriate when one class is a **type** of another class. For example, a `Bird` is an `Animal`, so you use inheritance.
- **Composition** is appropriate when one class **contains** another. For example, a `Car` contains an `Engine`, so you use composition.

---

### **5. Advantages of Composition over Inheritance**

1. **Flexibility**: In composition, you can change the behavior of a class by composing it with different objects without modifying its source code. For example, if you want a `Car` to use a different `Engine`, you can pass a new `Engine` object without changing the `Car` class.
2. **Avoids Inheritance Chain Issues**: Inheritance can lead to complex and fragile inheritance chains, especially if multiple layers are involved. Composition avoids this problem by keeping the relationship simpler.
3. **Easier to Test and Maintain**: Classes that use composition are easier to test and maintain because they are modular and loosely coupled.
4. **Better Encapsulation**: Composition promotes better encapsulation since the contained objects are generally not exposed outside of the class that contains them, thus protecting the internal workings of the class.

---

### **6. Code Comparison**

#### **Inheritance Example**
```python
# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working"

# Child class (inherits Employee)
class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team"

# Usage
manager = Manager("John", 5000)
print(manager.work())  # Output: John is managing the team
```

#### **Composition Example**
```python
# Class representing Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working"

# Class representing Manager that uses Employee
class Manager:
    def __init__(self, employee):
        self.employee = employee  # Composition: Manager has an Employee

    def work(self):
        return f"{self.employee.name} is managing the team"

# Usage
employee = Employee("John", 5000)
manager = Manager(employee)
print(manager.work())  # Output: John is managing the team
```

---

### **Conclusion**
- **Inheritance** is great when there's a clear **"is-a" relationship**, and you want to extend the behavior of a class by creating subclasses. However, it can create tightly coupled, harder-to-maintain systems.
- **Composition** is a better choice when there's a **"has-a" relationship** and you want a flexible, modular, and loosely coupled system. Composition is often preferred over inheritance when flexibility and reusability are the primary concerns.

Each technique has its use case, and understanding when to use each is key to good OOP design.