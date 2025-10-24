list=input("Enter a list").split()

list1=input("Enter a list1").split()

s=set(list)
s1=set(list1)

if s & s1:
    print("The list have atlease one in common")
else:
    print("No common Elements")
    
