from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x, i: x.rotate(n - i), res, range(n)), 0)
    return [list(d) for d in res]


print(doodledPassword([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5],
                                           [2, 3, 4, 5, 1],
                                           [3, 4, 5, 1, 2],
                                           [4, 5, 1, 2, 3],
                                           [5, 1, 2, 3, 4]])
print(doodledPassword([2, 2, 2, 2]) == [[2, 2, 2, 2],
                                        [2, 2, 2, 2],
                                        [2, 2, 2, 2],
                                        [2, 2, 2, 2]])
print(doodledPassword([9, 8, 7, 5, 4]) == [[9, 8, 7, 5, 4],
                                           [8, 7, 5, 4, 9],
                                           [7, 5, 4, 9, 8],
                                           [5, 4, 9, 8, 7],
                                           [4, 9, 8, 7, 5]])
