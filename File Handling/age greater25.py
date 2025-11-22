file=open("students.txt","r")
print("Students with age>25:\n")

for line in file:
    
    name,mobile,age,mail=line.strip().split(",")

    if int(age) > 25:
        print(f"Name:{name}, Age:{age}")
file.close()
