def find_value(key, **a):
    
    return a.get(key, "Key not found")

value = find_value('color', size='M', color='blue', price=19.99)
print(value)
