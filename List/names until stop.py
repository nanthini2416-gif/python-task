names = []

while True:
    name = input("Enter a name (or type 'stop' to finish): ")
    if name.lower() == 'stop':
        break
    names.append(name)

print("\nNames entered:")
for n in names:
     print(n)
