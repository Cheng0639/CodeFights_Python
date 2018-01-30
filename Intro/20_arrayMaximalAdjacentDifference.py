def arrayMaximalAdjacentDifference(a):
    return max([abs(a[i] - a[i + 1]) for i in range(len(a) - 1)])


print(arrayMaximalAdjacentDifference([2, 4, 1, 0]) == 3)
print(arrayMaximalAdjacentDifference([1, 1, 1, 1]) == 0)
print(arrayMaximalAdjacentDifference([-1, 4, 10, 3, -2]) == 7)
