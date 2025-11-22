file=open("students.txt","w")
n=int(input("Enter number of students"))

for i in range(n):
    name=input("Enter Name:")
    mobile=input("Enter Mobile:")
    age=input("Enter Age:")
    mail=input("Enter Mail:")
    file.write(f"{name},{mobile},{age},{mail}\n")

file.close()
print("Student details stored successfully!")
