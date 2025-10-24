
keys_input = input("Enter keys separated by space: ")
keys = keys_input.split()


default_value = input("Enter the default value: ")


my_dict = dict.fromkeys(keys, default_value)

print("Initialized dictionary:", my_dict)
