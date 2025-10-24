def prime(n):
    if n<2:
        return False
    for i in range (2,n+1):
        if n%i==0:
            return False
    return True


def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n

def armstrong(n):
    tot=0
    temp=n
    digit=len(str(n))
    while temp>0:
        digit=temp%10
        tot+=digit*digit
        temp//=10
    return tot==n
