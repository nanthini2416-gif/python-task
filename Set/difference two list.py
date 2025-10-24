list1 = input("Enter elements of the first list").split()
list2 = input("Enter elements of the second list").split()

set1 = set(list1)
set2 = set(list2)


dif = set1 - set2

print("Difference (elements in first list but not in second):", list(dif))

