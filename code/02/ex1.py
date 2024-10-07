class Car:
    # Class attribute
    number_of_wheels = 4  # All cars have 4 wheels

    def __init__(self, color, model):
        # Instance attributes
        self.color = color  # Each car can have a different color
        self.model = model  # Each car can have a different model

# Creating instances of the Car class { objects }
car1 = Car("red", "Toyota")
car2 = Car("blue", "Honda")

# Accessing instance attributes
print(f"Car 1: Color = {car1.color}, Model = {car1.model}")
print(f"Car 2: Color = {car2.color}, Model = {car2.model}")

# Accessing class attribute
print(f"All cars have {Car.number_of_wheels} wheels.")
