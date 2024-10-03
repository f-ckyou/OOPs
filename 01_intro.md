
#### **What is OOP**?

- Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **objects**. 
- Rather than focusing on functions and logic (as in procedural programming), OOP organizes the code into reusable blueprints called **classes**, which represent real-world entities or concepts.

OOP revolves around four key principles:
1. **Encapsulation**
2. **Abstraction**
3. **Inheritance**
4. **Polymorphism**

These principles help in building well-structured, modular, and maintainable code.

---

#### **Difference between Procedural and Object-Oriented Programming**

- **Procedural Programming**:
  - Focuses on **procedures or functions**.
  - Data and functions are separate; functions operate on data passed as arguments.
  - Code is written sequentially, and the flow is controlled by function calls.
  - Example languages: C, Pascal.

  Example:
  ```c
  // Procedural programming example in C
  int add(int a, int b) {
      return a + b;
  }

  int main() {
      int result = add(5, 10);
      printf("%d", result); // Output: 15
      return 0;
  }
  ```

- **Object-Oriented Programming**:
  - Focuses on **objects** that combine both data (attributes) and functions (methods).
  - Data is encapsulated within objects, and the methods define the behavior.
  - Instead of writing procedures, you define classes and create objects from them.
  - Example languages: Python, Java, C++.

  Example:
  ```python
  # OOP example in Python
  class Calculator:
      def add(self, a, b):
          return a + b

  calc = Calculator()
  print(calc.add(5, 10))  # Output: 15
  ```

---

#### **Benefits of OOP**

1. **Modularity**: 
   - Code is divided into separate, independent classes, making it easier to manage and maintain.

2. **Reusability**:
   - Classes can be reused in multiple programs, and inheritance allows you to build new classes from existing ones.

3. **Data Hiding (Encapsulation)**:
   - Object data can be kept private to prevent unintended modifications from outside the class.

4. **Code Maintenance**:
   - Changes to an object or class don’t necessarily affect other parts of the code, leading to more maintainable and adaptable codebases.

5. **Problem Solving using Real-World Modeling**:
   - OOP mirrors real-world objects and their interactions, making it intuitive for solving complex problems.

---

### **The Four Pillars of OOP**

#### 1. **Encapsulation**:
   - Encapsulation means binding the data (attributes) and the functions (methods) that manipulate that data into a single unit, called a class.
   - It restricts access to some of the object’s components, which helps in preventing unintended interference and misuse.

   Example:
   ```python
   class BankAccount:
       def __init__(self, balance):
           self.__balance = balance  # Private attribute

       def deposit(self, amount):
           self.__balance += amount

       def get_balance(self):
           return self.__balance

   account = BankAccount(100)
   account.deposit(50)
   print(account.get_balance())  # Output: 150
   ```

#### 2. **Abstraction**:
   - Abstraction focuses on hiding the complex implementation details and exposing only the necessary functionality. This is done using abstract classes or interfaces.
   - The user interacts with an object using a simplified interface without needing to understand the internal workings.

   Example:
   ```python
   from abc import ABC, abstractmethod

   class Animal(ABC):
       @abstractmethod
       def speak(self):
           pass

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   my_dog = Dog()
   print(my_dog.speak())  # Output: Woof!
   ```

#### 3. **Inheritance**:
   - Inheritance allows a class to inherit properties and behaviors (methods) from another class. It enables code reuse and the creation of a class hierarchy.
   - The class that is inherited is called the **parent class**, and the new class is called the **child class**.

   Example:
   ```python
   class Vehicle:
       def __init__(self, make, model):
           self.make = make
           self.model = model

   class Car(Vehicle):
       def car_info(self):
           return f"Car Make: {self.make}, Model: {self.model}"

   my_car = Car("Toyota", "Corolla")
   print(my_car.car_info())  # Output: Car Make: Toyota, Model: Corolla
   ```

#### 4. **Polymorphism**:
   - Polymorphism allows methods to be used interchangeably across different classes. A common example is having different classes implement the same method, but with different behaviors.

   Example:
   ```python
   class Bird:
       def speak(self):
           return "Chirp"

   class Dog:
       def speak(self):
           return "Bark"

   def animal_sound(animal):
       print(animal.speak())

   bird = Bird()
   dog = Dog()
   animal_sound(bird)  # Output: Chirp
   animal_sound(dog)   # Output: Bark
   ```

---

### **Understanding OOP with a Real-World Analogy**

Consider a **car** as an object. The car has:
- **Attributes**: Brand, color, engine type, etc.
- **Methods**: Start, stop, accelerate, brake, etc.

In OOP:
- **Class**: You define a `Car` class that describes what attributes (data) and methods (functions) a car should have.
- **Object**: When you create an actual car, you are creating an object (or instance) of the class `Car`.

By grouping related attributes and behaviors in a class, OOP lets you model real-world entities in code.

---

### **Summary**

Object-Oriented Programming is centered around creating reusable, modular, and structured code by defining **classes** and creating **objects**. OOP promotes better organization, code reusability, and scalability, making it ideal for building complex applications.

### What's Next?
The next step would be diving deeper into the foundation of OOP by learning about **Classes and Objects**.