set1_input = input("Enter elements of the first set").split()
set2_input = input("Enter elements of the second set").split()


set1 = set(set1_input)
set2 = set(set2_input)


sym_diff = set1 ^ set2



print("\nSet 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", sym_diff)
