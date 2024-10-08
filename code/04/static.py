class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @staticmethod
    def is_motor_vehicle():
        return "Cars are motor vehicles."

# Calling the static method
print(Car.is_motor_vehicle())




class fns:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
sum_result = fns.add(5, 10)
product_result = fns.multiply(4, 3)

print(f"Sum: {sum_result}")        # Output: Sum: 15
print(f"Product: {product_result}") # Output: Product: 12




class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

# Checking if strings are palindromes
print(StringUtils.is_palindrome("radar")) 
print(StringUtils.is_palindrome("hello"))  
