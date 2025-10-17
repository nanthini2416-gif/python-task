user_input = input("Enter items separated by commas: ")

items = [item.strip() for item in user_input.split(",")]


item_to_remove = input("Enter the item to remove: ").strip()


if item_to_remove in items:
    
    items.remove(item_to_remove)
    print("Updated list:", items)
else:
    print(f"'{item_to_remove}' not found in the list.")
