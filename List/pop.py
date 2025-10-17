items = []

count = int(input("How many items do you want to add to the list? "))


for i in range(count):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)

print("\nOriginal list:", items)

if items:
    removed_item = items.pop()
    print(f"\nRemoved last item: {removed_item}")
else:
    print("\nList is empty, nothing to remove.")

print("Updated list:", items)
