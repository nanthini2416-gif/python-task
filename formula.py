import math
a=int(input("Enter the Square"))
a=a**2
b=int(input("Enter The Breadth"))
l=int(input("Enter The Length"))
r=l*b
h=int(input("Enter The Height"))
r=int(input("Enter The Radius"))
t=1/2*(b*h)
print("The square is:",a)
print("The Rectangle is:",r)
print("The Triangle is:",t)
c=math.pi*r*r
print("The Circle is:",c)
b1=int(input("Enter b1 Value"))
b2=int(input("Enter b2 Value"))
trap=((b1+b2)*h/2)
print("The Trapexoid is:",trap)
