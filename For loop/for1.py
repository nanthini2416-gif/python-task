sum = 0

print("Numbers divisible by 9 between 100 and 200:")

for i in range(100, 201):
    if i % 9 == 0:
        print(i, end=" ")
        sum += i

print(f"\nSum: {sum}")
