def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

input_numbers = input("Enter numbers").split()


num_set = set(map(int, input_numbers))


prime_count = sum(1 for num in num_set if is_prime(num))

print(f"\nSet of numbers: {num_set}")
print(f"Number of prime numbers in the set: {prime_count}")
