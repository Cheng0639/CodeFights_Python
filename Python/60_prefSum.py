from itertools import accumulate


def prefSum(a):
    return list(accumulate(a))


print(prefSum([1, 2, 3]) == [1, 3, 6])
print(prefSum([1, 2, 3, -6]) == [1, 3, 6, 0])
print(prefSum([0, 0, 0]) == [0, 0, 0])
