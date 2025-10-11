num=int(input("Enter The Number of Times"))
f=0
l=1
print(f)
print(l)

for i in range(0,num):
    fibo=f+l
    print(fibo)
    f=l
    l=fibo
