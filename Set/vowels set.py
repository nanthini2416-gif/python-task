names_input = input("Enter names").split()

names_set = set(names_input)


vowels = set('aeiouAEIOU')

for name in names_set:
    count = sum(1 for char in name if char in vowels)
    print(f"Name: {name}, Number of vowels: {count}")
