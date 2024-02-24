# Imagine you're developing a graphics application that requires calculating the areas
# of different shapes. Currently, you have a base Shape class with an abstract
# get_area method that each concrete shape class (e.g., Circle, Square, Rectangle)
# must implement.

# Question: WAP to design this system to adhere to the Open-Closed Principle (OCP).
# This means you should be able to add new shapes without modifying existing code.
# Name your program o.py.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print("Area is: ")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "square":
            return Square(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "triangle":
            return Triangle(*args)
        else:
            raise ValueError("Unsupported shape type")