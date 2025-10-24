set_input = input("Enter elements of a set").split()
user_set = set(set_input)


set_to_dict = dict.fromkeys(user_set)


print("\nOriginal Set:", user_set)
print("Converted Dictionary:", set_to_dict)
