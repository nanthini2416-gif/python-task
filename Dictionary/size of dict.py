
my_dict = {}


n = int(input("How many key-value pairs do you want to enter? "))


for i in range(n):
    key = input(f"Enter key #{i + 1}: ")
    value = input(f"Enter value for key '{key}': ")
    my_dict[key] = value


size = len(my_dict)
print("Size of the dictionary:", size)
