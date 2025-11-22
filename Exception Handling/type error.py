try:
    a=input("Enter the first num")
    b=input("Enter the second num")

    if not (a.replace('.','',1).isdigit() and b.replace('.','',1).isdigit()):
        raise TypeError ("Enter the numberic only")
    print("Sum",float(a)+float(b))

except TypeError as t:
    print("Error",t)
