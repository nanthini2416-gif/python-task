item=input("Enter item").split()

i=set(item)

print("The set is",i)

remove_item=input("Enter item to remove")

if remove_item in i:
    i.remove(remove_item)
    print(f"remove_item removed")
else:
    print(f"remove_item not removed")

print("The set is",i)
