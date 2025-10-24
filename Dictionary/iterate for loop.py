my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}


print("Iterating over keys:")
for key in my_dict:
    print(f"{key}")


print("\nIterating over values:")
for value in my_dict.values():
    print(f"{value}")
    

print("\nIterating over key-value pairs:")

for key, value in my_dict.items():
    print(f"{key}: {value}")
