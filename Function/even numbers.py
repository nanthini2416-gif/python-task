def even_numbers(*args):
    for num in args:
        if num % 2 == 0:
            print(num)
even_numbers(1, 2, 3, 4, 5, 6)
