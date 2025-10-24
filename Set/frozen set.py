elements = input("Enter elements").split()

frozen = frozenset(elements)

print("\nFrozenset:", frozen)

sample_set = {"apple", "banana", "cherry"}

print("Union with sample set:", frozen.union(sample_set))

print("Intersection with sample set:", frozen.intersection(sample_set))


print("Difference with sample set:", frozen.difference(sample_set))

