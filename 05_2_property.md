In Python, **getters** and **setters** are methods used to access and modify the attributes (variables) of a class, while encapsulating the internal details. They allow controlled access to class attributes, which can help ensure data integrity and validation.

### Getters
A **getter** is a method that retrieves the value of a private or protected attribute. It "gets" the value of an attribute.

### Setters
A **setter** is a method that allows you to set or modify the value of a private or protected attribute. It "sets" the value while providing validation or other processing.

### Why Use Getters and Setters?
- **Encapsulation**: Hide the internal representation of an object from outside the class.
- **Validation**: Before assigning a value (setter) or before retrieving a value (getter), you can implement additional logic, such as data validation or formatting.
- **Flexibility**: You can change the internal representation without affecting the public API.

### Example without Getters and Setters:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.age)  # Direct access to the attribute
person.age = 30     # Direct modification
```

### Example with Getters and Setters:
```python
class Person:
    def __init__(self, name, age):
        self._name = name   # private attributes (by convention, not enforced)
        self._age = age

    # Getter method for age
    @property
    def age(self):
        return self._age

    # Setter method for age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")

person = Person("Alice", 25)
print(person.age)   # Calls getter
person.age = 30     # Calls setter
# person.age = -5   # Would raise ValueError
```

Here, the `@property` decorator turns the `age()` method into a getter, and the `@age.setter` decorator makes `age()` act as a setter. This way, you get the advantage of attribute-like access while retaining the ability to enforce rules (like preventing negative ages).


---- 
----

### The `@property` decorator:
- The `@property` decorator is a Pythonic way to define getters and setters in an elegant manner without directly using method calls like `get_` and `set_`. 
- It allows you to create methods that can be accessed like attributes, while still using logic to control how values are accessed or modified. 
- This makes the interface cleaner, while still providing encapsulation.

### Example 1: Using `@property` for a simple getter
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # We use _radius to indicate that it's "private"
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius

# Usage
c = Circle(10)
print(c.radius)  # Accessing the radius using @property (no parentheses)
```

- **Explanation**: In the above example, `@property` allows us to access the `radius` as if it were a regular attribute, but it's actually controlled by a method. If you need to add validation, this method can do it.

### Example 2: Using `@property` with a setter
To modify the attribute, we can add a setter method using `@<property_name>.setter`:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# Usage
c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 10    # Modifying the radius using the setter
print(c.radius)  # Output: 10
# c.radius = -2   # This will raise ValueError: Radius cannot be negative
```

- **Explanation**: Now the setter method allows controlled modification of the `radius`. If the value is negative, it raises an exception, enforcing a validation rule.

### Example 3: Using both getter and setter for encapsulation
Here’s a more elaborate example that shows how encapsulation works with `@property`, `getter`, and `setter`.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Convert Celsius to Fahrenheit"""
        return (self._celsius * 9/5) + 32

# Usage
temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0 (because 25°C = 77°F)

temp.celsius = 30       # Updating Celsius
print(temp.fahrenheit)  # Output: 86.0

# temp.celsius = -300   # Raises ValueError: Temperature below -273.15°C is not possible
```

- **Explanation**: In this case, `celsius` is a private attribute, and we use both a getter and a setter for it. The `fahrenheit` is a computed property that doesn't need a setter because it's derived from `celsius`. If you update the `celsius`, the `fahrenheit` will automatically reflect the change.

### Example 4: Controlling access with encapsulation

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Private balance attribute
    
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance"""
        if amount < 0:
            raise ValueError("Cannot set a negative balance!")
        self._balance = amount
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient balance!")

# Usage
acc = BankAccount("Alice", 1000)
print(acc.balance)  # Output: 1000

acc.deposit(500)    # Deposit 500
print(acc.balance)  # Output: 1500

acc.withdraw(300)   # Withdraw 300
print(acc.balance)  # Output: 1200

# acc.balance = -200  # Raises ValueError: Cannot set a negative balance!
```

- **Explanation**: The `balance` attribute is private, and it's only accessible or modifiable through the getter and setter. Additionally, the `deposit` and `withdraw` methods provide controlled ways to update the balance without exposing it directly.

### Why Use `@property`, Getters, and Setters?
1. **Encapsulation**: Hide internal details and expose a cleaner interface.
2. **Data Validation**: You can easily validate data before setting or getting attributes.
3. **Read-Only Properties**: You can define a property with only a getter to make it read-only (no setter).
4. **Computed Properties**: Use getters to create properties that are calculated dynamically (like converting Celsius to Fahrenheit).
5. **Maintain Backward Compatibility**: You can start with direct attribute access, then later convert it to a property without changing the interface for the class users.

### Example 5: Read-only property (No setter)
- A read-only property in Python is an attribute of a class that can only be accessed (read) but cannot be modified (written to) from outside the class. 
- This is achieved by defining a getter method (using the @property decorator) without defining a corresponding setter method.
- As a result, the attribute can be read, but any attempt to modify it will raise an error.

### How It Works:
- The `@property` decorator defines a getter method (`radius`) for the attribute `_radius`.
- Since there is no corresponding `@propertyname.setter` method, the property becomes **read-only**. You can retrieve the value, but you can't modify it.

### Benefits:
- **Immutability**: It prevents external modification of the property, ensuring data consistency and protecting sensitive or computed attributes.
- **Controlled Access**: You can control how the attribute is accessed without allowing unintended changes.

If you try to set a read-only property, it will result in an `AttributeError`.

```python
class Square:
    def __init__(self, side_length):
        self._side_length = side_length
    
    @property
    def area(self):
        """Area is a read-only property"""
        return self._side_length ** 2

# Usage
s = Square(5)
print(s.area)  # Output: 25

# s.area = 30  # Raises AttributeError: can't set attribute
```

- **Explanation**: Here, the `area` is computed using the side length of the square, but it's a read-only property because no setter is defined.

### Conclusion:
Using `@property` along with getters and setters in Python allows you to:
- Encapsulate your attributes.
- Add logic when accessing or modifying attributes.
- Maintain clean and intuitive syntax.
- Control access and ensure data integrity without exposing the internal structure of the class directly.

