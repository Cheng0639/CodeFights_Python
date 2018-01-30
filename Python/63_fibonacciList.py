from functools import reduce


def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x, y: x + [x[-1] + x[-2]], range(n - 2), [0, 1])]


print(fibonacciList(6) == [[],
                           [0],
                           [0],
                           [0, 0],
                           [0, 0, 0],
                           [0, 0, 0, 0, 0]])
print(fibonacciList(2) == [[],
                           [0]])
print(fibonacciList(8) == [[],
                           [0],
                           [0],
                           [0, 0],
                           [0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
