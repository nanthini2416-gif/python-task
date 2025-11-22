try:
    
    a=int(input("Enter a value"))
    b=int(input("Enter a value"))
    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter Only Numbers")

except Exception as e:
    print("Unexcept Error", e)

else:
    print("Division completed")

finally:
    print("End of the program")
    
    
    
    
