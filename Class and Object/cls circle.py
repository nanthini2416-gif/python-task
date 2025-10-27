import math

class circle:

    def area(self,r):
        return math.pi*r*r
    def perimeter(self,r):
        return 2*math.pi*r

c=circle()
r=5
print("Circle Area:",c.area(r))
print("Circle Perimeter:",c.perimeter(r))
