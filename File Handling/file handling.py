file=open("sample.txt","w")
file.write("Welcome to File Handling in Python\n")
file.close()

file=open("sample.txt","r")
content=file.read()
print("File Content:\n",content)
file.close()
