
s_input = input("Enter elements of a set").split()
s = set(s_input)


converted_tuple = tuple(s)

print("\nOriginal Set:",s)
print("Converted to Tuple:", converted_tuple)


tup= input("\nEnter elements of a tuple").split()
user_tup = tuple(tup)

convert_set= set(user_tup)

print("\nOriginal Tuple:", user_tup)
print("Converted to Set:", convert_set)
