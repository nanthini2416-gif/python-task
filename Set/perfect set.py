def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

input_numbers = input("Enter numbers").split()


num_set = set(map(int, input_numbers))


perfect_numbers = [num for num in num_set if is_perfect(num)]

print(f"\nSet of numbers: {num_set}")
print(f"Perfect numbers in the set: {perfect_numbers}")
