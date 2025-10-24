original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_input = input("Enter keys to extract, separated by space: ")
keys_to_extract = keys_input.split()

new_dict = {}

for key in keys_to_extract:
    if key in original_dict:
        new_dict[key]=original_dict[key]

print("New dictionary:", new_dict)
