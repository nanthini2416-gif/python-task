n=int(input("Enter Number"))
total=0
for i in range(1,n+1):
    total+=1/i
    print(f"1/{i}",end=" ")
print(f"\nsum of Harmonic series:{total}")
