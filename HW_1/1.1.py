from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

circle = Circle(3)
rectangle = Rectangle(2, 3)

print(f"Площадь круга: {circle.calculate_area()}")
print(f"Площадь прямоугольника: {rectangle.calculate_area()}")
