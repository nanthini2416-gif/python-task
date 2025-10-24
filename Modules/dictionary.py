def get_dictionary():
    
    d={}
    n=int(input("Enter number of items:"))
    for i in range(n):
        key=input("Enter a Key:")
        value=int(input("Enter a value:"))
        d[key]=value
    return d

def print_dictionary(d):
    for k, v in d.items():
        print(f"{k} : {v}")


def sum_dictionary(d):
    return sum(d.values())

