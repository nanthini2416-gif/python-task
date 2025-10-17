numbers=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for n in numbers:
    if n%2==0:
     even+=1
    else:
     odd+=1
print("Even Numbers",even)
print("odd Numbers",odd)
