class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Instance method
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object
my_car = Car("Toyota", "Fortuner", 2020)

# Calling the instance method
print(my_car.display_info())
