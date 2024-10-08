class Car:
    car_count = 0   # class variable
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.car_count += 1

    @classmethod
    def total_cars(cls):
        return f"Total cars created: {cls.car_count}"

# creating instances
car1 = Car("Toyota", "Fortuner", 2020)
car2 = Car("Audi", "R8", 2021)
car2 = Car("Mercedes", "Benz", 2022)

# Calling the class method
print(Car.total_cars())



class Product:
    discount_rate = 0.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def set_discount(cls, discount):
        cls.discount_rate = discount

    def discounted_price(self):
        return self.price * (1 - self.discount_rate)

# Creating an instance of Product
product1 = Product("Laptop", 1000)

# Setting a new discount rate using the class method
Product.set_discount(0.2) # if i will comment this line, disocunt rate will be : 0.1

print(f"The discounted price of the {product1.name} is ${product1.discounted_price():.2f}.")



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birth_year(cls, name, birthYear):
        current_year = 2024
        age = current_year - birthYear
        return cls(name, age)

# Creating an instance using the class method
person1 = Person.birth_year("Zoro", 2005)

# Displaying the person's information
print(f"{person1.name} is {person1.age} years old.")
