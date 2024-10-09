

## **6. Inheritance in Python**

**Inheritance** is a key concept in Object-Oriented Programming (OOP) that allows one class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass). This promotes code reusability and helps in building a hierarchical relationship between classes.

#### **Key Benefits of Inheritance**
1. **Code Reusability**: You can reuse the existing functionality of a class in a new class.
2. **Extensibility**: Subclasses can add new attributes or methods or modify existing ones.
3. **Modularity**: Related classes can be grouped together in a hierarchy, making the code easier to understand and maintain.

---

### **Types of Inheritance in Python**
There are various forms of inheritance:
1. **Single Inheritance**: A subclass inherits from one parent class.
2. **Multiple Inheritance**: A subclass inherits from more than one parent class.
3. **Multilevel Inheritance**: A subclass inherits from another subclass (creating a chain of inheritance).
4. **Hierarchical Inheritance**: Multiple subclasses inherit from a single parent class.
5. **Hybrid Inheritance**: A combination of two or more types of inheritance.

Let's explore each type in detail.

---

### **1. Single Inheritance**

A subclass inherits from a single parent class.

##### **Example:**
```python
# Parent class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name  # Attribute common to all animals

    def speak(self):  # Method common to all animals
        return f"{self.name} makes a sound."

# Child class (Subclass)
class Dog(Animal):
    def bark(self):  # Additional method specific to Dog class
        return f"{self.name} barks: Woof!"

# Creating an object of the subclass
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy makes a sound. (Inherited method)
print(dog.bark())   # Output: Buddy barks: Woof! (Subclass method)
```

- **Explanation**:
  - The `Dog` class inherits from the `Animal` class, so the `speak` method and `name` attribute are available in the `Dog` class.
  - The `Dog` class adds its own method `bark` without modifying the parent class.

---

### **2. Multiple Inheritance**

A class can inherit from more than one parent class, allowing it to access attributes and methods from multiple classes.

##### **Example:**
```python
# Parent class 1
class Mammal:
    def has_fur(self):
        return "Has fur."

# Parent class 2
class Canine:
    def howl(self):
        return "Howls."

# Child class inheriting from both Mammal and Canine
class Wolf(Mammal, Canine):
    def hunt(self):
        return "Hunts in packs."

# Creating an object of the subclass
wolf = Wolf()
print(wolf.has_fur())  # Output: Has fur. (Inherited from Mammal)
print(wolf.howl())     # Output: Howls. (Inherited from Canine)
print(wolf.hunt())     # Output: Hunts in packs. (Method of Wolf class)
```

- **Explanation**:
  - The `Wolf` class inherits from both `Mammal` and `Canine` classes, gaining access to methods from both parent classes.

**Note**: Python resolves method conflicts in multiple inheritance using the **Method Resolution Order (MRO)**, which follows a depth-first, left-to-right approach.

---

### **3. Multilevel Inheritance**

In this type of inheritance, a class inherits from a child class, forming a chain of inheritance.

##### **Example:**
```python
# Parent class (Superclass)
class Vehicle:
    def start_engine(self):
        return "Engine started."

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        return "Car is driving."

# Grandchild class inheriting from Car
class SportsCar(Car):
    def race(self):
        return "Racing at high speed."

# Creating an object of the grandchild class
sports_car = SportsCar()
print(sports_car.start_engine())  # Output: Engine started. (Inherited from Vehicle)
print(sports_car.drive())         # Output: Car is driving. (Inherited from Car)
print(sports_car.race())          # Output: Racing at high speed. (Method of SportsCar)
```

- **Explanation**:
  - `SportsCar` inherits from `Car`, and `Car` inherits from `Vehicle`, creating a chain of inheritance. `SportsCar` can access methods from both `Vehicle` and `Car`.

---

### **4. Hierarchical Inheritance**

In this type, multiple subclasses inherit from a single parent class.

##### **Example:**
```python
# Parent class (Superclass)
class Bird:
    def lay_eggs(self):
        return "Lays eggs."

# Child class 1 inheriting from Bird
class Sparrow(Bird):
    def fly(self):
        return "Flies at low altitude."

# Child class 2 inheriting from Bird
class Eagle(Bird):
    def fly(self):
        return "Flies at high altitude."

# Creating objects of subclasses
sparrow = Sparrow()
eagle = Eagle()

print(sparrow.lay_eggs())  # Output: Lays eggs. (Inherited from Bird)
print(sparrow.fly())       # Output: Flies at low altitude.

print(eagle.lay_eggs())    # Output: Lays eggs. (Inherited from Bird)
print(eagle.fly())         # Output: Flies at high altitude.
```

- **Explanation**:
  - Both `Sparrow` and `Eagle` inherit from the `Bird` class, but each subclass has its own version of the `fly` method.

---

### **5. Hybrid Inheritance**

Hybrid inheritance is a combination of two or more types of inheritance. It typically includes multiple inheritance with either hierarchical or multilevel inheritance.

##### **Example:**
```python
# Parent class
class Engine:
    def engine_info(self):
        return "Engine info."

# Intermediate child class
class Car(Engine):
    def car_info(self):
        return "Car info."

# Another parent class
class MusicSystem:
    def music_info(self):
        return "Music system info."

# Child class inheriting from both Car and MusicSystem
class SportsCar(Car, MusicSystem):
    def sports_car_info(self):
        return "Sports car info."

# Creating an object of the subclass
sports_car = SportsCar()
print(sports_car.engine_info())   # Output: Engine info. (Inherited from Car -> Engine)
print(sports_car.music_info())    # Output: Music system info. (Inherited from MusicSystem)
print(sports_car.sports_car_info())  # Output: Sports car info.
```

- **Explanation**:
  - `SportsCar` inherits from both `Car` (which inherits from `Engine`) and `MusicSystem`. This is a hybrid form of inheritance where different inheritance patterns are combined.

---

### **Overriding Methods in Inheritance**

Subclasses can override methods from the parent class to provide their own specific implementation.

##### **Example:**
```python
class Animal:
    def sound(self):
        return "Some generic sound."

class Cat(Animal):
    def sound(self):  # Overriding the sound method
        return "Meow."

# Creating an object of Cat
cat = Cat()
print(cat.sound())  # Output: Meow (overridden method)
```

- **Explanation**: 
  - The `Cat` class overrides the `sound` method from the `Animal` class to provide a specific sound.

---

### **Using `super()` to Access Parent Class Methods**

You can use the `super()` function to call a method from the parent class inside the child class.

##### **Example:**
```python
class Animal:
    def sound(self):
        return "Some generic sound."

class Dog(Animal):
    def sound(self):  # Overriding the sound method
        original_sound = super().sound()  # Call the parent method using super()
        return original_sound + " Woof!"

# Creating an object of Dog
dog = Dog()
print(dog.sound())  # Output: Some generic sound. Woof!
```

- **Explanation**:
  - The `super()` function calls the parent class's `sound` method in the `Dog` class, then adds "Woof!" to it.

---

### **Summary of Inheritance**
- **Inheritance** allows a class to inherit attributes and methods from another class.
- **Single, multiple, multilevel, hierarchical, and hybrid** inheritance define different inheritance patterns.
- **Method overriding** enables subclasses to provide specific implementations of methods.
- The `super()` function allows access to methods from the parent class in the subclass.

---
### Next Topic : **polymorphism**