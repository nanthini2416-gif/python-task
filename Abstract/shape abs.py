from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius



class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c



circle = Circle(5)
print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())

triangle = Triangle(3, 4, 5)
print("\nTriangle Area:", triangle.calculate_area())
print("Triangle Perimeter:", triangle.calculate_perimeter())
