### **5. Encapsulation in Python**

- **Encapsulation** is one of the fundamental principles of Object-Oriented Programming (OOP) that restricts direct access to an object's attributes and methods. 
- It helps protect the integrity of the data and hides the internal implementation details from the outside world. 
- Encapsulation is typically achieved through **access modifiers**.

---

### **Access Modifiers in Python**

Python uses naming conventions to indicate the level of access for class attributes and methods:
1. **Public**: Accessible from anywhere (default).
2. **Protected**: Indicated by a single underscore (`_`), accessible within the class and its subclasses.
3. **Private**: Indicated by a double underscore (`__`), accessible only within the class itself.

---

#### **1. Public Attributes and Methods**

By default, all attributes and methods are public, meaning they can be accessed from outside the class.

##### **Example:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

    def display_info(self):  # Public method
        return f"Car: {self.brand} {self.model}"

# Creating a Car object
my_car = Car("Toyota", "Corolla")
print(my_car.display_info())  # Output: Car: Toyota Corolla
```
- In this example, `brand` and `model` are public attributes, and `display_info` is a public method, accessible from outside the class.

---

#### **2. Protected Attributes and Methods**

Protected attributes and methods are intended to be accessed only within the class and by subclasses. They are indicated by a single underscore.

##### **Example:**
```python
class Animal:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _speak(self):  # Protected method
        return f"{self._name} makes a sound."

class Dog(Animal):
    def bark(self):
        return self._speak() + " Woof!"

# Creating a Dog object
my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy makes a sound. Woof!
```
- Here, `_name` and `_speak` are protected attributes and methods. They can be accessed in the `Dog` subclass but should not be accessed directly outside the class hierarchy.

---

#### **3. Private Attributes and Methods**

Private attributes and methods can only be accessed within the class itself. They are indicated by a double underscore.

##### **Example:**
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):  # Public method
        self.__balance += amount  # Modifying private attribute
        print(f"Deposited: ${amount}. New balance: ${self.__balance}")

    def __withdraw(self, amount):  # Private method
        if amount <= self.__balance:
            self.__balance -= amount  # Modifying private attribute
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds")

    def withdraw(self, amount):  # Public method to withdraw
        self.__withdraw(amount)  # Call private method

# Creating a BankAccount object
my_account = BankAccount("12345678", 1000)
my_account.deposit(500)  # Output: Deposited: $500. New balance: $1500
my_account.withdraw(200)  # Output: Withdrew: $200. New balance: $1300

# Attempting to access private attributes or methods will result in an AttributeError
# print(my_account.__balance)  # Raises AttributeError
# my_account.__withdraw(100)   # Raises AttributeError
```
- In this example, `__account_number` and `__balance` are private attributes, and `__withdraw` is a private method. They cannot be accessed directly outside the `BankAccount` class, ensuring data encapsulation.

---

### **Benefits of Encapsulation**

1. **Data Protection**: Encapsulation restricts access to the internal state of an object, preventing accidental modification and ensuring the integrity of the data.
2. **Abstraction**: It hides complex implementation details, allowing users to interact with the object through a simple interface.
3. **Modularity**: Changes to internal implementations can be made without affecting external code that uses the class, promoting maintainability.

---

### **Using Properties for Encapsulation**

Python provides a way to define methods that control access to an attribute using the `@property` decorator. This allows you to create getters and setters, enabling controlled access to private attributes.

##### **Example:**
```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    @property
    def name(self):  # Getter for name
        return self.__name

    @name.setter
    def name(self, new_name):  # Setter for name
        self.__name = new_name

    @property
    def age(self):  # Getter for age
        return self.__age

    @age.setter
    def age(self, new_age):  # Setter for age
        if new_age < 0:
            print("Age cannot be negative.")
        else:
            self.__age = new_age

# Creating a Person object
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice

person1.name = "Bob"  # Using the setter to change name
print(person1.name)  # Output: Bob

person1.age = -5  # Trying to set a negative age
# Output: Age cannot be negative.
print(person1.age)  # Output: 30 (age remains unchanged)
```
- Here, `name` and `age` are private attributes. The `@property` decorator allows controlled access to these attributes through getters and setters, enabling encapsulation while providing a clear interface for interaction.

---

### **Summary of Encapsulation**

- **Encapsulation** is the practice of restricting access to an object's internal data and methods.
- Python uses **public**, **protected**, and **private** access modifiers to control access.
- **Public** attributes and methods can be accessed from anywhere, while **protected** and **private** attributes and methods are restricted to the class and its subclasses or the class itself, respectively.
- Encapsulation protects data integrity and promotes code modularity, and it can be further enhanced using properties for controlled access.

---

### **Next Step: Inheritance**
