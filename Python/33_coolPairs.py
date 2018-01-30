def coolPairs(a, b):
    uniqueSums = {i + j for i in a for j in b if (i * j) % (i + j) == 0}
    return len(uniqueSums)


print(coolPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == 2)
print(coolPairs([1, 2, 3, 4, 5, 6],  [1, 2, 3, 4, 5, 6]) == 4)
print(coolPairs([2], [2]) == 1)
print(coolPairs([7, 8, 9], [5, 3, 2]) == 0)
