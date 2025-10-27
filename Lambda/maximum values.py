from functools import reduce


numbers = [10, 25, 7, 92, 56]


def compare(a, b):
    if a > b:
        return a
    else:
        return b


max_value = reduce(lambda a, b: compare(a, b), numbers)


print("Maximum value is:", max_value)
