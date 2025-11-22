try:
    num=[10,20,30,40,50]
    value=int(input("Enter a value to search:"))
    

    def find_value(num,value):
        if value not in num:
            raise ValueError(f"{value} is not fount in the list")
        else:
            print(f"{value} found in the list")
            
    find_value(num,value)

except ValueError as e:
    print("ERROR", e)
    
