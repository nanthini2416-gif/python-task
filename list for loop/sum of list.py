numbers = []

for i in range(5):
    num = float(input(f"Enter number #{i + 1}: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

print("\nThe numbers you entered are:", numbers)
print("The sum of the numbers is:", total)
