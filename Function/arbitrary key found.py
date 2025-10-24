def find(**a):
    key=input("Enter the key find:")
    
    if key in a:
        print(f"Key '{key}' found with value: {a[key]}")
    else:
        print(f"Key '{key}' not found in dictionary")

find(name="Nanthini",age=27,course="python")
        
        
