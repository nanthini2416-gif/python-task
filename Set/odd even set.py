input_numbers = input("Enter numbers").split()

num_set = set(map(int, input_numbers))

even_count = sum(1 for num in num_set if num % 2 == 0)
odd_count = len(num_set) - even_count

print(f"\nSet of numbers: {num_set}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
