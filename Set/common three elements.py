list1=input("Enter a list1").split()

list2=input("Enter a list2").split()

list3=input("Enter a list3").split()

s1=set(list1)
s2=set(list2)
s3=set(list3)

common=s1&s2&s3

print("common element is",common)
