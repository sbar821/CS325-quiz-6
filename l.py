# You're developing a 2D geometry drawing application that uses various shapes.
# There are currently base classes for Shape and specific subclasses for Circle,
# Rectangle, and Triangle. Each subclass implements a get_area() method to calculate
# its respective area.
# Question:
# WAP to ensure compliance with the Liskov Substitution Principle (LSP). Consider the
# following challenges and Name your program l.py.:
# Circle and Rectangle have a set_width() and set_height() method, while Triangle
# doesn't. How can you handle this difference without violating LSP?
# The get_area() method implementation varies across shapes. Is this a violation of
# LSP. If so, propose solutions to maintain consistency while accommodating specific
# area calculations.
# Imagine adding a new Polygon shape with multiple sides. How would you integrate it
# into the hierarchy without compromising LSP principles?

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print("Area is: ")

    def set_width(self, width):
        raise NotImplementedError("set_width() method not implemented")

    def set_height(self, height):
        raise NotImplementedError("set_height() method not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius ** 2

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height