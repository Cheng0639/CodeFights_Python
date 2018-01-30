def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1


print(makeArrayConsecutive2([6, 2, 3, 8]) == 3)
print(makeArrayConsecutive2([0, 3]) == 2)
print(makeArrayConsecutive2([5, 4, 6]) == 0)
print(makeArrayConsecutive2([6, 3]) == 2)
print(makeArrayConsecutive2([1]) == 0)
