a=float(input("Enter First Side"))
b=float(input("Enter Second Side"))
c=float(input("Enter Third Side"))
if a==b==c:
    print("Equal Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
