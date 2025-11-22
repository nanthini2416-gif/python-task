from abc import ABC, abstractmethod
import math


class Shapes(ABC):
    @abstractmethod
    def volume(self):
        pass



class Cylinder(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius * self.radius * self.height



class Cone(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius * self.radius * self.height


class Sphere(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3



cylinder = Cylinder(3, 5)
print("Cylinder Volume:", cylinder.volume())

cone = Cone(3, 5)
print("Cone Volume:", cone.volume())

sphere = Sphere(3)
print("Sphere Volume:", sphere.volume())
