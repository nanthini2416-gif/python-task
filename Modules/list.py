def get_list():
    lst=[]
    n=int(input("Enter Number of Elements:"))
    for i in range(n):
        lst.append(int(input(f"Enter Element{i+1}:")))
    return lst

def print_list(lst):
    print("List Elements:", lst)


def count_even(lst):
    #return len([x for x in lst if x%2==0])
    for x in lst:
        if x%2==0:
            return[x]
    
