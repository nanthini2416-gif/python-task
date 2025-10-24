set1_input = input("Enter elements of the first set").split()

set2_input = input("Enter elements of the second set").split()


set1 = set(set1_input)
set2 = set(set2_input)

set1.difference_update(set2)

print("\nSet 1 after removing elements present in Set 2:", set1)
