my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

key_to_check = input("Enter the key to check: ")

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does NOT exist in the dictionary.")
