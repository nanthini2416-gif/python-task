def add_numbers():
    try:
        a=int(input("Enter a number"))
        b=int(input("Enter b number"))
        
        print(a+b)
    

    except ValueError:
        print("Enter Only Numbers")

    except Exception as e:
        print("Unexcept Error", e)

    else:
        print("Division completed")

    finally:
        print("End of the program")

add_numbers()
