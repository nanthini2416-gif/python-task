
try:
    num=input("Enter a value:")
    
    if not num.isdigit():
        raise ValueError("Not a valid value")
    print("you entered:",int(num))

except ValueError as e:
    print("Error occured",e)




   
