file=open("students.txt","r")
count=len(file.readlines())
file.close()
print("Total Number of Students:",count)
