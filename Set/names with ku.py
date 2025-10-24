names_input = input("Enter names").split()

names_set = set(names_input)


count = sum(1 for name in names_set if "ku" in name.lower())


print(f"\nNames in the set: {names_set}")
print(f"Number of names containing 'Ku': {count}")
