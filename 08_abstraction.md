### **Abstraction in OOP**

- **Abstraction** is one of the four pillars of Object-Oriented Programming (OOP) along with Encapsulation, Inheritance, and Polymorphism. 
- Abstraction focuses on **hiding the complexity** of the internal implementation and only exposing the essential details to the user.
- It helps in reducing code complexity and increases reusability.

In Python, abstraction can be implemented using:
1. **Abstract Classes**
2. **Abstract Methods**

- Abstract classes in Python are created using the `ABC` (Abstract Base Class) module from the `abc` library. 
- These classes cannot be instantiated directly and are used as blueprints for other classes. 
- An abstract method is a method that is declared but contains no implementation. - Subclasses inheriting the abstract class must implement the abstract methods.

### **Key Concepts**
- **Abstract Class:** A class that contains one or more abstract methods.
- **Abstract Method:** A method declared in an abstract class but must be implemented by subclasses.
- **Cannot be Instantiated:** You cannot create an object of an abstract class directly.

### **How to Define Abstraction in Python**

To implement abstraction:
1. Import the `ABC` class and `abstractmethod` decorator from the `abc` module.
2. Define an abstract class that inherits from `ABC`.
3. Define one or more abstract methods inside the abstract class.
4. Any class inheriting the abstract class must provide implementations for all the abstract methods.

### **Example: Basic Abstraction**

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):  
    # Abstract method
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Subclass of Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the abstract method
    def area(self):
        return self.width * self.height

    # Implementing the abstract method
    def perimeter(self):
        return 2 * (self.width + self.height)

# Subclass of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract method
    def area(self):
        return 3.14 * self.radius * self.radius

    # Implementing the abstract method
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of the subclasses
rect = Rectangle(5, 10)
circle = Circle(7)

# Calling the methods
print(f"Rectangle Area: {rect.area()}")           # Output: 50
print(f"Rectangle Perimeter: {rect.perimeter()}") # Output: 30
print(f"Circle Area: {circle.area()}")            # Output: 153.86
print(f"Circle Perimeter: {circle.perimeter()}")  # Output: 43.96
```

### **Explanation:**
- **Shape class**: This is the abstract class that contains two abstract methods `area()` and `perimeter()`. It serves as a blueprint for any subclass that derives from it.
- **Rectangle and Circle classes**: These are concrete subclasses that inherit from `Shape`. They are required to implement the `area` and `perimeter` methods because these methods are abstract in the base class.

### **Key Points:**
1. **Abstract Class**: `Shape` cannot be instantiated. You cannot do `shape = Shape()`.
2. **Concrete Classes**: `Rectangle` and `Circle` provide implementations for the abstract methods (`area` and `perimeter`).
3. **Reusability**: Other shapes (like `Square`, `Triangle`, etc.) can be implemented similarly by inheriting from `Shape`.

### **Benefits of Abstraction:**
- **Code Maintenance**: You can change the internal implementation without affecting other parts of the program.
- **Reduced Complexity**: Abstraction hides unnecessary details from the user and shows only the essential information.
- **Encourages Reusability**: Common features can be defined in the abstract class, while specific features can be defined in subclasses.
- **Enforcing a Common Interface**: By creating an abstract class (`Shape`) with abstract methods (`area()` and `perimeter()`), you're defining a contract that all subclasses must follow. This guarantees that any class that inherits from `Shape` will have implementations of `area()` and `perimeter()`.

---

### **Exercise: Implement Abstraction**

Create an abstract class `Animal` with the following abstract methods:
- `sound()`: Represents the sound the animal makes.
- `move()`: Represents how the animal moves.

Then, create two subclasses `Dog` and `Bird` that inherit from `Animal`. Implement the `sound` and `move` methods for each class.

```python
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Subclass for Dog
class Dog(Animal):
    def sound(self):
        return "Barks"

    def move(self):
        return "Runs"

# Subclass for Bird
class Bird(Animal):
    def sound(self):
        return "Chirps"

    def move(self):
        return "Flies"

# Creating instances of the subclasses
dog = Dog()
bird = Bird()

# Test the methods
print(f"Dog Sound: {dog.sound()}")    # Output: Barks
print(f"Dog Move: {dog.move()}")      # Output: Runs
print(f"Bird Sound: {bird.sound()}")  # Output: Chirps
print(f"Bird Move: {bird.move()}")    # Output: Flies
```

#### **Task:**
- Create an abstract class `Animal` with the `sound` and `move` methods.
- Create the `Dog` and `Bird` classes that inherit from `Animal` and implement their respective behaviors.

---
<br>
<br>

## Difference btw Abstraction and Encapsulation

**Abstraction** and **Encapsulation** are both fundamental concepts in Object-Oriented Programming (OOP), but they serve different purposes. Here's a detailed comparison to understand their differences:

---

### **1. Purpose**

- **Abstraction**:
  - **What it does**: Hides the complexity of the system by exposing only the necessary and relevant parts of the object.
  - **Why it's used**: To simplify the interaction with objects by focusing on the essential details, without needing to understand the intricate internal workings.
  - **Example**: When using a car, you don't need to know how the engine works internally; you just need to know how to drive it (steering, pedals, etc.). Abstraction hides the complex mechanics of the car and exposes only the user-friendly interface.

- **Encapsulation**:
  - **What it does**: Bundles data (attributes) and methods (functions) that operate on the data into a single unit or class, while restricting direct access to some of the object's components.
  - **Why it's used**: To protect the internal state of an object and ensure controlled access/modification to its data.
  - **Example**: In a car, the engine is encapsulated. The user can't directly interact with it but can control it via the accelerator and other controls. It protects the internal mechanism from being manipulated directly and accidentally.

---

### **2. How They Work**

- **Abstraction**:
  - Achieved using **abstract classes** and **interfaces**. These provide a high-level description of the object and hide the underlying details.
  - Example:
    ```python
    from abc import ABC, abstractmethod

    class Car(ABC):
        @abstractmethod
        def drive(self):
            pass

    class Sedan(Car):
        def drive(self):
            print("Driving a Sedan")
    ```
    Here, `Car` is an abstract class. The user doesn't need to know how `drive()` is implemented. They only need to call `drive()` on the subclass (like `Sedan`).

- **Encapsulation**:
  - Achieved using **access modifiers** (e.g., private, protected, public in other languages). In Python, encapsulation is implemented using single underscores `_` or double underscores `__` to indicate restricted access.
  - Example:
    ```python
    class BankAccount:
        def __init__(self, balance):
            self.__balance = balance  # Encapsulated (private) attribute

        def deposit(self, amount):
            self.__balance += amount

        def withdraw(self, amount):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds")

        def get_balance(self):
            return self.__balance  # Controlled access via a method
    ```
    Here, the `__balance` is a private variable that cannot be accessed directly from outside the class. It can only be modified or accessed through methods like `deposit`, `withdraw`, and `get_balance`.

---

### **3. Focus**

- **Abstraction**:
  - Focuses on **hiding complexity** and showing only the essential details to the outside world.
  - Abstraction deals with **design**.
  
- **Encapsulation**:
  - Focuses on **data protection** by controlling how data is accessed and modified.
  - Encapsulation deals with **implementation**.

---

### **4. Example Scenario**

#### **Real-World Example (ATM Machine)**:
- **Abstraction**: 
  - When you use an ATM, you are only concerned with the simple operations like inserting your card, entering your PIN, and withdrawing money. The internal workings of how the machine communicates with the bank's server and processes transactions are hidden from you.
  
- **Encapsulation**:
  - Your bank account details, such as your balance or transaction history, are encapsulated inside the banking system. The system controls how and when this data can be accessed, ensuring that sensitive information is not exposed or tampered with directly.

#### **Code Example**:
```python
# Abstraction: Abstract class defines an abstract method withdraw()
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

# Encapsulation: Hides sensitive details of BankAccount (like balance)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Encapsulated balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn: {amount}, Remaining balance: {self.__balance}"
        else:
            return "Insufficient funds"

# Subclass of ATM implementing the abstract method
class UserATM(ATM):
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def withdraw(self, amount):
        return self.bank_account.withdraw(amount)

# Usage
account = BankAccount(1000)  # Encapsulation of balance
atm = UserATM(account)       # Abstraction via ATM
print(atm.withdraw(500))     # Withdraw money, Output: Withdrawn: 500, Remaining balance: 500
```
Here:
- **Abstraction**: The `ATM` class defines a `withdraw()` method that is implemented by `UserATM`. The user doesn't care how the withdrawal is processed internally.
- **Encapsulation**: The `__balance` attribute in `BankAccount` is private and can only be accessed or modified via methods, protecting its integrity.

---

### **5. Differences Summary**

| **Feature**          | **Abstraction**                                   | **Encapsulation**                                  |
|----------------------|---------------------------------------------------|---------------------------------------------------|
| **Focus**            | Hiding complexity                                 | Data protection and controlled access             |
| **Deals With**       | Design and interface                              | Data and implementation                           |
| **Implementation**   | Abstract classes and methods                      | Access modifiers (e.g., private, protected)       |
| **Example**          | ATM showing simple operations, hiding internal work| Bank account balance hidden, accessed via methods |
| **Goal**             | Simplify interaction                              | Control over data access and modification         |
| **Access**           | Not concerned with access control                 | Concerned with controlling how data is accessed   |

---

Both concepts work together to create more secure and maintainable code. **Abstraction** hides the complexity, while **encapsulation** protects and controls access to sensitive data.