def remove_last_key(**a):
    
    a.pop(list(a)[-1])
    print(a)
    
remove_last_key(x=10, y=20, z=30)
