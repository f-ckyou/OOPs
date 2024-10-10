# overloading the + operator for complex numbers

class ComplexNumbers:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        # Since the result of adding two complex numbers is also a complex number, we need to return the result as an object of the ComplexNumbers class
        #  we ensure that the result maintains the same data structure, 
        return ComplexNumbers(self.real + other.real, self.img + other.img)

    # string representation
    def __str__(self):
        return f"{self.real} + {self.img}i"

a = ComplexNumbers(1, 2)
b = ComplexNumbers(0, 4)
print(a+b)



# overloading the * operator for vectors

class Vectors:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vectors(2,2)
v2 = Vectors(3,3)
print(v1*v2)



# overloading the - operator for time

class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __sub__(self, other):
        m_s = self.h * 60 + self.m
        m_o = other.h * 60 + other.m
        d_m = m_s - m_o
        h = d_m // 60
        m = d_m % 60
        return Time(h, m)

    def __str__(self):
        return f"{self.h}h {self.m}m"

t1 = Time(6, 45)
t2 = Time(4, 37)
print(t1-t2)


# overloading the == operator for fractions

import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Testing
f1 = Fraction(2, 3)
f2 = Fraction(4, 6)
print(f1 == f2)  
