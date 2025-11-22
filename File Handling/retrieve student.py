file=open("students.txt","r")
print("students details\n")

for line in file:
   data=line.strip().split(",")
   print("Name:",data[0])
   print("mobile:",data[1])
   print("Age:",data[2])
   print("Mail:",data[3])

file.close()
