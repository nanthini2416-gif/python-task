file=open("students.txt","r")
print('students whose name starts with "A":\n')

for line in file:
    
    name,mobile,age,mail=line.strip().split(",")
    
    if name.startswith("A"):
        print(f"Name: {name}, Age: {age}")
file.close()
